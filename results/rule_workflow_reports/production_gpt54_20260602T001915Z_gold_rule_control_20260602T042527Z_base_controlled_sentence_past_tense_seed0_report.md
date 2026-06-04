# Gold-Rule Application Control: controlled_sentence_past_tense

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_controlled_sentence_past_tense_seed0`

Correct canonical rule: Label A iff the sentence is in past tense.

Correct prompt-facing rule: Label B iff the sentence is in past tense; Label A otherwise.

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
| 1 | controlled_sentence_past_tense_pool_0100 | The students label the folder. | A | A | yes |
| 2 | controlled_sentence_past_tense_pool_0034 | The guard calmly repaired the bench upstairs. | B | B | yes |
| 3 | controlled_sentence_past_tense_pool_0276 | The painter quickly covers the pot. | A | A | yes |
| 4 | controlled_sentence_past_tense_pool_0253 | The players slowly fix the radio. | A | A | yes |
| 5 | controlled_sentence_past_tense_pool_0265 | The guests quickly opened the box inside. | B | B | yes |
| 6 | controlled_sentence_past_tense_pool_0234 | The guests slowly repair the fence at work. | A | A | yes |
| 7 | controlled_sentence_past_tense_pool_0021 | Leo made the cake downtown. | B | B | yes |
| 8 | controlled_sentence_past_tense_pool_0149 | The volunteers lost the match. | B | B | yes |
| 9 | controlled_sentence_past_tense_pool_0223 | The guide calmly closed the book. | B | B | yes |
| 10 | controlled_sentence_past_tense_pool_0023 | The students clean the table. | A | A | yes |
| 11 | controlled_sentence_past_tense_pool_0004 | The nurse checked the ticket nearby. | B | B | yes |
| 12 | controlled_sentence_past_tense_pool_0057 | The mechanic ties the rope at work. | A | A | yes |
| 13 | controlled_sentence_past_tense_pool_0212 | The guard makes the sign. | A | A | yes |
| 14 | controlled_sentence_past_tense_pool_0263 | The clerk repairs the sink. | A | A | yes |
| 15 | controlled_sentence_past_tense_pool_0118 | The children slowly broke the vase. | B | B | yes |
| 16 | controlled_sentence_past_tense_pool_0044 | The students labeled the folder. | B | B | yes |
| 17 | controlled_sentence_past_tense_pool_0062 | Ravi slowly broke the vase nearby. | B | B | yes |
| 18 | controlled_sentence_past_tense_pool_0222 | The students clean the floor nearby. | A | A | yes |
| 19 | controlled_sentence_past_tense_pool_0165 | The cooks painted the fence inside. | B | B | yes |
| 20 | controlled_sentence_past_tense_pool_0063 | The gardeners slowly find the coin. | A | A | yes |
| 21 | controlled_sentence_past_tense_pool_0233 | The farmer washed the apple. | B | B | yes |
| 22 | controlled_sentence_past_tense_pool_0277 | The teacher stirs the soup at work. | A | A | yes |
| 23 | controlled_sentence_past_tense_pool_0075 | Mia quietly chose the seat upstairs. | B | B | yes |
| 24 | controlled_sentence_past_tense_pool_0193 | The painter moved the cart at home. | B | B | yes |
| 25 | controlled_sentence_past_tense_pool_0058 | The child quietly polished the silver outside. | B | B | yes |
| 26 | controlled_sentence_past_tense_pool_0101 | The farmer moves the table at work. | A | A | yes |
| 27 | controlled_sentence_past_tense_pool_0134 | The friends taught the class downtown. | B | B | yes |
| 28 | controlled_sentence_past_tense_pool_0115 | The children leave the station. | A | A | yes |
| 29 | controlled_sentence_past_tense_pool_0294 | The teacher quietly measured the doorway at work. | B | B | yes |
| 30 | controlled_sentence_past_tense_pool_0252 | Iris built the model. | B | B | yes |
| 31 | controlled_sentence_past_tense_pool_0091 | The gardeners slowly folded the blanket. | B | B | yes |
| 32 | controlled_sentence_past_tense_pool_0097 | The nurse drew the house at home. | B | B | yes |
| 33 | controlled_sentence_past_tense_pool_0266 | Iris calmly folded the towel outside. | B | B | yes |
| 34 | controlled_sentence_past_tense_pool_0197 | The cooks carefully water the garden. | A | A | yes |
| 35 | controlled_sentence_past_tense_pool_0095 | The painter buys the lamp. | A | A | yes |
| 36 | controlled_sentence_past_tense_pool_0111 | Eli quietly covers the table. | A | A | yes |
| 37 | controlled_sentence_past_tense_pool_0251 | The chef calmly bought the snack inside. | B | B | yes |
| 38 | controlled_sentence_past_tense_pool_0140 | Omar lit the lamp upstairs. | B | B | yes |
| 39 | controlled_sentence_past_tense_pool_0014 | The students carved the handle at home. | B | B | yes |
| 40 | controlled_sentence_past_tense_pool_0020 | The painter quietly heard the alarm at home. | B | B | yes |
| 41 | controlled_sentence_past_tense_pool_0211 | The child finds the file. | A | A | yes |
| 42 | controlled_sentence_past_tense_pool_0015 | The chef quietly throws the ball downtown. | A | A | yes |
| 43 | controlled_sentence_past_tense_pool_0219 | Ava hung the banner downtown. | B | B | yes |
| 44 | controlled_sentence_past_tense_pool_0012 | The child slowly records the score upstairs. | A | A | yes |
| 45 | controlled_sentence_past_tense_pool_0208 | Noah breaks the vase nearby. | A | A | yes |
| 46 | controlled_sentence_past_tense_pool_0080 | The guests calmly inspect the engine at work. | A | A | yes |
| 47 | controlled_sentence_past_tense_pool_0094 | The artists made the sign. | B | B | yes |
| 48 | controlled_sentence_past_tense_pool_0017 | Omar quietly wrote the note. | B | B | yes |
| 49 | controlled_sentence_past_tense_pool_0269 | The twins quietly sketched the face at work. | B | B | yes |
| 50 | controlled_sentence_past_tense_pool_0267 | The farmer quickly kept the promise at work. | B | B | yes |
