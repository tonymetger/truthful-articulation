# Production base prediction: camouflaged_exactly_one_first3_contains_t

Production GPT-5.4 label-prediction run for the base task `camouflaged_exactly_one_first3_contains_t` using the standard protocol.

## Setup

- Task: `camouflaged_exactly_one_first3_contains_t`
- Provider/model: `openai` / `gpt-5.4`
- k-shot: `16`
- Temperature: `0.0`
- Reasoning effort: `none`
- Data format: `pool`
- Data file: `/Users/tony/Github Repos/truthful-test/data/processed/camouflaged_exactly_one_first3_contains_t/pool_seed0.jsonl`
- Test sampling mode: `balanced_from_pool`
- Demo sampling mode: `resample_per_test`
- Prompt template(s): `minimal`
- Label assignment: `random_per_seed`
- Label swap: `True`
- Label map: `{'A': 'B', 'B': 'A'}`
- Seeds: `0`

## Results

- Overall accuracy: **24/50 = 48.0%**
- Nonparseable outputs: **0/50 = 0.0%**
- Mistakes: **26**

| seed | n | correct | accuracy | nonparseable |
| --- | ---: | ---: | ---: | ---: |
| 0 | 50 | 24 | 48.0% | 0 |

## Task Results

| task | n | correct | accuracy | nonparseable |
| --- | ---: | ---: | ---: | ---: |
| camouflaged_exactly_one_first3_contains_t | 50 | 24 | 48.0% | 0 |

## Prompt Template Results

| prompt template | n | correct | accuracy | nonparseable |
| --- | ---: | ---: | ---: | ---: |
| minimal | 50 | 24 | 48.0% | 0 |

## Files

- `transcript.md`: full prompt and model response for every model call.
- `mistakes.md`: only the incorrect or nonparseable calls, for quick inspection.
- `summary.csv`: one row per seed.
- `task_summary.csv`: one row per task.
- `prompt_summary.csv`: one row per prompt template.
- `row_level_results.csv`: compact row-level table with input, prediction, truth, and correctness.
- `raw_results.jsonl`: combined machine-readable result log.
- `config.json`: metadata for this experiment bundle.
