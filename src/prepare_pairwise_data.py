from __future__ import annotations

import argparse
from pathlib import Path

from .checks import format_data_report
from .io_utils import write_jsonl
from .pairwise import (
    DEFAULT_PAIRWISE_INPUT_FORMAT,
    available_pairwise_input_formats,
    build_pairwise_pool,
    format_pairwise_build_report,
)
from .tasks import (
    PoolConfig,
    available_pairwise_combination_rules,
    default_pool_path,
    get_task,
    load_processed_examples,
    make_pairwise_task_id,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare a pairwise transformed pool from an existing processed base-task pool."
        )
    )
    parser.add_argument("--base-task", required=True, help="Existing base task id.")
    parser.add_argument(
        "--combination-rule",
        choices=available_pairwise_combination_rules(),
        default="same",
        help=(
            "Boolean rule applied to the two base-task property values. "
            "`same` means Label A iff both items have the same base category."
        ),
    )
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--base-data-file",
        type=Path,
        default=None,
        help="Processed base pool JSONL. Defaults to data/processed/<base-task>/pool_seed<seed>.jsonl.",
    )
    parser.add_argument(
        "--pool-size",
        type=int,
        default=None,
        help="Total balanced pairwise rows. Defaults to the base task's default pool size.",
    )
    parser.add_argument(
        "--input-format",
        choices=available_pairwise_input_formats(),
        default=DEFAULT_PAIRWISE_INPUT_FORMAT,
        help="How the two source inputs are displayed inside the pairwise input.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output JSONL path. Defaults to data/processed/<pairwise-task>/pool_seed<seed>.jsonl.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base_task = get_task(args.base_task)
    pairwise_task_id = make_pairwise_task_id(base_task.task_id, args.combination_rule)
    pairwise_task = get_task(pairwise_task_id)

    base_data_file = args.base_data_file or default_pool_path(base_task.task_id, args.seed)
    if not base_data_file.exists():
        raise FileNotFoundError(
            f"Base data file not found: {base_data_file}. Prepare it first with "
            f"`python -m src.prepare_data --task {base_task.task_id} --seed {args.seed}`."
        )

    base_examples = load_processed_examples(base_data_file)
    config = PoolConfig(pool_size=args.pool_size or pairwise_task.default_pool_size)
    examples, report = build_pairwise_pool(
        base_examples,
        base_task_id=base_task.task_id,
        combination_rule=args.combination_rule,
        seed=args.seed,
        config=config,
        input_format=args.input_format,
    )
    output_path = args.output or default_pool_path(pairwise_task_id, args.seed)

    write_jsonl(output_path, [example.to_json() for example in examples])

    print(f"Wrote {len(examples)} examples to {output_path}")
    print()
    print(format_pairwise_build_report(report))
    print()
    print(format_data_report(examples, pairwise_task_id))


if __name__ == "__main__":
    main()
