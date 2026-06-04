# Rule Articulation Workflow: controlled_sentence_past_tense

Run ID: `production_gpt54_20260602T001915Z_articulation_20260602T011542Z_base_controlled_sentence_past_tense_seed0`

Correct prompt-facing rule: Label B iff the sentence is in past tense; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.964
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.964
- Rules with all evals correct: 47
- Rules with any eval correct: 49

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
| 1 | 5/5 | Label A if and only if the main verb is in present tense; otherwise label B. |
| 2 | 5/5 | Label A if and only if the verb is in present tense; otherwise label B. |
| 3 | 5/5 | Label A if and only if the sentence uses the simple present tense; otherwise label B. |
| 4 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 5 | 5/5 | Label A if and only if the verb is in the simple present tense; otherwise label B. |
| 6 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 7 | 5/5 | Label A if and only if the main verb is in the simple present tense; otherwise label B. |
| 8 | 5/5 | Label A if and only if the verb is in the present tense; otherwise label B. |
| 9 | 5/5 | Label A if and only if the sentence is in the simple present tense; otherwise label B. |
| 10 | 5/5 | Label A if and only if the sentence uses a present-tense verb; otherwise label B. |
| 11 | 0/5 | Label A if and only if the sentence contains an even number of words. |
| 12 | 5/5 | Label A if and only if the verb is in present tense; otherwise label B. |
| 13 | 5/5 | Label A if and only if the verb is in the simple present tense; otherwise label B. |
| 14 | 5/5 | Label A if and only if the verb is in the present tense; otherwise label B. |
| 15 | 5/5 | Label A if and only if the main verb is in present tense; otherwise label B. |
| 16 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 17 | 3/5 | Label A if and only if the sentence’s main verb is in the present tense ending in **-s**; otherwise label B. |
| 18 | 5/5 | Label A if and only if the sentence’s main verb is in the present tense; otherwise label B. |
| 19 | 5/5 | Label A if and only if the sentence is in the simple present tense; otherwise label B. |
| 20 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 21 | 5/5 | Label A if and only if the main verb is in the simple present tense; otherwise label B. |
| 22 | 5/5 | Label A if and only if the sentence uses present tense; otherwise label B. |
| 23 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 24 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 25 | 5/5 | Label A if and only if the main verb is in the present tense. |
| 26 | 5/5 | Label A if and only if the sentence’s verb is in the present tense; otherwise label B. |
| 27 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 28 | 5/5 | Label A if and only if the verb is in the present tense; otherwise label B. |
| 29 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 30 | 5/5 | Label A if and only if the main verb is in present tense; otherwise label B. |
| 31 | 5/5 | Label A if and only if the sentence’s main verb is in the present tense; otherwise label B. |
| 32 | 5/5 | Label A if and only if the main verb is in the simple present tense; otherwise label B. |
| 33 | 5/5 | Label A if and only if the main verb is in the present tense. |
| 34 | 5/5 | Label A if and only if the verb is in simple present tense; Label B if and only if the verb is in simple past tense. |
| 35 | 5/5 | Label A if and only if the sentence is in the simple present tense; otherwise label B. |
| 36 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 37 | 5/5 | Label A if and only if the main verb is in the present tense. |
| 38 | 5/5 | Label A if and only if the verb is in present tense; otherwise label B. |
| 39 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 40 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 41 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 42 | 5/5 | Label A if and only if the verb is in the present tense; otherwise label B. |
| 43 | 5/5 | Label A if and only if the main verb is in simple present tense; otherwise label B. |
| 44 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 45 | 5/5 | Label A if and only if the sentence is in the present tense. |
| 46 | 3/5 | Label A if and only if the sentence contains an adverb or a location phrase, but not both. |
| 47 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 48 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 49 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |
| 50 | 5/5 | Label A if and only if the main verb is in the present tense; otherwise label B. |

## Detailed Evaluations

### Rule 1: 5/5

Articulated rule: Label A if and only if the main verb is in present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0103 | Mia pushed the cart. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0035 | The student threw the ball. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0291 | The students calmly told the news. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0265 | The guests quickly opened the box inside. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0278 | Mia tells the joke. | A | A | yes |

### Rule 2: 5/5

Articulated rule: Label A if and only if the verb is in present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0139 | The neighbors calmly move the table at work. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0278 | Mia tells the joke. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0132 | The nurse sketches the tree. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0002 | Ravi carefully opened the gate. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0265 | The guests quickly opened the box inside. | B | B | yes |

### Rule 3: 5/5

Articulated rule: Label A if and only if the sentence uses the simple present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0050 | The baker takes the seat. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0261 | The cooks watered the flowers at work. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0008 | The scouts find the file. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0216 | The guard quickly repairs the bench at work. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0295 | The guard made the sign. | B | B | yes |

### Rule 4: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0146 | The farmer washes the apple. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0125 | The clerk made the bed. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0190 | The painter covers the pot upstairs. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0013 | The child quietly cleaned the shelf. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0014 | The students carved the handle at home. | B | B | yes |

### Rule 5: 5/5

Articulated rule: Label A if and only if the verb is in the simple present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0203 | The baker took the seat. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0010 | Eli slowly catches the fish downtown. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0167 | Ava recorded the score downtown. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0186 | The mechanic measured the board nearby. | B | B | yes |

### Rule 6: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0265 | The guests quickly opened the box inside. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0298 | Mia tells the story upstairs. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0231 | Iris slowly kept the promise. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0237 | The neighbors slowly lost the ticket at home. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0204 | The guests slowly repaired the fence at work. | B | B | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the main verb is in the simple present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0158 | The guests calmly inspected the engine at work. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0023 | The students clean the table. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0259 | The scouts moved the table inside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0283 | Eli slowly watered the plants at work. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0124 | The children heard the alarm at work. | B | B | yes |

### Rule 8: 5/5

Articulated rule: Label A if and only if the verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0287 | The scouts found the file. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0028 | The baker met the mayor. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0108 | The painter slowly arranged the books downtown. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0150 | The student inspects the roof at home. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0012 | The child slowly records the score upstairs. | A | A | yes |

### Rule 9: 5/5

Articulated rule: Label A if and only if the sentence is in the simple present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0109 | Mia told the story upstairs. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0130 | The guard calmly repairs the bench upstairs. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0067 | The teacher slowly joins the group inside. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0087 | The painter moves the cart at home. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0286 | The coach built the shelf. | B | B | yes |

### Rule 10: 5/5

Articulated rule: Label A if and only if the sentence uses a present-tense verb; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0177 | Nina sketched the statue at home. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0085 | Nina carefully arranges the flowers. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0182 | The child found the file. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0167 | Ava recorded the score downtown. | B | B | yes |

### Rule 11: 0/5

Articulated rule: Label A if and only if the sentence contains an even number of words.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0071 | The students cleaned the floor nearby. | B | A | no |
| 2 | controlled_sentence_past_tense_pool_0054 | The workers quickly counted the votes at home. | B | A | no |
| 3 | controlled_sentence_past_tense_pool_0212 | The guard makes the sign. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0166 | The guard stirs the batter. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0211 | The child finds the file. | A | B | no |

### Rule 12: 5/5

Articulated rule: Label A if and only if the verb is in present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0249 | The scouts hide the gift. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0011 | The students cleaned the table. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0295 | The guard made the sign. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0224 | The coach counted the votes. | B | B | yes |

### Rule 13: 5/5

Articulated rule: Label A if and only if the verb is in the simple present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0088 | Iris quietly sold the apples downtown. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0047 | The gardeners win the prize upstairs. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0183 | The artists quietly catch the ball. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0024 | The chef quietly ground the spices. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0224 | The coach counted the votes. | B | B | yes |

### Rule 14: 5/5

Articulated rule: Label A if and only if the verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0038 | The players slowly weigh the backpack. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0245 | Ravi cleaned the sink. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0266 | Iris calmly folded the towel outside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0145 | The child quietly sketches the tree inside. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0054 | The workers quickly counted the votes at home. | B | B | yes |

### Rule 15: 5/5

Articulated rule: Label A if and only if the main verb is in present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0154 | The nurse checks the ticket nearby. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0185 | The guard slowly fixes the bike upstairs. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0295 | The guard made the sign. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0072 | The guard cleaned the shelf nearby. | B | B | yes |

### Rule 16: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0155 | Ravi carefully labeled the box. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0248 | The volunteers quickly folded the paper. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0102 | Nina slowly opens the shop at home. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0096 | Iris met the guide. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0128 | The scouts hid the gift. | B | B | yes |

### Rule 17: 3/5

Articulated rule: Label A if and only if the sentence’s main verb is in the present tense ending in **-s**; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0153 | Omar lights the lamp upstairs. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0183 | The artists quietly catch the ball. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0116 | Nina carefully arranged the flowers. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0110 | The nurse sketched the tree. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0189 | The children hear the alarm at work. | A | B | no |

### Rule 18: 5/5

Articulated rule: Label A if and only if the sentence’s main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0088 | Iris quietly sold the apples downtown. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0096 | Iris met the guide. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0156 | The volunteers quickly fold the paper. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0011 | The students cleaned the table. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0235 | Zoe calmly teaches the song. | A | A | yes |

### Rule 19: 5/5

Articulated rule: Label A if and only if the sentence is in the simple present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0039 | Iris calmly folds the towel outside. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0297 | Eli paints the sign. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0240 | The mechanic washed the cup downtown. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0083 | The baker meets the mayor. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0176 | The friends send the card. | A | A | yes |

### Rule 20: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0208 | Noah breaks the vase nearby. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0022 | The farmer quickly lit the lamp. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0274 | The mechanic quietly writes the note. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0263 | The clerk repairs the sink. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0210 | The children left the station. | B | B | yes |

### Rule 21: 5/5

Articulated rule: Label A if and only if the main verb is in the simple present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0101 | The farmer moves the table at work. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0085 | Nina carefully arranges the flowers. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0004 | The nurse checked the ticket nearby. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0149 | The volunteers lost the match. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0110 | The nurse sketched the tree. | B | B | yes |

### Rule 22: 5/5

Articulated rule: Label A if and only if the sentence uses present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0172 | Iris hangs the coat at work. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0188 | The guide calmly closes the book. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0181 | Mia slowly hid the key outside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0155 | Ravi carefully labeled the box. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0158 | The guests calmly inspected the engine at work. | B | B | yes |

### Rule 23: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0289 | The neighbors slowly lose the ticket at home. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0003 | Mia told the truth. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0158 | The guests calmly inspected the engine at work. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0042 | The friends teach the class downtown. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0134 | The friends taught the class downtown. | B | B | yes |

### Rule 24: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0290 | Eli quietly covered the table. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0153 | Omar lights the lamp upstairs. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0056 | The cooks paint the fence inside. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0150 | The student inspects the roof at home. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0032 | The guard cleans the shelf nearby. | A | A | yes |

### Rule 25: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0033 | The chef quietly grinds the spices. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0234 | The guests slowly repair the fence at work. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0044 | The students labeled the folder. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0052 | The clerk quickly folded the towel inside. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0230 | The painter slowly arranges the books downtown. | A | A | yes |

### Rule 26: 5/5

Articulated rule: Label A if and only if the sentence’s verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0109 | Mia told the story upstairs. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0095 | The painter buys the lamp. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0226 | The gardeners slowly found the coin. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0296 | Nina slowly opened the shop at home. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0283 | Eli slowly watered the plants at work. | B | B | yes |

### Rule 27: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0072 | The guard cleaned the shelf nearby. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0005 | The mechanic ties the knot. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0075 | Mia quietly chose the seat upstairs. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0003 | Mia told the truth. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0036 | The helper collects the shells downtown. | A | A | yes |

### Rule 28: 5/5

Articulated rule: Label A if and only if the verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0120 | The students carve the handle at home. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0146 | The farmer washes the apple. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0079 | The nurse carefully leaves the room. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0067 | The teacher slowly joins the group inside. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0029 | The cooks calmly grind the coffee. | A | A | yes |

### Rule 29: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0270 | The chef slowly pulls the handle. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0054 | The workers quickly counted the votes at home. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0087 | The painter moves the cart at home. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0254 | Ava covers the table nearby. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0011 | The students cleaned the table. | B | B | yes |

### Rule 30: 5/5

Articulated rule: Label A if and only if the main verb is in present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0220 | Omar writes the answer at work. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0141 | The interns quickly label the jar outside. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0259 | The scouts moved the table inside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0200 | The players slowly weighed the backpack. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0034 | The guard calmly repaired the bench upstairs. | B | B | yes |

### Rule 31: 5/5

Articulated rule: Label A if and only if the sentence’s main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0177 | Nina sketched the statue at home. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0126 | Nina quietly hangs the banner outside. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0089 | Mia slowly hides the key outside. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0179 | The children slowly pushed the door nearby. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0201 | Ava covered the table nearby. | B | B | yes |

### Rule 32: 5/5

Articulated rule: Label A if and only if the main verb is in the simple present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0233 | The farmer washed the apple. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0273 | The student throws the ball. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0058 | The child quietly polished the silver outside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0188 | The guide calmly closes the book. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0080 | The guests calmly inspect the engine at work. | A | A | yes |

### Rule 33: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0084 | Leo makes the cake downtown. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0212 | The guard makes the sign. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0009 | The guide folded the blanket nearby. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0194 | The chef quietly threw the ball downtown. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0005 | The mechanic ties the knot. | A | A | yes |

### Rule 34: 5/5

Articulated rule: Label A if and only if the verb is in simple present tense; Label B if and only if the verb is in simple past tense.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0286 | The coach built the shelf. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0212 | The guard makes the sign. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0065 | The farmer won the game inside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0233 | The farmer washed the apple. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0025 | The guard quickly repaired the bench at work. | B | B | yes |

### Rule 35: 5/5

Articulated rule: Label A if and only if the sentence is in the simple present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0236 | The neighbors meet the guest upstairs. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0078 | The mechanic washes the cup downtown. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0090 | The coach carefully measures the doorway inside. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0260 | Ava carefully stirs the batter. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0029 | The cooks calmly grind the coffee. | A | A | yes |

### Rule 36: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0001 | Iris builds the model. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0006 | The coach counts the votes. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0198 | Mia told the joke. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0036 | The helper collects the shells downtown. | A | A | yes |

### Rule 37: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0000 | The cooks inspected the fence outside. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0115 | The children leave the station. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0290 | Eli quietly covered the table. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0248 | The volunteers quickly folded the paper. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0273 | The student throws the ball. | A | A | yes |

### Rule 38: 5/5

Articulated rule: Label A if and only if the verb is in present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0156 | The volunteers quickly fold the paper. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0123 | Omar wrote the answer at work. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0160 | The painter quickly covered the pot. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0072 | The guard cleaned the shelf nearby. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0141 | The interns quickly label the jar outside. | A | A | yes |

### Rule 39: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0047 | The gardeners win the prize upstairs. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0264 | Noah quietly hangs the banner. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0058 | The child quietly polished the silver outside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0106 | The children quietly catch the fish at work. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0115 | The children leave the station. | A | A | yes |

### Rule 40: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0151 | The helper bought the book downtown. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0090 | The coach carefully measures the doorway inside. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0046 | The helper buys the book downtown. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0166 | The guard stirs the batter. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0170 | The helper catches the fish. | A | A | yes |

### Rule 41: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0090 | The coach carefully measures the doorway inside. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0115 | The children leave the station. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0145 | The child quietly sketches the tree inside. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0079 | The nurse carefully leaves the room. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0083 | The baker meets the mayor. | A | A | yes |

### Rule 42: 5/5

Articulated rule: Label A if and only if the verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0179 | The children slowly pushed the door nearby. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0128 | The scouts hid the gift. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0130 | The guard calmly repairs the bench upstairs. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0234 | The guests slowly repair the fence at work. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0262 | Ravi carefully opens the gate. | A | A | yes |

### Rule 43: 5/5

Articulated rule: Label A if and only if the main verb is in simple present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0005 | The mechanic ties the knot. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0019 | The guard lit the fire. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0096 | Iris met the guide. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0048 | The artists quietly caught the ball. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0257 | The guide calmly hides the note. | A | A | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0046 | The helper buys the book downtown. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0103 | Mia pushed the cart. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0207 | The guide calmly hid the note. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0296 | Nina slowly opened the shop at home. | B | B | yes |

### Rule 45: 5/5

Articulated rule: Label A if and only if the sentence is in the present tense.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0067 | The teacher slowly joins the group inside. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0215 | The workers quickly count the votes at home. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0021 | Leo made the cake downtown. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0202 | Noah finds the coin. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0180 | Iris slowly keeps the promise. | A | A | yes |

### Rule 46: 3/5

Articulated rule: Label A if and only if the sentence contains an adverb or a location phrase, but not both.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0187 | Ravi calmly took the photo inside. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0094 | The artists made the sign. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0230 | The painter slowly arranges the books downtown. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0178 | The guide folds the blanket nearby. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0093 | The baker counts the coins at home. | A | A | yes |

### Rule 47: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0226 | The gardeners slowly found the coin. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0263 | The clerk repairs the sink. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0114 | The painter bought the lamp. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0052 | The clerk quickly folded the towel inside. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0271 | The interns quickly labeled the jar outside. | B | B | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0184 | Omar quietly writes the note. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0176 | The friends send the card. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0167 | Ava recorded the score downtown. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0141 | The interns quickly label the jar outside. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0022 | The farmer quickly lit the lamp. | B | B | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0192 | The farmer quickly keeps the promise at work. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0237 | The neighbors slowly lost the ticket at home. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0038 | The players slowly weigh the backpack. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0211 | The child finds the file. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0182 | The child found the file. | B | B | yes |

### Rule 50: 5/5

Articulated rule: Label A if and only if the main verb is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0242 | Ava hangs the banner downtown. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0294 | The teacher quietly measured the doorway at work. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0262 | Ravi carefully opens the gate. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0013 | The child quietly cleaned the shelf. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0266 | Iris calmly folded the towel outside. | B | B | yes |

