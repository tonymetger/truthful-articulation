from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .io_utils import EXPERIMENTS_DIR, RAW_MODEL_OUTPUTS_DIR, TABLES_DIR, REPO_ROOT
from .tasks import default_pool_path, get_task, make_pairwise_task_id


SOLID_TASKS = [
    "sst2_positive_sentiment",
    "trec_number_or_date_answer",
    "question_detection_with_punctuation",
    "question_detection_no_punctuation",
    "balanced_sentence_contains_digit",
    "controlled_sentence_contains_negation",
    "random_contains_ab",
    "json_age_at_least_18",
    "pair_first_chars_match",
    "random_more_a_than_b",
    "controlled_sentence_past_tense",
    "trec_human_answer",
    "trec_location_answer",
]

BORDERLINE_TASKS = [
    "sentence_contains_digit",
    "sentence_first_person_pronoun",
]

FAILED_TASKS = [
    "sentence_even_word_count",
    "sentence_second_word_contains_e",
    "controlled_sentence_has_10plus_letter_word",
    "sentence_has_long_word",
    "sentence_contains_negation",
    "sentence_past_tense_main_verb",
    "random_even_length",
    "random_third_equals_third_from_last",
    "random_exactly_two_digits",
    "random_no_repeated_chars",
    "random_starts_ends_same_char",
    "product_code_check_digit",
    "camouflaged_second_word_longer_than_penultimate",
    "camouflaged_exactly_one_first3_contains_t",
    "pair_boundary_initial_match",
]

TASK_GROUPS = {
    **{task_id: "solid" for task_id in SOLID_TASKS},
    **{task_id: "borderline" for task_id in BORDERLINE_TASKS},
    **{task_id: "failed" for task_id in FAILED_TASKS},
}


@dataclass(frozen=True)
class PlannedRun:
    kind: str
    task_id: str
    base_task_id: str
    selection_group: str
    run_id: str
    output_path: Path
    summary_path: Path
    experiment_id: str
    title: str
    description: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the production Step 1 prediction batch and write a LaTeX summary."
    )
    parser.add_argument(
        "--batch-id",
        default=None,
        help="Batch id used in run ids and output file names. Defaults to a UTC timestamp.",
    )
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--model", default="gpt-5.4")
    parser.add_argument("--provider", choices=("openai", "mock"), default="openai")
    parser.add_argument("--k", type=int, default=16)
    parser.add_argument("--n-test", type=int, default=50)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--reasoning-effort", default="none")
    parser.add_argument("--request-delay-seconds", type=float, default=0.25)
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip classification/export commands whose raw JSONL already exists.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional limit on planned runs, useful only for dry plumbing checks.",
    )
    return parser.parse_args()


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def run_command(command: list[str], *, cwd: Path = REPO_ROOT) -> subprocess.CompletedProcess[str]:
    print("+ " + " ".join(command), flush=True)
    return subprocess.run(
        command,
        cwd=cwd,
        check=True,
        text=True,
        capture_output=True,
    )


def ensure_base_pool(task_id: str, seed: int) -> None:
    if default_pool_path(task_id, seed).exists():
        return
    run_command(
        [
            sys.executable,
            "-m",
            "src.prepare_data",
            "--task",
            task_id,
            "--seed",
            str(seed),
        ]
    )


def ensure_pairwise_pool(base_task_id: str, seed: int) -> str:
    ensure_base_pool(base_task_id, seed)
    pairwise_task_id = make_pairwise_task_id(base_task_id, "same")
    run_command(
        [
            sys.executable,
            "-m",
            "src.prepare_pairwise_data",
            "--base-task",
            base_task_id,
            "--combination-rule",
            "same",
            "--seed",
            str(seed),
        ]
    )
    return pairwise_task_id


def make_planned_runs(batch_id: str, seed: int) -> list[PlannedRun]:
    planned: list[PlannedRun] = []
    base_tasks = SOLID_TASKS + BORDERLINE_TASKS + FAILED_TASKS

    for task_id in base_tasks:
        group = TASK_GROUPS[task_id]
        run_id = f"{batch_id}_base_{task_id}_seed{seed}"
        planned.append(
            PlannedRun(
                kind="base",
                task_id=task_id,
                base_task_id=task_id,
                selection_group=group,
                run_id=run_id,
                output_path=RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl",
                summary_path=TABLES_DIR / f"{run_id}_summary.csv",
                experiment_id=run_id,
                title=f"Production base prediction: {task_id}",
                description=(
                    "Production GPT-5.4 label-prediction run for the base task "
                    f"`{task_id}` using the standard protocol."
                ),
            )
        )

    for base_task_id in SOLID_TASKS:
        task_id = make_pairwise_task_id(base_task_id, "same")
        run_id = f"{batch_id}_pairwise_same_{base_task_id}_seed{seed}"
        planned.append(
            PlannedRun(
                kind="pairwise_same",
                task_id=task_id,
                base_task_id=base_task_id,
                selection_group="solid",
                run_id=run_id,
                output_path=RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl",
                summary_path=TABLES_DIR / f"{run_id}_summary.csv",
                experiment_id=run_id,
                title=f"Production pairwise-same prediction: {base_task_id}",
                description=(
                    "Production GPT-5.4 label-prediction run for the pairwise "
                    f"`same` transform of `{base_task_id}`. Canonical Label A "
                    "means the two displayed inputs have the same base-task category."
                ),
            )
        )

    return planned


def run_classification(planned: PlannedRun, args: argparse.Namespace) -> None:
    if planned.kind == "pairwise_same":
        ensure_pairwise_pool(planned.base_task_id, args.seed)
    else:
        ensure_base_pool(planned.task_id, args.seed)

    if args.skip_existing and planned.output_path.exists() and planned.summary_path.exists():
        print(f"Skipping existing run {planned.run_id}", flush=True)
        return

    run_command(
        [
            sys.executable,
            "-m",
            "src.run_classification",
            "--task",
            planned.task_id,
            "--provider",
            args.provider,
            "--model",
            args.model,
            "--k",
            str(args.k),
            "--n-test",
            str(args.n_test),
            "--seed",
            str(args.seed),
            "--demo-sampling-mode",
            "resample_per_test",
            "--data-format",
            "auto",
            "--label-assignment",
            "random_per_seed",
            "--prompt-template",
            "minimal",
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
            "--request-delay-seconds",
            str(args.request_delay_seconds),
        ]
    )


def export_experiment(planned: PlannedRun, batch_id: str) -> Path:
    output_root = EXPERIMENTS_DIR / batch_id
    completed = run_command(
        [
            sys.executable,
            "-m",
            "src.export_experiment",
            "--experiment-id",
            planned.experiment_id,
            "--title",
            planned.title,
            "--description",
            planned.description,
            "--result-files",
            str(planned.output_path),
            "--output-root",
            str(output_root),
        ]
    )
    output = completed.stdout.strip()
    print(output, flush=True)
    match = re.search(r"Wrote experiment bundle to (.+)", output)
    if match:
        return Path(match.group(1))
    return output_root


def load_rows(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def summarize_run(planned: PlannedRun, experiment_dir: Path) -> dict[str, Any]:
    rows = load_rows(planned.output_path)
    n = len(rows)
    correct = sum(1 for row in rows if row.get("correct"))
    nonparseable = sum(1 for row in rows if row.get("parsed_label") is None)
    parsed_counts = Counter(row.get("parsed_label") for row in rows)
    true_counts = Counter(row.get("true_label") for row in rows)
    canonical_counts = Counter(row.get("canonical_true_label") for row in rows)
    canonical_correct: dict[str, str] = {}
    for label in sorted(canonical_counts):
        label_rows = [row for row in rows if row.get("canonical_true_label") == label]
        label_correct = sum(1 for row in label_rows if row.get("correct"))
        canonical_correct[str(label)] = f"{label_correct}/{len(label_rows)}"

    return {
        "kind": planned.kind,
        "task_id": planned.task_id,
        "base_task_id": planned.base_task_id,
        "selection_group": planned.selection_group,
        "run_id": planned.run_id,
        "n": n,
        "correct": correct,
        "accuracy": correct / n if n else 0.0,
        "nonparseable": nonparseable,
        "parsed_A": parsed_counts.get("A", 0),
        "parsed_B": parsed_counts.get("B", 0),
        "true_A": true_counts.get("A", 0),
        "true_B": true_counts.get("B", 0),
        "canonical_A": canonical_counts.get("A", 0),
        "canonical_B": canonical_counts.get("B", 0),
        "canonical_A_correct": canonical_correct.get("A", ""),
        "canonical_B_correct": canonical_correct.get("B", ""),
        "raw_jsonl": relative(planned.output_path),
        "summary_csv": relative(planned.summary_path),
        "experiment_dir": relative(experiment_dir),
    }


def write_results_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "kind",
        "selection_group",
        "task_id",
        "base_task_id",
        "n",
        "correct",
        "accuracy",
        "nonparseable",
        "parsed_A",
        "parsed_B",
        "true_A",
        "true_B",
        "canonical_A_correct",
        "canonical_B_correct",
        "run_id",
        "raw_jsonl",
        "summary_csv",
        "experiment_dir",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def latex_escape(text: object) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in str(text))


def latex_identifier(text: object) -> str:
    return latex_escape(text).replace(r"\_", r"\_\allowbreak{}")


def pct(value: float) -> str:
    return f"{100 * value:.1f}\\%"


def table_rows(rows: list[dict[str, Any]], *, pairwise: bool) -> list[str]:
    lines: list[str] = []
    sort_key = (
        (lambda row: (row["selection_group"], row["base_task_id"]))
        if pairwise
        else (lambda row: (row["selection_group"], row["task_id"]))
    )
    for row in sorted(rows, key=sort_key):
        task_text = row["base_task_id"] if pairwise else row["task_id"]
        if pairwise:
            same = row["canonical_A_correct"]
            different = row["canonical_B_correct"]
            lines.append(
                " & ".join(
                    [
                        latex_identifier(task_text),
                        f"{row['correct']}/{row['n']}",
                        pct(float(row["accuracy"])),
                        latex_escape(same),
                        latex_escape(different),
                    ]
                )
                + r" \\"
            )
        else:
            lines.append(
                " & ".join(
                    [
                        latex_escape(row["selection_group"]),
                        latex_identifier(task_text),
                        f"{row['correct']}/{row['n']}",
                        pct(float(row["accuracy"])),
                        str(row["nonparseable"]),
                    ]
                )
                + r" \\"
            )
    return lines


def count_threshold(rows: list[dict[str, Any]], threshold: float) -> int:
    return sum(1 for row in rows if float(row["accuracy"]) >= threshold)


def mean_accuracy(rows: list[dict[str, Any]]) -> float:
    return sum(float(row["accuracy"]) for row in rows) / len(rows) if rows else 0.0


def write_latex_report(
    path: Path,
    *,
    batch_id: str,
    args: argparse.Namespace,
    rows: list[dict[str, Any]],
    csv_path: Path,
) -> None:
    base_rows = [row for row in rows if row["kind"] == "base"]
    pairwise_rows = [row for row in rows if row["kind"] == "pairwise_same"]
    base_by_group: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in base_rows:
        base_by_group[row["selection_group"]].append(row)

    lines = [
        r"\documentclass[11pt]{article}",
        r"\usepackage[margin=1in]{geometry}",
        r"\usepackage{booktabs}",
        r"\usepackage{longtable}",
        r"\usepackage{array}",
        r"\usepackage{xurl}",
        r"\usepackage[T1]{fontenc}",
        r"\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}",
        r"\begin{document}",
        "",
        r"\section*{Production Prediction Experiments}",
        "",
        (
            "This report summarizes only the production runs in batch "
            f"\\texttt{{{latex_escape(batch_id)}}}. All runs used "
            f"\\texttt{{{latex_escape(args.model)}}}, seed {args.seed}, "
            f"$k={args.k}$, $n={args.n_test}$, resampling demonstrations per "
            "test example, random-per-seed label assignment, the minimal prompt, "
            f"temperature {args.temperature}, and reasoning effort "
            f"\\texttt{{{latex_escape(args.reasoning_effort)}}}."
        ),
        "",
        (
            "Every row has a corresponding human-readable experiment folder under "
            f"\\path{{{relative(EXPERIMENTS_DIR / batch_id)}}}. "
            f"The machine-readable aggregate table is "
            f"\\path{{{relative(csv_path)}}}."
        ),
        "",
        r"\subsection*{Headline Findings From This Batch}",
        r"\begin{itemize}",
        (
            r"\item Base tasks: "
            f"{count_threshold(base_rows, 0.85)} of {len(base_rows)} reached "
            r"at least 85\% accuracy in this production run."
        ),
        (
            r"\item Base-task mean accuracy by selection group: "
            + "; ".join(
                f"{group}: {pct(mean_accuracy(base_by_group[group]))}"
                for group in ("solid", "borderline", "failed")
                if group in base_by_group
            )
            + "."
        ),
        (
            r"\item Pairwise-same solid-task transforms: "
            f"{count_threshold(pairwise_rows, 0.85)} of {len(pairwise_rows)} "
            r"reached at least 85\% accuracy."
        ),
        (
            r"\item Pairwise-same mean accuracy across the solid-task transforms was "
            f"{pct(mean_accuracy(pairwise_rows))}."
        ),
        r"\end{itemize}",
        "",
        r"\subsection*{Base Prediction Results}",
        r"\footnotesize",
        r"\begin{longtable}{L{0.15\linewidth}L{0.47\linewidth}rrr}",
        r"\toprule",
        r"Selection set & Task & Correct & Accuracy & Nonparseable \\",
        r"\midrule",
        r"\endhead",
        *table_rows(base_rows, pairwise=False),
        r"\bottomrule",
        r"\end{longtable}",
        r"\normalsize",
        "",
        r"\subsection*{Pairwise-Same Prediction Results For Solid Base Tasks}",
        (
            "For these rows, canonical Label A means the two displayed inputs have "
            "the same base-task category; canonical Label B means they have "
            "different base-task categories."
        ),
        "",
        r"\footnotesize",
        r"\begin{longtable}{L{0.49\linewidth}rrrr}",
        r"\toprule",
        r"Base task & Correct & Accuracy & Same correct & Different correct \\",
        r"\midrule",
        r"\endhead",
        *table_rows(pairwise_rows, pairwise=True),
        r"\bottomrule",
        r"\end{longtable}",
        r"\normalsize",
        "",
        r"\end{document}",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    batch_id = args.batch_id or f"production_gpt54_{utc_timestamp()}"
    planned_runs = make_planned_runs(batch_id, args.seed)
    if args.limit is not None:
        planned_runs = planned_runs[: args.limit]

    print(f"Batch id: {batch_id}", flush=True)
    print(f"Planned runs: {len(planned_runs)}", flush=True)

    rows: list[dict[str, Any]] = []
    for idx, planned in enumerate(planned_runs, start=1):
        print(f"\n[{idx}/{len(planned_runs)}] {planned.run_id}", flush=True)
        get_task(planned.task_id)
        run_classification(planned, args)
        experiment_dir = export_experiment(planned, batch_id)
        rows.append(summarize_run(planned, experiment_dir))

    csv_path = TABLES_DIR / f"{batch_id}_production_results.csv"
    tex_path = TABLES_DIR / f"{batch_id}_production_results.tex"
    write_results_csv(csv_path, rows)
    write_latex_report(tex_path, batch_id=batch_id, args=args, rows=rows, csv_path=csv_path)

    print(f"\nWrote aggregate CSV to {csv_path}", flush=True)
    print(f"Wrote LaTeX report to {tex_path}", flush=True)


if __name__ == "__main__":
    main()
