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
    SST2_RAW_PATH,
    TREC_RAW_PATH,
    UD_EWT_RAW_PATH,
    SplitConfig,
    default_pool_path,
    default_processed_path,
    ensure_sst2_raw,
    ensure_trec_raw,
    ensure_ud_english_ewt_raw,
    get_task,
    is_pairwise_task_id,
    load_processed_examples,
    make_task_dataset,
    make_task_pool,
    parse_pairwise_task_id,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare processed JSONL examples for a task."
    )
    parser.add_argument("--task", default="sst2_positive_sentiment", help="Task id to prepare.")
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed for pool or split construction.",
    )
    parser.add_argument(
        "--output-format",
        choices=("pool", "split"),
        default="pool",
        help=(
            "pool writes one balanced candidate pool; split writes the older "
            "fewshot/dev/test file."
        ),
    )
    parser.add_argument(
        "--pool-size",
        type=int,
        default=None,
        help="Total balanced examples in the candidate pool; defaults can vary by task.",
    )
    parser.add_argument("--fewshot-pool-size", type=int, default=100)
    parser.add_argument("--dev-size", type=int, default=50)
    parser.add_argument("--test-size", type=int, default=50)
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Processed JSONL output path.",
    )
    parser.add_argument(
        "--refresh-raw",
        action="store_true",
        help="Re-download/rebuild raw data cache.",
    )
    parser.add_argument(
        "--pairwise-base-data-file",
        type=Path,
        default=None,
        help=(
            "For pairwise task ids, optional processed base pool JSONL. Defaults "
            "to data/processed/<base-task>/pool_seed<seed>.jsonl."
        ),
    )
    parser.add_argument(
        "--pairwise-input-format",
        choices=available_pairwise_input_formats(),
        default=DEFAULT_PAIRWISE_INPUT_FORMAT,
        help="For pairwise task ids, how to display the two source examples.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    task = get_task(args.task)

    if is_pairwise_task_id(task.task_id):
        if args.output_format != "pool":
            raise ValueError("Pairwise transformed tasks currently support pool output only.")

        pairwise_parts = parse_pairwise_task_id(task.task_id)
        if pairwise_parts is None:
            raise ValueError(f"Could not parse pairwise task id {task.task_id!r}.")
        combination_rule, base_task_id = pairwise_parts
        base_data_file = args.pairwise_base_data_file or default_pool_path(
            base_task_id,
            args.seed,
        )
        if not base_data_file.exists():
            raise FileNotFoundError(
                f"Base data file not found: {base_data_file}. Prepare it first with "
                f"`python -m src.prepare_data --task {base_task_id} --seed {args.seed}`."
            )
        base_examples = load_processed_examples(base_data_file)
        config = PoolConfig(pool_size=args.pool_size or task.default_pool_size)
        examples, report = build_pairwise_pool(
            base_examples,
            base_task_id=base_task_id,
            combination_rule=combination_rule,
            seed=args.seed,
            config=config,
            input_format=args.pairwise_input_format,
        )
        output_path = args.output or default_pool_path(task.task_id, args.seed)
        write_jsonl(output_path, [example.to_json() for example in examples])

        print(f"Wrote {len(examples)} examples to {output_path}")
        print()
        print(format_pairwise_build_report(report))
        print()
        print(format_data_report(examples, task.task_id))
        return

    if task.task_id == "sst2_positive_sentiment":
        ensure_sst2_raw(SST2_RAW_PATH, refresh=args.refresh_raw)
    elif task.task_id in {
        "sentence_contains_digit",
        "sentence_has_long_word",
        "sentence_even_word_count",
        "sentence_second_word_contains_e",
        "sentence_contains_negation",
        "sentence_first_person_pronoun",
        "sentence_past_tense_main_verb",
        "camouflaged_second_word_longer_than_penultimate",
        "camouflaged_exactly_one_first3_contains_t",
        "pair_boundary_initial_match",
    }:
        ensure_ud_english_ewt_raw(UD_EWT_RAW_PATH, refresh=args.refresh_raw)
    elif task.task_id.startswith("trec_"):
        ensure_trec_raw(TREC_RAW_PATH, refresh=args.refresh_raw)
    elif task.task_id.startswith("question_detection_"):
        ensure_trec_raw(TREC_RAW_PATH, refresh=args.refresh_raw)
        ensure_sst2_raw(SST2_RAW_PATH, refresh=args.refresh_raw)

    if args.output_format == "pool":
        config = PoolConfig(pool_size=args.pool_size or task.default_pool_size)
        examples = make_task_pool(task.task_id, seed=args.seed, config=config)
        output_path = args.output or default_pool_path(task.task_id, args.seed)
    else:
        config = SplitConfig(
            fewshot_pool_size=args.fewshot_pool_size,
            dev_size=args.dev_size,
            test_size=args.test_size,
        )
        examples = make_task_dataset(task.task_id, seed=args.seed, config=config)
        output_path = args.output or default_processed_path(task.task_id, args.seed)

    write_jsonl(output_path, [example.to_json() for example in examples])

    print(f"Wrote {len(examples)} examples to {output_path}")
    print()
    print(format_data_report(examples, task.task_id))


if __name__ == "__main__":
    main()
