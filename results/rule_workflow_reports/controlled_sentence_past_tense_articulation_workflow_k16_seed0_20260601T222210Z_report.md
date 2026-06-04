# Rule Articulation Workflow: controlled_sentence_past_tense

Run ID: `controlled_sentence_past_tense_articulation_workflow_k16_seed0_20260601T222210Z`

Correct prompt-facing rule: Label B iff the sentence is in past tense; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.640
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.640
- Rules with all evals correct: 15
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
| 1 | 1/5 | Label A if and only if the sentence describes an action happening at home, inside, outside, nearby, upstairs, or with no location phrase; label B otherwise. |
| 2 | 1/5 | Label A if and only if the sentence describes an action done at home, inside, upstairs, downtown, or outside; otherwise label B. |
| 3 | 5/5 | Label A if and only if the sentence describes a physical action that is happening in the present tense and is not in a past-tense form. |
| 4 | 5/5 | Label A if and only if the sentence describes an action in the present tense or with a present-like form, while Label B if it describes the same kind of action in past tense. |
| 5 | 2/5 | Label A if and only if the sentence describes an action that is plausible for the subject and object, while Label B if the action is implausible or mismatched. |
| 6 | 5/5 | Label A if and only if the sentence describes an action that is happening now or is ongoing, rather than a completed past-tense event. |
| 7 | 5/5 | Label A if and only if the sentence describes an action in the present tense; otherwise label B. |
| 8 | 2/5 | Label A if and only if the sentence has no explicit location phrase like “nearby,” “outside,” “inside,” “at home,” or “at work.” |
| 9 | 3/5 | Label A if and only if the sentence describes an action that is physically plausible for the subject and object in the stated setting; otherwise label B. |
| 10 | 2/5 | Label A if and only if the sentence describes an action that is plausible for the subject, and Label B if the action is implausible or unnatural for that subject. |
| 11 | 1/5 | Label A if and only if the sentence describes an action happening upstairs, downtown, inside, or at home; otherwise label B. |
| 12 | 2/5 | Label A if and only if the sentence describes an action that is physically plausible for the subject and object, while Label B if the action is implausible or mismatched. |
| 13 | 2/5 | Label A if and only if the sentence describes a **weight/handling action** like weighing, opening, carving, losing, stirring, selling, or folding; otherwise label B. |
| 14 | 3/5 | Label A if and only if the sentence describes an action happening at work or nearby, while home and downtown sentences are Label B. |
| 15 | 2/5 | Label A if and only if the sentence describes an action that is abstract or non-physical, while Label B if it describes a concrete physical action on a tangible object. |
| 16 | 5/5 | Label A if and only if the sentence uses a present-tense verb in the simple present form (e.g., “makes,” “records,” “cleans”), while past-tense forms like “painted,” “ground,” “made,” “weighed,” and “repaired” are Label B. |
| 17 | 4/5 | Label A if and only if the sentence describes an action with a **change of location or state that is completed/caused directly** (e.g., moving, hanging, covering, lighting, folding, losing, finding), while Label B if it describes a **non-resultative or more static/maintenance action** (e.g., washing, repairing, weighing, keeping, stirring). |
| 18 | 2/5 | Label A if and only if the sentence describes an action happening in a location like **inside, outside, downtown, nearby, upstairs, or at home**; otherwise label B. |
| 19 | 4/5 | Label A if and only if the sentence describes an action that is physically plausible for the subject and object; otherwise label B. |
| 20 | 2/5 | Label A if and only if the sentence describes an action happening in a location like upstairs, outside, inside, at work, or at home, while Label B otherwise. |
| 21 | 2/5 | Label A if and only if the sentence describes an action done by a plural subject or by a singular subject with no adverb, while Label B if it has a singular subject with an adverb or a past-tense verb form. |
| 22 | 2/5 | Label A if and only if the sentence describes an action that is naturally done by a person or group on the object, while Label B if it describes an action that is less natural or mismatched for the subject/object. |
| 23 | 5/5 | Label A if and only if the sentence describes an action that is ongoing or habitual in the present tense, while Label B is used for completed past-tense actions. |
| 24 | 5/5 | Label A if and only if the sentence is in present tense; Label B if it is in past tense. |
| 25 | 5/5 | Label A if and only if the sentence describes an action that is in the present tense or habitual form, while past-tense forms like “made,” “built,” “caught,” “opened,” and “repaired” are Label B. |
| 26 | 4/5 | Label A if and only if the sentence describes an action done by a person with a tool-like object or work-related item in a non-outdoor setting; otherwise label B. |
| 27 | 5/5 | Label A if and only if the sentence is in the present tense; otherwise label B. |
| 28 | 3/5 | Label A if and only if the sentence describes a physically manipulable action on a concrete object, otherwise label B. |
| 29 | 2/5 | Label A if and only if the sentence describes an action done **at work, at home, downtown, or upstairs**; otherwise label B. |
| 30 | 3/5 | Label A if and only if the sentence describes an action done by a singular subject with no explicit location like “at work,” “at home,” “inside,” “upstairs,” or “nearby”; otherwise label B. |
| 31 | 3/5 | Label A if and only if the sentence contains an action that is unusual or semantically mismatched for the subject or object, otherwise label B. |
| 32 | 3/5 | Label A if and only if the sentence describes an action that is plausible for the subject, and Label B if the action is implausible or unnatural for the subject. |
| 33 | 3/5 | Label A if and only if the sentence describes a **concrete physical action or event** (like moving, writing, buying, weighing, leaving, or sketching), and Label B otherwise. |
| 34 | 3/5 | Label A if and only if the sentence describes an action done **outside, at work, or with a group/others**, rather than a simple indoor/home action. |
| 35 | 3/5 | Label A if and only if the sentence contains a plural subject or a first-person/singular proper-name subject with an action verb, while singular common-subject sentences are Label B. |
| 36 | 4/5 | Label A if and only if the sentence describes a physically plausible event; otherwise label B. |
| 37 | 2/5 | Label A if and only if the sentence describes a present-tense action with no explicit location phrase like “at home,” “at work,” “outside,” “downtown,” or “nearby.” |
| 38 | 3/5 | Label A if and only if the sentence describes an action with a singular subject and a plural object, while Label B applies otherwise. |
| 39 | 1/5 | Label A if and only if the sentence contains a motionless action with a location phrase like “at work,” “at home,” “downtown,” “outside,” “inside,” or “nearby”; otherwise label B. |
| 40 | 5/5 | Label A if and only if the sentence is in present tense and does not contain a past-tense verb form. |
| 41 | 5/5 | Label A if and only if the sentence is in the present tense. |
| 42 | 5/5 | Label A if and only if the sentence describes a present-tense action with no past-tense verb. |
| 43 | 5/5 | Label A if and only if the sentence describes an action that is not in the past tense and does not involve a clearly physical object being manipulated in a simple transitive way. |
| 44 | 4/5 | Label A if and only if the sentence describes an action that is happening in a location or setting like “inside,” “outside,” “at home,” “upstairs,” or “nearby,” rather than a plain action without such a location. |
| 45 | 1/5 | Label A if and only if the sentence describes an action happening outside or at a location other than home/downtown/work? |
| 46 | 3/5 | Label A if and only if the sentence describes an action that is plausible for the subject; otherwise label B. |
| 47 | 1/5 | Label A if and only if the sentence describes an action that is semantically plausible with the subject and object, otherwise label B. |
| 48 | 5/5 | Label A if and only if the sentence uses a present-tense verb form; otherwise label B. |
| 49 | 2/5 | Label A if and only if the sentence describes an action happening in a location like **work, downtown, outside, or inside** rather than a plain action without such a location. |
| 50 | 5/5 | Label A if and only if the sentence uses the simple present tense (e.g., “pushes,” “counts”) rather than the past tense (e.g., “pushed,” “counted”). |

## Detailed Evaluations

### Rule 1: 1/5

Articulated rule: Label A if and only if the sentence describes an action happening at home, inside, outside, nearby, upstairs, or with no location phrase; label B otherwise.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0103 | Mia pushed the cart. | B | A | no |
| 2 | controlled_sentence_past_tense_pool_0035 | The student threw the ball. | B | A | no |
| 3 | controlled_sentence_past_tense_pool_0291 | The students calmly told the news. | B | A | no |
| 4 | controlled_sentence_past_tense_pool_0265 | The guests quickly opened the box inside. | B | A | no |
| 5 | controlled_sentence_past_tense_pool_0278 | Mia tells the joke. | A | A | yes |

### Rule 2: 1/5

Articulated rule: Label A if and only if the sentence describes an action done at home, inside, upstairs, downtown, or outside; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0139 | The neighbors calmly move the table at work. | A | B | no |
| 2 | controlled_sentence_past_tense_pool_0278 | Mia tells the joke. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0132 | The nurse sketches the tree. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0002 | Ravi carefully opened the gate. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0265 | The guests quickly opened the box inside. | B | A | no |

### Rule 3: 5/5

Articulated rule: Label A if and only if the sentence describes a physical action that is happening in the present tense and is not in a past-tense form.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0050 | The baker takes the seat. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0261 | The cooks watered the flowers at work. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0008 | The scouts find the file. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0216 | The guard quickly repairs the bench at work. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0295 | The guard made the sign. | B | B | yes |

### Rule 4: 5/5

Articulated rule: Label A if and only if the sentence describes an action in the present tense or with a present-like form, while Label B if it describes the same kind of action in past tense.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0146 | The farmer washes the apple. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0125 | The clerk made the bed. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0190 | The painter covers the pot upstairs. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0013 | The child quietly cleaned the shelf. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0014 | The students carved the handle at home. | B | B | yes |

### Rule 5: 2/5

Articulated rule: Label A if and only if the sentence describes an action that is plausible for the subject and object, while Label B if the action is implausible or mismatched.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0203 | The baker took the seat. | B | A | no |
| 3 | controlled_sentence_past_tense_pool_0010 | Eli slowly catches the fish downtown. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0167 | Ava recorded the score downtown. | B | A | no |
| 5 | controlled_sentence_past_tense_pool_0186 | The mechanic measured the board nearby. | B | A | no |

### Rule 6: 5/5

Articulated rule: Label A if and only if the sentence describes an action that is happening now or is ongoing, rather than a completed past-tense event.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0265 | The guests quickly opened the box inside. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0298 | Mia tells the story upstairs. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0231 | Iris slowly kept the promise. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0237 | The neighbors slowly lost the ticket at home. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0204 | The guests slowly repaired the fence at work. | B | B | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the sentence describes an action in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0158 | The guests calmly inspected the engine at work. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0023 | The students clean the table. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0259 | The scouts moved the table inside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0283 | Eli slowly watered the plants at work. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0124 | The children heard the alarm at work. | B | B | yes |

### Rule 8: 2/5

Articulated rule: Label A if and only if the sentence has no explicit location phrase like “nearby,” “outside,” “inside,” “at home,” or “at work.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0287 | The scouts found the file. | B | A | no |
| 2 | controlled_sentence_past_tense_pool_0028 | The baker met the mayor. | B | A | no |
| 3 | controlled_sentence_past_tense_pool_0108 | The painter slowly arranged the books downtown. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0150 | The student inspects the roof at home. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0012 | The child slowly records the score upstairs. | A | A | yes |

### Rule 9: 3/5

Articulated rule: Label A if and only if the sentence describes an action that is physically plausible for the subject and object in the stated setting; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0109 | Mia told the story upstairs. | B | A | no |
| 2 | controlled_sentence_past_tense_pool_0130 | The guard calmly repairs the bench upstairs. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0067 | The teacher slowly joins the group inside. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0087 | The painter moves the cart at home. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0286 | The coach built the shelf. | B | A | no |

### Rule 10: 2/5

Articulated rule: Label A if and only if the sentence describes an action that is plausible for the subject, and Label B if the action is implausible or unnatural for that subject.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0177 | Nina sketched the statue at home. | B | A | no |
| 3 | controlled_sentence_past_tense_pool_0085 | Nina carefully arranges the flowers. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0182 | The child found the file. | B | A | no |
| 5 | controlled_sentence_past_tense_pool_0167 | Ava recorded the score downtown. | B | A | no |

### Rule 11: 1/5

Articulated rule: Label A if and only if the sentence describes an action happening upstairs, downtown, inside, or at home; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0071 | The students cleaned the floor nearby. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0054 | The workers quickly counted the votes at home. | B | A | no |
| 3 | controlled_sentence_past_tense_pool_0212 | The guard makes the sign. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0166 | The guard stirs the batter. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0211 | The child finds the file. | A | B | no |

### Rule 12: 2/5

Articulated rule: Label A if and only if the sentence describes an action that is physically plausible for the subject and object, while Label B if the action is implausible or mismatched.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0249 | The scouts hide the gift. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0011 | The students cleaned the table. | B | A | no |
| 3 | controlled_sentence_past_tense_pool_0295 | The guard made the sign. | B | A | no |
| 4 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0224 | The coach counted the votes. | B | A | no |

### Rule 13: 2/5

Articulated rule: Label A if and only if the sentence describes a **weight/handling action** like weighing, opening, carving, losing, stirring, selling, or folding; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0088 | Iris quietly sold the apples downtown. | B | A | no |
| 2 | controlled_sentence_past_tense_pool_0047 | The gardeners win the prize upstairs. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0183 | The artists quietly catch the ball. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0024 | The chef quietly ground the spices. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0224 | The coach counted the votes. | B | B | yes |

### Rule 14: 3/5

Articulated rule: Label A if and only if the sentence describes an action happening at work or nearby, while home and downtown sentences are Label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0038 | The players slowly weigh the backpack. | A | B | no |
| 2 | controlled_sentence_past_tense_pool_0245 | Ravi cleaned the sink. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0266 | Iris calmly folded the towel outside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0145 | The child quietly sketches the tree inside. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0054 | The workers quickly counted the votes at home. | B | B | yes |

### Rule 15: 2/5

Articulated rule: Label A if and only if the sentence describes an action that is abstract or non-physical, while Label B if it describes a concrete physical action on a tangible object.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0154 | The nurse checks the ticket nearby. | A | B | no |
| 2 | controlled_sentence_past_tense_pool_0185 | The guard slowly fixes the bike upstairs. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0295 | The guard made the sign. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0072 | The guard cleaned the shelf nearby. | B | B | yes |

### Rule 16: 5/5

Articulated rule: Label A if and only if the sentence uses a present-tense verb in the simple present form (e.g., “makes,” “records,” “cleans”), while past-tense forms like “painted,” “ground,” “made,” “weighed,” and “repaired” are Label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0155 | Ravi carefully labeled the box. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0248 | The volunteers quickly folded the paper. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0102 | Nina slowly opens the shop at home. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0096 | Iris met the guide. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0128 | The scouts hid the gift. | B | B | yes |

### Rule 17: 4/5

Articulated rule: Label A if and only if the sentence describes an action with a **change of location or state that is completed/caused directly** (e.g., moving, hanging, covering, lighting, folding, losing, finding), while Label B if it describes a **non-resultative or more static/maintenance action** (e.g., washing, repairing, weighing, keeping, stirring).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0153 | Omar lights the lamp upstairs. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0183 | The artists quietly catch the ball. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0116 | Nina carefully arranged the flowers. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0110 | The nurse sketched the tree. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0189 | The children hear the alarm at work. | A | B | no |

### Rule 18: 2/5

Articulated rule: Label A if and only if the sentence describes an action happening in a location like **inside, outside, downtown, nearby, upstairs, or at home**; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0088 | Iris quietly sold the apples downtown. | B | A | no |
| 2 | controlled_sentence_past_tense_pool_0096 | Iris met the guide. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0156 | The volunteers quickly fold the paper. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0011 | The students cleaned the table. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0235 | Zoe calmly teaches the song. | A | B | no |

### Rule 19: 4/5

Articulated rule: Label A if and only if the sentence describes an action that is physically plausible for the subject and object; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0039 | Iris calmly folds the towel outside. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0297 | Eli paints the sign. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0240 | The mechanic washed the cup downtown. | B | A | no |
| 4 | controlled_sentence_past_tense_pool_0083 | The baker meets the mayor. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0176 | The friends send the card. | A | A | yes |

### Rule 20: 2/5

Articulated rule: Label A if and only if the sentence describes an action happening in a location like upstairs, outside, inside, at work, or at home, while Label B otherwise.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0208 | Noah breaks the vase nearby. | A | B | no |
| 2 | controlled_sentence_past_tense_pool_0022 | The farmer quickly lit the lamp. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0274 | The mechanic quietly writes the note. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0263 | The clerk repairs the sink. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0210 | The children left the station. | B | B | yes |

### Rule 21: 2/5

Articulated rule: Label A if and only if the sentence describes an action done by a plural subject or by a singular subject with no adverb, while Label B if it has a singular subject with an adverb or a past-tense verb form.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0101 | The farmer moves the table at work. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0085 | Nina carefully arranges the flowers. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0004 | The nurse checked the ticket nearby. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0149 | The volunteers lost the match. | B | A | no |
| 5 | controlled_sentence_past_tense_pool_0110 | The nurse sketched the tree. | B | A | no |

### Rule 22: 2/5

Articulated rule: Label A if and only if the sentence describes an action that is naturally done by a person or group on the object, while Label B if it describes an action that is less natural or mismatched for the subject/object.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0172 | Iris hangs the coat at work. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0188 | The guide calmly closes the book. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0181 | Mia slowly hid the key outside. | B | A | no |
| 4 | controlled_sentence_past_tense_pool_0155 | Ravi carefully labeled the box. | B | A | no |
| 5 | controlled_sentence_past_tense_pool_0158 | The guests calmly inspected the engine at work. | B | A | no |

### Rule 23: 5/5

Articulated rule: Label A if and only if the sentence describes an action that is ongoing or habitual in the present tense, while Label B is used for completed past-tense actions.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0289 | The neighbors slowly lose the ticket at home. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0003 | Mia told the truth. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0158 | The guests calmly inspected the engine at work. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0042 | The friends teach the class downtown. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0134 | The friends taught the class downtown. | B | B | yes |

### Rule 24: 5/5

Articulated rule: Label A if and only if the sentence is in present tense; Label B if it is in past tense.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0290 | Eli quietly covered the table. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0153 | Omar lights the lamp upstairs. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0056 | The cooks paint the fence inside. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0150 | The student inspects the roof at home. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0032 | The guard cleans the shelf nearby. | A | A | yes |

### Rule 25: 5/5

Articulated rule: Label A if and only if the sentence describes an action that is in the present tense or habitual form, while past-tense forms like “made,” “built,” “caught,” “opened,” and “repaired” are Label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0033 | The chef quietly grinds the spices. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0234 | The guests slowly repair the fence at work. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0044 | The students labeled the folder. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0052 | The clerk quickly folded the towel inside. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0230 | The painter slowly arranges the books downtown. | A | A | yes |

### Rule 26: 4/5

Articulated rule: Label A if and only if the sentence describes an action done by a person with a tool-like object or work-related item in a non-outdoor setting; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0109 | Mia told the story upstairs. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0095 | The painter buys the lamp. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0226 | The gardeners slowly found the coin. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0296 | Nina slowly opened the shop at home. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0283 | Eli slowly watered the plants at work. | B | B | yes |

### Rule 27: 5/5

Articulated rule: Label A if and only if the sentence is in the present tense; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0072 | The guard cleaned the shelf nearby. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0005 | The mechanic ties the knot. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0075 | Mia quietly chose the seat upstairs. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0003 | Mia told the truth. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0036 | The helper collects the shells downtown. | A | A | yes |

### Rule 28: 3/5

Articulated rule: Label A if and only if the sentence describes a physically manipulable action on a concrete object, otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0120 | The students carve the handle at home. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0146 | The farmer washes the apple. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0079 | The nurse carefully leaves the room. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0067 | The teacher slowly joins the group inside. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0029 | The cooks calmly grind the coffee. | A | A | yes |

### Rule 29: 2/5

Articulated rule: Label A if and only if the sentence describes an action done **at work, at home, downtown, or upstairs**; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0270 | The chef slowly pulls the handle. | A | B | no |
| 2 | controlled_sentence_past_tense_pool_0054 | The workers quickly counted the votes at home. | B | A | no |
| 3 | controlled_sentence_past_tense_pool_0087 | The painter moves the cart at home. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0254 | Ava covers the table nearby. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0011 | The students cleaned the table. | B | B | yes |

### Rule 30: 3/5

Articulated rule: Label A if and only if the sentence describes an action done by a singular subject with no explicit location like “at work,” “at home,” “inside,” “upstairs,” or “nearby”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0220 | Omar writes the answer at work. | A | B | no |
| 2 | controlled_sentence_past_tense_pool_0141 | The interns quickly label the jar outside. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0259 | The scouts moved the table inside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0200 | The players slowly weighed the backpack. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0034 | The guard calmly repaired the bench upstairs. | B | B | yes |

### Rule 31: 3/5

Articulated rule: Label A if and only if the sentence contains an action that is unusual or semantically mismatched for the subject or object, otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0177 | Nina sketched the statue at home. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0126 | Nina quietly hangs the banner outside. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0089 | Mia slowly hides the key outside. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0179 | The children slowly pushed the door nearby. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0201 | Ava covered the table nearby. | B | B | yes |

### Rule 32: 3/5

Articulated rule: Label A if and only if the sentence describes an action that is plausible for the subject, and Label B if the action is implausible or unnatural for the subject.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0233 | The farmer washed the apple. | B | A | no |
| 2 | controlled_sentence_past_tense_pool_0273 | The student throws the ball. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0058 | The child quietly polished the silver outside. | B | A | no |
| 4 | controlled_sentence_past_tense_pool_0188 | The guide calmly closes the book. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0080 | The guests calmly inspect the engine at work. | A | A | yes |

### Rule 33: 3/5

Articulated rule: Label A if and only if the sentence describes a **concrete physical action or event** (like moving, writing, buying, weighing, leaving, or sketching), and Label B otherwise.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0084 | Leo makes the cake downtown. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0212 | The guard makes the sign. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0009 | The guide folded the blanket nearby. | B | A | no |
| 4 | controlled_sentence_past_tense_pool_0194 | The chef quietly threw the ball downtown. | B | A | no |
| 5 | controlled_sentence_past_tense_pool_0005 | The mechanic ties the knot. | A | A | yes |

### Rule 34: 3/5

Articulated rule: Label A if and only if the sentence describes an action done **outside, at work, or with a group/others**, rather than a simple indoor/home action.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0286 | The coach built the shelf. | B | A | no |
| 2 | controlled_sentence_past_tense_pool_0212 | The guard makes the sign. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0065 | The farmer won the game inside. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0233 | The farmer washed the apple. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0025 | The guard quickly repaired the bench at work. | B | A | no |

### Rule 35: 3/5

Articulated rule: Label A if and only if the sentence contains a plural subject or a first-person/singular proper-name subject with an action verb, while singular common-subject sentences are Label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0236 | The neighbors meet the guest upstairs. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0078 | The mechanic washes the cup downtown. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0090 | The coach carefully measures the doorway inside. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0260 | Ava carefully stirs the batter. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0029 | The cooks calmly grind the coffee. | A | A | yes |

### Rule 36: 4/5

Articulated rule: Label A if and only if the sentence describes a physically plausible event; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0001 | Iris builds the model. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0006 | The coach counts the votes. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0198 | Mia told the joke. | B | A | no |
| 5 | controlled_sentence_past_tense_pool_0036 | The helper collects the shells downtown. | A | A | yes |

### Rule 37: 2/5

Articulated rule: Label A if and only if the sentence describes a present-tense action with no explicit location phrase like “at home,” “at work,” “outside,” “downtown,” or “nearby.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0000 | The cooks inspected the fence outside. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0115 | The children leave the station. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0290 | Eli quietly covered the table. | B | A | no |
| 4 | controlled_sentence_past_tense_pool_0248 | The volunteers quickly folded the paper. | B | A | no |
| 5 | controlled_sentence_past_tense_pool_0273 | The student throws the ball. | A | A | yes |

### Rule 38: 3/5

Articulated rule: Label A if and only if the sentence describes an action with a singular subject and a plural object, while Label B applies otherwise.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0156 | The volunteers quickly fold the paper. | A | B | no |
| 2 | controlled_sentence_past_tense_pool_0123 | Omar wrote the answer at work. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0160 | The painter quickly covered the pot. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0072 | The guard cleaned the shelf nearby. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0141 | The interns quickly label the jar outside. | A | B | no |

### Rule 39: 1/5

Articulated rule: Label A if and only if the sentence contains a motionless action with a location phrase like “at work,” “at home,” “downtown,” “outside,” “inside,” or “nearby”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0047 | The gardeners win the prize upstairs. | A | B | no |
| 2 | controlled_sentence_past_tense_pool_0264 | Noah quietly hangs the banner. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0058 | The child quietly polished the silver outside. | B | A | no |
| 4 | controlled_sentence_past_tense_pool_0106 | The children quietly catch the fish at work. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0115 | The children leave the station. | A | B | no |

### Rule 40: 5/5

Articulated rule: Label A if and only if the sentence is in present tense and does not contain a past-tense verb form.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0151 | The helper bought the book downtown. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0090 | The coach carefully measures the doorway inside. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0046 | The helper buys the book downtown. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0166 | The guard stirs the batter. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0170 | The helper catches the fish. | A | A | yes |

### Rule 41: 5/5

Articulated rule: Label A if and only if the sentence is in the present tense.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0090 | The coach carefully measures the doorway inside. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0115 | The children leave the station. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0145 | The child quietly sketches the tree inside. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0079 | The nurse carefully leaves the room. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0083 | The baker meets the mayor. | A | A | yes |

### Rule 42: 5/5

Articulated rule: Label A if and only if the sentence describes a present-tense action with no past-tense verb.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0179 | The children slowly pushed the door nearby. | B | B | yes |
| 2 | controlled_sentence_past_tense_pool_0128 | The scouts hid the gift. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0130 | The guard calmly repairs the bench upstairs. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0234 | The guests slowly repair the fence at work. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0262 | Ravi carefully opens the gate. | A | A | yes |

### Rule 43: 5/5

Articulated rule: Label A if and only if the sentence describes an action that is not in the past tense and does not involve a clearly physical object being manipulated in a simple transitive way.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0005 | The mechanic ties the knot. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0019 | The guard lit the fire. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0096 | Iris met the guide. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0048 | The artists quietly caught the ball. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0257 | The guide calmly hides the note. | A | A | yes |

### Rule 44: 4/5

Articulated rule: Label A if and only if the sentence describes an action that is happening in a location or setting like “inside,” “outside,” “at home,” “upstairs,” or “nearby,” rather than a plain action without such a location.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0046 | The helper buys the book downtown. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0041 | The mechanic measures the board nearby. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0103 | Mia pushed the cart. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0207 | The guide calmly hid the note. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0296 | Nina slowly opened the shop at home. | B | A | no |

### Rule 45: 1/5

Articulated rule: Label A if and only if the sentence describes an action happening outside or at a location other than home/downtown/work?

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0067 | The teacher slowly joins the group inside. | A | B | no |
| 2 | controlled_sentence_past_tense_pool_0215 | The workers quickly count the votes at home. | A | B | no |
| 3 | controlled_sentence_past_tense_pool_0021 | Leo made the cake downtown. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0202 | Noah finds the coin. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0180 | Iris slowly keeps the promise. | A | B | no |

### Rule 46: 3/5

Articulated rule: Label A if and only if the sentence describes an action that is plausible for the subject; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0187 | Ravi calmly took the photo inside. | B | A | no |
| 2 | controlled_sentence_past_tense_pool_0094 | The artists made the sign. | B | A | no |
| 3 | controlled_sentence_past_tense_pool_0230 | The painter slowly arranges the books downtown. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0178 | The guide folds the blanket nearby. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0093 | The baker counts the coins at home. | A | A | yes |

### Rule 47: 1/5

Articulated rule: Label A if and only if the sentence describes an action that is semantically plausible with the subject and object, otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0226 | The gardeners slowly found the coin. | B | A | no |
| 2 | controlled_sentence_past_tense_pool_0263 | The clerk repairs the sink. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0114 | The painter bought the lamp. | B | A | no |
| 4 | controlled_sentence_past_tense_pool_0052 | The clerk quickly folded the towel inside. | B | A | no |
| 5 | controlled_sentence_past_tense_pool_0271 | The interns quickly labeled the jar outside. | B | A | no |

### Rule 48: 5/5

Articulated rule: Label A if and only if the sentence uses a present-tense verb form; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0184 | Omar quietly writes the note. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0176 | The friends send the card. | A | A | yes |
| 3 | controlled_sentence_past_tense_pool_0167 | Ava recorded the score downtown. | B | B | yes |
| 4 | controlled_sentence_past_tense_pool_0141 | The interns quickly label the jar outside. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0022 | The farmer quickly lit the lamp. | B | B | yes |

### Rule 49: 2/5

Articulated rule: Label A if and only if the sentence describes an action happening in a location like **work, downtown, outside, or inside** rather than a plain action without such a location.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0192 | The farmer quickly keeps the promise at work. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0237 | The neighbors slowly lost the ticket at home. | B | A | no |
| 3 | controlled_sentence_past_tense_pool_0038 | The players slowly weigh the backpack. | A | B | no |
| 4 | controlled_sentence_past_tense_pool_0211 | The child finds the file. | A | B | no |
| 5 | controlled_sentence_past_tense_pool_0182 | The child found the file. | B | B | yes |

### Rule 50: 5/5

Articulated rule: Label A if and only if the sentence uses the simple present tense (e.g., “pushes,” “counts”) rather than the past tense (e.g., “pushed,” “counted”).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_past_tense_pool_0242 | Ava hangs the banner downtown. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0294 | The teacher quietly measured the doorway at work. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0262 | Ravi carefully opens the gate. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0013 | The child quietly cleaned the shelf. | B | B | yes |
| 5 | controlled_sentence_past_tense_pool_0266 | Iris calmly folded the towel outside. | B | B | yes |

