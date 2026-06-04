# Gold-Rule Application Control: random_contains_ab

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_random_contains_ab_seed0`

Correct canonical rule: Label A iff the string contains the substring ab.

Correct prompt-facing rule: Label B iff the string contains the substring ab; Label A otherwise.

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
| 1 | random_contains_ab_pool_0362 | rurpltpe | A | A | yes |
| 2 | random_contains_ab_pool_0336 | krxnabditki | B | B | yes |
| 3 | random_contains_ab_pool_0100 | rrwfntd | A | A | yes |
| 4 | random_contains_ab_pool_0403 | abtayednm | B | B | yes |
| 5 | random_contains_ab_pool_0034 | qztoqdmmjko | A | A | yes |
| 6 | random_contains_ab_pool_0276 | abojcvhkhm | B | B | yes |
| 7 | random_contains_ab_pool_0464 | ewewtlokvb | A | A | yes |
| 8 | random_contains_ab_pool_0470 | nanab | B | B | yes |
| 9 | random_contains_ab_pool_0499 | caubtgfpabg | B | B | yes |
| 10 | random_contains_ab_pool_0413 | keagzgmmexyp | A | A | yes |
| 11 | random_contains_ab_pool_0253 | abcslla | B | B | yes |
| 12 | random_contains_ab_pool_0265 | jojgkgeo | A | A | yes |
| 13 | random_contains_ab_pool_0234 | jrhvwvld | A | A | yes |
| 14 | random_contains_ab_pool_0021 | hqvwfob | A | A | yes |
| 15 | random_contains_ab_pool_0149 | pabbj | B | B | yes |
| 16 | random_contains_ab_pool_0354 | tvdjvjsabya | B | B | yes |
| 17 | random_contains_ab_pool_0223 | ddrwctc | A | A | yes |
| 18 | random_contains_ab_pool_0023 | hiwknzkbc | A | A | yes |
| 19 | random_contains_ab_pool_0480 | nfhblovo | A | A | yes |
| 20 | random_contains_ab_pool_0004 | pvot | A | A | yes |
| 21 | random_contains_ab_pool_0057 | ruotwlbuabhg | B | B | yes |
| 22 | random_contains_ab_pool_0212 | uyoktt | A | A | yes |
| 23 | random_contains_ab_pool_0446 | xznk | A | A | yes |
| 24 | random_contains_ab_pool_0263 | abyea | B | B | yes |
| 25 | random_contains_ab_pool_0118 | rfrabtdop | B | B | yes |
| 26 | random_contains_ab_pool_0497 | eputcaj | A | A | yes |
| 27 | random_contains_ab_pool_0044 | wqdwabwg | B | B | yes |
| 28 | random_contains_ab_pool_0062 | ruthxyjazfsj | A | A | yes |
| 29 | random_contains_ab_pool_0315 | mabb | B | B | yes |
| 30 | random_contains_ab_pool_0222 | sbzpz | A | A | yes |
| 31 | random_contains_ab_pool_0165 | gcgbgutsflrr | A | A | yes |
| 32 | random_contains_ab_pool_0063 | wtyngyro | A | A | yes |
| 33 | random_contains_ab_pool_0233 | cixmpmvfjwjt | A | A | yes |
| 34 | random_contains_ab_pool_0277 | eoyfgh | A | A | yes |
| 35 | random_contains_ab_pool_0334 | irfabadadk | B | B | yes |
| 36 | random_contains_ab_pool_0075 | slvkqwkwth | A | A | yes |
| 37 | random_contains_ab_pool_0495 | ytstboyabrb | B | B | yes |
| 38 | random_contains_ab_pool_0193 | cdnab | B | B | yes |
| 39 | random_contains_ab_pool_0415 | pkubkpl | A | A | yes |
| 40 | random_contains_ab_pool_0058 | abqkpu | B | B | yes |
| 41 | random_contains_ab_pool_0101 | dabg | B | B | yes |
| 42 | random_contains_ab_pool_0134 | pcgdqetgab | B | B | yes |
| 43 | random_contains_ab_pool_0115 | abmejziwtfm | B | B | yes |
| 44 | random_contains_ab_pool_0348 | ilabjgjrmc | B | B | yes |
| 45 | random_contains_ab_pool_0486 | cnjjab | B | B | yes |
| 46 | random_contains_ab_pool_0294 | abnk | B | B | yes |
| 47 | random_contains_ab_pool_0498 | kbontflozoh | A | A | yes |
| 48 | random_contains_ab_pool_0387 | xqrgwglh | A | A | yes |
| 49 | random_contains_ab_pool_0252 | mwjhdqxo | A | A | yes |
| 50 | random_contains_ab_pool_0091 | tcabzi | B | B | yes |
