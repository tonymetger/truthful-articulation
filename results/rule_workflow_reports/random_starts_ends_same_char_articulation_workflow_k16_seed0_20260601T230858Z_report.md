# Rule Articulation Workflow: random_starts_ends_same_char

Run ID: `random_starts_ends_same_char_articulation_workflow_k16_seed0_20260601T230858Z`

Correct prompt-facing rule: Label B iff the first and last character are the same; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.520
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.520
- Rules with all evals correct: 2
- Rules with any eval correct: 48

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
| 1 | 2/5 | Label A if and only if the string contains more consonants than vowels. |
| 2 | 4/5 | Label A if and only if the string contains more vowels than the letter y. |
| 3 | 3/5 | Label A if and only if the input contains an odd number of vowels. |
| 4 | 3/5 | Label A if and only if the string contains more consonants from the first half of the alphabet (a–m) than from the second half (n–z). |
| 5 | 4/5 | Label A if and only if the string contains an odd number of vowels. |
| 6 | 3/5 | Label A if and only if the input contains an even number of vowels. |
| 7 | 3/5 | Label A if and only if the string contains an odd number of vowels. |
| 8 | 2/5 | Label A if and only if the string contains more consonants than vowels. |
| 9 | 2/5 | Label A if and only if the string contains more consonants than vowels. |
| 10 | 3/5 | Label A if and only if the string contains more consonants than vowels. |
| 11 | 2/5 | Label A if and only if the input contains more consonants than vowels. |
| 12 | 3/5 | Label A if and only if the input contains more vowels than consonants. |
| 13 | 2/5 | Label A if and only if the string contains an odd number of vowels. |
| 14 | 3/5 | Label A if and only if the string contains more consonants than vowels. |
| 15 | 3/5 | Label A if and only if the string contains an even number of vowels. |
| 16 | 2/5 | Label A if and only if the string contains more consonants than vowels. |
| 17 | 1/5 | Label A if and only if the string contains more consonants from the first half of the alphabet (b–m) than from the second half (n–z). |
| 18 | 2/5 | Label A if and only if the string contains an odd number of vowels. |
| 19 | 3/5 | Label A if and only if the string contains an odd number of vowels. |
| 20 | 4/5 | Label A if and only if the string contains more consonants than vowels. |
| 21 | 2/5 | Label A if and only if the string contains an odd number of vowels. |
| 22 | 2/5 | Label A if and only if the string contains more consonants than vowels. |
| 23 | 1/5 | Label A if and only if the input contains an odd number of vowels. |
| 24 | 1/5 | Label A if and only if the input contains more vowels than the label-B examples do, namely at least two vowels. |
| 25 | 4/5 | Label A if and only if the input contains more consonants than vowels. |
| 26 | 3/5 | Label A if and only if the string contains more consonants than vowels. |
| 27 | 5/5 | Label A if and only if the input contains more vowels than consonants. |
| 28 | 3/5 | Label A if and only if the string contains more consonants than vowels. |
| 29 | 2/5 | Label A if and only if the string contains more vowels than the letter "v". |
| 30 | 2/5 | Label A if and only if the string contains an even number of consonants. |
| 31 | 0/5 | Label A if and only if the string contains an even number of vowels. |
| 32 | 4/5 | Label A if and only if the string contains an even number of vowels. |
| 33 | 5/5 | Label A if and only if the input contains more consonants than vowels. |
| 34 | 3/5 | Label A if and only if the input contains an odd number of vowels. |
| 35 | 3/5 | Label A if and only if the string contains an even number of vowels. |
| 36 | 4/5 | Label A if and only if the string contains more consonants from the first half of the alphabet (a–m) than from the second half (n–z). |
| 37 | 1/5 | Label A if and only if the input contains more vowels than the letter "w". |
| 38 | 3/5 | Label A if and only if the string contains more vowels than consonants. |
| 39 | 2/5 | Label A if and only if the string contains more consonants than vowels. |
| 40 | 0/5 | Label A if and only if the string contains more consonants than vowels. |
| 41 | 2/5 | Label A if and only if the string contains more consonants than vowels. |
| 42 | 4/5 | Label A if and only if the string contains more consonants than vowels. |
| 43 | 3/5 | Label A if and only if the string contains more vowels than the string labeled B examples typically do—specifically, at least 3 vowels. |
| 44 | 3/5 | Label A if and only if the string contains more consonants than vowels. |
| 45 | 3/5 | Label A if and only if the input contains more vowels than the letter y. |
| 46 | 2/5 | Label A if and only if the input contains more vowels than the letter m. |
| 47 | 2/5 | Label A if and only if the string contains more vowels than the string labeled B examples do—specifically, at least 3 vowels. |
| 48 | 2/5 | Label A if and only if the input contains more consonants than vowels. |
| 49 | 2/5 | Label A if and only if the string contains at least one of the vowels a, e, i, o, or u exactly once. |
| 50 | 3/5 | Label A if and only if the string contains more vowels than consonants. |

## Detailed Evaluations

### Rule 1: 2/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0375 | jocj | B | A | no |
| 2 | random_starts_ends_same_char_pool_0347 | tfzbnnkn | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0104 | elqgrmcee | B | A | no |
| 4 | random_starts_ends_same_char_pool_0417 | wivaktblf | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0035 | selljujs | B | A | no |

### Rule 2: 4/5

Articulated rule: Label A if and only if the string contains more vowels than the letter y.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0136 | rixluliq | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0271 | migdskzm | B | B | yes |
| 3 | random_starts_ends_same_char_pool_0129 | zzkdz | B | B | yes |
| 4 | random_starts_ends_same_char_pool_0484 | aspqtnhvx | A | B | no |
| 5 | random_starts_ends_same_char_pool_0430 | mwzm | B | B | yes |

### Rule 3: 3/5

Articulated rule: Label A if and only if the input contains an odd number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0048 | gqjihcodrq | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0254 | lqmqql | B | A | no |
| 3 | random_starts_ends_same_char_pool_0414 | zlebq | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0008 | dmdnepssk | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0363 | yfcnjjy | B | A | no |

### Rule 4: 3/5

Articulated rule: Label A if and only if the string contains more consonants from the first half of the alphabet (a–m) than from the second half (n–z).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0378 | afmtwuaa | B | A | no |
| 2 | random_starts_ends_same_char_pool_0297 | ufbfuaqm | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0145 | prbqkhvfokp | B | A | no |
| 4 | random_starts_ends_same_char_pool_0125 | tfmaw | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0381 | gbqqpche | A | A | yes |

### Rule 5: 4/5

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0039 | cemoim | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0193 | ckqc | B | B | yes |
| 3 | random_starts_ends_same_char_pool_0010 | dkcq | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0157 | unmajuhgycu | B | A | no |
| 5 | random_starts_ends_same_char_pool_0176 | hbsh | B | B | yes |

### Rule 6: 3/5

Articulated rule: Label A if and only if the input contains an even number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0259 | iglajto | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0292 | uqtzf | A | B | no |
| 3 | random_starts_ends_same_char_pool_0361 | xzebaem | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0411 | bpewewtlokvc | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0472 | emowrglwbe | B | A | no |

### Rule 7: 3/5

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0156 | nhqeyfvpqtex | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0329 | cnbolttc | B | A | no |
| 3 | random_starts_ends_same_char_pool_0331 | stjvffspbv | A | B | no |
| 4 | random_starts_ends_same_char_pool_0436 | rnojohtrndn | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0369 | gazml | A | A | yes |

### Rule 8: 2/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0412 | fxymkizf | B | A | no |
| 2 | random_starts_ends_same_char_pool_0277 | zxqiybmlwg | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0463 | rxnpoditkiir | B | A | no |
| 4 | random_starts_ends_same_char_pool_0027 | lldd | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0104 | elqgrmcee | B | A | no |

### Rule 9: 2/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0103 | hyfjlh | B | A | no |
| 2 | random_starts_ends_same_char_pool_0122 | onvnao | B | B | yes |
| 3 | random_starts_ends_same_char_pool_0063 | wiwqio | A | B | no |
| 4 | random_starts_ends_same_char_pool_0488 | nbdn | B | A | no |
| 5 | random_starts_ends_same_char_pool_0341 | krdz | A | A | yes |

### Rule 10: 3/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0040 | fcydmi | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0298 | kxzxnmak | B | A | no |
| 3 | random_starts_ends_same_char_pool_0300 | ndrjtrn | B | A | no |
| 4 | random_starts_ends_same_char_pool_0177 | kpbyhiwknzl | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0410 | dkhkzprmrghn | A | A | yes |

### Rule 11: 2/5

Articulated rule: Label A if and only if the input contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0068 | fatrilxgmf | B | A | no |
| 2 | random_starts_ends_same_char_pool_0050 | lnbtol | B | A | no |
| 3 | random_starts_ends_same_char_pool_0300 | ndrjtrn | B | A | no |
| 4 | random_starts_ends_same_char_pool_0209 | milqtkekedxl | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0163 | rcjwqyymb | A | A | yes |

### Rule 12: 3/5

Articulated rule: Label A if and only if the input contains more vowels than consonants.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0244 | ewlkvgdwk | A | B | no |
| 2 | random_starts_ends_same_char_pool_0011 | nymfevnmoxxn | B | B | yes |
| 3 | random_starts_ends_same_char_pool_0412 | fxymkizf | B | B | yes |
| 4 | random_starts_ends_same_char_pool_0291 | hytt | A | B | no |
| 5 | random_starts_ends_same_char_pool_0482 | rymbfhr | B | B | yes |

### Rule 13: 2/5

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0086 | xmtopj | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0046 | ogktdto | B | A | no |
| 3 | random_starts_ends_same_char_pool_0183 | lfsbdgpckhip | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0023 | wrjwwvgzg | A | B | no |
| 5 | random_starts_ends_same_char_pool_0482 | rymbfhr | B | A | no |

### Rule 14: 3/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0038 | sfuqbyks | B | A | no |
| 2 | random_starts_ends_same_char_pool_0238 | sxzsknnpgf | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0259 | iglajto | A | B | no |
| 4 | random_starts_ends_same_char_pool_0140 | tgfpz | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0362 | jfszf | A | A | yes |

### Rule 15: 3/5

Articulated rule: Label A if and only if the string contains an even number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0387 | umcwyptuksl | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0456 | coixsiwrzmc | B | A | no |
| 3 | random_starts_ends_same_char_pool_0297 | ufbfuaqm | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0444 | ilsip | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0151 | uffrfphcwqiu | B | A | no |

### Rule 16: 2/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0151 | uffrfphcwqiu | B | A | no |
| 2 | random_starts_ends_same_char_pool_0460 | csqkhohlc | B | A | no |
| 3 | random_starts_ends_same_char_pool_0343 | cxrjujtnl | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0377 | eudn | A | B | no |
| 5 | random_starts_ends_same_char_pool_0241 | rbmrlualz | A | A | yes |

### Rule 17: 1/5

Articulated rule: Label A if and only if the string contains more consonants from the first half of the alphabet (b–m) than from the second half (n–z).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0157 | unmajuhgycu | B | A | no |
| 2 | random_starts_ends_same_char_pool_0186 | esqztoqdmmjl | A | B | no |
| 3 | random_starts_ends_same_char_pool_0341 | krdz | A | B | no |
| 4 | random_starts_ends_same_char_pool_0116 | kqabbydsk | B | A | no |
| 5 | random_starts_ends_same_char_pool_0337 | uwzu | B | B | yes |

### Rule 18: 2/5

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0089 | wctcafiosq | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0096 | gfcwkmpmtqmb | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0155 | zggjqwnuxxz | B | A | no |
| 4 | random_starts_ends_same_char_pool_0012 | nfaozign | B | A | no |
| 5 | random_starts_ends_same_char_pool_0373 | hnmpzangh | B | A | no |

### Rule 19: 3/5

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0037 | npufbtqijqda | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0387 | umcwyptuksl | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0289 | nswpentqqvcf | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0233 | vvgiluqouo | A | B | no |
| 5 | random_starts_ends_same_char_pool_0078 | xvmn | A | B | no |

### Rule 20: 4/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0347 | tfzbnnkn | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0204 | ybvmijmicu | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0021 | xvxderdll | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0269 | bxqhoqx | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0258 | aoigwfp | A | B | no |

### Rule 21: 2/5

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0470 | lsrbxul | B | A | no |
| 2 | random_starts_ends_same_char_pool_0095 | bvab | B | A | no |
| 3 | random_starts_ends_same_char_pool_0079 | iwynjgedvh | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0485 | wdprlykdw | B | A | no |
| 5 | random_starts_ends_same_char_pool_0004 | myix | A | A | yes |

### Rule 22: 2/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0471 | rwtzd | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0168 | pdtaqtp | B | A | no |
| 3 | random_starts_ends_same_char_pool_0184 | ohtktuekheo | B | A | no |
| 4 | random_starts_ends_same_char_pool_0177 | kpbyhiwknzl | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0152 | leoidsoihl | B | A | no |

### Rule 23: 1/5

Articulated rule: Label A if and only if the input contains an odd number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0338 | rfigzikr | B | A | no |
| 2 | random_starts_ends_same_char_pool_0367 | kprk | B | A | no |
| 3 | random_starts_ends_same_char_pool_0286 | uvgrtu | B | A | no |
| 4 | random_starts_ends_same_char_pool_0003 | bmadb | B | A | no |
| 5 | random_starts_ends_same_char_pool_0457 | fcpytmmfabcd | A | A | yes |

### Rule 24: 1/5

Articulated rule: Label A if and only if the input contains more vowels than the label-B examples do, namely at least two vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0287 | kaysyu | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0152 | leoidsoihl | B | A | no |
| 3 | random_starts_ends_same_char_pool_0365 | ieuqi | B | A | no |
| 4 | random_starts_ends_same_char_pool_0058 | gdpncdpwoqxg | B | A | no |
| 5 | random_starts_ends_same_char_pool_0149 | epjzwklute | B | A | no |

### Rule 25: 4/5

Articulated rule: Label A if and only if the input contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0033 | iqjzig | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0450 | xwoqzzwx | B | A | no |
| 3 | random_starts_ends_same_char_pool_0230 | svdinud | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0309 | vkfwkfhpmfd | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0429 | sshmir | A | A | yes |

### Rule 26: 3/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0105 | fsdquzrf | B | A | no |
| 2 | random_starts_ends_same_char_pool_0092 | jatw | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0220 | webd | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0289 | nswpentqqvcf | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0276 | svkgnqqds | B | A | no |

### Rule 27: 5/5

Articulated rule: Label A if and only if the input contains more vowels than consonants.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0068 | fatrilxgmf | B | B | yes |
| 2 | random_starts_ends_same_char_pool_0345 | jnddj | B | B | yes |
| 3 | random_starts_ends_same_char_pool_0005 | kogljk | B | B | yes |
| 4 | random_starts_ends_same_char_pool_0071 | sjwwzs | B | B | yes |
| 5 | random_starts_ends_same_char_pool_0003 | bmadb | B | B | yes |

### Rule 28: 3/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0113 | atbmebgvsmgq | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0139 | qrwd | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0339 | koxft | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0073 | ojexpbo | B | A | no |
| 5 | random_starts_ends_same_char_pool_0063 | wiwqio | A | B | no |

### Rule 29: 2/5

Articulated rule: Label A if and only if the string contains more vowels than the letter "v".

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0475 | qxxa | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0262 | zhkqhz | B | B | yes |
| 3 | random_starts_ends_same_char_pool_0053 | annsvkwha | B | A | no |
| 4 | random_starts_ends_same_char_pool_0365 | ieuqi | B | A | no |
| 5 | random_starts_ends_same_char_pool_0296 | yhsig | A | B | no |

### Rule 30: 2/5

Articulated rule: Label A if and only if the string contains an even number of consonants.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0217 | bzukktztoa | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0139 | qrwd | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0296 | yhsig | A | B | no |
| 4 | random_starts_ends_same_char_pool_0257 | buiimdljlb | B | A | no |
| 5 | random_starts_ends_same_char_pool_0320 | iauqdcki | B | A | no |

### Rule 31: 0/5

Articulated rule: Label A if and only if the string contains an even number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0171 | gwdvrpbg | B | A | no |
| 2 | random_starts_ends_same_char_pool_0122 | onvnao | B | A | no |
| 3 | random_starts_ends_same_char_pool_0299 | stuwqdwys | B | A | no |
| 4 | random_starts_ends_same_char_pool_0323 | keirvyyack | B | A | no |
| 5 | random_starts_ends_same_char_pool_0085 | nzeayqen | B | A | no |

### Rule 32: 4/5

Articulated rule: Label A if and only if the string contains an even number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0330 | timseueacfb | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0300 | ndrjtrn | B | A | no |
| 3 | random_starts_ends_same_char_pool_0225 | kkbqek | B | B | yes |
| 4 | random_starts_ends_same_char_pool_0265 | ncxvnrwew | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0054 | btrcsy | A | A | yes |

### Rule 33: 5/5

Articulated rule: Label A if and only if the input contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0082 | ktlqonzgmbm | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0364 | rtss | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0413 | jtwgnax | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0209 | milqtkekedxl | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0009 | boqr | A | A | yes |

### Rule 34: 3/5

Articulated rule: Label A if and only if the input contains an odd number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0440 | esvfxhqyje | B | A | no |
| 2 | random_starts_ends_same_char_pool_0282 | fvpd | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0211 | aytvqjdnxym | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0066 | qowi | A | B | no |
| 5 | random_starts_ends_same_char_pool_0231 | zdlxm | A | A | yes |

### Rule 35: 3/5

Articulated rule: Label A if and only if the string contains an even number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0234 | rpnsupydgvbl | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0302 | eedtlfane | B | A | no |
| 3 | random_starts_ends_same_char_pool_0074 | iehyi | B | A | no |
| 4 | random_starts_ends_same_char_pool_0417 | wivaktblf | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0464 | xaupibctuxbl | A | A | yes |

### Rule 36: 4/5

Articulated rule: Label A if and only if the string contains more consonants from the first half of the alphabet (a–m) than from the second half (n–z).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0001 | yabbahzkd | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0040 | fcydmi | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0354 | alrvpveyxia | B | A | no |
| 4 | random_starts_ends_same_char_pool_0414 | zlebq | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0420 | rbxgjrgi | A | A | yes |

### Rule 37: 1/5

Articulated rule: Label A if and only if the input contains more vowels than the letter "w".

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0497 | rwfntdwim | A | B | no |
| 2 | random_starts_ends_same_char_pool_0000 | eztqyryque | B | A | no |
| 3 | random_starts_ends_same_char_pool_0110 | yfzfz | A | B | no |
| 4 | random_starts_ends_same_char_pool_0281 | tsqcstwsoj | A | B | no |
| 5 | random_starts_ends_same_char_pool_0241 | rbmrlualz | A | A | yes |

### Rule 38: 3/5

Articulated rule: Label A if and only if the string contains more vowels than consonants.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0150 | ntkpwjbapxe | A | B | no |
| 2 | random_starts_ends_same_char_pool_0116 | kqabbydsk | B | B | yes |
| 3 | random_starts_ends_same_char_pool_0155 | zggjqwnuxxz | B | B | yes |
| 4 | random_starts_ends_same_char_pool_0070 | jmspvoty | A | B | no |
| 5 | random_starts_ends_same_char_pool_0485 | wdprlykdw | B | B | yes |

### Rule 39: 2/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0049 | mobdpm | B | A | no |
| 2 | random_starts_ends_same_char_pool_0262 | zhkqhz | B | A | no |
| 3 | random_starts_ends_same_char_pool_0384 | zjzefriraz | B | A | no |
| 4 | random_starts_ends_same_char_pool_0429 | sshmir | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0311 | hllkfngmba | A | A | yes |

### Rule 40: 0/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0344 | tzmt | B | A | no |
| 2 | random_starts_ends_same_char_pool_0327 | jrukfj | B | A | no |
| 3 | random_starts_ends_same_char_pool_0149 | epjzwklute | B | A | no |
| 4 | random_starts_ends_same_char_pool_0088 | dvcqisjlvxd | B | A | no |
| 5 | random_starts_ends_same_char_pool_0418 | xmhoutqrlfnx | B | A | no |

### Rule 41: 2/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0088 | dvcqisjlvxd | B | A | no |
| 2 | random_starts_ends_same_char_pool_0305 | buhmyyiza | A | B | no |
| 3 | random_starts_ends_same_char_pool_0408 | pzldxakylo | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0112 | uqjatelvlu | B | A | no |
| 5 | random_starts_ends_same_char_pool_0425 | vuav | B | B | yes |

### Rule 42: 4/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0478 | maxtyv | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0171 | gwdvrpbg | B | A | no |
| 3 | random_starts_ends_same_char_pool_0475 | qxxa | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0487 | qtvl | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0125 | tfmaw | A | A | yes |

### Rule 43: 3/5

Articulated rule: Label A if and only if the string contains more vowels than the string labeled B examples typically do—specifically, at least 3 vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0005 | kogljk | B | B | yes |
| 2 | random_starts_ends_same_char_pool_0019 | xgknyeudhlyx | B | A | no |
| 3 | random_starts_ends_same_char_pool_0092 | jatw | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0306 | impdwcnguf | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0047 | jqmiplj | B | A | no |

### Rule 44: 3/5

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0042 | ysxrmieuscj | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0038 | sfuqbyks | B | A | no |
| 3 | random_starts_ends_same_char_pool_0098 | hcez | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0203 | mclm | B | A | no |
| 5 | random_starts_ends_same_char_pool_0437 | zhacrdvjnmj | A | A | yes |

### Rule 45: 3/5

Articulated rule: Label A if and only if the input contains more vowels than the letter y.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0066 | qowi | A | A | yes |
| 2 | random_starts_ends_same_char_pool_0351 | wdpw | B | B | yes |
| 3 | random_starts_ends_same_char_pool_0205 | yeabty | B | A | no |
| 4 | random_starts_ends_same_char_pool_0415 | xscel | A | A | yes |
| 5 | random_starts_ends_same_char_pool_0022 | jtfjiqdrvvkj | B | A | no |

### Rule 46: 2/5

Articulated rule: Label A if and only if the input contains more vowels than the letter m.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0337 | uwzu | B | A | no |
| 2 | random_starts_ends_same_char_pool_0314 | whbjrcw | B | B | yes |
| 3 | random_starts_ends_same_char_pool_0358 | nixuynxbanrn | B | A | no |
| 4 | random_starts_ends_same_char_pool_0185 | fqceygf | B | A | no |
| 5 | random_starts_ends_same_char_pool_0392 | qviz | A | A | yes |

### Rule 47: 2/5

Articulated rule: Label A if and only if the string contains more vowels than the string labeled B examples do—specifically, at least 3 vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0416 | sfcch | A | B | no |
| 2 | random_starts_ends_same_char_pool_0220 | webd | A | A | yes |
| 3 | random_starts_ends_same_char_pool_0450 | xwoqzzwx | B | A | no |
| 4 | random_starts_ends_same_char_pool_0255 | nyvwn | B | B | yes |
| 5 | random_starts_ends_same_char_pool_0114 | sngogmcdrms | B | A | no |

### Rule 48: 2/5

Articulated rule: Label A if and only if the input contains more consonants than vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0385 | tynotsxqgft | B | A | no |
| 2 | random_starts_ends_same_char_pool_0456 | coixsiwrzmc | B | A | no |
| 3 | random_starts_ends_same_char_pool_0179 | tupndfivwghu | A | A | yes |
| 4 | random_starts_ends_same_char_pool_0171 | gwdvrpbg | B | A | no |
| 5 | random_starts_ends_same_char_pool_0454 | anywiira | B | B | yes |

### Rule 49: 2/5

Articulated rule: Label A if and only if the string contains at least one of the vowels a, e, i, o, or u exactly once.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0188 | jayokj | B | A | no |
| 2 | random_starts_ends_same_char_pool_0498 | jojxeniylino | A | B | no |
| 3 | random_starts_ends_same_char_pool_0235 | grpg | B | B | yes |
| 4 | random_starts_ends_same_char_pool_0455 | gxzg | B | B | yes |
| 5 | random_starts_ends_same_char_pool_0364 | rtss | A | B | no |

### Rule 50: 3/5

Articulated rule: Label A if and only if the string contains more vowels than consonants.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | random_starts_ends_same_char_pool_0485 | wdprlykdw | B | B | yes |
| 2 | random_starts_ends_same_char_pool_0237 | ihadtzi | B | A | no |
| 3 | random_starts_ends_same_char_pool_0287 | kaysyu | A | B | no |
| 4 | random_starts_ends_same_char_pool_0304 | yyznowqwjcby | B | B | yes |
| 5 | random_starts_ends_same_char_pool_0386 | vnqpv | B | B | yes |

