# Rule Articulation Workflow: controlled_sentence_contains_negation

Run ID: `controlled_sentence_contains_negation_articulation_workflow_k16_seed0_20260601T215759Z`

Correct prompt-facing rule: Label B iff the sentence contains an explicit negation marker such as no, not, never, nothing, nowhere, or without; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.984
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.984
- Rules with all evals correct: 46
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
| 1 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it is negated or expresses absence/denial. |
| 2 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative/absence expression. |
| 3 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “never,” “can’t,” “nothing,” “nobody,” or “neither.” |
| 4 | 5/5 | Label A if and only if the sentence is affirmative, while sentences with negation or absence words like “not,” “no,” “without,” or “nobody” are Label B. |
| 5 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it contains a negation or an equivalent negative expression like “not,” “never,” “nothing,” “nobody,” or “can’t.” |
| 6 | 5/5 | Label A if and only if the sentence is affirmative, meaning it states that the action happened or the thing exists; label B if it is negated or says nothing happened/exists. |
| 7 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it contains negation or an absence/without/nobody/nothing-type construction. |
| 8 | 5/5 | Label A if and only if the sentence is affirmative and does not contain a negation like “not,” “never,” “can’t,” or “nothing.” |
| 9 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative quantifier. |
| 10 | 5/5 | Label A if and only if the sentence is affirmative, and label B if it contains negation or an absence/negative construction. |
| 11 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative expression. |
| 12 | 5/5 | Label A if and only if the sentence describes an affirmative event or existence, and Label B if it contains negation, absence, or impossibility. |
| 13 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “no,” “nobody,” “nothing,” “nowhere,” or “neither/nor.” |
| 14 | 5/5 | Label A if and only if the sentence is affirmative, with no negation words like “not,” “never,” “no,” “nothing,” “nowhere,” or “won’t.” |
| 15 | 5/5 | Label A if and only if the sentence is affirmative, while sentences with negation or absence words like “not,” “without,” “nothing,” “neither,” or “can’t” are Label B. |
| 16 | 4/5 | Label A if and only if the sentence is affirmative and describes the subject having, doing, or being able to do something, while negated, absent, or “nothing/nowhere/neither” statements are Label B. |
| 17 | 5/5 | Label A if and only if the sentence is affirmative, with no negation words like “not,” “didn’t,” “never,” “no one,” “nothing,” or “nowhere.” |
| 18 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it is negated or contains a negative quantifier like “no,” “nobody,” or “never.” |
| 19 | 5/5 | Label A if and only if the sentence is affirmative and does not contain a negation word like “not,” “never,” “without,” “neither,” or “won’t.” |
| 20 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “never,” “no,” “nothing,” or “didn’t.” |
| 21 | 5/5 | Label A if and only if the sentence is affirmative or positive in meaning, and Label B if it contains negation or a negative construction. |
| 22 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it contains a negation or negative quantifier like “not,” “never,” “no,” “nothing,” or “nowhere.” |
| 23 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it is negated or contains a negative expression like “not,” “no,” “never,” “neither,” “can’t,” or “nowhere.” |
| 24 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation words like no, not, nobody, nothing, without, neither, or won’t. |
| 25 | 5/5 | Label A if and only if the sentence does **not** contain a negation or absence expression like “not,” “never,” “nothing,” “nowhere,” or “without.” |
| 26 | 4/5 | Label A if and only if the sentence is affirmative, and Label B if and only if it is negated or expresses inability/absence. |
| 27 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it is negated (including words like not, n't, won't, can't, neither...nor). |
| 28 | 5/5 | Label A if and only if the sentence is affirmative and does not contain a negation like “not,” “doesn’t,” “didn’t,” or “nobody/nothing/no one.” |
| 29 | 4/5 | Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “never,” “nothing,” or “won’t.” |
| 30 | 5/5 | Label A if and only if the sentence is affirmative, while Label B if it contains negation or an absence expression like “not,” “no,” “nobody,” “nothing,” “without,” or “neither/nor.” |
| 31 | 5/5 | Label A if and only if the sentence is affirmative, and label B if it contains negation or a negative/absent meaning such as “not,” “never,” “doesn’t,” “without,” or “nowhere.” |
| 32 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “didn’t,” “can’t,” “nothing,” “nowhere,” or “neither.” |
| 33 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “never,” “nothing,” “nowhere,” or “without.” |
| 34 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation words like not, won't, nobody, nothing, neither, or without. |
| 35 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative quantifier/modal. |
| 36 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it contains negation or an equivalent negative construction. |
| 37 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “never,” “no,” “nothing,” “nobody,” “neither,” or “nor.” |
| 38 | 5/5 | Label A if and only if the sentence is affirmative and does not contain a negation like “not,” “never,” “nothing,” or “nowhere.” |
| 39 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation, absence, or impossibility words like “not,” “never,” “can’t,” “won’t,” “nothing,” “nowhere,” or “neither/nor.” |
| 40 | 5/5 | Label A if and only if the sentence is affirmative and does not contain a clear negation such as “not,” “never,” “can’t,” “nobody,” “neither,” or “without.” |
| 41 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation words like **not, no, never, nothing, without, neither/nor**. |
| 42 | 5/5 | Label A if and only if the sentence is affirmative, and label B if it contains negation such as “no,” “nothing,” “nobody,” “never,” or “not.” |
| 43 | 5/5 | Label A if and only if the sentence is affirmative, or contains words like “somewhere,” “something,” “one,” “can,” or a positive action; label B if it is negated or contains “nowhere,” “nothing,” “no,” or “won’t.” |
| 44 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it is negated or contains a negative quantifier like “no,” “nothing,” or “won’t.” |
| 45 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative construction. |
| 46 | 5/5 | Label A if and only if the sentence describes a positive event or possession, and label B if it contains negation or absence (such as “no,” “nothing,” “nowhere,” “neither,” “without,” or “can’t”). |
| 47 | 5/5 | Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “didn’t,” “can’t,” “won’t,” “without,” “nothing,” or “no.” |
| 48 | 5/5 | Label A if and only if the sentence is affirmative and describes the subject doing or having something, while negated statements or statements of absence are labeled B. |
| 49 | 5/5 | Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative/absent quantifier. |
| 50 | 4/5 | Label A if and only if the sentence is affirmative and describes the subject having, doing, or being something; label B if it is negated or expresses absence, inability, or nowhere/nothing. |

## Detailed Evaluations

### Rule 1: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it is negated or expresses absence/denial.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0103 | Finn doesn't pack the green bag. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0035 | Ada didn't fetch the rope. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0291 | Willa won't trim the hedge. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0265 | Faye has no canvas roll. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0278 | Bea clearly closed the window. | A | A | yes |

### Rule 2: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative/absence expression.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0139 | Bea left with the rope. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0278 | Bea clearly closed the window. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0132 | Priya can slice the apple. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0002 | Finn is not fair today. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0265 | Faye has no canvas roll. | B | B | yes |

### Rule 3: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “never,” “can’t,” “nothing,” “nobody,” or “neither.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0050 | Zara will pour the juice. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0261 | Gus has no garden pot. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0008 | Pia was quite lively yesterday. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0216 | Ivan both sang and hummed. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0295 | Nia has nothing in the case. | B | B | yes |

### Rule 4: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, while sentences with negation or absence words like “not,” “no,” “without,” or “nobody” are Label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0146 | Maya has something in the cup. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0125 | Faye didn't mix the batter. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0190 | Sia always tied the ribbon. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0013 | Ada won't wrap the gift. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0014 | Paul found nothing near the garage. | B | B | yes |

### Rule 5: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it contains a negation or an equivalent negative expression like “not,” “never,” “nothing,” “nobody,” or “can’t.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0041 | Kiran did just fold the towel. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0203 | Vera saw nobody near the gate. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0010 | Priya saw someone near the pier. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0167 | Gus neither bowed nor stepped. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0186 | Priya can't slice the apple. | B | B | yes |

### Rule 6: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, meaning it states that the action happened or the thing exists; label B if it is negated or says nothing happened/exists.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0265 | Faye has no canvas roll. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0298 | Rina is quite cheerful today. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0231 | Mina never scanned the page. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0237 | Zoe saw nobody near the trail. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0204 | Eva went nowhere after sunrise. | B | B | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it contains negation or an absence/without/nobody/nothing-type construction.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0158 | Mila found nothing near the pier. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0023 | Eli did carefully pack the green bag. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0259 | Maya doesn't clean the desk. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0283 | Elsa saw nobody near the gate. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0124 | Dana can't bake the bread. | B | B | yes |

### Rule 8: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain a negation like “not,” “never,” “can’t,” or “nothing.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0287 | Nia did not pack the green bag. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0028 | Ivan neither sang nor hummed. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0108 | Sia never tied the ribbon. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0150 | Maya is quite steady today. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0012 | Julia quickly pushed the cart. | A | A | yes |

### Rule 9: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative quantifier.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0109 | Julia never pushed the cart. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0130 | Nia has something in the pan. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0067 | Toby does mark the spot. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0087 | Vera was quite cheerful yesterday. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0286 | Yara has nothing in the drawer. | B | B | yes |

### Rule 10: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and label B if it contains negation or an absence/negative construction.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0041 | Kiran did just fold the towel. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0177 | Liam doesn't water the plant. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0085 | Wes left with the key. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0182 | Leo neither bowed nor stepped. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0167 | Gus neither bowed nor stepped. | B | B | yes |

### Rule 11: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative expression.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0071 | Ravi left without the phone. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0054 | Elsa neither sang nor hummed. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0212 | Kiran is quite careful today. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0166 | Theo found something near the library. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0211 | Sia went somewhere after school. | A | A | yes |

### Rule 12: 5/5

Articulated rule: Label A if and only if the sentence describes an affirmative event or existence, and Label B if it contains negation, absence, or impossibility.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0249 | Uma was quite rested yesterday. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0011 | Maya left without the dish. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0295 | Nia has nothing in the case. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0041 | Kiran did just fold the towel. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0224 | Gus won't bake the bread. | B | B | yes |

### Rule 13: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “no,” “nobody,” “nothing,” “nowhere,” or “neither/nor.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0088 | Toby never dried the shirt. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0047 | Nia can warm the soup. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0183 | Tara did briefly slice the apple. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0024 | Nia has nothing in the pan. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0224 | Gus won't bake the bread. | B | B | yes |

### Rule 14: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, with no negation words like “not,” “never,” “no,” “nothing,” “nowhere,” or “won’t.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0038 | Vito saw someone near the bakery. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0245 | Yara was not eager yesterday. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0266 | Finn won't wash the red cup. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0145 | Elsa saw someone near the gate. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0054 | Elsa neither sang nor hummed. | B | B | yes |

### Rule 15: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, while sentences with negation or absence words like “not,” “without,” “nothing,” “neither,” or “can’t” are Label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0154 | Paul found something near the garage. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0185 | Kiran did quietly paint the wooden tray. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0295 | Nia has nothing in the case. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0041 | Kiran did just fold the towel. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0072 | Vito is not proud today. | B | B | yes |

### Rule 16: 4/5

Articulated rule: Label A if and only if the sentence is affirmative and describes the subject having, doing, or being able to do something, while negated, absent, or “nothing/nowhere/neither” statements are Label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0155 | Kiran left without the card. | B | A | no |
| 2 | controlled_sentence_contains_negation_pool_0248 | Paul can't print the flyer. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0102 | Vera did quickly cover the bowl. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0096 | Liam was not patient yesterday. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0128 | Nia can't warm the soup. | B | B | yes |

### Rule 17: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, with no negation words like “not,” “didn’t,” “never,” “no one,” “nothing,” or “nowhere.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0153 | Faye did mix the batter. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0183 | Tara did briefly slice the apple. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0116 | Keira went nowhere after training. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0110 | Sia went nowhere after school. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0189 | Sara saw someone near the lobby. | A | A | yes |

### Rule 18: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it is negated or contains a negative quantifier like “no,” “nobody,” or “never.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0088 | Toby never dried the shirt. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0096 | Liam was not patient yesterday. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0156 | Sara found something near the trail. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0011 | Maya left without the dish. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0235 | Omar did glue the label. | A | A | yes |

### Rule 19: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain a negation word like “not,” “never,” “without,” “neither,” or “won’t.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0039 | Kai left with the permit. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0297 | Uma has one short rope. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0240 | Holly didn't store the basket. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0083 | Marek is quite cheerful today. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0176 | Elsa both sang and hummed. | A | A | yes |

### Rule 20: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “never,” “no,” “nothing,” or “didn’t.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0208 | Paul can print the flyer. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0022 | Marek is not cheerful today. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0274 | Ravi left with the phone. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0263 | Julia found something near the kitchen. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0210 | Eva saw nobody near the lobby. | B | B | yes |

### Rule 21: 5/5

Articulated rule: Label A if and only if the sentence is affirmative or positive in meaning, and Label B if it contains negation or a negative construction.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0101 | Ben left with the lunch. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0085 | Wes left with the key. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0004 | Rina is not cheerful today. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0149 | Marek doesn't scan the page. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0110 | Sia went nowhere after school. | B | B | yes |

### Rule 22: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it contains a negation or negative quantifier like “not,” “never,” “no,” “nothing,” or “nowhere.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0172 | Eva saw someone near the lobby. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0188 | Pia has something in the jar. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0181 | Kara did not slice the apple. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0155 | Kiran left without the card. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0158 | Mila found nothing near the pier. | B | B | yes |

### Rule 23: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it is negated or contains a negative expression like “not,” “no,” “never,” “neither,” “can’t,” or “nowhere.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0289 | Nia has something in the case. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0003 | Theo didn't label the file. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0158 | Mila found nothing near the pier. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0042 | Dima does start the timer. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0134 | Maya has nothing in the cup. | B | B | yes |

### Rule 24: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like no, not, nobody, nothing, without, neither, or won’t.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0290 | Cora can't clean the desk. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0153 | Faye did mix the batter. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0056 | Eva went somewhere after sunrise. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0150 | Maya is quite steady today. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0032 | Rina found something near the garage. | A | A | yes |

### Rule 25: 5/5

Articulated rule: Label A if and only if the sentence does **not** contain a negation or absence expression like “not,” “never,” “nothing,” “nowhere,” or “without.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0033 | Elsa did warm the soup. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0234 | Ada will wrap the gift. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0044 | Bea never closed the window. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0052 | Reed found nothing near the gate. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0230 | Sam has one garden pot. | A | A | yes |

### Rule 26: 4/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if and only if it is negated or expresses inability/absence.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0109 | Julia never pushed the cart. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0095 | Theo went somewhere after breakfast. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0226 | Keira doesn't serve the salad. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0296 | Bea left without the rope. | B | A | no |
| 5 | controlled_sentence_contains_negation_pool_0283 | Elsa saw nobody near the gate. | B | B | yes |

### Rule 27: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it is negated (including words like not, n't, won't, can't, neither...nor).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0072 | Vito is not proud today. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0005 | Faye has one canvas roll. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0075 | Sam didn't mend the sock. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0003 | Theo didn't label the file. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0036 | Maya does clean the desk. | A | A | yes |

### Rule 28: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain a negation like “not,” “doesn’t,” “didn’t,” or “nobody/nothing/no one.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0120 | Zoe will polish the bell. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0146 | Maya has something in the cup. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0079 | Gus always weighed the melon. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0067 | Toby does mark the spot. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0029 | Grace does cool the tea. | A | A | yes |

### Rule 29: 4/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “never,” “nothing,” or “won’t.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0270 | Vito is quite proud today. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0054 | Elsa neither sang nor hummed. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0087 | Vera was quite cheerful yesterday. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0254 | Mila found something near the pier. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0011 | Maya left without the dish. | B | A | no |

### Rule 30: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, while Label B if it contains negation or an absence expression like “not,” “no,” “nobody,” “nothing,” “without,” or “neither/nor.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0220 | Yara is quite rested today. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0141 | Kara was quite calm yesterday. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0259 | Maya doesn't clean the desk. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0200 | Luca went nowhere after lunch. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0034 | Willa neither blinked nor stared. | B | B | yes |

### Rule 31: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and label B if it contains negation or a negative/absent meaning such as “not,” “never,” “doesn’t,” “without,” or “nowhere.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0177 | Liam doesn't water the plant. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0126 | Hana will shape the clay. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0089 | Marek left with the phone. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0179 | Hana won't shape the clay. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0201 | Sam has no fresh apple. | B | B | yes |

### Rule 32: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “didn’t,” “can’t,” “nothing,” “nowhere,” or “neither.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0233 | Vera saw nobody near the yard. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0273 | Axel did water the plant. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0058 | Priya saw nobody near the pier. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0188 | Pia has something in the jar. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0080 | Leo both bowed and stepped. | A | A | yes |

### Rule 33: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “never,” “nothing,” “nowhere,” or “without.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0084 | Jalen will light the candle. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0212 | Kiran is quite careful today. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0009 | Jalen won't light the candle. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0194 | Omar didn't glue the label. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0005 | Faye has one canvas roll. | A | A | yes |

### Rule 34: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like not, won't, nobody, nothing, neither, or without.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0286 | Yara has nothing in the drawer. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0212 | Kiran is quite careful today. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0065 | Rosa left without the blanket. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0233 | Vera saw nobody near the yard. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0025 | Keira doesn't wash the red cup. | B | B | yes |

### Rule 35: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative quantifier/modal.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0236 | Maya left with the dish. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0078 | Gus has one garden pot. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0090 | Ravi did fix the loose hinge. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0260 | Theo did label the file. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0029 | Grace does cool the tea. | A | A | yes |

### Rule 36: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it contains negation or an equivalent negative construction.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0001 | Nia did clearly pack the green bag. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0041 | Kiran did just fold the towel. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0006 | Kiran left with the card. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0198 | Sara saw nobody near the lobby. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0036 | Maya does clean the desk. | A | A | yes |

### Rule 37: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “never,” “no,” “nothing,” “nobody,” “neither,” or “nor.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0000 | Ivan did not move the chair. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0115 | Kara can trace the pattern. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0290 | Cora can't clean the desk. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0248 | Paul can't print the flyer. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0273 | Axel did water the plant. | A | A | yes |

### Rule 38: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain a negation like “not,” “never,” “nothing,” or “nowhere.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0156 | Sara found something near the trail. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0123 | Rina did not stir the sauce. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0160 | Kara can't trace the pattern. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0072 | Vito is not proud today. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0141 | Kara was quite calm yesterday. | A | A | yes |

### Rule 39: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation, absence, or impossibility words like “not,” “never,” “can’t,” “won’t,” “nothing,” “nowhere,” or “neither/nor.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0047 | Nia can warm the soup. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0264 | Vera saw someone near the gate. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0058 | Priya saw nobody near the pier. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0106 | Keira does serve the salad. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0115 | Kara can trace the pattern. | A | A | yes |

### Rule 40: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain a clear negation such as “not,” “never,” “can’t,” “nobody,” “neither,” or “without.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0151 | Zoe won't polish the bell. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0090 | Ravi did fix the loose hinge. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0046 | Finn does pack the green bag. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0166 | Theo found something near the library. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0170 | Faye both walked and turned. | A | A | yes |

### Rule 41: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like **not, no, never, nothing, without, neither/nor**.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0090 | Ravi did fix the loose hinge. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0115 | Kara can trace the pattern. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0145 | Elsa saw someone near the gate. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0079 | Gus always weighed the melon. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0083 | Marek is quite cheerful today. | A | A | yes |

### Rule 42: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and label B if it contains negation such as “no,” “nothing,” “nobody,” “never,” or “not.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0179 | Hana won't shape the clay. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0128 | Nia can't warm the soup. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0130 | Nia has something in the pan. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0234 | Ada will wrap the gift. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0262 | Lena has one brass bell. | A | A | yes |

### Rule 43: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, or contains words like “somewhere,” “something,” “one,” “can,” or a positive action; label B if it is negated or contains “nowhere,” “nothing,” “no,” or “won’t.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0005 | Faye has one canvas roll. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0019 | Vera is not ready today. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0096 | Liam was not patient yesterday. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0048 | Yara never weighed the melon. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0257 | Ben clearly framed the photo. | A | A | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it is negated or contains a negative quantifier like “no,” “nothing,” or “won’t.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0046 | Finn does pack the green bag. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0041 | Kiran did just fold the towel. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0103 | Finn doesn't pack the green bag. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0207 | Marek left without the phone. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0296 | Bea left without the rope. | B | B | yes |

### Rule 45: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative construction.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0067 | Toby does mark the spot. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0215 | Keira went somewhere after training. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0021 | Julia found nothing near the kitchen. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0202 | Vera is quite ready today. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0180 | Sam has something in the bowl. | A | A | yes |

### Rule 46: 5/5

Articulated rule: Label A if and only if the sentence describes a positive event or possession, and label B if it contains negation or absence (such as “no,” “nothing,” “nowhere,” “neither,” “without,” or “can’t”).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0187 | Finn has nothing in the bowl. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0094 | Elsa didn't warm the soup. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0230 | Sam has one garden pot. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0178 | Finn has something in the bowl. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0093 | Holly did store the basket. | A | A | yes |

### Rule 47: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and does not contain negation words like “not,” “didn’t,” “can’t,” “won’t,” “without,” “nothing,” or “no.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0226 | Keira doesn't serve the salad. | B | B | yes |
| 2 | controlled_sentence_contains_negation_pool_0263 | Julia found something near the kitchen. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0114 | Rina went nowhere after camp. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0052 | Reed found nothing near the gate. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0271 | Gia went nowhere after cleanup. | B | B | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if the sentence is affirmative and describes the subject doing or having something, while negated statements or statements of absence are labeled B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0184 | Willa both blinked and stared. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0176 | Elsa both sang and hummed. | A | A | yes |
| 3 | controlled_sentence_contains_negation_pool_0167 | Gus neither bowed nor stepped. | B | B | yes |
| 4 | controlled_sentence_contains_negation_pool_0141 | Kara was quite calm yesterday. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0022 | Marek is not cheerful today. | B | B | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if the sentence is affirmative, and Label B if it contains negation or a negative/absent quantifier.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0192 | Vito did clearly glue the label. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0237 | Zoe saw nobody near the trail. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0038 | Vito saw someone near the bakery. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0211 | Sia went somewhere after school. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0182 | Leo neither bowed nor stepped. | B | B | yes |

### Rule 50: 4/5

Articulated rule: Label A if and only if the sentence is affirmative and describes the subject having, doing, or being something; label B if it is negated or expresses absence, inability, or nowhere/nothing.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0242 | Yara was quite eager yesterday. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0294 | Elsa left without the file. | B | A | no |
| 3 | controlled_sentence_contains_negation_pool_0262 | Lena has one brass bell. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0013 | Ada won't wrap the gift. | B | B | yes |
| 5 | controlled_sentence_contains_negation_pool_0266 | Finn won't wash the red cup. | B | B | yes |

