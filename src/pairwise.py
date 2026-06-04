from __future__ import annotations

import json
import random
from collections import Counter
from dataclasses import dataclass

from .tasks import (
    Example,
    PAIRWISE_COMBINATION_RULES,
    PairwiseCombinationRule,
    PoolConfig,
    label_for_property,
    make_pairwise_task_id,
)


DEFAULT_PAIRWISE_INPUT_FORMAT = "plain_lines"
PAIRWISE_INPUT_FORMATS = ("plain_lines", "labeled_lines", "json_object")
PROPERTY_PAIRS = ((True, True), (True, False), (False, True), (False, False))


@dataclass(frozen=True)
class PairwiseBuildReport:
    task_id: str
    base_task_id: str
    combination_rule: str
    input_format: str
    pool_size: int
    source_examples: int
    source_property_counts: dict[bool, int]
    pair_property_counts: dict[bool, int]
    pair_type_counts: dict[str, int]


def available_pairwise_input_formats() -> list[str]:
    return sorted(PAIRWISE_INPUT_FORMATS)


def validate_pairwise_input_format(input_format: str) -> None:
    if input_format not in PAIRWISE_INPUT_FORMATS:
        available = ", ".join(available_pairwise_input_formats())
        raise ValueError(
            f"Unknown pairwise input format {input_format!r}. Available formats: {available}"
        )


def _indent_block(text: str) -> str:
    lines = text.splitlines() or [""]
    return "\n".join(f"  {line}" for line in lines)


def format_pairwise_input(left_input: str, right_input: str, input_format: str) -> str:
    validate_pairwise_input_format(input_format)
    if input_format == "plain_lines":
        return f"{left_input}\n{right_input}"
    if input_format == "json_object":
        return json.dumps(
            {"item_1": left_input, "item_2": right_input},
            ensure_ascii=False,
            sort_keys=True,
        )
    return (
        "Item 1:\n"
        f"{_indent_block(left_input)}\n\n"
        "Item 2:\n"
        f"{_indent_block(right_input)}"
    )


def _property_pair_key(left_property: bool, right_property: bool) -> str:
    return f"{int(left_property)}{int(right_property)}"


def _eligible_source_examples(
    base_examples: list[Example],
    base_task_id: str,
) -> list[Example]:
    source_examples = [example for example in base_examples if example.split == "pool"]
    if not source_examples:
        source_examples = list(base_examples)

    mismatched = sorted(
        {example.task_id for example in source_examples if example.task_id != base_task_id}
    )
    if mismatched:
        raise ValueError(
            f"Base data contains task ids other than {base_task_id!r}: {mismatched}"
        )

    return source_examples


def _allowed_property_pairs(
    combination_rule: PairwiseCombinationRule,
    desired_property_value: bool,
) -> list[tuple[bool, bool]]:
    return [
        pair
        for pair in PROPERTY_PAIRS
        if combination_rule.combine(pair[0], pair[1]) == desired_property_value
    ]


def _sample_pair(
    buckets: dict[bool, list[Example]],
    property_pair: tuple[bool, bool],
    rng: random.Random,
) -> tuple[Example, Example]:
    left_property, right_property = property_pair
    if left_property == right_property:
        if len(buckets[left_property]) < 2:
            raise ValueError(
                f"Need at least two source examples with property_value={left_property} "
                "to build pairwise examples."
            )
        left, right = rng.sample(buckets[left_property], 2)
    else:
        if not buckets[left_property] or not buckets[right_property]:
            raise ValueError(
                "Need source examples for both property values to build pairwise examples."
            )
        left = rng.choice(buckets[left_property])
        right = rng.choice(buckets[right_property])
    return left, right


def build_pairwise_pool(
    base_examples: list[Example],
    *,
    base_task_id: str,
    combination_rule: str,
    seed: int,
    config: PoolConfig,
    input_format: str = DEFAULT_PAIRWISE_INPUT_FORMAT,
) -> tuple[list[Example], PairwiseBuildReport]:
    validate_pairwise_input_format(input_format)
    if config.pool_size % 2:
        raise ValueError("Balanced pairwise pools require an even pool size.")
    if combination_rule not in PAIRWISE_COMBINATION_RULES:
        available = ", ".join(sorted(PAIRWISE_COMBINATION_RULES))
        raise ValueError(
            f"Unknown pairwise combination rule {combination_rule!r}. "
            f"Available rules: {available}"
        )

    task_id = make_pairwise_task_id(base_task_id, combination_rule)
    source_examples = _eligible_source_examples(base_examples, base_task_id)
    buckets: dict[bool, list[Example]] = {True: [], False: []}
    for example in source_examples:
        buckets[example.property_value].append(example)

    source_property_counts = {
        property_value: len(examples) for property_value, examples in buckets.items()
    }
    if not buckets[True] or not buckets[False]:
        raise ValueError(
            "Pairwise transforms need at least one positive and one negative source example. "
            f"Counts: {source_property_counts}"
        )

    rule = PAIRWISE_COMBINATION_RULES[combination_rule]
    allowed_pairs_by_value = {
        desired_value: _allowed_property_pairs(rule, desired_value)
        for desired_value in (True, False)
    }
    for desired_value, allowed_pairs in allowed_pairs_by_value.items():
        if not allowed_pairs:
            raise ValueError(
                f"Combination rule {combination_rule!r} cannot produce "
                f"property_value={desired_value}."
            )

    rng = random.Random(seed)
    desired_values = [True] * (config.pool_size // 2) + [False] * (config.pool_size // 2)
    rng.shuffle(desired_values)

    used_pair_ids: set[tuple[str, str]] = set()
    used_inputs: set[str] = set()
    pair_type_counts: Counter[str] = Counter()
    examples: list[Example] = []
    max_attempts = max(10_000, config.pool_size * 100)

    for pool_idx, desired_value in enumerate(desired_values):
        for _attempt in range(max_attempts):
            property_pair = rng.choice(allowed_pairs_by_value[desired_value])
            left, right = _sample_pair(buckets, property_pair, rng)
            pair_key = (left.example_id, right.example_id)
            if pair_key in used_pair_ids:
                continue

            pair_input = format_pairwise_input(left.input, right.input, input_format)
            if pair_input in used_inputs:
                continue

            used_pair_ids.add(pair_key)
            used_inputs.add(pair_input)
            pair_type_counts[_property_pair_key(*property_pair)] += 1
            examples.append(
                Example(
                    task_id=task_id,
                    example_id=f"{task_id}_pool_{pool_idx:04d}",
                    input=pair_input,
                    label=label_for_property(desired_value, config),
                    property_value=desired_value,
                    split="pool",
                    metadata={
                        "source": "pairwise_transform",
                        "seed": seed,
                        "base_task_id": base_task_id,
                        "combination_rule": combination_rule,
                        "combination_positive_rule": rule.positive_rule_text,
                        "combination_negative_rule": rule.negative_rule_text,
                        "input_format": input_format,
                        "left_example_id": left.example_id,
                        "right_example_id": right.example_id,
                        "left_input": left.input,
                        "right_input": right.input,
                        "left_label": left.label,
                        "right_label": right.label,
                        "left_property_value": left.property_value,
                        "right_property_value": right.property_value,
                        "property_pair": _property_pair_key(
                            left.property_value,
                            right.property_value,
                        ),
                    },
                )
            )
            break
        else:
            raise ValueError(
                f"Could not sample enough unique pairwise examples after {max_attempts} "
                f"attempts for desired property_value={desired_value}."
            )

    pair_property_counts = dict(Counter(example.property_value for example in examples))
    report = PairwiseBuildReport(
        task_id=task_id,
        base_task_id=base_task_id,
        combination_rule=combination_rule,
        input_format=input_format,
        pool_size=len(examples),
        source_examples=len(source_examples),
        source_property_counts=source_property_counts,
        pair_property_counts=pair_property_counts,
        pair_type_counts=dict(pair_type_counts),
    )
    return examples, report


def format_pairwise_build_report(report: PairwiseBuildReport) -> str:
    source_counts = ", ".join(
        f"{property_value}={count}"
        for property_value, count in sorted(report.source_property_counts.items())
    )
    pair_counts = ", ".join(
        f"{property_value}={count}"
        for property_value, count in sorted(report.pair_property_counts.items())
    )
    pair_type_counts = ", ".join(
        f"{pair_type}={count}" for pair_type, count in sorted(report.pair_type_counts.items())
    )
    return "\n".join(
        [
            "Pairwise transform report",
            f"  task_id: {report.task_id}",
            f"  base_task_id: {report.base_task_id}",
            f"  combination_rule: {report.combination_rule}",
            f"  input_format: {report.input_format}",
            f"  source_examples: {report.source_examples}",
            f"  source_property_counts: {source_counts}",
            f"  pair_property_counts: {pair_counts}",
            f"  pair_type_counts: {pair_type_counts}",
        ]
    )
