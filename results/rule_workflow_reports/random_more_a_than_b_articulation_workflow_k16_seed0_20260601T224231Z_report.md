# Rule Articulation Workflow: random_more_a_than_b

Run ID: `random_more_a_than_b_articulation_workflow_k16_seed0_20260601T224231Z`

Correct prompt-facing rule: Label B iff the string contains more a's than b's; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.808
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.808
- Rules with all evals correct: 21
- Rules with any eval correct: 50

## Settings

- Articulation model: `gpt-5.4`
- Rule-application model: `gpt-5.4`
- k-shot examples per articulated rule: `16`
- Seed: `0`
- Articulation prompt template: `minimal_rule_description`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Rule-Level Results

| Rule | Rule Accuracy | Articulated Rule |
|---:|---:|---|
| 1 | 3/5 | Label A if and only if the string contains more b’s than a’s. |
| 2 | 4/5 | Label A if and only if the string contains more b's than a's. |
| 3 | 3/5 | Label A if and only if the string contains more b’s than a’s. |
| 4 | 2/5 | Label B if and only if the string contains more a’s than b’s. |
| 5 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 6 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 7 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 8 | 5/5 | Label A if and only if the string contains more b's than a's. |
| 9 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 10 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 11 | 5/5 | Label A if and only if the string contains more b's than a's. |
| 12 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 13 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 14 | 3/5 | Label A if and only if the string contains more b's than a's. |
| 15 | 2/5 | Label A if and only if the string contains more b's than a's. |
| 16 | 4/5 | Label A if and only if the string contains more b's than a's. |
| 17 | 2/5 | Label A if and only if the string contains more b’s than a’s. |
| 18 | 4/5 | Label A if and only if the string contains more b's than a's. |
| 19 | 3/5 | Label A if and only if the string contains more b's than a's. |
| 20 | 2/5 | Label A if and only if the string contains more b's than a's. |
| 21 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 22 | 2/5 | Label A if and only if the string contains more b’s than a’s. |
| 23 | 5/5 | Label A if and only if the string contains more b's than a's. |
| 24 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 25 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 26 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 27 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 28 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 29 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 30 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 31 | 3/5 | Label A if and only if the string contains more b's than a's. |
| 32 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 33 | 4/5 | Label A if and only if the string contains more b's than a's. |
| 34 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 35 | 5/5 | Label A if and only if the string contains more b's than a's. |
| 36 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 37 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 38 | 3/5 | Label A if and only if the string contains more b's than a's. |
| 39 | 1/5 | Label A if and only if the input contains an even number of b's. |
| 40 | 5/5 | Label A if and only if the string contains more b's than a's. |
| 41 | 5/5 | Label A if and only if the string contains more b's than a's. |
| 42 | 5/5 | Label A if and only if the string contains more b's than a's. |
| 43 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 44 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 45 | 4/5 | Label A if and only if the string contains more b's than a's. |
| 46 | 4/5 | Label A if and only if the string contains more b’s than a’s. |
| 47 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 48 | 5/5 | Label A if and only if the string contains more b’s than a’s. |
| 49 | 5/5 | Label A if and only if the string contains more b's than a's. |
| 50 | 4/5 | Label A if and only if the string contains more b's than a's. |

## Detailed Evaluations

### Rule 1: 3/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0375 | baaaabaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0348 | aabbbaaaabbb | A | B | no |
| 3 | random_more_a_than_b_pool_0105 | babaaaabaabb | B | B | yes |
| 4 | random_more_a_than_b_pool_0417 | aaaabaabb | B | B | yes |
| 5 | random_more_a_than_b_pool_0035 | baaababbaaab | B | A | no |

### Rule 2: 4/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0135 | babaaaaba | B | B | yes |
| 2 | random_more_a_than_b_pool_0272 | bbbaabbbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0128 | baababaaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0483 | aabababbbab | A | A | yes |
| 5 | random_more_a_than_b_pool_0430 | abaaabaaabb | B | A | no |

### Rule 3: 3/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0048 | baaababaaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0254 | babbabbbba | A | A | yes |
| 3 | random_more_a_than_b_pool_0414 | abaaabaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0008 | aabaaababb | B | A | no |
| 5 | random_more_a_than_b_pool_0363 | abaaaaabbbbb | A | B | no |

### Rule 4: 2/5

Articulated rule: Label B if and only if the string contains more a’s than b’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0378 | aabbbbbbbbb | A | A | yes |
| 2 | random_more_a_than_b_pool_0297 | baaaaabbbbb | A | B | no |
| 3 | random_more_a_than_b_pool_0145 | abbbbaabb | A | B | no |
| 4 | random_more_a_than_b_pool_0124 | abaabaabb | B | A | no |
| 5 | random_more_a_than_b_pool_0381 | bababbbbb | A | A | yes |

### Rule 5: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0039 | bbbaaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0193 | abbbbbabbabb | A | A | yes |
| 3 | random_more_a_than_b_pool_0010 | bbbbbabbbaa | A | A | yes |
| 4 | random_more_a_than_b_pool_0157 | abaaabbbaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0177 | bbbbaaaaba | A | A | yes |

### Rule 6: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0258 | aaababaabb | B | A | no |
| 2 | random_more_a_than_b_pool_0292 | aabbaaaabaab | B | B | yes |
| 3 | random_more_a_than_b_pool_0361 | bbbbbbbbaaa | A | A | yes |
| 4 | random_more_a_than_b_pool_0411 | aaabaaaabbaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0472 | abbbbabaabb | A | A | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0156 | babbbaabaaba | A | A | yes |
| 2 | random_more_a_than_b_pool_0329 | abbabbaaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0331 | bababbba | A | A | yes |
| 4 | random_more_a_than_b_pool_0436 | abbbbabab | A | A | yes |
| 5 | random_more_a_than_b_pool_0369 | baaabaaba | B | B | yes |

### Rule 8: 5/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0412 | baaabbaaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0277 | bbbabaab | A | A | yes |
| 3 | random_more_a_than_b_pool_0463 | aabaaaaabba | B | B | yes |
| 4 | random_more_a_than_b_pool_0027 | bababbaaabba | A | A | yes |
| 5 | random_more_a_than_b_pool_0104 | babababba | A | A | yes |

### Rule 9: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0103 | bbbbaaababab | A | A | yes |
| 2 | random_more_a_than_b_pool_0122 | abbababa | A | B | no |
| 3 | random_more_a_than_b_pool_0063 | abbababbbbba | A | A | yes |
| 4 | random_more_a_than_b_pool_0488 | baabbabab | A | A | yes |
| 5 | random_more_a_than_b_pool_0341 | aaaababaaa | B | B | yes |

### Rule 10: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0040 | abbbaaab | A | B | no |
| 2 | random_more_a_than_b_pool_0298 | aabaaabaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0300 | aabbaabaaba | B | B | yes |
| 4 | random_more_a_than_b_pool_0177 | bbbbaaaaba | A | A | yes |
| 5 | random_more_a_than_b_pool_0410 | bbabbbbaab | A | A | yes |

### Rule 11: 5/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0068 | bbbbabaaba | A | A | yes |
| 2 | random_more_a_than_b_pool_0050 | abbabbbba | A | A | yes |
| 3 | random_more_a_than_b_pool_0300 | aabbaabaaba | B | B | yes |
| 4 | random_more_a_than_b_pool_0209 | aaaaabaabb | B | B | yes |
| 5 | random_more_a_than_b_pool_0163 | bbbbaaab | A | A | yes |

### Rule 12: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0244 | bbbabaabbbbb | A | A | yes |
| 2 | random_more_a_than_b_pool_0011 | bbabbaaaab | A | A | yes |
| 3 | random_more_a_than_b_pool_0413 | aabbbabab | A | A | yes |
| 4 | random_more_a_than_b_pool_0291 | aaabbaab | B | B | yes |
| 5 | random_more_a_than_b_pool_0482 | baaababbbbb | A | A | yes |

### Rule 13: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0086 | bbaabbbab | A | A | yes |
| 2 | random_more_a_than_b_pool_0046 | aaabaaabaaab | B | B | yes |
| 3 | random_more_a_than_b_pool_0183 | aabaabab | B | A | no |
| 4 | random_more_a_than_b_pool_0023 | aabababbaabb | A | A | yes |
| 5 | random_more_a_than_b_pool_0482 | baaababbbbb | A | A | yes |

### Rule 14: 3/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0038 | abaabbaab | B | A | no |
| 2 | random_more_a_than_b_pool_0238 | baabbaab | A | B | no |
| 3 | random_more_a_than_b_pool_0260 | babbaababb | A | A | yes |
| 4 | random_more_a_than_b_pool_0140 | aaaaaabaaaba | B | B | yes |
| 5 | random_more_a_than_b_pool_0362 | babaabbaa | B | B | yes |

### Rule 15: 2/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0387 | aaababab | B | B | yes |
| 2 | random_more_a_than_b_pool_0456 | abbbbaaabbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0297 | baaaaabbbbb | A | B | no |
| 4 | random_more_a_than_b_pool_0444 | aaababbaaba | B | A | no |
| 5 | random_more_a_than_b_pool_0151 | aaabaabbbba | B | A | no |

### Rule 16: 4/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0151 | aaabaabbbba | B | A | no |
| 2 | random_more_a_than_b_pool_0460 | aaababaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0343 | baabbbbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0377 | aaaaaaababab | B | B | yes |
| 5 | random_more_a_than_b_pool_0240 | baaaababaa | B | B | yes |

### Rule 17: 2/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0155 | bbaaaaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0187 | aaabbaba | B | A | no |
| 3 | random_more_a_than_b_pool_0341 | aaaababaaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0117 | aabbaabb | A | B | no |
| 5 | random_more_a_than_b_pool_0337 | abaabbabaab | B | A | no |

### Rule 18: 4/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0089 | babbaaaba | B | A | no |
| 2 | random_more_a_than_b_pool_0097 | aaabbbabaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0154 | bbaaaaaba | B | B | yes |
| 4 | random_more_a_than_b_pool_0012 | aabbbbbaba | A | A | yes |
| 5 | random_more_a_than_b_pool_0373 | aabbbbbbbaa | A | A | yes |

### Rule 19: 3/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0037 | abababab | A | B | no |
| 2 | random_more_a_than_b_pool_0387 | aaababab | B | B | yes |
| 3 | random_more_a_than_b_pool_0291 | aaabbaab | B | A | no |
| 4 | random_more_a_than_b_pool_0233 | aaaaabbaab | B | B | yes |
| 5 | random_more_a_than_b_pool_0078 | aababbbabaaa | B | B | yes |

### Rule 20: 2/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0347 | abaaabba | B | A | no |
| 2 | random_more_a_than_b_pool_0204 | abaababbabb | A | A | yes |
| 3 | random_more_a_than_b_pool_0021 | baaabaaab | B | A | no |
| 4 | random_more_a_than_b_pool_0269 | babaaabbabaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0258 | aaababaabb | B | A | no |

### Rule 21: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0470 | ababbbaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0095 | aaaababbabaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0080 | bbaaabaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0485 | baaaabbbab | A | B | no |
| 5 | random_more_a_than_b_pool_0004 | abaabbabb | A | A | yes |

### Rule 22: 2/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0471 | abaabaab | B | A | no |
| 2 | random_more_a_than_b_pool_0167 | baaaababbbab | A | B | no |
| 3 | random_more_a_than_b_pool_0184 | bbaaabbbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0177 | bbbbaaaaba | A | A | yes |
| 5 | random_more_a_than_b_pool_0151 | aaabaabbbba | B | A | no |

### Rule 23: 5/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0338 | bbaaaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0367 | bbabbababaa | A | A | yes |
| 3 | random_more_a_than_b_pool_0286 | aaababbaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0003 | bbbabababa | A | A | yes |
| 5 | random_more_a_than_b_pool_0457 | ababbbaaa | B | B | yes |

### Rule 24: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0288 | abbbbbaabbaa | A | A | yes |
| 2 | random_more_a_than_b_pool_0153 | abbbbaaab | A | A | yes |
| 3 | random_more_a_than_b_pool_0365 | aaabbabbbaaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0058 | abaabbaaba | B | A | no |
| 5 | random_more_a_than_b_pool_0150 | aaaabaaaa | B | B | yes |

### Rule 25: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0034 | babbabbb | A | A | yes |
| 2 | random_more_a_than_b_pool_0450 | bbaabaabbba | A | A | yes |
| 3 | random_more_a_than_b_pool_0230 | bbabbabba | A | A | yes |
| 4 | random_more_a_than_b_pool_0309 | abbbabaaabb | A | A | yes |
| 5 | random_more_a_than_b_pool_0429 | abbabbab | A | A | yes |

### Rule 26: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0106 | ababababa | B | B | yes |
| 2 | random_more_a_than_b_pool_0091 | bbbaaabb | A | A | yes |
| 3 | random_more_a_than_b_pool_0221 | aaabbaaaaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0289 | abaababaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0277 | bbbabaab | A | A | yes |

### Rule 27: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0068 | bbbbabaaba | A | A | yes |
| 2 | random_more_a_than_b_pool_0345 | aaabbbbbaaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0005 | bbaaaaabb | B | B | yes |
| 4 | random_more_a_than_b_pool_0071 | aabababb | A | A | yes |
| 5 | random_more_a_than_b_pool_0003 | bbbabababa | A | A | yes |

### Rule 28: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0113 | babaaabbbaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0139 | bbbaaaaaabab | B | B | yes |
| 3 | random_more_a_than_b_pool_0339 | babbabba | A | A | yes |
| 4 | random_more_a_than_b_pool_0073 | ababaabbb | A | A | yes |
| 5 | random_more_a_than_b_pool_0063 | abbababbbbba | A | A | yes |

### Rule 29: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0475 | abbababaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0262 | babaabaaaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0053 | babbabaa | A | A | yes |
| 4 | random_more_a_than_b_pool_0365 | aaabbabbbaaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0296 | babbbaaaaab | B | B | yes |

### Rule 30: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0217 | abbaaaabaaba | B | B | yes |
| 2 | random_more_a_than_b_pool_0137 | abbbabab | A | A | yes |
| 3 | random_more_a_than_b_pool_0296 | babbbaaaaab | B | A | no |
| 4 | random_more_a_than_b_pool_0257 | baabaaaaaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0320 | aaababbab | B | B | yes |

### Rule 31: 3/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0172 | baaaaabaabb | B | B | yes |
| 2 | random_more_a_than_b_pool_0122 | abbababa | A | B | no |
| 3 | random_more_a_than_b_pool_0299 | abbbbbab | A | A | yes |
| 4 | random_more_a_than_b_pool_0323 | bbbaabaaaba | B | A | no |
| 5 | random_more_a_than_b_pool_0085 | aaaabaabbb | B | B | yes |

### Rule 32: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0330 | bbaababbbba | A | A | yes |
| 2 | random_more_a_than_b_pool_0300 | aabbaabaaba | B | B | yes |
| 3 | random_more_a_than_b_pool_0225 | bbbaaabbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0265 | aaabaaab | B | B | yes |
| 5 | random_more_a_than_b_pool_0054 | baabaabbbb | A | A | yes |

### Rule 33: 4/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0082 | aaabaaaaaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0364 | ababbaabbbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0413 | aabbbabab | A | A | yes |
| 4 | random_more_a_than_b_pool_0208 | abbababab | A | A | yes |
| 5 | random_more_a_than_b_pool_0009 | aaabaabbb | B | A | no |

### Rule 34: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0441 | aaabbbbb | A | A | yes |
| 2 | random_more_a_than_b_pool_0282 | baabaaab | B | A | no |
| 3 | random_more_a_than_b_pool_0211 | babbaabaab | A | A | yes |
| 4 | random_more_a_than_b_pool_0066 | babbaaabab | A | A | yes |
| 5 | random_more_a_than_b_pool_0230 | bbabbabba | A | A | yes |

### Rule 35: 5/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0233 | aaaaabbaab | B | B | yes |
| 2 | random_more_a_than_b_pool_0302 | aaaabbbabaaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0073 | ababaabbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0416 | bbbbbbbaa | A | A | yes |
| 5 | random_more_a_than_b_pool_0464 | babbaaba | A | A | yes |

### Rule 36: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0001 | ababbbaaba | A | A | yes |
| 2 | random_more_a_than_b_pool_0040 | abbbaaab | A | A | yes |
| 3 | random_more_a_than_b_pool_0353 | bbbabbabb | A | A | yes |
| 4 | random_more_a_than_b_pool_0414 | abaaabaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0420 | abbbbbbaab | A | A | yes |

### Rule 37: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0497 | baaabbbbaba | A | A | yes |
| 2 | random_more_a_than_b_pool_0000 | abaabaabbab | B | A | no |
| 3 | random_more_a_than_b_pool_0110 | babbbbabaa | A | A | yes |
| 4 | random_more_a_than_b_pool_0281 | ababbbbbbb | A | A | yes |
| 5 | random_more_a_than_b_pool_0241 | bbabbababbb | A | A | yes |

### Rule 38: 3/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0150 | aaaabaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0116 | bbabbaaabb | A | A | yes |
| 3 | random_more_a_than_b_pool_0154 | bbaaaaaba | B | B | yes |
| 4 | random_more_a_than_b_pool_0069 | aaaaabaabbb | B | A | no |
| 5 | random_more_a_than_b_pool_0485 | baaaabbbab | A | B | no |

### Rule 39: 1/5

Articulated rule: Label A if and only if the input contains an even number of b's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0049 | aabbabbaaab | B | A | no |
| 2 | random_more_a_than_b_pool_0261 | aaaaaaabbbab | B | A | no |
| 3 | random_more_a_than_b_pool_0384 | bbaaabbaaaaa | B | A | no |
| 4 | random_more_a_than_b_pool_0429 | abbabbab | A | A | yes |
| 5 | random_more_a_than_b_pool_0311 | aababaaaaaa | B | A | no |

### Rule 40: 5/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0344 | aaabaabaabaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0327 | abbaabaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0149 | bbaabaabbaba | A | A | yes |
| 4 | random_more_a_than_b_pool_0088 | babbbaabbab | A | A | yes |
| 5 | random_more_a_than_b_pool_0419 | ababbbaaab | A | A | yes |

### Rule 41: 5/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0088 | babbbaabbab | A | A | yes |
| 2 | random_more_a_than_b_pool_0305 | bbbabababab | A | A | yes |
| 3 | random_more_a_than_b_pool_0408 | baaaaaab | B | B | yes |
| 4 | random_more_a_than_b_pool_0112 | abbabaaabbaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0425 | baabaabaaa | B | B | yes |

### Rule 42: 5/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0478 | aaabbaabbba | B | B | yes |
| 2 | random_more_a_than_b_pool_0171 | bbabbabbaa | A | A | yes |
| 3 | random_more_a_than_b_pool_0475 | abbababaaaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0487 | baabbaaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0125 | abaabbbaab | A | A | yes |

### Rule 43: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0005 | bbaaaaabb | B | B | yes |
| 2 | random_more_a_than_b_pool_0019 | abbbbabbab | A | A | yes |
| 3 | random_more_a_than_b_pool_0091 | bbbaaabb | A | A | yes |
| 4 | random_more_a_than_b_pool_0306 | ababaaab | B | B | yes |
| 5 | random_more_a_than_b_pool_0047 | bbbbaabaab | A | A | yes |

### Rule 44: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0042 | baaabbaaaba | B | B | yes |
| 2 | random_more_a_than_b_pool_0038 | abaabbaab | B | A | no |
| 3 | random_more_a_than_b_pool_0099 | abbababaab | A | A | yes |
| 4 | random_more_a_than_b_pool_0204 | abaababbabb | A | A | yes |
| 5 | random_more_a_than_b_pool_0437 | bbabbaaabab | A | A | yes |

### Rule 45: 4/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0066 | babbaaabab | A | A | yes |
| 2 | random_more_a_than_b_pool_0351 | bbbbabbbaab | A | A | yes |
| 3 | random_more_a_than_b_pool_0206 | aabaabbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0415 | babaaaabba | B | B | yes |
| 5 | random_more_a_than_b_pool_0022 | aaababaab | B | A | no |

### Rule 46: 4/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0337 | abaabbabaab | B | A | no |
| 2 | random_more_a_than_b_pool_0314 | babbaabb | A | A | yes |
| 3 | random_more_a_than_b_pool_0358 | baabbbbbaab | A | A | yes |
| 4 | random_more_a_than_b_pool_0184 | bbaaabbbb | A | A | yes |
| 5 | random_more_a_than_b_pool_0392 | aabaaabbaa | B | B | yes |

### Rule 47: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0417 | aaaabaabb | B | B | yes |
| 2 | random_more_a_than_b_pool_0221 | aaabbaaaaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0450 | bbaabaabbba | A | A | yes |
| 4 | random_more_a_than_b_pool_0255 | baaaaaabb | B | B | yes |
| 5 | random_more_a_than_b_pool_0114 | aabbabbbbba | A | A | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if the string contains more b’s than a’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0386 | aabbababa | B | B | yes |
| 2 | random_more_a_than_b_pool_0456 | abbbbaaabbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0178 | bbbabbbabb | A | A | yes |
| 4 | random_more_a_than_b_pool_0170 | bbbabbababb | A | A | yes |
| 5 | random_more_a_than_b_pool_0454 | aabbbbaabb | A | A | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0189 | baabaaba | B | B | yes |
| 2 | random_more_a_than_b_pool_0498 | baabbaabaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0234 | bbbbbaba | A | A | yes |
| 4 | random_more_a_than_b_pool_0455 | bbbbbaaaaaaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0364 | ababbaabbbb | A | A | yes |

### Rule 50: 4/5

Articulated rule: Label A if and only if the string contains more b's than a's.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0485 | baaaabbbab | A | B | no |
| 2 | random_more_a_than_b_pool_0237 | babbbbbab | A | A | yes |
| 3 | random_more_a_than_b_pool_0287 | baaaabaaaabb | B | B | yes |
| 4 | random_more_a_than_b_pool_0304 | baabbbbabab | A | A | yes |
| 5 | random_more_a_than_b_pool_0385 | baaababa | B | B | yes |

