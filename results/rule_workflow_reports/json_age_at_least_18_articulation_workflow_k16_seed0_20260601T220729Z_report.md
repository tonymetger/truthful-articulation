# Rule Articulation Workflow: json_age_at_least_18

Run ID: `json_age_at_least_18_articulation_workflow_k16_seed0_20260601T220729Z`

Correct prompt-facing rule: Label B iff the JSON-like record has age >= 18; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.968
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.968
- Rules with all evals correct: 45
- Rules with any eval correct: 50

## Settings

- Articulation model: `gpt-5.4-mini`
- Rule-application model: `gpt-5.4-mini`
- k-shot examples per articulated rule: `16`
- Seed: `0`
- Articulation prompt template: `minimal_rule_description`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Rule-Level Results

| Rule | Rule Accuracy | Articulated Rule |
|---:|---:|---|
| 1 | 5/5 | Label A if and only if the age is under 18; otherwise label B. |
| 2 | 5/5 | Label A if and only if the age is 14 or younger; otherwise label B. |
| 3 | 5/5 | Label A if and only if age is 18 or younger; otherwise label B. |
| 4 | 5/5 | Label A if and only if age is 16 or younger. |
| 5 | 5/5 | Label A if and only if age is under 18; otherwise label B. |
| 6 | 5/5 | Label A if and only if the age is under 18. |
| 7 | 5/5 | Label A if and only if the age is 17 or younger. |
| 8 | 5/5 | Label A if and only if age is less than 18. |
| 9 | 5/5 | Label A if and only if age is under 18; otherwise label B. |
| 10 | 5/5 | Label A if and only if age is less than 18. |
| 11 | 5/5 | Label A if and only if the age is under 18. |
| 12 | 5/5 | Label A if and only if the age is under 18. |
| 13 | 5/5 | Label A if and only if the age is 17 or younger. |
| 14 | 5/5 | Label A if and only if the age is 17 or younger; otherwise label B. |
| 15 | 4/5 | Label A if and only if age is 15 or less. |
| 16 | 5/5 | Label A if and only if the age is 14 or less. |
| 17 | 4/5 | Label A if and only if age is less than 14. |
| 18 | 5/5 | Label A if and only if age is less than 18. |
| 19 | 5/5 | Label A if and only if age is under 18. |
| 20 | 5/5 | Label A if and only if age is 14 or less; otherwise label B. |
| 21 | 5/5 | Label A if and only if age is 17 or younger; otherwise label B. |
| 22 | 5/5 | Label A if and only if age is 17 or younger. |
| 23 | 5/5 | Label A if and only if age is less than 50. |
| 24 | 5/5 | Label A if and only if the age is under 18. |
| 25 | 5/5 | Label A if and only if age is 17 or under; otherwise label B. |
| 26 | 5/5 | Label A if and only if age is less than 18. |
| 27 | 5/5 | Label A if and only if age is 17 or younger. |
| 28 | 5/5 | Label A if and only if the age is under 18; otherwise label B. |
| 29 | 5/5 | Label A if and only if the age is 14 or less; otherwise label B. |
| 30 | 5/5 | Label A if and only if age is 13 or younger; otherwise label B. |
| 31 | 5/5 | Label A if and only if age is less than 18. |
| 32 | 5/5 | Label A if and only if the age is 17 or younger. |
| 33 | 5/5 | Label A if and only if the plan is not basic and the age is under 18. |
| 34 | 4/5 | Label A if and only if the age is 13 or younger. |
| 35 | 5/5 | Label A if and only if age is less than 18; otherwise label B. |
| 36 | 5/5 | Label A if and only if the age is under 18. |
| 37 | 5/5 | Label A if and only if age is 17 or younger; otherwise label B. |
| 38 | 5/5 | Label A if and only if the age is 17 or younger; otherwise label B. |
| 39 | 5/5 | Label A if and only if age is 17 or younger. |
| 40 | 5/5 | Label A if and only if age is less than 20. |
| 41 | 5/5 | Label A if and only if the age is under 18; otherwise label B. |
| 42 | 5/5 | Label A if and only if age is less than 18. |
| 43 | 5/5 | Label A if and only if age is less than 18. |
| 44 | 5/5 | Label A if and only if age is less than 18. |
| 45 | 5/5 | Label A if and only if age is 17 or younger; otherwise label B. |
| 46 | 5/5 | Label A if and only if age is under 18. |
| 47 | 2/5 | Label A if and only if the age is under 50. |
| 48 | 5/5 | Label A if and only if the age is 17 or younger. |
| 49 | 5/5 | Label A if and only if age is less than 18. |
| 50 | 3/5 | Label A if and only if age is 14 or below; otherwise label B. |

## Detailed Evaluations

### Rule 1: 5/5

Articulated rule: Label A if and only if the age is under 18; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0376 | {"name": "Morgan", "age": 57, "country": "Brazil", "plan": "pro"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0346 | {"name": "Riley", "age": 9, "country": "Mexico", "plan": "plus"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0106 | {"name": "Blair", "age": 10, "country": "Spain", "plan": "trial"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0417 | {"name": "Finley", "age": 14, "country": "France", "plan": "plus"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0035 | {"name": "Riley", "age": 13, "country": "Kenya", "plan": "plus"} | A | A | yes |

### Rule 2: 5/5

Articulated rule: Label A if and only if the age is 14 or younger; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0135 | {"name": "Jordan", "age": 47, "country": "Canada", "plan": "basic"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0272 | {"name": "Alex", "age": 12, "country": "Spain", "plan": "trial"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0128 | {"name": "Devin", "age": 47, "country": "Kenya", "plan": "trial"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0484 | {"name": "Alex", "age": 63, "country": "Kenya", "plan": "plus"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0430 | {"name": "Taylor", "age": 32, "country": "United States", "plan": "pro"} | B | B | yes |

### Rule 3: 5/5

Articulated rule: Label A if and only if age is 18 or younger; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0048 | {"name": "Quinn", "age": 37, "country": "Kenya", "plan": "basic"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0254 | {"name": "Devin", "age": 79, "country": "Kenya", "plan": "pro"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0414 | {"name": "Blair", "age": 15, "country": "Spain", "plan": "trial"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0008 | {"name": "Alex", "age": 32, "country": "Brazil", "plan": "student"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0362 | {"name": "Taylor", "age": 9, "country": "Brazil", "plan": "pro"} | A | A | yes |

### Rule 4: 5/5

Articulated rule: Label A if and only if age is 16 or younger.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0378 | {"name": "Casey", "age": 46, "country": "Norway", "plan": "pro"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0297 | {"name": "Alex", "age": 7, "country": "Canada", "plan": "pro"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0145 | {"name": "Casey", "age": 76, "country": "Brazil", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0125 | {"name": "Riley", "age": 36, "country": "Kenya", "plan": "basic"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0381 | {"name": "Casey", "age": 44, "country": "Mexico", "plan": "trial"} | B | B | yes |

### Rule 5: 5/5

Articulated rule: Label A if and only if age is under 18; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0039 | {"name": "Blair", "age": 7, "country": "Norway", "plan": "trial"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0193 | {"name": "Casey", "age": 38, "country": "France", "plan": "student"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0010 | {"name": "Casey", "age": 13, "country": "Canada", "plan": "student"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0157 | {"name": "Kai", "age": 20, "country": "France", "plan": "pro"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0177 | {"name": "Casey", "age": 10, "country": "Kenya", "plan": "pro"} | A | A | yes |

### Rule 6: 5/5

Articulated rule: Label A if and only if the age is under 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0258 | {"name": "Blair", "age": 30, "country": "Mexico", "plan": "student"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0292 | {"name": "Finley", "age": 19, "country": "United States", "plan": "plus"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0361 | {"name": "Finley", "age": 14, "country": "Japan", "plan": "basic"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0411 | {"name": "Finley", "age": 9, "country": "Canada", "plan": "basic"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0472 | {"name": "Kai", "age": 6, "country": "Kenya", "plan": "basic"} | A | A | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the age is 17 or younger.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0156 | {"name": "Harper", "age": 76, "country": "France", "plan": "student"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0328 | {"name": "Riley", "age": 38, "country": "India", "plan": "pro"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0330 | {"name": "Harper", "age": 70, "country": "Brazil", "plan": "trial"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0435 | {"name": "Alex", "age": 49, "country": "Japan", "plan": "plus"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0369 | {"name": "Blair", "age": 28, "country": "Canada", "plan": "student"} | B | B | yes |

### Rule 8: 5/5

Articulated rule: Label A if and only if age is less than 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0412 | {"name": "Taylor", "age": 13, "country": "Brazil", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0277 | {"name": "Kai", "age": 46, "country": "Norway", "plan": "trial"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0463 | {"name": "Jordan", "age": 52, "country": "Spain", "plan": "student"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0027 | {"name": "Harper", "age": 6, "country": "Norway", "plan": "plus"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0104 | {"name": "Devin", "age": 68, "country": "Japan", "plan": "student"} | B | B | yes |

### Rule 9: 5/5

Articulated rule: Label A if and only if age is under 18; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0103 | {"name": "Riley", "age": 32, "country": "India", "plan": "basic"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0122 | {"name": "Devin", "age": 6, "country": "Kenya", "plan": "student"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0063 | {"name": "Quinn", "age": 73, "country": "United States", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0488 | {"name": "Riley", "age": 59, "country": "Japan", "plan": "plus"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0341 | {"name": "Quinn", "age": 10, "country": "Japan", "plan": "basic"} | A | A | yes |

### Rule 10: 5/5

Articulated rule: Label A if and only if age is less than 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0040 | {"name": "Alex", "age": 70, "country": "Kenya", "plan": "student"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0298 | {"name": "Blair", "age": 17, "country": "Kenya", "plan": "pro"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0300 | {"name": "Devin", "age": 18, "country": "Spain", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0177 | {"name": "Casey", "age": 10, "country": "Kenya", "plan": "pro"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0409 | {"name": "Casey", "age": 15, "country": "Mexico", "plan": "plus"} | A | A | yes |

### Rule 11: 5/5

Articulated rule: Label A if and only if the age is under 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0068 | {"name": "Jordan", "age": 11, "country": "United States", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0051 | {"name": "Kai", "age": 33, "country": "Kenya", "plan": "plus"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0300 | {"name": "Devin", "age": 18, "country": "Spain", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0208 | {"name": "Riley", "age": 58, "country": "Norway", "plan": "basic"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0163 | {"name": "Sam", "age": 52, "country": "Norway", "plan": "basic"} | B | B | yes |

### Rule 12: 5/5

Articulated rule: Label A if and only if the age is under 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0243 | {"name": "Blair", "age": 7, "country": "Spain", "plan": "pro"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0011 | {"name": "Alex", "age": 20, "country": "France", "plan": "pro"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0412 | {"name": "Taylor", "age": 13, "country": "Brazil", "plan": "plus"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0291 | {"name": "Harper", "age": 18, "country": "Mexico", "plan": "pro"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0482 | {"name": "Harper", "age": 74, "country": "France", "plan": "plus"} | B | B | yes |

### Rule 13: 5/5

Articulated rule: Label A if and only if the age is 17 or younger.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0086 | {"name": "Quinn", "age": 5, "country": "Spain", "plan": "student"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0047 | {"name": "Quinn", "age": 13, "country": "France", "plan": "student"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0183 | {"name": "Finley", "age": 7, "country": "United States", "plan": "pro"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0023 | {"name": "Harper", "age": 59, "country": "Spain", "plan": "pro"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0482 | {"name": "Harper", "age": 74, "country": "France", "plan": "plus"} | B | B | yes |

### Rule 14: 5/5

Articulated rule: Label A if and only if the age is 17 or younger; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0038 | {"name": "Emery", "age": 26, "country": "United States", "plan": "basic"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0238 | {"name": "Riley", "age": 32, "country": "Norway", "plan": "student"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0260 | {"name": "Harper", "age": 44, "country": "United States", "plan": "pro"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0140 | {"name": "Quinn", "age": 62, "country": "India", "plan": "student"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0362 | {"name": "Taylor", "age": 9, "country": "Brazil", "plan": "pro"} | A | A | yes |

### Rule 15: 4/5

Articulated rule: Label A if and only if age is 15 or less.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0388 | {"name": "Taylor", "age": 52, "country": "Brazil", "plan": "plus"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0456 | {"name": "Harper", "age": 43, "country": "Norway", "plan": "basic"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0298 | {"name": "Blair", "age": 17, "country": "Kenya", "plan": "pro"} | A | B | no |
| 4 | json_age_at_least_18_pool_0444 | {"name": "Alex", "age": 63, "country": "Brazil", "plan": "student"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0151 | {"name": "Morgan", "age": 24, "country": "Canada", "plan": "pro"} | B | B | yes |

### Rule 16: 5/5

Articulated rule: Label A if and only if the age is 14 or less.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0151 | {"name": "Morgan", "age": 24, "country": "Canada", "plan": "pro"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0460 | {"name": "Casey", "age": 12, "country": "United States", "plan": "student"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0343 | {"name": "Quinn", "age": 8, "country": "Canada", "plan": "trial"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0377 | {"name": "Kai", "age": 14, "country": "United States", "plan": "basic"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0240 | {"name": "Alex", "age": 32, "country": "Spain", "plan": "plus"} | B | B | yes |

### Rule 17: 4/5

Articulated rule: Label A if and only if age is less than 14.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0155 | {"name": "Kai", "age": 9, "country": "Kenya", "plan": "pro"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0187 | {"name": "Harper", "age": 6, "country": "Brazil", "plan": "trial"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0341 | {"name": "Quinn", "age": 10, "country": "Japan", "plan": "basic"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0117 | {"name": "Casey", "age": 15, "country": "Norway", "plan": "pro"} | A | B | no |
| 5 | json_age_at_least_18_pool_0337 | {"name": "Emery", "age": 10, "country": "Japan", "plan": "pro"} | A | A | yes |

### Rule 18: 5/5

Articulated rule: Label A if and only if age is less than 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0090 | {"name": "Kai", "age": 71, "country": "Norway", "plan": "trial"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0097 | {"name": "Sam", "age": 58, "country": "Japan", "plan": "basic"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0154 | {"name": "Morgan", "age": 5, "country": "France", "plan": "basic"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0012 | {"name": "Kai", "age": 37, "country": "Kenya", "plan": "basic"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0374 | {"name": "Finley", "age": 79, "country": "Spain", "plan": "plus"} | B | B | yes |

### Rule 19: 5/5

Articulated rule: Label A if and only if age is under 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0036 | {"name": "Morgan", "age": 7, "country": "India", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0387 | {"name": "Kai", "age": 5, "country": "Brazil", "plan": "basic"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0291 | {"name": "Harper", "age": 18, "country": "Mexico", "plan": "pro"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0234 | {"name": "Taylor", "age": 13, "country": "Canada", "plan": "pro"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0078 | {"name": "Alex", "age": 47, "country": "United States", "plan": "basic"} | B | B | yes |

### Rule 20: 5/5

Articulated rule: Label A if and only if age is 14 or less; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0347 | {"name": "Jordan", "age": 40, "country": "Norway", "plan": "pro"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0203 | {"name": "Sam", "age": 13, "country": "Brazil", "plan": "student"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0021 | {"name": "Morgan", "age": 24, "country": "Norway", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0269 | {"name": "Taylor", "age": 9, "country": "Kenya", "plan": "plus"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0258 | {"name": "Blair", "age": 30, "country": "Mexico", "plan": "student"} | B | B | yes |

### Rule 21: 5/5

Articulated rule: Label A if and only if age is 17 or younger; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0470 | {"name": "Finley", "age": 8, "country": "Japan", "plan": "basic"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0095 | {"name": "Harper", "age": 34, "country": "Japan", "plan": "student"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0080 | {"name": "Taylor", "age": 14, "country": "United States", "plan": "trial"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0485 | {"name": "Jordan", "age": 7, "country": "India", "plan": "trial"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0004 | {"name": "Harper", "age": 13, "country": "France", "plan": "basic"} | A | A | yes |

### Rule 22: 5/5

Articulated rule: Label A if and only if age is 17 or younger.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0471 | {"name": "Riley", "age": 14, "country": "Canada", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0168 | {"name": "Riley", "age": 11, "country": "India", "plan": "basic"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0184 | {"name": "Harper", "age": 5, "country": "Norway", "plan": "basic"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0177 | {"name": "Casey", "age": 10, "country": "Kenya", "plan": "pro"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0151 | {"name": "Morgan", "age": 24, "country": "Canada", "plan": "pro"} | B | B | yes |

### Rule 23: 5/5

Articulated rule: Label A if and only if age is less than 50.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0338 | {"name": "Taylor", "age": 13, "country": "Kenya", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0367 | {"name": "Jordan", "age": 51, "country": "Canada", "plan": "plus"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0286 | {"name": "Sam", "age": 7, "country": "United States", "plan": "student"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0003 | {"name": "Riley", "age": 16, "country": "Brazil", "plan": "trial"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0457 | {"name": "Harper", "age": 5, "country": "Mexico", "plan": "pro"} | A | A | yes |

### Rule 24: 5/5

Articulated rule: Label A if and only if the age is under 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0288 | {"name": "Emery", "age": 20, "country": "Kenya", "plan": "plus"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0153 | {"name": "Harper", "age": 68, "country": "Norway", "plan": "pro"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0364 | {"name": "Sam", "age": 69, "country": "India", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0058 | {"name": "Sam", "age": 17, "country": "France", "plan": "basic"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0149 | {"name": "Blair", "age": 27, "country": "France", "plan": "plus"} | B | B | yes |

### Rule 25: 5/5

Articulated rule: Label A if and only if age is 17 or under; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0033 | {"name": "Sam", "age": 8, "country": "Norway", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0450 | {"name": "Finley", "age": 39, "country": "Kenya", "plan": "basic"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0229 | {"name": "Morgan", "age": 26, "country": "Mexico", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0309 | {"name": "Morgan", "age": 15, "country": "Japan", "plan": "student"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0428 | {"name": "Blair", "age": 11, "country": "India", "plan": "basic"} | A | A | yes |

### Rule 26: 5/5

Articulated rule: Label A if and only if age is less than 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0105 | {"name": "Quinn", "age": 8, "country": "France", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0091 | {"name": "Devin", "age": 16, "country": "Japan", "plan": "trial"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0221 | {"name": "Devin", "age": 13, "country": "Norway", "plan": "trial"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0290 | {"name": "Casey", "age": 67, "country": "Canada", "plan": "student"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0277 | {"name": "Kai", "age": 46, "country": "Norway", "plan": "trial"} | B | B | yes |

### Rule 27: 5/5

Articulated rule: Label A if and only if age is 17 or younger.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0068 | {"name": "Jordan", "age": 11, "country": "United States", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0345 | {"name": "Emery", "age": 12, "country": "Mexico", "plan": "trial"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0005 | {"name": "Jordan", "age": 14, "country": "United States", "plan": "student"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0072 | {"name": "Morgan", "age": 30, "country": "Canada", "plan": "pro"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0003 | {"name": "Riley", "age": 16, "country": "Brazil", "plan": "trial"} | A | A | yes |

### Rule 28: 5/5

Articulated rule: Label A if and only if the age is under 18; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0113 | {"name": "Devin", "age": 18, "country": "United States", "plan": "basic"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0139 | {"name": "Kai", "age": 12, "country": "Norway", "plan": "student"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0339 | {"name": "Alex", "age": 27, "country": "United States", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0073 | {"name": "Finley", "age": 23, "country": "India", "plan": "plus"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0063 | {"name": "Quinn", "age": 73, "country": "United States", "plan": "plus"} | B | B | yes |

### Rule 29: 5/5

Articulated rule: Label A if and only if the age is 14 or less; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0475 | {"name": "Casey", "age": 6, "country": "Japan", "plan": "trial"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0263 | {"name": "Devin", "age": 5, "country": "Brazil", "plan": "trial"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0053 | {"name": "Casey", "age": 66, "country": "Mexico", "plan": "student"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0366 | {"name": "Alex", "age": 11, "country": "Canada", "plan": "plus"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0295 | {"name": "Finley", "age": 6, "country": "Norway", "plan": "pro"} | A | A | yes |

### Rule 30: 5/5

Articulated rule: Label A if and only if age is 13 or younger; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0217 | {"name": "Harper", "age": 31, "country": "Brazil", "plan": "basic"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0138 | {"name": "Casey", "age": 50, "country": "Spain", "plan": "plus"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0296 | {"name": "Finley", "age": 36, "country": "Mexico", "plan": "basic"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0257 | {"name": "Jordan", "age": 56, "country": "Mexico", "plan": "plus"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0319 | {"name": "Finley", "age": 27, "country": "India", "plan": "plus"} | B | B | yes |

### Rule 31: 5/5

Articulated rule: Label A if and only if age is less than 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0172 | {"name": "Harper", "age": 7, "country": "India", "plan": "basic"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0122 | {"name": "Devin", "age": 6, "country": "Kenya", "plan": "student"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0299 | {"name": "Emery", "age": 18, "country": "Brazil", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0323 | {"name": "Devin", "age": 19, "country": "Canada", "plan": "pro"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0085 | {"name": "Morgan", "age": 73, "country": "France", "plan": "student"} | B | B | yes |

### Rule 32: 5/5

Articulated rule: Label A if and only if the age is 17 or younger.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0330 | {"name": "Harper", "age": 70, "country": "Brazil", "plan": "trial"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0301 | {"name": "Taylor", "age": 63, "country": "Spain", "plan": "pro"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0224 | {"name": "Riley", "age": 6, "country": "Mexico", "plan": "pro"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0265 | {"name": "Blair", "age": 77, "country": "Canada", "plan": "student"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0055 | {"name": "Sam", "age": 9, "country": "Kenya", "plan": "plus"} | A | A | yes |

### Rule 33: 5/5

Articulated rule: Label A if and only if the plan is not basic and the age is under 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0082 | {"name": "Jordan", "age": 6, "country": "Japan", "plan": "student"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0366 | {"name": "Alex", "age": 11, "country": "Canada", "plan": "plus"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0413 | {"name": "Alex", "age": 17, "country": "Kenya", "plan": "plus"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0207 | {"name": "Finley", "age": 64, "country": "Canada", "plan": "plus"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0009 | {"name": "Devin", "age": 14, "country": "Canada", "plan": "trial"} | A | A | yes |

### Rule 34: 4/5

Articulated rule: Label A if and only if the age is 13 or younger.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0439 | {"name": "Alex", "age": 18, "country": "Brazil", "plan": "basic"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0282 | {"name": "Sam", "age": 12, "country": "Mexico", "plan": "trial"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0211 | {"name": "Jordan", "age": 8, "country": "Kenya", "plan": "basic"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0066 | {"name": "Riley", "age": 11, "country": "France", "plan": "plus"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0230 | {"name": "Emery", "age": 16, "country": "Kenya", "plan": "pro"} | A | B | no |

### Rule 35: 5/5

Articulated rule: Label A if and only if age is less than 18; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0233 | {"name": "Jordan", "age": 19, "country": "India", "plan": "trial"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0302 | {"name": "Harper", "age": 72, "country": "Canada", "plan": "trial"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0073 | {"name": "Finley", "age": 23, "country": "India", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0417 | {"name": "Finley", "age": 14, "country": "France", "plan": "plus"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0464 | {"name": "Jordan", "age": 58, "country": "Canada", "plan": "trial"} | B | B | yes |

### Rule 36: 5/5

Articulated rule: Label A if and only if the age is under 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0001 | {"name": "Alex", "age": 52, "country": "Kenya", "plan": "trial"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0039 | {"name": "Blair", "age": 7, "country": "Norway", "plan": "trial"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0354 | {"name": "Riley", "age": 5, "country": "United States", "plan": "trial"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0414 | {"name": "Blair", "age": 15, "country": "Spain", "plan": "trial"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0420 | {"name": "Finley", "age": 10, "country": "Japan", "plan": "student"} | A | A | yes |

### Rule 37: 5/5

Articulated rule: Label A if and only if age is 17 or younger; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0497 | {"name": "Emery", "age": 17, "country": "Brazil", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0000 | {"name": "Riley", "age": 8, "country": "France", "plan": "pro"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0110 | {"name": "Emery", "age": 50, "country": "Norway", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0281 | {"name": "Harper", "age": 50, "country": "United States", "plan": "plus"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0241 | {"name": "Finley", "age": 7, "country": "Spain", "plan": "basic"} | A | A | yes |

### Rule 38: 5/5

Articulated rule: Label A if and only if the age is 17 or younger; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0150 | {"name": "Morgan", "age": 11, "country": "India", "plan": "pro"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0116 | {"name": "Quinn", "age": 5, "country": "India", "plan": "trial"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0154 | {"name": "Morgan", "age": 5, "country": "France", "plan": "basic"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0068 | {"name": "Jordan", "age": 11, "country": "United States", "plan": "plus"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0485 | {"name": "Jordan", "age": 7, "country": "India", "plan": "trial"} | A | A | yes |

### Rule 39: 5/5

Articulated rule: Label A if and only if age is 17 or younger.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0050 | {"name": "Finley", "age": 79, "country": "Spain", "plan": "student"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0261 | {"name": "Alex", "age": 13, "country": "Japan", "plan": "pro"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0384 | {"name": "Devin", "age": 63, "country": "Kenya", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0429 | {"name": "Casey", "age": 22, "country": "India", "plan": "basic"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0311 | {"name": "Taylor", "age": 79, "country": "India", "plan": "student"} | B | B | yes |

### Rule 40: 5/5

Articulated rule: Label A if and only if age is less than 20.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0344 | {"name": "Blair", "age": 17, "country": "Mexico", "plan": "basic"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0328 | {"name": "Riley", "age": 38, "country": "India", "plan": "pro"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0150 | {"name": "Morgan", "age": 11, "country": "India", "plan": "pro"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0088 | {"name": "Jordan", "age": 7, "country": "Japan", "plan": "plus"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0418 | {"name": "Harper", "age": 7, "country": "Mexico", "plan": "pro"} | A | A | yes |

### Rule 41: 5/5

Articulated rule: Label A if and only if the age is under 18; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0089 | {"name": "Devin", "age": 63, "country": "France", "plan": "pro"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0305 | {"name": "Morgan", "age": 59, "country": "Mexico", "plan": "pro"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0408 | {"name": "Harper", "age": 20, "country": "Brazil", "plan": "pro"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0112 | {"name": "Blair", "age": 23, "country": "Spain", "plan": "trial"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0424 | {"name": "Alex", "age": 8, "country": "Spain", "plan": "pro"} | A | A | yes |

### Rule 42: 5/5

Articulated rule: Label A if and only if age is less than 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0478 | {"name": "Kai", "age": 32, "country": "Norway", "plan": "basic"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0171 | {"name": "Harper", "age": 8, "country": "Norway", "plan": "plus"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0475 | {"name": "Casey", "age": 6, "country": "Japan", "plan": "trial"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0487 | {"name": "Casey", "age": 76, "country": "United States", "plan": "student"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0125 | {"name": "Riley", "age": 36, "country": "Kenya", "plan": "basic"} | B | B | yes |

### Rule 43: 5/5

Articulated rule: Label A if and only if age is less than 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0005 | {"name": "Jordan", "age": 14, "country": "United States", "plan": "student"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0019 | {"name": "Finley", "age": 51, "country": "Mexico", "plan": "pro"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0091 | {"name": "Devin", "age": 16, "country": "Japan", "plan": "trial"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0307 | {"name": "Taylor", "age": 14, "country": "Mexico", "plan": "plus"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0047 | {"name": "Quinn", "age": 13, "country": "France", "plan": "student"} | A | A | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if age is less than 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0042 | {"name": "Riley", "age": 10, "country": "Spain", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0038 | {"name": "Emery", "age": 26, "country": "United States", "plan": "basic"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0099 | {"name": "Taylor", "age": 32, "country": "France", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0203 | {"name": "Sam", "age": 13, "country": "Brazil", "plan": "student"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0437 | {"name": "Blair", "age": 69, "country": "India", "plan": "plus"} | B | B | yes |

### Rule 45: 5/5

Articulated rule: Label A if and only if age is 17 or younger; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0066 | {"name": "Riley", "age": 11, "country": "France", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0352 | {"name": "Emery", "age": 11, "country": "India", "plan": "plus"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0206 | {"name": "Quinn", "age": 75, "country": "Canada", "plan": "student"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0415 | {"name": "Riley", "age": 59, "country": "Canada", "plan": "student"} | B | B | yes |
| 5 | json_age_at_least_18_pool_0022 | {"name": "Casey", "age": 51, "country": "Canada", "plan": "plus"} | B | B | yes |

### Rule 46: 5/5

Articulated rule: Label A if and only if age is under 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0336 | {"name": "Quinn", "age": 49, "country": "India", "plan": "trial"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0314 | {"name": "Alex", "age": 11, "country": "Kenya", "plan": "pro"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0357 | {"name": "Taylor", "age": 8, "country": "Mexico", "plan": "trial"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0184 | {"name": "Harper", "age": 5, "country": "Norway", "plan": "basic"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0392 | {"name": "Devin", "age": 32, "country": "Japan", "plan": "pro"} | B | B | yes |

### Rule 47: 2/5

Articulated rule: Label A if and only if the age is under 50.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0416 | {"name": "Morgan", "age": 40, "country": "United States", "plan": "plus"} | B | A | no |
| 2 | json_age_at_least_18_pool_0222 | {"name": "Jordan", "age": 9, "country": "Spain", "plan": "pro"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0450 | {"name": "Finley", "age": 39, "country": "Kenya", "plan": "basic"} | B | A | no |
| 4 | json_age_at_least_18_pool_0256 | {"name": "Alex", "age": 41, "country": "Canada", "plan": "trial"} | B | A | no |
| 5 | json_age_at_least_18_pool_0114 | {"name": "Casey", "age": 55, "country": "Canada", "plan": "trial"} | B | B | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if the age is 17 or younger.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0385 | {"name": "Finley", "age": 70, "country": "Canada", "plan": "trial"} | B | B | yes |
| 2 | json_age_at_least_18_pool_0455 | {"name": "Alex", "age": 17, "country": "Kenya", "plan": "pro"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0179 | {"name": "Quinn", "age": 23, "country": "Norway", "plan": "plus"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0170 | {"name": "Quinn", "age": 16, "country": "France", "plan": "basic"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0453 | {"name": "Blair", "age": 17, "country": "Japan", "plan": "basic"} | A | A | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if age is less than 18.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0189 | {"name": "Jordan", "age": 15, "country": "United States", "plan": "plus"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0498 | {"name": "Riley", "age": 12, "country": "Kenya", "plan": "basic"} | A | A | yes |
| 3 | json_age_at_least_18_pool_0234 | {"name": "Taylor", "age": 13, "country": "Canada", "plan": "pro"} | A | A | yes |
| 4 | json_age_at_least_18_pool_0455 | {"name": "Alex", "age": 17, "country": "Kenya", "plan": "pro"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0365 | {"name": "Blair", "age": 54, "country": "Spain", "plan": "basic"} | B | B | yes |

### Rule 50: 3/5

Articulated rule: Label A if and only if age is 14 or below; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0485 | {"name": "Jordan", "age": 7, "country": "India", "plan": "trial"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0237 | {"name": "Kai", "age": 78, "country": "France", "plan": "plus"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0287 | {"name": "Sam", "age": 16, "country": "Canada", "plan": "trial"} | A | B | no |
| 4 | json_age_at_least_18_pool_0304 | {"name": "Emery", "age": 15, "country": "India", "plan": "student"} | A | B | no |
| 5 | json_age_at_least_18_pool_0385 | {"name": "Finley", "age": 70, "country": "Canada", "plan": "trial"} | B | B | yes |

