from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .io_utils import EXPERIMENTS_DIR, read_jsonl, write_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a human-readable experiment folder from result JSONL files."
    )
    parser.add_argument(
        "--experiment-id",
        default=None,
        help=(
            "Optional experiment slug. By default the output folder is "
            "<UTC timestamp>_<slug>, so this does not need to be globally unique."
        ),
    )
    parser.add_argument("--title", required=True, help="Human-readable experiment title.")
    parser.add_argument("--description", default="", help="Short note about what this experiment tests.")
    parser.add_argument("--result-files", type=Path, nargs="+", required=True)
    parser.add_argument("--output-root", type=Path, default=EXPERIMENTS_DIR)
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return slug or "experiment"


def make_experiment_dir_name(experiment_id: str | None, title: str, timestamp: str) -> str:
    slug = slugify(experiment_id or title)
    return f"{timestamp}_{slug}"


def extract_final_input(prompt: str) -> str:
    matches = re.findall(r"Input: (.+?)\nLabel:", prompt, flags=re.DOTALL)
    if not matches:
        return ""
    input_text = matches[-1].strip()
    try:
        return str(json.loads(input_text))
    except json.JSONDecodeError:
        return input_text.strip('"')


def load_result_rows(paths: list[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path_idx, path in enumerate(paths):
        for row_idx, row in enumerate(read_jsonl(path)):
            row["_source_result_file"] = str(path)
            row["_source_file_index"] = path_idx
            row["_source_row_index"] = row_idx
            row["test_input"] = extract_final_input(str(row.get("prompt", "")))
            rows.append(row)
    return sorted(
        rows,
        key=lambda row: (
            row.get("seed", 0),
            row.get("_source_file_index", 0),
            row.get("_source_row_index", 0),
        ),
    )


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        raise ValueError("Cannot summarize an empty result set.")
    first = rows[0]
    n = len(rows)
    correct = sum(1 for row in rows if row.get("correct"))
    nonparseable = sum(1 for row in rows if row.get("parsed_label") is None)
    task_ids = sorted({str(row.get("task_id")) for row in rows})
    data_files = sorted({str(row.get("data_file")) for row in rows if row.get("data_file")})
    eval_data_files = sorted(
        {str(row.get("eval_data_file")) for row in rows if row.get("eval_data_file")}
    )
    prompt_templates = sorted(
        {str(row.get("prompt_template")) for row in rows if row.get("prompt_template")}
    )
    return {
        "task_id": first.get("task_id"),
        "task_ids": ",".join(task_ids),
        "task_count": len(task_ids),
        "model": first.get("model"),
        "provider": first.get("provider"),
        "k": first.get("k_shot"),
        "temperature": first.get("temperature"),
        "reasoning_effort": first.get("reasoning_effort"),
        "data_format": first.get("data_format"),
        "data_file": first.get("data_file"),
        "data_files": "\n".join(data_files),
        "eval_data_file": first.get("eval_data_file"),
        "eval_data_files": "\n".join(eval_data_files),
        "eval_task_id": first.get("eval_task_id"),
        "test_sampling_mode": first.get("test_sampling_mode"),
        "demo_sampling_mode": first.get("demo_sampling_mode"),
        "prompt_template": (
            prompt_templates[0] if len(prompt_templates) == 1 else "multiple"
        ),
        "prompt_templates": ",".join(prompt_templates),
        "label_assignment_mode": first.get("label_assignment_mode"),
        "label_swap": first.get("label_swap"),
        "label_map": first.get("label_map"),
        "seeds": ",".join(str(seed) for seed in sorted({row.get("seed") for row in rows})),
        "n_test": n,
        "correct": correct,
        "accuracy": correct / n if n else 0.0,
        "nonparseable": nonparseable,
        "nonparseable_rate": nonparseable / n if n else 0.0,
        "cue_correct": sum(1 for row in rows if row.get("cue_correct")),
        "cue_accuracy": (
            sum(1 for row in rows if row.get("cue_correct")) / n
            if first.get("cue_label") is not None
            else None
        ),
    }


def summarize_by_seed(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[Any, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[row.get("seed")].append(row)

    summaries = []
    for seed in sorted(groups):
        summary = summarize(groups[seed])
        summary["seed"] = seed
        summaries.append(summary)
    return summaries


def summarize_by_task(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[str(row.get("task_id"))].append(row)

    summaries = []
    for task_id in sorted(groups):
        summary = summarize(groups[task_id])
        summary["task_id"] = task_id
        summary["seed"] = ",".join(
            str(seed) for seed in sorted({row.get("seed") for row in groups[task_id]})
        )
        summaries.append(summary)
    return summaries


def summarize_by_prompt_template(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[str(row.get("prompt_template", ""))].append(row)

    summaries = []
    for prompt_template in sorted(groups):
        summary = summarize(groups[prompt_template])
        summary["prompt_template"] = prompt_template
        summary["seed"] = ",".join(
            str(seed) for seed in sorted({row.get("seed") for row in groups[prompt_template]})
        )
        summaries.append(summary)
    return summaries


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def format_percent(value: Any) -> str:
    try:
        return f"{100 * float(value):.1f}%"
    except (TypeError, ValueError):
        return "n/a"


def format_markdown_table(rows: list[dict[str, Any]]) -> str:
    lines = [
        "| seed | n | correct | accuracy | nonparseable |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            "| {seed} | {n_test} | {correct} | {accuracy} | {nonparseable} |".format(
                seed=row["seed"],
                n_test=row["n_test"],
                correct=row["correct"],
                accuracy=format_percent(row["accuracy"]),
                nonparseable=row["nonparseable"],
            )
        )
    return "\n".join(lines)


def format_task_markdown_table(rows: list[dict[str, Any]]) -> str:
    lines = [
        "| task | n | correct | accuracy | nonparseable |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in sorted(rows, key=lambda item: (-float(item["accuracy"]), item["task_id"])):
        lines.append(
            "| {task_id} | {n_test} | {correct} | {accuracy} | {nonparseable} |".format(
                task_id=row["task_id"],
                n_test=row["n_test"],
                correct=row["correct"],
                accuracy=format_percent(row["accuracy"]),
                nonparseable=row["nonparseable"],
            )
        )
    return "\n".join(lines)


def format_prompt_markdown_table(rows: list[dict[str, Any]]) -> str:
    lines = [
        "| prompt template | n | correct | accuracy | nonparseable |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in sorted(rows, key=lambda item: (-float(item["accuracy"]), item["prompt_template"])):
        lines.append(
            "| {prompt_template} | {n_test} | {correct} | {accuracy} | {nonparseable} |".format(
                prompt_template=row["prompt_template"],
                n_test=row["n_test"],
                correct=row["correct"],
                accuracy=format_percent(row["accuracy"]),
                nonparseable=row["nonparseable"],
            )
        )
    return "\n".join(lines)


def write_readme(
    path: Path,
    title: str,
    description: str,
    aggregate: dict[str, Any],
    seed_summaries: list[dict[str, Any]],
    task_summaries: list[dict[str, Any]],
    prompt_summaries: list[dict[str, Any]],
    rows: list[dict[str, Any]],
) -> None:
    mistakes = [row for row in rows if not row.get("correct")]
    setup_task_line = (
        f"- Tasks: `{aggregate.get('task_ids')}`"
        if aggregate.get("task_count", 1) > 1
        else f"- Task: `{aggregate.get('task_id')}`"
    )
    setup_data_line = (
        f"- Data files: `{aggregate.get('task_count')}` task-specific pool files"
        if aggregate.get("task_count", 1) > 1
        else f"- Data file: `{aggregate.get('data_file')}`"
    )
    eval_data_file = aggregate.get("eval_data_file")
    if eval_data_file and eval_data_file != aggregate.get("data_file"):
        setup_data_line += f"\n- Evaluation data file: `{eval_data_file}`"
    lines = [
        f"# {title}",
        "",
        description.strip() or "No description provided.",
        "",
        "## Setup",
        "",
        setup_task_line,
        f"- Provider/model: `{aggregate.get('provider')}` / `{aggregate.get('model')}`",
        f"- k-shot: `{aggregate.get('k')}`",
        f"- Temperature: `{aggregate.get('temperature')}`",
        f"- Reasoning effort: `{aggregate.get('reasoning_effort')}`",
        f"- Data format: `{aggregate.get('data_format')}`",
        setup_data_line,
        f"- Test sampling mode: `{aggregate.get('test_sampling_mode')}`",
        f"- Demo sampling mode: `{aggregate.get('demo_sampling_mode')}`",
        f"- Prompt template(s): `{aggregate.get('prompt_templates') or aggregate.get('prompt_template')}`",
        f"- Label assignment: `{aggregate.get('label_assignment_mode')}`",
        f"- Label swap: `{aggregate.get('label_swap')}`",
        f"- Label map: `{aggregate.get('label_map')}`",
        f"- Seeds: `{aggregate.get('seeds')}`",
        "",
        "## Results",
        "",
        f"- Overall accuracy: **{aggregate['correct']}/{aggregate['n_test']} = {format_percent(aggregate['accuracy'])}**",
        f"- Nonparseable outputs: **{aggregate['nonparseable']}/{aggregate['n_test']} = {format_percent(aggregate['nonparseable_rate'])}**",
        (
            "- Spacing-cue agreement: "
            f"**{aggregate['cue_correct']}/{aggregate['n_test']} = {format_percent(aggregate['cue_accuracy'])}**"
            if aggregate.get("cue_accuracy") is not None
            else "- Spacing-cue agreement: n/a"
        ),
        f"- Mistakes: **{len(mistakes)}**",
        "",
        format_markdown_table(seed_summaries),
        "",
        "## Task Results",
        "",
        format_task_markdown_table(task_summaries),
        "",
        "## Prompt Template Results",
        "",
        format_prompt_markdown_table(prompt_summaries),
        "",
        "## Files",
        "",
        "- `transcript.md`: full prompt and model response for every model call.",
        "- `mistakes.md`: only the incorrect or nonparseable calls, for quick inspection.",
        "- `summary.csv`: one row per seed.",
        "- `task_summary.csv`: one row per task.",
        "- `prompt_summary.csv`: one row per prompt template.",
        "- `row_level_results.csv`: compact row-level table with input, prediction, truth, and correctness.",
        "- `raw_results.jsonl`: combined machine-readable result log.",
        "- `config.json`: metadata for this experiment bundle.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_transcript(path: Path, rows: list[dict[str, Any]]) -> None:
    lines = ["# Full Transcript", ""]
    for idx, row in enumerate(rows, start=1):
        correct_text = "correct" if row.get("correct") else "incorrect"
        lines.extend(
            [
                f"## Call {idx:03d}: seed {row.get('seed')} / {row.get('test_example_id')} / {correct_text}",
                "",
                f"- Run ID: `{row.get('run_id')}`",
                f"- Canonical true label: `{row.get('canonical_true_label', row.get('true_label'))}`",
                f"- Prompt true label: `{row.get('true_label')}`",
                f"- Cue-implied prompt label: `{row.get('cue_label')}`",
                f"- Parsed label: `{row.get('parsed_label')}`",
                f"- Raw output: `{row.get('raw_output')}`",
                "",
                "### Prompt Sent To Model",
                "",
                "```text",
                str(row.get("prompt", "")),
                "```",
                "",
                "### Model Response",
                "",
                "```text",
                str(row.get("raw_output", "")),
                "```",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_mistakes(path: Path, rows: list[dict[str, Any]]) -> None:
    mistakes = [row for row in rows if not row.get("correct")]
    lines = ["# Mistakes", ""]
    if not mistakes:
        lines.append("No incorrect or nonparseable outputs.")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    for row in mistakes:
        lines.extend(
            [
                f"## seed {row.get('seed')} / {row.get('test_example_id')}",
                "",
                f"- True label: `{row.get('true_label')}`",
                f"- Canonical true label: `{row.get('canonical_true_label', row.get('true_label'))}`",
                f"- Cue-implied prompt label: `{row.get('cue_label')}`",
                f"- Parsed label: `{row.get('parsed_label')}`",
                f"- Raw output: `{row.get('raw_output')}`",
                "",
                "Input:",
                "",
                "```text",
                str(row.get("test_input", "")),
                "```",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_config(
    path: Path,
    experiment_id: str,
    experiment_slug: str,
    timestamp: str,
    title: str,
    description: str,
    result_files: list[Path],
    aggregate: dict[str, Any],
) -> None:
    config = {
        "experiment_id": experiment_id,
        "experiment_slug": experiment_slug,
        "timestamp_utc": timestamp,
        "title": title,
        "description": description,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_result_files": [str(path) for path in result_files],
        "aggregate": aggregate,
    }
    path.write_text(json.dumps(config, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    timestamp = utc_timestamp()
    experiment_slug = slugify(args.experiment_id or args.title)
    experiment_id = make_experiment_dir_name(args.experiment_id, args.title, timestamp)
    experiment_dir = args.output_root / experiment_id
    if experiment_dir.exists():
        if not args.overwrite:
            raise FileExistsError(
                f"{experiment_dir} already exists. Use --overwrite to rebuild it."
            )
        shutil.rmtree(experiment_dir)
    experiment_dir.mkdir(parents=True)

    rows = load_result_rows(args.result_files)
    aggregate = summarize(rows)
    seed_summaries = summarize_by_seed(rows)
    task_summaries = summarize_by_task(rows)
    prompt_summaries = summarize_by_prompt_template(rows)

    write_readme(
        experiment_dir / "README.md",
        args.title,
        args.description,
        aggregate,
        seed_summaries,
        task_summaries,
        prompt_summaries,
        rows,
    )
    write_config(
        experiment_dir / "config.json",
        experiment_id,
        experiment_slug,
        timestamp,
        args.title,
        args.description,
        args.result_files,
        aggregate,
    )
    write_transcript(experiment_dir / "transcript.md", rows)
    write_mistakes(experiment_dir / "mistakes.md", rows)
    write_jsonl(experiment_dir / "raw_results.jsonl", rows)
    write_csv(
        experiment_dir / "summary.csv",
        seed_summaries,
        [
            "task_id",
            "model",
            "provider",
            "k",
            "seed",
            "n_test",
            "correct",
            "accuracy",
            "nonparseable",
            "nonparseable_rate",
            "cue_correct",
            "cue_accuracy",
            "temperature",
            "reasoning_effort",
            "data_format",
            "data_file",
            "eval_data_format",
            "eval_data_file",
            "eval_task_id",
            "test_sampling_mode",
            "demo_sampling_mode",
            "prompt_template",
            "label_assignment_mode",
            "label_swap",
            "label_map",
        ],
    )
    write_csv(
        experiment_dir / "task_summary.csv",
        task_summaries,
        [
            "task_id",
            "model",
            "provider",
            "k",
            "seed",
            "n_test",
            "correct",
            "accuracy",
            "nonparseable",
            "nonparseable_rate",
            "cue_correct",
            "cue_accuracy",
            "temperature",
            "reasoning_effort",
            "data_format",
            "data_file",
            "test_sampling_mode",
            "demo_sampling_mode",
            "prompt_template",
            "label_assignment_mode",
            "label_swap",
            "label_map",
        ],
    )
    write_csv(
        experiment_dir / "prompt_summary.csv",
        prompt_summaries,
        [
            "prompt_template",
            "task_id",
            "model",
            "provider",
            "k",
            "seed",
            "n_test",
            "correct",
            "accuracy",
            "nonparseable",
            "nonparseable_rate",
            "cue_correct",
            "cue_accuracy",
            "temperature",
            "reasoning_effort",
            "data_format",
            "data_file",
            "test_sampling_mode",
            "demo_sampling_mode",
            "label_assignment_mode",
            "label_swap",
            "label_map",
        ],
    )
    write_csv(
        experiment_dir / "row_level_results.csv",
        rows,
        [
            "run_id",
            "task_id",
            "model",
            "provider",
            "k_shot",
            "seed",
            "data_format",
            "data_file",
            "test_sampling_mode",
            "test_sampling_seed",
            "label_assignment_mode",
            "label_assignment_seed",
            "label_swap",
            "label_map",
            "test_example_id",
            "test_input",
            "canonical_true_label",
            "true_label",
            "cue_canonical_label",
            "cue_label",
            "cue_correct",
            "raw_output",
            "parsed_label",
            "correct",
            "temperature",
            "reasoning_effort",
            "demo_sampling_mode",
            "prompt_template",
            "demo_seed",
            "demo_example_ids",
        ],
    )

    print(f"Wrote experiment bundle to {experiment_dir}")


if __name__ == "__main__":
    main()
