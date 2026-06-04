# Gold-Rule Application Control: balanced_sentence_contains_digit

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_balanced_sentence_contains_digit_seed0`

Correct canonical rule: Label A iff the input contains at least one digit.

Correct prompt-facing rule: Label B iff the input contains at least one digit; Label A otherwise.

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
| 1 | balanced_sentence_contains_digit_pool_0100 | Four neat books waited outside. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0034 | Jonah carried 9 silver plates. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0276 | Tess packed ten blue apples. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0253 | The shelf held six purple shells. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0265 | Theo carried 12 white towels. | B | B | yes |
| 6 | balanced_sentence_contains_digit_pool_0234 | Owen found five loose leaves. | A | A | yes |
| 7 | balanced_sentence_contains_digit_pool_0021 | 11 quiet maps fell softly. | B | B | yes |
| 8 | balanced_sentence_contains_digit_pool_0149 | 8 loose cookies waited outside. | B | B | yes |
| 9 | balanced_sentence_contains_digit_pool_0223 | Tess packed 10 blue apples. | B | B | yes |
| 10 | balanced_sentence_contains_digit_pool_0023 | Aria packed eleven loose flowers. | A | A | yes |
| 11 | balanced_sentence_contains_digit_pool_0004 | The shelf held 9 blue shells. | B | B | yes |
| 12 | balanced_sentence_contains_digit_pool_0057 | Milo found nine cool notes. | A | A | yes |
| 13 | balanced_sentence_contains_digit_pool_0212 | Ben found three calm tiles. | A | A | yes |
| 14 | balanced_sentence_contains_digit_pool_0263 | Near the door sat two round apples. | A | A | yes |
| 15 | balanced_sentence_contains_digit_pool_0118 | Near the door sat 4 small coins. | B | B | yes |
| 16 | balanced_sentence_contains_digit_pool_0044 | The basket had 4 cool coins. | B | B | yes |
| 17 | balanced_sentence_contains_digit_pool_0062 | Leo counted 2 bright boxes. | B | B | yes |
| 18 | balanced_sentence_contains_digit_pool_0222 | Ryan found four purple brushes. | A | A | yes |
| 19 | balanced_sentence_contains_digit_pool_0165 | 6 crisp leaves fell softly. | B | B | yes |
| 20 | balanced_sentence_contains_digit_pool_0063 | Sofia saved eleven clean seeds. | A | A | yes |
| 21 | balanced_sentence_contains_digit_pool_0233 | Theo sorted 3 brown flowers. | B | B | yes |
| 22 | balanced_sentence_contains_digit_pool_0277 | Owen found four warm pens. | A | A | yes |
| 23 | balanced_sentence_contains_digit_pool_0075 | 7 plain mugs waited outside. | B | B | yes |
| 24 | balanced_sentence_contains_digit_pool_0193 | Milo packed 4 blue boxes. | B | B | yes |
| 25 | balanced_sentence_contains_digit_pool_0058 | 5 cool leaves fell softly. | B | B | yes |
| 26 | balanced_sentence_contains_digit_pool_0101 | Two clean maps fell softly. | A | A | yes |
| 27 | balanced_sentence_contains_digit_pool_0134 | Lila saved 4 silver books. | B | B | yes |
| 28 | balanced_sentence_contains_digit_pool_0115 | The shelf held nine blue shells. | A | A | yes |
| 29 | balanced_sentence_contains_digit_pool_0294 | Ryan sorted 4 quiet pens. | B | B | yes |
| 30 | balanced_sentence_contains_digit_pool_0252 | Ruby carried 9 smooth bags. | B | B | yes |
| 31 | balanced_sentence_contains_digit_pool_0091 | Finn found 2 early rings. | B | B | yes |
| 32 | balanced_sentence_contains_digit_pool_0097 | The basket had 2 purple cards. | B | B | yes |
| 33 | balanced_sentence_contains_digit_pool_0266 | Milo found 9 cool notes. | B | B | yes |
| 34 | balanced_sentence_contains_digit_pool_0197 | Two clean rings waited outside. | A | A | yes |
| 35 | balanced_sentence_contains_digit_pool_0095 | The shelf held twelve quiet beads. | A | A | yes |
| 36 | balanced_sentence_contains_digit_pool_0111 | Leo found eleven white beads. | A | A | yes |
| 37 | balanced_sentence_contains_digit_pool_0251 | Mia saved 12 simple cards. | B | B | yes |
| 38 | balanced_sentence_contains_digit_pool_0140 | Only 8 quiet apples stayed dry. | B | B | yes |
| 39 | balanced_sentence_contains_digit_pool_0014 | 2 clean maps fell softly. | B | B | yes |
| 40 | balanced_sentence_contains_digit_pool_0020 | Owen found 5 loose leaves. | B | B | yes |
| 41 | balanced_sentence_contains_digit_pool_0211 | Nora counted ten quiet apples. | A | A | yes |
| 42 | balanced_sentence_contains_digit_pool_0015 | Clara counted twelve round tiles. | A | A | yes |
| 43 | balanced_sentence_contains_digit_pool_0219 | Ivy sorted 2 silver plates. | B | B | yes |
| 44 | balanced_sentence_contains_digit_pool_0012 | Jude saved five smooth cups. | A | A | yes |
| 45 | balanced_sentence_contains_digit_pool_0208 | Only seven plain brushes stayed dry. | A | A | yes |
| 46 | balanced_sentence_contains_digit_pool_0080 | The basket had eleven white coins. | A | A | yes |
| 47 | balanced_sentence_contains_digit_pool_0094 | 4 neat books waited outside. | B | B | yes |
| 48 | balanced_sentence_contains_digit_pool_0017 | Lila packed 4 plain flowers. | B | B | yes |
| 49 | balanced_sentence_contains_digit_pool_0269 | The basket had 10 purple notes. | B | B | yes |
| 50 | balanced_sentence_contains_digit_pool_0267 | The shelf held 12 yellow flowers. | B | B | yes |
