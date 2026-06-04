from __future__ import annotations

import argparse
import csv
import os
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

from .io_utils import RAW_MODEL_OUTPUTS_DIR, TABLES_DIR, append_jsonl, read_jsonl
from .model_client import make_client
from .prompts import (
    DEFAULT_RULE_APPLICATION_PROMPT_TEMPLATE,
    available_rule_application_prompt_templates,
    build_rule_application_prompt,
    parse_label,
)
from .run_classification import (
    DEFAULT_MODEL,
    DEFAULT_PROVIDER,
    DEFAULT_REASONING_EFFORT,
    DEFAULT_REQUEST_DELAY_SECONDS,
    DEFAULT_TEMPERATURE,
)


DEFAULT_RULE_APPLICATION_PROMPT_TEMPLATE_NAME = DEFAULT_RULE_APPLICATION_PROMPT_TEMPLATE


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate articulated rules by asking a model to classify held-out "
            "inputs from the rule alone."
        )
    )
    parser.add_argument(
        "--articulation-results",
        type=Path,
        required=True,
        help="JSONL output from src.run_articulation.",
    )
    parser.add_argument("--provider", choices=("openai", "mock"), default=DEFAULT_PROVIDER)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument(
        "--rule-application-prompt-template",
        "--prompt-template",
        dest="rule_application_prompt_template",
        choices=available_rule_application_prompt_templates(),
        default=DEFAULT_RULE_APPLICATION_PROMPT_TEMPLATE_NAME,
        help="Named rule-application prompt template from src/prompts.py.",
    )
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    parser.add_argument(
        "--reasoning-effort",
        choices=("none", "minimal", "low", "medium", "high", "xhigh"),
        default=DEFAULT_REASONING_EFFORT,
        help="Optional Responses API reasoning.effort value; use 'none' for non-reasoning GPT-5.x runs.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional maximum number of articulated rules to evaluate.",
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


def require_string(row: dict[str, Any], field: str, row_number: int) -> str:
    value = row.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(
            f"Articulation row {row_number} is missing non-empty string field {field!r}."
        )
    return value


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    n_test = len(rows)
    correct = sum(1 for row in rows if row["correct"])
    nonparseable = sum(1 for row in rows if row["parsed_label"] is None)
    first = rows[0]
    return {
        "task_id": first.get("task_id"),
        "source_run_id": first.get("source_run_id"),
        "source_articulation_results": first.get("source_articulation_results"),
        "application_model": first.get("model"),
        "application_provider": first.get("provider"),
        "n_test": n_test,
        "accuracy": correct / n_test if n_test else 0.0,
        "nonparseable_rate": nonparseable / n_test if n_test else 0.0,
        "rule_application_prompt_template": first.get(
            "rule_application_prompt_template"
        ),
        "articulation_model": first.get("articulation_model"),
        "articulation_provider": first.get("articulation_provider"),
        "articulation_prompt_template": first.get("articulation_prompt_template"),
        "label_assignment_mode": first.get("label_assignment_mode"),
        "label_swap": first.get("label_swap"),
        "label_map": first.get("label_map"),
    }


def write_summary_csv(path: Path, row: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "task_id",
                "source_run_id",
                "source_articulation_results",
                "application_model",
                "application_provider",
                "n_test",
                "accuracy",
                "nonparseable_rate",
                "rule_application_prompt_template",
                "articulation_model",
                "articulation_provider",
                "articulation_prompt_template",
                "label_assignment_mode",
                "label_swap",
                "label_map",
            ],
        )
        writer.writeheader()
        writer.writerow(row)


def main() -> None:
    args = parse_args()
    articulation_rows = read_jsonl(args.articulation_results)
    if args.limit is not None:
        if args.limit < 1:
            raise ValueError("--limit must be positive.")
        articulation_rows = articulation_rows[: args.limit]
    if not articulation_rows:
        raise ValueError(f"No articulation rows found in {args.articulation_results}.")

    first = articulation_rows[0]
    task_id = first.get("task_id", "unknown_task")
    source_run_id = first.get("run_id", args.articulation_results.stem)
    run_id = args.run_id or (
        f"{task_id}_rule_application_{source_run_id}_"
        f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    )
    output_path = args.output or RAW_MODEL_OUTPUTS_DIR / f"{run_id}.jsonl"
    summary_path = args.summary_output or TABLES_DIR / f"{run_id}_summary.csv"
    client = make_client(args.provider, args.model)

    if output_path.exists():
        os.remove(output_path)

    result_rows: list[dict[str, object]] = []
    for row_idx, articulation_row in enumerate(
        tqdm(articulation_rows, desc=f"{task_id} rule application"),
        start=1,
    ):
        articulated_rule = require_string(
            articulation_row,
            "articulated_rule",
            row_idx,
        )
        test_input = require_string(articulation_row, "heldout_input", row_idx)
        true_label = require_string(articulation_row, "heldout_prompt_label", row_idx)
        if true_label not in {"A", "B"}:
            raise ValueError(
                f"Articulation row {row_idx} has invalid heldout_prompt_label "
                f"{true_label!r}; expected 'A' or 'B'."
            )

        prompt = build_rule_application_prompt(
            articulated_rule,
            test_input,
            prompt_template=args.rule_application_prompt_template,
        )
        raw_output = client.complete(
            prompt,
            temperature=args.temperature,
            reasoning_effort=args.reasoning_effort,
        )
        parsed_label = parse_label(raw_output)
        result_row = {
            "run_id": run_id,
            "source_articulation_results": str(args.articulation_results),
            "source_row_number": row_idx,
            "source_run_id": articulation_row.get("run_id"),
            "task_id": articulation_row.get("task_id"),
            "provider": args.provider,
            "model": args.model,
            "temperature": args.temperature,
            "reasoning_effort": args.reasoning_effort,
            "rule_application_prompt_template": args.rule_application_prompt_template,
            "articulation_provider": articulation_row.get("provider"),
            "articulation_model": articulation_row.get("model"),
            "articulation_prompt_template": articulation_row.get(
                "articulation_prompt_template"
            ),
            "articulated_rule": articulated_rule,
            "canonical_rule_text": articulation_row.get("canonical_rule_text"),
            "prompt_rule_text": articulation_row.get("prompt_rule_text"),
            "label_assignment_mode": articulation_row.get("label_assignment_mode"),
            "label_assignment_seed": articulation_row.get("label_assignment_seed"),
            "label_swap": articulation_row.get("label_swap"),
            "label_map": articulation_row.get("label_map"),
            "test_example_id": articulation_row.get("heldout_example_id"),
            "test_input": test_input,
            "canonical_true_label": articulation_row.get("heldout_canonical_label"),
            "true_label": true_label,
            "prompt": prompt,
            "raw_output": raw_output,
            "parsed_label": parsed_label,
            "correct": parsed_label == true_label,
        }
        result_rows.append(result_row)
        append_jsonl(output_path, [result_row])
        if args.request_delay_seconds > 0:
            time.sleep(args.request_delay_seconds)

    summary_row = summarize(result_rows)
    write_summary_csv(summary_path, summary_row)

    print(f"Wrote rule-application outputs to {output_path}")
    print(f"Wrote summary to {summary_path}")
    print(summary_row)


if __name__ == "__main__":
    main()
