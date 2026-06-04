from __future__ import annotations

import argparse
import csv
import os
import random
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    def tqdm(iterable, **kwargs):  # type: ignore[no-redef]
        del kwargs
        return iterable

from .io_utils import (
    RAW_MODEL_OUTPUTS_DIR,
    RULE_WORKFLOW_REPORTS_DIR,
    TABLES_DIR,
    append_jsonl,
)
from .model_client import make_client
from .prompts import (
    DEFAULT_ARTICULATION_PROMPT_TEMPLATE,
    DEFAULT_RULE_APPLICATION_PROMPT_TEMPLATE,
    available_articulation_prompt_templates,
    available_rule_application_prompt_templates,
    build_articulation_prompt,
    build_rule_application_prompt,
    parse_label,
)
from .run_articulation import (
    normalize_articulated_rule,
    prompt_facing_rule_text,
    select_sampled_examples,
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


DEFAULT_RULE_EVAL_EXAMPLES = 5
RULE_EVAL_SEED_OFFSET = 80_000


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run the full rule-articulation workflow: infer a rule from examples, "
            "then evaluate that rule on fresh held-out examples."
        )
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
        choices=available_articulation_prompt_templates(),
        default=DEFAULT_ARTICULATION_PROMPT_TEMPLATE,
        help="Named articulation prompt template from src/prompts.py.",
    )
    parser.add_argument(
        "--rule-application-prompt-template",
        choices=available_rule_application_prompt_templates(),
        default=DEFAULT_RULE_APPLICATION_PROMPT_TEMPLATE,
        help="Named rule-application prompt template from src/prompts.py.",
    )
    parser.add_argument("--provider", choices=("openai", "mock"), default=DEFAULT_PROVIDER)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument(
        "--application-provider",
        choices=("openai", "mock"),
        default=None,
        help="Provider for rule-application calls; defaults to --provider.",
    )
    parser.add_argument(
        "--application-model",
        default=None,
        help="Model for rule-application calls; defaults to --model.",
    )
    parser.add_argument("--k", type=int, default=DEFAULT_K_SHOT)
    parser.add_argument(
        "--n-samples",
        "--n-test",
        dest="n_samples",
        type=int,
        default=DEFAULT_N_TEST,
        help="Number of independent articulated rules to generate.",
    )
    parser.add_argument(
        "--rule-eval-examples",
        type=int,
        default=DEFAULT_RULE_EVAL_EXAMPLES,
        help="Number of fresh held-out examples used to evaluate each articulated rule.",
    )
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--demo-sampling-mode",
        choices=("fixed_per_seed", "resample_per_test"),
        default=DEFAULT_DEMO_SAMPLING_MODE,
        help=(
            "fixed_per_seed uses one demonstration set for all articulated rules; "
            "resample_per_test draws a fresh balanced demonstration set for each rule."
        ),
    )
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    parser.add_argument(
        "--application-temperature",
        type=float,
        default=None,
        help="Temperature for rule-application calls; defaults to --temperature.",
    )
    parser.add_argument(
        "--reasoning-effort",
        choices=("none", "minimal", "low", "medium", "high", "xhigh"),
        default=DEFAULT_REASONING_EFFORT,
        help="Reasoning effort for articulation calls.",
    )
    parser.add_argument(
        "--application-reasoning-effort",
        choices=("none", "minimal", "low", "medium", "high", "xhigh"),
        default=None,
        help="Reasoning effort for rule-application calls; defaults to --reasoning-effort.",
    )
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--summary-output", type=Path, default=None)
    parser.add_argument("--markdown-output", type=Path, default=None)
    parser.add_argument(
        "--request-delay-seconds",
        type=float,
        default=DEFAULT_REQUEST_DELAY_SECONDS,
        help="Optional sleep after each model call, useful for avoiding rate limits.",
    )
    return parser.parse_args()


def sample_uniform_eval_examples(
    candidates: list[Example],
    n: int,
    seed: int,
    *,
    excluded_example_ids: set[str],
) -> list[Example]:
    available = [
        example for example in candidates if example.example_id not in excluded_example_ids
    ]
    if len(available) < n:
        raise ValueError(
            "Not enough evaluation examples after excluding demonstration rows: "
            f"need {n}, have {len(available)}."
        )
    rng = random.Random(seed)
    return rng.sample(available, n)


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    n_eval = len(rows)
    correct = sum(1 for row in rows if row["correct"])
    nonparseable = sum(1 for row in rows if row["parsed_label"] is None)
    by_rule: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_rule[int(row["rule_index"])].append(row)
    rule_scores = [
        sum(1 for row in rule_rows if row["correct"]) / len(rule_rows)
        for rule_rows in by_rule.values()
    ]
    first = rows[0]
    return {
        "task_id": first["task_id"],
        "run_id": first["run_id"],
        "articulation_model": first["articulation_model"],
        "articulation_provider": first["articulation_provider"],
        "application_model": first["application_model"],
        "application_provider": first["application_provider"],
        "k": first["k_shot"],
        "seed": first["seed"],
        "n_articulated_rules": len(by_rule),
        "rule_eval_examples": first["rule_eval_examples"],
        "total_rule_application_calls": n_eval,
        "accuracy": correct / n_eval if n_eval else 0.0,
        "nonparseable_rate": nonparseable / n_eval if n_eval else 0.0,
        "mean_rule_accuracy": sum(rule_scores) / len(rule_scores) if rule_scores else 0.0,
        "rules_all_correct": sum(1 for score in rule_scores if score == 1.0),
        "rules_any_correct": sum(1 for score in rule_scores if score > 0.0),
        "data_format": first.get("data_format"),
        "data_file": first.get("data_file"),
        "label_assignment_mode": first.get("label_assignment_mode"),
        "label_swap": first.get("label_swap"),
        "label_map": first.get("label_map"),
        "articulation_prompt_template": first.get("articulation_prompt_template"),
        "rule_application_prompt_template": first.get(
            "rule_application_prompt_template"
        ),
    }


def write_summary_csv(path: Path, row: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "task_id",
                "run_id",
                "articulation_model",
                "articulation_provider",
                "application_model",
                "application_provider",
                "k",
                "seed",
                "n_articulated_rules",
                "rule_eval_examples",
                "total_rule_application_calls",
                "accuracy",
                "nonparseable_rate",
                "mean_rule_accuracy",
                "rules_all_correct",
                "rules_any_correct",
                "data_format",
                "data_file",
                "label_assignment_mode",
                "label_swap",
                "label_map",
                "articulation_prompt_template",
                "rule_application_prompt_template",
            ],
        )
        writer.writeheader()
        writer.writerow(row)


def markdown_cell(text: object) -> str:
    return str(text).replace("\n", " ").replace("|", "\\|")


def write_markdown_report(
    path: Path,
    *,
    summary_row: dict[str, object],
    prompt_rule_text: str,
    rows: list[dict[str, object]],
) -> None:
    by_rule: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_rule[int(row["rule_index"])].append(row)

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(f"# Rule Articulation Workflow: {summary_row['task_id']}\n\n")
        f.write(f"Run ID: `{summary_row['run_id']}`\n\n")
        f.write(f"Correct prompt-facing rule: {prompt_rule_text}\n\n")
        f.write("## Summary\n\n")
        f.write(f"- Articulated rules: {summary_row['n_articulated_rules']}\n")
        f.write(f"- Evaluation examples per rule: {summary_row['rule_eval_examples']}\n")
        f.write(
            "- Total rule-application calls: "
            f"{summary_row['total_rule_application_calls']}\n"
        )
        f.write(f"- Rule-application accuracy: {summary_row['accuracy']:.3f}\n")
        f.write(
            f"- Nonparseable rate: {summary_row['nonparseable_rate']:.3f}\n"
        )
        f.write(f"- Mean per-rule accuracy: {summary_row['mean_rule_accuracy']:.3f}\n")
        f.write(f"- Rules with all evals correct: {summary_row['rules_all_correct']}\n")
        f.write(f"- Rules with any eval correct: {summary_row['rules_any_correct']}\n\n")
        f.write("## Settings\n\n")
        f.write(f"- Articulation model: `{summary_row['articulation_model']}`\n")
        f.write(f"- Rule-application model: `{summary_row['application_model']}`\n")
        f.write(f"- k-shot examples per articulated rule: `{summary_row['k']}`\n")
        f.write(f"- Seed: `{summary_row['seed']}`\n")
        f.write(
            "- Articulation prompt template: "
            f"`{summary_row['articulation_prompt_template']}`\n"
        )
        f.write(
            "- Rule-application prompt template: "
            f"`{summary_row['rule_application_prompt_template']}`\n"
        )
        f.write(
            "- Label assignment: "
            f"`{summary_row['label_assignment_mode']}`, swap="
            f"`{summary_row['label_swap']}`\n\n"
        )
        f.write("## Rule-Level Results\n\n")
        f.write("| Rule | Rule Accuracy | Articulated Rule |\n")
        f.write("|---:|---:|---|\n")
        for rule_index in sorted(by_rule):
            rule_rows = by_rule[rule_index]
            correct = sum(1 for row in rule_rows if row["correct"])
            total = len(rule_rows)
            rule_text = rule_rows[0]["articulated_rule"]
            f.write(
                f"| {rule_index} | {correct}/{total} | "
                f"{markdown_cell(rule_text)} |\n"
            )

        f.write("\n## Detailed Evaluations\n\n")
        for rule_index in sorted(by_rule):
            rule_rows = by_rule[rule_index]
            correct = sum(1 for row in rule_rows if row["correct"])
            total = len(rule_rows)
            f.write(f"### Rule {rule_index}: {correct}/{total}\n\n")
            f.write(f"Articulated rule: {rule_rows[0]['articulated_rule']}\n\n")
            f.write("| Eval | Example ID | Input | True | Predicted | Correct |\n")
            f.write("|---:|---|---|:---:|:---:|:---:|\n")
            for row in rule_rows:
                correct_mark = "yes" if row["correct"] else "no"
                predicted = row["parsed_label"] if row["parsed_label"] is not None else ""
                f.write(
                    f"| {row['rule_eval_index']} | "
                    f"{markdown_cell(row['eval_example_id'])} | "
                    f"{markdown_cell(row['eval_input'])} | "
                    f"{markdown_cell(row['eval_true_label'])} | "
                    f"{markdown_cell(predicted)} | {correct_mark} |\n"
                )
            f.write("\n")


def main() -> None:
    args = parse_args()
    if args.n_samples < 1:
        raise ValueError("--n-samples must be positive.")
    if args.rule_eval_examples < 1:
        raise ValueError("--rule-eval-examples must be positive.")

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
        n_samples=args.n_samples,
        seed=args.seed,
    )
    eval_candidates = (
        [example for example in examples if example.split == "pool"]
        if data_format == "pool"
        else list(examples)
    )

    label_map, label_swap, label_assignment_seed = make_label_assignment(
        args.label_assignment,
        args.seed,
    )
    prompt_rule_text = prompt_facing_rule_text(task.rule_text, label_map)

    application_provider = args.application_provider or args.provider
    application_model = args.application_model or args.model
    application_temperature = (
        args.temperature
        if args.application_temperature is None
        else args.application_temperature
    )
    application_reasoning_effort = (
        args.reasoning_effort
        if args.application_reasoning_effort is None
        else args.application_reasoning_effort
    )

    run_id = args.run_id or (
        f"{task.task_id}_articulation_workflow_k{args.k}_seed{args.seed}_"
        f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    )
    output_path = args.output or RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl"
    summary_path = args.summary_output or TABLES_DIR / f"{run_id}_summary.csv"
    markdown_path = (
        args.markdown_output or RULE_WORKFLOW_REPORTS_DIR / f"{run_id}_report.md"
    )
    articulation_client = make_client(args.provider, args.model)
    application_client = make_client(application_provider, application_model)

    for path in (output_path, markdown_path):
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
                context="pool fixed articulation workflow demonstrations",
            )
        else:
            fixed_demonstrations = sample_balanced_from_split(
                examples,
                "fewshot_pool",
                args.k,
                args.seed,
            )

    result_rows: list[dict[str, object]] = []
    for rule_index, anchor_example in enumerate(
        tqdm(sampled_examples, desc=f"{task.task_id} articulation workflow"),
        start=1,
    ):
        sample_idx = rule_index - 1
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
                    excluded_example_ids={anchor_example.example_id},
                    context="pool articulation workflow demonstrations",
                )
            else:
                demonstrations = sample_balanced_from_split(
                    examples,
                    "fewshot_pool",
                    args.k,
                    demo_seed,
                )

        articulation_prompt = build_articulation_prompt(
            demonstrations,
            label_map=label_map,
            prompt_template=args.articulation_prompt_template,
        )
        articulation_raw_output = articulation_client.complete(
            articulation_prompt,
            temperature=args.temperature,
            reasoning_effort=args.reasoning_effort,
        )
        articulated_rule = normalize_articulated_rule(articulation_raw_output)
        if args.request_delay_seconds > 0:
            time.sleep(args.request_delay_seconds)

        demo_example_ids = {example.example_id for example in demonstrations}
        eval_seed = (
            args.seed * 10_000_000
            + sample_idx * 10_000
            + RULE_EVAL_SEED_OFFSET
        )
        eval_examples = sample_uniform_eval_examples(
            eval_candidates,
            args.rule_eval_examples,
            eval_seed,
            excluded_example_ids=demo_example_ids,
        )

        for rule_eval_index, eval_example in enumerate(eval_examples, start=1):
            eval_true_label = label_map[eval_example.label]
            application_prompt = build_rule_application_prompt(
                articulated_rule,
                eval_example.input,
                prompt_template=args.rule_application_prompt_template,
            )
            application_raw_output = application_client.complete(
                application_prompt,
                temperature=application_temperature,
                reasoning_effort=application_reasoning_effort,
            )
            parsed_label = parse_label(application_raw_output)
            row = {
                "run_id": run_id,
                "task_id": task.task_id,
                "seed": args.seed,
                "data_format": data_format,
                "data_file": str(data_file),
                "articulation_sample_sampling_mode": sampling_mode,
                "articulation_sample_sampling_seed": sampling_seed,
                "label_assignment_mode": args.label_assignment,
                "label_assignment_seed": label_assignment_seed,
                "label_swap": label_swap,
                "label_map": label_map,
                "k_shot": args.k,
                "rule_eval_examples": args.rule_eval_examples,
                "rule_eval_seed": eval_seed,
                "demo_sampling_mode": args.demo_sampling_mode,
                "demo_seed": demo_seed,
                "demo_example_ids": sorted(demo_example_ids),
                "articulation_provider": args.provider,
                "articulation_model": args.model,
                "articulation_temperature": args.temperature,
                "articulation_reasoning_effort": args.reasoning_effort,
                "articulation_prompt_template": args.articulation_prompt_template,
                "articulation_anchor_example_id": anchor_example.example_id,
                "articulation_anchor_input": anchor_example.input,
                "articulation_anchor_canonical_label": anchor_example.label,
                "articulation_anchor_prompt_label": label_map[anchor_example.label],
                "articulation_prompt": articulation_prompt,
                "articulation_raw_output": articulation_raw_output,
                "articulated_rule": articulated_rule,
                "canonical_rule_text": task.rule_text,
                "prompt_rule_text": prompt_rule_text,
                "rule_index": rule_index,
                "rule_eval_index": rule_eval_index,
                "application_provider": application_provider,
                "application_model": application_model,
                "application_temperature": application_temperature,
                "application_reasoning_effort": application_reasoning_effort,
                "rule_application_prompt_template": (
                    args.rule_application_prompt_template
                ),
                "eval_example_id": eval_example.example_id,
                "eval_input": eval_example.input,
                "eval_canonical_label": eval_example.label,
                "eval_true_label": eval_true_label,
                "application_prompt": application_prompt,
                "application_raw_output": application_raw_output,
                "parsed_label": parsed_label,
                "correct": parsed_label == eval_true_label,
            }
            result_rows.append(row)
            append_jsonl(output_path, [row])
            if args.request_delay_seconds > 0:
                time.sleep(args.request_delay_seconds)

    summary_row = summarize(result_rows)
    write_summary_csv(summary_path, summary_row)
    write_markdown_report(
        markdown_path,
        summary_row=summary_row,
        prompt_rule_text=prompt_rule_text,
        rows=result_rows,
    )

    print(f"Wrote workflow outputs to {output_path}")
    print(f"Wrote summary to {summary_path}")
    print(f"Wrote markdown report to {markdown_path}")
    print(summary_row)


if __name__ == "__main__":
    main()
