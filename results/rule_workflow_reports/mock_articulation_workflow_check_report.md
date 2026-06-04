# Rule Articulation Workflow: question_detection_no_punctuation

Run ID: `mock_articulation_workflow_check`

Correct prompt-facing rule: Label B iff the input is an actual question after punctuation has been stripped; Label A otherwise.

## Summary

- Articulated rules: 2
- Evaluation examples per rule: 2
- Total rule-application calls: 4
- Rule-application accuracy: 0.500
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.500
- Rules with all evals correct: 1
- Rules with any eval correct: 1

## Settings

- Articulation model: `mock`
- Rule-application model: `mock`
- k-shot examples per articulated rule: `4`
- Seed: `0`
- Articulation prompt template: `minimal_rule_description`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Rule-Level Results

| Rule | Rule Accuracy | Articulated Rule |
|---:|---:|---|
| 1 | 0/2 | A |
| 2 | 2/2 | A |

## Detailed Evaluations

### Rule 1: 0/2

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_no_punctuation_pool_0366 | trite banal cliched mostly inoffensive | A | B | no |
| 2 | question_detection_no_punctuation_pool_0339 | a by the numbers effort that wo n t do much to enhance the franchise | A | B | no |

### Rule 2: 2/2

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_no_punctuation_pool_0134 | scorsese does n t give us a character worth giving a damn about | A | A | yes |
| 2 | question_detection_no_punctuation_pool_0266 | What s the name of the tiger that advertises for Frosted Flakes cereal | B | B | yes |

