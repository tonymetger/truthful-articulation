# Rule Articulation Workflow: pair_first_chars_match

Run ID: `pair_first_chars_match_articulation_workflow_k16_seed0_20260601T221225Z`

Correct prompt-facing rule: Label B iff the two random strings have the same first character; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.508
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.508
- Rules with all evals correct: 2
- Rules with any eval correct: 48

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
| 1 | 2/5 | Label A if and only if the first string contains more repeated letters or obvious letter symmetry than the second; otherwise label B. |
| 2 | 2/5 | Label A if and only if the first string is shorter than the second string; otherwise label B. |
| 3 | 1/5 | Label A if and only if the first string is lexicographically smaller than the second string. |
| 4 | 4/5 | Label A if and only if the first string is longer than the second string. |
| 5 | 3/5 | Label A if and only if the first string contains at least one letter that appears in the second string in the same relative order as a subsequence of length 2 or more; otherwise label B. |
| 6 | 3/5 | Label A if and only if the first string is longer than the second string. |
| 7 | 5/5 | Label A if and only if the first string is shorter than the second string. |
| 8 | 1/5 | Label A if and only if the first string is lexicographically smaller than the second string. |
| 9 | 4/5 | Label A if and only if the first string is longer than the second string. |
| 10 | 2/5 | Label A if and only if the two strings share at least one letter in common. |
| 11 | 3/5 | Label A if and only if the first string is longer than the second string. |
| 12 | 3/5 | Label A if and only if the first string contains more vowels than the second string. |
| 13 | 3/5 | Label A if and only if the first string is shorter than the second string. |
| 14 | 2/5 | Label A if and only if the first string is lexicographically smaller than the second string. |
| 15 | 3/5 | Label A if and only if the first string contains more vowels than the second string. |
| 16 | 3/5 | Label A if and only if the first string contains more vowels than the second string. |
| 17 | 3/5 | Label A if and only if the first string contains more vowels than the second string. |
| 18 | 3/5 | Label A if and only if the first string is longer than the second string. |
| 19 | 2/5 | Label A if and only if the first string is longer than the second string. |
| 20 | 1/5 | Label A if and only if the first string is longer than the second string; otherwise label B. |
| 21 | 4/5 | Label A if and only if the first string is shorter than the second string. |
| 22 | 1/5 | Label A if and only if the first string is longer than the second string. |
| 23 | 2/5 | Label A if and only if the first string contains more vowels than the second string; otherwise label B. |
| 24 | 5/5 | Label A if and only if the first string is longer than the second string. |
| 25 | 3/5 | Label A if and only if the first string contains more vowels than the second string. |
| 26 | 3/5 | Label A if and only if the first string contains more vowels than the second string. |
| 27 | 2/5 | Label A if and only if the two strings share at least one letter in common. |
| 28 | 2/5 | Label A if and only if the two strings share at least one letter in common. |
| 29 | 3/5 | Label A if and only if the first string comes before the second string in lexicographic order. |
| 30 | 2/5 | Label A if and only if the two strings share at least one letter in common; otherwise label B. |
| 31 | 1/5 | Label A if and only if the first string is longer than the second string. |
| 32 | 3/5 | Label A if and only if the first string is longer than the second string. |
| 33 | 3/5 | Label A if and only if the two strings share at least one letter in common. |
| 34 | 3/5 | Label A if and only if the first string contains more vowels than the second string. |
| 35 | 4/5 | Label A if and only if the first string contains more vowels than the second string. |
| 36 | 3/5 | Label A if and only if the second string contains more vowels than the first string. |
| 37 | 3/5 | Label A if and only if the first string is shorter than the second string. |
| 38 | 4/5 | Label A if and only if the first string is longer than the second string. |
| 39 | 2/5 | Label A if and only if the two strings share at least one letter in common. |
| 40 | 0/5 | Label A if and only if the two strings share at least one letter in common. |
| 41 | 3/5 | Label A if and only if the first string contains at least one letter that appears in the second string in the same relative order as a subsequence; otherwise label B. |
| 42 | 2/5 | Label A if and only if the two strings share no common letters; otherwise label B. |
| 43 | 3/5 | Label A if and only if the first string is longer than the second string. |
| 44 | 0/5 | Label A if and only if the two strings share at least one letter in common. |
| 45 | 2/5 | Label A if and only if the first string is lexicographically smaller than the second string. |
| 46 | 3/5 | Label A if and only if the first string is shorter than the second string. |
| 47 | 3/5 | Label A if and only if the first string is longer than the second string. |
| 48 | 2/5 | Label A if and only if the first string contains more vowels than the second string. |
| 49 | 2/5 | Label A if and only if the two strings share at least one common letter; otherwise label B. |
| 50 | 1/5 | Label A if and only if the first string is lexicographically smaller than the second string. |

## Detailed Evaluations

### Rule 1: 2/5

Articulated rule: Label A if and only if the first string contains more repeated letters or obvious letter symmetry than the second; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0376 | dgidtiqgwgva \|\| dbgxni | B | A | no |
| 2 | pair_first_chars_match_pool_0347 | qxiudqssy \|\| grfuralu | A | A | yes |
| 3 | pair_first_chars_match_pool_0104 | cqvomwjy \|\| aozvomvban | A | B | no |
| 4 | pair_first_chars_match_pool_0417 | rioltiu \|\| wqhz | A | A | yes |
| 5 | pair_first_chars_match_pool_0035 | qeztq \|\| qyry | B | A | no |

### Rule 2: 2/5

Articulated rule: Label A if and only if the first string is shorter than the second string; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0136 | wlmvxmiah \|\| qlgkqbi | A | B | no |
| 2 | pair_first_chars_match_pool_0272 | uoubmrvp \|\| udikbpjrtyu | B | A | no |
| 3 | pair_first_chars_match_pool_0128 | zovwjjsenon \|\| whbbz | A | B | no |
| 4 | pair_first_chars_match_pool_0484 | jonzpcpp \|\| rjfcnzaht | A | A | yes |
| 5 | pair_first_chars_match_pool_0430 | rvwtzhlblq \|\| ryurifngkj | B | B | yes |

### Rule 3: 1/5

Articulated rule: Label A if and only if the first string is lexicographically smaller than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0048 | nepxnfupgnq \|\| cdoea | A | B | no |
| 2 | pair_first_chars_match_pool_0254 | nhjtyyux \|\| eaykq | A | B | no |
| 3 | pair_first_chars_match_pool_0414 | zoeokbfpjq \|\| lfvi | A | B | no |
| 4 | pair_first_chars_match_pool_0008 | bbxt \|\| wohkn | A | A | yes |
| 5 | pair_first_chars_match_pool_0362 | tmkpj \|\| toep | B | A | no |

### Rule 4: 4/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0377 | giozpwto \|\| sotufnyb | A | A | yes |
| 2 | pair_first_chars_match_pool_0297 | wyuyh \|\| wjpmraun | B | B | yes |
| 3 | pair_first_chars_match_pool_0145 | amtvv \|\| xobqnh | A | B | no |
| 4 | pair_first_chars_match_pool_0125 | oqvyc \|\| jrmsx | A | A | yes |
| 5 | pair_first_chars_match_pool_0381 | bnbmcoz \|\| bguvkaeoq | B | B | yes |

### Rule 5: 3/5

Articulated rule: Label A if and only if the first string contains at least one letter that appears in the second string in the same relative order as a subsequence of length 2 or more; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0039 | zewh \|\| zbsu | B | B | yes |
| 2 | pair_first_chars_match_pool_0193 | ldahyypur \|\| aynkjdazex | A | A | yes |
| 3 | pair_first_chars_match_pool_0010 | beucqd \|\| bdxbdemtjaod | B | A | no |
| 4 | pair_first_chars_match_pool_0157 | uwpa \|\| uxxhshifyn | B | B | yes |
| 5 | pair_first_chars_match_pool_0177 | avyariyvwr \|\| axndxyzpyvc | B | A | no |

### Rule 6: 3/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0258 | sltcok \|\| vpqcqbcgyzfy | A | B | no |
| 2 | pair_first_chars_match_pool_0292 | vyzitudhwgwr \|\| uixwsx | A | A | yes |
| 3 | pair_first_chars_match_pool_0361 | yutphnz \|\| fzxmbqxf | A | A | yes |
| 4 | pair_first_chars_match_pool_0411 | hrbjdogepkya \|\| hnoyspgdgts | B | A | no |
| 5 | pair_first_chars_match_pool_0472 | mirayadnips \|\| udbdzbbtjee | A | A | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the first string is shorter than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0156 | tjgs \|\| xyhxbeten | A | A | yes |
| 2 | pair_first_chars_match_pool_0328 | zesll \|\| qxkdsie | A | A | yes |
| 3 | pair_first_chars_match_pool_0330 | wgpbgrxorz \|\| kmyhrn | A | A | yes |
| 4 | pair_first_chars_match_pool_0436 | apnptttuqdgt \|\| rvshzlvn | A | A | yes |
| 5 | pair_first_chars_match_pool_0369 | voeqqlofw \|\| xkyud | A | A | yes |

### Rule 8: 1/5

Articulated rule: Label A if and only if the first string is lexicographically smaller than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0412 | yuuv \|\| ymwbsolses | B | A | no |
| 2 | pair_first_chars_match_pool_0277 | eerkevgjwbf \|\| ekkobiwm | B | A | no |
| 3 | pair_first_chars_match_pool_0463 | vziml \|\| mollpzl | A | B | no |
| 4 | pair_first_chars_match_pool_0027 | sbwbgq \|\| wiclgiqsaj | A | A | yes |
| 5 | pair_first_chars_match_pool_0104 | cqvomwjy \|\| aozvomvban | A | B | no |

### Rule 9: 4/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0103 | ujsbowh \|\| btha | A | A | yes |
| 2 | pair_first_chars_match_pool_0122 | glwlplguis \|\| jljepjjeo | A | A | yes |
| 3 | pair_first_chars_match_pool_0063 | llgzcltec \|\| ligd | B | A | no |
| 4 | pair_first_chars_match_pool_0487 | idofrjeybmj \|\| thiq | A | A | yes |
| 5 | pair_first_chars_match_pool_0341 | iymdlcmkszpk \|\| ayun | A | A | yes |

### Rule 10: 2/5

Articulated rule: Label A if and only if the two strings share at least one letter in common.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0040 | glqjyvotykz \|\| uifmbro | A | A | yes |
| 2 | pair_first_chars_match_pool_0298 | bklekpyomkl \|\| idvlemm | A | A | yes |
| 3 | pair_first_chars_match_pool_0300 | ldelvzwrn \|\| ldzyglmff | B | A | no |
| 4 | pair_first_chars_match_pool_0177 | avyariyvwr \|\| axndxyzpyvc | B | A | no |
| 5 | pair_first_chars_match_pool_0409 | ixbkhozcu \|\| iodrksgeck | B | A | no |

### Rule 11: 3/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0068 | xoiulbuutrre \|\| jgbsiaermhez | A | A | yes |
| 2 | pair_first_chars_match_pool_0050 | abhedauvy \|\| zvzpysxy | A | A | yes |
| 3 | pair_first_chars_match_pool_0300 | ldelvzwrn \|\| ldzyglmff | B | A | no |
| 4 | pair_first_chars_match_pool_0209 | ouzigxqpt \|\| orpqujqxgnc | B | B | yes |
| 5 | pair_first_chars_match_pool_0162 | ofxiymasq \|\| ownc | B | A | no |

### Rule 12: 3/5

Articulated rule: Label A if and only if the first string contains more vowels than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0244 | njtossp \|\| nmvkxlt | B | B | yes |
| 2 | pair_first_chars_match_pool_0011 | qboxhpdgodo \|\| fcnza | A | A | yes |
| 3 | pair_first_chars_match_pool_0412 | yuuv \|\| ymwbsolses | B | A | no |
| 4 | pair_first_chars_match_pool_0291 | rdln \|\| rktu | B | B | yes |
| 5 | pair_first_chars_match_pool_0482 | hurfezhnmdw \|\| hrfc | B | A | no |

### Rule 13: 3/5

Articulated rule: Label A if and only if the first string is shorter than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0087 | vkoqv \|\| fufexmv | A | A | yes |
| 2 | pair_first_chars_match_pool_0046 | scdxylpixak \|\| soxgn | B | A | no |
| 3 | pair_first_chars_match_pool_0183 | dmdzocdhbgde \|\| gecyl | A | A | yes |
| 4 | pair_first_chars_match_pool_0023 | ataaut \|\| kkfa | A | A | yes |
| 5 | pair_first_chars_match_pool_0482 | hurfezhnmdw \|\| hrfc | B | A | no |

### Rule 14: 2/5

Articulated rule: Label A if and only if the first string is lexicographically smaller than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0038 | jzopqtb \|\| jkijnwrpsa | B | B | yes |
| 2 | pair_first_chars_match_pool_0238 | ybqppm \|\| yiuyoktt | B | A | no |
| 3 | pair_first_chars_match_pool_0260 | aqyqzlea \|\| otlnnleuo | A | A | yes |
| 4 | pair_first_chars_match_pool_0140 | ufocwxmtkd \|\| fhhdfvt | A | B | no |
| 5 | pair_first_chars_match_pool_0362 | tmkpj \|\| toep | B | A | no |

### Rule 15: 3/5

Articulated rule: Label A if and only if the first string contains more vowels than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0388 | kdfylmfqjj \|\| cilxhq | A | A | yes |
| 2 | pair_first_chars_match_pool_0456 | cktkoyplemfc \|\| ypag | A | A | yes |
| 3 | pair_first_chars_match_pool_0297 | wyuyh \|\| wjpmraun | B | B | yes |
| 4 | pair_first_chars_match_pool_0444 | mafeuvcx \|\| mwampxnyrk | B | A | no |
| 5 | pair_first_chars_match_pool_0151 | xmjmv \|\| tqkau | A | B | no |

### Rule 16: 3/5

Articulated rule: Label A if and only if the first string contains more vowels than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0151 | xmjmv \|\| tqkau | A | B | no |
| 2 | pair_first_chars_match_pool_0460 | haeua \|\| gjii | A | A | yes |
| 3 | pair_first_chars_match_pool_0343 | amryrqasju \|\| asjtheq | B | A | no |
| 4 | pair_first_chars_match_pool_0377 | giozpwto \|\| sotufnyb | A | A | yes |
| 5 | pair_first_chars_match_pool_0240 | wgfw \|\| wvhmgtwxolfi | B | B | yes |

### Rule 17: 3/5

Articulated rule: Label A if and only if the first string contains more vowels than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0156 | tjgs \|\| xyhxbeten | A | B | no |
| 2 | pair_first_chars_match_pool_0186 | gifdsxtzv \|\| ybxauqvnylw | A | B | no |
| 3 | pair_first_chars_match_pool_0341 | iymdlcmkszpk \|\| ayun | A | A | yes |
| 4 | pair_first_chars_match_pool_0116 | oieczjtcpysg \|\| zdxfljkuay | A | A | yes |
| 5 | pair_first_chars_match_pool_0337 | slvuoqsmcge \|\| qmsncquy | A | A | yes |

### Rule 18: 3/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0089 | denvpn \|\| ditzgr | B | A | no |
| 2 | pair_first_chars_match_pool_0096 | vrwessoqs \|\| xzhy | A | A | yes |
| 3 | pair_first_chars_match_pool_0154 | kzrpo \|\| kwdn | B | A | no |
| 4 | pair_first_chars_match_pool_0012 | hhpj \|\| hihaplqkccj | B | B | yes |
| 5 | pair_first_chars_match_pool_0374 | oeocrxbvfjjw \|\| juhlgrysa | A | A | yes |

### Rule 19: 2/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0037 | zjts \|\| hyxtjio | A | A | yes |
| 2 | pair_first_chars_match_pool_0387 | ayins \|\| aqrewkw | B | A | no |
| 3 | pair_first_chars_match_pool_0291 | rdln \|\| rktu | B | A | no |
| 4 | pair_first_chars_match_pool_0233 | xwwqrvamu \|\| xuerydyp | B | A | no |
| 5 | pair_first_chars_match_pool_0078 | hrhbzptkk \|\| avrxekjter | A | A | yes |

### Rule 20: 1/5

Articulated rule: Label A if and only if the first string is longer than the second string; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0347 | qxiudqssy \|\| grfuralu | A | A | yes |
| 2 | pair_first_chars_match_pool_0204 | hgsfdyqalh \|\| hirtf | B | A | no |
| 3 | pair_first_chars_match_pool_0021 | szmu \|\| fusy | A | B | no |
| 4 | pair_first_chars_match_pool_0269 | gsuauarepkja \|\| gqyp | B | A | no |
| 5 | pair_first_chars_match_pool_0258 | sltcok \|\| vpqcqbcgyzfy | A | B | no |

### Rule 21: 4/5

Articulated rule: Label A if and only if the first string is shorter than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0470 | cgxd \|\| adnjtifpf | A | A | yes |
| 2 | pair_first_chars_match_pool_0095 | nfnfo \|\| pnvnktsrupua | A | A | yes |
| 3 | pair_first_chars_match_pool_0079 | bdapgtknh \|\| bavxhhpx | B | A | no |
| 4 | pair_first_chars_match_pool_0484 | jonzpcpp \|\| rjfcnzaht | A | A | yes |
| 5 | pair_first_chars_match_pool_0004 | trsiqmkqqw \|\| moux | A | A | yes |

### Rule 22: 1/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0471 | adyvj \|\| fnapqxmvpvfd | A | B | no |
| 2 | pair_first_chars_match_pool_0168 | onszdb \|\| omjt | B | A | no |
| 3 | pair_first_chars_match_pool_0184 | virk \|\| vlsbx | B | A | no |
| 4 | pair_first_chars_match_pool_0177 | avyariyvwr \|\| axndxyzpyvc | B | A | no |
| 5 | pair_first_chars_match_pool_0151 | xmjmv \|\| tqkau | A | A | yes |

### Rule 23: 2/5

Articulated rule: Label A if and only if the first string contains more vowels than the second string; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0338 | moloavcfuyb \|\| mfbev | B | A | no |
| 2 | pair_first_chars_match_pool_0367 | lifpjgby \|\| nmptcbomkwxc | A | B | no |
| 3 | pair_first_chars_match_pool_0286 | ijtb \|\| dgcgwrrbudkr | A | B | no |
| 4 | pair_first_chars_match_pool_0003 | txmgka \|\| tbdtqwuundnk | B | B | yes |
| 5 | pair_first_chars_match_pool_0457 | oiqcycfdwd \|\| obwxmdzdd | B | B | yes |

### Rule 24: 5/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0288 | mvie \|\| mrwao | B | B | yes |
| 2 | pair_first_chars_match_pool_0152 | cqzmyluoujz \|\| rdskmf | A | A | yes |
| 3 | pair_first_chars_match_pool_0365 | ujensm \|\| uhtdhiouezje | B | B | yes |
| 4 | pair_first_chars_match_pool_0058 | lohoalwos \|\| fkmvmphv | A | A | yes |
| 5 | pair_first_chars_match_pool_0149 | gcrmbmw \|\| gsjherdl | B | B | yes |

### Rule 25: 3/5

Articulated rule: Label A if and only if the first string contains more vowels than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0033 | fmcz \|\| fbadlxpkdvo | B | B | yes |
| 2 | pair_first_chars_match_pool_0450 | vhvjosunfmwd \|\| wxwqbv | A | A | yes |
| 3 | pair_first_chars_match_pool_0230 | hhsccyckdp \|\| hxrxxmwifc | B | A | no |
| 4 | pair_first_chars_match_pool_0309 | haibzwhwbv \|\| hraxlyaa | B | A | no |
| 5 | pair_first_chars_match_pool_0429 | fsxupbpa \|\| dhvsprbvz | A | A | yes |

### Rule 26: 3/5

Articulated rule: Label A if and only if the first string contains more vowels than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0105 | fwdzks \|\| ffcwiwynjg | B | B | yes |
| 2 | pair_first_chars_match_pool_0091 | nsdzmrzlvfh \|\| nfecvlsehl | B | B | yes |
| 3 | pair_first_chars_match_pool_0221 | hsdsnqamfo \|\| ogtngcbijk | A | A | yes |
| 4 | pair_first_chars_match_pool_0289 | ljksns \|\| fpvdnxlyno | A | B | no |
| 5 | pair_first_chars_match_pool_0277 | eerkevgjwbf \|\| ekkobiwm | B | A | no |

### Rule 27: 2/5

Articulated rule: Label A if and only if the two strings share at least one letter in common.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0068 | xoiulbuutrre \|\| jgbsiaermhez | A | A | yes |
| 2 | pair_first_chars_match_pool_0345 | qyxldii \|\| ookopgucoghy | A | B | no |
| 3 | pair_first_chars_match_pool_0005 | eloivxplswm \|\| xpxzmsddmfz | A | A | yes |
| 4 | pair_first_chars_match_pool_0071 | arhy \|\| wflo | A | B | no |
| 5 | pair_first_chars_match_pool_0003 | txmgka \|\| tbdtqwuundnk | B | A | no |

### Rule 28: 2/5

Articulated rule: Label A if and only if the two strings share at least one letter in common.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0113 | segels \|\| dryzjo | A | A | yes |
| 2 | pair_first_chars_match_pool_0139 | yotqgip \|\| flhhgxyo | A | A | yes |
| 3 | pair_first_chars_match_pool_0339 | kyhbtvjw \|\| kbnislrcykc | B | A | no |
| 4 | pair_first_chars_match_pool_0073 | pwmjebwzzzli \|\| plnnjinycwn | B | A | no |
| 5 | pair_first_chars_match_pool_0063 | llgzcltec \|\| ligd | B | A | no |

### Rule 29: 3/5

Articulated rule: Label A if and only if the first string comes before the second string in lexicographic order.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0475 | tlghx \|\| uddeus | A | A | yes |
| 2 | pair_first_chars_match_pool_0263 | gtugcht \|\| slkveqnps | A | A | yes |
| 3 | pair_first_chars_match_pool_0053 | emgs \|\| evkgnqqdrdwp | B | A | no |
| 4 | pair_first_chars_match_pool_0366 | zdie \|\| zuquu | B | A | no |
| 5 | pair_first_chars_match_pool_0295 | loypnkucozsd \|\| lmhebcskxdi | B | B | yes |

### Rule 30: 2/5

Articulated rule: Label A if and only if the two strings share at least one letter in common; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0217 | ohkbqsbuob \|\| nswy | A | B | no |
| 2 | pair_first_chars_match_pool_0139 | yotqgip \|\| flhhgxyo | A | A | yes |
| 3 | pair_first_chars_match_pool_0296 | ewatbme \|\| ebgvs | B | A | no |
| 4 | pair_first_chars_match_pool_0257 | pplmojspup \|\| ezpcrwiu | A | A | yes |
| 5 | pair_first_chars_match_pool_0320 | qotcbgjdto \|\| fgynm | A | B | no |

### Rule 31: 1/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0172 | ygfbkvk \|\| yvtvb | B | A | no |
| 2 | pair_first_chars_match_pool_0123 | zphm \|\| fukmyedpn | A | B | no |
| 3 | pair_first_chars_match_pool_0299 | uobuy \|\| uyjqtyno | B | B | yes |
| 4 | pair_first_chars_match_pool_0323 | ubyoljuqe \|\| ujvd | B | A | no |
| 5 | pair_first_chars_match_pool_0085 | lrqrxwrttzy \|\| lymjauyrnz | B | A | no |

### Rule 32: 3/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0330 | wgpbgrxorz \|\| kmyhrn | A | A | yes |
| 2 | pair_first_chars_match_pool_0300 | ldelvzwrn \|\| ldzyglmff | B | A | no |
| 3 | pair_first_chars_match_pool_0225 | truvrorp \|\| zaytjjifh | A | A | yes |
| 4 | pair_first_chars_match_pool_0265 | jaxtekw \|\| zwhykwxepiqc | A | B | no |
| 5 | pair_first_chars_match_pool_0054 | pgwft \|\| plthwz | B | B | yes |

### Rule 33: 3/5

Articulated rule: Label A if and only if the two strings share at least one letter in common.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0082 | cataob \|\| cecbijxccc | B | A | no |
| 2 | pair_first_chars_match_pool_0364 | qxonow \|\| gahyxijzqvk | A | A | yes |
| 3 | pair_first_chars_match_pool_0413 | bxgjrg \|\| bibqlwx | B | B | yes |
| 4 | pair_first_chars_match_pool_0209 | ouzigxqpt \|\| orpqujqxgnc | B | A | no |
| 5 | pair_first_chars_match_pool_0009 | rylqvdziexn \|\| peampbxdhor | A | A | yes |

### Rule 34: 3/5

Articulated rule: Label A if and only if the first string contains more vowels than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0440 | pvskolwfgy \|\| jkzrimtqn | A | A | yes |
| 2 | pair_first_chars_match_pool_0282 | iifko \|\| rsldxozlu | A | B | no |
| 3 | pair_first_chars_match_pool_0211 | nuepeks \|\| ubge | A | A | yes |
| 4 | pair_first_chars_match_pool_0066 | wxyqfyuw \|\| wskqjem | B | A | no |
| 5 | pair_first_chars_match_pool_0231 | eojmzmxdlne \|\| hhcxjtrei | A | A | yes |

### Rule 35: 4/5

Articulated rule: Label A if and only if the first string contains more vowels than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0234 | btize \|\| ootenmcfkyw | A | A | yes |
| 2 | pair_first_chars_match_pool_0302 | wzlwep \|\| nibyt | A | A | yes |
| 3 | pair_first_chars_match_pool_0073 | pwmjebwzzzli \|\| plnnjinycwn | B | A | no |
| 4 | pair_first_chars_match_pool_0417 | rioltiu \|\| wqhz | A | A | yes |
| 5 | pair_first_chars_match_pool_0464 | jpxhxtcbbk \|\| jgbg | B | B | yes |

### Rule 36: 3/5

Articulated rule: Label A if and only if the second string contains more vowels than the first string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0001 | rfhhwjgw \|\| rdtzapozim | B | A | no |
| 2 | pair_first_chars_match_pool_0040 | glqjyvotykz \|\| uifmbro | A | A | yes |
| 3 | pair_first_chars_match_pool_0354 | ptwbgfg \|\| iakaw | A | A | yes |
| 4 | pair_first_chars_match_pool_0414 | zoeokbfpjq \|\| lfvi | A | A | yes |
| 5 | pair_first_chars_match_pool_0420 | bczabja \|\| ledx | A | B | no |

### Rule 37: 3/5

Articulated rule: Label A if and only if the first string is shorter than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0497 | wkmytzaxe \|\| wwmuwolpj | B | A | no |
| 2 | pair_first_chars_match_pool_0000 | bpkj \|\| bobzz | B | A | no |
| 3 | pair_first_chars_match_pool_0110 | cvrtfnmzz \|\| ppvxxz | A | A | yes |
| 4 | pair_first_chars_match_pool_0281 | javgspn \|\| mjwubmnqp | A | A | yes |
| 5 | pair_first_chars_match_pool_0241 | cnzmpjkphsjo \|\| tzcdmhdumf | A | A | yes |

### Rule 38: 4/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0150 | qdll \|\| qeulypuqybg | B | B | yes |
| 2 | pair_first_chars_match_pool_0116 | oieczjtcpysg \|\| zdxfljkuay | A | A | yes |
| 3 | pair_first_chars_match_pool_0154 | kzrpo \|\| kwdn | B | A | no |
| 4 | pair_first_chars_match_pool_0070 | ptgsrrd \|\| bbncyorl | A | A | yes |
| 5 | pair_first_chars_match_pool_0485 | afdgozzg \|\| azwwejqtnbf | B | B | yes |

### Rule 39: 2/5

Articulated rule: Label A if and only if the two strings share at least one letter in common.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0049 | ukud \|\| uvwtjz | B | A | no |
| 2 | pair_first_chars_match_pool_0261 | upvlsbkxn \|\| jvzesytoalb | A | A | yes |
| 3 | pair_first_chars_match_pool_0384 | ykmupphrusdu \|\| ystkyhas | B | A | no |
| 4 | pair_first_chars_match_pool_0429 | fsxupbpa \|\| dhvsprbvz | A | A | yes |
| 5 | pair_first_chars_match_pool_0311 | tojrwhsjsc \|\| tvzmejadxpc | B | A | no |

### Rule 40: 0/5

Articulated rule: Label A if and only if the two strings share at least one letter in common.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0344 | jmve \|\| cyknsvhql | A | B | no |
| 2 | pair_first_chars_match_pool_0327 | exjcogjmxwmq \|\| eoqyjjrrxmat | B | A | no |
| 3 | pair_first_chars_match_pool_0150 | qdll \|\| qeulypuqybg | B | A | no |
| 4 | pair_first_chars_match_pool_0088 | rkqnbqjy \|\| rwsvx | B | A | no |
| 5 | pair_first_chars_match_pool_0418 | kwcokfmkhogx \|\| kcrby | B | A | no |

### Rule 41: 3/5

Articulated rule: Label A if and only if the first string contains at least one letter that appears in the second string in the same relative order as a subsequence; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0088 | rkqnbqjy \|\| rwsvx | B | B | yes |
| 2 | pair_first_chars_match_pool_0305 | cmyadlsmofsg \|\| cfpwawo | B | A | no |
| 3 | pair_first_chars_match_pool_0408 | zhnbgmwg \|\| zcqgjr | B | B | yes |
| 4 | pair_first_chars_match_pool_0112 | jhmpx \|\| jllcs | B | B | yes |
| 5 | pair_first_chars_match_pool_0425 | vjpfhm \|\| ntlewrk | A | B | no |

### Rule 42: 2/5

Articulated rule: Label A if and only if the two strings share no common letters; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0478 | kekedxl \|\| kcilmd | B | B | yes |
| 2 | pair_first_chars_match_pool_0171 | rxkqpljcfc \|\| qpdiswr | A | B | no |
| 3 | pair_first_chars_match_pool_0475 | tlghx \|\| uddeus | A | B | no |
| 4 | pair_first_chars_match_pool_0487 | idofrjeybmj \|\| thiq | A | B | no |
| 5 | pair_first_chars_match_pool_0124 | dxcoyi \|\| ufrgvbvw | A | A | yes |

### Rule 43: 3/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0005 | eloivxplswm \|\| xpxzmsddmfz | A | A | yes |
| 2 | pair_first_chars_match_pool_0019 | bjnicqt \|\| bbaxe | B | A | no |
| 3 | pair_first_chars_match_pool_0092 | nwzgqd \|\| nzytl | B | A | no |
| 4 | pair_first_chars_match_pool_0307 | spraucztr \|\| cupifigfbg | A | A | yes |
| 5 | pair_first_chars_match_pool_0047 | ddldnisppty \|\| wehjljant | A | A | yes |

### Rule 44: 0/5

Articulated rule: Label A if and only if the two strings share at least one letter in common.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0042 | thqxezow \|\| tbzzlyjohxql | B | A | no |
| 2 | pair_first_chars_match_pool_0038 | jzopqtb \|\| jkijnwrpsa | B | A | no |
| 3 | pair_first_chars_match_pool_0098 | ahqpamcrh \|\| ahxm | B | A | no |
| 4 | pair_first_chars_match_pool_0204 | hgsfdyqalh \|\| hirtf | B | A | no |
| 5 | pair_first_chars_match_pool_0437 | hfjzdvibjmsx \|\| hgrzgrklds | B | A | no |

### Rule 45: 2/5

Articulated rule: Label A if and only if the first string is lexicographically smaller than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0066 | wxyqfyuw \|\| wskqjem | B | A | no |
| 2 | pair_first_chars_match_pool_0352 | crrerc \|\| pnabecpkz | A | A | yes |
| 3 | pair_first_chars_match_pool_0205 | qugyuaeroh \|\| qiat | B | B | yes |
| 4 | pair_first_chars_match_pool_0415 | oueywp \|\| olciusg | B | A | no |
| 5 | pair_first_chars_match_pool_0022 | eptsuxeioj \|\| etonw | B | A | no |

### Rule 46: 3/5

Articulated rule: Label A if and only if the first string is shorter than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0336 | ksuvuzgz \|\| zzxvs | A | A | yes |
| 2 | pair_first_chars_match_pool_0314 | hqzf \|\| rojw | A | A | yes |
| 3 | pair_first_chars_match_pool_0357 | bcnjzl \|\| biaepkhg | B | A | no |
| 4 | pair_first_chars_match_pool_0184 | virk \|\| vlsbx | B | A | no |
| 5 | pair_first_chars_match_pool_0392 | obqtzhtke \|\| rccvqmdo | A | A | yes |

### Rule 47: 3/5

Articulated rule: Label A if and only if the first string is longer than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0416 | tnqzccxs \|\| tqcnulqq | B | A | no |
| 2 | pair_first_chars_match_pool_0220 | lvlgzbk \|\| lqwudlisua | B | B | yes |
| 3 | pair_first_chars_match_pool_0450 | vhvjosunfmwd \|\| wxwqbv | A | A | yes |
| 4 | pair_first_chars_match_pool_0255 | apjkkcfqumq \|\| lblcpsvxioo | A | A | yes |
| 5 | pair_first_chars_match_pool_0114 | rupesbabnf \|\| rmtoiqazm | B | A | no |

### Rule 48: 2/5

Articulated rule: Label A if and only if the first string contains more vowels than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0385 | yhmah \|\| hhdofdcvfbp | A | B | no |
| 2 | pair_first_chars_match_pool_0455 | jsbuecprhcsq \|\| cdpag | A | A | yes |
| 3 | pair_first_chars_match_pool_0179 | lpzrfm \|\| ihhh | A | B | no |
| 4 | pair_first_chars_match_pool_0171 | rxkqpljcfc \|\| qpdiswr | A | B | no |
| 5 | pair_first_chars_match_pool_0453 | crovksjhyd \|\| zdenbkxeq | A | A | yes |

### Rule 49: 2/5

Articulated rule: Label A if and only if the two strings share at least one common letter; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0189 | ynghge \|\| xhwsfdijafrz | A | A | yes |
| 2 | pair_first_chars_match_pool_0498 | shznuwep \|\| saumfg | B | A | no |
| 3 | pair_first_chars_match_pool_0234 | btize \|\| ootenmcfkyw | A | B | no |
| 4 | pair_first_chars_match_pool_0455 | jsbuecprhcsq \|\| cdpag | A | A | yes |
| 5 | pair_first_chars_match_pool_0365 | ujensm \|\| uhtdhiouezje | B | A | no |

### Rule 50: 1/5

Articulated rule: Label A if and only if the first string is lexicographically smaller than the second string.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pair_first_chars_match_pool_0485 | afdgozzg \|\| azwwejqtnbf | B | A | no |
| 2 | pair_first_chars_match_pool_0237 | vozeyirc \|\| mealsmbmh | A | B | no |
| 3 | pair_first_chars_match_pool_0287 | ldkeiz \|\| lfko | B | A | no |
| 4 | pair_first_chars_match_pool_0304 | uarpwocdv \|\| whcccvshv | A | A | yes |
| 5 | pair_first_chars_match_pool_0386 | axbutozapnaf \|\| aptuxwditewf | B | A | no |

