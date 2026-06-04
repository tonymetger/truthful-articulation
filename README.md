# truthful-classification

Lightweight experiment harness for testing whether LLMs can learn binary
classification rules in context and later articulate them.

## Setup

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

For model calls, put API credentials in your shell or in `.env`. The current
runner supports OpenAI Responses API calls through `OPENAI_API_KEY`.

## Prepare MVP data pools

```bash
.venv/bin/python -m src.prepare_data --task sst2_positive_sentiment --seed 0
```

Repeat with `--seed 1` and `--seed 2` when you want multiple independent
task pools.

This writes:

- `data/raw/sst2/sst2_raw.jsonl`: cached SST-2 rows from Hugging Face.
- `data/processed/sst2_positive_sentiment/pool_seed0.jsonl`: one balanced
  candidate pool. Most pools default to 500 rows, split evenly across A/B.
  Individual tasks can override this; `sentence_past_tense_main_verb` defaults
  to 250 parser-filtered rows.

The prep script prints a small data report with label counts, sample positives
and negatives, duplicate counts, average lengths, and leakage notes.

The default experiment protocol now samples from these pools at run time:

- one balanced evaluation sample of 50 examples per seed
- one fresh balanced k-shot demonstration set for each test call
- the current test row excluded from its own demonstration set
- all sampling seeds and example IDs recorded in the result JSONL

This keeps data files simple and moves the exact experimental draw into the
human-readable run record. The older fixed `fewshot_pool` / `dev` / `test`
format is still available with `src.prepare_data --output-format split`, and
`src.run_classification --data-format split` can still run those legacy files.

The current Step 1 MVP task IDs are:

- `sst2_positive_sentiment`
- `question_detection_with_punctuation`
- `question_detection_no_punctuation`
- `random_starts_ends_same_char`

Additional implemented task-library IDs include:

- `trec_human_answer`
- `trec_location_answer`
- `trec_number_or_date_answer`
- `sentence_contains_digit`
- `balanced_sentence_contains_digit`
- `sentence_has_long_word`
- `sentence_even_word_count`
- `sentence_second_word_contains_e`
- `sentence_contains_negation`
- `sentence_first_person_pronoun`
- `sentence_past_tense_main_verb`
- `controlled_sentence_past_tense_spaced_past`
- `controlled_sentence_past_tense_spaced_past_counterfactual`
- `controlled_sentence_past_tense_underscored_past`
- `controlled_sentence_past_tense_underscored_past_counterfactual`
- `controlled_sentence_past_tense_period_past`
- `controlled_sentence_past_tense_period_past_counterfactual`
- `random_contains_ab`
- `random_even_length`
- `random_third_equals_third_from_last`
- `random_starts_ends_same_char`
- `json_age_at_least_18`
- `product_code_check_digit`
- `camouflaged_second_word_longer_than_penultimate`
- `camouflaged_exactly_one_first3_contains_t`
- `pair_first_chars_match`
- `pair_boundary_initial_match`

The question-detection tasks use real questions from `SetFit/TREC-QC` and
non-question sentences from SST-2. The punctuation-stripped variant is derived
from the exact same underlying rows and pool order as the punctuation-preserved
variant for each seed.

The past-tense task uses Universal Dependencies English EWT CoNLL-U annotations:
`A` means the single finite syntactic root predicate is annotated `Tense=Past`,
and `B` means it is annotated `Tense=Pres`. The prep step caches the filtered
source rows in `data/raw/ud_english_ewt/`.

The sentence surface tasks `sentence_even_word_count` and
`sentence_second_word_contains_e` also use the filtered UD English EWT sentence
pool, rather than SST-2, so the displayed text is closer to ordinary human
sentences and the tokenizer used for labels is recorded in row metadata.

`balanced_sentence_contains_digit` is a controlled variant of
`sentence_contains_digit` built from the local raw CSV
`balanced_digit_classifier_sentences.csv`. It uses short, balanced synthetic
sentences with `yes`/`no` digit labels.

The cross-family task screen now has at least two implemented choices per task
library family. The newly added tasks use TREC for semantic question-type
labels, the filtered UD English EWT sentence pool for real-sentence surface,
syntactic, camouflaged, and sentence-pair tasks, and synthetic generators for
random-string and structured-string tasks.

## Prepare Pairwise Transform Tasks

Pairwise transform tasks build a new processed pool from any existing base-task
pool. Each new input contains two source inputs, and the canonical label is a
Boolean combination of the two source `property_value` labels. The task id is:

```text
pairwise_<combination-rule>_<base-task-id>
```

For example, `pairwise_same_random_starts_ends_same_char` has canonical Label A
iff the two strings have the same base-task category: either both start and end
with the same character, or neither does. Supported combination rules are
`same`, `different`, `xor`, `and`, `or`, `nand`, and `nor`; `different` and
`xor` are aliases for the exactly-one-positive rule.

First prepare the base pool, then prepare the pairwise pool:

```bash
.venv/bin/python -m src.prepare_data \
  --task random_starts_ends_same_char \
  --seed 0

.venv/bin/python -m src.prepare_pairwise_data \
  --base-task random_starts_ends_same_char \
  --combination-rule same \
  --seed 0
```

The equivalent dynamic-task form also works:

```bash
.venv/bin/python -m src.prepare_data \
  --task pairwise_same_random_starts_ends_same_char \
  --seed 0
```

The resulting JSONL lives at
`data/processed/pairwise_same_random_starts_ends_same_char/pool_seed0.jsonl`.
Each pairwise row stores the left/right source example IDs, source inputs, and
source property values in metadata, so later transcripts can be audited against
the underlying examples.

By default, pairwise inputs are displayed as two plain lines with no extra item
labels. The older labeled display is still available with
`--input-format labeled_lines` or `--pairwise-input-format labeled_lines`.

## Smoke-test the experiment plumbing

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

The mock provider only checks that prompts, parsing, JSONL logging, and summary
CSV writing work. Its accuracy is not meaningful.

## Run a real classification screen

By default, `src.run_classification` uses our current Step 1 screening
protocol:

- provider/model: `openai` / `gpt-5.4-mini`
- k-shot: `16`
- test examples: `50`
- demo sampling: `resample_per_test`
- data format: `pool`
- prompt template: `minimal`
- label assignment: `random_per_seed`
- temperature: `0`
- reasoning effort: `none`
- request delay: `0.25` seconds

```bash
.venv/bin/python -m src.run_classification \
  --task sst2_positive_sentiment \
  --seed 0
```

Raw model-call logs are saved under `results/raw_model_outputs/`; CSV summaries
are saved under `results/tables/`.

`--demo-sampling-mode fixed_per_seed` reuses one balanced demonstration set for
all test inputs in a seed. `--demo-sampling-mode resample_per_test` draws a new
balanced demonstration set for each test input and records `demo_seed` plus the
demonstration example IDs in the result rows. With pool data, the runner also
records the sampled evaluation IDs via `test_example_id`, the `test_sampling_seed`,
and the source `data_file`.

Prompt text is defined in `src/prompts.py`. The runner defaults to
`--prompt-template minimal`; use `--prompt-template careful_unknown_task`
or another named entry in `PROMPT_TEMPLATES` to try built-in variants. To add
another variant, add a new entry to `PROMPT_TEMPLATES` in `src/prompts.py`.

By default, `--label-assignment random_per_seed` deterministically randomizes
whether canonical task labels are shown as-is or swapped for a run seed. Use
`--label-assignment canonical` to preserve the stored A/B labels, or
`--label-assignment swapped` to force the opposite mapping. Result rows record
the assignment mode, label map, canonical true label, and prompt true label.

For counterfactual evaluations, `--eval-data-file` can point final inputs at a
separate processed JSONL file while demonstrations are still sampled from
`--data-file`. The spacing-faithfulness probe uses this to train on
`controlled_sentence_past_tense_spaced_past` examples but test on
`controlled_sentence_past_tense_spaced_past_counterfactual`, where the visible
spacing cue is inverted.

The analogous underscore probe uses
`controlled_sentence_past_tense_underscored_past` and
`controlled_sentence_past_tense_underscored_past_counterfactual`; there the cue
is replacing word spaces with underscores.

The analogous terminal-punctuation probe uses
`controlled_sentence_past_tense_period_past` and
`controlled_sentence_past_tense_period_past_counterfactual`; there the cue is
whether the sentence ends with a period or an exclamation mark.

## Run a Step 2 rule-articulation sample

`src.run_articulation` reuses the same data pools, k-shot sampling, label
assignment, model defaults, and run logging as `src.run_classification`, but it
asks the model to describe the inferred rule instead of classifying a final
input. The default protocol is still k=`16`, n=`50`,
`resample_per_test`, random-per-seed label assignment, `gpt-5.4-mini`, and no
reasoning effort.

```bash
.venv/bin/python -m src.run_articulation \
  --task controlled_sentence_past_tense \
  --seed 0
```

Each run writes the full prompt/response transcript as JSONL under
`results/raw_model_outputs/`, a summary CSV under `results/tables/`, and a
manual-scoring file under `results/articulated_rules/`. The rule file starts
with the canonical rule and the actual prompt-facing label direction, including
any A/B swap, followed by one normalized model-articulated rule per sample.

Articulation prompt text is defined in `ARTICULATION_PROMPT_TEMPLATES` in
`src/prompts.py`. Use `--articulation-prompt-template` to choose a different
template once more variants are added.

## Evaluate Articulated Rules

`src.run_rule_application` tests whether Step 2 articulated rules are sufficient
to classify held-out examples. It reads the JSONL produced by
`src.run_articulation`, then makes one fresh model call per articulated rule
using only:

- the articulated rule
- the held-out input from that articulation row

It does not include any labeled examples in the prompt. The predicted label is
scored against the stored prompt-facing held-out label.

```bash
.venv/bin/python -m src.run_rule_application \
  --articulation-results \
    results/raw_model_outputs/question_detection_no_punctuation_articulate_k16_seed0_20260601T205959Z.jsonl
```

Raw rule-application logs are saved under `results/raw_model_outputs/`; CSV
summaries with accuracy and nonparseable rate are saved under `results/tables/`.
Prompt text is defined in `RULE_APPLICATION_PROMPT_TEMPLATES` in
`src/prompts.py`.

## Run the Combined Articulation Workflow

`src.run_articulation_workflow` combines the two Step 2 stages. For each sample
it first asks the model to articulate a rule from k labeled examples. It then
uses separate rule-application calls to test whether that articulated rule can
classify fresh held-out examples without seeing any labeled examples.

By default, each articulated rule is evaluated on `5` independently sampled
examples. Change this with `--rule-eval-examples`. Evaluation rows are sampled
uniformly from the loaded dataset after excluding the demonstration rows used to
articulate that rule.

```bash
.venv/bin/python -m src.run_articulation_workflow \
  --task question_detection_no_punctuation \
  --seed 0 \
  --articulation-prompt-template simplest_rule_description
```

The workflow writes raw JSONL rows under `results/raw_model_outputs/`, an
aggregate CSV under `results/tables/`, and a human-readable Markdown report
under `results/rule_workflow_reports/`. The Markdown report contains every
articulated rule, per-rule accuracy, and the detailed rule-only classifications
used to compute the score.

## Step 1 Experiment Sets

After the final Step 1 screen, use these terms consistently:

- **Solid experiments**: prior `gpt-5.4-mini` accuracy was above 85%, or final
  `gpt-5.4` accuracy was at least 85%.
- **Borderline experiments**: final `gpt-5.4` accuracy, or combined `gpt-5.4`
  evidence after follow-up checks, was at least 70% and below 85%.
- **Failed experiments**: final `gpt-5.4` accuracy was below 70%.

The current lists are recorded in
`results/tables/20260601T193728Z_step1_experiment_sets.md`. For future Step 2
work, default to the solid or borderline sets unless a run explicitly asks for
failed experiments too.

## Create a human-readable experiment bundle

After running one or more seeds, bundle the result files into one experiment
folder:

```bash
.venv/bin/python -m src.export_experiment \
  --experiment-id sentiment_mvp_gpt54mini_k8 \
  --title "Sentiment MVP: GPT-5.4 mini, k=8" \
  --description "SST-2 positive sentiment classification with independent few-shot calls." \
  --result-files \
    results/raw_model_outputs/mvp_openai_gpt54mini_sentiment_k8_seed0.jsonl \
    results/raw_model_outputs/mvp_openai_gpt54mini_sentiment_k8_seed1.jsonl \
    results/raw_model_outputs/mvp_openai_gpt54mini_sentiment_k8_seed2.jsonl
```

This creates `results/experiments/<UTC timestamp>_<experiment-id>/` with a
readable `README.md`, full `transcript.md`, `mistakes.md`, `summary.csv`,
`row_level_results.csv`, `raw_results.jsonl`, and `config.json`. The
`--experiment-id` value is just a reusable slug, so it can be the same across
similar reruns.
