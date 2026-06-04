# Gold-Rule Application Control: controlled_sentence_contains_negation

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_rerun_controlled_sentence_contains_negation_iff_seed0_20260602T1535Z`

Correct canonical rule: Label A iff the sentence is negated rather than affirmative.

Correct prompt-facing rule: Label B iff the sentence is negated rather than affirmative; Label A otherwise.

## Summary

- Gold rules tested: `1`
- Rule-application calls: `50`
- Rule-application accuracy: `49/50` = `0.980`
- Nonparseable rate: `0.000`

## Settings

- Rule-application model: `gpt-5.4`
- Seed: `0`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Detailed Evaluations

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | controlled_sentence_contains_negation_pool_0100 | Faye has something in the tray. | A | A | yes |
| 2 | controlled_sentence_contains_negation_pool_0034 | Willa neither blinked nor stared. | B | B | yes |
| 3 | controlled_sentence_contains_negation_pool_0276 | Liam was quite patient yesterday. | A | A | yes |
| 4 | controlled_sentence_contains_negation_pool_0253 | Willa will trim the hedge. | A | A | yes |
| 5 | controlled_sentence_contains_negation_pool_0265 | Faye has no canvas roll. | B | B | yes |
| 6 | controlled_sentence_contains_negation_pool_0234 | Ada will wrap the gift. | A | A | yes |
| 7 | controlled_sentence_contains_negation_pool_0021 | Julia found nothing near the kitchen. | B | B | yes |
| 8 | controlled_sentence_contains_negation_pool_0149 | Marek doesn't scan the page. | B | B | yes |
| 9 | controlled_sentence_contains_negation_pool_0223 | Rina went nowhere after the game. | B | B | yes |
| 10 | controlled_sentence_contains_negation_pool_0023 | Eli did carefully pack the green bag. | A | A | yes |
| 11 | controlled_sentence_contains_negation_pool_0004 | Rina is not cheerful today. | B | B | yes |
| 12 | controlled_sentence_contains_negation_pool_0057 | Zoe will carry the small box. | A | A | yes |
| 13 | controlled_sentence_contains_negation_pool_0212 | Kiran is quite careful today. | A | A | yes |
| 14 | controlled_sentence_contains_negation_pool_0263 | Julia found something near the kitchen. | A | A | yes |
| 15 | controlled_sentence_contains_negation_pool_0118 | Uma has no short rope. | B | B | yes |
| 16 | controlled_sentence_contains_negation_pool_0044 | Bea never closed the window. | B | B | yes |
| 17 | controlled_sentence_contains_negation_pool_0062 | Zoe won't carry the small box. | B | B | yes |
| 18 | controlled_sentence_contains_negation_pool_0222 | Rina went somewhere after camp. | A | A | yes |
| 19 | controlled_sentence_contains_negation_pool_0165 | Pia has nothing in the jar. | B | B | yes |
| 20 | controlled_sentence_contains_negation_pool_0063 | Gus both bowed and stepped. | A | A | yes |
| 21 | controlled_sentence_contains_negation_pool_0233 | Vera saw nobody near the yard. | B | B | yes |
| 22 | controlled_sentence_contains_negation_pool_0277 | Vera saw someone near the yard. | A | A | yes |
| 23 | controlled_sentence_contains_negation_pool_0075 | Sam didn't mend the sock. | B | B | yes |
| 24 | controlled_sentence_contains_negation_pool_0193 | Tara did not slice the apple. | B | B | yes |
| 25 | controlled_sentence_contains_negation_pool_0058 | Priya saw nobody near the pier. | B | B | yes |
| 26 | controlled_sentence_contains_negation_pool_0101 | Ben left with the lunch. | A | A | yes |
| 27 | controlled_sentence_contains_negation_pool_0134 | Maya has nothing in the cup. | B | B | yes |
| 28 | controlled_sentence_contains_negation_pool_0115 | Kara can trace the pattern. | A | A | yes |
| 29 | controlled_sentence_contains_negation_pool_0294 | Elsa left without the file. | B | A | no |
| 30 | controlled_sentence_contains_negation_pool_0252 | Leo didn't sort the cards. | B | B | yes |
| 31 | controlled_sentence_contains_negation_pool_0091 | Theo went nowhere after breakfast. | B | B | yes |
| 32 | controlled_sentence_contains_negation_pool_0097 | Tess found nothing near the lobby. | B | B | yes |
| 33 | controlled_sentence_contains_negation_pool_0266 | Finn won't wash the red cup. | B | B | yes |
| 34 | controlled_sentence_contains_negation_pool_0197 | Gia went somewhere after cleanup. | A | A | yes |
| 35 | controlled_sentence_contains_negation_pool_0095 | Theo went somewhere after breakfast. | A | A | yes |
| 36 | controlled_sentence_contains_negation_pool_0111 | Marek does scan the page. | A | A | yes |
| 37 | controlled_sentence_contains_negation_pool_0251 | Uma was not rested yesterday. | B | B | yes |
| 38 | controlled_sentence_contains_negation_pool_0140 | Maya is not steady today. | B | B | yes |
| 39 | controlled_sentence_contains_negation_pool_0014 | Paul found nothing near the garage. | B | B | yes |
| 40 | controlled_sentence_contains_negation_pool_0020 | Kiran doesn't mark the spot. | B | B | yes |
| 41 | controlled_sentence_contains_negation_pool_0211 | Sia went somewhere after school. | A | A | yes |
| 42 | controlled_sentence_contains_negation_pool_0015 | Finn has one bright coin. | A | A | yes |
| 43 | controlled_sentence_contains_negation_pool_0219 | Cora can't shape the clay. | B | B | yes |
| 44 | controlled_sentence_contains_negation_pool_0012 | Julia quickly pushed the cart. | A | A | yes |
| 45 | controlled_sentence_contains_negation_pool_0208 | Paul can print the flyer. | A | A | yes |
| 46 | controlled_sentence_contains_negation_pool_0080 | Leo both bowed and stepped. | A | A | yes |
| 47 | controlled_sentence_contains_negation_pool_0094 | Elsa didn't warm the soup. | B | B | yes |
| 48 | controlled_sentence_contains_negation_pool_0017 | Ben never framed the photo. | B | B | yes |
| 49 | controlled_sentence_contains_negation_pool_0269 | Tess found nothing near the market. | B | B | yes |
| 50 | controlled_sentence_contains_negation_pool_0267 | Cora can't lock the door. | B | B | yes |
