# Gold-Rule Application Control: json_age_at_least_18

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_json_age_at_least_18_seed0`

Correct canonical rule: Label A iff the JSON-like record has age >= 18.

Correct prompt-facing rule: Label B iff the JSON-like record has age >= 18; Label A otherwise.

## Summary

- Gold rules tested: `1`
- Rule-application calls: `50`
- Rule-application accuracy: `50/50` = `1.000`
- Nonparseable rate: `0.000`

## Settings

- Rule-application model: `gpt-5.4`
- Seed: `0`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Detailed Evaluations

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | json_age_at_least_18_pool_0362 | {"name": "Taylor", "age": 9, "country": "Brazil", "plan": "pro"} | A | A | yes |
| 2 | json_age_at_least_18_pool_0336 | {"name": "Quinn", "age": 49, "country": "India", "plan": "trial"} | B | B | yes |
| 3 | json_age_at_least_18_pool_0100 | {"name": "Taylor", "age": 22, "country": "Kenya", "plan": "pro"} | B | B | yes |
| 4 | json_age_at_least_18_pool_0403 | {"name": "Blair", "age": 15, "country": "Kenya", "plan": "student"} | A | A | yes |
| 5 | json_age_at_least_18_pool_0034 | {"name": "Finley", "age": 20, "country": "United States", "plan": "plus"} | B | B | yes |
| 6 | json_age_at_least_18_pool_0276 | {"name": "Morgan", "age": 12, "country": "France", "plan": "basic"} | A | A | yes |
| 7 | json_age_at_least_18_pool_0464 | {"name": "Jordan", "age": 58, "country": "Canada", "plan": "trial"} | B | B | yes |
| 8 | json_age_at_least_18_pool_0470 | {"name": "Finley", "age": 8, "country": "Japan", "plan": "basic"} | A | A | yes |
| 9 | json_age_at_least_18_pool_0499 | {"name": "Blair", "age": 17, "country": "Kenya", "plan": "student"} | A | A | yes |
| 10 | json_age_at_least_18_pool_0413 | {"name": "Alex", "age": 17, "country": "Kenya", "plan": "plus"} | A | A | yes |
| 11 | json_age_at_least_18_pool_0253 | {"name": "Harper", "age": 18, "country": "Kenya", "plan": "plus"} | B | B | yes |
| 12 | json_age_at_least_18_pool_0265 | {"name": "Blair", "age": 77, "country": "Canada", "plan": "student"} | B | B | yes |
| 13 | json_age_at_least_18_pool_0234 | {"name": "Taylor", "age": 13, "country": "Canada", "plan": "pro"} | A | A | yes |
| 14 | json_age_at_least_18_pool_0021 | {"name": "Morgan", "age": 24, "country": "Norway", "plan": "plus"} | B | B | yes |
| 15 | json_age_at_least_18_pool_0149 | {"name": "Blair", "age": 27, "country": "France", "plan": "plus"} | B | B | yes |
| 16 | json_age_at_least_18_pool_0354 | {"name": "Riley", "age": 5, "country": "United States", "plan": "trial"} | A | A | yes |
| 17 | json_age_at_least_18_pool_0223 | {"name": "Finley", "age": 5, "country": "Japan", "plan": "basic"} | A | A | yes |
| 18 | json_age_at_least_18_pool_0023 | {"name": "Harper", "age": 59, "country": "Spain", "plan": "pro"} | B | B | yes |
| 19 | json_age_at_least_18_pool_0480 | {"name": "Casey", "age": 57, "country": "Kenya", "plan": "trial"} | B | B | yes |
| 20 | json_age_at_least_18_pool_0004 | {"name": "Harper", "age": 13, "country": "France", "plan": "basic"} | A | A | yes |
| 21 | json_age_at_least_18_pool_0057 | {"name": "Quinn", "age": 62, "country": "Brazil", "plan": "pro"} | B | B | yes |
| 22 | json_age_at_least_18_pool_0212 | {"name": "Casey", "age": 5, "country": "Mexico", "plan": "pro"} | A | A | yes |
| 23 | json_age_at_least_18_pool_0446 | {"name": "Kai", "age": 27, "country": "France", "plan": "plus"} | B | B | yes |
| 24 | json_age_at_least_18_pool_0263 | {"name": "Devin", "age": 5, "country": "Brazil", "plan": "trial"} | A | A | yes |
| 25 | json_age_at_least_18_pool_0118 | {"name": "Blair", "age": 13, "country": "Brazil", "plan": "basic"} | A | A | yes |
| 26 | json_age_at_least_18_pool_0497 | {"name": "Emery", "age": 17, "country": "Brazil", "plan": "plus"} | A | A | yes |
| 27 | json_age_at_least_18_pool_0044 | {"name": "Morgan", "age": 12, "country": "Norway", "plan": "pro"} | A | A | yes |
| 28 | json_age_at_least_18_pool_0062 | {"name": "Harper", "age": 49, "country": "Japan", "plan": "plus"} | B | B | yes |
| 29 | json_age_at_least_18_pool_0315 | {"name": "Quinn", "age": 49, "country": "Brazil", "plan": "student"} | B | B | yes |
| 30 | json_age_at_least_18_pool_0222 | {"name": "Jordan", "age": 9, "country": "Spain", "plan": "pro"} | A | A | yes |
| 31 | json_age_at_least_18_pool_0165 | {"name": "Emery", "age": 13, "country": "Norway", "plan": "plus"} | A | A | yes |
| 32 | json_age_at_least_18_pool_0063 | {"name": "Quinn", "age": 73, "country": "United States", "plan": "plus"} | B | B | yes |
| 33 | json_age_at_least_18_pool_0233 | {"name": "Jordan", "age": 19, "country": "India", "plan": "trial"} | B | B | yes |
| 34 | json_age_at_least_18_pool_0277 | {"name": "Kai", "age": 46, "country": "Norway", "plan": "trial"} | B | B | yes |
| 35 | json_age_at_least_18_pool_0334 | {"name": "Morgan", "age": 10, "country": "Japan", "plan": "trial"} | A | A | yes |
| 36 | json_age_at_least_18_pool_0075 | {"name": "Harper", "age": 75, "country": "India", "plan": "student"} | B | B | yes |
| 37 | json_age_at_least_18_pool_0495 | {"name": "Jordan", "age": 70, "country": "Kenya", "plan": "trial"} | B | B | yes |
| 38 | json_age_at_least_18_pool_0193 | {"name": "Casey", "age": 38, "country": "France", "plan": "student"} | B | B | yes |
| 39 | json_age_at_least_18_pool_0415 | {"name": "Riley", "age": 59, "country": "Canada", "plan": "student"} | B | B | yes |
| 40 | json_age_at_least_18_pool_0058 | {"name": "Sam", "age": 17, "country": "France", "plan": "basic"} | A | A | yes |
| 41 | json_age_at_least_18_pool_0101 | {"name": "Harper", "age": 17, "country": "India", "plan": "student"} | A | A | yes |
| 42 | json_age_at_least_18_pool_0134 | {"name": "Riley", "age": 61, "country": "Spain", "plan": "pro"} | B | B | yes |
| 43 | json_age_at_least_18_pool_0115 | {"name": "Morgan", "age": 20, "country": "United States", "plan": "plus"} | B | B | yes |
| 44 | json_age_at_least_18_pool_0348 | {"name": "Taylor", "age": 74, "country": "United States", "plan": "plus"} | B | B | yes |
| 45 | json_age_at_least_18_pool_0486 | {"name": "Kai", "age": 15, "country": "Canada", "plan": "basic"} | A | A | yes |
| 46 | json_age_at_least_18_pool_0294 | {"name": "Sam", "age": 12, "country": "India", "plan": "pro"} | A | A | yes |
| 47 | json_age_at_least_18_pool_0498 | {"name": "Riley", "age": 12, "country": "Kenya", "plan": "basic"} | A | A | yes |
| 48 | json_age_at_least_18_pool_0387 | {"name": "Kai", "age": 5, "country": "Brazil", "plan": "basic"} | A | A | yes |
| 49 | json_age_at_least_18_pool_0252 | {"name": "Kai", "age": 51, "country": "United States", "plan": "trial"} | B | B | yes |
| 50 | json_age_at_least_18_pool_0091 | {"name": "Devin", "age": 16, "country": "Japan", "plan": "trial"} | A | A | yes |
