from __future__ import annotations

import argparse
import csv
import os
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    def tqdm(iterable, **kwargs):  # type: ignore[no-redef]
        del kwargs
        return iterable

from .io_utils import ARTICULATED_RULES_DIR, RAW_MODEL_OUTPUTS_DIR, TABLES_DIR, append_jsonl
from .model_client import make_client
from .prompts import (
    DEFAULT_ARTICULATION_PROMPT_TEMPLATE,
    available_articulation_prompt_templates,
    build_articulation_prompt,
)
from .run_classification import (
    DEFAULT_DATA_FORMAT,
    DEFAULT_DEMO_SAMPLING_MODE,
    DEFAULT_K_SHOT,
    DEFAULT_LABEL_ASSIGNMENT,
    DEFAULT_MODEL,
    DEFAULT_N_TEST,
    DEFAULT_PROVIDER,
    DEFAULT_REASONING_EFFORT,
    DEFAULT_REQUEST_DELAY_SECONDS,
    DEFAULT_TEMPERATURE,
    default_data_path,
    detect_data_format,
    make_label_assignment,
    sample_balanced_from_examples,
    sample_balanced_from_split,
)
from .tasks import Example, get_task, load_processed_examples


DEFAULT_ARTICULATION_PROMPT_TEMPLATE_NAME = DEFAULT_ARTICULATION_PROMPT_TEMPLATE


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run few-shot rule articulation for one task."
    )
    parser.add_argument("--task", default="sst2_positive_sentiment")
    parser.add_argument("--data-file", type=Path, default=None)
    parser.add_argument(
        "--data-format",
        choices=("auto", "pool", "split"),
        default=DEFAULT_DATA_FORMAT,
        help="auto uses the default pool file; split supports legacy fewshot/dev/test files.",
    )
    parser.add_argument(
        "--label-assignment",
        choices=("random_per_seed", "canonical", "swapped"),
        default=DEFAULT_LABEL_ASSIGNMENT,
        help=(
            "How canonical task labels are shown in prompts. random_per_seed "
            "deterministically randomizes whether canonical labels are swapped."
        ),
    )
    parser.add_argument(
        "--articulation-prompt-template",
        "--prompt-template",
        dest="articulation_prompt_template",
        choices=available_articulation_prompt_templates(),
        default=DEFAULT_ARTICULATION_PROMPT_TEMPLATE_NAME,
        help="Named articulation prompt template from src/prompts.py.",
    )
    parser.add_argument("--provider", choices=("openai", "mock"), default=DEFAULT_PROVIDER)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--k", type=int, default=DEFAULT_K_SHOT)
    parser.add_argument(
        "--n-samples",
        "--n-test",
        dest="n_test",
        type=int,
        default=DEFAULT_N_TEST,
        help="Number of independent articulation samples to run.",
    )
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--demo-sampling-mode",
        choices=("fixed_per_seed", "resample_per_test"),
        default=DEFAULT_DEMO_SAMPLING_MODE,
        help=(
            "fixed_per_seed uses one demonstration set for all samples in a seed; "
            "resample_per_test draws a fresh balanced demonstration set for each sample."
        ),
    )
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    parser.add_argument(
        "--reasoning-effort",
        choices=("none", "minimal", "low", "medium", "high", "xhigh"),
        default=DEFAULT_REASONING_EFFORT,
        help="Optional Responses API reasoning.effort value; use 'none' for non-reasoning GPT-5.x runs.",
    )
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--rules-output", type=Path, default=None)
    parser.add_argument("--summary-output", type=Path, default=None)
    parser.add_argument(
        "--request-delay-seconds",
        type=float,
        default=DEFAULT_REQUEST_DELAY_SECONDS,
        help="Optional sleep after each model call, useful for avoiding rate limits.",
    )
    return parser.parse_args()


def canonical_rule_condition(rule_text: str) -> str:
    rule_text = " ".join(rule_text.strip().split())
    prefix = "Label A iff "
    if rule_text.startswith(prefix):
        condition = rule_text[len(prefix):]
    else:
        condition = f"the canonical Label A condition holds ({rule_text})"
    condition = condition.rstrip(".")
    condition = condition.removesuffix("; otherwise label B")
    condition = condition.removesuffix("; otherwise Label B")
    return condition


def prompt_facing_rule_text(canonical_rule_text: str, label_map: dict[str, str]) -> str:
    positive_prompt_label = label_map["A"]
    negative_prompt_label = label_map["B"]
    condition = canonical_rule_condition(canonical_rule_text)
    return (
        f"Label {positive_prompt_label} iff {condition}; "
        f"Label {negative_prompt_label} otherwise."
    )


def normalize_articulated_rule(raw_output: str) -> str:
    cleaned = " ".join(raw_output.strip().split())
    return cleaned or "<empty output>"


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    first = rows[0]
    return {
        "task_id": first["task_id"],
        "k": first["k_shot"],
        "seed": first["seed"],
        "n_samples": len(rows),
        "data_format": first.get("data_format"),
        "data_file": first.get("data_file"),
        "label_assignment_mode": first.get("label_assignment_mode"),
        "label_swap": first.get("label_swap"),
        "label_map": first.get("label_map"),
        "articulation_prompt_template": first.get("articulation_prompt_template"),
        "rules_output": first.get("rules_output"),
    }


def write_summary_csv(path: Path, row: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "task_id",
                "k",
                "seed",
                "n_samples",
                "data_format",
                "data_file",
                "label_assignment_mode",
                "label_swap",
                "label_map",
                "articulation_prompt_template",
                "rules_output",
            ],
        )
        writer.writeheader()
        writer.writerow(row)


def write_rules_file(
    path: Path,
    *,
    task_id: str,
    run_id: str,
    canonical_rule_text: str,
    prompt_rule_text: str,
    label_map: dict[str, str],
    rows: list[dict[str, object]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(f"# Articulated Rules: {task_id}\n\n")
        f.write(f"Run ID: `{run_id}`\n\n")
        f.write(f"Correct canonical rule: {canonical_rule_text}\n\n")
        f.write(
            "Prompt label map: "
            f"canonical A -> {label_map['A']}; canonical B -> {label_map['B']}.\n\n"
        )
        f.write(f"Correct prompt-facing rule: {prompt_rule_text}\n\n")
        f.write("## Model-Articulated Rules\n\n")
        for idx, row in enumerate(rows, start=1):
            f.write(f"{idx}. {row['articulated_rule']}\n")


def select_sampled_examples(
    examples: list[Example],
    *,
    data_format: str,
    n_samples: int,
    seed: int,
) -> tuple[list[Example], list[Example], str, int]:
    sampling_seed = seed + 10_000
    sampling_mode = (
        "balanced_from_pool" if data_format == "pool" else "balanced_from_test_split"
    )
    if data_format == "pool":
        pool_examples = [example for example in examples if example.split == "pool"]
        sampled_examples = sample_balanced_from_examples(
            pool_examples,
            n_samples,
            sampling_seed,
            context="pool articulation sample",
        )
        return sampled_examples, pool_examples, sampling_mode, sampling_seed

    sampled_examples = sample_balanced_from_split(
        examples,
        "test",
        n_samples,
        sampling_seed,
    )
    return sampled_examples, [], sampling_mode, sampling_seed


def main() -> None:
    args = parse_args()
    task = get_task(args.task)
    data_file = args.data_file or default_data_path(
        task.task_id,
        args.seed,
        args.data_format,
    )
    if not data_file.exists():
        raise FileNotFoundError(
            f"Data file not found: {data_file}. Prepare it with "
            f"`python -m src.prepare_data --task {task.task_id} --seed {args.seed}`."
        )
    examples = load_processed_examples(data_file)
    data_format = detect_data_format(examples, args.data_format)
    sampled_examples, pool_examples, sampling_mode, sampling_seed = select_sampled_examples(
        examples,
        data_format=data_format,
        n_samples=args.n_test,
        seed=args.seed,
    )

    label_map, label_swap, label_assignment_seed = make_label_assignment(
        args.label_assignment,
        args.seed,
    )
    prompt_rule_text = prompt_facing_rule_text(task.rule_text, label_map)

    run_id = args.run_id or (
        f"{task.task_id}_articulate_k{args.k}_seed{args.seed}_"
        f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    )
    output_path = args.output or RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl"
    rules_path = args.rules_output or ARTICULATED_RULES_DIR / f"{run_id}_rules.md"
    summary_path = args.summary_output or TABLES_DIR / f"{run_id}_summary.csv"
    client = make_client(args.provider, args.model)

    result_rows: list[dict[str, object]] = []
    for path in (output_path, rules_path):
        if path.exists():
            os.remove(path)

    fixed_demonstrations: list[Example] | None = None
    if args.demo_sampling_mode == "fixed_per_seed":
        if data_format == "pool":
            fixed_demonstrations = sample_balanced_from_examples(
                pool_examples,
                args.k,
                args.seed,
                excluded_example_ids={example.example_id for example in sampled_examples},
                context="pool fixed articulation demonstrations",
            )
        else:
            fixed_demonstrations = sample_balanced_from_split(
                examples,
                "fewshot_pool",
                args.k,
                args.seed,
            )

    for sample_idx, heldout_example in enumerate(
        tqdm(sampled_examples, desc=f"{task.task_id} articulation seed={args.seed}")
    ):
        if fixed_demonstrations is not None:
            demonstrations = fixed_demonstrations
            demo_seed = args.seed
        else:
            demo_seed = args.seed * 1_000_000 + sample_idx
            if data_format == "pool":
                demonstrations = sample_balanced_from_examples(
                    pool_examples,
                    args.k,
                    demo_seed,
                    excluded_example_ids={heldout_example.example_id},
                    context="pool articulation demonstrations",
                )
            else:
                demonstrations = sample_balanced_from_split(
                    examples,
                    "fewshot_pool",
                    args.k,
                    demo_seed,
                )

        prompt = build_articulation_prompt(
            demonstrations,
            label_map=label_map,
            prompt_template=args.articulation_prompt_template,
        )
        raw_output = client.complete(
            prompt,
            temperature=args.temperature,
            reasoning_effort=args.reasoning_effort,
        )
        row = {
            "run_id": run_id,
            "task_id": task.task_id,
            "model": args.model,
            "provider": args.provider,
            "k_shot": args.k,
            "seed": args.seed,
            "data_format": data_format,
            "data_file": str(data_file),
            "sample_sampling_mode": sampling_mode,
            "sample_sampling_seed": sampling_seed,
            "label_assignment_mode": args.label_assignment,
            "label_assignment_seed": label_assignment_seed,
            "label_swap": label_swap,
            "label_map": label_map,
            "demo_sampling_mode": args.demo_sampling_mode,
            "articulation_prompt_template": args.articulation_prompt_template,
            "demo_seed": demo_seed,
            "demo_example_ids": [example.example_id for example in demonstrations],
            "temperature": args.temperature,
            "reasoning_effort": args.reasoning_effort,
            "heldout_example_id": heldout_example.example_id,
            "heldout_input": heldout_example.input,
            "heldout_canonical_label": heldout_example.label,
            "heldout_prompt_label": label_map[heldout_example.label],
            "canonical_rule_text": task.rule_text,
            "prompt_rule_text": prompt_rule_text,
            "rules_output": str(rules_path),
            "prompt": prompt,
            "raw_output": raw_output,
            "articulated_rule": normalize_articulated_rule(raw_output),
        }
        result_rows.append(row)
        append_jsonl(output_path, [row])
        if args.request_delay_seconds > 0:
            time.sleep(args.request_delay_seconds)

    write_rules_file(
        rules_path,
        task_id=task.task_id,
        run_id=run_id,
        canonical_rule_text=task.rule_text,
        prompt_rule_text=prompt_rule_text,
        label_map=label_map,
        rows=result_rows,
    )
    summary_row = summarize(result_rows)
    write_summary_csv(summary_path, summary_row)

    print(f"Wrote raw model outputs to {output_path}")
    print(f"Wrote articulated rules to {rules_path}")
    print(f"Wrote summary to {summary_path}")
    print(summary_row)


if __name__ == "__main__":
    main()
