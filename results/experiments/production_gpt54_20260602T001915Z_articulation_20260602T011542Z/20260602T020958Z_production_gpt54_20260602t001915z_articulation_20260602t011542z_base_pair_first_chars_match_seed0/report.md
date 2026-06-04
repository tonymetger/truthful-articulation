# Rule Articulation Workflow: pair_first_chars_match

Run ID: `production_gpt54_20260602T001915Z_articulation_20260602T011542Z_base_pair_first_chars_match_seed0`

Correct prompt-facing rule: Label B iff the two random strings have the same first character; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.752
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.752
- Rules with all evals correct: 24
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
| 1 | 1/5 | Label A if and only if the two strings contain the same number of vowels. |
| 2 | 2/5 | Label B if and only if the two strings start with the same letter. |
| 3 | 5/5 | Label A if and only if the two strings start with different letters or both start with the same letter and the first string is shorter than the second. |
| 4 | 3/5 | Label B if and only if the two strings start with the same letter. |
| 5 | 2/5 | Label A if and only if the second character of the first string is a vowel. |
| 6 | 5/5 | Label A if and only if the two strings start with different letters. |
| 7 | 5/5 | Label A if and only if the two strings start with different letters. |
| 8 | 5/5 | Label A if and only if the two strings start with different letters. |
| 9 | 4/5 | Label A if and only if the two strings contain the same total number of vowels. |
| 10 | 2/5 | Label A if and only if the two strings contain the same number of vowels. |
| 11 | 5/5 | Label A if and only if the two strings start with different letters. |
| 12 | 3/5 | Label A if and only if the two strings contain the same number of vowels. |
| 13 | 3/5 | Label A if and only if the second character of the first string comes earlier in the alphabet than the second character of the second string. |
| 14 | 2/5 | Label A if and only if the two parts start with letters that are consecutive in the alphabet (including the same letter); otherwise label B. |
| 15 | 5/5 | Label A if and only if the two strings start with different letters. |
| 16 | 4/5 | Label A if and only if the two strings start with different letters or the second letters are the same; otherwise label B. |
| 17 | 5/5 | Label A if and only if the two strings start with different letters. |
| 18 | 3/5 | Label A if and only if the two strings contain the same number of vowels. |
| 19 | 5/5 | Label A if and only if the two strings start with different letters. |
| 20 | 5/5 | Label A if and only if the two strings start with different letters. |
| 21 | 3/5 | Label B if and only if the two strings start with the same letter. |
| 22 | 2/5 | Label A if and only if the two strings start with letters of the same alphabetic parity (both vowels/consonants is false; rather, both first letters are both in odd positions or both in even positions in the alphabet). |
| 23 | 5/5 | Label A if and only if the two strings start with different letters. |
| 24 | 4/5 | Label A if and only if the two strings start with different letters or both have even length; otherwise label B. |
| 25 | 5/5 | Label A if and only if the two strings start with different letters. |
| 26 | 5/5 | Label A if and only if the two strings start with different letters. |
| 27 | 4/5 | Label A if and only if the two strings have the same parity of length (both even or both odd). |
| 28 | 2/5 | Label A if and only if the two strings contain the same number of vowels. |
| 29 | 3/5 | Label B if and only if the two strings start with the same letter. |
| 30 | 2/5 | Label B if and only if the two strings start with the same letter. |
| 31 | 5/5 | Label A if and only if the two strings start with different letters. |
| 32 | 3/5 | Label A if and only if the two strings have the same parity of length (both even or both odd). |
| 33 | 5/5 | Label A if and only if the two strings start with different letters. |
| 34 | 5/5 | Label A if and only if the two strings start with different letters. |
| 35 | 5/5 | Label A if and only if the two strings start with different letters. |
| 36 | 5/5 | Label A if and only if the two strings start with different letters. |
| 37 | 1/5 | Label A if and only if the two strings have the same parity of length (both odd or both even). |
| 38 | 1/5 | Label B if and only if the two strings start with the same letter. |
| 39 | 3/5 | Label A if and only if the two strings contain the same total number of vowels. |
| 40 | 2/5 | Label A if and only if the second character of the first string comes earlier in the alphabet than the second character of the second string. |
| 41 | 5/5 | Label A if and only if the two strings start with different letters. |
| 42 | 3/5 | Label B if and only if the two strings start with the same letter. |
| 43 | 5/5 | Label B if and only if the two strings start with the same letter and the second string is shorter than the first. |
| 44 | 5/5 | Label A if and only if the two strings start with letters of opposite vowel/consonant type; otherwise label B. |
| 45 | 5/5 | Label A if and only if the two strings start with different letters. |
| 46 | 5/5 | Label A if and only if the two strings start with different letters after the separator. |
| 47 | 3/5 | Label A if and only if the two strings start with letters of opposite vowel/consonant type. |
| 48 | 5/5 | Label A if and only if the two strings start with different letters. |
| 49 | 3/5 | Label A if and only if the two strings contain the same number of vowels. |
| 50 | 5/5 | Label A if and only if the two strings start with different letters; otherwise label B. |

## Detailed Evaluations

### Rule 1: 1/5

Articulated rule: Label A if and only if the two strings contain the same number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0376 | dgidtiqgwgva \|\| dbgxni | B | A | no |
| 2 | pair_first_chars_match_pool_0347 | qxiudqssy \|\| grfuralu | A | A | yes |
| 3 | pair_first_chars_match_pool_0104 | cqvomwjy \|\| aozvomvban | A | B | no |
| 4 | pair_first_chars_match_pool_0417 | rioltiu \|\| wqhz | A | B | no |
| 5 | pair_first_chars_match_pool_0035 | qeztq \|\| qyry | B | A | no |

### Rule 2: 2/5

Articulated rule: Label B if and only if the two strings start with the same letter.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0136 | wlmvxmiah \|\| qlgkqbi | A | A | yes |
| 2 | pair_first_chars_match_pool_0272 | uoubmrvp \|\| udikbpjrtyu | B | B | yes |
| 3 | pair_first_chars_match_pool_0128 | zovwjjsenon \|\| whbbz | A | B | no |
| 4 | pair_first_chars_match_pool_0484 | jonzpcpp \|\| rjfcnzaht | A | B | no |
| 5 | pair_first_chars_match_pool_0430 | rvwtzhlblq \|\| ryurifngkj | B | A | no |

### Rule 3: 5/5

Articulated rule: Label A if and only if the two strings start with different letters or both start with the same letter and the first string is shorter than the second.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0048 | nepxnfupgnq \|\| cdoea | A | A | yes |
| 2 | pair_first_chars_match_pool_0254 | nhjtyyux \|\| eaykq | A | A | yes |
| 3 | pair_first_chars_match_pool_0414 | zoeokbfpjq \|\| lfvi | A | A | yes |
| 4 | pair_first_chars_match_pool_0008 | bbxt \|\| wohkn | A | A | yes |
| 5 | pair_first_chars_match_pool_0362 | tmkpj \|\| toep | B | B | yes |

### Rule 4: 3/5

Articulated rule: Label B if and only if the two strings start with the same letter.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0377 | giozpwto \|\| sotufnyb | A | B | no |
| 2 | pair_first_chars_match_pool_0297 | wyuyh \|\| wjpmraun | B | B | yes |
| 3 | pair_first_chars_match_pool_0145 | amtvv \|\| xobqnh | A | B | no |
| 4 | pair_first_chars_match_pool_0125 | oqvyc \|\| jrmsx | A | A | yes |
| 5 | pair_first_chars_match_pool_0381 | bnbmcoz \|\| bguvkaeoq | B | B | yes |

### Rule 5: 2/5

Articulated rule: Label A if and only if the second character of the first string is a vowel.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0039 | zewh \|\| zbsu | B | A | no |
| 2 | pair_first_chars_match_pool_0193 | ldahyypur \|\| aynkjdazex | A | B | no |
| 3 | pair_first_chars_match_pool_0010 | beucqd \|\| bdxbdemtjaod | B | A | no |
| 4 | pair_first_chars_match_pool_0157 | uwpa \|\| uxxhshifyn | B | B | yes |
| 5 | pair_first_chars_match_pool_0177 | avyariyvwr \|\| axndxyzpyvc | B | B | yes |

### Rule 6: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0258 | sltcok \|\| vpqcqbcgyzfy | A | A | yes |
| 2 | pair_first_chars_match_pool_0292 | vyzitudhwgwr \|\| uixwsx | A | A | yes |
| 3 | pair_first_chars_match_pool_0361 | yutphnz \|\| fzxmbqxf | A | A | yes |
| 4 | pair_first_chars_match_pool_0411 | hrbjdogepkya \|\| hnoyspgdgts | B | B | yes |
| 5 | pair_first_chars_match_pool_0472 | mirayadnips \|\| udbdzbbtjee | A | A | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0156 | tjgs \|\| xyhxbeten | A | A | yes |
| 2 | pair_first_chars_match_pool_0328 | zesll \|\| qxkdsie | A | A | yes |
| 3 | pair_first_chars_match_pool_0330 | wgpbgrxorz \|\| kmyhrn | A | A | yes |
| 4 | pair_first_chars_match_pool_0436 | apnptttuqdgt \|\| rvshzlvn | A | A | yes |
| 5 | pair_first_chars_match_pool_0369 | voeqqlofw \|\| xkyud | A | A | yes |

### Rule 8: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0412 | yuuv \|\| ymwbsolses | B | B | yes |
| 2 | pair_first_chars_match_pool_0277 | eerkevgjwbf \|\| ekkobiwm | B | B | yes |
| 3 | pair_first_chars_match_pool_0463 | vziml \|\| mollpzl | A | A | yes |
| 4 | pair_first_chars_match_pool_0027 | sbwbgq \|\| wiclgiqsaj | A | A | yes |
| 5 | pair_first_chars_match_pool_0104 | cqvomwjy \|\| aozvomvban | A | A | yes |

### Rule 9: 4/5

Articulated rule: Label A if and only if the two strings contain the same total number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0103 | ujsbowh \|\| btha | A | A | yes |
| 2 | pair_first_chars_match_pool_0122 | glwlplguis \|\| jljepjjeo | A | A | yes |
| 3 | pair_first_chars_match_pool_0063 | llgzcltec \|\| ligd | B | A | no |
| 4 | pair_first_chars_match_pool_0487 | idofrjeybmj \|\| thiq | A | A | yes |
| 5 | pair_first_chars_match_pool_0341 | iymdlcmkszpk \|\| ayun | A | A | yes |

### Rule 10: 2/5

Articulated rule: Label A if and only if the two strings contain the same number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0040 | glqjyvotykz \|\| uifmbro | A | A | yes |
| 2 | pair_first_chars_match_pool_0298 | bklekpyomkl \|\| idvlemm | A | A | yes |
| 3 | pair_first_chars_match_pool_0300 | ldelvzwrn \|\| ldzyglmff | B | A | no |
| 4 | pair_first_chars_match_pool_0177 | avyariyvwr \|\| axndxyzpyvc | B | A | no |
| 5 | pair_first_chars_match_pool_0409 | ixbkhozcu \|\| iodrksgeck | B | A | no |

### Rule 11: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0068 | xoiulbuutrre \|\| jgbsiaermhez | A | A | yes |
| 2 | pair_first_chars_match_pool_0050 | abhedauvy \|\| zvzpysxy | A | A | yes |
| 3 | pair_first_chars_match_pool_0300 | ldelvzwrn \|\| ldzyglmff | B | B | yes |
| 4 | pair_first_chars_match_pool_0209 | ouzigxqpt \|\| orpqujqxgnc | B | B | yes |
| 5 | pair_first_chars_match_pool_0162 | ofxiymasq \|\| ownc | B | B | yes |

### Rule 12: 3/5

Articulated rule: Label A if and only if the two strings contain the same number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0244 | njtossp \|\| nmvkxlt | B | A | no |
| 2 | pair_first_chars_match_pool_0011 | qboxhpdgodo \|\| fcnza | A | A | yes |
| 3 | pair_first_chars_match_pool_0412 | yuuv \|\| ymwbsolses | B | B | yes |
| 4 | pair_first_chars_match_pool_0291 | rdln \|\| rktu | B | A | no |
| 5 | pair_first_chars_match_pool_0482 | hurfezhnmdw \|\| hrfc | B | B | yes |

### Rule 13: 3/5

Articulated rule: Label A if and only if the second character of the first string comes earlier in the alphabet than the second character of the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0087 | vkoqv \|\| fufexmv | A | B | no |
| 2 | pair_first_chars_match_pool_0046 | scdxylpixak \|\| soxgn | B | A | no |
| 3 | pair_first_chars_match_pool_0183 | dmdzocdhbgde \|\| gecyl | A | A | yes |
| 4 | pair_first_chars_match_pool_0023 | ataaut \|\| kkfa | A | A | yes |
| 5 | pair_first_chars_match_pool_0482 | hurfezhnmdw \|\| hrfc | B | B | yes |

### Rule 14: 2/5

Articulated rule: Label A if and only if the two parts start with letters that are consecutive in the alphabet (including the same letter); otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0038 | jzopqtb \|\| jkijnwrpsa | B | A | no |
| 2 | pair_first_chars_match_pool_0238 | ybqppm \|\| yiuyoktt | B | B | yes |
| 3 | pair_first_chars_match_pool_0260 | aqyqzlea \|\| otlnnleuo | A | B | no |
| 4 | pair_first_chars_match_pool_0140 | ufocwxmtkd \|\| fhhdfvt | A | B | no |
| 5 | pair_first_chars_match_pool_0362 | tmkpj \|\| toep | B | B | yes |

### Rule 15: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0388 | kdfylmfqjj \|\| cilxhq | A | A | yes |
| 2 | pair_first_chars_match_pool_0456 | cktkoyplemfc \|\| ypag | A | A | yes |
| 3 | pair_first_chars_match_pool_0297 | wyuyh \|\| wjpmraun | B | B | yes |
| 4 | pair_first_chars_match_pool_0444 | mafeuvcx \|\| mwampxnyrk | B | B | yes |
| 5 | pair_first_chars_match_pool_0151 | xmjmv \|\| tqkau | A | A | yes |

### Rule 16: 4/5

Articulated rule: Label A if and only if the two strings start with different letters or the second letters are the same; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0151 | xmjmv \|\| tqkau | A | A | yes |
| 2 | pair_first_chars_match_pool_0460 | haeua \|\| gjii | A | A | yes |
| 3 | pair_first_chars_match_pool_0343 | amryrqasju \|\| asjtheq | B | A | no |
| 4 | pair_first_chars_match_pool_0377 | giozpwto \|\| sotufnyb | A | A | yes |
| 5 | pair_first_chars_match_pool_0240 | wgfw \|\| wvhmgtwxolfi | B | B | yes |

### Rule 17: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0156 | tjgs \|\| xyhxbeten | A | A | yes |
| 2 | pair_first_chars_match_pool_0186 | gifdsxtzv \|\| ybxauqvnylw | A | A | yes |
| 3 | pair_first_chars_match_pool_0341 | iymdlcmkszpk \|\| ayun | A | A | yes |
| 4 | pair_first_chars_match_pool_0116 | oieczjtcpysg \|\| zdxfljkuay | A | A | yes |
| 5 | pair_first_chars_match_pool_0337 | slvuoqsmcge \|\| qmsncquy | A | A | yes |

### Rule 18: 3/5

Articulated rule: Label A if and only if the two strings contain the same number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0089 | denvpn \|\| ditzgr | B | A | no |
| 2 | pair_first_chars_match_pool_0096 | vrwessoqs \|\| xzhy | A | A | yes |
| 3 | pair_first_chars_match_pool_0154 | kzrpo \|\| kwdn | B | A | no |
| 4 | pair_first_chars_match_pool_0012 | hhpj \|\| hihaplqkccj | B | B | yes |
| 5 | pair_first_chars_match_pool_0374 | oeocrxbvfjjw \|\| juhlgrysa | A | A | yes |

### Rule 19: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0037 | zjts \|\| hyxtjio | A | A | yes |
| 2 | pair_first_chars_match_pool_0387 | ayins \|\| aqrewkw | B | B | yes |
| 3 | pair_first_chars_match_pool_0291 | rdln \|\| rktu | B | B | yes |
| 4 | pair_first_chars_match_pool_0233 | xwwqrvamu \|\| xuerydyp | B | B | yes |
| 5 | pair_first_chars_match_pool_0078 | hrhbzptkk \|\| avrxekjter | A | A | yes |

### Rule 20: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0347 | qxiudqssy \|\| grfuralu | A | A | yes |
| 2 | pair_first_chars_match_pool_0204 | hgsfdyqalh \|\| hirtf | B | B | yes |
| 3 | pair_first_chars_match_pool_0021 | szmu \|\| fusy | A | A | yes |
| 4 | pair_first_chars_match_pool_0269 | gsuauarepkja \|\| gqyp | B | B | yes |
| 5 | pair_first_chars_match_pool_0258 | sltcok \|\| vpqcqbcgyzfy | A | A | yes |

### Rule 21: 3/5

Articulated rule: Label B if and only if the two strings start with the same letter.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0470 | cgxd \|\| adnjtifpf | A | A | yes |
| 2 | pair_first_chars_match_pool_0095 | nfnfo \|\| pnvnktsrupua | A | B | no |
| 3 | pair_first_chars_match_pool_0079 | bdapgtknh \|\| bavxhhpx | B | B | yes |
| 4 | pair_first_chars_match_pool_0484 | jonzpcpp \|\| rjfcnzaht | A | B | no |
| 5 | pair_first_chars_match_pool_0004 | trsiqmkqqw \|\| moux | A | A | yes |

### Rule 22: 2/5

Articulated rule: Label A if and only if the two strings start with letters of the same alphabetic parity (both vowels/consonants is false; rather, both first letters are both in odd positions or both in even positions in the alphabet).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0471 | adyvj \|\| fnapqxmvpvfd | A | B | no |
| 2 | pair_first_chars_match_pool_0168 | onszdb \|\| omjt | B | A | no |
| 3 | pair_first_chars_match_pool_0184 | virk \|\| vlsbx | B | B | yes |
| 4 | pair_first_chars_match_pool_0177 | avyariyvwr \|\| axndxyzpyvc | B | A | no |
| 5 | pair_first_chars_match_pool_0151 | xmjmv \|\| tqkau | A | A | yes |

### Rule 23: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0338 | moloavcfuyb \|\| mfbev | B | B | yes |
| 2 | pair_first_chars_match_pool_0367 | lifpjgby \|\| nmptcbomkwxc | A | A | yes |
| 3 | pair_first_chars_match_pool_0286 | ijtb \|\| dgcgwrrbudkr | A | A | yes |
| 4 | pair_first_chars_match_pool_0003 | txmgka \|\| tbdtqwuundnk | B | B | yes |
| 5 | pair_first_chars_match_pool_0457 | oiqcycfdwd \|\| obwxmdzdd | B | B | yes |

### Rule 24: 4/5

Articulated rule: Label A if and only if the two strings start with different letters or both have even length; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0288 | mvie \|\| mrwao | B | B | yes |
| 2 | pair_first_chars_match_pool_0152 | cqzmyluoujz \|\| rdskmf | A | A | yes |
| 3 | pair_first_chars_match_pool_0365 | ujensm \|\| uhtdhiouezje | B | B | yes |
| 4 | pair_first_chars_match_pool_0058 | lohoalwos \|\| fkmvmphv | A | A | yes |
| 5 | pair_first_chars_match_pool_0149 | gcrmbmw \|\| gsjherdl | B | A | no |

### Rule 25: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0033 | fmcz \|\| fbadlxpkdvo | B | B | yes |
| 2 | pair_first_chars_match_pool_0450 | vhvjosunfmwd \|\| wxwqbv | A | A | yes |
| 3 | pair_first_chars_match_pool_0230 | hhsccyckdp \|\| hxrxxmwifc | B | B | yes |
| 4 | pair_first_chars_match_pool_0309 | haibzwhwbv \|\| hraxlyaa | B | B | yes |
| 5 | pair_first_chars_match_pool_0429 | fsxupbpa \|\| dhvsprbvz | A | A | yes |

### Rule 26: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0105 | fwdzks \|\| ffcwiwynjg | B | B | yes |
| 2 | pair_first_chars_match_pool_0091 | nsdzmrzlvfh \|\| nfecvlsehl | B | B | yes |
| 3 | pair_first_chars_match_pool_0221 | hsdsnqamfo \|\| ogtngcbijk | A | A | yes |
| 4 | pair_first_chars_match_pool_0289 | ljksns \|\| fpvdnxlyno | A | A | yes |
| 5 | pair_first_chars_match_pool_0277 | eerkevgjwbf \|\| ekkobiwm | B | B | yes |

### Rule 27: 4/5

Articulated rule: Label A if and only if the two strings have the same parity of length (both even or both odd).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0068 | xoiulbuutrre \|\| jgbsiaermhez | A | A | yes |
| 2 | pair_first_chars_match_pool_0345 | qyxldii \|\| ookopgucoghy | A | B | no |
| 3 | pair_first_chars_match_pool_0005 | eloivxplswm \|\| xpxzmsddmfz | A | A | yes |
| 4 | pair_first_chars_match_pool_0071 | arhy \|\| wflo | A | A | yes |
| 5 | pair_first_chars_match_pool_0003 | txmgka \|\| tbdtqwuundnk | B | B | yes |

### Rule 28: 2/5

Articulated rule: Label A if and only if the two strings contain the same number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0113 | segels \|\| dryzjo | A | A | yes |
| 2 | pair_first_chars_match_pool_0139 | yotqgip \|\| flhhgxyo | A | A | yes |
| 3 | pair_first_chars_match_pool_0339 | kyhbtvjw \|\| kbnislrcykc | B | A | no |
| 4 | pair_first_chars_match_pool_0073 | pwmjebwzzzli \|\| plnnjinycwn | B | A | no |
| 5 | pair_first_chars_match_pool_0063 | llgzcltec \|\| ligd | B | A | no |

### Rule 29: 3/5

Articulated rule: Label B if and only if the two strings start with the same letter.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0475 | tlghx \|\| uddeus | A | B | no |
| 2 | pair_first_chars_match_pool_0263 | gtugcht \|\| slkveqnps | A | B | no |
| 3 | pair_first_chars_match_pool_0053 | emgs \|\| evkgnqqdrdwp | B | B | yes |
| 4 | pair_first_chars_match_pool_0366 | zdie \|\| zuquu | B | B | yes |
| 5 | pair_first_chars_match_pool_0295 | loypnkucozsd \|\| lmhebcskxdi | B | B | yes |

### Rule 30: 2/5

Articulated rule: Label B if and only if the two strings start with the same letter.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0217 | ohkbqsbuob \|\| nswy | A | B | no |
| 2 | pair_first_chars_match_pool_0139 | yotqgip \|\| flhhgxyo | A | B | no |
| 3 | pair_first_chars_match_pool_0296 | ewatbme \|\| ebgvs | B | B | yes |
| 4 | pair_first_chars_match_pool_0257 | pplmojspup \|\| ezpcrwiu | A | B | no |
| 5 | pair_first_chars_match_pool_0320 | qotcbgjdto \|\| fgynm | A | A | yes |

### Rule 31: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0172 | ygfbkvk \|\| yvtvb | B | B | yes |
| 2 | pair_first_chars_match_pool_0123 | zphm \|\| fukmyedpn | A | A | yes |
| 3 | pair_first_chars_match_pool_0299 | uobuy \|\| uyjqtyno | B | B | yes |
| 4 | pair_first_chars_match_pool_0323 | ubyoljuqe \|\| ujvd | B | B | yes |
| 5 | pair_first_chars_match_pool_0085 | lrqrxwrttzy \|\| lymjauyrnz | B | B | yes |

### Rule 32: 3/5

Articulated rule: Label A if and only if the two strings have the same parity of length (both even or both odd).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0330 | wgpbgrxorz \|\| kmyhrn | A | A | yes |
| 2 | pair_first_chars_match_pool_0300 | ldelvzwrn \|\| ldzyglmff | B | B | yes |
| 3 | pair_first_chars_match_pool_0225 | truvrorp \|\| zaytjjifh | A | B | no |
| 4 | pair_first_chars_match_pool_0265 | jaxtekw \|\| zwhykwxepiqc | A | B | no |
| 5 | pair_first_chars_match_pool_0054 | pgwft \|\| plthwz | B | B | yes |

### Rule 33: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0082 | cataob \|\| cecbijxccc | B | B | yes |
| 2 | pair_first_chars_match_pool_0364 | qxonow \|\| gahyxijzqvk | A | A | yes |
| 3 | pair_first_chars_match_pool_0413 | bxgjrg \|\| bibqlwx | B | B | yes |
| 4 | pair_first_chars_match_pool_0209 | ouzigxqpt \|\| orpqujqxgnc | B | B | yes |
| 5 | pair_first_chars_match_pool_0009 | rylqvdziexn \|\| peampbxdhor | A | A | yes |

### Rule 34: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0440 | pvskolwfgy \|\| jkzrimtqn | A | A | yes |
| 2 | pair_first_chars_match_pool_0282 | iifko \|\| rsldxozlu | A | A | yes |
| 3 | pair_first_chars_match_pool_0211 | nuepeks \|\| ubge | A | A | yes |
| 4 | pair_first_chars_match_pool_0066 | wxyqfyuw \|\| wskqjem | B | B | yes |
| 5 | pair_first_chars_match_pool_0231 | eojmzmxdlne \|\| hhcxjtrei | A | A | yes |

### Rule 35: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0234 | btize \|\| ootenmcfkyw | A | A | yes |
| 2 | pair_first_chars_match_pool_0302 | wzlwep \|\| nibyt | A | A | yes |
| 3 | pair_first_chars_match_pool_0073 | pwmjebwzzzli \|\| plnnjinycwn | B | B | yes |
| 4 | pair_first_chars_match_pool_0417 | rioltiu \|\| wqhz | A | A | yes |
| 5 | pair_first_chars_match_pool_0464 | jpxhxtcbbk \|\| jgbg | B | B | yes |

### Rule 36: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0001 | rfhhwjgw \|\| rdtzapozim | B | B | yes |
| 2 | pair_first_chars_match_pool_0040 | glqjyvotykz \|\| uifmbro | A | A | yes |
| 3 | pair_first_chars_match_pool_0354 | ptwbgfg \|\| iakaw | A | A | yes |
| 4 | pair_first_chars_match_pool_0414 | zoeokbfpjq \|\| lfvi | A | A | yes |
| 5 | pair_first_chars_match_pool_0420 | bczabja \|\| ledx | A | A | yes |

### Rule 37: 1/5

Articulated rule: Label A if and only if the two strings have the same parity of length (both odd or both even).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0497 | wkmytzaxe \|\| wwmuwolpj | B | B | yes |
| 2 | pair_first_chars_match_pool_0000 | bpkj \|\| bobzz | B | A | no |
| 3 | pair_first_chars_match_pool_0110 | cvrtfnmzz \|\| ppvxxz | A | B | no |
| 4 | pair_first_chars_match_pool_0281 | javgspn \|\| mjwubmnqp | A | B | no |
| 5 | pair_first_chars_match_pool_0241 | cnzmpjkphsjo \|\| tzcdmhdumf | A | B | no |

### Rule 38: 1/5

Articulated rule: Label B if and only if the two strings start with the same letter.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0150 | qdll \|\| qeulypuqybg | B | A | no |
| 2 | pair_first_chars_match_pool_0116 | oieczjtcpysg \|\| zdxfljkuay | A | B | no |
| 3 | pair_first_chars_match_pool_0154 | kzrpo \|\| kwdn | B | B | yes |
| 4 | pair_first_chars_match_pool_0070 | ptgsrrd \|\| bbncyorl | A | B | no |
| 5 | pair_first_chars_match_pool_0485 | afdgozzg \|\| azwwejqtnbf | B | A | no |

### Rule 39: 3/5

Articulated rule: Label A if and only if the two strings contain the same total number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0049 | ukud \|\| uvwtjz | B | B | yes |
| 2 | pair_first_chars_match_pool_0261 | upvlsbkxn \|\| jvzesytoalb | A | A | yes |
| 3 | pair_first_chars_match_pool_0384 | ykmupphrusdu \|\| ystkyhas | B | A | no |
| 4 | pair_first_chars_match_pool_0429 | fsxupbpa \|\| dhvsprbvz | A | A | yes |
| 5 | pair_first_chars_match_pool_0311 | tojrwhsjsc \|\| tvzmejadxpc | B | A | no |

### Rule 40: 2/5

Articulated rule: Label A if and only if the second character of the first string comes earlier in the alphabet than the second character of the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0344 | jmve \|\| cyknsvhql | A | B | no |
| 2 | pair_first_chars_match_pool_0327 | exjcogjmxwmq \|\| eoqyjjrrxmat | B | B | yes |
| 3 | pair_first_chars_match_pool_0150 | qdll \|\| qeulypuqybg | B | A | no |
| 4 | pair_first_chars_match_pool_0088 | rkqnbqjy \|\| rwsvx | B | A | no |
| 5 | pair_first_chars_match_pool_0418 | kwcokfmkhogx \|\| kcrby | B | B | yes |

### Rule 41: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0088 | rkqnbqjy \|\| rwsvx | B | B | yes |
| 2 | pair_first_chars_match_pool_0305 | cmyadlsmofsg \|\| cfpwawo | B | B | yes |
| 3 | pair_first_chars_match_pool_0408 | zhnbgmwg \|\| zcqgjr | B | B | yes |
| 4 | pair_first_chars_match_pool_0112 | jhmpx \|\| jllcs | B | B | yes |
| 5 | pair_first_chars_match_pool_0425 | vjpfhm \|\| ntlewrk | A | A | yes |

### Rule 42: 3/5

Articulated rule: Label B if and only if the two strings start with the same letter.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0478 | kekedxl \|\| kcilmd | B | B | yes |
| 2 | pair_first_chars_match_pool_0171 | rxkqpljcfc \|\| qpdiswr | A | A | yes |
| 3 | pair_first_chars_match_pool_0475 | tlghx \|\| uddeus | A | B | no |
| 4 | pair_first_chars_match_pool_0487 | idofrjeybmj \|\| thiq | A | B | no |
| 5 | pair_first_chars_match_pool_0124 | dxcoyi \|\| ufrgvbvw | A | A | yes |

### Rule 43: 5/5

Articulated rule: Label B if and only if the two strings start with the same letter and the second string is shorter than the first.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0005 | eloivxplswm \|\| xpxzmsddmfz | A | A | yes |
| 2 | pair_first_chars_match_pool_0019 | bjnicqt \|\| bbaxe | B | B | yes |
| 3 | pair_first_chars_match_pool_0092 | nwzgqd \|\| nzytl | B | B | yes |
| 4 | pair_first_chars_match_pool_0307 | spraucztr \|\| cupifigfbg | A | A | yes |
| 5 | pair_first_chars_match_pool_0047 | ddldnisppty \|\| wehjljant | A | A | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if the two strings start with letters of opposite vowel/consonant type; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0042 | thqxezow \|\| tbzzlyjohxql | B | B | yes |
| 2 | pair_first_chars_match_pool_0038 | jzopqtb \|\| jkijnwrpsa | B | B | yes |
| 3 | pair_first_chars_match_pool_0098 | ahqpamcrh \|\| ahxm | B | B | yes |
| 4 | pair_first_chars_match_pool_0204 | hgsfdyqalh \|\| hirtf | B | B | yes |
| 5 | pair_first_chars_match_pool_0437 | hfjzdvibjmsx \|\| hgrzgrklds | B | B | yes |

### Rule 45: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0066 | wxyqfyuw \|\| wskqjem | B | B | yes |
| 2 | pair_first_chars_match_pool_0352 | crrerc \|\| pnabecpkz | A | A | yes |
| 3 | pair_first_chars_match_pool_0205 | qugyuaeroh \|\| qiat | B | B | yes |
| 4 | pair_first_chars_match_pool_0415 | oueywp \|\| olciusg | B | B | yes |
| 5 | pair_first_chars_match_pool_0022 | eptsuxeioj \|\| etonw | B | B | yes |

### Rule 46: 5/5

Articulated rule: Label A if and only if the two strings start with different letters after the separator.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0336 | ksuvuzgz \|\| zzxvs | A | A | yes |
| 2 | pair_first_chars_match_pool_0314 | hqzf \|\| rojw | A | A | yes |
| 3 | pair_first_chars_match_pool_0357 | bcnjzl \|\| biaepkhg | B | B | yes |
| 4 | pair_first_chars_match_pool_0184 | virk \|\| vlsbx | B | B | yes |
| 5 | pair_first_chars_match_pool_0392 | obqtzhtke \|\| rccvqmdo | A | A | yes |

### Rule 47: 3/5

Articulated rule: Label A if and only if the two strings start with letters of opposite vowel/consonant type.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0416 | tnqzccxs \|\| tqcnulqq | B | B | yes |
| 2 | pair_first_chars_match_pool_0220 | lvlgzbk \|\| lqwudlisua | B | B | yes |
| 3 | pair_first_chars_match_pool_0450 | vhvjosunfmwd \|\| wxwqbv | A | B | no |
| 4 | pair_first_chars_match_pool_0255 | apjkkcfqumq \|\| lblcpsvxioo | A | B | no |
| 5 | pair_first_chars_match_pool_0114 | rupesbabnf \|\| rmtoiqazm | B | B | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if the two strings start with different letters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0385 | yhmah \|\| hhdofdcvfbp | A | A | yes |
| 2 | pair_first_chars_match_pool_0455 | jsbuecprhcsq \|\| cdpag | A | A | yes |
| 3 | pair_first_chars_match_pool_0179 | lpzrfm \|\| ihhh | A | A | yes |
| 4 | pair_first_chars_match_pool_0171 | rxkqpljcfc \|\| qpdiswr | A | A | yes |
| 5 | pair_first_chars_match_pool_0453 | crovksjhyd \|\| zdenbkxeq | A | A | yes |

### Rule 49: 3/5

Articulated rule: Label A if and only if the two strings contain the same number of vowels.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0189 | ynghge \|\| xhwsfdijafrz | A | B | no |
| 2 | pair_first_chars_match_pool_0498 | shznuwep \|\| saumfg | B | A | no |
| 3 | pair_first_chars_match_pool_0234 | btize \|\| ootenmcfkyw | A | A | yes |
| 4 | pair_first_chars_match_pool_0455 | jsbuecprhcsq \|\| cdpag | A | A | yes |
| 5 | pair_first_chars_match_pool_0365 | ujensm \|\| uhtdhiouezje | B | B | yes |

### Rule 50: 5/5

Articulated rule: Label A if and only if the two strings start with different letters; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0485 | afdgozzg \|\| azwwejqtnbf | B | B | yes |
| 2 | pair_first_chars_match_pool_0237 | vozeyirc \|\| mealsmbmh | A | A | yes |
| 3 | pair_first_chars_match_pool_0287 | ldkeiz \|\| lfko | B | B | yes |
| 4 | pair_first_chars_match_pool_0304 | uarpwocdv \|\| whcccvshv | A | A | yes |
| 5 | pair_first_chars_match_pool_0386 | axbutozapnaf \|\| aptuxwditewf | B | B | yes |

