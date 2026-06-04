# Gold-Rule Application Control: trec_location_answer

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_trec_location_answer_seed0`

Correct canonical rule: Label A iff the question is related to locations, geography, or the earth.

Correct prompt-facing rule: Label B iff the question is related to locations, geography, or the earth; Label A otherwise.

## Summary

- Gold rules tested: `1`
- Rule-application calls: `50`
- Rule-application accuracy: `45/50` = `0.900`
- Nonparseable rate: `0.000`

## Settings

- Rule-application model: `gpt-5.4`
- Seed: `0`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Detailed Evaluations

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0362 | What is the country of origin for the name Thomas ? | B | B | yes |
| 2 | trec_location_answer_pool_0336 | How many times a day should you take a prescription marked `` q.i.d . '' ? | A | A | yes |
| 3 | trec_location_answer_pool_0100 | What country contains Africa 's northernmost point ? | B | B | yes |
| 4 | trec_location_answer_pool_0403 | What U.S. state records the least rainfall ? | B | B | yes |
| 5 | trec_location_answer_pool_0034 | What U.S. state comes last in an alphabetical list ? | B | B | yes |
| 6 | trec_location_answer_pool_0276 | What is the meaning of `` subaru ? '' | A | A | yes |
| 7 | trec_location_answer_pool_0464 | What canal does the Thatcher Ferry Bridge span ? | B | B | yes |
| 8 | trec_location_answer_pool_0470 | What phenomenon would you expect to read about in the monthly publication The Bigfoot News ? | A | A | yes |
| 9 | trec_location_answer_pool_0499 | What 's the longest river in the world ? | B | B | yes |
| 10 | trec_location_answer_pool_0413 | Who portrayed George M. Cohan in 1942 's Yankee Doodle Dandy ? | A | A | yes |
| 11 | trec_location_answer_pool_0253 | What country covers 8 , 600 , 387 square miles ? | B | B | yes |
| 12 | trec_location_answer_pool_0265 | What ocean is the largest in the world ? | B | B | yes |
| 13 | trec_location_answer_pool_0234 | What English word contains the most letters ? | A | A | yes |
| 14 | trec_location_answer_pool_0021 | What are faults in the earth 's crust ? | A | B | no |
| 15 | trec_location_answer_pool_0149 | What North American city would you visit to see Cleopatra 's Needle ? | B | B | yes |
| 16 | trec_location_answer_pool_0354 | Where can an individual get a contact lens tested that burned the entire surface of eye when new ? | B | A | no |
| 17 | trec_location_answer_pool_0223 | What desert has been called The Garden of Allah ? | B | B | yes |
| 18 | trec_location_answer_pool_0023 | What ice creams contain seaweed ? | A | A | yes |
| 19 | trec_location_answer_pool_0480 | Where is Belize located ? | B | B | yes |
| 20 | trec_location_answer_pool_0004 | What year did the Andy Griffith show begin ? | A | A | yes |
| 21 | trec_location_answer_pool_0057 | How many Marx Brothers were there ? | A | A | yes |
| 22 | trec_location_answer_pool_0212 | What caused an adjournment of the 25th anniversary session of the United Nations General Assembly ? | A | A | yes |
| 23 | trec_location_answer_pool_0446 | What country did the ancient Romans refer to as Hibernia ? | B | B | yes |
| 24 | trec_location_answer_pool_0263 | What is the temperature of the sun 's surface ? | A | B | no |
| 25 | trec_location_answer_pool_0118 | Who kept the most famous diary in the English language ? | A | A | yes |
| 26 | trec_location_answer_pool_0497 | Which country has the most water pollution ? | B | B | yes |
| 27 | trec_location_answer_pool_0044 | Where is the largest post office building in the world ? | B | B | yes |
| 28 | trec_location_answer_pool_0062 | Where in the United States do people live the longest ? | B | B | yes |
| 29 | trec_location_answer_pool_0315 | What is solar wind ? | A | A | yes |
| 30 | trec_location_answer_pool_0222 | Where are the headquarters of Eli Lilly ? | B | B | yes |
| 31 | trec_location_answer_pool_0165 | What is the fear of the computer called ? | A | A | yes |
| 32 | trec_location_answer_pool_0063 | What was the name of the U.S. 's first manned space program ? | A | A | yes |
| 33 | trec_location_answer_pool_0233 | Why do they call a hamburger a hamburger when there is no ham ? | A | A | yes |
| 34 | trec_location_answer_pool_0277 | What ocean does Mauritania border ? | B | B | yes |
| 35 | trec_location_answer_pool_0334 | Where can I find the history of the Hungarian language ? | B | B | yes |
| 36 | trec_location_answer_pool_0075 | Who was Damocles ? | A | A | yes |
| 37 | trec_location_answer_pool_0495 | What was the minimum wage in 1991 ? | A | A | yes |
| 38 | trec_location_answer_pool_0193 | What is the name of the song that Dracula plays on the organ ? | A | A | yes |
| 39 | trec_location_answer_pool_0415 | What season begins with the vernal equinox ? | A | B | no |
| 40 | trec_location_answer_pool_0058 | What are the numbers that fit into Fermont 's last theorem ? | A | B | no |
| 41 | trec_location_answer_pool_0101 | What is the origin of U.S. Army sergeant 's stripes ? | A | A | yes |
| 42 | trec_location_answer_pool_0134 | Where is the world championship sled dog race held each February ? | B | B | yes |
| 43 | trec_location_answer_pool_0115 | Who plays the cop in the movie `` Kindergarten Cop '' ? | A | A | yes |
| 44 | trec_location_answer_pool_0348 | What U.S. state is Mammoth Cave National Park in ? | B | B | yes |
| 45 | trec_location_answer_pool_0486 | When is St. Patrick 's Day ? | A | A | yes |
| 46 | trec_location_answer_pool_0294 | What are the world 's three largest oceans , in order of size ? | B | B | yes |
| 47 | trec_location_answer_pool_0498 | In 1990 , what day of the week did Christmas fall on ? | A | A | yes |
| 48 | trec_location_answer_pool_0387 | What is an eclipse ? | A | A | yes |
| 49 | trec_location_answer_pool_0252 | What city is graced by the Arch of Titus ? | B | B | yes |
| 50 | trec_location_answer_pool_0091 | What Judith Rossner novel was made into a film starring Diane Keaton ? | A | A | yes |
