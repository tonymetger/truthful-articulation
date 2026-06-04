from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    def tqdm(iterable, **kwargs):  # type: ignore[no-redef]
        del kwargs
        return iterable

from .io_utils import (
    EXPERIMENTS_DIR,
    RAW_MODEL_OUTPUTS_DIR,
    RULE_WORKFLOW_REPORTS_DIR,
    TABLES_DIR,
    append_jsonl,
)
from .model_client import make_client
from .prompts import (
    DEFAULT_RULE_APPLICATION_PROMPT_TEMPLATE,
    available_rule_application_prompt_templates,
    build_rule_application_prompt,
    parse_label,
)
from .run_articulation import prompt_facing_rule_text
from .run_articulation_workflow import (
    RULE_EVAL_SEED_OFFSET,
    markdown_cell,
    sample_uniform_eval_examples,
)
from .run_classification import (
    DEFAULT_DATA_FORMAT,
    DEFAULT_LABEL_ASSIGNMENT,
    DEFAULT_PROVIDER,
    DEFAULT_REASONING_EFFORT,
    DEFAULT_REQUEST_DELAY_SECONDS,
    DEFAULT_TEMPERATURE,
    default_data_path,
    detect_data_format,
    make_label_assignment,
)
from .run_production_batch import latex_escape, latex_identifier, pct, relative
from .tasks import Example, get_task, is_pairwise_task_id, load_processed_examples


DEFAULT_GOLD_RULE_MODEL = "gpt-5.4"
DEFAULT_N_EVAL_EXAMPLES = 50
DEFAULT_PREDICTION_BATCH_ID = "production_gpt54_20260602T001915Z"


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Control for rule articulation: give the model the prompt-facing "
            "gold rule directly and evaluate rule application on held-out inputs."
        )
    )
    parser.add_argument("--task", required=True)
    parser.add_argument("--data-file", type=Path, default=None)
    parser.add_argument(
        "--eval-data-file",
        type=Path,
        default=None,
        help=(
            "Optional separate processed JSONL file for rule-application inputs. "
            "The gold rule is taken from --task, but evaluation rows are sampled "
            "from this file."
        ),
    )
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
        "--rule-application-prompt-template",
        choices=available_rule_application_prompt_templates(),
        default=DEFAULT_RULE_APPLICATION_PROMPT_TEMPLATE,
    )
    parser.add_argument("--provider", choices=("openai", "mock"), default=DEFAULT_PROVIDER)
    parser.add_argument("--model", default=DEFAULT_GOLD_RULE_MODEL)
    parser.add_argument("--n-eval-examples", type=int, default=DEFAULT_N_EVAL_EXAMPLES)
    parser.add_argument("--seed", type=int, default=0)
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
    parser.add_argument("--batch-id", default=None)
    parser.add_argument(
        "--prediction-batch-id",
        default=DEFAULT_PREDICTION_BATCH_ID,
        help="Production prediction batch whose LaTeX report should be updated.",
    )
    parser.add_argument(
        "--no-experiment-folder",
        action="store_true",
        help="Do not create a human-readable experiment folder.",
    )
    parser.add_argument(
        "--no-update-latex",
        action="store_true",
        help="Write outputs without inserting the aggregate control table into LaTeX.",
    )
    parser.add_argument(
        "--request-delay-seconds",
        type=float,
        default=DEFAULT_REQUEST_DELAY_SECONDS,
    )
    return parser.parse_args()


def load_eval_candidates(
    task_id: str,
    seed: int,
    data_file_arg: Path | None,
    data_format_arg: str,
) -> tuple[Path, str, list[Example], list[Example]]:
    data_file = data_file_arg or default_data_path(task_id, seed, data_format_arg)
    if not data_file.exists():
        raise FileNotFoundError(
            f"Data file not found: {data_file}. Prepare it with "
            f"`python -m src.prepare_data --task {task_id} --seed {seed}`."
        )
    examples = load_processed_examples(data_file)
    data_format = detect_data_format(examples, data_format_arg)
    eval_candidates = (
        [example for example in examples if example.split == "pool"]
        if data_format == "pool"
        else list(examples)
    )
    return data_file, data_format, examples, eval_candidates


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    if not rows:
        raise ValueError("Cannot summarize an empty gold-rule control run.")
    first = rows[0]
    n_eval = len(rows)
    correct = sum(1 for row in rows if row["correct"])
    nonparseable = sum(1 for row in rows if row["parsed_label"] is None)
    return {
        "task_id": first["task_id"],
        "run_id": first["run_id"],
        "control_type": first["control_type"],
        "application_model": first["application_model"],
        "application_provider": first["application_provider"],
        "seed": first["seed"],
        "n_gold_rules": 1,
        "rule_eval_examples": n_eval,
        "total_rule_application_calls": n_eval,
        "correct": correct,
        "accuracy": correct / n_eval if n_eval else 0.0,
        "nonparseable": nonparseable,
        "nonparseable_rate": nonparseable / n_eval if n_eval else 0.0,
        "data_format": first.get("data_format"),
        "data_file": first.get("data_file"),
        "eval_data_format": first.get("eval_data_format"),
        "eval_data_file": first.get("eval_data_file"),
        "eval_task_id": first.get("eval_task_id"),
        "eval_sampling_mode": first.get("eval_sampling_mode"),
        "eval_sampling_seed": first.get("eval_sampling_seed"),
        "label_assignment_mode": first.get("label_assignment_mode"),
        "label_swap": first.get("label_swap"),
        "label_map": first.get("label_map"),
        "rule_application_prompt_template": first.get(
            "rule_application_prompt_template"
        ),
        "application_temperature": first.get("application_temperature"),
        "application_reasoning_effort": first.get("application_reasoning_effort"),
        "canonical_rule_text": first.get("canonical_rule_text"),
        "prompt_rule_text": first.get("prompt_rule_text"),
    }


def write_summary_csv(path: Path, row: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "task_id",
                "run_id",
                "control_type",
                "application_model",
                "application_provider",
                "seed",
                "n_gold_rules",
                "rule_eval_examples",
                "total_rule_application_calls",
                "correct",
                "accuracy",
                "nonparseable",
                "nonparseable_rate",
                "data_format",
                "data_file",
                "eval_data_format",
                "eval_data_file",
                "eval_task_id",
                "eval_sampling_mode",
                "eval_sampling_seed",
                "label_assignment_mode",
                "label_swap",
                "label_map",
                "rule_application_prompt_template",
                "application_temperature",
                "application_reasoning_effort",
                "canonical_rule_text",
                "prompt_rule_text",
            ],
        )
        writer.writeheader()
        writer.writerow(row)


def write_markdown_report(
    path: Path,
    *,
    summary_row: dict[str, object],
    rows: list[dict[str, object]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(f"# Gold-Rule Application Control: {summary_row['task_id']}\n\n")
        f.write(f"Run ID: `{summary_row['run_id']}`\n\n")
        f.write(f"Correct canonical rule: {summary_row['canonical_rule_text']}\n\n")
        f.write(
            f"Correct prompt-facing rule: {summary_row['prompt_rule_text']}\n\n"
        )
        f.write("## Summary\n\n")
        f.write("- Gold rules tested: `1`\n")
        f.write(
            "- Rule-application calls: "
            f"`{summary_row['total_rule_application_calls']}`\n"
        )
        f.write(
            "- Rule-application accuracy: "
            f"`{summary_row['correct']}/{summary_row['total_rule_application_calls']}` "
            f"= `{float(summary_row['accuracy']):.3f}`\n"
        )
        f.write(
            f"- Nonparseable rate: `{float(summary_row['nonparseable_rate']):.3f}`\n\n"
        )
        f.write("## Settings\n\n")
        f.write(f"- Rule-application model: `{summary_row['application_model']}`\n")
        f.write(f"- Seed: `{summary_row['seed']}`\n")
        f.write(
            "- Rule-application prompt template: "
            f"`{summary_row['rule_application_prompt_template']}`\n"
        )
        f.write(
            "- Label assignment: "
            f"`{summary_row['label_assignment_mode']}`, swap="
            f"`{summary_row['label_swap']}`\n\n"
        )
        f.write("## Detailed Evaluations\n\n")
        f.write("| Eval | Example ID | Input | True | Predicted | Correct |\n")
        f.write("|---:|---|---|:---:|:---:|:---:|\n")
        for row in rows:
            predicted = row["parsed_label"] if row["parsed_label"] is not None else ""
            correct_mark = "yes" if row["correct"] else "no"
            f.write(
                f"| {row['rule_eval_index']} | "
                f"{markdown_cell(row['eval_example_id'])} | "
                f"{markdown_cell(row['eval_input'])} | "
                f"{markdown_cell(row['eval_true_label'])} | "
                f"{markdown_cell(predicted)} | {correct_mark} |\n"
            )


def write_transcript(path: Path, rows: list[dict[str, object]]) -> None:
    lines = ["# Full Gold-Rule Control Transcript", ""]
    for idx, row in enumerate(rows, start=1):
        correct_text = "correct" if row["correct"] else "incorrect"
        lines.extend(
            [
                f"## Call {idx:03d}: {row['eval_example_id']} / {correct_text}",
                "",
                f"- Run ID: `{row['run_id']}`",
                f"- Canonical true label: `{row['eval_canonical_label']}`",
                f"- Prompt true label: `{row['eval_true_label']}`",
                f"- Parsed label: `{row['parsed_label']}`",
                f"- Raw output: `{row['application_raw_output']}`",
                "",
                "### Prompt Sent To Model",
                "",
                "```text",
                str(row["application_prompt"]),
                "```",
                "",
                "### Model Response",
                "",
                "```text",
                str(row["application_raw_output"]),
                "```",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_experiment_folder(
    *,
    batch_id: str,
    run_id: str,
    output_path: Path,
    summary_path: Path,
    markdown_path: Path,
    summary_row: dict[str, object],
    rows: list[dict[str, object]],
) -> Path:
    folder_root = EXPERIMENTS_DIR / batch_id
    folder = folder_root / f"{utc_timestamp()}_{run_id.lower()}"
    folder.mkdir(parents=True, exist_ok=False)

    shutil.copy2(output_path, folder / "raw_results.jsonl")
    shutil.copy2(summary_path, folder / "summary.csv")
    shutil.copy2(markdown_path, folder / "report.md")
    write_transcript(folder / "transcript.md", rows)

    config = {
        "title": f"Gold-rule application control: {summary_row['task_id']}",
        "description": (
            "Control run that gives the rule-application model the correct "
            "prompt-facing rule directly, bypassing rule articulation."
        ),
        "kind": "gold_rule_control",
        "task_id": summary_row["task_id"],
        "run_id": run_id,
        "source_raw_results": relative(output_path),
        "source_summary": relative(summary_path),
        "source_report": relative(markdown_path),
    }
    (folder / "config.json").write_text(
        json.dumps(config, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    accuracy = 100 * float(summary_row["accuracy"])
    readme = [
        f"# Gold-rule application control: {summary_row['task_id']}",
        "",
        "This run gives the rule-application model the correct prompt-facing rule directly.",
        "",
        "## Summary",
        "",
        f"- Task: `{summary_row['task_id']}`",
        f"- Run ID: `{run_id}`",
        f"- Gold rules: `{summary_row['n_gold_rules']}`",
        f"- Rule-application calls: `{summary_row['total_rule_application_calls']}`",
        f"- Rule-application accuracy: `{accuracy:.1f}%`",
        f"- Nonparseable rate: `{100 * float(summary_row['nonparseable_rate']):.1f}%`",
        "",
        "## Files",
        "",
        "- `report.md`: compact human-readable result table.",
        "- `transcript.md`: full prompt and model response for every call.",
        "- `summary.csv`: aggregate workflow summary.",
        "- `raw_results.jsonl`: full prompts, responses, labels, and evaluation rows.",
        "- `config.json`: source paths and run metadata.",
        "",
    ]
    (folder / "README.md").write_text("\n".join(readme), encoding="utf-8")
    return folder


def read_existing_aggregate(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_aggregate_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "kind",
        "task_id",
        "run_id",
        "n_gold_rules",
        "rule_eval_examples",
        "total_rule_application_calls",
        "correct",
        "accuracy",
        "nonparseable",
        "nonparseable_rate",
        "application_model",
        "application_provider",
        "seed",
        "label_swap",
        "raw_jsonl",
        "summary_csv",
        "markdown_report",
        "experiment_dir",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def update_aggregate_csv(
    path: Path,
    summary_row: dict[str, object],
    *,
    output_path: Path,
    summary_path: Path,
    markdown_path: Path,
    experiment_dir: Path | None,
) -> list[dict[str, Any]]:
    new_row = {
        "kind": "gold_rule_control",
        "task_id": summary_row["task_id"],
        "run_id": summary_row["run_id"],
        "n_gold_rules": summary_row["n_gold_rules"],
        "rule_eval_examples": summary_row["rule_eval_examples"],
        "total_rule_application_calls": summary_row["total_rule_application_calls"],
        "correct": summary_row["correct"],
        "accuracy": summary_row["accuracy"],
        "nonparseable": summary_row["nonparseable"],
        "nonparseable_rate": summary_row["nonparseable_rate"],
        "application_model": summary_row["application_model"],
        "application_provider": summary_row["application_provider"],
        "seed": summary_row["seed"],
        "label_swap": summary_row["label_swap"],
        "raw_jsonl": relative(output_path),
        "summary_csv": relative(summary_path),
        "markdown_report": relative(markdown_path),
        "experiment_dir": relative(experiment_dir) if experiment_dir else "",
    }
    rows = [
        row for row in read_existing_aggregate(path)
        if row.get("run_id") != str(summary_row["run_id"])
    ]
    rows.append(new_row)
    rows.sort(key=lambda row: str(row["task_id"]))
    write_aggregate_csv(path, rows)
    return rows


def gold_control_table_rows(rows: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    for row in sorted(rows, key=lambda item: str(item["task_id"])):
        run_set = (
            "pairwise high"
            if is_pairwise_task_id(str(row["task_id"]))
            else "solid base"
        )
        run_id = str(row.get("run_id", ""))
        run_label = "rerun" if "rerun" in run_id else "initial"
        total = int(row["total_rule_application_calls"])
        correct = int(round(float(row["accuracy"]) * total))
        lines.append(
            " & ".join(
                [
                    latex_escape(run_set),
                    latex_identifier(str(row["task_id"])),
                    latex_escape(run_label),
                    f"{correct}/{total}",
                    pct(float(row["accuracy"])),
                    f"{100 * float(row['nonparseable_rate']):.1f}\\%",
                ]
            )
            + r" \\"
        )
    return lines


def build_latex_section(batch_id: str, csv_path: Path, rows: list[dict[str, Any]]) -> str:
    base_rows = [
        row for row in rows if not is_pairwise_task_id(str(row["task_id"]))
    ]
    pairwise_rows = [
        row for row in rows if is_pairwise_task_id(str(row["task_id"]))
    ]
    base_ge_85 = sum(1 for row in base_rows if float(row["accuracy"]) >= 0.85)
    pairwise_ge_85 = sum(
        1 for row in pairwise_rows if float(row["accuracy"]) >= 0.85
    )

    def mean_accuracy(section_rows: list[dict[str, Any]]) -> float:
        if not section_rows:
            return 0.0
        return sum(float(row["accuracy"]) for row in section_rows) / len(section_rows)

    lines = [
        r"\subsection*{Gold-Rule Application Control Results}",
        "",
        (
            "This control bypasses the articulation step: the model is given the "
            "correct prompt-facing rule directly and is then asked to classify "
            "fresh held-out examples with the same rule-application prompt, "
            "GPT-5.4, seed, label assignment, temperature, and no-reasoning "
            "settings used in the production articulation workflows."
        ),
        "",
        r"\begin{itemize}",
        (
            r"\item Solid base control runs: "
            f"{base_ge_85} of {len(base_rows)} gold-rule controls reached at "
            r"least 85\% rule-application accuracy; mean accuracy was "
            f"{pct(mean_accuracy(base_rows))}."
        ),
        (
            r"\item Pairwise-same high-prediction control runs: "
            f"{pairwise_ge_85} of {len(pairwise_rows)} gold-rule controls reached at "
            r"least 85\% rule-application accuracy; mean accuracy was "
            f"{pct(mean_accuracy(pairwise_rows))}."
        ),
        r"\end{itemize}",
        "",
        (
            "Detailed reports and raw transcripts are stored in individual "
            f"folders under \\path{{{relative(EXPERIMENTS_DIR / batch_id)}}}. "
            f"The aggregate gold-rule control table is \\path{{{relative(csv_path)}}}."
        ),
        "",
        r"\footnotesize",
        r"\begin{longtable}{L{0.14\linewidth}L{0.38\linewidth}L{0.10\linewidth}rrr}",
        r"\toprule",
        r"Run set & Task & Run & Eval correct & Accuracy & Nonparseable \\",
        r"\midrule",
        r"\endhead",
        *gold_control_table_rows(rows),
        r"\bottomrule",
        r"\end{longtable}",
        r"\normalsize",
        "",
    ]
    return "\n".join(lines)


def insert_or_replace_latex_section(tex_path: Path, section: str) -> None:
    text = tex_path.read_text(encoding="utf-8")
    marker = r"\subsection*{Gold-Rule Application Control Results}"
    if marker in text:
        import re

        pattern = re.compile(
            re.escape(marker) + r".*?(?=\\end\{document\})",
            flags=re.DOTALL,
        )
        text = pattern.sub(lambda _match: section + "\n\n", text)
    else:
        text = text.replace(r"\end{document}", section + "\n\\end{document}")
    tex_path.write_text(text, encoding="utf-8")


def main() -> None:
    args = parse_args()
    if args.n_eval_examples < 1:
        raise ValueError("--n-eval-examples must be positive.")

    task = get_task(args.task)
    data_file, data_format, _examples, eval_candidates = load_eval_candidates(
        task.task_id,
        args.seed,
        args.data_file,
        args.data_format,
    )
    eval_data_file = args.eval_data_file or data_file
    eval_data_format = data_format
    if args.eval_data_file is not None:
        if not eval_data_file.exists():
            raise FileNotFoundError(
                f"Evaluation data file not found: {eval_data_file}."
            )
        eval_file_examples = load_processed_examples(eval_data_file)
        eval_data_format = detect_data_format(eval_file_examples, args.data_format)
        eval_candidates = (
            [example for example in eval_file_examples if example.split == "pool"]
            if eval_data_format == "pool"
            else list(eval_file_examples)
        )
    label_map, label_swap, label_assignment_seed = make_label_assignment(
        args.label_assignment,
        args.seed,
    )
    prompt_rule_text = prompt_facing_rule_text(task.rule_text, label_map)

    eval_seed = args.seed * 10_000_000 + RULE_EVAL_SEED_OFFSET
    eval_examples = sample_uniform_eval_examples(
        eval_candidates,
        args.n_eval_examples,
        eval_seed,
        excluded_example_ids=set(),
    )
    eval_sampling_mode = (
        "uniform_from_pool"
        if eval_data_format == "pool"
        else "uniform_from_all_splits"
    )

    timestamp = utc_timestamp()
    run_id = args.run_id or (
        f"{task.task_id}_gold_rule_control_n{args.n_eval_examples}_"
        f"seed{args.seed}_{timestamp}"
    )
    batch_id = args.batch_id or f"gold_rule_control_{timestamp}"
    output_path = args.output or RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl"
    summary_path = args.summary_output or TABLES_DIR / f"{run_id}_summary.csv"
    markdown_path = (
        args.markdown_output
        or RULE_WORKFLOW_REPORTS_DIR / f"{run_id}_report.md"
    )
    for path in (output_path, markdown_path):
        if path.exists():
            os.remove(path)

    client = make_client(args.provider, args.model)
    result_rows: list[dict[str, object]] = []
    for eval_index, eval_example in enumerate(
        tqdm(eval_examples, desc=f"{task.task_id} gold-rule control"),
        start=1,
    ):
        eval_true_label = label_map[eval_example.label]
        application_prompt = build_rule_application_prompt(
            prompt_rule_text,
            eval_example.input,
            prompt_template=args.rule_application_prompt_template,
        )
        application_raw_output = client.complete(
            application_prompt,
            temperature=args.temperature,
            reasoning_effort=args.reasoning_effort,
        )
        parsed_label = parse_label(application_raw_output)
        row = {
            "run_id": run_id,
            "task_id": task.task_id,
            "control_type": "gold_rule",
            "seed": args.seed,
            "data_format": data_format,
            "data_file": str(data_file),
            "eval_data_format": eval_data_format,
            "eval_data_file": str(eval_data_file),
            "eval_task_id": eval_example.task_id,
            "eval_sampling_mode": eval_sampling_mode,
            "eval_sampling_seed": eval_seed,
            "label_assignment_mode": args.label_assignment,
            "label_assignment_seed": label_assignment_seed,
            "label_swap": label_swap,
            "label_map": label_map,
            "canonical_rule_text": task.rule_text,
            "prompt_rule_text": prompt_rule_text,
            "gold_rule": prompt_rule_text,
            "rule_index": 1,
            "rule_eval_index": eval_index,
            "rule_eval_examples": args.n_eval_examples,
            "application_provider": args.provider,
            "application_model": args.model,
            "application_temperature": args.temperature,
            "application_reasoning_effort": args.reasoning_effort,
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
        rows=result_rows,
    )

    experiment_dir: Path | None = None
    if not args.no_experiment_folder:
        experiment_dir = write_experiment_folder(
            batch_id=batch_id,
            run_id=run_id,
            output_path=output_path,
            summary_path=summary_path,
            markdown_path=markdown_path,
            summary_row=summary_row,
            rows=result_rows,
        )

    aggregate_path = TABLES_DIR / f"{batch_id}_gold_rule_control_results.csv"
    aggregate_rows = update_aggregate_csv(
        aggregate_path,
        summary_row,
        output_path=output_path,
        summary_path=summary_path,
        markdown_path=markdown_path,
        experiment_dir=experiment_dir,
    )

    if not args.no_update_latex:
        tex_path = TABLES_DIR / f"{args.prediction_batch_id}_production_results.tex"
        section = build_latex_section(batch_id, aggregate_path, aggregate_rows)
        insert_or_replace_latex_section(tex_path, section)

    print(f"Wrote gold-rule outputs to {output_path}")
    print(f"Wrote summary to {summary_path}")
    print(f"Wrote markdown report to {markdown_path}")
    if experiment_dir is not None:
        print(f"Wrote experiment folder to {experiment_dir}")
    print(f"Wrote aggregate gold-rule control CSV to {aggregate_path}")
    if not args.no_update_latex:
        print(
            "Updated LaTeX report "
            f"{TABLES_DIR / f'{args.prediction_batch_id}_production_results.tex'}"
        )
    print(summary_row)


if __name__ == "__main__":
    main()
