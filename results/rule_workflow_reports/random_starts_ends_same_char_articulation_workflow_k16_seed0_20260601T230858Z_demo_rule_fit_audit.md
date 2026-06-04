# Demo-Fit Audit: random_starts_ends_same_char

Source JSONL: `results/raw_model_outputs/random_starts_ends_same_char_articulation_workflow_k16_seed0_20260601T230858Z.jsonl`

Prompt-facing labels in this run were swapped: `Label B` iff the first and last character are the same; `Label A` otherwise.

This audit asks whether each model-articulated alternative rule would have classified the 16 labeled examples shown in the articulation prompt. For all rules in this run, the model stated a `Label A iff ...` rule, so the predicate below predicts `A` when true and `B` otherwise.

Vowels are interpreted as `a,e,i,o,u`; all other lowercase letters, including `y`, are consonants. For rules such as "more vowels than the letter y", I interpreted this as `vowel_count > count(y)`.

## Summary

- Audited rules: 50
- Rules whose articulated rule perfectly fit all 16 prompt examples: 0/50
- Perfect-fitting rule indices: none
- Rules fitting at least 14/16 prompt examples: 1/50
- At-least-14/16 rule indices: [49]
- Mean fit on the 16 prompt examples: 8.60/16 = 53.8%
- Intended starts/ends-same rule fit: 16/16 for every prompt, as expected from the data labels.

### Fit Histogram

| Prompt-example fit | Number of articulated rules |
|---:|---:|
| 4/16 | 2 |
| 5/16 | 1 |
| 6/16 | 1 |
| 7/16 | 5 |
| 8/16 | 20 |
| 9/16 | 11 |
| 10/16 | 1 |
| 11/16 | 5 |
| 12/16 | 1 |
| 13/16 | 2 |
| 14/16 | 1 |

### Predicate Families

| Interpreted predicate | Count |
|---|---:|
| `consonants > vowels` | 19 |
| `vowels odd` | 9 |
| `vowels even` | 5 |
| `vowels > consonants` | 4 |
| `vowels > count_y` | 2 |
| `a_m_consonants > n_z_consonants` | 2 |
| `vowels >= 3` | 2 |
| `b_m_consonants > n_z_consonants` | 1 |
| `vowels >= 2` | 1 |
| `vowels > count_v` | 1 |
| `consonants even` | 1 |
| `vowels > count_w` | 1 |
| `vowels > count_m` | 1 |
| `any vowel occurs exactly once` | 1 |

## Rule-by-Rule Results

| Rule | Prompt fit | Eval fit | Interpreted predicate | Articulated rule |
|---:|---:|---:|---|---|
| 1 | 8/16 | 2/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 2 | 11/16 | 4/5 | `vowels > count_y` | Label A if and only if the string contains more vowels than the letter y. |
| 3 | 12/16 | 3/5 | `vowels odd` | Label A if and only if the input contains an odd number of vowels. |
| 4 | 9/16 | 3/5 | `a_m_consonants > n_z_consonants` | Label A if and only if the string contains more consonants from the first half of the alphabet (a–m) than from the second half (n–z). |
| 5 | 9/16 | 4/5 | `vowels odd` | Label A if and only if the string contains an odd number of vowels. |
| 6 | 6/16 | 3/5 | `vowels even` | Label A if and only if the input contains an even number of vowels. |
| 7 | 9/16 | 3/5 | `vowels odd` | Label A if and only if the string contains an odd number of vowels. |
| 8 | 9/16 | 2/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 9 | 7/16 | 2/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 10 | 8/16 | 3/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 11 | 9/16 | 2/5 | `consonants > vowels` | Label A if and only if the input contains more consonants than vowels. |
| 12 | 8/16 | 3/5 | `vowels > consonants` | Label A if and only if the input contains more vowels than consonants. |
| 13 | 4/16 | 2/5 | `vowels odd` | Label A if and only if the string contains an odd number of vowels. |
| 14 | 8/16 | 3/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 15 | 8/16 | 3/5 | `vowels even` | Label A if and only if the string contains an even number of vowels. |
| 16 | 8/16 | 2/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 17 | 11/16 | 1/5 | `b_m_consonants > n_z_consonants` | Label A if and only if the string contains more consonants from the first half of the alphabet (b–m) than from the second half (n–z). |
| 18 | 13/16 | 2/5 | `vowels odd` | Label A if and only if the string contains an odd number of vowels. |
| 19 | 8/16 | 3/5 | `vowels odd` | Label A if and only if the string contains an odd number of vowels. |
| 20 | 8/16 | 4/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 21 | 10/16 | 2/5 | `vowels odd` | Label A if and only if the string contains an odd number of vowels. |
| 22 | 8/16 | 2/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 23 | 8/16 | 1/5 | `vowels odd` | Label A if and only if the input contains an odd number of vowels. |
| 24 | 8/16 | 1/5 | `vowels >= 2` | Label A if and only if the input contains more vowels than the label-B examples do, namely at least two vowels. |
| 25 | 7/16 | 4/5 | `consonants > vowels` | Label A if and only if the input contains more consonants than vowels. |
| 26 | 9/16 | 3/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 27 | 7/16 | 5/5 | `vowels > consonants` | Label A if and only if the input contains more vowels than consonants. |
| 28 | 8/16 | 3/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 29 | 8/16 | 2/5 | `vowels > count_v` | Label A if and only if the string contains more vowels than the letter "v". |
| 30 | 7/16 | 2/5 | `consonants even` | Label A if and only if the string contains an even number of consonants. |
| 31 | 11/16 | 0/5 | `vowels even` | Label A if and only if the string contains an even number of vowels. |
| 32 | 5/16 | 4/5 | `vowels even` | Label A if and only if the string contains an even number of vowels. |
| 33 | 9/16 | 5/5 | `consonants > vowels` | Label A if and only if the input contains more consonants than vowels. |
| 34 | 8/16 | 3/5 | `vowels odd` | Label A if and only if the input contains an odd number of vowels. |
| 35 | 4/16 | 3/5 | `vowels even` | Label A if and only if the string contains an even number of vowels. |
| 36 | 9/16 | 4/5 | `a_m_consonants > n_z_consonants` | Label A if and only if the string contains more consonants from the first half of the alphabet (a–m) than from the second half (n–z). |
| 37 | 13/16 | 1/5 | `vowels > count_w` | Label A if and only if the input contains more vowels than the letter "w". |
| 38 | 7/16 | 3/5 | `vowels > consonants` | Label A if and only if the string contains more vowels than consonants. |
| 39 | 8/16 | 2/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 40 | 9/16 | 0/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 41 | 9/16 | 2/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 42 | 9/16 | 4/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 43 | 8/16 | 3/5 | `vowels >= 3` | Label A if and only if the string contains more vowels than the string labeled B examples typically do—specifically, at least 3 vowels. |
| 44 | 8/16 | 3/5 | `consonants > vowels` | Label A if and only if the string contains more consonants than vowels. |
| 45 | 8/16 | 3/5 | `vowels > count_y` | Label A if and only if the input contains more vowels than the letter y. |
| 46 | 11/16 | 2/5 | `vowels > count_m` | Label A if and only if the input contains more vowels than the letter m. |
| 47 | 11/16 | 2/5 | `vowels >= 3` | Label A if and only if the string contains more vowels than the string labeled B examples do—specifically, at least 3 vowels. |
| 48 | 8/16 | 2/5 | `consonants > vowels` | Label A if and only if the input contains more consonants than vowels. |
| 49 | 14/16 | 2/5 | `any vowel occurs exactly once` | Label A if and only if the string contains at least one of the vowels a, e, i, o, or u exactly once. |
| 50 | 8/16 | 3/5 | `vowels > consonants` | Label A if and only if the string contains more vowels than consonants. |

## First Rule Detailed Check

Rule 1 articulated rule: Label A if and only if the string contains more consonants than vowels.

Interpreted predicate: `consonants > vowels`. It fits 8/16 prompt examples, so it does **not** explain the labeled examples the model saw.

| Input | True label | Rule label | Vowels | Consonants | First=Last |
|---|:---:|:---:|---:|---:|:---:|
| `jmspvoty` | A | A | 1 | 7 | no |
| `volhtsbd` | A | A | 1 | 7 | no |
| `zzkdz` | B | A | 0 | 5 | yes |
| `jnndveeaj` | B | A | 3 | 6 | yes |
| `tyjdkx` | A | A | 0 | 6 | no |
| `bmadb` | B | A | 1 | 4 | yes |
| `gqgizcgtwzwq` | A | A | 1 | 11 | no |
| `jrukfj` | B | A | 1 | 5 | yes |
| `catgc` | B | A | 1 | 4 | yes |
| `wetyvemgw` | B | A | 2 | 7 | yes |
| `otlhedjpqvwb` | A | A | 2 | 10 | no |
| `pjsfezp` | B | A | 1 | 6 | yes |
| `qxweckhq` | B | A | 1 | 7 | yes |
| `ejzix` | A | A | 2 | 3 | no |
| `atbmebgvsmgq` | A | A | 2 | 10 | no |
| `vlenggf` | A | A | 1 | 6 | no |

## Mismatch Details

The rows below list the prompt examples that the articulated rule would misclassify.

### Rule 1: 8/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `zzkdz` | B | A | 0 | 5 | z | z |
| `jnndveeaj` | B | A | 3 | 6 | j | j |
| `bmadb` | B | A | 1 | 4 | b | b |
| `jrukfj` | B | A | 1 | 5 | j | j |
| `catgc` | B | A | 1 | 4 | c | c |
| `wetyvemgw` | B | A | 2 | 7 | w | w |
| `pjsfezp` | B | A | 1 | 6 | p | p |
| `qxweckhq` | B | A | 1 | 7 | q | q |

### Rule 2: 11/16

Articulated rule: Label A if and only if the string contains more vowels than the letter y.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `tbhufauqvnvt` | B | A | 3 | 9 | t | t |
| `csqkhohlc` | B | A | 1 | 8 | c | c |
| `vihuywfilquv` | B | A | 4 | 8 | v | v |
| `aqcvcva` | B | A | 2 | 5 | a | a |
| `jayokj` | B | A | 2 | 4 | j | j |

### Rule 3: 12/16

Articulated rule: Label A if and only if the input contains an odd number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `ouarfeyzvns` | A | B | 4 | 7 | o | s |
| `szsmrwd` | A | B | 0 | 7 | s | d |
| `rwtzd` | A | B | 0 | 5 | r | d |
| `ydemicrswjq` | A | B | 2 | 9 | y | q |

### Rule 4: 9/16

Articulated rule: Label A if and only if the string contains more consonants from the first half of the alphabet (a–m) than from the second half (n–z).

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `kzmudrbek` | B | A | 2 | 7 | k | k |
| `yxgjtrsb` | A | B | 0 | 8 | y | b |
| `ahsalyz` | A | B | 2 | 5 | a | z |
| `dmdnepssk` | A | B | 1 | 8 | d | k |
| `catgc` | B | A | 1 | 4 | c | c |
| `jayokj` | B | A | 2 | 4 | j | j |
| `hdtmncrgqgh` | B | A | 0 | 11 | h | h |

### Rule 5: 9/16

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `gqwyhsst` | A | B | 0 | 8 | g | t |
| `cnbolttc` | B | A | 1 | 7 | c | c |
| `rbmrlualz` | A | B | 2 | 7 | r | z |
| `esqztoqdmmjl` | A | B | 2 | 10 | e | l |
| `tedgt` | B | A | 1 | 4 | t | t |
| `umcwyptuksl` | A | B | 2 | 9 | u | l |
| `tlsokmqt` | B | A | 1 | 7 | t | t |

### Rule 6: 6/16

Articulated rule: Label A if and only if the input contains an even number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `esvfxhqyje` | B | A | 2 | 8 | e | e |
| `gxzg` | B | A | 0 | 4 | g | g |
| `kzjmbgk` | B | A | 0 | 7 | k | k |
| `bnnrwawg` | A | B | 1 | 7 | b | g |
| `kmnlhelmn` | A | B | 1 | 8 | k | n |
| `fatrilxgmf` | B | A | 2 | 8 | f | f |
| `qukwqg` | A | B | 1 | 5 | q | g |
| `hzuiyjcleoh` | B | A | 4 | 7 | h | h |
| `akrpdvvzry` | A | B | 1 | 9 | a | y |
| `cemoim` | A | B | 3 | 3 | c | m |

### Rule 7: 9/16

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `jocj` | B | A | 1 | 3 | j | j |
| `qowi` | A | B | 2 | 2 | q | i |
| `ystqgijffsy` | B | A | 1 | 10 | y | y |
| `eghu` | A | B | 2 | 2 | e | u |
| `bmvkfk` | A | B | 0 | 6 | b | k |
| `rzzau` | A | B | 2 | 3 | r | u |
| `bmadb` | B | A | 1 | 4 | b | b |

### Rule 8: 9/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `dvdpxjxzjjmd` | B | A | 0 | 12 | d | d |
| `emowrglwbe` | B | A | 3 | 7 | e | e |
| `xgbybqzcwx` | B | A | 0 | 10 | x | x |
| `uffrfphcwqiu` | B | A | 3 | 9 | u | u |
| `vnqpv` | B | A | 0 | 5 | v | v |
| `bxwtb` | B | A | 0 | 5 | b | b |
| `nzeayqen` | B | A | 3 | 5 | n | n |

### Rule 9: 7/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `hzuiyjcleoh` | B | A | 4 | 7 | h | h |
| `miinyylm` | B | A | 2 | 6 | m | m |
| `uuodlvoun` | A | B | 5 | 4 | u | n |
| `arqklsa` | B | A | 2 | 5 | a | a |
| `tedgt` | B | A | 1 | 4 | t | t |
| `mybtiaslm` | B | A | 2 | 7 | m | m |
| `jlnj` | B | A | 0 | 4 | j | j |
| `keirvyyack` | B | A | 3 | 7 | k | k |
| `yeabty` | B | A | 2 | 4 | y | y |

### Rule 10: 8/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `dvcqisjlvxd` | B | A | 1 | 10 | d | d |
| `zezz` | B | A | 1 | 3 | z | z |
| `akxkui` | A | B | 3 | 3 | a | i |
| `gvsg` | B | A | 0 | 4 | g | g |
| `xumytavgtxpx` | B | A | 2 | 10 | x | x |
| `qprtq` | B | A | 0 | 5 | q | q |
| `kzjmbgk` | B | A | 0 | 7 | k | k |
| `clhic` | B | A | 1 | 4 | c | c |

### Rule 11: 9/16

Articulated rule: Label A if and only if the input contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `xhxmovinlx` | B | A | 2 | 8 | x | x |
| `wiwqio` | A | B | 3 | 3 | w | o |
| `eghu` | A | B | 2 | 2 | e | u |
| `zgwubgogqvz` | B | A | 2 | 9 | z | z |
| `drkd` | B | A | 0 | 4 | d | d |
| `mltseum` | B | A | 2 | 5 | m | m |
| `qedkaxkeksq` | B | A | 3 | 8 | q | q |

### Rule 12: 8/16

Articulated rule: Label A if and only if the input contains more vowels than consonants.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `zxqiybmlwg` | A | B | 1 | 9 | z | g |
| `yeputcajo` | A | B | 4 | 5 | y | o |
| `vcsiyrl` | A | B | 1 | 6 | v | l |
| `ahsalyz` | A | B | 2 | 5 | a | z |
| `saoy` | A | B | 2 | 2 | s | y |
| `rcjwqyymb` | A | B | 0 | 9 | r | b |
| `yaplinfb` | A | B | 2 | 6 | y | b |
| `sshmir` | A | B | 1 | 5 | s | r |

### Rule 13: 4/16

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `iqjzig` | A | B | 2 | 4 | i | g |
| `ierwi` | B | A | 3 | 2 | i | i |
| `ojexpbo` | B | A | 3 | 4 | o | o |
| `qhpsgsb` | A | B | 0 | 7 | q | b |
| `yaplinfb` | A | B | 2 | 6 | y | b |
| `btrcsy` | A | B | 0 | 6 | b | y |
| `ulchou` | B | A | 3 | 3 | u | u |
| `rwtzd` | A | B | 0 | 5 | r | d |
| `fvpd` | A | B | 0 | 4 | f | d |
| `wdmmsow` | B | A | 1 | 6 | w | w |
| `uluqbu` | B | A | 3 | 3 | u | u |
| `zggjqwnuxxz` | B | A | 1 | 10 | z | z |

### Rule 14: 8/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `uffrfphcwqiu` | B | A | 3 | 9 | u | u |
| `qcidwdiaq` | B | A | 3 | 6 | q | q |
| `lcdlwl` | B | A | 0 | 6 | l | l |
| `lqmqql` | B | A | 0 | 6 | l | l |
| `hakwxh` | B | A | 1 | 5 | h | h |
| `hyfjlh` | B | A | 0 | 6 | h | h |
| `forkenimf` | B | A | 3 | 6 | f | f |
| `csqkhohlc` | B | A | 1 | 8 | c | c |

### Rule 15: 8/16

Articulated rule: Label A if and only if the string contains an even number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `onszdbm` | A | B | 1 | 6 | o | m |
| `xzxwco` | A | B | 1 | 5 | x | o |
| `xumytavgtxpx` | B | A | 2 | 10 | x | x |
| `hyfjlh` | B | A | 0 | 6 | h | h |
| `rppkr` | B | A | 0 | 5 | r | r |
| `jfmeej` | B | A | 2 | 4 | j | j |
| `vojedsfeiyji` | A | B | 5 | 7 | v | i |
| `akxkui` | A | B | 3 | 3 | a | i |

### Rule 16: 8/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `sfuqbyks` | B | A | 1 | 7 | s | s |
| `xqwvrmtigcnx` | B | A | 1 | 11 | x | x |
| `nfaozign` | B | A | 3 | 5 | n | n |
| `tigcevnfgst` | B | A | 2 | 9 | t | t |
| `lsrbxul` | B | A | 1 | 6 | l | l |
| `vwjbaauicv` | B | A | 4 | 6 | v | v |
| `xwoqzzwx` | B | A | 1 | 7 | x | x |
| `sqnsuhabns` | B | A | 2 | 8 | s | s |

### Rule 17: 11/16

Articulated rule: Label A if and only if the string contains more consonants from the first half of the alphabet (b–m) than from the second half (n–z).

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `bjqzrgtrh` | A | B | 0 | 9 | b | h |
| `iqjzig` | A | B | 2 | 4 | i | g |
| `nswpentqqvcf` | A | B | 1 | 11 | n | f |
| `xmtopj` | A | B | 1 | 5 | x | j |
| `pinbwipbrpyq` | A | B | 2 | 10 | p | q |

### Rule 18: 13/16

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `skefiuwfsfoz` | A | B | 4 | 8 | s | z |
| `zndxdvaersl` | A | B | 2 | 9 | z | l |
| `lsrbxul` | B | A | 1 | 6 | l | l |

### Rule 19: 8/16

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `yabbahzkd` | A | B | 2 | 7 | y | d |
| `xwoqzzwx` | B | A | 1 | 7 | x | x |
| `cvshs` | A | B | 0 | 5 | c | s |
| `pbrqjk` | A | B | 0 | 6 | p | k |
| `pdtaqtp` | B | A | 1 | 6 | p | p |
| `hytt` | A | B | 0 | 4 | h | t |
| `nsoja` | A | B | 2 | 3 | n | a |
| `pjsfezp` | B | A | 1 | 6 | p | p |

### Rule 20: 8/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `qcidwdiaq` | B | A | 3 | 6 | q | q |
| `alrvpveyxia` | B | A | 4 | 7 | a | a |
| `ohowyyveto` | B | A | 4 | 6 | o | o |
| `rfigzikr` | B | A | 2 | 6 | r | r |
| `unmajuhgycu` | B | A | 4 | 7 | u | u |
| `wetyvemgw` | B | A | 2 | 7 | w | w |
| `vkkrujbzwv` | B | A | 1 | 9 | v | v |
| `vwtjzv` | B | A | 0 | 6 | v | v |

### Rule 21: 10/16

Articulated rule: Label A if and only if the string contains an odd number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `bfijrjvo` | A | B | 2 | 6 | b | o |
| `pdtaqtp` | B | A | 1 | 6 | p | p |
| `pteqvcgjp` | B | A | 1 | 8 | p | p |
| `mxhzgom` | B | A | 1 | 6 | m | m |
| `fsdquzrf` | B | A | 1 | 7 | f | f |
| `fvpd` | A | B | 0 | 4 | f | d |

### Rule 22: 8/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `fxymkizf` | B | A | 1 | 7 | f | f |
| `bmwsb` | B | A | 0 | 5 | b | b |
| `teyevzmzt` | B | A | 2 | 7 | t | t |
| `jplj` | B | A | 0 | 4 | j | j |
| `tzmt` | B | A | 0 | 4 | t | t |
| `zyhfrrcyz` | B | A | 0 | 9 | z | z |
| `heehipzjexh` | B | A | 4 | 7 | h | h |
| `mobdpm` | B | A | 1 | 5 | m | m |

### Rule 23: 8/16

Articulated rule: Label A if and only if the input contains an odd number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `ilsip` | A | B | 2 | 3 | i | p |
| `gqjihcodrq` | A | B | 2 | 8 | g | q |
| `ihadtzi` | B | A | 3 | 4 | i | i |
| `bchebb` | B | A | 1 | 5 | b | b |
| `dtqwuundnkv` | A | B | 2 | 9 | d | v |
| `vneowev` | B | A | 3 | 4 | v | v |
| `kkbqek` | B | A | 1 | 5 | k | k |
| `xqwvrmtigcnx` | B | A | 1 | 11 | x | x |

### Rule 24: 8/16

Articulated rule: Label A if and only if the input contains more vowels than the label-B examples do, namely at least two vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `stjvffspbv` | A | B | 0 | 10 | s | v |
| `sqgu` | A | B | 1 | 3 | s | u |
| `gqgizcgtwzwq` | A | B | 1 | 11 | g | q |
| `czmgfgbkn` | A | B | 0 | 9 | c | n |
| `zzwxaxozgz` | B | A | 2 | 8 | z | z |
| `fcydmi` | A | B | 1 | 5 | f | i |
| `kzmudrbek` | B | A | 2 | 7 | k | k |
| `ogktdto` | B | A | 2 | 5 | o | o |

### Rule 25: 7/16

Articulated rule: Label A if and only if the input contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `hakwxh` | B | A | 1 | 5 | h | h |
| `kprk` | B | A | 0 | 4 | k | k |
| `heehipzjexh` | B | A | 4 | 7 | h | h |
| `nzeayqen` | B | A | 3 | 5 | n | n |
| `jocj` | B | A | 1 | 3 | j | j |
| `qhpjimnpwq` | B | A | 1 | 9 | q | q |
| `eztqyryque` | B | A | 3 | 7 | e | e |
| `selljujs` | B | A | 2 | 6 | s | s |
| `akdeu` | A | B | 3 | 2 | a | u |

### Rule 26: 9/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `uecwmusxhu` | B | A | 4 | 6 | u | u |
| `rxnpoditkiir` | B | A | 4 | 8 | r | r |
| `qhpjimnpwq` | B | A | 1 | 9 | q | q |
| `dvcqisjlvxd` | B | A | 1 | 10 | d | d |
| `ojexpbo` | B | A | 3 | 4 | o | o |
| `hakwxh` | B | A | 1 | 5 | h | h |
| `vneowev` | B | A | 3 | 4 | v | v |

### Rule 27: 7/16

Articulated rule: Label A if and only if the input contains more vowels than consonants.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `bmvkfk` | A | B | 0 | 6 | b | k |
| `xxve` | A | B | 1 | 3 | x | e |
| `snhuuxwuw` | A | B | 3 | 6 | s | w |
| `wctcafiosq` | A | B | 3 | 7 | w | q |
| `qviz` | A | B | 1 | 3 | q | z |
| `gqgizcgtwzwq` | A | B | 1 | 11 | g | q |
| `ofuuvssjqs` | A | B | 3 | 7 | o | s |
| `ierwi` | B | A | 3 | 2 | i | i |
| `jygfbkvkvtvb` | A | B | 0 | 12 | j | b |

### Rule 28: 8/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `tedgt` | B | A | 1 | 4 | t | t |
| `vihuywfilquv` | B | A | 4 | 8 | v | v |
| `zezz` | B | A | 1 | 3 | z | z |
| `zggjqwnuxxz` | B | A | 1 | 10 | z | z |
| `khmbynriyzfk` | B | A | 1 | 11 | k | k |
| `yigymmny` | B | A | 1 | 7 | y | y |
| `xgbybqzcwx` | B | A | 0 | 10 | x | x |
| `alrvpveyxia` | B | A | 4 | 7 | a | a |

### Rule 29: 8/16

Articulated rule: Label A if and only if the string contains more vowels than the letter "v".

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `olagsgcpevco` | B | A | 4 | 8 | o | o |
| `axtmvnm` | A | B | 1 | 6 | a | m |
| `tgfpz` | A | B | 0 | 5 | t | z |
| `ktuk` | B | A | 1 | 3 | k | k |
| `avypmmugcnia` | B | A | 4 | 8 | a | a |
| `uffrfphcwqiu` | B | A | 3 | 9 | u | u |
| `vlenggf` | A | B | 1 | 6 | v | f |
| `vwjbaauicv` | B | A | 4 | 6 | v | v |

### Rule 30: 7/16

Articulated rule: Label A if and only if the string contains an even number of consonants.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `csqkhohlc` | B | A | 1 | 8 | c | c |
| `sfcch` | A | B | 0 | 5 | s | h |
| `gxzg` | B | A | 0 | 4 | g | g |
| `volhtsbd` | A | B | 1 | 7 | v | d |
| `kpuwsyjysqcb` | A | B | 1 | 11 | k | b |
| `lpbaixbl` | B | A | 2 | 6 | l | l |
| `hcez` | A | B | 1 | 3 | h | z |
| `wiwqio` | A | B | 3 | 3 | w | o |
| `selljujs` | B | A | 2 | 6 | s | s |

### Rule 31: 11/16

Articulated rule: Label A if and only if the string contains an even number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `mmoqosthm` | B | A | 2 | 7 | m | m |
| `kpbyhiwknzl` | A | B | 1 | 10 | k | l |
| `mltseum` | B | A | 2 | 5 | m | m |
| `wewmlxqrgx` | A | B | 1 | 9 | w | x |
| `volhtsbd` | A | B | 1 | 7 | v | d |

### Rule 32: 5/16

Articulated rule: Label A if and only if the string contains an even number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `sqnsuhabns` | B | A | 2 | 8 | s | s |
| `pheilkp` | B | A | 2 | 5 | p | p |
| `gldcg` | B | A | 0 | 5 | g | g |
| `snhuuxwuw` | A | B | 3 | 6 | s | w |
| `gvsg` | B | A | 0 | 4 | g | g |
| `myix` | A | B | 1 | 3 | m | x |
| `sqgu` | A | B | 1 | 3 | s | u |
| `fekxasbf` | B | A | 2 | 6 | f | f |
| `gbqqpche` | A | B | 1 | 7 | g | e |
| `hllkfngmba` | A | B | 1 | 9 | h | a |
| `wvgnw` | B | A | 0 | 5 | w | w |

### Rule 33: 9/16

Articulated rule: Label A if and only if the input contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `bbflajb` | B | A | 1 | 6 | b | b |
| `fqceygf` | B | A | 1 | 6 | f | f |
| `jlnj` | B | A | 0 | 4 | j | j |
| `epjzwklute` | B | A | 3 | 7 | e | e |
| `annsvkwha` | B | A | 2 | 7 | a | a |
| `arqklsa` | B | A | 2 | 5 | a | a |
| `qedkaxkeksq` | B | A | 3 | 8 | q | q |

### Rule 34: 8/16

Articulated rule: Label A if and only if the input contains an odd number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `jfszf` | A | B | 0 | 5 | j | f |
| `nfjmojrbfpfn` | B | A | 1 | 11 | n | n |
| `nzeayqen` | B | A | 3 | 5 | n | n |
| `thraqqdbslt` | B | A | 1 | 10 | t | t |
| `ietmwgi` | B | A | 3 | 4 | i | i |
| `eudn` | A | B | 2 | 2 | e | n |
| `skefiuwfsfoz` | A | B | 4 | 8 | s | z |
| `zezz` | B | A | 1 | 3 | z | z |

### Rule 35: 4/16

Articulated rule: Label A if and only if the string contains an even number of vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `ohowyyveto` | B | A | 4 | 6 | o | o |
| `kzwenddgdfzg` | A | B | 1 | 11 | k | g |
| `gwef` | A | B | 1 | 3 | g | f |
| `fatrilxgmf` | B | A | 2 | 8 | f | f |
| `hvcxczucqah` | B | A | 2 | 9 | h | h |
| `ijyp` | A | B | 1 | 3 | i | p |
| `volhtsbd` | A | B | 1 | 7 | v | d |
| `jofd` | A | B | 1 | 3 | j | d |
| `tmanh` | A | B | 1 | 4 | t | h |
| `bpewewtlokvc` | A | B | 3 | 9 | b | c |
| `kzjmbgk` | B | A | 0 | 7 | k | k |
| `wewmlxqrgx` | A | B | 1 | 9 | w | x |

### Rule 36: 9/16

Articulated rule: Label A if and only if the string contains more consonants from the first half of the alphabet (a–m) than from the second half (n–z).

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `btxi` | A | B | 1 | 3 | b | i |
| `kzjmbgk` | B | A | 0 | 7 | k | k |
| `buhmyyiza` | A | B | 3 | 6 | b | a |
| `drkd` | B | A | 0 | 4 | d | d |
| `ntkpwjbapxe` | A | B | 2 | 9 | n | e |
| `tmanh` | A | B | 1 | 4 | t | h |
| `tfmaw` | A | B | 1 | 4 | t | w |

### Rule 37: 13/16

Articulated rule: Label A if and only if the input contains more vowels than the letter "w".

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `jrukfj` | B | A | 1 | 5 | j | j |
| `rwtzd` | A | B | 0 | 5 | r | d |
| `ystqgijffsy` | B | A | 1 | 10 | y | y |

### Rule 38: 7/16

Articulated rule: Label A if and only if the string contains more vowels than consonants.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `xvxderdll` | A | B | 1 | 8 | x | l |
| `aoxca` | B | A | 3 | 2 | a | a |
| `ovdfudzr` | A | B | 2 | 6 | o | r |
| `jygfbkvkvtvb` | A | B | 0 | 12 | j | b |
| `snhuuxwuw` | A | B | 3 | 6 | s | w |
| `fcpytmmfabcd` | A | B | 1 | 11 | f | d |
| `xxve` | A | B | 1 | 3 | x | e |
| `bpewewtlokvc` | A | B | 3 | 9 | b | c |
| `ksbcqqizeil` | A | B | 3 | 8 | k | l |

### Rule 39: 8/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `dtovd` | B | A | 1 | 4 | d | d |
| `gvsg` | B | A | 0 | 4 | g | g |
| `olagsgcpevco` | B | A | 4 | 8 | o | o |
| `kqabbydsk` | B | A | 1 | 8 | k | k |
| `bbflajb` | B | A | 1 | 6 | b | b |
| `lqmqql` | B | A | 0 | 6 | l | l |
| `dvdpxjxzjjmd` | B | A | 0 | 12 | d | d |
| `ktuk` | B | A | 1 | 3 | k | k |

### Rule 40: 9/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `ietmwgi` | B | A | 3 | 4 | i | i |
| `gvsg` | B | A | 0 | 4 | g | g |
| `xumytavgtxpx` | B | A | 2 | 10 | x | x |
| `gxzg` | B | A | 0 | 4 | g | g |
| `ystqgijffsy` | B | A | 1 | 10 | y | y |
| `wypcvw` | B | A | 0 | 6 | w | w |
| `esvfxhqyje` | B | A | 2 | 8 | e | e |

### Rule 41: 9/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `migdskzm` | B | A | 1 | 7 | m | m |
| `cnbolttc` | B | A | 1 | 7 | c | c |
| `coixsiwrzmc` | B | A | 3 | 8 | c | c |
| `vipv` | B | A | 1 | 3 | v | v |
| `bscvzb` | B | A | 0 | 6 | b | b |
| `pmsnrcipp` | B | A | 1 | 8 | p | p |
| `fhazfxzf` | B | A | 1 | 7 | f | f |

### Rule 42: 9/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `ssghcs` | B | A | 0 | 6 | s | s |
| `ihadtzi` | B | A | 3 | 4 | i | i |
| `sfuqbyks` | B | A | 1 | 7 | s | s |
| `tedgt` | B | A | 1 | 4 | t | t |
| `pjsfezp` | B | A | 1 | 6 | p | p |
| `cblvnegc` | B | A | 1 | 7 | c | c |
| `qprtq` | B | A | 0 | 5 | q | q |

### Rule 43: 8/16

Articulated rule: Label A if and only if the string contains more vowels than the string labeled B examples typically do—specifically, at least 3 vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `nzeayqen` | B | A | 3 | 5 | n | n |
| `nixuynxbanrn` | B | A | 3 | 9 | n | n |
| `ihadtzi` | B | A | 3 | 4 | i | i |
| `onszdbm` | A | B | 1 | 6 | o | m |
| `vlenggf` | A | B | 1 | 6 | v | f |
| `ksuq` | A | B | 1 | 3 | k | q |
| `xxve` | A | B | 1 | 3 | x | e |
| `rnojohtrndn` | A | B | 2 | 9 | r | n |

### Rule 44: 8/16

Articulated rule: Label A if and only if the string contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `rvmr` | B | A | 0 | 4 | r | r |
| `saoy` | A | B | 2 | 2 | s | y |
| `ojexpbo` | B | A | 3 | 4 | o | o |
| `vmwzfeaav` | B | A | 3 | 6 | v | v |
| `hyfjlh` | B | A | 0 | 6 | h | h |
| `pteqvcgjp` | B | A | 1 | 8 | p | p |
| `uidxslu` | B | A | 3 | 4 | u | u |
| `tzmt` | B | A | 0 | 4 | t | t |

### Rule 45: 8/16

Articulated rule: Label A if and only if the input contains more vowels than the letter y.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `annsvkwha` | B | A | 2 | 7 | a | a |
| `zjzefriraz` | B | A | 3 | 7 | z | z |
| `vdlnhyiz` | A | B | 1 | 7 | v | z |
| `jrqhkxjh` | A | B | 0 | 8 | j | h |
| `rtss` | A | B | 0 | 4 | r | s |
| `ojexpbo` | B | A | 3 | 4 | o | o |
| `uecwmusxhu` | B | A | 4 | 6 | u | u |
| `fekxasbf` | B | A | 2 | 6 | f | f |

### Rule 46: 11/16

Articulated rule: Label A if and only if the input contains more vowels than the letter m.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `zdlxm` | A | B | 0 | 5 | z | m |
| `tfmaw` | A | B | 1 | 4 | t | w |
| `avypmmugcnia` | B | A | 4 | 8 | a | a |
| `fsdquzrf` | B | A | 1 | 7 | f | f |
| `ulchou` | B | A | 3 | 3 | u | u |

### Rule 47: 11/16

Articulated rule: Label A if and only if the string contains more vowels than the string labeled B examples do—specifically, at least 3 vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `stjvffspbv` | A | B | 0 | 10 | s | v |
| `wczmi` | A | B | 1 | 4 | w | i |
| `afmfdnkqyi` | A | B | 2 | 8 | a | i |
| `uidxslu` | B | A | 3 | 4 | u | u |
| `guztgllak` | A | B | 2 | 7 | g | k |

### Rule 48: 8/16

Articulated rule: Label A if and only if the input contains more consonants than vowels.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `yabpy` | B | A | 1 | 4 | y | y |
| `eldtrnzyce` | B | A | 2 | 8 | e | e |
| `vihuywfilquv` | B | A | 4 | 8 | v | v |
| `dwotoffkd` | B | A | 2 | 7 | d | d |
| `betfpucseaxb` | B | A | 4 | 8 | b | b |
| `ndrjtrn` | B | A | 0 | 7 | n | n |
| `lsrbxul` | B | A | 1 | 6 | l | l |
| `zggjqwnuxxz` | B | A | 1 | 10 | z | z |

### Rule 49: 14/16

Articulated rule: Label A if and only if the string contains at least one of the vowels a, e, i, o, or u exactly once.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `jqmiplj` | B | A | 1 | 6 | j | j |
| `sngogmcdrms` | B | A | 1 | 10 | s | s |

### Rule 50: 8/16

Articulated rule: Label A if and only if the string contains more vowels than consonants.

| Input | True | Rule prediction | Vowels | Consonants | First | Last |
|---|:---:|:---:|---:|---:|:---:|:---:|
| `njyntapgqjg` | A | B | 1 | 10 | n | g |
| `nsoja` | A | B | 2 | 3 | n | a |
| `zltxdrmiug` | A | B | 2 | 8 | z | g |
| `kpuwsyjysqcb` | A | B | 1 | 11 | k | b |
| `ouarfeyzvns` | A | B | 4 | 7 | o | s |
| `koxft` | A | B | 1 | 4 | k | t |
| `akxntpl` | A | B | 1 | 6 | a | l |
| `eyorebue` | B | A | 5 | 3 | e | e |

