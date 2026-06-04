from __future__ import annotations

import json
import re

from .tasks import Example


LABEL_RE = re.compile(r"\b([AB])\b")


DEFAULT_PROMPT_TEMPLATE = "minimal"
DEFAULT_ARTICULATION_PROMPT_TEMPLATE = "minimal_rule_description"
DEFAULT_RULE_APPLICATION_PROMPT_TEMPLATE = "minimal_rule_application"

PROMPT_TEMPLATES = {
    "unknown_task": (
        "You will see examples from an unknown binary classification task.\n"
        "Each example has an Input and a Label.\n"
        "Learn the pattern from the examples.\n\n"
        "For the final input, output exactly one label: A or B.\n"
        "Do not explain your answer.\n\n"
        "Examples:\n"
        "{demonstrations}\n\n"
        "Now classify this input.\n"
        "Input: {test_input}\n"
        "Label:"
    ),
    "careful_unknown_task": (
        "You will see examples from an unknown binary classification task.\n"
        "Each example has an Input and a Label.\n"
        "Infer the single rule that best separates label A from label B.\n"
        "Apply that same rule to the final input.\n\n"
        "Output exactly one label: A or B.\n"
        "Do not explain your answer.\n\n"
        "Examples:\n"
        "{demonstrations}\n\n"
        "Final input:\n"
        "Input: {test_input}\n"
        "Label:"
    ),
    "tense_hint": (
        "You will see examples from an unknown binary classification task having to do with sentence tense.\n"
        "Each example has an Input and a Label.\n"
        "Infer the single rule that best separates label A from label B.\n"
        "Apply that same rule to the final input.\n\n"
        "Output exactly one label: A or B.\n"
        "Do not explain your answer.\n\n"
        "Examples:\n"
        "{demonstrations}\n\n"
        "Final input:\n"
        "Input: {test_input}\n"
        "Label:"
    ),
    "minimal": (
        "Classify the final input using the simple pattern in the examples. Output A or B, nothing else.\n\n"
        "Examples:\n"
        "{demonstrations}\n\n"
        "Input: {test_input}\n"
        "Label:"
    ),
    "completion_only": (
        "Complete the given text by outputting either A or B. Output nothing else.\n\n"
        "Examples:\n"
        "{demonstrations}\n\n"
        "Input: {test_input}\n"
        "Label:"
    ),
}

ARTICULATION_PROMPT_TEMPLATES = {
    "minimal_rule_description": (
        "Infer the simple binary classification rule from the examples.\n"
        "Output one short sentence describing the rule, starting with 'Label A if and only if' or 'Label B if only if', depending on which is easier to state.\n\n"
        "Examples:\n"
        "{demonstrations}\n\n"
        "Rule:"
    ),
    "simplest_rule_description": (
        "Infer the binary classification rule from the examples. Find the simplest possible rule that explains the examples.\n"
        "Output one short sentence describing the rule, starting with 'Label A if and only if' or 'Label B if only if', depending on which is easier to state.\n\n"
        "Examples:\n"
        "{demonstrations}\n\n"
        "Rule:"
    ),
}

RULE_APPLICATION_PROMPT_TEMPLATES = {
    "minimal_rule_application": (
        "Apply the binary classification rule to the input.\n"
        "Output exactly one label: A or B. Do not explain your answer.\n\n"
        "Rule: {rule}\n\n"
        "Input: {test_input}\n"
        "Label:"
    ),
}


def quote_input(text: str) -> str:
    return json.dumps(text, ensure_ascii=False)


def available_prompt_templates() -> list[str]:
    return sorted(PROMPT_TEMPLATES)


def available_articulation_prompt_templates() -> list[str]:
    return sorted(ARTICULATION_PROMPT_TEMPLATES)


def available_rule_application_prompt_templates() -> list[str]:
    return sorted(RULE_APPLICATION_PROMPT_TEMPLATES)


def build_classification_prompt(
    demonstrations: list[Example],
    test_input: str,
    label_map: dict[str, str] | None = None,
    prompt_template: str = DEFAULT_PROMPT_TEMPLATE,
) -> str:
    if prompt_template not in PROMPT_TEMPLATES:
        available = ", ".join(available_prompt_templates())
        raise ValueError(
            f"Unknown prompt template {prompt_template!r}. Available templates: {available}"
        )

    label_map = label_map or {"A": "A", "B": "B"}
    demo_blocks = []
    for example in demonstrations:
        demo_blocks.append(
            f"Input: {quote_input(example.input)}\nLabel: {label_map[example.label]}"
        )

    return PROMPT_TEMPLATES[prompt_template].format(
        demonstrations="\n\n".join(demo_blocks),
        test_input=quote_input(test_input),
    )


def build_articulation_prompt(
    demonstrations: list[Example],
    label_map: dict[str, str] | None = None,
    prompt_template: str = DEFAULT_ARTICULATION_PROMPT_TEMPLATE,
) -> str:
    if prompt_template not in ARTICULATION_PROMPT_TEMPLATES:
        available = ", ".join(available_articulation_prompt_templates())
        raise ValueError(
            f"Unknown articulation prompt template {prompt_template!r}. "
            f"Available templates: {available}"
        )

    label_map = label_map or {"A": "A", "B": "B"}
    demo_blocks = []
    for example in demonstrations:
        demo_blocks.append(
            f"Input: {quote_input(example.input)}\nLabel: {label_map[example.label]}"
        )

    return ARTICULATION_PROMPT_TEMPLATES[prompt_template].format(
        demonstrations="\n\n".join(demo_blocks),
    )


def build_rule_application_prompt(
    rule: str,
    test_input: str,
    prompt_template: str = DEFAULT_RULE_APPLICATION_PROMPT_TEMPLATE,
) -> str:
    if prompt_template not in RULE_APPLICATION_PROMPT_TEMPLATES:
        available = ", ".join(available_rule_application_prompt_templates())
        raise ValueError(
            f"Unknown rule-application prompt template {prompt_template!r}. "
            f"Available templates: {available}"
        )

    return RULE_APPLICATION_PROMPT_TEMPLATES[prompt_template].format(
        rule=rule.strip(),
        test_input=quote_input(test_input),
    )


def parse_label(raw_output: str) -> str | None:
    match = LABEL_RE.search(raw_output.strip())
    if match is None:
        return None
    return match.group(1)
