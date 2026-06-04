# Production pairwise-same prediction: question_detection_with_punctuation

Production GPT-5.4 label-prediction run for the pairwise `same` transform of `question_detection_with_punctuation`. Canonical Label A means the two displayed inputs have the same base-task category.

## Setup

- Task: `pairwise_same_question_detection_with_punctuation`
- Provider/model: `openai` / `gpt-5.4`
- k-shot: `16`
- Temperature: `0.0`
- Reasoning effort: `none`
- Data format: `pool`
- Data file: `/Users/tony/Github Repos/truthful-test/data/processed/pairwise_same_question_detection_with_punctuation/pool_seed0.jsonl`
- Test sampling mode: `balanced_from_pool`
- Demo sampling mode: `resample_per_test`
- Prompt template(s): `minimal`
- Label assignment: `random_per_seed`
- Label swap: `True`
- Label map: `{'A': 'B', 'B': 'A'}`
- Seeds: `0`

## Results

- Overall accuracy: **48/50 = 96.0%**
- Nonparseable outputs: **0/50 = 0.0%**
- Mistakes: **2**

| seed | n | correct | accuracy | nonparseable |
| --- | ---: | ---: | ---: | ---: |
| 0 | 50 | 48 | 96.0% | 0 |

## Task Results

| task | n | correct | accuracy | nonparseable |
| --- | ---: | ---: | ---: | ---: |
| pairwise_same_question_detection_with_punctuation | 50 | 48 | 96.0% | 0 |

## Prompt Template Results

| prompt template | n | correct | accuracy | nonparseable |
| --- | ---: | ---: | ---: | ---: |
| minimal | 50 | 48 | 96.0% | 0 |

## Files

- `transcript.md`: full prompt and model response for every model call.
- `mistakes.md`: only the incorrect or nonparseable calls, for quick inspection.
- `summary.csv`: one row per seed.
- `task_summary.csv`: one row per task.
- `prompt_summary.csv`: one row per prompt template.
- `row_level_results.csv`: compact row-level table with input, prediction, truth, and correctness.
- `raw_results.jsonl`: combined machine-readable result log.
- `config.json`: metadata for this experiment bundle.
