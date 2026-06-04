# Gold-Rule Application Control: trec_human_answer

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_trec_human_answer_seed0`

Correct canonical rule: Label A iff the question asks for a person or human entity.

Correct prompt-facing rule: Label B iff the question asks for a person or human entity; Label A otherwise.

## Summary

- Gold rules tested: `1`
- Rule-application calls: `50`
- Rule-application accuracy: `43/50` = `0.860`
- Nonparseable rate: `0.000`

## Settings

- Rule-application model: `gpt-5.4`
- Seed: `0`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Detailed Evaluations

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0362 | What is the Peloponnesian League ? | A | A | yes |
| 2 | trec_human_answer_pool_0336 | What daughter of Henry VIII and Anne Boleyn became queen of England ? | B | B | yes |
| 3 | trec_human_answer_pool_0100 | What Democratic prankster waved the train out of the station while Richard Nixon spoke from the caboose ? | B | B | yes |
| 4 | trec_human_answer_pool_0403 | What ocean does Mauritania border ? | A | A | yes |
| 5 | trec_human_answer_pool_0034 | What Ivy League school plays its home games at Palmer Stadium ? | B | A | no |
| 6 | trec_human_answer_pool_0276 | What is another word for diet ? | A | A | yes |
| 7 | trec_human_answer_pool_0464 | Who is the worst US President ever ? | B | B | yes |
| 8 | trec_human_answer_pool_0470 | What TV comedian worked with White Fang , Black Tooth and Pookie the Lion ? | B | B | yes |
| 9 | trec_human_answer_pool_0499 | What architect originated the glass house designed the Chicago Federal Center had a philosophy of `` less is more , '' and produced plans that were the forerunner of the California ranch house ? | B | B | yes |
| 10 | trec_human_answer_pool_0413 | Who is the actress Bette Davis once said she wished she looked like ? | B | B | yes |
| 11 | trec_human_answer_pool_0253 | What occupation has the highest divorce rate ? | B | A | no |
| 12 | trec_human_answer_pool_0265 | Who is Malaysia 's 43rd prime minister ? | B | B | yes |
| 13 | trec_human_answer_pool_0234 | How do birds find their way back to the same place every year ? | A | A | yes |
| 14 | trec_human_answer_pool_0021 | What was Mark Johnson referring to when he said : `` I still can 't believe it- we beat the Russians ? '' | A | A | yes |
| 15 | trec_human_answer_pool_0149 | What is the name of the highest mountain in Africa ? | A | A | yes |
| 16 | trec_human_answer_pool_0354 | Who is the prophet of the religion of Islam ? | B | B | yes |
| 17 | trec_human_answer_pool_0223 | What are xerophytes ? | A | A | yes |
| 18 | trec_human_answer_pool_0023 | Name the ship Beany and Cecil sailed . | A | A | yes |
| 19 | trec_human_answer_pool_0480 | What is another astronomic term for the Northern Lights ? | A | A | yes |
| 20 | trec_human_answer_pool_0004 | What are field effect transistors ? | A | A | yes |
| 21 | trec_human_answer_pool_0057 | What ill-fated craft was captained by Ernst Lehmann ? | A | A | yes |
| 22 | trec_human_answer_pool_0212 | Name four famous cartoon cats . | A | A | yes |
| 23 | trec_human_answer_pool_0446 | What Argentine boxer was shot dead outside a Nevada brothel in May ? | B | B | yes |
| 24 | trec_human_answer_pool_0263 | What fool is not so wise To lose an oath to win a paradise ? | B | A | no |
| 25 | trec_human_answer_pool_0118 | How did Bob Marley die ? | A | A | yes |
| 26 | trec_human_answer_pool_0497 | Who famously rode to warn the people of Massachusetts that the British were coming ? | B | B | yes |
| 27 | trec_human_answer_pool_0044 | What do I call the sons and daughters of my first cousins ? | A | B | no |
| 28 | trec_human_answer_pool_0062 | Who said `` Give me liberty or give me death '' ? | B | B | yes |
| 29 | trec_human_answer_pool_0315 | How many people die from snakebite poisoning in the U.S. per year ? | A | A | yes |
| 30 | trec_human_answer_pool_0222 | What movie has made the most money ? | A | A | yes |
| 31 | trec_human_answer_pool_0165 | Who invented the toothbrush ? | B | B | yes |
| 32 | trec_human_answer_pool_0063 | What is Garry Kasparov famous for ? | A | B | no |
| 33 | trec_human_answer_pool_0233 | What concerts are held in New York this week ? | A | A | yes |
| 34 | trec_human_answer_pool_0277 | Who 's the only president buried in Washington | B | B | yes |
| 35 | trec_human_answer_pool_0334 | Who co-starred with Julie Andrews in Mary Poppins ? | B | B | yes |
| 36 | trec_human_answer_pool_0075 | What 2th-century fictional character attends Pencey Prep School ? | B | B | yes |
| 37 | trec_human_answer_pool_0495 | Who is Mia Farrow 's mother ? | B | B | yes |
| 38 | trec_human_answer_pool_0193 | What organization has a Security Council ? | B | A | no |
| 39 | trec_human_answer_pool_0415 | Which college did Dikembe Mutombo attend ? | B | A | no |
| 40 | trec_human_answer_pool_0058 | What spy novelist served as Moscow correspondent for Reuter and The Times of London ? | B | B | yes |
| 41 | trec_human_answer_pool_0101 | What is the origin of gametophytic tissue ? | A | A | yes |
| 42 | trec_human_answer_pool_0134 | What 's the name of the actress who starred in the movie , `` Silence of the Lambs '' ? | B | B | yes |
| 43 | trec_human_answer_pool_0115 | What country has problems with hooligans ? | A | A | yes |
| 44 | trec_human_answer_pool_0348 | Who discovered imaginary numbers ? | B | B | yes |
| 45 | trec_human_answer_pool_0486 | Who were the only two bald U.S. Presidents ? | B | B | yes |
| 46 | trec_human_answer_pool_0294 | Name one of the Seven Wonders of the Ancient World . | A | A | yes |
| 47 | trec_human_answer_pool_0498 | Who 's baby was Sweet Pea on the Popeye cartoon ? | B | B | yes |
| 48 | trec_human_answer_pool_0387 | How many member states are in the UN ? | A | A | yes |
| 49 | trec_human_answer_pool_0252 | What are Maid-Rites ? | A | A | yes |
| 50 | trec_human_answer_pool_0091 | Who is Rocky 's and Bullwinkle 's ever-lost friend ? | B | B | yes |
