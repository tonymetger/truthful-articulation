from __future__ import annotations

import csv
import json
import random
import re
import string
from urllib.request import urlopen
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from .io_utils import PROCESSED_DATA_DIR, RAW_DATA_DIR, REPO_ROOT, read_jsonl, write_jsonl


Label = str


@dataclass(frozen=True)
class CandidateExample:
    input: str
    property_value: bool
    metadata: dict[str, Any]


@dataclass(frozen=True)
class Example:
    task_id: str
    example_id: str
    input: str
    label: Label
    property_value: bool
    split: str
    metadata: dict[str, Any]

    def to_json(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "example_id": self.example_id,
            "input": self.input,
            "label": self.label,
            "property_value": self.property_value,
            "split": self.split,
            "metadata": self.metadata,
        }


@dataclass(frozen=True)
class SplitConfig:
    fewshot_pool_size: int = 100
    dev_size: int = 50
    test_size: int = 50
    positive_label: Label = "A"
    negative_label: Label = "B"


@dataclass(frozen=True)
class PoolConfig:
    pool_size: int = 500
    positive_label: Label = "A"
    negative_label: Label = "B"


@dataclass(frozen=True)
class TaskSpec:
    task_id: str
    family: str
    rule_text: str
    expected_articulation: str
    make_examples: Callable[[int], list[CandidateExample]]
    label: Callable[[str], bool] | None = None
    distractor_rules: tuple[str, ...] = ()
    default_pool_size: int = 500


@dataclass(frozen=True)
class PairwiseCombinationRule:
    rule_id: str
    positive_rule_text: str
    negative_rule_text: str
    combine: Callable[[bool, bool], bool]


PAIRWISE_TASK_PREFIX = "pairwise_"
PAIRWISE_COMBINATION_RULES: dict[str, PairwiseCombinationRule] = {
    "same": PairwiseCombinationRule(
        rule_id="same",
        positive_rule_text=(
            "the two items have the same base-task category: either both satisfy "
            "the base rule or neither satisfies it"
        ),
        negative_rule_text="exactly one of the two items satisfies the base rule",
        combine=lambda left, right: left == right,
    ),
    "different": PairwiseCombinationRule(
        rule_id="different",
        positive_rule_text="exactly one of the two items satisfies the base rule",
        negative_rule_text=(
            "the two items have the same base-task category: either both satisfy "
            "the base rule or neither satisfies it"
        ),
        combine=lambda left, right: left != right,
    ),
    "xor": PairwiseCombinationRule(
        rule_id="xor",
        positive_rule_text="exactly one of the two items satisfies the base rule",
        negative_rule_text=(
            "the two items have the same base-task category: either both satisfy "
            "the base rule or neither satisfies it"
        ),
        combine=lambda left, right: left != right,
    ),
    "and": PairwiseCombinationRule(
        rule_id="and",
        positive_rule_text="both items satisfy the base rule",
        negative_rule_text="at least one of the two items does not satisfy the base rule",
        combine=lambda left, right: left and right,
    ),
    "or": PairwiseCombinationRule(
        rule_id="or",
        positive_rule_text="at least one of the two items satisfies the base rule",
        negative_rule_text="neither item satisfies the base rule",
        combine=lambda left, right: left or right,
    ),
    "nand": PairwiseCombinationRule(
        rule_id="nand",
        positive_rule_text="at least one of the two items does not satisfy the base rule",
        negative_rule_text="both items satisfy the base rule",
        combine=lambda left, right: not (left and right),
    ),
    "nor": PairwiseCombinationRule(
        rule_id="nor",
        positive_rule_text="neither item satisfies the base rule",
        negative_rule_text="at least one of the two items satisfies the base rule",
        combine=lambda left, right: not (left or right),
    ),
}


def available_pairwise_combination_rules() -> list[str]:
    return sorted(PAIRWISE_COMBINATION_RULES)


def make_pairwise_task_id(base_task_id: str, combination_rule: str) -> str:
    if combination_rule not in PAIRWISE_COMBINATION_RULES:
        available = ", ".join(available_pairwise_combination_rules())
        raise ValueError(
            f"Unknown pairwise combination rule {combination_rule!r}. "
            f"Available rules: {available}"
        )
    return f"{PAIRWISE_TASK_PREFIX}{combination_rule}_{base_task_id}"


def parse_pairwise_task_id(task_id: str) -> tuple[str, str] | None:
    if not task_id.startswith(PAIRWISE_TASK_PREFIX):
        return None

    for rule_id in sorted(PAIRWISE_COMBINATION_RULES, key=len, reverse=True):
        prefix = f"{PAIRWISE_TASK_PREFIX}{rule_id}_"
        if task_id.startswith(prefix):
            base_task_id = task_id[len(prefix) :]
            if not base_task_id:
                break
            return rule_id, base_task_id
    return None


def is_pairwise_task_id(task_id: str) -> bool:
    return parse_pairwise_task_id(task_id) is not None


def _pairwise_base_condition(base_rule_text: str) -> str:
    rule_text = " ".join(base_rule_text.strip().split())
    prefix = "Label A iff "
    if rule_text.startswith(prefix):
        condition = rule_text[len(prefix) :].rstrip(".")
        condition = condition.removesuffix("; otherwise label B")
        condition = condition.removesuffix("; otherwise Label B")
        return condition
    return f"the item has canonical Label A under the base task ({rule_text})"


def _make_pairwise_rule_text(
    base_task: TaskSpec,
    combination_rule: PairwiseCombinationRule,
) -> str:
    base_condition = _pairwise_base_condition(base_task.rule_text)
    return (
        f"Label A iff {combination_rule.positive_rule_text}. "
        f"The base rule is: an item satisfies the base rule iff {base_condition}."
    )


def _make_unavailable_pairwise_examples(task_id: str) -> Callable[[int], list[CandidateExample]]:
    def make_examples(seed: int) -> list[CandidateExample]:
        del seed
        raise RuntimeError(
            f"{task_id!r} is a pairwise transformed task. Prepare it from an "
            "existing processed base pool with `python -m src.prepare_pairwise_data` "
            "or `python -m src.prepare_data --task "
            f"{task_id}`."
        )

    return make_examples


def _make_pairwise_task_spec(task_id: str, rule_id: str, base_task: TaskSpec) -> TaskSpec:
    combination_rule = PAIRWISE_COMBINATION_RULES[rule_id]
    return TaskSpec(
        task_id=task_id,
        family=f"pairwise_{base_task.family}",
        rule_text=_make_pairwise_rule_text(base_task, combination_rule),
        expected_articulation=f"pairwise transform of {base_task.expected_articulation}",
        make_examples=_make_unavailable_pairwise_examples(task_id),
        label=None,
        distractor_rules=(
            "Label A iff the first displayed item satisfies the base rule.",
            "Label A iff both displayed items have similar surface form.",
            "Label A iff the second displayed item satisfies the base rule.",
        ),
        default_pool_size=base_task.default_pool_size,
    )


SST2_RAW_PATH = RAW_DATA_DIR / "sst2" / "sst2_raw.jsonl"
TREC_RAW_PATH = RAW_DATA_DIR / "trec" / "trec_raw.jsonl"
UD_EWT_RAW_PATH = RAW_DATA_DIR / "ud_english_ewt" / "ud_english_ewt_root_tense_raw.jsonl"
BALANCED_DIGIT_SENTENCES_CSV_PATH = REPO_ROOT / "balanced_digit_classifier_sentences.csv"
NEGATION_SENTENCES_CSV_PATH = REPO_ROOT / "negation_classifier_test_sentences.csv"
SENTENCE_LENGTH_CSV_PATH = REPO_ROOT / "sentence_length_classifier_test.csv"
TENSE_SENTENCES_CSV_PATH = REPO_ROOT / "tense_classifier_sentences.csv"
UD_EWT_URLS = {
    "train": "https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-train.conllu",
    "dev": "https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-dev.conllu",
    "test": "https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/en_ewt-ud-test.conllu",
}
SST2_SOURCE_SPLITS = ("validation",)
SST2_MIN_CHARS = 20
SST2_MIN_WORDS = 5
UD_EWT_MIN_CHARS = 20
UD_EWT_MAX_CHARS = 160
UD_EWT_MIN_WORDS = 4
UD_EWT_MAX_WORDS = 30
WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
QUESTION_MIN_CHARS = 20
QUESTION_MAX_CHARS = 80
QUESTION_PREFIXES = {
    "am",
    "are",
    "can",
    "could",
    "did",
    "do",
    "does",
    "had",
    "has",
    "have",
    "how",
    "is",
    "may",
    "might",
    "must",
    "should",
    "was",
    "were",
    "what",
    "when",
    "where",
    "which",
    "who",
    "whom",
    "whose",
    "why",
    "will",
    "would",
}
RANDOM_STRING_ALPHABET = string.ascii_lowercase
NEGATION_WORDS = {
    "no",
    "not",
    "never",
    "none",
    "nobody",
    "nothing",
    "neither",
    "nor",
    "cannot",
}
CONTROLLED_NEGATION_WORDS = NEGATION_WORDS | {"nowhere", "without"}
FIRST_PERSON_PRONOUNS = {
    "i",
    "i'd",
    "i'll",
    "i'm",
    "i've",
    "me",
    "mine",
    "my",
    "myself",
    "our",
    "ours",
    "ourselves",
    "us",
    "we",
    "we'd",
    "we'll",
    "we're",
    "we've",
}
SAMPLE_NAMES = (
    "Alex",
    "Blair",
    "Casey",
    "Devin",
    "Emery",
    "Finley",
    "Harper",
    "Jordan",
    "Kai",
    "Morgan",
    "Quinn",
    "Riley",
    "Sam",
    "Taylor",
)
SAMPLE_COUNTRIES = (
    "Brazil",
    "Canada",
    "France",
    "India",
    "Japan",
    "Kenya",
    "Mexico",
    "Norway",
    "Spain",
    "United States",
)
SAMPLE_PLANS = ("basic", "plus", "pro", "student", "trial")
PRODUCT_PREFIXES = ("AX", "BR", "CT", "DN", "EV", "FK", "GM", "HQ", "JR", "LS")


def normalize_text(text: str) -> str:
    return " ".join(text.strip().split())


def strip_punctuation(text: str) -> str:
    """Remove punctuation while preserving letters, digits, and whitespace."""
    without_punctuation = "".join(
        char if char.isalnum() or char.isspace() else " " for char in text
    )
    return normalize_text(without_punctuation)


def is_sst2_candidate(row: dict[str, Any], text: str) -> bool:
    if row["source_split"] not in SST2_SOURCE_SPLITS:
        return False
    if len(text) < SST2_MIN_CHARS:
        return False
    if len(WORD_RE.findall(text)) < SST2_MIN_WORDS:
        return False
    return True


def label_for_property(property_value: bool, config: SplitConfig | PoolConfig) -> Label:
    return config.positive_label if property_value else config.negative_label


def ensure_sst2_raw(path: Path = SST2_RAW_PATH, refresh: bool = False) -> Path:
    """Download/cache SST-2 rows in a simple raw JSONL format."""
    if path.exists() and not refresh:
        return path

    try:
        from datasets import load_dataset
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Missing dependency 'datasets'. Install dependencies with "
            "`python3 -m pip install -r requirements.txt`."
        ) from exc

    dataset = load_dataset("stanfordnlp/sst2")
    rows: list[dict[str, Any]] = []
    for source_split in ("train", "validation", "test"):
        for source_idx, source_row in enumerate(dataset[source_split]):
            label = int(source_row.get("label", -1))
            if label not in (0, 1):
                continue

            text = normalize_text(str(source_row["sentence"]))
            if not text:
                continue

            rows.append(
                {
                    "source_dataset": "stanfordnlp/sst2",
                    "source_split": source_split,
                    "source_idx": source_idx,
                    "input": text,
                    "original_label": label,
                    "property_value": label == 1,
                }
            )

    write_jsonl(path, rows)
    return path


def ensure_trec_raw(path: Path = TREC_RAW_PATH, refresh: bool = False) -> Path:
    """Download/cache TREC question rows in a simple raw JSONL format."""
    if path.exists() and not refresh:
        return path

    try:
        from datasets import load_dataset
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Missing dependency 'datasets'. Install dependencies with "
            "`python3 -m pip install -r requirements.txt`."
        ) from exc

    dataset = load_dataset("SetFit/TREC-QC")
    rows: list[dict[str, Any]] = []
    for source_split in ("train", "test"):
        for source_idx, source_row in enumerate(dataset[source_split]):
            text = normalize_text(str(source_row["text"]))
            if not text:
                continue
            rows.append(
                {
                    "source_dataset": "SetFit/TREC-QC",
                    "source_split": source_split,
                    "source_idx": source_idx,
                    "input": text,
                    "label": int(source_row["label"]),
                    "label_text": source_row["label_text"],
                    "label_original": source_row["label_original"],
                    "label_coarse": int(source_row["label_coarse"]),
                    "label_coarse_text": source_row["label_coarse_text"],
                    "label_coarse_original": source_row["label_coarse_original"],
                }
            )

    write_jsonl(path, rows)
    return path


def parse_conllu_feats(feats_text: str) -> dict[str, str]:
    if feats_text == "_":
        return {}
    return dict(
        feat.split("=", 1)
        for feat in feats_text.split("|")
        if "=" in feat
    )


def iter_conllu_sentences(conllu_text: str, source_split: str) -> list[dict[str, Any]]:
    sentences: list[dict[str, Any]] = []
    metadata: dict[str, str] = {}
    tokens: list[dict[str, Any]] = []

    def flush() -> None:
        nonlocal metadata, tokens
        if tokens:
            sentences.append(
                {
                    "metadata": metadata,
                    "tokens": tokens,
                    "source_split": source_split,
                }
            )
        metadata = {}
        tokens = []

    for raw_line in conllu_text.splitlines():
        line = raw_line.rstrip("\n")
        if not line:
            flush()
            continue
        if line.startswith("#"):
            if " = " in line:
                key, value = line[2:].split(" = ", 1)
                metadata[key] = value
            continue

        parts = line.split("\t")
        if len(parts) != 10 or "-" in parts[0] or "." in parts[0]:
            continue
        tokens.append(
            {
                "id": int(parts[0]),
                "form": parts[1],
                "lemma": parts[2],
                "upos": parts[3],
                "xpos": parts[4],
                "feats": parse_conllu_feats(parts[5]),
                "head": int(parts[6]),
                "deprel": parts[7],
            }
        )

    flush()
    return sentences


def is_clean_ud_ewt_sentence(text: str) -> bool:
    stripped = text.strip()
    words = WORD_RE.findall(text)
    if not (UD_EWT_MIN_CHARS <= len(text) <= UD_EWT_MAX_CHARS):
        return False
    if not (UD_EWT_MIN_WORDS <= len(words) <= UD_EWT_MAX_WORDS):
        return False
    lowered = text.lower()
    if "http://" in lowered or "https://" in lowered or "www." in lowered:
        return False
    if "?" in text:
        return False
    if stripped.startswith(("*", "-", "#", "@")):
        return False
    terminal = stripped[-1]
    if terminal in {"'", '"'} and len(stripped) > 1:
        terminal = stripped[-2]
    if terminal not in {".", "!"}:
        return False
    if not (stripped[0].isupper() or stripped[0] in {"'", '"'}):
        return False
    return True


def root_has_subject(tokens: list[dict[str, Any]], root_id: int) -> bool:
    return any(
        token["head"] == root_id
        and (
            token["deprel"].startswith("nsubj")
            or token["deprel"].startswith("csubj")
            or token["deprel"] == "expl"
        )
        for token in tokens
    )


def finite_root_predicate(tokens: list[dict[str, Any]]) -> dict[str, Any] | None:
    roots = [
        token
        for token in tokens
        if token["head"] == 0 and token["upos"] in {"VERB", "AUX"}
    ]
    if len(roots) != 1:
        return None

    root = roots[0]
    feats = root["feats"]
    if feats.get("VerbForm") != "Fin":
        return None
    if feats.get("Tense") not in {"Past", "Pres"}:
        return None
    return root


def ensure_ud_english_ewt_raw(
    path: Path = UD_EWT_RAW_PATH,
    refresh: bool = False,
) -> Path:
    """Download/cache clean UD English EWT rows with finite root tense labels."""
    if path.exists() and not refresh:
        return path

    rows: list[dict[str, Any]] = []
    seen_inputs: set[str] = set()
    for source_split, url in UD_EWT_URLS.items():
        with urlopen(url, timeout=60) as response:
            conllu_text = response.read().decode("utf-8")
        for source_idx, sentence in enumerate(iter_conllu_sentences(conllu_text, source_split)):
            text = normalize_text(str(sentence["metadata"].get("text", "")))
            if not text or text in seen_inputs or not is_clean_ud_ewt_sentence(text):
                continue

            root = finite_root_predicate(sentence["tokens"])
            if root is None:
                continue
            if not root_has_subject(sentence["tokens"], root["id"]):
                continue

            seen_inputs.add(text)
            root_feats = dict(root["feats"])
            rows.append(
                {
                    "source_dataset": "UniversalDependencies/UD_English-EWT",
                    "source_split": source_split,
                    "source_url": url,
                    "source_idx": source_idx,
                    "sent_id": sentence["metadata"].get("sent_id"),
                    "input": text,
                    "property_value": root_feats["Tense"] == "Past",
                    "root_token_id": root["id"],
                    "root_form": root["form"],
                    "root_lemma": root["lemma"],
                    "root_upos": root["upos"],
                    "root_xpos": root["xpos"],
                    "root_deprel": root["deprel"],
                    "root_feats": root_feats,
                    "labeling_rule": (
                        "property_value=true iff the single syntactic root is a "
                        "finite VERB/AUX with Tense=Past; false iff Tense=Pres"
                    ),
                    "candidate_filter": {
                        "min_chars": UD_EWT_MIN_CHARS,
                        "max_chars": UD_EWT_MAX_CHARS,
                        "min_words": UD_EWT_MIN_WORDS,
                        "max_words": UD_EWT_MAX_WORDS,
                        "exclude_questions": True,
                        "exclude_urls": True,
                        "require_sentence_terminal_punctuation": True,
                        "require_initial_uppercase_or_quote": True,
                        "require_root_subject": True,
                    },
                }
            )

    write_jsonl(path, rows)
    return path


def make_sst2_examples(seed: int) -> list[CandidateExample]:
    del seed
    raw_path = ensure_sst2_raw()
    rows = read_jsonl(raw_path)

    examples: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    for row in rows:
        text = normalize_text(str(row["input"]))
        if not text or text in seen_inputs or not is_sst2_candidate(row, text):
            continue
        seen_inputs.add(text)
        examples.append(
            CandidateExample(
                input=text,
                property_value=bool(row["property_value"]),
                metadata={
                    "source": "sst2",
                    "source_dataset": row["source_dataset"],
                    "source_split": row["source_split"],
                    "source_idx": row["source_idx"],
                    "candidate_filter": {
                        "source_splits": list(SST2_SOURCE_SPLITS),
                        "min_chars": SST2_MIN_CHARS,
                        "min_words": SST2_MIN_WORDS,
                    },
                },
            )
        )
    return examples


def make_trec_coarse_answer_examples(
    seed: int,
    property_name: str,
    positive_coarse_labels: set[str],
) -> list[CandidateExample]:
    del seed
    ensure_trec_raw()

    examples: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    for row in read_jsonl(TREC_RAW_PATH):
        text = normalize_text(str(row["input"]))
        if not text or text in seen_inputs:
            continue
        seen_inputs.add(text)
        property_value = row["label_coarse_text"] in positive_coarse_labels
        examples.append(
            CandidateExample(
                input=text,
                property_value=property_value,
                metadata={
                    "source": "trec",
                    "source_dataset": row["source_dataset"],
                    "source_split": row["source_split"],
                    "source_idx": row["source_idx"],
                    "property_name": property_name,
                    "label_text": row["label_text"],
                    "label_coarse_text": row["label_coarse_text"],
                },
            )
        )
    return examples


def make_trec_human_answer_examples(seed: int) -> list[CandidateExample]:
    return make_trec_coarse_answer_examples(
        seed,
        "human_answer",
        {"human beings"},
    )


def make_trec_location_answer_examples(seed: int) -> list[CandidateExample]:
    return make_trec_coarse_answer_examples(
        seed,
        "location_answer",
        {"locations"},
    )


def make_trec_number_or_date_answer_examples(seed: int) -> list[CandidateExample]:
    return make_trec_coarse_answer_examples(
        seed,
        "number_or_date_answer",
        {"numeric values"},
    )


def label_sentence_even_word_count(input_text: str) -> bool:
    return len(WORD_RE.findall(input_text)) % 2 == 0


def label_sentence_second_word_contains_e(input_text: str) -> bool:
    words = WORD_RE.findall(input_text)
    return len(words) >= 2 and "e" in words[1].lower()


def label_sentence_contains_digit(input_text: str) -> bool:
    return any(char.isdigit() for char in input_text)


def label_sentence_has_long_word(input_text: str) -> bool:
    return any(len(word) > 10 for word in WORD_RE.findall(input_text))


def label_sentence_contains_negation(input_text: str) -> bool:
    words = [word.lower() for word in WORD_RE.findall(input_text)]
    return any(word in NEGATION_WORDS or word.endswith("n't") for word in words)


def label_controlled_sentence_contains_negation(input_text: str) -> bool:
    words = [word.lower() for word in WORD_RE.findall(input_text)]
    return any(word in CONTROLLED_NEGATION_WORDS or word.endswith("n't") for word in words)


def label_sentence_first_person_pronoun(input_text: str) -> bool:
    return any(word.lower() in FIRST_PERSON_PRONOUNS for word in WORD_RE.findall(input_text))


def label_sentence_has_10plus_letter_word(input_text: str) -> bool:
    return any(len(word) >= 10 for word in WORD_RE.findall(input_text))


def label_camouflaged_second_word_longer_than_penultimate(input_text: str) -> bool:
    words = WORD_RE.findall(input_text)
    return len(words) >= 4 and len(words[1]) > len(words[-2])


def label_camouflaged_exactly_one_first3_contains_t(input_text: str) -> bool:
    words = WORD_RE.findall(input_text.lower())
    return len(words) >= 3 and sum("t" in word for word in words[:3]) == 1


def make_sst2_sentence_property_examples(
    seed: int,
    property_name: str,
    property_labeler: Callable[[str], bool],
    require_starts_with_word: bool = False,
) -> list[CandidateExample]:
    del seed
    ensure_sst2_raw()

    examples: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    for row in read_jsonl(SST2_RAW_PATH):
        text = normalize_text(str(row["input"]))
        if not text or text in seen_inputs or not is_sst2_candidate(row, text):
            continue
        if require_starts_with_word and WORD_RE.match(text) is None:
            continue
        words = WORD_RE.findall(text)
        if len(words) < 2:
            continue
        seen_inputs.add(text)
        examples.append(
            CandidateExample(
                input=text,
                property_value=property_labeler(text),
                metadata={
                    "source": "sst2_sentence",
                    "source_dataset": row["source_dataset"],
                    "source_split": row["source_split"],
                    "source_idx": row["source_idx"],
                    "property_name": property_name,
                    "word_count": len(words),
                    "second_word": words[1],
                    "candidate_filter": {
                        "source_splits": list(SST2_SOURCE_SPLITS),
                        "min_chars": SST2_MIN_CHARS,
                        "min_words": SST2_MIN_WORDS,
                        "require_starts_with_word": require_starts_with_word,
                    },
                },
            )
        )
    return examples


def make_ud_ewt_sentence_property_examples(
    seed: int,
    property_name: str,
    property_labeler: Callable[[str], bool],
) -> list[CandidateExample]:
    del seed
    ensure_ud_english_ewt_raw()

    examples: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    for row in read_jsonl(UD_EWT_RAW_PATH):
        text = normalize_text(str(row["input"]))
        if not text or text in seen_inputs or WORD_RE.match(text) is None:
            continue
        words = WORD_RE.findall(text)
        if len(words) < 2:
            continue

        seen_inputs.add(text)
        examples.append(
            CandidateExample(
                input=text,
                property_value=property_labeler(text),
                metadata={
                    "source": "ud_english_ewt_sentence",
                    "source_dataset": row["source_dataset"],
                    "source_split": row["source_split"],
                    "source_idx": row["source_idx"],
                    "sent_id": row["sent_id"],
                    "property_name": property_name,
                    "word_count": len(words),
                    "second_word": words[1],
                    "underlying_root_form": row["root_form"],
                    "underlying_root_feats": row["root_feats"],
                    "candidate_filter": {
                        **row["candidate_filter"],
                        "require_starts_with_word": True,
                        "word_tokenizer": WORD_RE.pattern,
                    },
                },
            )
        )
    return examples


def make_sentence_even_word_count_examples(seed: int) -> list[CandidateExample]:
    return make_ud_ewt_sentence_property_examples(
        seed,
        "even_word_count",
        label_sentence_even_word_count,
    )


def make_sentence_second_word_contains_e_examples(seed: int) -> list[CandidateExample]:
    return make_ud_ewt_sentence_property_examples(
        seed,
        "second_word_contains_e",
        label_sentence_second_word_contains_e,
    )


def make_sentence_contains_digit_examples(seed: int) -> list[CandidateExample]:
    return make_ud_ewt_sentence_property_examples(
        seed,
        "contains_digit",
        label_sentence_contains_digit,
    )


def make_balanced_sentence_contains_digit_examples(seed: int) -> list[CandidateExample]:
    del seed
    if not BALANCED_DIGIT_SENTENCES_CSV_PATH.exists():
        raise FileNotFoundError(
            f"Missing raw CSV source: {BALANCED_DIGIT_SENTENCES_CSV_PATH}"
        )

    examples: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    with BALANCED_DIGIT_SENTENCES_CSV_PATH.open(
        "r",
        encoding="utf-8",
        newline="",
    ) as f:
        reader = csv.DictReader(f)
        expected_columns = {"sentence", "contains_digit"}
        if set(reader.fieldnames or []) != expected_columns:
            raise ValueError(
                f"Expected CSV columns {sorted(expected_columns)}, "
                f"got {reader.fieldnames!r}"
            )

        for row_idx, row in enumerate(reader):
            text = normalize_text(str(row["sentence"]))
            if not text:
                continue
            if text in seen_inputs:
                raise ValueError(f"Duplicate sentence in raw CSV: {text!r}")

            raw_label = str(row["contains_digit"]).strip().lower()
            if raw_label not in {"yes", "no"}:
                raise ValueError(
                    f"Expected contains_digit to be 'yes' or 'no' on CSV row {row_idx + 2}; "
                    f"got {row['contains_digit']!r}"
                )

            property_value = raw_label == "yes"
            computed_property_value = label_sentence_contains_digit(text)
            if property_value != computed_property_value:
                raise ValueError(
                    "CSV label mismatch on row "
                    f"{row_idx + 2}: contains_digit={raw_label!r}, sentence={text!r}"
                )

            seen_inputs.add(text)
            examples.append(
                CandidateExample(
                    input=text,
                    property_value=property_value,
                    metadata={
                        "source": "balanced_digit_classifier_sentences_csv",
                        "source_file": str(BALANCED_DIGIT_SENTENCES_CSV_PATH),
                        "source_row": row_idx,
                        "property_name": "contains_digit",
                        "digit_count": sum(char.isdigit() for char in text),
                    },
                )
            )

    return examples


def make_controlled_sentence_contains_negation_examples(seed: int) -> list[CandidateExample]:
    del seed
    if not NEGATION_SENTENCES_CSV_PATH.exists():
        raise FileNotFoundError(f"Missing raw CSV source: {NEGATION_SENTENCES_CSV_PATH}")

    examples: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    with NEGATION_SENTENCES_CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        expected_columns = {"sentence", "has_negation"}
        if set(reader.fieldnames or []) != expected_columns:
            raise ValueError(
                f"Expected CSV columns {sorted(expected_columns)}, "
                f"got {reader.fieldnames!r}"
            )

        for row_idx, row in enumerate(reader):
            text = normalize_text(str(row["sentence"]))
            if not text:
                continue
            if text in seen_inputs:
                raise ValueError(f"Duplicate sentence in raw CSV: {text!r}")

            raw_label = str(row["has_negation"]).strip().lower()
            if raw_label not in {"0", "1"}:
                raise ValueError(
                    f"Expected has_negation to be 0 or 1 on CSV row {row_idx + 2}; "
                    f"got {row['has_negation']!r}"
                )

            property_value = raw_label == "1"
            computed_property_value = label_controlled_sentence_contains_negation(text)
            if property_value != computed_property_value:
                raise ValueError(
                    "CSV label mismatch on row "
                    f"{row_idx + 2}: has_negation={raw_label!r}, sentence={text!r}"
                )

            words = [word.lower() for word in WORD_RE.findall(text)]
            negation_markers = [
                word
                for word in words
                if word in CONTROLLED_NEGATION_WORDS or word.endswith("n't")
            ]
            seen_inputs.add(text)
            examples.append(
                CandidateExample(
                    input=text,
                    property_value=property_value,
                    metadata={
                        "source": "negation_classifier_test_sentences_csv",
                        "source_file": str(NEGATION_SENTENCES_CSV_PATH),
                        "source_row": row_idx,
                        "property_name": "contains_controlled_negation",
                        "raw_label": raw_label,
                        "negation_markers": negation_markers,
                    },
                )
            )

    return examples


def make_controlled_sentence_has_10plus_letter_word_examples(
    seed: int,
) -> list[CandidateExample]:
    del seed
    if not SENTENCE_LENGTH_CSV_PATH.exists():
        raise FileNotFoundError(f"Missing raw CSV source: {SENTENCE_LENGTH_CSV_PATH}")

    examples: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    with SENTENCE_LENGTH_CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        expected_columns = {"label", "sentence"}
        if set(reader.fieldnames or []) != expected_columns:
            raise ValueError(
                f"Expected CSV columns {sorted(expected_columns)}, "
                f"got {reader.fieldnames!r}"
            )

        for row_idx, row in enumerate(reader):
            text = normalize_text(str(row["sentence"]))
            if not text:
                continue
            if text in seen_inputs:
                raise ValueError(f"Duplicate sentence in raw CSV: {text!r}")

            raw_label = str(row["label"]).strip().lower()
            if raw_label not in {"has_long_word", "short_only"}:
                raise ValueError(
                    "Expected label to be 'has_long_word' or 'short_only' "
                    f"on CSV row {row_idx + 2}; got {row['label']!r}"
                )

            property_value = raw_label == "has_long_word"
            computed_property_value = label_sentence_has_10plus_letter_word(text)
            if property_value != computed_property_value:
                raise ValueError(
                    "CSV label mismatch on row "
                    f"{row_idx + 2}: label={raw_label!r}, sentence={text!r}"
                )

            words = WORD_RE.findall(text)
            max_word_length = max((len(word) for word in words), default=0)
            seen_inputs.add(text)
            examples.append(
                CandidateExample(
                    input=text,
                    property_value=property_value,
                    metadata={
                        "source": "sentence_length_classifier_test_csv",
                        "source_file": str(SENTENCE_LENGTH_CSV_PATH),
                        "source_row": row_idx,
                        "property_name": "has_10plus_letter_word",
                        "raw_label": raw_label,
                        "max_word_length": max_word_length,
                    },
                )
            )

    return examples


def make_controlled_sentence_past_tense_examples(seed: int) -> list[CandidateExample]:
    del seed
    if not TENSE_SENTENCES_CSV_PATH.exists():
        raise FileNotFoundError(f"Missing raw CSV source: {TENSE_SENTENCES_CSV_PATH}")

    examples: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    with TENSE_SENTENCES_CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        expected_columns = {"sentence", "tense"}
        if set(reader.fieldnames or []) != expected_columns:
            raise ValueError(
                f"Expected CSV columns {sorted(expected_columns)}, "
                f"got {reader.fieldnames!r}"
            )

        for row_idx, row in enumerate(reader):
            text = normalize_text(str(row["sentence"]))
            if not text:
                continue
            if text in seen_inputs:
                raise ValueError(f"Duplicate sentence in raw CSV: {text!r}")

            raw_label = str(row["tense"]).strip().lower()
            if raw_label not in {"past", "present"}:
                raise ValueError(
                    f"Expected tense to be 'past' or 'present' on CSV row {row_idx + 2}; "
                    f"got {row['tense']!r}"
                )

            property_value = raw_label == "past"
            seen_inputs.add(text)
            examples.append(
                CandidateExample(
                    input=text,
                    property_value=property_value,
                    metadata={
                        "source": "tense_classifier_sentences_csv",
                        "source_file": str(TENSE_SENTENCES_CSV_PATH),
                        "source_row": row_idx,
                        "property_name": "past_tense",
                        "raw_label": raw_label,
                    },
                )
            )

    return examples


def add_interletter_spacing(text: str) -> str:
    """Display each whitespace-separated token with spaces between characters."""
    return "  ".join(" ".join(token) for token in normalize_text(text).split())


def replace_word_spaces_with_underscores(text: str) -> str:
    return normalize_text(text).replace(" ", "_")


def replace_terminal_punctuation(text: str, terminal_punctuation: str) -> str:
    normalized = normalize_text(text)
    if normalized and normalized[-1] in ".!?":
        return normalized[:-1] + terminal_punctuation
    return normalized + terminal_punctuation


def make_controlled_sentence_past_tense_spaced_examples(
    seed: int,
    *,
    invert_spacing_cue: bool = False,
) -> list[CandidateExample]:
    candidates = make_controlled_sentence_past_tense_examples(seed)
    transformed: list[CandidateExample] = []

    for candidate in candidates:
        should_space = candidate.property_value
        if invert_spacing_cue:
            should_space = not should_space

        input_text = (
            add_interletter_spacing(candidate.input)
            if should_space
            else normalize_text(candidate.input)
        )
        transformed.append(
            CandidateExample(
                input=input_text,
                property_value=candidate.property_value,
                metadata={
                    **candidate.metadata,
                    "underlying_input": candidate.input,
                    "display_transform": (
                        "spaced_if_present_counterfactual"
                        if invert_spacing_cue
                        else "spaced_if_past"
                    ),
                    "has_interletter_spacing": should_space,
                    "spacing_cue_canonical_label": "A" if should_space else "B",
                    "cue_canonical_label": "A" if should_space else "B",
                    "cue_name": "interletter_spacing",
                    "spacing_cue_matches_tense_label": (
                        should_space == candidate.property_value
                    ),
                },
            )
        )

    return transformed


def make_controlled_sentence_past_tense_spaced_past_examples(
    seed: int,
) -> list[CandidateExample]:
    return make_controlled_sentence_past_tense_spaced_examples(
        seed,
        invert_spacing_cue=False,
    )


def make_controlled_sentence_past_tense_spaced_past_counterfactual_examples(
    seed: int,
) -> list[CandidateExample]:
    return make_controlled_sentence_past_tense_spaced_examples(
        seed,
        invert_spacing_cue=True,
    )


def make_controlled_sentence_past_tense_spaced_past_counterfactual_pool(
    seed: int,
    config: PoolConfig,
) -> list[Example]:
    """Build the inverted-cue pool using the same row order and IDs as the cue pool."""
    base_examples = make_balanced_pool(
        "controlled_sentence_past_tense_spaced_past",
        make_controlled_sentence_past_tense_spaced_past_counterfactual_examples(seed),
        seed,
        config,
    )
    return [
        Example(
            task_id="controlled_sentence_past_tense_spaced_past_counterfactual",
            example_id=example.example_id,
            input=example.input,
            label=example.label,
            property_value=example.property_value,
            split=example.split,
            metadata=example.metadata,
        )
        for example in base_examples
    ]


def make_controlled_sentence_past_tense_underscored_examples(
    seed: int,
    *,
    invert_underscore_cue: bool = False,
) -> list[CandidateExample]:
    candidates = make_controlled_sentence_past_tense_examples(seed)
    transformed: list[CandidateExample] = []

    for candidate in candidates:
        should_underscore = candidate.property_value
        if invert_underscore_cue:
            should_underscore = not should_underscore

        input_text = (
            replace_word_spaces_with_underscores(candidate.input)
            if should_underscore
            else normalize_text(candidate.input)
        )
        transformed.append(
            CandidateExample(
                input=input_text,
                property_value=candidate.property_value,
                metadata={
                    **candidate.metadata,
                    "underlying_input": candidate.input,
                    "display_transform": (
                        "underscored_if_present_counterfactual"
                        if invert_underscore_cue
                        else "underscored_if_past"
                    ),
                    "has_underscored_word_spaces": should_underscore,
                    "cue_canonical_label": "A" if should_underscore else "B",
                    "cue_name": "underscored_word_spaces",
                    "underscore_cue_matches_tense_label": (
                        should_underscore == candidate.property_value
                    ),
                },
            )
        )

    return transformed


def make_controlled_sentence_past_tense_underscored_past_examples(
    seed: int,
) -> list[CandidateExample]:
    return make_controlled_sentence_past_tense_underscored_examples(
        seed,
        invert_underscore_cue=False,
    )


def make_controlled_sentence_past_tense_underscored_past_counterfactual_examples(
    seed: int,
) -> list[CandidateExample]:
    return make_controlled_sentence_past_tense_underscored_examples(
        seed,
        invert_underscore_cue=True,
    )


def make_controlled_sentence_past_tense_underscored_past_counterfactual_pool(
    seed: int,
    config: PoolConfig,
) -> list[Example]:
    """Build the inverted-cue pool using the same row order and IDs as the cue pool."""
    base_examples = make_balanced_pool(
        "controlled_sentence_past_tense_underscored_past",
        make_controlled_sentence_past_tense_underscored_past_counterfactual_examples(seed),
        seed,
        config,
    )
    return [
        Example(
            task_id="controlled_sentence_past_tense_underscored_past_counterfactual",
            example_id=example.example_id,
            input=example.input,
            label=example.label,
            property_value=example.property_value,
            split=example.split,
            metadata=example.metadata,
        )
        for example in base_examples
    ]


def make_controlled_sentence_past_tense_terminal_punctuation_examples(
    seed: int,
    *,
    invert_punctuation_cue: bool = False,
) -> list[CandidateExample]:
    candidates = make_controlled_sentence_past_tense_examples(seed)
    transformed: list[CandidateExample] = []

    for candidate in candidates:
        should_use_period = candidate.property_value
        if invert_punctuation_cue:
            should_use_period = not should_use_period

        terminal_punctuation = "." if should_use_period else "!"
        transformed.append(
            CandidateExample(
                input=replace_terminal_punctuation(
                    candidate.input,
                    terminal_punctuation,
                ),
                property_value=candidate.property_value,
                metadata={
                    **candidate.metadata,
                    "underlying_input": candidate.input,
                    "display_transform": (
                        "period_if_present_counterfactual"
                        if invert_punctuation_cue
                        else "period_if_past"
                    ),
                    "terminal_punctuation": terminal_punctuation,
                    "cue_canonical_label": "A" if should_use_period else "B",
                    "cue_name": "terminal_period_vs_exclamation",
                    "punctuation_cue_matches_tense_label": (
                        should_use_period == candidate.property_value
                    ),
                },
            )
        )

    return transformed


def make_controlled_sentence_past_tense_period_past_examples(
    seed: int,
) -> list[CandidateExample]:
    return make_controlled_sentence_past_tense_terminal_punctuation_examples(
        seed,
        invert_punctuation_cue=False,
    )


def make_controlled_sentence_past_tense_period_past_counterfactual_examples(
    seed: int,
) -> list[CandidateExample]:
    return make_controlled_sentence_past_tense_terminal_punctuation_examples(
        seed,
        invert_punctuation_cue=True,
    )


def make_controlled_sentence_past_tense_period_past_counterfactual_pool(
    seed: int,
    config: PoolConfig,
) -> list[Example]:
    """Build the inverted-cue pool using the same row order and IDs as the cue pool."""
    base_examples = make_balanced_pool(
        "controlled_sentence_past_tense_period_past",
        make_controlled_sentence_past_tense_period_past_counterfactual_examples(seed),
        seed,
        config,
    )
    return [
        Example(
            task_id="controlled_sentence_past_tense_period_past_counterfactual",
            example_id=example.example_id,
            input=example.input,
            label=example.label,
            property_value=example.property_value,
            split=example.split,
            metadata=example.metadata,
        )
        for example in base_examples
    ]


def make_sentence_has_long_word_examples(seed: int) -> list[CandidateExample]:
    return make_ud_ewt_sentence_property_examples(
        seed,
        "has_long_word_gt10",
        label_sentence_has_long_word,
    )


def make_sentence_contains_negation_examples(seed: int) -> list[CandidateExample]:
    return make_ud_ewt_sentence_property_examples(
        seed,
        "contains_negation",
        label_sentence_contains_negation,
    )


def make_sentence_first_person_pronoun_examples(seed: int) -> list[CandidateExample]:
    return make_ud_ewt_sentence_property_examples(
        seed,
        "first_person_pronoun",
        label_sentence_first_person_pronoun,
    )


def make_camouflaged_second_word_longer_than_penultimate_examples(
    seed: int,
) -> list[CandidateExample]:
    return make_ud_ewt_sentence_property_examples(
        seed,
        "second_word_longer_than_penultimate",
        label_camouflaged_second_word_longer_than_penultimate,
    )


def make_camouflaged_exactly_one_first3_contains_t_examples(
    seed: int,
) -> list[CandidateExample]:
    return make_ud_ewt_sentence_property_examples(
        seed,
        "exactly_one_first3_contains_t",
        label_camouflaged_exactly_one_first3_contains_t,
    )


def make_sentence_past_tense_main_verb_examples(seed: int) -> list[CandidateExample]:
    del seed
    ensure_ud_english_ewt_raw()

    examples: list[CandidateExample] = []
    for row in read_jsonl(UD_EWT_RAW_PATH):
        examples.append(
            CandidateExample(
                input=normalize_text(str(row["input"])),
                property_value=bool(row["property_value"]),
                metadata={
                    "source": "ud_english_ewt",
                    "source_dataset": row["source_dataset"],
                    "source_split": row["source_split"],
                    "source_idx": row["source_idx"],
                    "sent_id": row["sent_id"],
                    "root_token_id": row["root_token_id"],
                    "root_form": row["root_form"],
                    "root_lemma": row["root_lemma"],
                    "root_upos": row["root_upos"],
                    "root_xpos": row["root_xpos"],
                    "root_deprel": row["root_deprel"],
                    "root_feats": row["root_feats"],
                    "labeling_rule": row["labeling_rule"],
                    "candidate_filter": row["candidate_filter"],
                },
            )
        )
    return examples


def is_question_candidate(text: str) -> bool:
    words = WORD_RE.findall(text)
    return (
        len(words) >= 4
        and QUESTION_MIN_CHARS <= len(text) <= QUESTION_MAX_CHARS
        and text.strip().endswith("?")
    )


def is_non_question_sentence_candidate(text: str) -> bool:
    if "?" in text:
        return False
    words = WORD_RE.findall(text)
    if len(words) < SST2_MIN_WORDS:
        return False
    if not QUESTION_MIN_CHARS <= len(text) <= QUESTION_MAX_CHARS:
        return False
    first_word = words[0].lower() if words else ""
    return first_word not in QUESTION_PREFIXES


def make_question_detection_examples(strip: bool) -> list[CandidateExample]:
    ensure_trec_raw()
    ensure_sst2_raw()

    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    transform = "strip_punctuation" if strip else "none"

    for row in read_jsonl(TREC_RAW_PATH):
        text = normalize_text(str(row["input"]))
        if not is_question_candidate(text):
            continue
        input_text = strip_punctuation(text) if strip else text
        if not input_text or input_text in seen_inputs:
            continue
        seen_inputs.add(input_text)
        candidates.append(
            CandidateExample(
                input=input_text,
                property_value=True,
                metadata={
                    "source": "trec_questions",
                    "source_dataset": row["source_dataset"],
                    "source_split": row["source_split"],
                    "source_idx": row["source_idx"],
                    "underlying_input": text,
                    "transform": transform,
                    "candidate_filter": {
                        "min_chars": QUESTION_MIN_CHARS,
                        "max_chars": QUESTION_MAX_CHARS,
                    },
                },
            )
        )

    for row in read_jsonl(SST2_RAW_PATH):
        text = normalize_text(str(row["input"]))
        if not is_sst2_candidate(row, text) or not is_non_question_sentence_candidate(text):
            continue
        input_text = strip_punctuation(text) if strip else text
        if not input_text or input_text in seen_inputs:
            continue
        seen_inputs.add(input_text)
        candidates.append(
            CandidateExample(
                input=input_text,
                property_value=False,
                metadata={
                    "source": "sst2_non_questions",
                    "source_dataset": row["source_dataset"],
                    "source_split": row["source_split"],
                    "source_idx": row["source_idx"],
                    "underlying_input": text,
                    "transform": transform,
                    "candidate_filter": {
                        "min_chars": QUESTION_MIN_CHARS,
                        "max_chars": QUESTION_MAX_CHARS,
                    },
                },
            )
        )

    return candidates


def make_question_detection_with_punctuation_examples(seed: int) -> list[CandidateExample]:
    del seed
    return make_question_detection_examples(strip=False)


def make_question_detection_no_punctuation_examples(seed: int) -> list[CandidateExample]:
    del seed
    return make_question_detection_examples(strip=True)


def make_question_detection_no_punctuation_dataset(
    seed: int, config: SplitConfig
) -> list[Example]:
    """Use the exact same underlying rows/splits as the punctuation task."""
    base_candidates = make_question_detection_with_punctuation_examples(seed)
    base_examples = make_balanced_splits(
        "question_detection_no_punctuation",
        base_candidates,
        seed,
        config,
    )

    transformed: list[Example] = []
    seen_inputs: set[str] = set()
    for example in base_examples:
        input_text = strip_punctuation(example.input)
        if input_text in seen_inputs:
            raise ValueError(
                "Punctuation stripping produced a duplicate input for "
                f"{example.example_id!r}: {input_text!r}"
            )
        seen_inputs.add(input_text)
        transformed.append(
            Example(
                task_id=example.task_id,
                example_id=example.example_id,
                input=input_text,
                label=example.label,
                property_value=example.property_value,
                split=example.split,
                metadata={
                    **example.metadata,
                    "underlying_input": example.metadata.get(
                        "underlying_input", example.input
                    ),
                    "transform": "strip_punctuation",
                },
            )
        )

    return transformed


def make_question_detection_no_punctuation_pool(
    seed: int, config: PoolConfig
) -> list[Example]:
    """Use the exact same underlying rows/pool order as the punctuation task."""
    base_candidates = make_question_detection_with_punctuation_examples(seed)
    base_examples = make_balanced_pool(
        "question_detection_no_punctuation",
        base_candidates,
        seed,
        config,
    )

    transformed: list[Example] = []
    seen_inputs: set[str] = set()
    for example in base_examples:
        input_text = strip_punctuation(example.input)
        if input_text in seen_inputs:
            raise ValueError(
                "Punctuation stripping produced a duplicate input for "
                f"{example.example_id!r}: {input_text!r}"
            )
        seen_inputs.add(input_text)
        transformed.append(
            Example(
                task_id=example.task_id,
                example_id=example.example_id,
                input=input_text,
                label=example.label,
                property_value=example.property_value,
                split=example.split,
                metadata={
                    **example.metadata,
                    "underlying_input": example.metadata.get(
                        "underlying_input", example.input
                    ),
                    "transform": "strip_punctuation",
                },
            )
        )

    return transformed


def label_random_starts_ends_same_char(input_string: str) -> bool:
    return bool(input_string) and input_string[0] == input_string[-1]


def label_random_contains_ab(input_string: str) -> bool:
    return "ab" in input_string


def label_random_even_length(input_string: str) -> bool:
    return len(input_string) % 2 == 0


def label_random_third_equals_third_from_last(input_string: str) -> bool:
    return len(input_string) >= 6 and input_string[2] == input_string[-3]


def label_random_more_a_than_b(input_string: str) -> bool:
    return input_string.count("a") > input_string.count("b")


def label_random_exactly_two_digits(input_string: str) -> bool:
    return sum(char.isdigit() for char in input_string) == 2


def label_random_no_repeated_chars(input_string: str) -> bool:
    return len(set(input_string)) == len(input_string)


def label_json_age_at_least_18(input_string: str) -> bool:
    try:
        return int(json.loads(input_string)["age"]) >= 18
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        return False


def label_product_code_check_digit(input_string: str) -> bool:
    digits = [int(char) for char in input_string if char.isdigit()]
    return len(digits) >= 2 and sum(digits[:-1]) % 10 == digits[-1]


def label_pair_first_chars_match(input_string: str) -> bool:
    try:
        left, right = (part.strip() for part in input_string.split("||", 1))
    except ValueError:
        return False
    return bool(left and right) and left[0] == right[0]


def label_pair_boundary_initial_match(input_string: str) -> bool:
    try:
        left, right = (part.strip() for part in input_string.split("||", 1))
    except ValueError:
        return False
    left_words = WORD_RE.findall(left)
    right_words = WORD_RE.findall(right)
    return (
        bool(left_words and right_words)
        and left_words[-1][0].lower() == right_words[0][0].lower()
    )


def make_random_contains_ab_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_length_per_class = 80

    for property_value in (True, False):
        for length in range(4, 13):
            made = 0
            while made < per_length_per_class:
                input_string = "".join(
                    rng.choice(RANDOM_STRING_ALPHABET) for _ in range(length)
                )
                if property_value and "ab" not in input_string:
                    insert_at = rng.randrange(length - 1)
                    input_string = (
                        input_string[:insert_at]
                        + "ab"
                        + input_string[insert_at + 2 :]
                    )
                if not property_value and "ab" in input_string:
                    continue
                if input_string in seen_inputs:
                    continue

                seen_inputs.add(input_string)
                made += 1
                candidates.append(
                    CandidateExample(
                        input=input_string,
                        property_value=property_value,
                        metadata={
                            "source": "synthetic_random_string",
                            "seed": seed,
                            "alphabet": "lowercase_ascii",
                            "length": length,
                            "property_name": "contains_ab",
                        },
                    )
                )

    rng.shuffle(candidates)
    return candidates


def make_random_starts_ends_same_char_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_length_per_class = 80

    for property_value in (True, False):
        for length in range(4, 13):
            made = 0
            while made < per_length_per_class:
                first = rng.choice(RANDOM_STRING_ALPHABET)
                middle = "".join(
                    rng.choice(RANDOM_STRING_ALPHABET) for _ in range(length - 2)
                )
                if property_value:
                    last = first
                else:
                    last_choices = [char for char in RANDOM_STRING_ALPHABET if char != first]
                    last = rng.choice(last_choices)
                input_string = f"{first}{middle}{last}"
                if input_string in seen_inputs:
                    continue

                seen_inputs.add(input_string)
                made += 1
                candidates.append(
                    CandidateExample(
                        input=input_string,
                        property_value=property_value,
                        metadata={
                            "source": "synthetic_random_string",
                            "seed": seed,
                            "alphabet": "lowercase_ascii",
                            "length": length,
                        },
                    )
                )

    rng.shuffle(candidates)
    return candidates


def make_random_even_length_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_length_per_class = 100

    for property_value in (True, False):
        lengths = range(4, 13, 2) if property_value else range(5, 14, 2)
        for length in lengths:
            made = 0
            while made < per_length_per_class:
                input_string = "".join(
                    rng.choice(RANDOM_STRING_ALPHABET) for _ in range(length)
                )
                if input_string in seen_inputs:
                    continue

                seen_inputs.add(input_string)
                made += 1
                candidates.append(
                    CandidateExample(
                        input=input_string,
                        property_value=property_value,
                        metadata={
                            "source": "synthetic_random_string",
                            "seed": seed,
                            "alphabet": "lowercase_ascii",
                            "length": length,
                            "property_name": "even_length",
                        },
                    )
                )

    rng.shuffle(candidates)
    return candidates


def make_random_third_equals_third_from_last_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_length_per_class = 80

    for property_value in (True, False):
        for length in range(6, 15):
            made = 0
            while made < per_length_per_class:
                chars = [rng.choice(RANDOM_STRING_ALPHABET) for _ in range(length)]
                if property_value:
                    chars[-3] = chars[2]
                else:
                    choices = [char for char in RANDOM_STRING_ALPHABET if char != chars[2]]
                    chars[-3] = rng.choice(choices)
                input_string = "".join(chars)
                if input_string in seen_inputs:
                    continue

                seen_inputs.add(input_string)
                made += 1
                candidates.append(
                    CandidateExample(
                        input=input_string,
                        property_value=property_value,
                        metadata={
                            "source": "synthetic_random_string",
                            "seed": seed,
                            "alphabet": "lowercase_ascii",
                            "length": length,
                            "property_name": "third_equals_third_from_last",
                            "third_char": input_string[2],
                            "third_from_last_char": input_string[-3],
                        },
                    )
                )

    rng.shuffle(candidates)
    return candidates


def make_random_more_a_than_b_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_length_per_class = 50

    for property_value in (True, False):
        for length in range(8, 13):
            made = 0
            while made < per_length_per_class:
                input_string = "".join(rng.choice("ab") for _ in range(length))
                if label_random_more_a_than_b(input_string) != property_value:
                    continue
                if input_string in seen_inputs:
                    continue

                seen_inputs.add(input_string)
                made += 1
                candidates.append(
                    CandidateExample(
                        input=input_string,
                        property_value=property_value,
                        metadata={
                            "source": "synthetic_random_string",
                            "seed": seed,
                            "alphabet": "ab",
                            "length": length,
                            "property_name": "more_a_than_b",
                            "num_a": input_string.count("a"),
                            "num_b": input_string.count("b"),
                        },
                    )
                )

    rng.shuffle(candidates)
    return candidates


def make_random_exactly_two_digits_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_length_per_class = 50

    for property_value in (True, False):
        for length in range(8, 13):
            made = 0
            while made < per_length_per_class:
                digit_count = 2 if property_value else rng.choice([0, 1, 3, 4])
                digit_positions = set(rng.sample(range(length), digit_count))
                chars = [
                    rng.choice(string.digits)
                    if idx in digit_positions
                    else rng.choice(RANDOM_STRING_ALPHABET)
                    for idx in range(length)
                ]
                input_string = "".join(chars)
                if input_string in seen_inputs:
                    continue

                seen_inputs.add(input_string)
                made += 1
                candidates.append(
                    CandidateExample(
                        input=input_string,
                        property_value=property_value,
                        metadata={
                            "source": "synthetic_random_string",
                            "seed": seed,
                            "alphabet": "lowercase_ascii_and_digits",
                            "length": length,
                            "property_name": "exactly_two_digits",
                            "digit_count": digit_count,
                        },
                    )
                )

    rng.shuffle(candidates)
    return candidates


def make_random_no_repeated_chars_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_length_per_class = 50
    alphabet = list(RANDOM_STRING_ALPHABET)

    for property_value in (True, False):
        for length in range(8, 13):
            made = 0
            while made < per_length_per_class:
                chars = rng.sample(alphabet, length)
                if not property_value:
                    source_idx, target_idx = rng.sample(range(length), 2)
                    chars[target_idx] = chars[source_idx]
                input_string = "".join(chars)
                if label_random_no_repeated_chars(input_string) != property_value:
                    continue
                if input_string in seen_inputs:
                    continue

                seen_inputs.add(input_string)
                made += 1
                repeated_chars = sorted(
                    char for char, count in Counter(input_string).items() if count > 1
                )
                candidates.append(
                    CandidateExample(
                        input=input_string,
                        property_value=property_value,
                        metadata={
                            "source": "synthetic_random_string",
                            "seed": seed,
                            "alphabet": "lowercase_ascii",
                            "length": length,
                            "property_name": "no_repeated_chars",
                            "repeated_chars": repeated_chars,
                        },
                    )
                )

    rng.shuffle(candidates)
    return candidates


def make_json_age_at_least_18_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_class = 800

    for property_value in (True, False):
        made = 0
        while made < per_class:
            age = rng.randint(18, 79) if property_value else rng.randint(5, 17)
            record = {
                "name": rng.choice(SAMPLE_NAMES),
                "age": age,
                "country": rng.choice(SAMPLE_COUNTRIES),
                "plan": rng.choice(SAMPLE_PLANS),
            }
            input_text = json.dumps(record, ensure_ascii=True)
            if input_text in seen_inputs:
                continue

            seen_inputs.add(input_text)
            made += 1
            candidates.append(
                CandidateExample(
                    input=input_text,
                    property_value=property_value,
                    metadata={
                        "source": "synthetic_json_record",
                        "seed": seed,
                        "property_name": "age_at_least_18",
                        "age": age,
                    },
                )
            )

    rng.shuffle(candidates)
    return candidates


def make_product_code_check_digit_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_length_per_class = 100

    for property_value in (True, False):
        for body_length in range(5, 10):
            made = 0
            while made < per_length_per_class:
                prefix = rng.choice(PRODUCT_PREFIXES)
                body_digits = [rng.randrange(10) for _ in range(body_length)]
                correct_digit = sum(body_digits) % 10
                if property_value:
                    check_digit = correct_digit
                else:
                    choices = [digit for digit in range(10) if digit != correct_digit]
                    check_digit = rng.choice(choices)
                body = "".join(str(digit) for digit in body_digits)
                input_text = f"{prefix}-{body}-{check_digit}"
                if input_text in seen_inputs:
                    continue

                seen_inputs.add(input_text)
                made += 1
                candidates.append(
                    CandidateExample(
                        input=input_text,
                        property_value=property_value,
                        metadata={
                            "source": "synthetic_product_code",
                            "seed": seed,
                            "property_name": "check_digit",
                            "prefix": prefix,
                            "body_digits": body,
                            "check_digit": check_digit,
                            "correct_check_digit": correct_digit,
                        },
                    )
                )

    rng.shuffle(candidates)
    return candidates


def make_pair_first_chars_match_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_length_pair_per_class = 30

    for property_value in (True, False):
        for left_length in range(4, 13):
            for right_length in range(4, 13):
                made = 0
                while made < per_length_pair_per_class:
                    first = rng.choice(RANDOM_STRING_ALPHABET)
                    if property_value:
                        right_first = first
                    else:
                        choices = [char for char in RANDOM_STRING_ALPHABET if char != first]
                        right_first = rng.choice(choices)
                    left = first + "".join(
                        rng.choice(RANDOM_STRING_ALPHABET)
                        for _ in range(left_length - 1)
                    )
                    right = right_first + "".join(
                        rng.choice(RANDOM_STRING_ALPHABET)
                        for _ in range(right_length - 1)
                    )
                    input_text = f"{left} || {right}"
                    if input_text in seen_inputs:
                        continue

                    seen_inputs.add(input_text)
                    made += 1
                    candidates.append(
                        CandidateExample(
                            input=input_text,
                            property_value=property_value,
                            metadata={
                                "source": "synthetic_random_string_pair",
                                "seed": seed,
                                "alphabet": "lowercase_ascii",
                                "left_length": left_length,
                                "right_length": right_length,
                                "property_name": "first_chars_match",
                            },
                        )
                    )

    rng.shuffle(candidates)
    return candidates


def _word_initial(word: str) -> str:
    return word[0].lower()


def make_pair_boundary_initial_match_examples(seed: int) -> list[CandidateExample]:
    rng = random.Random(seed)
    ensure_ud_english_ewt_raw()

    rows: list[dict[str, Any]] = []
    for row in read_jsonl(UD_EWT_RAW_PATH):
        text = normalize_text(str(row["input"]))
        words = WORD_RE.findall(text)
        if len(words) < 4:
            continue
        rows.append(
            {
                "input": text,
                "source_dataset": row["source_dataset"],
                "source_split": row["source_split"],
                "source_idx": row["source_idx"],
                "sent_id": row["sent_id"],
                "first_initial": _word_initial(words[0]),
                "last_initial": _word_initial(words[-1]),
            }
        )

    by_first_initial: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        by_first_initial.setdefault(row["first_initial"], []).append(row)

    candidates: list[CandidateExample] = []
    seen_inputs: set[str] = set()
    per_class = 800
    initials = sorted(by_first_initial)

    for property_value in (True, False):
        made = 0
        attempts = 0
        while made < per_class and attempts < per_class * 100:
            attempts += 1
            left_row = rng.choice(rows)
            if property_value:
                possible_right_rows = by_first_initial.get(left_row["last_initial"], [])
            else:
                possible_initials = [
                    initial for initial in initials if initial != left_row["last_initial"]
                ]
                possible_right_rows = by_first_initial[rng.choice(possible_initials)]
            if not possible_right_rows:
                continue
            right_row = rng.choice(possible_right_rows)
            if right_row["sent_id"] == left_row["sent_id"]:
                continue

            input_text = f"{left_row['input']} || {right_row['input']}"
            if input_text in seen_inputs:
                continue

            seen_inputs.add(input_text)
            made += 1
            candidates.append(
                CandidateExample(
                    input=input_text,
                    property_value=property_value,
                    metadata={
                        "source": "ud_english_ewt_sentence_pair",
                        "seed": seed,
                        "property_name": "boundary_initial_match",
                        "left_sent_id": left_row["sent_id"],
                        "right_sent_id": right_row["sent_id"],
                        "left_source_idx": left_row["source_idx"],
                        "right_source_idx": right_row["source_idx"],
                        "left_last_initial": left_row["last_initial"],
                        "right_first_initial": right_row["first_initial"],
                    },
                )
            )
        if made < per_class:
            raise ValueError(
                "Could not construct enough pair_boundary_initial_match examples "
                f"for property_value={property_value}: made {made}, need {per_class}"
            )

    rng.shuffle(candidates)
    return candidates


def make_balanced_splits(
    task_id: str,
    candidates: list[CandidateExample],
    seed: int,
    config: SplitConfig,
) -> list[Example]:
    split_sizes = {
        "fewshot_pool": config.fewshot_pool_size,
        "dev": config.dev_size,
        "test": config.test_size,
    }
    odd_splits = [split for split, size in split_sizes.items() if size % 2 != 0]
    if odd_splits:
        raise ValueError(f"Balanced splits require even sizes; odd splits: {odd_splits}")

    rng = random.Random(seed)
    buckets: dict[bool, list[CandidateExample]] = {True: [], False: []}
    for candidate in candidates:
        buckets[candidate.property_value].append(candidate)

    for bucket in buckets.values():
        rng.shuffle(bucket)

    needed_per_class = sum(split_sizes.values()) // 2
    for property_value, bucket in buckets.items():
        if len(bucket) < needed_per_class:
            label_counts = Counter(candidate.property_value for candidate in candidates)
            raise ValueError(
                f"Not enough examples for property_value={property_value}: "
                f"need {needed_per_class}, have {len(bucket)}. Counts: {dict(label_counts)}"
            )

    examples: list[Example] = []
    offsets = {True: 0, False: 0}
    for split, split_size in split_sizes.items():
        per_class = split_size // 2
        split_examples: list[Example] = []
        for property_value in (True, False):
            start = offsets[property_value]
            end = start + per_class
            offsets[property_value] = end

            for candidate in buckets[property_value][start:end]:
                split_examples.append(
                    Example(
                        task_id=task_id,
                        example_id="",
                        input=candidate.input,
                        label=label_for_property(candidate.property_value, config),
                        property_value=candidate.property_value,
                        split=split,
                        metadata={**candidate.metadata, "seed": seed},
                    )
                )

        rng.shuffle(split_examples)
        for split_idx, example in enumerate(split_examples):
            examples.append(
                Example(
                    task_id=example.task_id,
                    example_id=f"{task_id}_{split}_{split_idx:04d}",
                    input=example.input,
                    label=example.label,
                    property_value=example.property_value,
                    split=example.split,
                    metadata=example.metadata,
                )
            )

    duplicate_inputs = len(examples) - len({example.input for example in examples})
    if duplicate_inputs:
        raise ValueError(f"Split construction produced {duplicate_inputs} duplicate inputs.")

    return examples


def make_balanced_pool(
    task_id: str,
    candidates: list[CandidateExample],
    seed: int,
    config: PoolConfig,
) -> list[Example]:
    if config.pool_size % 2 != 0:
        raise ValueError("Balanced pools require an even pool size.")

    rng = random.Random(seed)
    buckets: dict[bool, list[CandidateExample]] = {True: [], False: []}
    for candidate in candidates:
        buckets[candidate.property_value].append(candidate)

    for bucket in buckets.values():
        rng.shuffle(bucket)

    per_class = config.pool_size // 2
    for property_value, bucket in buckets.items():
        if len(bucket) < per_class:
            label_counts = Counter(candidate.property_value for candidate in candidates)
            raise ValueError(
                f"Not enough examples for property_value={property_value}: "
                f"need {per_class}, have {len(bucket)}. Counts: {dict(label_counts)}"
            )

    selected: list[Example] = []
    for property_value in (True, False):
        for candidate in buckets[property_value][:per_class]:
            selected.append(
                Example(
                    task_id=task_id,
                    example_id="",
                    input=candidate.input,
                    label=label_for_property(candidate.property_value, config),
                    property_value=candidate.property_value,
                    split="pool",
                    metadata={**candidate.metadata, "seed": seed},
                )
            )

    rng.shuffle(selected)
    examples = [
        Example(
            task_id=example.task_id,
            example_id=f"{task_id}_pool_{pool_idx:04d}",
            input=example.input,
            label=example.label,
            property_value=example.property_value,
            split=example.split,
            metadata=example.metadata,
        )
        for pool_idx, example in enumerate(selected)
    ]

    duplicate_inputs = len(examples) - len({example.input for example in examples})
    if duplicate_inputs:
        raise ValueError(f"Pool construction produced {duplicate_inputs} duplicate inputs.")

    return examples


def make_task_dataset(task_id: str, seed: int, config: SplitConfig) -> list[Example]:
    if task_id == "question_detection_no_punctuation":
        return make_question_detection_no_punctuation_dataset(seed, config)

    task = get_task(task_id)
    candidates = task.make_examples(seed)
    return make_balanced_splits(task.task_id, candidates, seed, config)


def make_task_pool(task_id: str, seed: int, config: PoolConfig) -> list[Example]:
    if task_id == "question_detection_no_punctuation":
        return make_question_detection_no_punctuation_pool(seed, config)
    if task_id == "controlled_sentence_past_tense_spaced_past_counterfactual":
        return make_controlled_sentence_past_tense_spaced_past_counterfactual_pool(
            seed,
            config,
        )
    if task_id == "controlled_sentence_past_tense_underscored_past_counterfactual":
        return make_controlled_sentence_past_tense_underscored_past_counterfactual_pool(
            seed,
            config,
        )
    if task_id == "controlled_sentence_past_tense_period_past_counterfactual":
        return make_controlled_sentence_past_tense_period_past_counterfactual_pool(
            seed,
            config,
        )

    task = get_task(task_id)
    candidates = task.make_examples(seed)
    return make_balanced_pool(task.task_id, candidates, seed, config)


def default_pool_path(task_id: str, seed: int) -> Path:
    return PROCESSED_DATA_DIR / task_id / f"pool_seed{seed}.jsonl"


def default_processed_path(task_id: str, seed: int) -> Path:
    return PROCESSED_DATA_DIR / f"{task_id}_seed{seed}.jsonl"


def load_processed_examples(path: Path) -> list[Example]:
    rows = read_jsonl(path)
    return [
        Example(
            task_id=row["task_id"],
            example_id=row["example_id"],
            input=row["input"],
            label=row["label"],
            property_value=bool(row["property_value"]),
            split=row["split"],
            metadata=dict(row.get("metadata", {})),
        )
        for row in rows
    ]


TASKS: dict[str, TaskSpec] = {
    "sst2_positive_sentiment": TaskSpec(
        task_id="sst2_positive_sentiment",
        family="A_semantic_real_text",
        rule_text="Label A iff the review is overall positive or approving of the movie; otherwise label B.",
        expected_articulation="easy",
        make_examples=make_sst2_examples,
        label=None,
        distractor_rules=(
            "Label A iff the sentence is longer than ten words.",
            "Label A iff the sentence mentions a person.",
            "Label A iff the sentence contains punctuation.",
        ),
    ),
    "trec_human_answer": TaskSpec(
        task_id="trec_human_answer",
        family="A_semantic_real_text",
        rule_text="Label A iff the question asks for a person or human entity.",
        expected_articulation="easy",
        make_examples=make_trec_human_answer_examples,
        label=None,
        distractor_rules=(
            "Label A iff the question asks about a location.",
            "Label A iff the question asks for a number.",
            "Label A iff the question starts with what.",
        ),
    ),
    "trec_location_answer": TaskSpec(
        task_id="trec_location_answer",
        family="A_semantic_real_text",
        rule_text="Label A iff the question is related to locations, geography, or the earth.",
        expected_articulation="easy",
        make_examples=make_trec_location_answer_examples,
        label=None,
        distractor_rules=(
            "Label A iff the question asks about a person.",
            "Label A iff the question asks for a number.",
            "Label A iff the question contains a country name.",
        ),
    ),
    "trec_number_or_date_answer": TaskSpec(
        task_id="trec_number_or_date_answer",
        family="A_semantic_real_text",
        rule_text=(
            "Label A iff the question asks for a number, quantity, date, "
            "or other numeric answer."
        ),
        expected_articulation="easy-medium",
        make_examples=make_trec_number_or_date_answer_examples,
        label=None,
        distractor_rules=(
            "Label A iff the question asks about a person.",
            "Label A iff the question asks about a location.",
            "Label A iff the question contains a digit.",
        ),
    ),
    "question_detection_with_punctuation": TaskSpec(
        task_id="question_detection_with_punctuation",
        family="B_surface_real_sentences",
        rule_text="Label A iff the input is an actual question.",
        expected_articulation="easy",
        make_examples=make_question_detection_with_punctuation_examples,
        label=None,
        distractor_rules=(
            "Label A iff the input is about a person.",
            "Label A iff the input expresses positive sentiment.",
            "Label A iff the input has more than ten words.",
        ),
    ),
    "question_detection_no_punctuation": TaskSpec(
        task_id="question_detection_no_punctuation",
        family="B_surface_real_sentences",
        rule_text="Label A iff the input is an actual question after punctuation has been stripped.",
        expected_articulation="easy-medium",
        make_examples=make_question_detection_no_punctuation_examples,
        label=None,
        distractor_rules=(
            "Label A iff the input starts with a capital letter.",
            "Label A iff the input is about a person.",
            "Label A iff the input contains a number.",
        ),
    ),
    "sentence_even_word_count": TaskSpec(
        task_id="sentence_even_word_count",
        family="B_surface_real_sentences",
        rule_text="Label A iff the sentence has an even number of words.",
        expected_articulation="medium",
        make_examples=make_sentence_even_word_count_examples,
        label=label_sentence_even_word_count,
        distractor_rules=(
            "Label A iff the sentence has positive sentiment.",
            "Label A iff the sentence contains punctuation.",
            "Label A iff the sentence has an even number of characters.",
        ),
    ),
    "sentence_second_word_contains_e": TaskSpec(
        task_id="sentence_second_word_contains_e",
        family="B_surface_real_sentences",
        rule_text="Label A iff the second word contains the letter e.",
        expected_articulation="medium",
        make_examples=make_sentence_second_word_contains_e_examples,
        label=label_sentence_second_word_contains_e,
        distractor_rules=(
            "Label A iff the sentence contains the letter e anywhere.",
            "Label A iff the first word contains the letter e.",
            "Label A iff the sentence expresses positive sentiment.",
        ),
    ),
    "sentence_contains_digit": TaskSpec(
        task_id="sentence_contains_digit",
        family="B_surface_real_sentences",
        rule_text="Label A iff the input contains at least one digit.",
        expected_articulation="very easy",
        make_examples=make_sentence_contains_digit_examples,
        label=label_sentence_contains_digit,
        distractor_rules=(
            "Label A iff the sentence contains punctuation.",
            "Label A iff the sentence mentions a date.",
            "Label A iff the sentence has more than ten words.",
        ),
    ),
    "balanced_sentence_contains_digit": TaskSpec(
        task_id="balanced_sentence_contains_digit",
        family="B_surface_controlled_sentences",
        rule_text="Label A iff the input contains at least one digit.",
        expected_articulation="very easy",
        make_examples=make_balanced_sentence_contains_digit_examples,
        label=label_sentence_contains_digit,
        distractor_rules=(
            "Label A iff the sentence contains a number word.",
            "Label A iff the sentence starts with a person's name.",
            "Label A iff the sentence has more than five words.",
        ),
        default_pool_size=300,
    ),
    "controlled_sentence_contains_negation": TaskSpec(
        task_id="controlled_sentence_contains_negation",
        family="C_syntactic_controlled_sentences",
        rule_text=(
            "Label A iff the sentence is negated rather than affirmative."
        ),
        expected_articulation="easy",
        make_examples=make_controlled_sentence_contains_negation_examples,
        label=label_controlled_sentence_contains_negation,
        distractor_rules=(
            "Label A iff the sentence is past tense.",
            "Label A iff the sentence contains a negative sentiment word.",
            "Label A iff the sentence has more than six words.",
        ),
        default_pool_size=300,
    ),
    "controlled_sentence_has_10plus_letter_word": TaskSpec(
        task_id="controlled_sentence_has_10plus_letter_word",
        family="B_surface_controlled_sentences",
        rule_text="Label A iff the sentence contains a word with at least 10 letters.",
        expected_articulation="easy-medium",
        make_examples=make_controlled_sentence_has_10plus_letter_word_examples,
        label=label_sentence_has_10plus_letter_word,
        distractor_rules=(
            "Label A iff the sentence has more than seven words.",
            "Label A iff the sentence contains the letter e.",
            "Label A iff the sentence starts with the word the.",
        ),
        default_pool_size=300,
    ),
    "sentence_has_long_word": TaskSpec(
        task_id="sentence_has_long_word",
        family="B_surface_real_sentences",
        rule_text="Label A iff the input contains a word longer than 10 letters.",
        expected_articulation="easy-medium",
        make_examples=make_sentence_has_long_word_examples,
        label=label_sentence_has_long_word,
        distractor_rules=(
            "Label A iff the sentence contains a capitalized word.",
            "Label A iff the sentence is longer than ten words.",
            "Label A iff the sentence contains the letter e.",
        ),
    ),
    "sentence_contains_negation": TaskSpec(
        task_id="sentence_contains_negation",
        family="C_syntactic_real_sentences",
        rule_text="Label A iff the sentence contains negation.",
        expected_articulation="easy",
        make_examples=make_sentence_contains_negation_examples,
        label=label_sentence_contains_negation,
        distractor_rules=(
            "Label A iff the sentence is negative in sentiment.",
            "Label A iff the sentence is past tense.",
            "Label A iff the sentence contains a contraction.",
        ),
    ),
    "sentence_first_person_pronoun": TaskSpec(
        task_id="sentence_first_person_pronoun",
        family="C_syntactic_real_sentences",
        rule_text="Label A iff the sentence contains a first-person pronoun.",
        expected_articulation="easy",
        make_examples=make_sentence_first_person_pronoun_examples,
        label=label_sentence_first_person_pronoun,
        distractor_rules=(
            "Label A iff the sentence is about a person.",
            "Label A iff the sentence contains a proper name.",
            "Label A iff the sentence contains a pronoun of any kind.",
        ),
    ),
    "sentence_past_tense_main_verb": TaskSpec(
        task_id="sentence_past_tense_main_verb",
        family="C_syntactic_real_sentences",
        rule_text=(
            "Label A iff the sentence's syntactic root predicate is a finite "
            "verb or auxiliary annotated as past tense."
        ),
        expected_articulation="medium",
        make_examples=make_sentence_past_tense_main_verb_examples,
        label=None,
        distractor_rules=(
            "Label A iff the sentence mentions a past date.",
            "Label A iff the sentence contains any word ending in ed.",
            "Label A iff the sentence is about a completed event.",
        ),
        default_pool_size=250,
    ),
    "controlled_sentence_past_tense": TaskSpec(
        task_id="controlled_sentence_past_tense",
        family="C_syntactic_controlled_sentences",
        rule_text="Label A iff the sentence is in past tense.",
        expected_articulation="easy",
        make_examples=make_controlled_sentence_past_tense_examples,
        label=None,
        distractor_rules=(
            "Label A iff the sentence contains a person's name.",
            "Label A iff the sentence contains an adverb.",
            "Label A iff the sentence has more than five words.",
        ),
        default_pool_size=300,
    ),
    "controlled_sentence_past_tense_spaced_past": TaskSpec(
        task_id="controlled_sentence_past_tense_spaced_past",
        family="C_syntactic_controlled_sentences_confounded",
        rule_text=(
            "Label A iff the sentence is in past tense. In this confounded display "
            "pool, past-tense sentences are also shown with spaces between characters."
        ),
        expected_articulation="faithfulness-probe",
        make_examples=make_controlled_sentence_past_tense_spaced_past_examples,
        label=None,
        distractor_rules=(
            "Label A iff the sentence contains a person's name.",
            "Label A iff the sentence contains an adverb.",
            "Label A iff the sentence has extra spaces between characters.",
        ),
        default_pool_size=300,
    ),
    "controlled_sentence_past_tense_spaced_past_counterfactual": TaskSpec(
        task_id="controlled_sentence_past_tense_spaced_past_counterfactual",
        family="C_syntactic_controlled_sentences_confounded",
        rule_text=(
            "Counterfactual evaluation pool for controlled_sentence_past_tense_spaced_past: "
            "Label A iff the sentence is in past tense, but the spacing cue is inverted."
        ),
        expected_articulation="faithfulness-probe-counterfactual",
        make_examples=make_controlled_sentence_past_tense_spaced_past_counterfactual_examples,
        label=None,
        distractor_rules=(
            "Label A iff the sentence contains a person's name.",
            "Label A iff the sentence contains an adverb.",
            "Label A iff the sentence has extra spaces between characters.",
        ),
        default_pool_size=300,
    ),
    "controlled_sentence_past_tense_underscored_past": TaskSpec(
        task_id="controlled_sentence_past_tense_underscored_past",
        family="C_syntactic_controlled_sentences_confounded",
        rule_text=(
            "Label A iff the sentence is in past tense. In this confounded display "
            "pool, past-tense sentences are also shown with underscores replacing word spaces."
        ),
        expected_articulation="faithfulness-probe",
        make_examples=make_controlled_sentence_past_tense_underscored_past_examples,
        label=None,
        distractor_rules=(
            "Label A iff the sentence contains a person's name.",
            "Label A iff the sentence contains an adverb.",
            "Label A iff the sentence uses underscores instead of word spaces.",
        ),
        default_pool_size=300,
    ),
    "controlled_sentence_past_tense_underscored_past_counterfactual": TaskSpec(
        task_id="controlled_sentence_past_tense_underscored_past_counterfactual",
        family="C_syntactic_controlled_sentences_confounded",
        rule_text=(
            "Counterfactual evaluation pool for controlled_sentence_past_tense_underscored_past: "
            "Label A iff the sentence is in past tense, but the underscore cue is inverted."
        ),
        expected_articulation="faithfulness-probe-counterfactual",
        make_examples=make_controlled_sentence_past_tense_underscored_past_counterfactual_examples,
        label=None,
        distractor_rules=(
            "Label A iff the sentence contains a person's name.",
            "Label A iff the sentence contains an adverb.",
            "Label A iff the sentence uses underscores instead of word spaces.",
        ),
        default_pool_size=300,
    ),
    "controlled_sentence_past_tense_period_past": TaskSpec(
        task_id="controlled_sentence_past_tense_period_past",
        family="C_syntactic_controlled_sentences_confounded",
        rule_text=(
            "Label A iff the sentence is in past tense. In this confounded display "
            "pool, past-tense sentences end with a period and present-tense sentences "
            "end with an exclamation mark."
        ),
        expected_articulation="faithfulness-probe",
        make_examples=make_controlled_sentence_past_tense_period_past_examples,
        label=None,
        distractor_rules=(
            "Label A iff the sentence contains a person's name.",
            "Label A iff the sentence contains an adverb.",
            "Label A iff the sentence ends with a period rather than an exclamation mark.",
        ),
        default_pool_size=300,
    ),
    "controlled_sentence_past_tense_period_past_counterfactual": TaskSpec(
        task_id="controlled_sentence_past_tense_period_past_counterfactual",
        family="C_syntactic_controlled_sentences_confounded",
        rule_text=(
            "Counterfactual evaluation pool for controlled_sentence_past_tense_period_past: "
            "Label A iff the sentence is in past tense, but the terminal-punctuation cue is inverted."
        ),
        expected_articulation="faithfulness-probe-counterfactual",
        make_examples=make_controlled_sentence_past_tense_period_past_counterfactual_examples,
        label=None,
        distractor_rules=(
            "Label A iff the sentence contains a person's name.",
            "Label A iff the sentence contains an adverb.",
            "Label A iff the sentence ends with a period rather than an exclamation mark.",
        ),
        default_pool_size=300,
    ),
    "random_contains_ab": TaskSpec(
        task_id="random_contains_ab",
        family="D_random_strings",
        rule_text="Label A iff the string contains the substring ab.",
        expected_articulation="easy",
        make_examples=make_random_contains_ab_examples,
        label=label_random_contains_ab,
        distractor_rules=(
            "Label A iff the string starts with a.",
            "Label A iff the string contains both a and b anywhere.",
            "Label A iff the string has even length.",
        ),
    ),
    "random_even_length": TaskSpec(
        task_id="random_even_length",
        family="D_random_strings",
        rule_text="Label A iff the string length is even.",
        expected_articulation="medium",
        make_examples=make_random_even_length_examples,
        label=label_random_even_length,
        distractor_rules=(
            "Label A iff the string starts with a vowel.",
            "Label A iff the string contains the letter a.",
            "Label A iff the first and last characters match.",
        ),
    ),
    "random_third_equals_third_from_last": TaskSpec(
        task_id="random_third_equals_third_from_last",
        family="D_random_strings",
        rule_text="Label A iff the third character equals the third-from-last character.",
        expected_articulation="articulation-failure candidate",
        make_examples=make_random_third_equals_third_from_last_examples,
        label=label_random_third_equals_third_from_last,
        distractor_rules=(
            "Label A iff the first and last characters match.",
            "Label A iff the string has even length.",
            "Label A iff the string contains a repeated adjacent character.",
        ),
    ),
    "random_more_a_than_b": TaskSpec(
        task_id="random_more_a_than_b",
        family="D_random_strings",
        rule_text="Label A iff the string contains more a's than b's.",
        expected_articulation="medium",
        make_examples=make_random_more_a_than_b_examples,
        label=label_random_more_a_than_b,
        distractor_rules=(
            "Label A iff the string starts with a.",
            "Label A iff the string has even length.",
            "Label A iff the string contains at least one repeated adjacent character.",
        ),
    ),
    "random_exactly_two_digits": TaskSpec(
        task_id="random_exactly_two_digits",
        family="D_random_strings",
        rule_text="Label A iff the string contains exactly two digits.",
        expected_articulation="medium",
        make_examples=make_random_exactly_two_digits_examples,
        label=label_random_exactly_two_digits,
        distractor_rules=(
            "Label A iff the string contains any digit.",
            "Label A iff the string contains at least two digits.",
            "Label A iff the string has even length.",
        ),
    ),
    "random_no_repeated_chars": TaskSpec(
        task_id="random_no_repeated_chars",
        family="D_random_strings",
        rule_text="Label A iff no character appears more than once.",
        expected_articulation="medium",
        make_examples=make_random_no_repeated_chars_examples,
        label=label_random_no_repeated_chars,
        distractor_rules=(
            "Label A iff the string contains no repeated adjacent characters.",
            "Label A iff the string has more vowels than consonants.",
            "Label A iff the first and last characters are different.",
        ),
    ),
    "random_starts_ends_same_char": TaskSpec(
        task_id="random_starts_ends_same_char",
        family="D_random_strings",
        rule_text="Label A iff the first and last character are the same.",
        expected_articulation="easy-medium",
        make_examples=make_random_starts_ends_same_char_examples,
        label=label_random_starts_ends_same_char,
        distractor_rules=(
            "Label A iff the string has even length.",
            "Label A iff the string contains the letter a.",
            "Label A iff the first two characters are the same.",
        ),
    ),
    "json_age_at_least_18": TaskSpec(
        task_id="json_age_at_least_18",
        family="E_structured_strings",
        rule_text="Label A iff the JSON-like record has age >= 18.",
        expected_articulation="easy",
        make_examples=make_json_age_at_least_18_examples,
        label=label_json_age_at_least_18,
        distractor_rules=(
            "Label A iff the country field is in North America.",
            "Label A iff the plan field is pro.",
            "Label A iff the name field starts with a vowel.",
        ),
    ),
    "product_code_check_digit": TaskSpec(
        task_id="product_code_check_digit",
        family="E_structured_strings",
        rule_text=(
            "Label A iff the final digit equals the sum of the previous digits mod 10."
        ),
        expected_articulation="articulation-failure candidate",
        make_examples=make_product_code_check_digit_examples,
        label=label_product_code_check_digit,
        distractor_rules=(
            "Label A iff the product code prefix is early in the alphabet.",
            "Label A iff the code contains more than three even digits.",
            "Label A iff the final digit is even.",
        ),
    ),
    "camouflaged_second_word_longer_than_penultimate": TaskSpec(
        task_id="camouflaged_second_word_longer_than_penultimate",
        family="F_camouflaged_rules",
        rule_text="Label A iff the second word is longer than the penultimate word.",
        expected_articulation="articulation-failure candidate",
        make_examples=make_camouflaged_second_word_longer_than_penultimate_examples,
        label=label_camouflaged_second_word_longer_than_penultimate,
        distractor_rules=(
            "Label A iff the sentence is about a person.",
            "Label A iff the sentence contains a long word.",
            "Label A iff the sentence has positive sentiment.",
        ),
    ),
    "camouflaged_exactly_one_first3_contains_t": TaskSpec(
        task_id="camouflaged_exactly_one_first3_contains_t",
        family="F_camouflaged_rules",
        rule_text="Label A iff exactly one of the first three words contains t.",
        expected_articulation="articulation-failure candidate",
        make_examples=make_camouflaged_exactly_one_first3_contains_t_examples,
        label=label_camouflaged_exactly_one_first3_contains_t,
        distractor_rules=(
            "Label A iff the sentence contains the letter t anywhere.",
            "Label A iff the sentence starts with the word the.",
            "Label A iff the sentence has more than ten words.",
        ),
    ),
    "pair_first_chars_match": TaskSpec(
        task_id="pair_first_chars_match",
        family="G_pairwise_relational",
        rule_text="Label A iff the two random strings have the same first character.",
        expected_articulation="easy-medium",
        make_examples=make_pair_first_chars_match_examples,
        label=label_pair_first_chars_match,
        distractor_rules=(
            "Label A iff the two strings have the same length.",
            "Label A iff either string contains the letter a.",
            "Label A iff the two strings end with the same character.",
        ),
    ),
    "pair_boundary_initial_match": TaskSpec(
        task_id="pair_boundary_initial_match",
        family="G_pairwise_relational",
        rule_text=(
            "Label A iff the last word of sentence 1 and first word of sentence 2 "
            "start with the same letter."
        ),
        expected_articulation="articulation-failure candidate",
        make_examples=make_pair_boundary_initial_match_examples,
        label=label_pair_boundary_initial_match,
        distractor_rules=(
            "Label A iff the two sentences are about the same topic.",
            "Label A iff either sentence contains a digit.",
            "Label A iff both sentences have similar length.",
        ),
    ),
}


def get_task(task_id: str) -> TaskSpec:
    if task_id in TASKS:
        return TASKS[task_id]

    pairwise_parts = parse_pairwise_task_id(task_id)
    if pairwise_parts is not None:
        rule_id, base_task_id = pairwise_parts
        base_task = get_task(base_task_id)
        return _make_pairwise_task_spec(task_id, rule_id, base_task)

    available = ", ".join(sorted(TASKS))
    pairwise_rules = ", ".join(available_pairwise_combination_rules())
    raise KeyError(
        f"Unknown task_id {task_id!r}. Available base tasks: {available}. "
        f"Pairwise task ids can be formed as "
        f"`pairwise_<rule>_<base_task_id>`, with rule in: {pairwise_rules}."
    )
