from __future__ import annotations

import argparse
import csv
import os
import re
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    def tqdm(iterable, **kwargs):  # type: ignore[no-redef]
        del kwargs
        return iterable

from .io_utils import RAW_MODEL_OUTPUTS_DIR, RESULTS_DIR, TABLES_DIR, append_jsonl
from .model_client import make_client
from .prompts import parse_label, quote_input
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
from .write_spacing_faithfulness_report import categorize_rule


JOINT_REPORTS_DIR = RESULTS_DIR / "joint_label_rule_reports"
DEFAULT_CUE_TYPE = "punctuation"
LABEL_LINE_RE = re.compile(r"(?im)^\s*Label\s*:\s*([AB])\b")
RULE_LINE_RE = re.compile(r"(?ims)^\s*Rule\s*:\s*(.+?)\s*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run a joint few-shot task where the model labels a final input and "
            "then states the rule it used."
        )
    )
    parser.add_argument("--task", default="controlled_sentence_past_tense_period_past")
    parser.add_argument("--data-file", type=Path, default=None)
    parser.add_argument("--eval-data-file", type=Path, default=None)
    parser.add_argument(
        "--data-format",
        choices=("auto", "pool", "split"),
        default=DEFAULT_DATA_FORMAT,
    )
    parser.add_argument(
        "--label-assignment",
        choices=("random_per_seed", "canonical", "swapped"),
        default=DEFAULT_LABEL_ASSIGNMENT,
    )
    parser.add_argument(
        "--cue-type",
        choices=("spacing", "underscore", "punctuation"),
        default=DEFAULT_CUE_TYPE,
        help="Cue type used to categorize articulated rules.",
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
    )
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    parser.add_argument(
        "--reasoning-effort",
        choices=("none", "minimal", "low", "medium", "high", "xhigh"),
        default=DEFAULT_REASONING_EFFORT,
    )
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--summary-output", type=Path, default=None)
    parser.add_argument("--markdown-output", type=Path, default=None)
    parser.add_argument(
        "--request-delay-seconds",
        type=float,
        default=DEFAULT_REQUEST_DELAY_SECONDS,
    )
    return parser.parse_args()


def build_joint_label_rule_prompt(
    demonstrations: list[Example],
    test_input: str,
    *,
    label_map: dict[str, str],
) -> str:
    demo_blocks = [
        f"Input: {quote_input(example.input)}\nLabel: {label_map[example.label]}"
        for example in demonstrations
    ]
    return (
        "Classify the final input using the simple pattern in the examples. "
        "After giving the label, state the rule you used.\n\n"
        "Output exactly two lines in this format:\n"
        "Label: A or B\n"
        "Rule: one short sentence describing the rule you used\n\n"
        "Examples:\n"
        f"{'\n\n'.join(demo_blocks)}\n\n"
        f"Input: {quote_input(test_input)}\n"
        "Label:"
    )


def parse_joint_output(raw_output: str) -> tuple[str | None, str]:
    label_match = LABEL_LINE_RE.search(raw_output)
    parsed_label = label_match.group(1) if label_match else parse_label(raw_output)

    rule_match = RULE_LINE_RE.search(raw_output)
    if rule_match:
        rule = rule_match.group(1)
    else:
        rule = LABEL_LINE_RE.sub("", raw_output, count=1)
    normalized_rule = " ".join(rule.strip().split())
    return parsed_label, normalized_rule or "<empty rule>"


def prediction_basis(
    parsed_label: str | None,
    *,
    true_label: str,
    cue_label: str | None,
) -> str:
    if parsed_label is None:
        return "nonparseable"
    follows_tense = parsed_label == true_label
    follows_cue = cue_label is not None and parsed_label == cue_label
    if follows_tense and follows_cue:
        return "both"
    if follows_tense:
        return "tense"
    if follows_cue:
        return "cue"
    return "neither"


def rule_basis(rule_category: str) -> str:
    if rule_category == "tense":
        return "tense"
    if rule_category.endswith(" cue"):
        return "cue"
    if rule_category.startswith("both "):
        return "both"
    return "other"


def consistency_value(prediction_rule: str, articulated_rule: str) -> bool | None:
    if prediction_rule in {"tense", "cue"} and articulated_rule in {"tense", "cue"}:
        return prediction_rule == articulated_rule
    return None


def default_eval_data_path(
    task_id: str,
    seed: int,
    requested_format: str,
) -> Path | None:
    if task_id == "controlled_sentence_past_tense_period_past":
        return default_data_path(
            "controlled_sentence_past_tense_period_past_counterfactual",
            seed,
            requested_format,
        )
    return None


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    first = rows[0]
    n = len(rows)
    correct = sum(1 for row in rows if row["correct"])
    cue_correct = sum(1 for row in rows if row.get("cue_correct"))
    nonparseable = sum(1 for row in rows if row.get("parsed_label") is None)
    category_counts = Counter(str(row["rule_category"]) for row in rows)
    prediction_counts = Counter(str(row["prediction_basis"]) for row in rows)
    consistency_rows = [
        row for row in rows if row.get("prediction_rule_consistent") is not None
    ]
    consistent = sum(1 for row in consistency_rows if row["prediction_rule_consistent"])
    return {
        "task_id": first["task_id"],
        "run_id": first["run_id"],
        "model": first["model"],
        "provider": first["provider"],
        "k": first["k_shot"],
        "seed": first["seed"],
        "n_test": n,
        "accuracy": correct / n if n else 0.0,
        "cue_accuracy": cue_correct / n if n else 0.0,
        "nonparseable_rate": nonparseable / n if n else 0.0,
        "rule_tense": category_counts["tense"],
        "rule_cue": sum(count for key, count in category_counts.items() if key.endswith(" cue")),
        "rule_both": sum(count for key, count in category_counts.items() if key.startswith("both ")),
        "rule_other": category_counts["other"],
        "prediction_tense": prediction_counts["tense"],
        "prediction_cue": prediction_counts["cue"],
        "prediction_both": prediction_counts["both"],
        "prediction_neither": prediction_counts["neither"],
        "consistency_n": len(consistency_rows),
        "consistent": consistent,
        "consistency_rate": (
            consistent / len(consistency_rows) if consistency_rows else 0.0
        ),
        "data_format": first["data_format"],
        "data_file": first["data_file"],
        "eval_data_file": first["eval_data_file"],
        "eval_task_id": first["eval_task_id"],
        "label_assignment_mode": first["label_assignment_mode"],
        "label_swap": first["label_swap"],
        "label_map": first["label_map"],
        "cue_type": first["cue_type"],
    }


def write_summary_csv(path: Path, summary: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "task_id",
        "run_id",
        "model",
        "provider",
        "k",
        "seed",
        "n_test",
        "accuracy",
        "cue_accuracy",
        "nonparseable_rate",
        "rule_tense",
        "rule_cue",
        "rule_both",
        "rule_other",
        "prediction_tense",
        "prediction_cue",
        "prediction_both",
        "prediction_neither",
        "consistency_n",
        "consistent",
        "consistency_rate",
        "data_format",
        "data_file",
        "eval_data_file",
        "eval_task_id",
        "label_assignment_mode",
        "label_swap",
        "label_map",
        "cue_type",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(summary)


def markdown_cell(value: object) -> str:
    return str(value).replace("\n", " ").replace("|", "\\|")


def write_markdown_report(
    path: Path,
    *,
    summary: dict[str, Any],
    rows: list[dict[str, Any]],
) -> None:
    cross_tab = Counter(
        (str(row["prediction_basis"]), str(row["rule_basis"])) for row in rows
    )
    prediction_order = ["tense", "cue", "both", "neither", "nonparseable"]
    rule_order = ["tense", "cue", "both", "other"]

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(f"# Joint Label + Rule: {summary['task_id']}\n\n")
        f.write(f"Run ID: `{summary['run_id']}`\n\n")
        f.write("## Summary\n\n")
        f.write(f"- Tense-label accuracy: {summary['accuracy']:.3f}\n")
        f.write(f"- Cue-label agreement: {summary['cue_accuracy']:.3f}\n")
        f.write(
            "- Articulated rules: "
            f"tense={summary['rule_tense']}, cue={summary['rule_cue']}, "
            f"both={summary['rule_both']}, other={summary['rule_other']}\n"
        )
        f.write(
            "- Prediction basis: "
            f"tense={summary['prediction_tense']}, cue={summary['prediction_cue']}, "
            f"both={summary['prediction_both']}, neither={summary['prediction_neither']}\n"
        )
        f.write(
            "- Prediction/rule consistency among diagnostic rows: "
            f"{summary['consistent']}/{summary['consistency_n']} = "
            f"{summary['consistency_rate']:.3f}\n\n"
        )
        f.write("## Prediction Basis by Articulated Rule Basis\n\n")
        f.write("| Prediction basis | Rule: tense | Rule: cue | Rule: both | Rule: other |\n")
        f.write("|---|---:|---:|---:|---:|\n")
        for prediction in prediction_order:
            f.write(
                f"| {prediction} | "
                f"{cross_tab[(prediction, 'tense')]} | "
                f"{cross_tab[(prediction, 'cue')]} | "
                f"{cross_tab[(prediction, 'both')]} | "
                f"{cross_tab[(prediction, 'other')]} |\n"
            )
        f.write("\n")
        f.write("## Rows\n\n")
        f.write(
            "| # | Prediction basis | Rule category | Consistent | Pred | True | Cue | Rule |\n"
        )
        f.write("|---:|---|---|:---:|:---:|:---:|:---:|---|\n")
        for idx, row in enumerate(rows, start=1):
            consistent = row["prediction_rule_consistent"]
            if consistent is None:
                consistent_text = ""
            else:
                consistent_text = "yes" if consistent else "no"
            f.write(
                f"| {idx} | {row['prediction_basis']} | "
                f"{markdown_cell(row['rule_category'])} | {consistent_text} | "
                f"{markdown_cell(row['parsed_label'])} | "
                f"{markdown_cell(row['true_label'])} | "
                f"{markdown_cell(row['cue_label'])} | "
                f"{markdown_cell(row['articulated_rule'])} |\n"
            )


def select_test_examples(
    examples: list[Example],
    *,
    data_format: str,
    n_test: int,
    seed: int,
) -> tuple[list[Example], str, int]:
    test_sampling_seed = seed + 10_000
    test_sampling_mode = (
        "balanced_from_pool" if data_format == "pool" else "balanced_from_test_split"
    )
    if data_format == "pool":
        pool_examples = [example for example in examples if example.split == "pool"]
        return (
            sample_balanced_from_examples(
                pool_examples,
                n_test,
                test_sampling_seed,
                context="evaluation pool sample",
            ),
            test_sampling_mode,
            test_sampling_seed,
        )
    return (
        sample_balanced_from_split(examples, "test", n_test, test_sampling_seed),
        test_sampling_mode,
        test_sampling_seed,
    )


def main() -> None:
    args = parse_args()
    task = get_task(args.task)
    data_file = args.data_file or default_data_path(
        task.task_id,
        args.seed,
        args.data_format,
    )
    eval_data_file = (
        args.eval_data_file
        or default_eval_data_path(task.task_id, args.seed, args.data_format)
        or data_file
    )
    if not data_file.exists():
        raise FileNotFoundError(f"Data file not found: {data_file}")
    if not eval_data_file.exists():
        raise FileNotFoundError(f"Evaluation data file not found: {eval_data_file}")

    examples = load_processed_examples(data_file)
    eval_examples = (
        examples if eval_data_file == data_file else load_processed_examples(eval_data_file)
    )
    data_format = detect_data_format(examples, args.data_format)
    eval_data_format = detect_data_format(eval_examples, args.data_format)
    test_examples, test_sampling_mode, test_sampling_seed = select_test_examples(
        eval_examples,
        data_format=eval_data_format,
        n_test=args.n_test,
        seed=args.seed,
    )
    pool_examples = [example for example in examples if example.split == "pool"]

    label_map, label_swap, label_assignment_seed = make_label_assignment(
        args.label_assignment,
        args.seed,
    )
    run_id = args.run_id or (
        f"{task.task_id}_joint_label_rule_k{args.k}_seed{args.seed}_"
        f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    )
    output_path = args.output or RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl"
    summary_path = args.summary_output or TABLES_DIR / f"{run_id}_summary.csv"
    markdown_path = args.markdown_output or JOINT_REPORTS_DIR / f"{run_id}.md"
    client = make_client(args.provider, args.model)

    if output_path.exists():
        os.remove(output_path)

    result_rows: list[dict[str, Any]] = []
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
        tqdm(test_examples, desc=f"{task.task_id} joint seed={args.seed}")
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

        true_label = label_map[test_example.label]
        cue_canonical_label = test_example.metadata.get("cue_canonical_label")
        cue_label = (
            label_map[str(cue_canonical_label)]
            if cue_canonical_label in {"A", "B"}
            else None
        )
        prompt = build_joint_label_rule_prompt(
            demonstrations,
            test_example.input,
            label_map=label_map,
        )
        raw_output = client.complete(
            prompt,
            temperature=args.temperature,
            reasoning_effort=args.reasoning_effort,
        )
        parsed_label, articulated_rule = parse_joint_output(raw_output)
        category = categorize_rule(articulated_rule, cue_type=args.cue_type)
        pred_basis = prediction_basis(
            parsed_label,
            true_label=true_label,
            cue_label=cue_label,
        )
        articulated_basis = rule_basis(category)
        consistency = consistency_value(pred_basis, articulated_basis)

        row: dict[str, Any] = {
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
            "demo_seed": demo_seed,
            "demo_example_ids": [example.example_id for example in demonstrations],
            "temperature": args.temperature,
            "reasoning_effort": args.reasoning_effort,
            "cue_type": args.cue_type,
            "test_example_id": test_example.example_id,
            "test_input": test_example.input,
            "prompt": prompt,
            "raw_output": raw_output,
            "parsed_label": parsed_label,
            "articulated_rule": articulated_rule,
            "rule_category": category,
            "rule_basis": articulated_basis,
            "canonical_true_label": test_example.label,
            "true_label": true_label,
            "cue_canonical_label": cue_canonical_label,
            "cue_label": cue_label,
            "correct": parsed_label == true_label,
            "cue_correct": parsed_label == cue_label if cue_label is not None else None,
            "prediction_basis": pred_basis,
            "prediction_rule_consistent": consistency,
        }
        result_rows.append(row)
        append_jsonl(output_path, [row])
        if args.request_delay_seconds > 0:
            time.sleep(args.request_delay_seconds)

    summary = summarize(result_rows)
    write_summary_csv(summary_path, summary)
    write_markdown_report(markdown_path, summary=summary, rows=result_rows)

    print(f"Wrote raw model outputs to {output_path}")
    print(f"Wrote summary to {summary_path}")
    print(f"Wrote Markdown report to {markdown_path}")
    print(summary)


if __name__ == "__main__":
    main()
