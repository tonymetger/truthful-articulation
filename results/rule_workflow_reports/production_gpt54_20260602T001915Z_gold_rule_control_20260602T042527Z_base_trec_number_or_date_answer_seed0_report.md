# Gold-Rule Application Control: trec_number_or_date_answer

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_trec_number_or_date_answer_seed0`

Correct canonical rule: Label A iff the question asks for a number, quantity, date, or other numeric answer.

Correct prompt-facing rule: Label B iff the question asks for a number, quantity, date, or other numeric answer; Label A otherwise.

## Summary

- Gold rules tested: `1`
- Rule-application calls: `50`
- Rule-application accuracy: `48/50` = `0.960`
- Nonparseable rate: `0.000`

## Settings

- Rule-application model: `gpt-5.4`
- Seed: `0`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Detailed Evaluations

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0362 | Who was the first African American to play for the Brooklyn Dodgers ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0336 | What is the chemical reactivity of neon ? | B | A | no |
| 3 | trec_number_or_date_answer_pool_0100 | How many megawatts will the power project in Indonesia , built by a consortium headed by Mission Energy of US , produce ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0403 | What indoor sport saw the Phoenix Inferno become the Phoenix Pride on July 14 , 1983 , when the temperature hit 111 degrees ? | A | B | no |
| 5 | trec_number_or_date_answer_pool_0034 | What year did the United States abolish the draft ? | B | B | yes |
| 6 | trec_number_or_date_answer_pool_0276 | What is a `` node '' in computer terms ? | A | A | yes |
| 7 | trec_number_or_date_answer_pool_0464 | How much was the minimum wage in 1991 ? | B | B | yes |
| 8 | trec_number_or_date_answer_pool_0470 | How much did Lucy Van Pelt originally charge for psychiatric sessions ? | B | B | yes |
| 9 | trec_number_or_date_answer_pool_0499 | What year did the Titanic start on its journey ? | B | B | yes |
| 10 | trec_number_or_date_answer_pool_0413 | When was the NFL established ? | B | B | yes |
| 11 | trec_number_or_date_answer_pool_0253 | What is the chance of conceiving quadruplets ? | B | B | yes |
| 12 | trec_number_or_date_answer_pool_0265 | When did Hitler come to power in Germany ? | B | B | yes |
| 13 | trec_number_or_date_answer_pool_0234 | Who did Napolean defeat at Jena and Auerstadt ? | A | A | yes |
| 14 | trec_number_or_date_answer_pool_0021 | Who is the actress known for her role in the movie `` Gypsy '' ? | A | A | yes |
| 15 | trec_number_or_date_answer_pool_0149 | What company markets a shampoo `` for brunettes only '' ? | A | A | yes |
| 16 | trec_number_or_date_answer_pool_0354 | When is Father 's Day ? | B | B | yes |
| 17 | trec_number_or_date_answer_pool_0223 | What is the rounded part on the top of a matchbook called ? | A | A | yes |
| 18 | trec_number_or_date_answer_pool_0023 | What is the weather like on the moon ? | A | A | yes |
| 19 | trec_number_or_date_answer_pool_0480 | What is a fear of rejection ? | A | A | yes |
| 20 | trec_number_or_date_answer_pool_0004 | Why is Jane Goodall famous ? | A | A | yes |
| 21 | trec_number_or_date_answer_pool_0057 | What organization is the Security Council a part of ? | A | A | yes |
| 22 | trec_number_or_date_answer_pool_0212 | Who was Randy Steven Craft 's lawyer ? | A | A | yes |
| 23 | trec_number_or_date_answer_pool_0446 | How many miles is it from London , England to Plymouth , England ? | B | B | yes |
| 24 | trec_number_or_date_answer_pool_0263 | What percentage of Americans own their homes ? | B | B | yes |
| 25 | trec_number_or_date_answer_pool_0118 | What is a heuristic ? | A | A | yes |
| 26 | trec_number_or_date_answer_pool_0497 | How long does it take for your body to restore blood after you donate your blood ? | B | B | yes |
| 27 | trec_number_or_date_answer_pool_0044 | What city is sometimes called The Athens of Switzerland ? | A | A | yes |
| 28 | trec_number_or_date_answer_pool_0062 | What is the life span of the average monkey ? | B | B | yes |
| 29 | trec_number_or_date_answer_pool_0315 | What was Thatcher 's first name ? | A | A | yes |
| 30 | trec_number_or_date_answer_pool_0222 | Who invented the radio ? | A | A | yes |
| 31 | trec_number_or_date_answer_pool_0165 | How many stations do you shoot from in the basketball game `` Around the World '' ? | B | B | yes |
| 32 | trec_number_or_date_answer_pool_0063 | What is genocide ? | A | A | yes |
| 33 | trec_number_or_date_answer_pool_0233 | What is the world 's deadliest infectious disease ? | A | A | yes |
| 34 | trec_number_or_date_answer_pool_0277 | When did the Chernobyl nuclear accident occur ? | B | B | yes |
| 35 | trec_number_or_date_answer_pool_0334 | What is the world 's population ? | B | B | yes |
| 36 | trec_number_or_date_answer_pool_0075 | On average , how long time does it take to type a screenplay ? | B | B | yes |
| 37 | trec_number_or_date_answer_pool_0495 | How many bails are there in a cricket wicket ? | B | B | yes |
| 38 | trec_number_or_date_answer_pool_0193 | How many bones are there in the human hand ? | B | B | yes |
| 39 | trec_number_or_date_answer_pool_0415 | What year was the NAACP founded ? | B | B | yes |
| 40 | trec_number_or_date_answer_pool_0058 | What will the California gas tax be in the year 2000 ? | B | B | yes |
| 41 | trec_number_or_date_answer_pool_0101 | Which gender has bigger thighs ? | A | A | yes |
| 42 | trec_number_or_date_answer_pool_0134 | What is the elevation of St. Louis , MO ? | B | B | yes |
| 43 | trec_number_or_date_answer_pool_0115 | What university was Woodrow Wilson President of ? | A | A | yes |
| 44 | trec_number_or_date_answer_pool_0348 | How many tiles did the Space Shuttle Columbia lose on its second flight ? | B | B | yes |
| 45 | trec_number_or_date_answer_pool_0486 | How many people in the USA say their number one source of information is the newspaper ? | B | B | yes |
| 46 | trec_number_or_date_answer_pool_0294 | Who was the first US President to ride in an automobile to his inauguration ? | A | A | yes |
| 47 | trec_number_or_date_answer_pool_0498 | How many letters appear with the numbers 2 to 9 on a telephone dial ? | B | B | yes |
| 48 | trec_number_or_date_answer_pool_0387 | What country has the port of Haifa ? | A | A | yes |
| 49 | trec_number_or_date_answer_pool_0252 | What country contains the highest point in South America ? | A | A | yes |
| 50 | trec_number_or_date_answer_pool_0091 | How many disks does each player have in a four-handed game of Crokinole ? | B | B | yes |
