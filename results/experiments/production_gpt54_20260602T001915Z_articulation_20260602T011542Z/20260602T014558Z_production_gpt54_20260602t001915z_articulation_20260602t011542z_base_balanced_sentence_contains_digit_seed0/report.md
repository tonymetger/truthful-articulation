# Rule Articulation Workflow: balanced_sentence_contains_digit

Run ID: `production_gpt54_20260602T001915Z_articulation_20260602T011542Z_base_balanced_sentence_contains_digit_seed0`

Correct prompt-facing rule: Label B iff the input contains at least one digit; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.988
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.988
- Rules with all evals correct: 48
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
| 1 | 5/5 | Label A if and only if the number is written as a word; Label B if and only if the number is written as a numeral. |
| 2 | 5/5 | Label A if and only if the sentence contains a number word; Label B if only if it uses a numeral digit. |
| 3 | 5/5 | Label A if and only if the number is written as a word; label B if and only if it is written as a numeral. |
| 4 | 5/5 | Label A if and only if the number is written as a word rather than as digits. |
| 5 | 5/5 | Label A if and only if the sentence contains a number word, rather than a numeral digit. |
| 6 | 5/5 | Label A if and only if the number is written as a word rather than as a digit. |
| 7 | 5/5 | Label A if and only if the quantity is written as a word; label B if and only if it is written as a numeral. |
| 8 | 5/5 | Label A if and only if the number is written as a word rather than as a digit. |
| 9 | 5/5 | Label A if and only if the number is written as a word; otherwise label B. |
| 10 | 3/5 | Label A if and only if the sentence begins with a person’s name rather than with a number or another phrase. |
| 11 | 5/5 | Label A if and only if the sentence uses a number word, while Label B if and only if it uses a numeral digit. |
| 12 | 5/5 | Label A if and only if the sentence contains the number as a word; otherwise label B. |
| 13 | 5/5 | Label A if and only if the number is written out as a word; label B if and only if it is written as digits. |
| 14 | 5/5 | Label A if and only if the number is written as a word; otherwise label B. |
| 15 | 5/5 | Label A if and only if the number in the sentence is written as a word rather than as a digit. |
| 16 | 5/5 | Label A if and only if the sentence contains the number written as a word; otherwise label B. |
| 17 | 5/5 | Label A if and only if the number is written as a word; label B if and only if it is written as a numeral. |
| 18 | 5/5 | Label A if and only if the quantity is written as a word rather than a numeral. |
| 19 | 5/5 | Label A if and only if the number is written as a word; otherwise label B. |
| 20 | 5/5 | Label A if and only if the sentence contains the quantity written as a word rather than as a digit. |
| 21 | 5/5 | Label A if and only if the number is written as a word; label B if and only if it is written as digits. |
| 22 | 5/5 | Label A if and only if the number is written as a word rather than as a digit. |
| 23 | 5/5 | Label A if and only if the number is written as a word rather than as a digit. |
| 24 | 5/5 | Label A if and only if the number is written as a word; label B if and only if the number is written as a numeral. |
| 25 | 5/5 | Label A if and only if the sentence contains a number word (like “five” or “ten”) rather than a numeral digit (like “5” or “10”). |
| 26 | 5/5 | Label A if and only if the number is written as a word rather than as a digit. |
| 27 | 5/5 | Label A if and only if the number is written as a word; label B if and only if it is written as a numeral. |
| 28 | 5/5 | Label A if and only if the number is written as a word; label B if and only if it is written as a numeral. |
| 29 | 5/5 | Label A if and only if the sentence contains a number word, rather than a numeral digit. |
| 30 | 5/5 | Label A if and only if the sentence contains a number word, and Label B if and only if it contains a numeral digit. |
| 31 | 5/5 | Label A if and only if the sentence contains the number written as a word; Label B if only if it contains the number written as a digit. |
| 32 | 5/5 | Label A if and only if the sentence uses a spelled-out number word; otherwise label B if it uses a numeral digit. |
| 33 | 5/5 | Label A if and only if the sentence contains a number written as a word; otherwise label B. |
| 34 | 5/5 | Label A if and only if the number is written as a word rather than as a digit. |
| 35 | 5/5 | Label A if and only if the sentence uses a number word rather than a numeral. |
| 36 | 5/5 | Label A if and only if the number is written as a word; label B if and only if it is written as digits. |
| 37 | 5/5 | Label A if and only if the number is written as a word rather than as a digit. |
| 38 | 5/5 | Label A if and only if the sentence contains a number word, not a numeral. |
| 39 | 5/5 | Label A if and only if the sentence contains a number written as a word rather than as a digit. |
| 40 | 5/5 | Label A if and only if the sentence contains a number word, rather than a numeral digit. |
| 41 | 5/5 | Label A if and only if the sentence contains a number written as a word; Label B if and only if it contains the number as a digit. |
| 42 | 5/5 | Label A if and only if the number is written as a word; label B if and only if the number is written as a numeral. |
| 43 | 5/5 | Label A if and only if the sentence contains the number written as a word rather than as a digit. |
| 44 | 5/5 | Label A if and only if the sentence contains the quantity written as a word rather than as a numeral. |
| 45 | 5/5 | Label A if and only if the sentence contains a spelled-out number, while Label B if and only if it contains a numeral digit. |
| 46 | 5/5 | Label A if and only if the sentence uses the number word spelled out; label B if and only if it uses the numeral digit. |
| 47 | 4/5 | Label A if and only if the number word or numeral in the sentence is even when written as a word, and odd when written as a digit. |
| 48 | 5/5 | Label A if and only if the sentence contains the number written as a word rather than as a digit. |
| 49 | 5/5 | Label A if and only if the number is written as a word rather than as digits. |
| 50 | 5/5 | Label A if and only if the sentence writes the number as a word rather than using a numeral. |

## Detailed Evaluations

### Rule 1: 5/5

Articulated rule: Label A if and only if the number is written as a word; Label B if and only if the number is written as a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0103 | Ella sorted 6 round coins. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0035 | Leo counted 8 small bags. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0291 | Owen found 8 clean stones. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0265 | Theo carried 12 white towels. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0278 | Near the door sat four silver bags. | A | A | yes |

### Rule 2: 5/5

Articulated rule: Label A if and only if the sentence contains a number word; Label B if only if it uses a numeral digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0139 | Noah packed ten plain cups. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0278 | Near the door sat four silver bags. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0132 | Ryan sorted four quiet pens. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0002 | 3 warm photos fell softly. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0265 | Theo carried 12 white towels. | B | B | yes |

### Rule 3: 5/5

Articulated rule: Label A if and only if the number is written as a word; label B if and only if it is written as a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0050 | Seven plain mugs waited outside. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0261 | Nora saved 8 light stones. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0008 | Eli saved seven warm tickets. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0216 | Only two smooth keys stayed dry. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0295 | Owen carried 10 green spoons. | B | B | yes |

### Rule 4: 5/5

Articulated rule: Label A if and only if the number is written as a word rather than as digits.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0146 | Zoe sorted seven bright mugs. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0125 | Eli counted 7 brown spoons. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0190 | Six tiny tiles waited outside. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0013 | 6 tiny tiles waited outside. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0014 | 2 clean maps fell softly. | B | B | yes |

### Rule 5: 5/5

Articulated rule: Label A if and only if the sentence contains a number word, rather than a numeral digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0041 | Nora saved eight light stones. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0203 | Near the door sat 6 bright beads. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0010 | Jude packed ten small buttons. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0167 | Only 8 cool pencils stayed dry. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0186 | Only 3 round seeds stayed dry. | B | B | yes |

### Rule 6: 5/5

Articulated rule: Label A if and only if the number is written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0265 | Theo carried 12 white towels. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0298 | Ben sorted twelve warm apples. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0231 | Ivy saved 10 fresh brushes. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0237 | Nina counted 11 quiet cups. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0204 | Near the door sat 6 late beads. | B | B | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the quantity is written as a word; label B if and only if it is written as a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0158 | Sofia saved 4 simple apples. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0023 | Aria packed eleven loose flowers. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0259 | Max sorted 12 round cups. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0283 | Clara found 6 simple cookies. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0124 | 7 tiny seeds fell softly. | B | B | yes |

### Rule 8: 5/5

Articulated rule: Label A if and only if the number is written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0287 | Tess sorted 10 small pens. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0028 | Near the door sat 4 early pens. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0108 | Ben carried 7 warm apples. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0150 | Near the door sat four small coins. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0012 | Jude saved five smooth cups. | A | A | yes |

### Rule 9: 5/5

Articulated rule: Label A if and only if the number is written as a word; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0109 | 2 clean rings waited outside. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0130 | Lila saved four silver books. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0067 | Aria carried nine late leaves. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0087 | Zoe counted six silver tiles. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0286 | Only 7 plain brushes stayed dry. | B | B | yes |

### Rule 10: 3/5

Articulated rule: Label A if and only if the sentence begins with a person’s name rather than with a number or another phrase.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0041 | Nora saved eight light stones. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0177 | Noah saved 6 green bags. | B | A | no |
| 3 | balanced_sentence_contains_digit_pool_0085 | The basket had five green leaves. | A | B | no |
| 4 | balanced_sentence_contains_digit_pool_0182 | 3 loose bags fell softly. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0167 | Only 8 cool pencils stayed dry. | B | B | yes |

### Rule 11: 5/5

Articulated rule: Label A if and only if the sentence uses a number word, while Label B if and only if it uses a numeral digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0071 | Ella packed 4 calm buttons. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0054 | Ryan found 4 purple brushes. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0212 | Ben found three calm tiles. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0166 | Sofia saved four simple apples. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0211 | Nora counted ten quiet apples. | A | A | yes |

### Rule 12: 5/5

Articulated rule: Label A if and only if the sentence contains the number as a word; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0249 | Tess counted three fresh maps. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0011 | Leo found 11 white beads. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0295 | Owen carried 10 green spoons. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0041 | Nora saved eight light stones. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0224 | The basket had 7 small maps. | B | B | yes |

### Rule 13: 5/5

Articulated rule: Label A if and only if the number is written out as a word; label B if and only if it is written as digits.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0088 | Ryan sorted 11 purple seeds. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0047 | Ruby found four fresh beads. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0183 | Near the door sat nine clean tickets. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0024 | The shelf held 6 purple shells. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0224 | The basket had 7 small maps. | B | B | yes |

### Rule 14: 5/5

Articulated rule: Label A if and only if the number is written as a word; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0038 | The basket had twelve clean spoons. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0245 | Only 7 early pens stayed dry. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0266 | Milo found 9 cool notes. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0145 | Near the door sat three happy beads. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0054 | Ryan found 4 purple brushes. | B | B | yes |

### Rule 15: 5/5

Articulated rule: Label A if and only if the number in the sentence is written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0154 | Clara found six simple cookies. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0185 | Only three warm shells stayed dry. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0295 | Owen carried 10 green spoons. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0041 | Nora saved eight light stones. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0072 | Eli counted 7 brown tiles. | B | B | yes |

### Rule 16: 5/5

Articulated rule: Label A if and only if the sentence contains the number written as a word; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0155 | The shelf held 3 warm towels. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0248 | Emma counted 3 cool boxes. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0102 | The shelf held eleven quick tiles. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0096 | Cole carried 4 early tiles. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0128 | Near the door sat 4 calm keys. | B | B | yes |

### Rule 17: 5/5

Articulated rule: Label A if and only if the number is written as a word; label B if and only if it is written as a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0153 | Near the door sat three blue rings. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0183 | Near the door sat nine clean tickets. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0116 | Near the door sat 6 tiny cookies. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0110 | 5 round notes waited outside. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0189 | Leo counted two bright boxes. | A | A | yes |

### Rule 18: 5/5

Articulated rule: Label A if and only if the quantity is written as a word rather than a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0088 | Ryan sorted 11 purple seeds. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0096 | Cole carried 4 early tiles. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0156 | Only seven early pens stayed dry. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0011 | Leo found 11 white beads. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0235 | Nine blue books fell softly. | A | A | yes |

### Rule 19: 5/5

Articulated rule: Label A if and only if the number is written as a word; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0039 | Twelve smooth keys fell softly. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0297 | Three warm photos fell softly. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0240 | Owen found 4 warm pens. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0083 | Tess sorted seven yellow coins. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0176 | Ben saved six brown rings. | A | A | yes |

### Rule 20: 5/5

Articulated rule: Label A if and only if the sentence contains the quantity written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0208 | Only seven plain brushes stayed dry. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0022 | Only 6 yellow cookies stayed dry. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0274 | Finn packed seven calm cookies. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0263 | Near the door sat two round apples. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0210 | Ben carried 2 quick mugs. | B | B | yes |

### Rule 21: 5/5

Articulated rule: Label A if and only if the number is written as a word; label B if and only if it is written as digits.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0101 | Two clean maps fell softly. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0085 | The basket had five green leaves. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0004 | The shelf held 9 blue shells. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0149 | 8 loose cookies waited outside. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0110 | 5 round notes waited outside. | B | B | yes |

### Rule 22: 5/5

Articulated rule: Label A if and only if the number is written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0172 | The basket had eleven yellow apples. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0188 | Clara sorted ten quick buttons. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0181 | Noah packed 10 plain cups. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0155 | The shelf held 3 warm towels. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0158 | Sofia saved 4 simple apples. | B | B | yes |

### Rule 23: 5/5

Articulated rule: Label A if and only if the number is written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0289 | Luca saved nine simple photos. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0003 | Ryan sorted 7 calm keys. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0158 | Sofia saved 4 simple apples. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0042 | Three tiny stones fell softly. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0134 | Lila saved 4 silver books. | B | B | yes |

### Rule 24: 5/5

Articulated rule: Label A if and only if the number is written as a word; label B if and only if the number is written as a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0290 | 2 crisp mugs waited outside. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0153 | Near the door sat three blue rings. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0056 | Eight loose cookies waited outside. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0150 | Near the door sat four small coins. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0032 | The basket had ten purple notes. | A | A | yes |

### Rule 25: 5/5

Articulated rule: Label A if and only if the sentence contains a number word (like “five” or “ten”) rather than a numeral digit (like “5” or “10”).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0033 | Only six yellow cookies stayed dry. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0234 | Owen found five loose leaves. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0044 | The basket had 4 cool coins. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0052 | The shelf held 11 quick tiles. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0230 | Ryan sorted seven calm keys. | A | A | yes |

### Rule 26: 5/5

Articulated rule: Label A if and only if the number is written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0109 | 2 clean rings waited outside. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0095 | The shelf held twelve quiet beads. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0226 | Nora sorted 4 clean candles. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0296 | Theo carried 12 soft mugs. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0283 | Clara found 6 simple cookies. | B | B | yes |

### Rule 27: 5/5

Articulated rule: Label A if and only if the number is written as a word; label B if and only if it is written as a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0072 | Eli counted 7 brown tiles. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0005 | Only twelve fresh stones stayed dry. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0075 | 7 plain mugs waited outside. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0003 | Ryan sorted 7 calm keys. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0036 | Five cool leaves fell softly. | A | A | yes |

### Rule 28: 5/5

Articulated rule: Label A if and only if the number is written as a word; label B if and only if it is written as a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0120 | Only eight cool pencils stayed dry. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0146 | Zoe sorted seven bright mugs. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0079 | The shelf held three yellow towels. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0067 | Aria carried nine late leaves. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0029 | Only eight quiet apples stayed dry. | A | A | yes |

### Rule 29: 5/5

Articulated rule: Label A if and only if the sentence contains a number word, rather than a numeral digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0270 | Grace found eleven quick pens. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0054 | Ryan found 4 purple brushes. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0087 | Zoe counted six silver tiles. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0254 | Six crisp leaves fell softly. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0011 | Leo found 11 white beads. | B | B | yes |

### Rule 30: 5/5

Articulated rule: Label A if and only if the sentence contains a number word, and Label B if and only if it contains a numeral digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0220 | Ruby saved two tiny brushes. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0141 | Ten yellow spoons waited outside. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0259 | Max sorted 12 round cups. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0200 | Nora counted 10 quiet apples. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0034 | Jonah carried 9 silver plates. | B | B | yes |

### Rule 31: 5/5

Articulated rule: Label A if and only if the sentence contains the number written as a word; Label B if only if it contains the number written as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0177 | Noah saved 6 green bags. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0126 | Ruby carried nine smooth bags. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0089 | Cole carried four early tiles. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0179 | Jonah saved 5 neat mugs. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0201 | Zoe counted 6 silver tiles. | B | B | yes |

### Rule 32: 5/5

Articulated rule: Label A if and only if the sentence uses a spelled-out number word; otherwise label B if it uses a numeral digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0233 | Theo sorted 3 brown flowers. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0273 | Owen found two bright stones. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0058 | 5 cool leaves fell softly. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0188 | Clara sorted ten quick buttons. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0080 | The basket had eleven white coins. | A | A | yes |

### Rule 33: 5/5

Articulated rule: Label A if and only if the sentence contains a number written as a word; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0084 | Maya sorted nine silver brushes. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0212 | Ben found three calm tiles. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0009 | 3 fresh cookies fell softly. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0194 | Theo found 10 late books. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0005 | Only twelve fresh stones stayed dry. | A | A | yes |

### Rule 34: 5/5

Articulated rule: Label A if and only if the number is written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0286 | Only 7 plain brushes stayed dry. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0212 | Ben found three calm tiles. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0065 | Theo saved 5 smooth stones. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0233 | Theo sorted 3 brown flowers. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0025 | Only 12 happy stones stayed dry. | B | B | yes |

### Rule 35: 5/5

Articulated rule: Label A if and only if the sentence uses a number word rather than a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0236 | Theo carried twelve white towels. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0078 | Three soft cookies fell softly. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0090 | Eleven quiet maps fell softly. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0260 | Eli counted seven brown tiles. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0029 | Only eight quiet apples stayed dry. | A | A | yes |

### Rule 36: 5/5

Articulated rule: Label A if and only if the number is written as a word; label B if and only if it is written as digits.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0001 | Noah saved six green bags. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0041 | Nora saved eight light stones. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0006 | Five round notes waited outside. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0198 | Ella saved 2 yellow candles. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0036 | Five cool leaves fell softly. | A | A | yes |

### Rule 37: 5/5

Articulated rule: Label A if and only if the number is written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0000 | Aria packed 11 loose flowers. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0115 | The shelf held nine blue shells. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0290 | 2 crisp mugs waited outside. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0248 | Emma counted 3 cool boxes. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0273 | Owen found two bright stones. | A | A | yes |

### Rule 38: 5/5

Articulated rule: Label A if and only if the sentence contains a number word, not a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0156 | Only seven early pens stayed dry. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0123 | Near the door sat 3 happy beads. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0160 | Ruby found 4 fresh beads. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0072 | Eli counted 7 brown tiles. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0141 | Ten yellow spoons waited outside. | A | A | yes |

### Rule 39: 5/5

Articulated rule: Label A if and only if the sentence contains a number written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0047 | Ruby found four fresh beads. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0264 | Theo saved five smooth stones. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0058 | 5 cool leaves fell softly. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0106 | Ben carried seven warm apples. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0115 | The shelf held nine blue shells. | A | A | yes |

### Rule 40: 5/5

Articulated rule: Label A if and only if the sentence contains a number word, rather than a numeral digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0151 | Near the door sat 4 silver bags. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0090 | Eleven quiet maps fell softly. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0046 | Ryan sorted eleven purple seeds. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0166 | Sofia saved four simple apples. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0170 | Owen carried ten green spoons. | A | A | yes |

### Rule 41: 5/5

Articulated rule: Label A if and only if the sentence contains a number written as a word; Label B if and only if it contains the number as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0090 | Eleven quiet maps fell softly. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0115 | The shelf held nine blue shells. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0145 | Near the door sat three happy beads. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0079 | The shelf held three yellow towels. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0083 | Tess sorted seven yellow coins. | A | A | yes |

### Rule 42: 5/5

Articulated rule: Label A if and only if the number is written as a word; label B if and only if the number is written as a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0179 | Jonah saved 5 neat mugs. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0128 | Near the door sat 4 calm keys. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0130 | Lila saved four silver books. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0234 | Owen found five loose leaves. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0262 | Ella packed four calm buttons. | A | A | yes |

### Rule 43: 5/5

Articulated rule: Label A if and only if the sentence contains the number written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0005 | Only twelve fresh stones stayed dry. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0019 | Only 12 brown leaves stayed dry. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0096 | Cole carried 4 early tiles. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0048 | The shelf held 5 calm pens. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0257 | The shelf held ten cool maps. | A | A | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if the sentence contains the quantity written as a word rather than as a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0046 | Ryan sorted eleven purple seeds. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0041 | Nora saved eight light stones. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0103 | Ella sorted 6 round coins. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0207 | Luca sorted 7 quick rings. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0296 | Theo carried 12 soft mugs. | B | B | yes |

### Rule 45: 5/5

Articulated rule: Label A if and only if the sentence contains a spelled-out number, while Label B if and only if it contains a numeral digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0067 | Aria carried nine late leaves. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0215 | Milo packed four blue boxes. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0021 | 11 quiet maps fell softly. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0202 | Seven neat towels waited outside. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0180 | Nine simple beads waited outside. | A | A | yes |

### Rule 46: 5/5

Articulated rule: Label A if and only if the sentence uses the number word spelled out; label B if and only if it uses the numeral digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0187 | The shelf held 6 early brushes. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0094 | 4 neat books waited outside. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0230 | Ryan sorted seven calm keys. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0178 | Near the door sat six late beads. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0093 | Three loose bags fell softly. | A | A | yes |

### Rule 47: 4/5

Articulated rule: Label A if and only if the number word or numeral in the sentence is even when written as a word, and odd when written as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0226 | Nora sorted 4 clean candles. | B | B | yes |
| 2 | balanced_sentence_contains_digit_pool_0263 | Near the door sat two round apples. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0114 | Finn counted 5 quiet coins. | B | A | no |
| 4 | balanced_sentence_contains_digit_pool_0052 | The shelf held 11 quick tiles. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0271 | Theo sorted 2 purple seeds. | B | B | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if the sentence contains the number written as a word rather than as a digit.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0184 | Finn found two early rings. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0176 | Ben saved six brown rings. | A | A | yes |
| 3 | balanced_sentence_contains_digit_pool_0167 | Only 8 cool pencils stayed dry. | B | B | yes |
| 4 | balanced_sentence_contains_digit_pool_0141 | Ten yellow spoons waited outside. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0022 | Only 6 yellow cookies stayed dry. | B | B | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if the number is written as a word rather than as digits.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0192 | Ivy saved ten fresh brushes. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0237 | Nina counted 11 quiet cups. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0038 | The basket had twelve clean spoons. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0211 | Nora counted ten quiet apples. | A | A | yes |
| 5 | balanced_sentence_contains_digit_pool_0182 | 3 loose bags fell softly. | B | B | yes |

### Rule 50: 5/5

Articulated rule: Label A if and only if the sentence writes the number as a word rather than using a numeral.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | balanced_sentence_contains_digit_pool_0242 | Nina counted eleven quiet cups. | A | A | yes |
| 2 | balanced_sentence_contains_digit_pool_0294 | Ryan sorted 4 quiet pens. | B | B | yes |
| 3 | balanced_sentence_contains_digit_pool_0262 | Ella packed four calm buttons. | A | A | yes |
| 4 | balanced_sentence_contains_digit_pool_0013 | 6 tiny tiles waited outside. | B | B | yes |
| 5 | balanced_sentence_contains_digit_pool_0266 | Milo found 9 cool notes. | B | B | yes |

