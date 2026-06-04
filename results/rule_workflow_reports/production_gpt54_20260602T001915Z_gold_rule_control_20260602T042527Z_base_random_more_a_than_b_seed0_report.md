# Gold-Rule Application Control: random_more_a_than_b

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_random_more_a_than_b_seed0`

Correct canonical rule: Label A iff the string contains more a's than b's.

Correct prompt-facing rule: Label B iff the string contains more a's than b's; Label A otherwise.

## Summary

- Gold rules tested: `1`
- Rule-application calls: `50`
- Rule-application accuracy: `46/50` = `0.920`
- Nonparseable rate: `0.000`

## Settings

- Rule-application model: `gpt-5.4`
- Seed: `0`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Detailed Evaluations

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0362 | babaabbaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0336 | aababaabbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0100 | abbabaabaabb | A | A | yes |
| 4 | random_more_a_than_b_pool_0403 | abaaaabb | B | A | no |
| 5 | random_more_a_than_b_pool_0034 | babbabbb | A | A | yes |
| 6 | random_more_a_than_b_pool_0276 | baaaaabbb | B | A | no |
| 7 | random_more_a_than_b_pool_0464 | babbaaba | A | A | yes |
| 8 | random_more_a_than_b_pool_0470 | ababbbaaaa | B | B | yes |
| 9 | random_more_a_than_b_pool_0499 | aaabbabb | A | A | yes |
| 10 | random_more_a_than_b_pool_0413 | aabbbabab | A | A | yes |
| 11 | random_more_a_than_b_pool_0253 | bbbbababbb | A | A | yes |
| 12 | random_more_a_than_b_pool_0265 | aaabaaab | B | B | yes |
| 13 | random_more_a_than_b_pool_0234 | bbbbbaba | A | A | yes |
| 14 | random_more_a_than_b_pool_0021 | baaabaaab | B | B | yes |
| 15 | random_more_a_than_b_pool_0149 | bbaabaabbaba | A | A | yes |
| 16 | random_more_a_than_b_pool_0354 | aabaabbabaaa | B | B | yes |
| 17 | random_more_a_than_b_pool_0223 | bbaabaaaab | B | B | yes |
| 18 | random_more_a_than_b_pool_0023 | aabababbaabb | A | A | yes |
| 19 | random_more_a_than_b_pool_0480 | abaabaaa | B | B | yes |
| 20 | random_more_a_than_b_pool_0004 | abaabbabb | A | A | yes |
| 21 | random_more_a_than_b_pool_0057 | ababaabababb | A | A | yes |
| 22 | random_more_a_than_b_pool_0212 | bbbbabbaaaa | A | A | yes |
| 23 | random_more_a_than_b_pool_0446 | aabbaaaab | B | B | yes |
| 24 | random_more_a_than_b_pool_0263 | bbbbbbaaaba | A | A | yes |
| 25 | random_more_a_than_b_pool_0118 | abababaaba | B | B | yes |
| 26 | random_more_a_than_b_pool_0497 | baaabbbbaba | A | A | yes |
| 27 | random_more_a_than_b_pool_0044 | abaaabbaba | B | B | yes |
| 28 | random_more_a_than_b_pool_0062 | aaaabbbbb | A | A | yes |
| 29 | random_more_a_than_b_pool_0315 | bbaababbb | A | A | yes |
| 30 | random_more_a_than_b_pool_0222 | abbbabba | A | A | yes |
| 31 | random_more_a_than_b_pool_0165 | baaaaaaa | B | B | yes |
| 32 | random_more_a_than_b_pool_0063 | abbababbbbba | A | A | yes |
| 33 | random_more_a_than_b_pool_0233 | aaaaabbaab | B | B | yes |
| 34 | random_more_a_than_b_pool_0277 | bbbabaab | A | A | yes |
| 35 | random_more_a_than_b_pool_0334 | bbaababab | A | A | yes |
| 36 | random_more_a_than_b_pool_0075 | abbbaaabbaa | B | A | no |
| 37 | random_more_a_than_b_pool_0495 | aababbaaab | B | B | yes |
| 38 | random_more_a_than_b_pool_0193 | abbbbbabbabb | A | A | yes |
| 39 | random_more_a_than_b_pool_0415 | babaaaabba | B | B | yes |
| 40 | random_more_a_than_b_pool_0058 | abaabbaaba | B | B | yes |
| 41 | random_more_a_than_b_pool_0101 | baaabbbbbba | A | A | yes |
| 42 | random_more_a_than_b_pool_0134 | aaaaaaaaba | B | B | yes |
| 43 | random_more_a_than_b_pool_0115 | aaaabaaa | B | B | yes |
| 44 | random_more_a_than_b_pool_0348 | aabbbaaaabbb | A | A | yes |
| 45 | random_more_a_than_b_pool_0486 | abbaaaaabb | B | A | no |
| 46 | random_more_a_than_b_pool_0294 | baaabaab | B | B | yes |
| 47 | random_more_a_than_b_pool_0498 | baabbaabaa | B | B | yes |
| 48 | random_more_a_than_b_pool_0387 | aaababab | B | B | yes |
| 49 | random_more_a_than_b_pool_0252 | bbaabaaa | B | B | yes |
| 50 | random_more_a_than_b_pool_0091 | bbbaaabb | A | A | yes |
