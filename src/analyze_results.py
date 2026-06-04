from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

from .io_utils import TABLES_DIR, read_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize classification JSONL result files.")
    parser.add_argument("result_files", type=Path, nargs="+")
    parser.add_argument("--output", type=Path, default=TABLES_DIR / "classification_summary.csv")
    return parser.parse_args()


def summarize_group(rows: list[dict[str, object]]) -> dict[str, object]:
    first = rows[0]
    n = len(rows)
    correct = sum(1 for row in rows if row.get("correct"))
    nonparseable = sum(1 for row in rows if row.get("parsed_label") is None)
    return {
        "run_id": first.get("run_id"),
        "task_id": first.get("task_id"),
        "model": first.get("model"),
        "provider": first.get("provider"),
        "k": first.get("k_shot"),
        "seed": first.get("seed"),
        "n_test": n,
        "accuracy": correct / n if n else 0.0,
        "nonparseable_rate": nonparseable / n if n else 0.0,
    }


def main() -> None:
    args = parse_args()
    groups: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    for path in args.result_files:
        for row in read_jsonl(path):
            key = (
                row.get("run_id"),
                row.get("task_id"),
                row.get("model"),
                row.get("provider"),
                row.get("k_shot"),
                row.get("seed"),
            )
            groups[key].append(row)

    summary_rows = [summarize_group(rows) for rows in groups.values()]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "run_id",
                "task_id",
                "model",
                "provider",
                "k",
                "seed",
                "n_test",
                "accuracy",
                "nonparseable_rate",
            ],
        )
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"Wrote {len(summary_rows)} summary rows to {args.output}")


if __name__ == "__main__":
    main()
