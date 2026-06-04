from __future__ import annotations

import argparse
import csv
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    def tqdm(iterable, **kwargs):  # type: ignore[no-redef]
        del kwargs
        return iterable

from .io_utils import RAW_MODEL_OUTPUTS_DIR, TABLES_DIR, append_jsonl
from .model_client import make_client
from .prompts import (
    DEFAULT_PROMPT_TEMPLATE,
    available_prompt_templates,
    build_classification_prompt,
    parse_label,
)
from .tasks import (
    Example,
    default_pool_path,
    default_processed_path,
    get_task,
    load_processed_examples,
)


DEFAULT_PROVIDER = "openai"
DEFAULT_MODEL = "gpt-5.4-mini"
DEFAULT_K_SHOT = 16
DEFAULT_N_TEST = 50
DEFAULT_DEMO_SAMPLING_MODE = "resample_per_test"
DEFAULT_TEMPERATURE = 0.0
DEFAULT_REASONING_EFFORT = "none"
DEFAULT_REQUEST_DELAY_SECONDS = 0.25
DEFAULT_DATA_FORMAT = "auto"
DEFAULT_LABEL_ASSIGNMENT = "random_per_seed"
DEFAULT_PROMPT_TEMPLATE_NAME = DEFAULT_PROMPT_TEMPLATE
LABEL_ASSIGNMENT_SEED_OFFSET = 50_000


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run few-shot classification for one task.")
    parser.add_argument("--task", default="sst2_positive_sentiment")
    parser.add_argument("--data-file", type=Path, default=None)
    parser.add_argument(
        "--eval-data-file",
        type=Path,
        default=None,
        help=(
            "Optional separate processed JSONL file for final inputs. "
            "Demonstrations are sampled from --data-file and evaluation rows "
            "from this file."
        ),
    )
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
        "--prompt-template",
        choices=available_prompt_templates(),
        default=DEFAULT_PROMPT_TEMPLATE_NAME,
        help="Named prompt template from src/prompts.py.",
    )
    parser.add_argument("--provider", choices=("openai", "mock"), default=DEFAULT_PROVIDER)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--k", type=int, default=DEFAULT_K_SHOT)
    parser.add_argument("--n-test", type=int, default=DEFAULT_N_TEST)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--demo-sampling-mode",
        choices=("fixed_per_seed", "resample_per_test"),
        default=DEFAULT_DEMO_SAMPLING_MODE,
        help=(
            "fixed_per_seed uses one demonstration set for all test calls in a seed; "
            "resample_per_test draws a fresh balanced demonstration set for each test call."
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
    parser.add_argument("--summary-output", type=Path, default=None)
    parser.add_argument(
        "--request-delay-seconds",
        type=float,
        default=DEFAULT_REQUEST_DELAY_SECONDS,
        help="Optional sleep after each model call, useful for avoiding rate limits.",
    )
    return parser.parse_args()


def default_data_path(task_id: str, seed: int, requested_format: str) -> Path:
    if requested_format == "split":
        return default_processed_path(task_id, seed)
    return default_pool_path(task_id, seed)


def detect_data_format(examples: list[Example], requested_format: str) -> str:
    splits = {example.split for example in examples}
    if requested_format != "auto":
        data_format = requested_format
    elif "pool" in splits:
        data_format = "pool"
    else:
        data_format = "split"

    if data_format == "pool" and "pool" not in splits:
        raise ValueError("Requested pool data, but the data file has no split='pool' rows.")
    if data_format == "split" and not {"fewshot_pool", "test"}.issubset(splits):
        raise ValueError(
            "Requested split data, but the data file does not contain both "
            "split='fewshot_pool' and split='test' rows."
        )
    return data_format


def sample_balanced_from_examples(
    examples: list[Example],
    n: int,
    seed: int,
    *,
    excluded_example_ids: set[str] | None = None,
    context: str = "examples",
) -> list[Example]:
    rng = random.Random(seed)
    excluded_example_ids = excluded_example_ids or set()
    available_examples = [
        example for example in examples if example.example_id not in excluded_example_ids
    ]
    by_label = {
        "A": [example for example in available_examples if example.label == "A"],
        "B": [example for example in available_examples if example.label == "B"],
    }
    per_label = n // 2
    requested_by_label = {"A": per_label, "B": per_label}
    if n % 2:
        requested_by_label[rng.choice(["A", "B"])] += 1

    sampled: list[Example] = []
    for label, label_examples in by_label.items():
        requested = requested_by_label[label]
        if len(label_examples) < requested:
            raise ValueError(
                f"Not enough {label} examples in {context}: "
                f"need {requested}, have {len(label_examples)}"
            )
        rng.shuffle(label_examples)
        sampled.extend(label_examples[:requested])
    rng.shuffle(sampled)
    return sampled


def sample_balanced_from_split(
    examples: list[Example],
    split: str,
    n: int,
    seed: int,
) -> list[Example]:
    split_examples = [example for example in examples if example.split == split]
    return sample_balanced_from_examples(split_examples, n, seed, context=f"split {split!r}")


def make_label_assignment(
    mode: str,
    seed: int,
) -> tuple[dict[str, str], bool, int | None]:
    if mode == "canonical":
        return {"A": "A", "B": "B"}, False, None
    if mode == "swapped":
        return {"A": "B", "B": "A"}, True, None
    if mode == "random_per_seed":
        label_assignment_seed = seed + LABEL_ASSIGNMENT_SEED_OFFSET
        label_swap = random.Random(label_assignment_seed).choice([False, True])
        if label_swap:
            return {"A": "B", "B": "A"}, True, label_assignment_seed
        return {"A": "A", "B": "B"}, False, label_assignment_seed
    raise ValueError(f"Unknown label assignment mode {mode!r}.")


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    n_test = len(rows)
    correct = sum(1 for row in rows if row["correct"])
    nonparseable = sum(1 for row in rows if row["parsed_label"] is None)
    first = rows[0]
    return {
        "task_id": first["task_id"],
        "k": first["k_shot"],
        "seed": first["seed"],
        "n_test": n_test,
        "accuracy": correct / n_test if n_test else 0.0,
        "nonparseable_rate": nonparseable / n_test if n_test else 0.0,
        "data_format": first.get("data_format"),
        "data_file": first.get("data_file"),
        "eval_data_format": first.get("eval_data_format"),
        "eval_data_file": first.get("eval_data_file"),
        "eval_task_id": first.get("eval_task_id"),
        "label_assignment_mode": first.get("label_assignment_mode"),
        "label_swap": first.get("label_swap"),
        "label_map": first.get("label_map"),
        "prompt_template": first.get("prompt_template"),
        "cue_accuracy": (
            sum(1 for row in rows if row.get("cue_correct")) / n_test
            if rows and first.get("cue_label") is not None
            else None
        ),
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
                "n_test",
                "accuracy",
                "nonparseable_rate",
                "data_format",
                "data_file",
                "eval_data_format",
                "eval_data_file",
                "eval_task_id",
                "label_assignment_mode",
                "label_swap",
                "label_map",
                "prompt_template",
                "cue_accuracy",
            ],
        )
        writer.writeheader()
        writer.writerow(row)


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
    eval_data_file = args.eval_data_file or data_file
    if not eval_data_file.exists():
        raise FileNotFoundError(f"Evaluation data file not found: {eval_data_file}.")
    eval_examples = (
        examples if eval_data_file == data_file else load_processed_examples(eval_data_file)
    )
    eval_data_format = detect_data_format(eval_examples, args.data_format)
    test_sampling_seed = args.seed + 10_000
    test_sampling_mode = (
        "balanced_from_pool"
        if eval_data_format == "pool"
        else "balanced_from_test_split"
    )

    if eval_data_format == "pool":
        eval_pool_examples = [
            example for example in eval_examples if example.split == "pool"
        ]
        test_examples = sample_balanced_from_examples(
            eval_pool_examples,
            args.n_test,
            test_sampling_seed,
            context="evaluation pool sample",
        )
    else:
        test_examples = sample_balanced_from_split(
            eval_examples,
            "test",
            args.n_test,
            test_sampling_seed,
        )

    if data_format == "pool":
        pool_examples = [example for example in examples if example.split == "pool"]
    else:
        pool_examples = []

    label_map, label_swap, label_assignment_seed = make_label_assignment(
        args.label_assignment,
        args.seed,
    )

    run_id = args.run_id or (
        f"{task.task_id}_k{args.k}_seed{args.seed}_"
        f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    )
    output_path = args.output or RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl"
    summary_path = args.summary_output or TABLES_DIR / f"{run_id}_summary.csv"
    client = make_client(args.provider, args.model)

    result_rows: list[dict[str, object]] = []
    if output_path.exists():
        os.remove(output_path)

    fixed_demonstrations: list[Example] | None = None
    if args.demo_sampling_mode == "fixed_per_seed":
        if data_format == "pool":
            fixed_demonstrations = sample_balanced_from_examples(
                pool_examples,
                args.k,
                args.seed,
                excluded_example_ids={example.example_id for example in test_examples},
                context="pool fixed demonstrations",
            )
        else:
            fixed_demonstrations = sample_balanced_from_split(
                examples,
                "fewshot_pool",
                args.k,
                args.seed,
            )

    for test_idx, test_example in enumerate(
        tqdm(test_examples, desc=f"{task.task_id} seed={args.seed}")
    ):
        if fixed_demonstrations is not None:
            demonstrations = fixed_demonstrations
            demo_seed = args.seed
        else:
            demo_seed = args.seed * 1_000_000 + test_idx
            if data_format == "pool":
                demonstrations = sample_balanced_from_examples(
                    pool_examples,
                    args.k,
                    demo_seed,
                    excluded_example_ids={test_example.example_id},
                    context="pool demonstrations",
                )
            else:
                demonstrations = sample_balanced_from_split(
                    examples,
                    "fewshot_pool",
                    args.k,
                    demo_seed,
                )

        prompt_true_label = label_map[test_example.label]
        cue_canonical_label = test_example.metadata.get(
            "cue_canonical_label",
            test_example.metadata.get("spacing_cue_canonical_label"),
        )
        cue_label = (
            label_map[str(cue_canonical_label)]
            if cue_canonical_label in {"A", "B"}
            else None
        )
        prompt = build_classification_prompt(
            demonstrations,
            test_example.input,
            label_map=label_map,
            prompt_template=args.prompt_template,
        )
        raw_output = client.complete(
            prompt,
            temperature=args.temperature,
            reasoning_effort=args.reasoning_effort,
        )
        parsed_label = parse_label(raw_output)
        result_rows.append(
            {
                "run_id": run_id,
                "task_id": task.task_id,
                "model": args.model,
                "provider": args.provider,
                "k_shot": args.k,
                "seed": args.seed,
                "data_format": data_format,
                "data_file": str(data_file),
                "eval_data_format": eval_data_format,
                "eval_data_file": str(eval_data_file),
                "eval_task_id": test_example.task_id,
                "test_sampling_mode": test_sampling_mode,
                "test_sampling_seed": test_sampling_seed,
                "label_assignment_mode": args.label_assignment,
                "label_assignment_seed": label_assignment_seed,
                "label_swap": label_swap,
                "label_map": label_map,
                "demo_sampling_mode": args.demo_sampling_mode,
                "prompt_template": args.prompt_template,
                "demo_seed": demo_seed,
                "demo_example_ids": [example.example_id for example in demonstrations],
                "temperature": args.temperature,
                "reasoning_effort": args.reasoning_effort,
                "test_example_id": test_example.example_id,
                "prompt": prompt,
                "raw_output": raw_output,
                "parsed_label": parsed_label,
                "canonical_true_label": test_example.label,
                "true_label": prompt_true_label,
                "correct": parsed_label == prompt_true_label,
                "cue_canonical_label": cue_canonical_label,
                "cue_label": cue_label,
                "cue_correct": (
                    parsed_label == cue_label if cue_label is not None else None
                ),
            }
        )
        append_jsonl(output_path, [result_rows[-1]])
        if args.request_delay_seconds > 0:
            time.sleep(args.request_delay_seconds)

    summary_row = summarize(result_rows)
    write_summary_csv(summary_path, summary_row)

    print(f"Wrote raw model outputs to {output_path}")
    print(f"Wrote summary to {summary_path}")
    print(summary_row)


if __name__ == "__main__":
    main()
