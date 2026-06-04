from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .io_utils import RAW_MODEL_OUTPUTS_DIR, REPO_ROOT, RULE_WORKFLOW_REPORTS_DIR, TABLES_DIR
from .run_gold_rule_control import build_latex_section, insert_or_replace_latex_section
from .run_production_articulation_batch import PAIRWISE_HIGH_PREDICTION_BASE_TASKS
from .run_production_batch import SOLID_TASKS, ensure_base_pool, ensure_pairwise_pool
from .tasks import get_task, make_pairwise_task_id


DEFAULT_PREDICTION_BATCH_ID = "production_gpt54_20260602T001915Z"


@dataclass(frozen=True)
class PlannedControl:
    kind: str
    task_id: str
    base_task_id: str
    run_id: str
    output_path: Path
    summary_path: Path
    markdown_path: Path


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run the production gold-rule application controls for the same "
            "tasks used in the production articulation batch."
        )
    )
    parser.add_argument(
        "--prediction-batch-id",
        default=DEFAULT_PREDICTION_BATCH_ID,
        help="Existing prediction batch id whose LaTeX report should be updated.",
    )
    parser.add_argument("--batch-id", default=None)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--provider", choices=("openai", "mock"), default="openai")
    parser.add_argument("--model", default="gpt-5.4")
    parser.add_argument("--n-eval-examples", type=int, default=50)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--reasoning-effort", default="none")
    parser.add_argument("--request-delay-seconds", type=float, default=0.25)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--skip-existing", action="store_true")
    parser.add_argument(
        "--no-update-latex",
        action="store_true",
        help="Run controls and write CSV/folders without editing the production LaTeX file.",
    )
    return parser.parse_args()


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


def make_planned_controls(batch_id: str, seed: int) -> list[PlannedControl]:
    planned: list[PlannedControl] = []
    for task_id in SOLID_TASKS:
        run_id = f"{batch_id}_base_{task_id}_seed{seed}"
        planned.append(
            PlannedControl(
                kind="solid_base",
                task_id=task_id,
                base_task_id=task_id,
                run_id=run_id,
                output_path=RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl",
                summary_path=TABLES_DIR / f"{run_id}_summary.csv",
                markdown_path=RULE_WORKFLOW_REPORTS_DIR / f"{run_id}_report.md",
            )
        )

    for base_task_id in PAIRWISE_HIGH_PREDICTION_BASE_TASKS:
        task_id = make_pairwise_task_id(base_task_id, "same")
        run_id = f"{batch_id}_pairwise_same_{base_task_id}_seed{seed}"
        planned.append(
            PlannedControl(
                kind="pairwise_high_prediction",
                task_id=task_id,
                base_task_id=base_task_id,
                run_id=run_id,
                output_path=RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl",
                summary_path=TABLES_DIR / f"{run_id}_summary.csv",
                markdown_path=RULE_WORKFLOW_REPORTS_DIR / f"{run_id}_report.md",
            )
        )

    return planned


def ensure_data(planned: PlannedControl, seed: int) -> None:
    if planned.kind == "pairwise_high_prediction":
        ensure_pairwise_pool(planned.base_task_id, seed)
    else:
        ensure_base_pool(planned.task_id, seed)


def run_control(planned: PlannedControl, args: argparse.Namespace, batch_id: str) -> None:
    ensure_data(planned, args.seed)
    if (
        args.skip_existing
        and planned.output_path.exists()
        and planned.summary_path.exists()
        and planned.markdown_path.exists()
    ):
        print(f"Skipping existing gold-rule control {planned.run_id}", flush=True)
        return

    run_command(
        [
            sys.executable,
            "-m",
            "src.run_gold_rule_control",
            "--task",
            planned.task_id,
            "--provider",
            args.provider,
            "--model",
            args.model,
            "--n-eval-examples",
            str(args.n_eval_examples),
            "--seed",
            str(args.seed),
            "--data-format",
            "auto",
            "--label-assignment",
            "random_per_seed",
            "--rule-application-prompt-template",
            "minimal_rule_application",
            "--temperature",
            str(args.temperature),
            "--reasoning-effort",
            args.reasoning_effort,
            "--run-id",
            planned.run_id,
            "--output",
            str(planned.output_path),
            "--summary-output",
            str(planned.summary_path),
            "--markdown-output",
            str(planned.markdown_path),
            "--batch-id",
            batch_id,
            "--prediction-batch-id",
            args.prediction_batch_id,
            "--no-update-latex",
            "--request-delay-seconds",
            str(args.request_delay_seconds),
        ]
    )


def load_aggregate_rows(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    args = parse_args()
    if args.n_eval_examples < 1:
        raise ValueError("--n-eval-examples must be positive.")

    batch_id = args.batch_id or (
        f"{args.prediction_batch_id}_gold_rule_control_{utc_timestamp()}"
    )
    planned = make_planned_controls(batch_id, args.seed)
    if args.limit is not None:
        planned = planned[: args.limit]

    print(f"Gold-rule control batch id: {batch_id}", flush=True)
    print(f"Planned controls: {len(planned)}", flush=True)

    for idx, control in enumerate(planned, start=1):
        print(f"\n[{idx}/{len(planned)}] {control.run_id}", flush=True)
        get_task(control.task_id)
        run_control(control, args, batch_id)

    csv_path = TABLES_DIR / f"{batch_id}_gold_rule_control_results.csv"
    rows = load_aggregate_rows(csv_path)
    print(f"\nWrote aggregate gold-rule control CSV to {csv_path}", flush=True)

    if not args.no_update_latex:
        tex_path = TABLES_DIR / f"{args.prediction_batch_id}_production_results.tex"
        section = build_latex_section(batch_id, csv_path, rows)
        insert_or_replace_latex_section(tex_path, section)
        print(f"Updated LaTeX report {tex_path}", flush=True)


if __name__ == "__main__":
    main()
