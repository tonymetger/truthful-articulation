from __future__ import annotations

from collections import Counter, defaultdict

from .tasks import Example


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def format_data_report(examples: list[Example], task_id: str) -> str:
    lines: list[str] = []
    lines.append(f"Data check for {task_id}")
    lines.append("")

    by_split_label = Counter((example.split, example.label) for example in examples)
    lines.append("Rows by split and label:")
    split_order = {"pool": 0, "fewshot_pool": 1, "dev": 2, "test": 3}
    splits = sorted(
        {example.split for example in examples},
        key=lambda split: (split_order.get(split, 99), split),
    )
    labels = sorted({example.label for example in examples})
    for split in splits:
        parts = [f"{label}={by_split_label[(split, label)]}" for label in labels]
        lines.append(f"  {split}: " + ", ".join(parts))

    inputs = [example.input for example in examples]
    duplicate_count = len(inputs) - len(set(inputs))
    lines.append(f"Duplicate input count across processed file: {duplicate_count}")
    lines.append("")

    source_counts = Counter(
        str(example.metadata.get("source", "unknown")) for example in examples
    )
    lines.append("Rows by metadata source:")
    for source, count in sorted(source_counts.items()):
        lines.append(f"  {source}: {count}")
    lines.append("")

    by_property: dict[bool, list[Example]] = defaultdict(list)
    for example in examples:
        by_property[example.property_value].append(example)

    for property_value, heading in (
        (True, "Positive/property_value=true"),
        (False, "Negative/property_value=false"),
    ):
        lines.append(f"{heading} examples:")
        for example in by_property[property_value][:5]:
            lines.append(f"  - [{example.split}/{example.label}] {example.input}")
        lines.append("")

    lines.append("Average input length by label:")
    for label in ("A", "B"):
        label_examples = [example for example in examples if example.label == label]
        avg_chars = _mean([len(example.input) for example in label_examples])
        avg_words = _mean([len(example.input.split()) for example in label_examples])
        lines.append(f"  {label}: {avg_chars:.1f} chars, {avg_words:.1f} words")
    lines.append("")

    lines.append("Leakage notes:")
    lines.append(
        "  - Classification prompts include only Input and Label fields for demonstrations."
    )
    lines.append("  - The task rule text is stored in code/metadata and is not inserted into prompts.")
    if task_id == "sst2_positive_sentiment":
        lines.append(
            "  - Sentiment-bearing words are the intended signal for this SST-2 baseline, not leakage."
        )
    elif task_id.startswith("trec_"):
        lines.append("  - Labels come from TREC question-type annotations.")
        lines.append("  - Question wording may reveal answer type, which is the intended semantic signal.")
    elif task_id.startswith("question_detection_"):
        lines.append("  - Positives come from TREC questions and negatives from SST-2 review sentences.")
        lines.append(
            "  - This is an MVP source/style confound; inspect no-punctuation results with that in mind."
        )
    elif task_id == "sentence_past_tense_main_verb":
        lines.append("  - Inputs come from Universal Dependencies English EWT.")
        lines.append(
            "  - Labels use UD annotations for the single finite VERB/AUX syntactic root."
        )
    elif task_id.startswith("controlled_sentence_"):
        lines.append("  - Inputs come from a controlled CSV supplied at the repository root.")
        lines.append(
            "  - Labels are stored in the CSV and validated where a deterministic surface labeler is available."
        )
    elif task_id in {"sentence_even_word_count", "sentence_second_word_contains_e"}:
        lines.append("  - Inputs come from the filtered Universal Dependencies English EWT pool.")
        lines.append(
            "  - Labels are derived from visible sentence form using the same tokenizer recorded in metadata."
        )
    elif task_id.startswith("sentence_"):
        lines.append("  - Inputs come from a shared real-sentence pool across labels.")
        lines.append("  - Labels are derived from sentence form rather than SST-2 sentiment.")
    elif task_id.startswith("camouflaged_"):
        lines.append("  - Inputs come from the filtered Universal Dependencies English EWT pool.")
        lines.append(
            "  - Labels are hidden surface rules over semantically rich real sentences."
        )
    elif task_id.startswith("pairwise_"):
        lines.append("  - Inputs are deterministic pairwise transforms of a processed base pool.")
        lines.append(
            "  - Each row records the source example IDs and source property values in metadata."
        )
    elif task_id == "random_starts_ends_same_char":
        lines.append("  - Inputs are synthetic lowercase strings with matched length ranges across labels.")
    elif task_id.startswith("random_"):
        lines.append("  - Inputs are synthetic strings with matched length ranges across labels.")
    elif task_id.startswith("json_"):
        lines.append("  - Inputs are synthetic JSON-like records with controlled field distributions.")
    elif task_id.startswith("product_code_"):
        lines.append("  - Inputs are synthetic product codes with controlled check digits.")
    elif task_id.startswith("pair_"):
        lines.append("  - Inputs contain two fields separated by `||`; labels depend on a relation.")
    else:
        lines.append("  - No task-specific leakage notes configured yet.")

    return "\n".join(lines)
