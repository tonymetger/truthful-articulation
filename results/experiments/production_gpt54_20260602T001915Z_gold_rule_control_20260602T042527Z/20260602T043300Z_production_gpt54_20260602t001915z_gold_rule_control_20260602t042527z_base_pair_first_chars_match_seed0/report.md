# Gold-Rule Application Control: pair_first_chars_match

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_pair_first_chars_match_seed0`

Correct canonical rule: Label A iff the two random strings have the same first character.

Correct prompt-facing rule: Label B iff the two random strings have the same first character; Label A otherwise.

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
| 1 | pair_first_chars_match_pool_0362 | tmkpj \|\| toep | B | B | yes |
| 2 | pair_first_chars_match_pool_0336 | ksuvuzgz \|\| zzxvs | A | A | yes |
| 3 | pair_first_chars_match_pool_0100 | kaxupbxgcqup \|\| kkoeeydir | B | B | yes |
| 4 | pair_first_chars_match_pool_0403 | hmlwzyivnrm \|\| hxsso | B | B | yes |
| 5 | pair_first_chars_match_pool_0034 | njqc \|\| yfprcaox | A | A | yes |
| 6 | pair_first_chars_match_pool_0276 | xpbt \|\| xgalpmaq | B | B | yes |
| 7 | pair_first_chars_match_pool_0464 | jpxhxtcbbk \|\| jgbg | B | B | yes |
| 8 | pair_first_chars_match_pool_0470 | cgxd \|\| adnjtifpf | A | A | yes |
| 9 | pair_first_chars_match_pool_0499 | byal \|\| yuzslhhlp | A | A | yes |
| 10 | pair_first_chars_match_pool_0413 | bxgjrg \|\| bibqlwx | B | B | yes |
| 11 | pair_first_chars_match_pool_0253 | gldxhyxggp \|\| feoyv | A | A | yes |
| 12 | pair_first_chars_match_pool_0265 | jaxtekw \|\| zwhykwxepiqc | A | A | yes |
| 13 | pair_first_chars_match_pool_0234 | btize \|\| ootenmcfkyw | A | A | yes |
| 14 | pair_first_chars_match_pool_0021 | szmu \|\| fusy | A | A | yes |
| 15 | pair_first_chars_match_pool_0149 | gcrmbmw \|\| gsjherdl | B | B | yes |
| 16 | pair_first_chars_match_pool_0354 | ptwbgfg \|\| iakaw | A | A | yes |
| 17 | pair_first_chars_match_pool_0223 | fafb \|\| labneboaobe | A | A | yes |
| 18 | pair_first_chars_match_pool_0023 | ataaut \|\| kkfa | A | A | yes |
| 19 | pair_first_chars_match_pool_0480 | ovktdifjfbk \|\| kluheokvacf | A | A | yes |
| 20 | pair_first_chars_match_pool_0004 | trsiqmkqqw \|\| moux | A | A | yes |
| 21 | pair_first_chars_match_pool_0057 | zbzcwnockb \|\| wozmlxf | A | A | yes |
| 22 | pair_first_chars_match_pool_0212 | uvne \|\| uoweqkeg | B | B | yes |
| 23 | pair_first_chars_match_pool_0446 | sqydaktlies \|\| stkdfpjk | B | B | yes |
| 24 | pair_first_chars_match_pool_0263 | gtugcht \|\| slkveqnps | A | A | yes |
| 25 | pair_first_chars_match_pool_0118 | zisxxvas \|\| zeivex | B | B | yes |
| 26 | pair_first_chars_match_pool_0497 | wkmytzaxe \|\| wwmuwolpj | B | B | yes |
| 27 | pair_first_chars_match_pool_0044 | cdjstpxtd \|\| ojdgri | A | A | yes |
| 28 | pair_first_chars_match_pool_0062 | sdwtikxrzmt \|\| jhzwxk | A | A | yes |
| 29 | pair_first_chars_match_pool_0315 | hxmov \|\| hinl | B | B | yes |
| 30 | pair_first_chars_match_pool_0222 | bxixc \|\| bkunayvih | B | B | yes |
| 31 | pair_first_chars_match_pool_0165 | mieusc \|\| mjnjyntapgqj | B | B | yes |
| 32 | pair_first_chars_match_pool_0063 | llgzcltec \|\| ligd | B | B | yes |
| 33 | pair_first_chars_match_pool_0233 | xwwqrvamu \|\| xuerydyp | B | B | yes |
| 34 | pair_first_chars_match_pool_0277 | eerkevgjwbf \|\| ekkobiwm | B | B | yes |
| 35 | pair_first_chars_match_pool_0334 | oztndijfji \|\| eezgi | A | A | yes |
| 36 | pair_first_chars_match_pool_0075 | betcuohxltm \|\| bmvvz | B | B | yes |
| 37 | pair_first_chars_match_pool_0495 | ztxhwucy \|\| xjirkyic | A | A | yes |
| 38 | pair_first_chars_match_pool_0193 | ldahyypur \|\| aynkjdazex | A | A | yes |
| 39 | pair_first_chars_match_pool_0415 | oueywp \|\| olciusg | B | B | yes |
| 40 | pair_first_chars_match_pool_0058 | lohoalwos \|\| fkmvmphv | A | A | yes |
| 41 | pair_first_chars_match_pool_0101 | dfpwnyyi \|\| dgwn | B | B | yes |
| 42 | pair_first_chars_match_pool_0134 | qiaphvcur \|\| qvag | B | B | yes |
| 43 | pair_first_chars_match_pool_0115 | zeiypkgth \|\| zssbarzq | B | B | yes |
| 44 | pair_first_chars_match_pool_0348 | qhrcu \|\| bhxdlyn | A | A | yes |
| 45 | pair_first_chars_match_pool_0486 | itxrvh \|\| ijfhgpxhh | B | B | yes |
| 46 | pair_first_chars_match_pool_0294 | smkljb \|\| ioxkqts | A | A | yes |
| 47 | pair_first_chars_match_pool_0498 | shznuwep \|\| saumfg | B | B | yes |
| 48 | pair_first_chars_match_pool_0387 | ayins \|\| aqrewkw | B | B | yes |
| 49 | pair_first_chars_match_pool_0252 | ynvabeiedq \|\| fdvqxrvq | A | A | yes |
| 50 | pair_first_chars_match_pool_0091 | nsdzmrzlvfh \|\| nfecvlsehl | B | B | yes |
