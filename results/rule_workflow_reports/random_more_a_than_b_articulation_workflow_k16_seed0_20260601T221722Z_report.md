# Rule Articulation Workflow: random_more_a_than_b

Run ID: `random_more_a_than_b_articulation_workflow_k16_seed0_20260601T221722Z`

Correct prompt-facing rule: Label B iff the string contains more a's than b's; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.592
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.592
- Rules with all evals correct: 5
- Rules with any eval correct: 49

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
| 1 | 2/5 | Label A if and only if the string contains an even number of `a` characters. |
| 2 | 4/5 | Label A if and only if the string contains at least one **bb** substring. |
| 3 | 5/5 | Label A if and only if the string contains more **b**’s than **a**’s; otherwise label B. |
| 4 | 4/5 | Label A if and only if the string contains an even number of `a` characters. |
| 5 | 3/5 | Label A if and only if the string contains an even number of **a**s. |
| 6 | 4/5 | Label A if and only if the string contains exactly two runs of consecutive identical letters. |
| 7 | 3/5 | Label A if and only if the string contains an even number of **b**s. |
| 8 | 3/5 | Label A if and only if the string contains an even number of **b**s. |
| 9 | 4/5 | Label A if and only if the string contains an even number of **a**s. |
| 10 | 3/5 | Label A if and only if the string contains an even number of `a` characters. |
| 11 | 2/5 | Label A if and only if the string contains an even number of **a**s. |
| 12 | 4/5 | Label A if and only if the string contains an even number of `a` characters. |
| 13 | 3/5 | Label A if and only if the string contains an odd number of **b**’s. |
| 14 | 4/5 | Label A if and only if the string contains more **b**s than **a**s; otherwise label B. |
| 15 | 2/5 | Label A if and only if the string contains an even number of **a**s. |
| 16 | 1/5 | Label A if and only if the string contains an odd number of **b**’s. |
| 17 | 0/5 | Label A if and only if the string contains an odd number of **b**s. |
| 18 | 2/5 | Label A if and only if the string contains an even number of **b**’s. |
| 19 | 1/5 | Label A if and only if the string contains an even number of **a**s. |
| 20 | 1/5 | Label A if and only if the string contains an even number of **b**’s. |
| 21 | 1/5 | Label A if and only if the string contains more **a**s than **b**s. |
| 22 | 3/5 | Label A if and only if the string contains an even number of **b**s. |
| 23 | 2/5 | Label A if and only if the string contains an even number of **b**s. |
| 24 | 5/5 | Label A if and only if the string contains more **b**s than **a**s; otherwise label B. |
| 25 | 5/5 | Label A if and only if the string contains an even number of **b**’s. |
| 26 | 3/5 | Label A if and only if the string contains an even number of **b**s. |
| 27 | 4/5 | Label A if and only if the string contains more **b**’s than **a**’s. |
| 28 | 3/5 | Label A if and only if the string contains no occurrence of three consecutive identical letters. |
| 29 | 1/5 | Label A if and only if the string contains an even number of **b**’s. |
| 30 | 2/5 | Label A if and only if the string contains an even number of **a**s. |
| 31 | 2/5 | Label A if and only if the string contains an even number of **b**’s. |
| 32 | 3/5 | Label A if and only if the string contains an odd number of **b**s. |
| 33 | 4/5 | Label A if and only if the string contains an even number of **b**’s. |
| 34 | 4/5 | Label A if and only if the string contains more **b**s than **a**s. |
| 35 | 4/5 | Label A if and only if the string contains an even number of **b**s. |
| 36 | 4/5 | Label A if and only if the string contains an even number of **a**’s. |
| 37 | 4/5 | Label A if and only if the string contains an even number of **b**’s. |
| 38 | 2/5 | Label A if and only if the string contains an even number of `b` characters. |
| 39 | 1/5 | Label A if and only if the string contains an even number of `b` characters. |
| 40 | 3/5 | Label A if and only if the string contains an even number of `a` characters. |
| 41 | 2/5 | Label A if and only if the string contains an even number of **a**s. |
| 42 | 2/5 | Label A if and only if the string contains an even number of **a**s. |
| 43 | 4/5 | Label A if and only if the string contains more **b**s than **a**s; otherwise label B. |
| 44 | 3/5 | Label A if and only if the string contains an even number of **a**’s. |
| 45 | 3/5 | Label A if and only if the string contains an odd number of `b` characters. |
| 46 | 5/5 | Label A if and only if the string contains more **b**’s than **a**’s; otherwise label B. |
| 47 | 2/5 | Label A if and only if the string contains an even number of **a**’s. |
| 48 | 4/5 | Label A if and only if the string contains an even number of transitions between a and b. |
| 49 | 5/5 | Label A if and only if the string contains more **b**s than **a**s; otherwise label B. |
| 50 | 3/5 | Label A if and only if the string contains an even number of **a**s. |

## Detailed Evaluations

### Rule 1: 2/5

Articulated rule: Label A if and only if the string contains an even number of `a` characters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0375 | baaaabaaaa | B | A | no |
| 2 | random_more_a_than_b_pool_0348 | aabbbaaaabbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0105 | babaaaabaabb | B | A | no |
| 4 | random_more_a_than_b_pool_0417 | aaaabaabb | B | B | yes |
| 5 | random_more_a_than_b_pool_0035 | baaababbaaab | B | A | no |

### Rule 2: 4/5

Articulated rule: Label A if and only if the string contains at least one **bb** substring.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0135 | babaaaaba | B | B | yes |
| 2 | random_more_a_than_b_pool_0272 | bbbaabbbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0128 | baababaaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0483 | aabababbbab | A | A | yes |
| 5 | random_more_a_than_b_pool_0430 | abaaabaaabb | B | A | no |

### Rule 3: 5/5

Articulated rule: Label A if and only if the string contains more **b**’s than **a**’s; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0048 | baaababaaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0254 | babbabbbba | A | A | yes |
| 3 | random_more_a_than_b_pool_0414 | abaaabaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0008 | aabaaababb | B | B | yes |
| 5 | random_more_a_than_b_pool_0363 | abaaaaabbbbb | A | A | yes |

### Rule 4: 4/5

Articulated rule: Label A if and only if the string contains an even number of `a` characters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0378 | aabbbbbbbbb | A | A | yes |
| 2 | random_more_a_than_b_pool_0297 | baaaaabbbbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0145 | abbbbaabb | A | A | yes |
| 4 | random_more_a_than_b_pool_0124 | abaabaabb | B | A | no |
| 5 | random_more_a_than_b_pool_0381 | bababbbbb | A | A | yes |

### Rule 5: 3/5

Articulated rule: Label A if and only if the string contains an even number of **a**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0039 | bbbaaaaa | B | A | no |
| 2 | random_more_a_than_b_pool_0193 | abbbbbabbabb | A | A | yes |
| 3 | random_more_a_than_b_pool_0010 | bbbbbabbbaa | A | A | yes |
| 4 | random_more_a_than_b_pool_0157 | abaaabbbaa | B | A | no |
| 5 | random_more_a_than_b_pool_0177 | bbbbaaaaba | A | A | yes |

### Rule 6: 4/5

Articulated rule: Label A if and only if the string contains exactly two runs of consecutive identical letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0258 | aaababaabb | B | B | yes |
| 2 | random_more_a_than_b_pool_0292 | aabbaaaabaab | B | B | yes |
| 3 | random_more_a_than_b_pool_0361 | bbbbbbbbaaa | A | A | yes |
| 4 | random_more_a_than_b_pool_0411 | aaabaaaabbaa | B | A | no |
| 5 | random_more_a_than_b_pool_0472 | abbbbabaabb | A | A | yes |

### Rule 7: 3/5

Articulated rule: Label A if and only if the string contains an even number of **b**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0156 | babbbaabaaba | A | A | yes |
| 2 | random_more_a_than_b_pool_0329 | abbabbaaa | B | A | no |
| 3 | random_more_a_than_b_pool_0331 | bababbba | A | A | yes |
| 4 | random_more_a_than_b_pool_0436 | abbbbabab | A | A | yes |
| 5 | random_more_a_than_b_pool_0369 | baaabaaba | B | A | no |

### Rule 8: 3/5

Articulated rule: Label A if and only if the string contains an even number of **b**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0412 | baaabbaaaaa | B | A | no |
| 2 | random_more_a_than_b_pool_0277 | bbbabaab | A | A | yes |
| 3 | random_more_a_than_b_pool_0463 | aabaaaaabba | B | A | no |
| 4 | random_more_a_than_b_pool_0027 | bababbaaabba | A | A | yes |
| 5 | random_more_a_than_b_pool_0104 | babababba | A | A | yes |

### Rule 9: 4/5

Articulated rule: Label A if and only if the string contains an even number of **a**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0103 | bbbbaaababab | A | A | yes |
| 2 | random_more_a_than_b_pool_0122 | abbababa | A | A | yes |
| 3 | random_more_a_than_b_pool_0063 | abbababbbbba | A | A | yes |
| 4 | random_more_a_than_b_pool_0488 | baabbabab | A | A | yes |
| 5 | random_more_a_than_b_pool_0341 | aaaababaaa | B | A | no |

### Rule 10: 3/5

Articulated rule: Label A if and only if the string contains an even number of `a` characters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0040 | abbbaaab | A | A | yes |
| 2 | random_more_a_than_b_pool_0298 | aabaaabaa | B | A | no |
| 3 | random_more_a_than_b_pool_0300 | aabbaabaaba | B | A | no |
| 4 | random_more_a_than_b_pool_0177 | bbbbaaaaba | A | A | yes |
| 5 | random_more_a_than_b_pool_0410 | bbabbbbaab | A | A | yes |

### Rule 11: 2/5

Articulated rule: Label A if and only if the string contains an even number of **a**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0068 | bbbbabaaba | A | A | yes |
| 2 | random_more_a_than_b_pool_0050 | abbabbbba | A | A | yes |
| 3 | random_more_a_than_b_pool_0300 | aabbaabaaba | B | A | no |
| 4 | random_more_a_than_b_pool_0209 | aaaaabaabb | B | A | no |
| 5 | random_more_a_than_b_pool_0163 | bbbbaaab | A | B | no |

### Rule 12: 4/5

Articulated rule: Label A if and only if the string contains an even number of `a` characters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0244 | bbbabaabbbbb | A | A | yes |
| 2 | random_more_a_than_b_pool_0011 | bbabbaaaab | A | A | yes |
| 3 | random_more_a_than_b_pool_0413 | aabbbabab | A | A | yes |
| 4 | random_more_a_than_b_pool_0291 | aaabbaab | B | A | no |
| 5 | random_more_a_than_b_pool_0482 | baaababbbbb | A | A | yes |

### Rule 13: 3/5

Articulated rule: Label A if and only if the string contains an odd number of **b**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0086 | bbaabbbab | A | A | yes |
| 2 | random_more_a_than_b_pool_0046 | aaabaaabaaab | B | A | no |
| 3 | random_more_a_than_b_pool_0183 | aabaabab | B | A | no |
| 4 | random_more_a_than_b_pool_0023 | aabababbaabb | A | A | yes |
| 5 | random_more_a_than_b_pool_0482 | baaababbbbb | A | A | yes |

### Rule 14: 4/5

Articulated rule: Label A if and only if the string contains more **b**s than **a**s; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0038 | abaabbaab | B | B | yes |
| 2 | random_more_a_than_b_pool_0238 | baabbaab | A | B | no |
| 3 | random_more_a_than_b_pool_0260 | babbaababb | A | A | yes |
| 4 | random_more_a_than_b_pool_0140 | aaaaaabaaaba | B | B | yes |
| 5 | random_more_a_than_b_pool_0362 | babaabbaa | B | B | yes |

### Rule 15: 2/5

Articulated rule: Label A if and only if the string contains an even number of **a**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0387 | aaababab | B | A | no |
| 2 | random_more_a_than_b_pool_0456 | abbbbaaabbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0297 | baaaaabbbbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0444 | aaababbaaba | B | A | no |
| 5 | random_more_a_than_b_pool_0151 | aaabaabbbba | B | A | no |

### Rule 16: 1/5

Articulated rule: Label A if and only if the string contains an odd number of **b**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0151 | aaabaabbbba | B | A | no |
| 2 | random_more_a_than_b_pool_0460 | aaababaa | B | A | no |
| 3 | random_more_a_than_b_pool_0343 | baabbbbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0377 | aaaaaaababab | B | A | no |
| 5 | random_more_a_than_b_pool_0240 | baaaababaa | B | A | no |

### Rule 17: 0/5

Articulated rule: Label A if and only if the string contains an odd number of **b**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0155 | bbaaaaaaa | B | A | no |
| 2 | random_more_a_than_b_pool_0187 | aaabbaba | B | A | no |
| 3 | random_more_a_than_b_pool_0341 | aaaababaaa | B | A | no |
| 4 | random_more_a_than_b_pool_0117 | aabbaabb | A | B | no |
| 5 | random_more_a_than_b_pool_0337 | abaabbabaab | B | A | no |

### Rule 18: 2/5

Articulated rule: Label A if and only if the string contains an even number of **b**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0089 | babbaaaba | B | A | no |
| 2 | random_more_a_than_b_pool_0097 | aaabbbabaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0154 | bbaaaaaba | B | A | no |
| 4 | random_more_a_than_b_pool_0012 | aabbbbbaba | A | B | no |
| 5 | random_more_a_than_b_pool_0373 | aabbbbbbbaa | A | A | yes |

### Rule 19: 1/5

Articulated rule: Label A if and only if the string contains an even number of **a**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0037 | abababab | A | A | yes |
| 2 | random_more_a_than_b_pool_0387 | aaababab | B | A | no |
| 3 | random_more_a_than_b_pool_0291 | aaabbaab | B | A | no |
| 4 | random_more_a_than_b_pool_0233 | aaaaabbaab | B | A | no |
| 5 | random_more_a_than_b_pool_0078 | aababbbabaaa | B | A | no |

### Rule 20: 1/5

Articulated rule: Label A if and only if the string contains an even number of **b**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0347 | abaaabba | B | A | no |
| 2 | random_more_a_than_b_pool_0204 | abaababbabb | A | A | yes |
| 3 | random_more_a_than_b_pool_0021 | baaabaaab | B | A | no |
| 4 | random_more_a_than_b_pool_0269 | babaaabbabaa | B | A | no |
| 5 | random_more_a_than_b_pool_0258 | aaababaabb | B | A | no |

### Rule 21: 1/5

Articulated rule: Label A if and only if the string contains more **a**s than **b**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0470 | ababbbaaaa | B | A | no |
| 2 | random_more_a_than_b_pool_0095 | aaaababbabaa | B | A | no |
| 3 | random_more_a_than_b_pool_0080 | bbaaabaa | B | A | no |
| 4 | random_more_a_than_b_pool_0485 | baaaabbbab | A | A | yes |
| 5 | random_more_a_than_b_pool_0004 | abaabbabb | A | B | no |

### Rule 22: 3/5

Articulated rule: Label A if and only if the string contains an even number of **b**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0471 | abaabaab | B | A | no |
| 2 | random_more_a_than_b_pool_0167 | baaaababbbab | A | A | yes |
| 3 | random_more_a_than_b_pool_0184 | bbaaabbbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0177 | bbbbaaaaba | A | A | yes |
| 5 | random_more_a_than_b_pool_0151 | aaabaabbbba | B | A | no |

### Rule 23: 2/5

Articulated rule: Label A if and only if the string contains an even number of **b**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0338 | bbaaaaaa | B | A | no |
| 2 | random_more_a_than_b_pool_0367 | bbabbababaa | A | A | yes |
| 3 | random_more_a_than_b_pool_0286 | aaababbaa | B | A | no |
| 4 | random_more_a_than_b_pool_0003 | bbbabababa | A | A | yes |
| 5 | random_more_a_than_b_pool_0457 | ababbbaaa | B | A | no |

### Rule 24: 5/5

Articulated rule: Label A if and only if the string contains more **b**s than **a**s; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0288 | abbbbbaabbaa | A | A | yes |
| 2 | random_more_a_than_b_pool_0153 | abbbbaaab | A | A | yes |
| 3 | random_more_a_than_b_pool_0365 | aaabbabbbaaa | B | B | yes |
| 4 | random_more_a_than_b_pool_0058 | abaabbaaba | B | B | yes |
| 5 | random_more_a_than_b_pool_0150 | aaaabaaaa | B | B | yes |

### Rule 25: 5/5

Articulated rule: Label A if and only if the string contains an even number of **b**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0034 | babbabbb | A | A | yes |
| 2 | random_more_a_than_b_pool_0450 | bbaabaabbba | A | A | yes |
| 3 | random_more_a_than_b_pool_0230 | bbabbabba | A | A | yes |
| 4 | random_more_a_than_b_pool_0309 | abbbabaaabb | A | A | yes |
| 5 | random_more_a_than_b_pool_0429 | abbabbab | A | A | yes |

### Rule 26: 3/5

Articulated rule: Label A if and only if the string contains an even number of **b**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0106 | ababababa | B | B | yes |
| 2 | random_more_a_than_b_pool_0091 | bbbaaabb | A | A | yes |
| 3 | random_more_a_than_b_pool_0221 | aaabbaaaaa | B | A | no |
| 4 | random_more_a_than_b_pool_0289 | abaababaa | B | A | no |
| 5 | random_more_a_than_b_pool_0277 | bbbabaab | A | A | yes |

### Rule 27: 4/5

Articulated rule: Label A if and only if the string contains more **b**’s than **a**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0068 | bbbbabaaba | A | A | yes |
| 2 | random_more_a_than_b_pool_0345 | aaabbbbbaaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0005 | bbaaaaabb | B | A | no |
| 4 | random_more_a_than_b_pool_0071 | aabababb | A | A | yes |
| 5 | random_more_a_than_b_pool_0003 | bbbabababa | A | A | yes |

### Rule 28: 3/5

Articulated rule: Label A if and only if the string contains no occurrence of three consecutive identical letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0113 | babaaabbbaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0139 | bbbaaaaaabab | B | B | yes |
| 3 | random_more_a_than_b_pool_0339 | babbabba | A | A | yes |
| 4 | random_more_a_than_b_pool_0073 | ababaabbb | A | B | no |
| 5 | random_more_a_than_b_pool_0063 | abbababbbbba | A | B | no |

### Rule 29: 1/5

Articulated rule: Label A if and only if the string contains an even number of **b**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0475 | abbababaaaa | B | A | no |
| 2 | random_more_a_than_b_pool_0262 | babaabaaaa | B | A | no |
| 3 | random_more_a_than_b_pool_0053 | babbabaa | A | A | yes |
| 4 | random_more_a_than_b_pool_0365 | aaabbabbbaaa | B | A | no |
| 5 | random_more_a_than_b_pool_0296 | babbbaaaaab | B | A | no |

### Rule 30: 2/5

Articulated rule: Label A if and only if the string contains an even number of **a**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0217 | abbaaaabaaba | B | A | no |
| 2 | random_more_a_than_b_pool_0137 | abbbabab | A | A | yes |
| 3 | random_more_a_than_b_pool_0296 | babbbaaaaab | B | A | no |
| 4 | random_more_a_than_b_pool_0257 | baabaaaaaa | B | A | no |
| 5 | random_more_a_than_b_pool_0320 | aaababbab | B | B | yes |

### Rule 31: 2/5

Articulated rule: Label A if and only if the string contains an even number of **b**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0172 | baaaaabaabb | B | A | no |
| 2 | random_more_a_than_b_pool_0122 | abbababa | A | A | yes |
| 3 | random_more_a_than_b_pool_0299 | abbbbbab | A | A | yes |
| 4 | random_more_a_than_b_pool_0323 | bbbaabaaaba | B | A | no |
| 5 | random_more_a_than_b_pool_0085 | aaaabaabbb | B | A | no |

### Rule 32: 3/5

Articulated rule: Label A if and only if the string contains an odd number of **b**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0330 | bbaababbbba | A | A | yes |
| 2 | random_more_a_than_b_pool_0300 | aabbaabaaba | B | A | no |
| 3 | random_more_a_than_b_pool_0225 | bbbaaabbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0265 | aaabaaab | B | A | no |
| 5 | random_more_a_than_b_pool_0054 | baabaabbbb | A | A | yes |

### Rule 33: 4/5

Articulated rule: Label A if and only if the string contains an even number of **b**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0082 | aaabaaaaaaaa | B | B | yes |
| 2 | random_more_a_than_b_pool_0364 | ababbaabbbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0413 | aabbbabab | A | A | yes |
| 4 | random_more_a_than_b_pool_0208 | abbababab | A | A | yes |
| 5 | random_more_a_than_b_pool_0009 | aaabaabbb | B | A | no |

### Rule 34: 4/5

Articulated rule: Label A if and only if the string contains more **b**s than **a**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0441 | aaabbbbb | A | A | yes |
| 2 | random_more_a_than_b_pool_0282 | baabaaab | B | A | no |
| 3 | random_more_a_than_b_pool_0211 | babbaabaab | A | A | yes |
| 4 | random_more_a_than_b_pool_0066 | babbaaabab | A | A | yes |
| 5 | random_more_a_than_b_pool_0230 | bbabbabba | A | A | yes |

### Rule 35: 4/5

Articulated rule: Label A if and only if the string contains an even number of **b**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0233 | aaaaabbaab | B | A | no |
| 2 | random_more_a_than_b_pool_0302 | aaaabbbabaaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0073 | ababaabbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0416 | bbbbbbbaa | A | A | yes |
| 5 | random_more_a_than_b_pool_0464 | babbaaba | A | A | yes |

### Rule 36: 4/5

Articulated rule: Label A if and only if the string contains an even number of **a**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0001 | ababbbaaba | A | A | yes |
| 2 | random_more_a_than_b_pool_0040 | abbbaaab | A | A | yes |
| 3 | random_more_a_than_b_pool_0353 | bbbabbabb | A | A | yes |
| 4 | random_more_a_than_b_pool_0414 | abaaabaa | B | A | no |
| 5 | random_more_a_than_b_pool_0420 | abbbbbbaab | A | A | yes |

### Rule 37: 4/5

Articulated rule: Label A if and only if the string contains an even number of **b**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0497 | baaabbbbaba | A | A | yes |
| 2 | random_more_a_than_b_pool_0000 | abaabaabbab | B | A | no |
| 3 | random_more_a_than_b_pool_0110 | babbbbabaa | A | A | yes |
| 4 | random_more_a_than_b_pool_0281 | ababbbbbbb | A | A | yes |
| 5 | random_more_a_than_b_pool_0241 | bbabbababbb | A | A | yes |

### Rule 38: 2/5

Articulated rule: Label A if and only if the string contains an even number of `b` characters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0150 | aaaabaaaa | B | A | no |
| 2 | random_more_a_than_b_pool_0116 | bbabbaaabb | A | A | yes |
| 3 | random_more_a_than_b_pool_0154 | bbaaaaaba | B | A | no |
| 4 | random_more_a_than_b_pool_0069 | aaaaabaabbb | B | A | no |
| 5 | random_more_a_than_b_pool_0485 | baaaabbbab | A | A | yes |

### Rule 39: 1/5

Articulated rule: Label A if and only if the string contains an even number of `b` characters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0049 | aabbabbaaab | B | A | no |
| 2 | random_more_a_than_b_pool_0261 | aaaaaaabbbab | B | A | no |
| 3 | random_more_a_than_b_pool_0384 | bbaaabbaaaaa | B | A | no |
| 4 | random_more_a_than_b_pool_0429 | abbabbab | A | A | yes |
| 5 | random_more_a_than_b_pool_0311 | aababaaaaaa | B | A | no |

### Rule 40: 3/5

Articulated rule: Label A if and only if the string contains an even number of `a` characters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0344 | aaabaabaabaa | B | A | no |
| 2 | random_more_a_than_b_pool_0327 | abbaabaa | B | A | no |
| 3 | random_more_a_than_b_pool_0149 | bbaabaabbaba | A | A | yes |
| 4 | random_more_a_than_b_pool_0088 | babbbaabbab | A | A | yes |
| 5 | random_more_a_than_b_pool_0419 | ababbbaaab | A | A | yes |

### Rule 41: 2/5

Articulated rule: Label A if and only if the string contains an even number of **a**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0088 | babbbaabbab | A | A | yes |
| 2 | random_more_a_than_b_pool_0305 | bbbabababab | A | A | yes |
| 3 | random_more_a_than_b_pool_0408 | baaaaaab | B | A | no |
| 4 | random_more_a_than_b_pool_0112 | abbabaaabbaa | B | A | no |
| 5 | random_more_a_than_b_pool_0425 | baabaabaaa | B | A | no |

### Rule 42: 2/5

Articulated rule: Label A if and only if the string contains an even number of **a**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0478 | aaabbaabbba | B | A | no |
| 2 | random_more_a_than_b_pool_0171 | bbabbabbaa | A | A | yes |
| 3 | random_more_a_than_b_pool_0475 | abbababaaaa | B | A | no |
| 4 | random_more_a_than_b_pool_0487 | baabbaaa | B | A | no |
| 5 | random_more_a_than_b_pool_0125 | abaabbbaab | A | A | yes |

### Rule 43: 4/5

Articulated rule: Label A if and only if the string contains more **b**s than **a**s; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0005 | bbaaaaabb | B | A | no |
| 2 | random_more_a_than_b_pool_0019 | abbbbabbab | A | A | yes |
| 3 | random_more_a_than_b_pool_0091 | bbbaaabb | A | A | yes |
| 4 | random_more_a_than_b_pool_0306 | ababaaab | B | B | yes |
| 5 | random_more_a_than_b_pool_0047 | bbbbaabaab | A | A | yes |

### Rule 44: 3/5

Articulated rule: Label A if and only if the string contains an even number of **a**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0042 | baaabbaaaba | B | A | no |
| 2 | random_more_a_than_b_pool_0038 | abaabbaab | B | A | no |
| 3 | random_more_a_than_b_pool_0099 | abbababaab | A | A | yes |
| 4 | random_more_a_than_b_pool_0204 | abaababbabb | A | A | yes |
| 5 | random_more_a_than_b_pool_0437 | bbabbaaabab | A | A | yes |

### Rule 45: 3/5

Articulated rule: Label A if and only if the string contains an odd number of `b` characters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0066 | babbaaabab | A | A | yes |
| 2 | random_more_a_than_b_pool_0351 | bbbbabbbaab | A | A | yes |
| 3 | random_more_a_than_b_pool_0206 | aabaabbb | A | A | yes |
| 4 | random_more_a_than_b_pool_0415 | babaaaabba | B | A | no |
| 5 | random_more_a_than_b_pool_0022 | aaababaab | B | A | no |

### Rule 46: 5/5

Articulated rule: Label A if and only if the string contains more **b**’s than **a**’s; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0337 | abaabbabaab | B | B | yes |
| 2 | random_more_a_than_b_pool_0314 | babbaabb | A | A | yes |
| 3 | random_more_a_than_b_pool_0358 | baabbbbbaab | A | A | yes |
| 4 | random_more_a_than_b_pool_0184 | bbaaabbbb | A | A | yes |
| 5 | random_more_a_than_b_pool_0392 | aabaaabbaa | B | B | yes |

### Rule 47: 2/5

Articulated rule: Label A if and only if the string contains an even number of **a**’s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0417 | aaaabaabb | B | A | no |
| 2 | random_more_a_than_b_pool_0221 | aaabbaaaaa | B | A | no |
| 3 | random_more_a_than_b_pool_0450 | bbaabaabbba | A | A | yes |
| 4 | random_more_a_than_b_pool_0255 | baaaaaabb | B | A | no |
| 5 | random_more_a_than_b_pool_0114 | aabbabbbbba | A | A | yes |

### Rule 48: 4/5

Articulated rule: Label A if and only if the string contains an even number of transitions between a and b.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0386 | aabbababa | B | A | no |
| 2 | random_more_a_than_b_pool_0456 | abbbbaaabbb | A | A | yes |
| 3 | random_more_a_than_b_pool_0178 | bbbabbbabb | A | A | yes |
| 4 | random_more_a_than_b_pool_0170 | bbbabbababb | A | A | yes |
| 5 | random_more_a_than_b_pool_0454 | aabbbbaabb | A | A | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if the string contains more **b**s than **a**s; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0189 | baabaaba | B | B | yes |
| 2 | random_more_a_than_b_pool_0498 | baabbaabaa | B | B | yes |
| 3 | random_more_a_than_b_pool_0234 | bbbbbaba | A | A | yes |
| 4 | random_more_a_than_b_pool_0455 | bbbbbaaaaaaa | B | B | yes |
| 5 | random_more_a_than_b_pool_0364 | ababbaabbbb | A | A | yes |

### Rule 50: 3/5

Articulated rule: Label A if and only if the string contains an even number of **a**s.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_more_a_than_b_pool_0485 | baaaabbbab | A | A | yes |
| 2 | random_more_a_than_b_pool_0237 | babbbbbab | A | A | yes |
| 3 | random_more_a_than_b_pool_0287 | baaaabaaaabb | B | A | no |
| 4 | random_more_a_than_b_pool_0304 | baabbbbabab | A | A | yes |
| 5 | random_more_a_than_b_pool_0385 | baaababa | B | A | no |

