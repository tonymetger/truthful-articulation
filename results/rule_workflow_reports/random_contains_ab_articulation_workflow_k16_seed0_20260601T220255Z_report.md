# Rule Articulation Workflow: random_contains_ab

Run ID: `random_contains_ab_articulation_workflow_k16_seed0_20260601T220255Z`

Correct prompt-facing rule: Label B iff the string contains the substring ab; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.968
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.968
- Rules with all evals correct: 43
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
| 1 | 4/5 | Label A if and only if the string contains no substring "ab". |
| 2 | 5/5 | Label B if and only if the string contains the substring **"ab"**; otherwise label A. |
| 3 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 4 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 5 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 6 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 7 | 4/5 | Label A if and only if the string contains at least one letter that appears more than once; otherwise label B. |
| 8 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 9 | 5/5 | Label B if and only if the string contains the substring **"ab"**; otherwise label A. |
| 10 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 11 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 12 | 3/5 | Label A if and only if the string contains no letter **b**. |
| 13 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 14 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 15 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 16 | 5/5 | Label B if and only if the string contains the substring **"ab"**. |
| 17 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 18 | 5/5 | Label B if and only if the string contains the substring "ab"; otherwise label A. |
| 19 | 5/5 | Label B if and only if the string contains the substring "ab"; otherwise label A. |
| 20 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 21 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 22 | 5/5 | Label A if and only if the string contains no substring **"ab"**. |
| 23 | 5/5 | Label B if and only if the string contains the substring "ab"; otherwise label A. |
| 24 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 25 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 26 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 27 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 28 | 5/5 | Label B if and only if the string contains the substring **"ab"**. |
| 29 | 5/5 | Label A if and only if the string contains no substring **"ab"**. |
| 30 | 4/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 31 | 5/5 | Label A if and only if the string contains no letter **a**. |
| 32 | 5/5 | Label B if and only if the string contains the substring **"ab"**; otherwise label A. |
| 33 | 4/5 | Label A if and only if the string contains no letter **b**. |
| 34 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 35 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 36 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**; otherwise label B. |
| 37 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 38 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 39 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 40 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 41 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 42 | 5/5 | Label A if and only if the string contains no substring "ab". |
| 43 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 44 | 5/5 | Label A if and only if the string contains no substring **"ab"**. |
| 45 | 4/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 46 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 47 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |
| 48 | 5/5 | Label A if and only if the string contains no substring **"ab"**. |
| 49 | 5/5 | Label A if and only if the string does **not** contain the substring **"ab"**; otherwise label B. |
| 50 | 4/5 | Label A if and only if the string does **not** contain the substring **"ab"**. |

## Detailed Evaluations

### Rule 1: 4/5

Articulated rule: Label A if and only if the string contains no substring "ab".

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0375 | nqvyabzckpsk | B | B | yes |
| 2 | random_contains_ab_pool_0347 | ttfqtmkdf | A | A | yes |
| 3 | random_contains_ab_pool_0104 | abkizpm | B | A | no |
| 4 | random_contains_ab_pool_0417 | bpcjgqlwun | A | A | yes |
| 5 | random_contains_ab_pool_0035 | irqrkab | B | B | yes |

### Rule 2: 5/5

Articulated rule: Label B if and only if the string contains the substring **"ab"**; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0136 | iajo | A | A | yes |
| 2 | random_contains_ab_pool_0271 | vjxdkswabqio | B | B | yes |
| 3 | random_contains_ab_pool_0129 | wabwsarmad | B | B | yes |
| 4 | random_contains_ab_pool_0484 | upydgvblmi | A | A | yes |
| 5 | random_contains_ab_pool_0430 | eapzxgtab | B | B | yes |

### Rule 3: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0048 | kmnlhe | A | A | yes |
| 2 | random_contains_ab_pool_0254 | mmjfmavkabqg | B | B | yes |
| 3 | random_contains_ab_pool_0414 | tuxbzlrpns | A | A | yes |
| 4 | random_contains_ab_pool_0008 | nunpbkz | A | A | yes |
| 5 | random_contains_ab_pool_0363 | abvi | B | B | yes |

### Rule 4: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0378 | aabct | B | B | yes |
| 2 | random_contains_ab_pool_0297 | aopchc | A | A | yes |
| 3 | random_contains_ab_pool_0145 | nikdzeoabqec | B | B | yes |
| 4 | random_contains_ab_pool_0125 | iozxt | A | A | yes |
| 5 | random_contains_ab_pool_0381 | cilmdksemq | A | A | yes |

### Rule 5: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0039 | vaktbl | A | A | yes |
| 2 | random_contains_ab_pool_0193 | cdnab | B | B | yes |
| 3 | random_contains_ab_pool_0010 | yeuhprfb | A | A | yes |
| 4 | random_contains_ab_pool_0157 | bggtaboci | B | B | yes |
| 5 | random_contains_ab_pool_0176 | dwyxabbideba | B | B | yes |

### Rule 6: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0259 | iymql | A | A | yes |
| 2 | random_contains_ab_pool_0292 | dtjd | A | A | yes |
| 3 | random_contains_ab_pool_0361 | icrswjqfw | A | A | yes |
| 4 | random_contains_ab_pool_0411 | bijxccch | A | A | yes |
| 5 | random_contains_ab_pool_0472 | smweabtqg | B | B | yes |

### Rule 7: 4/5

Articulated rule: Label A if and only if the string contains at least one letter that appears more than once; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0156 | gjadlzqhsamb | A | A | yes |
| 2 | random_contains_ab_pool_0329 | xabk | B | B | yes |
| 3 | random_contains_ab_pool_0331 | ygbpafd | A | B | no |
| 4 | random_contains_ab_pool_0436 | orlnwyzxyii | A | A | yes |
| 5 | random_contains_ab_pool_0369 | cgjcgfh | A | A | yes |

### Rule 8: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0412 | kabkeksyc | B | B | yes |
| 2 | random_contains_ab_pool_0277 | eoyfgh | A | A | yes |
| 3 | random_contains_ab_pool_0463 | yabfhp | B | B | yes |
| 4 | random_contains_ab_pool_0027 | iqpuwihwryaj | A | A | yes |
| 5 | random_contains_ab_pool_0104 | abkizpm | B | B | yes |

### Rule 9: 5/5

Articulated rule: Label B if and only if the string contains the substring **"ab"**; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0103 | fhrabjte | B | B | yes |
| 2 | random_contains_ab_pool_0122 | nfaabsb | B | B | yes |
| 3 | random_contains_ab_pool_0063 | wtyngyro | A | A | yes |
| 4 | random_contains_ab_pool_0488 | drwabwvhm | B | B | yes |
| 5 | random_contains_ab_pool_0341 | djojxeniyl | A | A | yes |

### Rule 10: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0040 | fspkaaigqsry | A | A | yes |
| 2 | random_contains_ab_pool_0298 | abbvdowiykio | B | B | yes |
| 3 | random_contains_ab_pool_0300 | abzzk | B | B | yes |
| 4 | random_contains_ab_pool_0177 | cgsvxxacny | A | A | yes |
| 5 | random_contains_ab_pool_0410 | xdvcrhfog | A | A | yes |

### Rule 11: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0068 | abcvufs | B | B | yes |
| 2 | random_contains_ab_pool_0050 | csuezabijyo | B | B | yes |
| 3 | random_contains_ab_pool_0300 | abzzk | B | B | yes |
| 4 | random_contains_ab_pool_0209 | mtimseuea | A | A | yes |
| 5 | random_contains_ab_pool_0163 | rpjxmsouplz | A | A | yes |

### Rule 12: 3/5

Articulated rule: Label A if and only if the string contains no letter **b**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0244 | arxestjv | A | A | yes |
| 2 | random_contains_ab_pool_0011 | knyeudhabx | B | B | yes |
| 3 | random_contains_ab_pool_0412 | kabkeksyc | B | A | no |
| 4 | random_contains_ab_pool_0291 | hgiff | A | A | yes |
| 5 | random_contains_ab_pool_0482 | jabve | B | A | no |

### Rule 13: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0086 | bisqxbvp | A | A | yes |
| 2 | random_contains_ab_pool_0046 | qugrab | B | B | yes |
| 3 | random_contains_ab_pool_0183 | cataobec | A | A | yes |
| 4 | random_contains_ab_pool_0023 | hiwknzkbc | A | A | yes |
| 5 | random_contains_ab_pool_0482 | jabve | B | B | yes |

### Rule 14: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0038 | bmabm | B | B | yes |
| 2 | random_contains_ab_pool_0238 | ikkbovx | A | A | yes |
| 3 | random_contains_ab_pool_0259 | iymql | A | A | yes |
| 4 | random_contains_ab_pool_0140 | hctfnohyvjt | A | A | yes |
| 5 | random_contains_ab_pool_0362 | rurpltpe | A | A | yes |

### Rule 15: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0387 | xqrgwglh | A | A | yes |
| 2 | random_contains_ab_pool_0456 | tdab | B | B | yes |
| 3 | random_contains_ab_pool_0297 | aopchc | A | A | yes |
| 4 | random_contains_ab_pool_0444 | swynukj | A | A | yes |
| 5 | random_contains_ab_pool_0151 | xrhdxzmlab | B | B | yes |

### Rule 16: 5/5

Articulated rule: Label B if and only if the string contains the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0151 | xrhdxzmlab | B | B | yes |
| 2 | random_contains_ab_pool_0460 | abmzu | B | B | yes |
| 3 | random_contains_ab_pool_0343 | lvogj | A | A | yes |
| 4 | random_contains_ab_pool_0377 | bcedzdzmpmfk | A | A | yes |
| 5 | random_contains_ab_pool_0241 | lzndxdvae | A | A | yes |

### Rule 17: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0157 | bggtaboci | B | B | yes |
| 2 | random_contains_ab_pool_0186 | ojtpuwkyjud | A | A | yes |
| 3 | random_contains_ab_pool_0341 | djojxeniyl | A | A | yes |
| 4 | random_contains_ab_pool_0116 | maabhgycsx | B | B | yes |
| 5 | random_contains_ab_pool_0337 | uabrt | B | B | yes |

### Rule 18: 5/5

Articulated rule: Label B if and only if the string contains the substring "ab"; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0089 | zkrggetom | A | A | yes |
| 2 | random_contains_ab_pool_0096 | gjrgi | A | A | yes |
| 3 | random_contains_ab_pool_0155 | coabmgfxoafa | B | B | yes |
| 4 | random_contains_ab_pool_0012 | qoabhvmq | B | B | yes |
| 5 | random_contains_ab_pool_0373 | ilabja | B | B | yes |

### Rule 19: 5/5

Articulated rule: Label B if and only if the string contains the substring "ab"; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0037 | dtqwuundn | A | A | yes |
| 2 | random_contains_ab_pool_0387 | xqrgwglh | A | A | yes |
| 3 | random_contains_ab_pool_0289 | cbvtbb | A | A | yes |
| 4 | random_contains_ab_pool_0233 | cixmpmvfjwjt | A | A | yes |
| 5 | random_contains_ab_pool_0078 | prrh | A | A | yes |

### Rule 20: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0347 | ttfqtmkdf | A | A | yes |
| 2 | random_contains_ab_pool_0204 | edewcolgtfww | A | A | yes |
| 3 | random_contains_ab_pool_0021 | hqvwfob | A | A | yes |
| 4 | random_contains_ab_pool_0269 | awlovpbisvig | A | A | yes |
| 5 | random_contains_ab_pool_0258 | cibwuhu | A | A | yes |

### Rule 21: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0470 | nanab | B | B | yes |
| 2 | random_contains_ab_pool_0095 | lgssabbdeisj | B | B | yes |
| 3 | random_contains_ab_pool_0079 | zhpycbcraark | A | A | yes |
| 4 | random_contains_ab_pool_0485 | cleoabuobu | B | B | yes |
| 5 | random_contains_ab_pool_0004 | pvot | A | A | yes |

### Rule 22: 5/5

Articulated rule: Label A if and only if the string contains no substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0471 | islhizhzxaq | A | A | yes |
| 2 | random_contains_ab_pool_0168 | wabc | B | B | yes |
| 3 | random_contains_ab_pool_0184 | zjbaabf | B | B | yes |
| 4 | random_contains_ab_pool_0177 | cgsvxxacny | A | A | yes |
| 5 | random_contains_ab_pool_0152 | svbcabbvhhpi | B | B | yes |

### Rule 23: 5/5

Articulated rule: Label B if and only if the string contains the substring "ab"; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0338 | zabwctyvdg | B | B | yes |
| 2 | random_contains_ab_pool_0367 | tofsmabeiaoz | B | B | yes |
| 3 | random_contains_ab_pool_0286 | sabjleolbkd | B | B | yes |
| 4 | random_contains_ab_pool_0003 | udvabyqfpu | B | B | yes |
| 5 | random_contains_ab_pool_0457 | kfvasjfao | A | A | yes |

### Rule 24: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0287 | wxtdvhscrhe | A | A | yes |
| 2 | random_contains_ab_pool_0152 | svbcabbvhhpi | B | B | yes |
| 3 | random_contains_ab_pool_0365 | yexab | B | B | yes |
| 4 | random_contains_ab_pool_0058 | abqkpu | B | B | yes |
| 5 | random_contains_ab_pool_0149 | pabbj | B | B | yes |

### Rule 25: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0033 | zwenddgdfz | A | A | yes |
| 2 | random_contains_ab_pool_0450 | clab | B | B | yes |
| 3 | random_contains_ab_pool_0230 | jyphu | A | A | yes |
| 4 | random_contains_ab_pool_0309 | hyxfqttfiv | A | A | yes |
| 5 | random_contains_ab_pool_0429 | ovft | A | A | yes |

### Rule 26: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0105 | msjab | B | B | yes |
| 2 | random_contains_ab_pool_0092 | tvzwl | A | A | yes |
| 3 | random_contains_ab_pool_0220 | osezymbrza | A | A | yes |
| 4 | random_contains_ab_pool_0289 | cbvtbb | A | A | yes |
| 5 | random_contains_ab_pool_0276 | abojcvhkhm | B | B | yes |

### Rule 27: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0068 | abcvufs | B | B | yes |
| 2 | random_contains_ab_pool_0345 | gkabtc | B | B | yes |
| 3 | random_contains_ab_pool_0005 | abadiv | B | B | yes |
| 4 | random_contains_ab_pool_0071 | kiabbf | B | B | yes |
| 5 | random_contains_ab_pool_0003 | udvabyqfpu | B | B | yes |

### Rule 28: 5/5

Articulated rule: Label B if and only if the string contains the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0113 | mjsrfhva | A | A | yes |
| 2 | random_contains_ab_pool_0139 | lwhbaifsbo | A | A | yes |
| 3 | random_contains_ab_pool_0339 | fhuqpay | A | A | yes |
| 4 | random_contains_ab_pool_0073 | abkn | B | B | yes |
| 5 | random_contains_ab_pool_0063 | wtyngyro | A | A | yes |

### Rule 29: 5/5

Articulated rule: Label A if and only if the string contains no substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0475 | nrbln | A | A | yes |
| 2 | random_contains_ab_pool_0262 | jcuymgiabh | B | B | yes |
| 3 | random_contains_ab_pool_0053 | mhmhabm | B | B | yes |
| 4 | random_contains_ab_pool_0365 | yexab | B | B | yes |
| 5 | random_contains_ab_pool_0296 | cehqepjsb | A | A | yes |

### Rule 30: 4/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0217 | ivdsmvwmdoca | A | A | yes |
| 2 | random_contains_ab_pool_0139 | lwhbaifsbo | A | A | yes |
| 3 | random_contains_ab_pool_0296 | cehqepjsb | A | A | yes |
| 4 | random_contains_ab_pool_0257 | atvtabgqrwd | B | A | no |
| 5 | random_contains_ab_pool_0320 | abgvv | B | B | yes |

### Rule 31: 5/5

Articulated rule: Label A if and only if the string contains no letter **a**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0171 | ylqnabhpj | B | B | yes |
| 2 | random_contains_ab_pool_0122 | nfaabsb | B | B | yes |
| 3 | random_contains_ab_pool_0299 | lvjxkuihmaby | B | B | yes |
| 4 | random_contains_ab_pool_0323 | thabqfw | B | B | yes |
| 5 | random_contains_ab_pool_0085 | pabr | B | B | yes |

### Rule 32: 5/5

Articulated rule: Label B if and only if the string contains the substring **"ab"**; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0330 | aeoqxovnqbee | A | A | yes |
| 2 | random_contains_ab_pool_0300 | abzzk | B | B | yes |
| 3 | random_contains_ab_pool_0225 | eilkab | B | B | yes |
| 4 | random_contains_ab_pool_0265 | jojgkgeo | A | A | yes |
| 5 | random_contains_ab_pool_0054 | ctesdcrhtber | A | A | yes |

### Rule 33: 4/5

Articulated rule: Label A if and only if the string contains no letter **b**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0082 | vclbgprcsgzx | A | B | no |
| 2 | random_contains_ab_pool_0364 | zapizd | A | A | yes |
| 3 | random_contains_ab_pool_0413 | keagzgmmexyp | A | A | yes |
| 4 | random_contains_ab_pool_0209 | mtimseuea | A | A | yes |
| 5 | random_contains_ab_pool_0009 | xxuqn | A | A | yes |

### Rule 34: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0440 | iaby | B | B | yes |
| 2 | random_contains_ab_pool_0282 | lkvgdw | A | A | yes |
| 3 | random_contains_ab_pool_0211 | innszqjszp | A | A | yes |
| 4 | random_contains_ab_pool_0066 | wnmonxgt | A | A | yes |
| 5 | random_contains_ab_pool_0231 | gitzsojievi | A | A | yes |

### Rule 35: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0234 | jrhvwvld | A | A | yes |
| 2 | random_contains_ab_pool_0302 | seceeabnmalj | B | B | yes |
| 3 | random_contains_ab_pool_0074 | ioab | B | B | yes |
| 4 | random_contains_ab_pool_0417 | bpcjgqlwun | A | A | yes |
| 5 | random_contains_ab_pool_0464 | ewewtlokvb | A | A | yes |

### Rule 36: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0001 | bahzkd | A | A | yes |
| 2 | random_contains_ab_pool_0040 | fspkaaigqsry | A | A | yes |
| 3 | random_contains_ab_pool_0354 | tvdjvjsabya | B | B | yes |
| 4 | random_contains_ab_pool_0414 | tuxbzlrpns | A | A | yes |
| 5 | random_contains_ab_pool_0420 | amozt | A | A | yes |

### Rule 37: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0497 | eputcaj | A | A | yes |
| 2 | random_contains_ab_pool_0000 | nfabyqd | B | B | yes |
| 3 | random_contains_ab_pool_0110 | bdkk | A | A | yes |
| 4 | random_contains_ab_pool_0281 | bcnjzl | A | A | yes |
| 5 | random_contains_ab_pool_0241 | lzndxdvae | A | A | yes |

### Rule 38: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0150 | kuhkkwlle | A | A | yes |
| 2 | random_contains_ab_pool_0116 | maabhgycsx | B | B | yes |
| 3 | random_contains_ab_pool_0155 | coabmgfxoafa | B | B | yes |
| 4 | random_contains_ab_pool_0070 | dlnhy | A | A | yes |
| 5 | random_contains_ab_pool_0485 | cleoabuobu | B | B | yes |

### Rule 39: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0049 | bjrabo | B | B | yes |
| 2 | random_contains_ab_pool_0262 | jcuymgiabh | B | B | yes |
| 3 | random_contains_ab_pool_0384 | qqdrabpd | B | B | yes |
| 4 | random_contains_ab_pool_0429 | ovft | A | A | yes |
| 5 | random_contains_ab_pool_0311 | sinbiydwwsmg | A | A | yes |

### Rule 40: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0344 | kvpkabpqviy | B | B | yes |
| 2 | random_contains_ab_pool_0327 | pptnmmbjabkd | B | B | yes |
| 3 | random_contains_ab_pool_0149 | pabbj | B | B | yes |
| 4 | random_contains_ab_pool_0088 | zlthvabpqubg | B | B | yes |
| 5 | random_contains_ab_pool_0418 | jmab | B | B | yes |

### Rule 41: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0088 | zlthvabpqubg | B | B | yes |
| 2 | random_contains_ab_pool_0305 | ppoksjcdd | A | A | yes |
| 3 | random_contains_ab_pool_0408 | poculwnrj | A | A | yes |
| 4 | random_contains_ab_pool_0112 | abvesrga | B | B | yes |
| 5 | random_contains_ab_pool_0425 | fuuabrtejlpq | B | B | yes |

### Rule 42: 5/5

Articulated rule: Label A if and only if the string contains no substring "ab".

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0478 | kjyjkn | A | A | yes |
| 2 | random_contains_ab_pool_0171 | ylqnabhpj | B | B | yes |
| 3 | random_contains_ab_pool_0475 | nrbln | A | A | yes |
| 4 | random_contains_ab_pool_0487 | mltpzpwlrzef | A | A | yes |
| 5 | random_contains_ab_pool_0125 | iozxt | A | A | yes |

### Rule 43: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0005 | abadiv | B | B | yes |
| 2 | random_contains_ab_pool_0019 | epabxjwz | B | B | yes |
| 3 | random_contains_ab_pool_0092 | tvzwl | A | A | yes |
| 4 | random_contains_ab_pool_0306 | qhrslayecq | A | A | yes |
| 5 | random_contains_ab_pool_0047 | abqdrvvkae | B | B | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if the string contains no substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0042 | wcngufvv | A | A | yes |
| 2 | random_contains_ab_pool_0038 | bmabm | B | B | yes |
| 3 | random_contains_ab_pool_0098 | errbx | A | A | yes |
| 4 | random_contains_ab_pool_0203 | ayvihuywabl | B | B | yes |
| 5 | random_contains_ab_pool_0437 | txrxnjfnriu | A | A | yes |

### Rule 45: 4/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0066 | wnmonxgt | A | A | yes |
| 2 | random_contains_ab_pool_0351 | jabjrbfpfd | B | A | no |
| 3 | random_contains_ab_pool_0205 | aabncrfh | B | B | yes |
| 4 | random_contains_ab_pool_0415 | pkubkpl | A | A | yes |
| 5 | random_contains_ab_pool_0022 | emvnabysxt | B | B | yes |

### Rule 46: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0337 | uabrt | B | B | yes |
| 2 | random_contains_ab_pool_0314 | smkhabbp | B | B | yes |
| 3 | random_contains_ab_pool_0358 | euwtabsg | B | B | yes |
| 4 | random_contains_ab_pool_0185 | refeabha | B | B | yes |
| 5 | random_contains_ab_pool_0392 | wndndjoifmte | A | A | yes |

### Rule 47: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0416 | yvylz | A | A | yes |
| 2 | random_contains_ab_pool_0220 | osezymbrza | A | A | yes |
| 3 | random_contains_ab_pool_0450 | clab | B | B | yes |
| 4 | random_contains_ab_pool_0255 | vmtqybosabmi | B | B | yes |
| 5 | random_contains_ab_pool_0114 | dkeizaboyclz | B | B | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if the string contains no substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0385 | kldpbab | B | B | yes |
| 2 | random_contains_ab_pool_0456 | tdab | B | B | yes |
| 3 | random_contains_ab_pool_0179 | rwqfyawda | A | A | yes |
| 4 | random_contains_ab_pool_0171 | ylqnabhpj | B | B | yes |
| 5 | random_contains_ab_pool_0454 | pijab | B | B | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0188 | uabgmcnbbz | B | B | yes |
| 2 | random_contains_ab_pool_0498 | kbontflozoh | A | A | yes |
| 3 | random_contains_ab_pool_0235 | abnkvxwwm | B | B | yes |
| 4 | random_contains_ab_pool_0455 | glabj | B | B | yes |
| 5 | random_contains_ab_pool_0364 | zapizd | A | A | yes |

### Rule 50: 4/5

Articulated rule: Label A if and only if the string does **not** contain the substring **"ab"**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_contains_ab_pool_0485 | cleoabuobu | B | B | yes |
| 2 | random_contains_ab_pool_0237 | rewkaburmg | B | A | no |
| 3 | random_contains_ab_pool_0287 | wxtdvhscrhe | A | A | yes |
| 4 | random_contains_ab_pool_0304 | xozgbnabq | B | B | yes |
| 5 | random_contains_ab_pool_0386 | csabbqzh | B | B | yes |

