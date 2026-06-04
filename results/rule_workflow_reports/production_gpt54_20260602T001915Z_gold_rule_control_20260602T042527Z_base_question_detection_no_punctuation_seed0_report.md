# Gold-Rule Application Control: question_detection_no_punctuation

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_question_detection_no_punctuation_seed0`

Correct canonical rule: Label A iff the input is an actual question after punctuation has been stripped.

Correct prompt-facing rule: Label B iff the input is an actual question after punctuation has been stripped; Label A otherwise.

## Summary

- Gold rules tested: `1`
- Rule-application calls: `50`
- Rule-application accuracy: `47/50` = `0.940`
- Nonparseable rate: `0.000`

## Settings

- Rule-application model: `gpt-5.4`
- Seed: `0`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Detailed Evaluations

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_no_punctuation_pool_0362 | What was known as the Spice Island | B | A | no |
| 2 | question_detection_no_punctuation_pool_0336 | What baseball team was the first to make numbers part of their uniform | B | B | yes |
| 3 | question_detection_no_punctuation_pool_0100 | movie fans get ready to take off the other direction | A | A | yes |
| 4 | question_detection_no_punctuation_pool_0403 | Who is the only president to serve 2 non consecutive terms | B | B | yes |
| 5 | question_detection_no_punctuation_pool_0034 | How many times has Harold Stassen announced a drive for the White House | B | B | yes |
| 6 | question_detection_no_punctuation_pool_0276 | What are the different types of plastic | B | B | yes |
| 7 | question_detection_no_punctuation_pool_0464 | we have n t seen such hilarity since say it is n t so | A | A | yes |
| 8 | question_detection_no_punctuation_pool_0470 | but it s too long and too convoluted and it ends in a muddle | A | A | yes |
| 9 | question_detection_no_punctuation_pool_0499 | What is Candlemas Day | B | B | yes |
| 10 | question_detection_no_punctuation_pool_0413 | What is an Angelus | B | B | yes |
| 11 | question_detection_no_punctuation_pool_0253 | a shapeless blob of desperate entertainment | A | A | yes |
| 12 | question_detection_no_punctuation_pool_0265 | one of the smartest takes on singles culture i ve seen in a long time | A | A | yes |
| 13 | question_detection_no_punctuation_pool_0234 | a quiet treasure a film to be savored | A | A | yes |
| 14 | question_detection_no_punctuation_pool_0021 | a solid film but more conscientious than it is truly stirring | A | A | yes |
| 15 | question_detection_no_punctuation_pool_0149 | the film s tone and pacing are off almost from the get go | A | A | yes |
| 16 | question_detection_no_punctuation_pool_0354 | How many people are taller than 7 feet | B | B | yes |
| 17 | question_detection_no_punctuation_pool_0223 | How many home runs did Babe Ruth hit in his lifetime | B | B | yes |
| 18 | question_detection_no_punctuation_pool_0023 | What shape shifting menace did Rom come to Earth to fight | B | B | yes |
| 19 | question_detection_no_punctuation_pool_0480 | a fast funny highly enjoyable movie | A | A | yes |
| 20 | question_detection_no_punctuation_pool_0004 | What California bridge was Don Brown the first to cross on May 27 1937 | B | B | yes |
| 21 | question_detection_no_punctuation_pool_0057 | What predators exist on Antarctica | B | B | yes |
| 22 | question_detection_no_punctuation_pool_0212 | collateral damage finally delivers the goods for schwarzenegger fans | A | A | yes |
| 23 | question_detection_no_punctuation_pool_0446 | Which Kevin Costner movie involves the Sioux Indians | B | A | no |
| 24 | question_detection_no_punctuation_pool_0263 | What chapter of Gone with the Wind has Rhett Butler leaving Scarlett O Hara | B | A | no |
| 25 | question_detection_no_punctuation_pool_0118 | What is meant by blood SED rate | B | B | yes |
| 26 | question_detection_no_punctuation_pool_0497 | like you could n t smell this turkey rotting from miles away | A | A | yes |
| 27 | question_detection_no_punctuation_pool_0044 | the film s performances are thrilling | A | A | yes |
| 28 | question_detection_no_punctuation_pool_0062 | it all feels like a monty python sketch gone horribly wrong | A | A | yes |
| 29 | question_detection_no_punctuation_pool_0315 | or doing last year s taxes with your ex wife | A | A | yes |
| 30 | question_detection_no_punctuation_pool_0222 | binoche makes it interesting trying to find out | A | A | yes |
| 31 | question_detection_no_punctuation_pool_0165 | not only unfunny but downright repellent | A | A | yes |
| 32 | question_detection_no_punctuation_pool_0063 | for movie lovers as well as opera lovers tosca is a real treat | A | A | yes |
| 33 | question_detection_no_punctuation_pool_0233 | What was Joe Namath s first contract worth | B | B | yes |
| 34 | question_detection_no_punctuation_pool_0277 | the humor is forced and heavy handed and occasionally simply unpleasant | A | A | yes |
| 35 | question_detection_no_punctuation_pool_0334 | a smart witty follow up | A | A | yes |
| 36 | question_detection_no_punctuation_pool_0075 | What magic does Mandrake employ | B | B | yes |
| 37 | question_detection_no_punctuation_pool_0495 | the minor figures surrounding bobby form a gritty urban mosaic | A | A | yes |
| 38 | question_detection_no_punctuation_pool_0193 | if your taste runs to difficult films you absolutely ca n t miss it | A | A | yes |
| 39 | question_detection_no_punctuation_pool_0415 | Where is the Rose Bowl played | B | B | yes |
| 40 | question_detection_no_punctuation_pool_0058 | verbinski implements every hack artist trick to give us the ooky spookies | A | A | yes |
| 41 | question_detection_no_punctuation_pool_0101 | When was China s first nuclear test | B | B | yes |
| 42 | question_detection_no_punctuation_pool_0134 | scorsese does n t give us a character worth giving a damn about | A | A | yes |
| 43 | question_detection_no_punctuation_pool_0115 | What s the U S Navy hymn | B | B | yes |
| 44 | question_detection_no_punctuation_pool_0348 | blanchett s performance confirms her power once again | A | A | yes |
| 45 | question_detection_no_punctuation_pool_0486 | a sequence of ridiculous shoot em up scenes | A | A | yes |
| 46 | question_detection_no_punctuation_pool_0294 | Where can I find information about Bob Barr representative from Georgia | B | B | yes |
| 47 | question_detection_no_punctuation_pool_0498 | plays like a volatile and overlong w magazine fashion spread | A | A | yes |
| 48 | question_detection_no_punctuation_pool_0387 | it treats women like idiots | A | A | yes |
| 49 | question_detection_no_punctuation_pool_0252 | How many corners does a spritsail have | B | B | yes |
| 50 | question_detection_no_punctuation_pool_0091 | the performances take the movie to a higher level | A | A | yes |
