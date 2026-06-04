from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .io_utils import (
    EXPERIMENTS_DIR,
    RAW_MODEL_OUTPUTS_DIR,
    REPO_ROOT,
    RULE_WORKFLOW_REPORTS_DIR,
    TABLES_DIR,
)
from .run_production_batch import (
    SOLID_TASKS,
    ensure_base_pool,
    ensure_pairwise_pool,
    latex_escape,
    latex_identifier,
    pct,
    relative,
)
from .tasks import get_task, make_pairwise_task_id


PAIRWISE_HIGH_PREDICTION_BASE_TASKS = [
    "sst2_positive_sentiment",
    "question_detection_with_punctuation",
    "question_detection_no_punctuation",
]


@dataclass(frozen=True)
class PlannedWorkflow:
    kind: str
    task_id: str
    base_task_id: str
    run_id: str
    output_path: Path
    summary_path: Path
    markdown_path: Path
    title: str
    description: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run the production rule-articulation workflow batch and add the "
            "results to the production LaTeX report."
        )
    )
    parser.add_argument(
        "--prediction-batch-id",
        default="production_gpt54_20260602T001915Z",
        help="Existing prediction batch id whose LaTeX report should be updated.",
    )
    parser.add_argument("--batch-id", default=None)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--provider", choices=("openai", "mock"), default="openai")
    parser.add_argument("--model", default="gpt-5.4")
    parser.add_argument("--k", type=int, default=16)
    parser.add_argument("--n-samples", type=int, default=50)
    parser.add_argument("--rule-eval-examples", type=int, default=5)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--reasoning-effort", default="none")
    parser.add_argument("--request-delay-seconds", type=float, default=0.25)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--skip-existing", action="store_true")
    parser.add_argument(
        "--no-update-latex",
        action="store_true",
        help="Run workflows and write CSV/folders without editing the production LaTeX file.",
    )
    return parser.parse_args()


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def run_command(command: list[str], *, cwd: Path = REPO_ROOT) -> subprocess.CompletedProcess[str]:
    print("+ " + " ".join(command), flush=True)
    try:
        return subprocess.run(
            command,
            cwd=cwd,
            check=True,
            text=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as exc:
        if exc.stdout:
            print(exc.stdout, flush=True)
        if exc.stderr:
            print(exc.stderr, flush=True)
        raise


def make_planned_workflows(batch_id: str, seed: int) -> list[PlannedWorkflow]:
    planned: list[PlannedWorkflow] = []
    for task_id in SOLID_TASKS:
        run_id = f"{batch_id}_base_{task_id}_seed{seed}"
        planned.append(
            PlannedWorkflow(
                kind="solid_base",
                task_id=task_id,
                base_task_id=task_id,
                run_id=run_id,
                output_path=RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl",
                summary_path=TABLES_DIR / f"{run_id}_summary.csv",
                markdown_path=RULE_WORKFLOW_REPORTS_DIR / f"{run_id}_report.md",
                title=f"Production articulation workflow: {task_id}",
                description=(
                    "Production GPT-5.4 rule-articulation workflow for the solid "
                    f"base task `{task_id}`."
                ),
            )
        )

    for base_task_id in PAIRWISE_HIGH_PREDICTION_BASE_TASKS:
        task_id = make_pairwise_task_id(base_task_id, "same")
        run_id = f"{batch_id}_pairwise_same_{base_task_id}_seed{seed}"
        planned.append(
            PlannedWorkflow(
                kind="pairwise_high_prediction",
                task_id=task_id,
                base_task_id=base_task_id,
                run_id=run_id,
                output_path=RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl",
                summary_path=TABLES_DIR / f"{run_id}_summary.csv",
                markdown_path=RULE_WORKFLOW_REPORTS_DIR / f"{run_id}_report.md",
                title=f"Production articulation workflow: pairwise same {base_task_id}",
                description=(
                    "Production GPT-5.4 rule-articulation workflow for the pairwise "
                    f"`same` transform of `{base_task_id}`."
                ),
            )
        )

    return planned


def ensure_data(planned: PlannedWorkflow, seed: int) -> None:
    if planned.kind == "pairwise_high_prediction":
        ensure_pairwise_pool(planned.base_task_id, seed)
    else:
        ensure_base_pool(planned.task_id, seed)


def run_workflow(planned: PlannedWorkflow, args: argparse.Namespace) -> None:
    ensure_data(planned, args.seed)
    if (
        args.skip_existing
        and planned.output_path.exists()
        and planned.summary_path.exists()
        and planned.markdown_path.exists()
    ):
        print(f"Skipping existing workflow {planned.run_id}", flush=True)
        return

    run_command(
        [
            sys.executable,
            "-m",
            "src.run_articulation_workflow",
            "--task",
            planned.task_id,
            "--provider",
            args.provider,
            "--model",
            args.model,
            "--application-provider",
            args.provider,
            "--application-model",
            args.model,
            "--k",
            str(args.k),
            "--n-samples",
            str(args.n_samples),
            "--rule-eval-examples",
            str(args.rule_eval_examples),
            "--seed",
            str(args.seed),
            "--demo-sampling-mode",
            "resample_per_test",
            "--data-format",
            "auto",
            "--label-assignment",
            "random_per_seed",
            "--articulation-prompt-template",
            "minimal_rule_description",
            "--rule-application-prompt-template",
            "minimal_rule_application",
            "--temperature",
            str(args.temperature),
            "--application-temperature",
            str(args.temperature),
            "--reasoning-effort",
            args.reasoning_effort,
            "--application-reasoning-effort",
            args.reasoning_effort,
            "--run-id",
            planned.run_id,
            "--output",
            str(planned.output_path),
            "--summary-output",
            str(planned.summary_path),
            "--markdown-output",
            str(planned.markdown_path),
            "--request-delay-seconds",
            str(args.request_delay_seconds),
        ]
    )


def load_summary(path: Path) -> dict[str, str]:
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 1:
        raise ValueError(f"Expected exactly one summary row in {path}, found {len(rows)}.")
    return rows[0]


def make_workflow_folder(
    planned: PlannedWorkflow,
    summary: dict[str, str],
    *,
    batch_id: str,
) -> Path:
    folder_root = EXPERIMENTS_DIR / batch_id
    folder_name = f"{utc_timestamp()}_{planned.run_id.lower()}"
    folder = folder_root / folder_name
    folder.mkdir(parents=True, exist_ok=False)

    shutil.copy2(planned.output_path, folder / "raw_results.jsonl")
    shutil.copy2(planned.summary_path, folder / "summary.csv")
    shutil.copy2(planned.markdown_path, folder / "report.md")

    config = {
        "title": planned.title,
        "description": planned.description,
        "kind": planned.kind,
        "task_id": planned.task_id,
        "base_task_id": planned.base_task_id,
        "run_id": planned.run_id,
        "source_raw_results": relative(planned.output_path),
        "source_summary": relative(planned.summary_path),
        "source_report": relative(planned.markdown_path),
    }
    (folder / "config.json").write_text(
        json.dumps(config, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    accuracy = 100 * float(summary["accuracy"])
    mean_rule_accuracy = 100 * float(summary["mean_rule_accuracy"])
    readme = [
        f"# {planned.title}",
        "",
        planned.description,
        "",
        "## Summary",
        "",
        f"- Task: `{planned.task_id}`",
        f"- Run ID: `{planned.run_id}`",
        f"- Articulated rules: `{summary['n_articulated_rules']}`",
        f"- Evaluation examples per rule: `{summary['rule_eval_examples']}`",
        f"- Total rule-application calls: `{summary['total_rule_application_calls']}`",
        f"- Rule-application accuracy: `{accuracy:.1f}%`",
        f"- Mean per-rule accuracy: `{mean_rule_accuracy:.1f}%`",
        f"- Rules with all evals correct: `{summary['rules_all_correct']}`",
        f"- Nonparseable rate: `{100 * float(summary['nonparseable_rate']):.1f}%`",
        "",
        "## Files",
        "",
        "- `report.md`: human-readable articulated rules and detailed evaluations.",
        "- `summary.csv`: aggregate workflow summary.",
        "- `raw_results.jsonl`: full prompts, responses, labels, and evaluation rows.",
        "- `config.json`: source paths and run metadata.",
        "",
    ]
    (folder / "README.md").write_text("\n".join(readme), encoding="utf-8")
    return folder


def find_existing_workflow_folder(batch_id: str, run_id: str) -> Path | None:
    folder_root = EXPERIMENTS_DIR / batch_id
    if not folder_root.exists():
        return None
    matches = sorted(folder_root.glob(f"*_{run_id.lower()}"))
    if matches:
        return matches[-1]
    return None


def summarize_workflow(
    planned: PlannedWorkflow,
    summary: dict[str, str],
    folder: Path,
) -> dict[str, Any]:
    return {
        "kind": planned.kind,
        "task_id": planned.task_id,
        "base_task_id": planned.base_task_id,
        "run_id": planned.run_id,
        "n_articulated_rules": int(summary["n_articulated_rules"]),
        "rule_eval_examples": int(summary["rule_eval_examples"]),
        "total_rule_application_calls": int(summary["total_rule_application_calls"]),
        "accuracy": float(summary["accuracy"]),
        "mean_rule_accuracy": float(summary["mean_rule_accuracy"]),
        "rules_all_correct": int(summary["rules_all_correct"]),
        "rules_any_correct": int(summary["rules_any_correct"]),
        "nonparseable_rate": float(summary["nonparseable_rate"]),
        "raw_jsonl": relative(planned.output_path),
        "summary_csv": relative(planned.summary_path),
        "markdown_report": relative(planned.markdown_path),
        "experiment_dir": relative(folder),
    }


def write_results_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "kind",
        "task_id",
        "base_task_id",
        "n_articulated_rules",
        "rule_eval_examples",
        "total_rule_application_calls",
        "accuracy",
        "mean_rule_accuracy",
        "rules_all_correct",
        "rules_any_correct",
        "nonparseable_rate",
        "run_id",
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


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def articulation_table_rows(rows: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    for row in sorted(rows, key=lambda item: (item["kind"], item["task_id"])):
        run_set = "solid base" if row["kind"] == "solid_base" else "pairwise high"
        lines.append(
            " & ".join(
                [
                    latex_escape(run_set),
                    latex_identifier(row["task_id"]),
                    f"{int(round(float(row['accuracy']) * int(row['total_rule_application_calls'])))}/{row['total_rule_application_calls']}",
                    pct(float(row["accuracy"])),
                    f"{row['rules_all_correct']}/{row['n_articulated_rules']}",
                    f"{100 * float(row['nonparseable_rate']):.1f}\\%",
                ]
            )
            + r" \\"
        )
    return lines


def build_latex_section(batch_id: str, csv_path: Path, rows: list[dict[str, Any]]) -> str:
    solid_rows = [row for row in rows if row["kind"] == "solid_base"]
    pairwise_rows = [row for row in rows if row["kind"] == "pairwise_high_prediction"]
    solid_ge_85 = sum(1 for row in solid_rows if float(row["accuracy"]) >= 0.85)
    pairwise_ge_85 = sum(1 for row in pairwise_rows if float(row["accuracy"]) >= 0.85)
    lines = [
        r"\subsection*{Rule Articulation Workflow Results}",
        "",
        (
            "This section summarizes the production articulation workflows in batch "
            f"\\path{{{batch_id}}}. Each workflow generated 50 "
            "articulated rules from 16 labeled demonstrations and evaluated each "
            "rule on 5 fresh held-out examples using the same GPT-5.4, seed, "
            "label-assignment, prompt, temperature, and no-reasoning settings as "
            "the production prediction runs."
        ),
        "",
        (
            "Detailed per-rule reports and raw transcripts are stored in individual "
            f"folders under \\path{{{relative(EXPERIMENTS_DIR / batch_id)}}}. "
            f"The aggregate articulation table is \\path{{{relative(csv_path)}}}."
        ),
        "",
        r"\begin{itemize}",
        (
            r"\item Solid base tasks: "
            f"{solid_ge_85} of {len(solid_rows)} articulation workflows reached "
            r"at least 85\% rule-application accuracy; mean accuracy was "
            f"{pct(mean([float(row['accuracy']) for row in solid_rows]))}."
        ),
        (
            r"\item Pairwise-same high-prediction tasks: "
            f"{pairwise_ge_85} of {len(pairwise_rows)} articulation workflows reached "
            r"at least 85\% rule-application accuracy; mean accuracy was "
            f"{pct(mean([float(row['accuracy']) for row in pairwise_rows]))}."
        ),
        r"\end{itemize}",
        "",
        r"\scriptsize",
        r"\begin{longtable}{L{0.12\linewidth}L{0.34\linewidth}rrrr}",
        r"\toprule",
        r"Run set & Task & Eval correct & Accuracy & Rules 5/5 & Nonparseable \\",
        r"\midrule",
        r"\endhead",
        *articulation_table_rows(rows),
        r"\bottomrule",
        r"\end{longtable}",
        r"\normalsize",
        "",
    ]
    return "\n".join(lines)


def insert_or_replace_latex_section(tex_path: Path, section: str) -> None:
    text = tex_path.read_text(encoding="utf-8")
    marker = r"\subsection*{Rule Articulation Workflow Results}"
    if marker in text:
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
    batch_id = args.batch_id or (
        f"{args.prediction_batch_id}_articulation_{utc_timestamp()}"
    )
    planned = make_planned_workflows(batch_id, args.seed)
    if args.limit is not None:
        planned = planned[: args.limit]

    print(f"Articulation batch id: {batch_id}", flush=True)
    print(f"Planned workflows: {len(planned)}", flush=True)

    rows: list[dict[str, Any]] = []
    for idx, workflow in enumerate(planned, start=1):
        print(f"\n[{idx}/{len(planned)}] {workflow.run_id}", flush=True)
        get_task(workflow.task_id)
        run_workflow(workflow, args)
        summary = load_summary(workflow.summary_path)
        folder = (
            find_existing_workflow_folder(batch_id, workflow.run_id)
            if args.skip_existing
            else None
        )
        if folder is None:
            folder = make_workflow_folder(workflow, summary, batch_id=batch_id)
        else:
            print(f"Reusing workflow folder {folder}", flush=True)
        rows.append(summarize_workflow(workflow, summary, folder))
        print(f"Wrote workflow folder to {folder}", flush=True)

    csv_path = TABLES_DIR / f"{batch_id}_articulation_results.csv"
    write_results_csv(csv_path, rows)
    print(f"\nWrote aggregate articulation CSV to {csv_path}", flush=True)

    if not args.no_update_latex:
        tex_path = TABLES_DIR / f"{args.prediction_batch_id}_production_results.tex"
        section = build_latex_section(batch_id, csv_path, rows)
        insert_or_replace_latex_section(tex_path, section)
        print(f"Updated LaTeX report {tex_path}", flush=True)


if __name__ == "__main__":
    main()
