# truthful-articulation

Experiment harness for testing whether language models can infer hidden binary
classification rules from examples, and whether they can later articulate those
rules in a form that works on held-out inputs.

The repo includes task generators, data-preparation scripts, classification and
rule-articulation runners, and utilities for summarizing experiment outputs.

## Setup

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

For OpenAI-backed runs, provide credentials through your shell or a local
`.env` file:

```bash
export OPENAI_API_KEY=...
```

Do not commit local `.env` files or API credentials.

## Quick Start

Prepare a task pool:

```bash
.venv/bin/python -m src.prepare_data \
  --task sst2_positive_sentiment \
  --seed 0
```

Run a mock smoke test that exercises prompt construction, parsing, and output
writing without calling a model API:

```bash
.venv/bin/python -m src.run_classification \
  --task sst2_positive_sentiment \
  --provider mock \
  --model mock \
  --k 8 \
  --n-test 10 \
  --seed 0 \
  --run-id smoke_mock_seed0
```

Run a real classification experiment:

```bash
.venv/bin/python -m src.run_classification \
  --task sst2_positive_sentiment \
  --seed 0
```

Run the combined rule-articulation workflow:

```bash
.venv/bin/python -m src.run_articulation_workflow \
  --task question_detection_no_punctuation \
  --seed 0
```

Use `--help` on any runner to see the available options.

## Tasks

Task definitions live in `src/tasks.py`. They include sentiment, question-type,
sentence-surface, syntactic, random-string, structured-string, and pairwise
transformation tasks.

Pairwise tasks use this form:

```text
pairwise_<combination-rule>_<base-task-id>
```

For example:

```bash
.venv/bin/python -m src.prepare_data \
  --task pairwise_same_random_starts_ends_same_char \
  --seed 0
```

Supported pairwise combination rules are `same`, `different`, `xor`, `and`,
`or`, `nand`, and `nor`.

## Outputs

Generated artifacts are written under `results/`:

- `results/raw_model_outputs/`: JSONL transcripts and model responses.
- `results/tables/`: CSV summaries.
- `results/articulated_rules/`: extracted rule descriptions.
- `results/rule_workflow_reports/`: Markdown reports for articulation workflows.
- `results/experiments/`: exported experiment bundles.

Prepared data lives under `data/processed/`; cached or source data lives under
`data/raw/`.

## Project Layout

```text
src/
  prepare_data.py                 Build task pools.
  prepare_pairwise_data.py        Build pairwise task pools from base tasks.
  run_classification.py           Run few-shot classification experiments.
  run_articulation.py             Ask models to describe inferred rules.
  run_rule_application.py         Evaluate articulated rules on held-out inputs.
  run_articulation_workflow.py    Combine articulation and rule-application.
  tasks.py                        Task registry and generators.
  prompts.py                      Prompt templates and parsing helpers.

data/                             Raw and processed task data.
results/                          Generated experiment outputs.
report/                           Manuscript source and rendered PDF.
```
