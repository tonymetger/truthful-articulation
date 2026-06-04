# Rule Articulation Workflow: trec_human_answer

Run ID: `production_gpt54_20260602T001915Z_articulation_20260602T011542Z_base_trec_human_answer_seed0`

Correct prompt-facing rule: Label B iff the question asks for a person or human entity; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.724
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.724
- Rules with all evals correct: 12
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
| 1 | 2/5 | Label A if and only if the question has 7 or fewer words; otherwise label B. |
| 2 | 4/5 | Label A if and only if the question begins with a wh-word other than “who” or asks “how many/how often,” while Label B if and only if it is a “who/whose/name which person” question. |
| 3 | 4/5 | Label A if and only if the question begins with a wh-word other than “who”; otherwise label B. |
| 4 | 5/5 | Label A if and only if the question is a general knowledge or definitional query, rather than asking about a specific named person’s identity, relation, or ownership. |
| 5 | 2/5 | Label A if and only if the question begins with “What,” “How,” or “Why”; otherwise label B. |
| 6 | 4/5 | Label A if and only if the question begins with a wh-word other than “who”; otherwise label B. |
| 7 | 2/5 | Label A if and only if the question begins with “What”; otherwise label B. |
| 8 | 5/5 | Label A if and only if the question is asking for a definition, explanation, or general fact, rather than asking to identify a specific person. |
| 9 | 3/5 | Label A if and only if the question begins with “What” or “How”; otherwise label B. |
| 10 | 4/5 | Label A if and only if the question asks for the meaning, definition, classification, quantity, or identity of a thing rather than asking for a specific named person, team, or institution. |
| 11 | 2/5 | Label A if and only if the question begins with “What” or “How”; otherwise label B. |
| 12 | 3/5 | Label A if and only if the question begins with “What” or “Why”; otherwise label B. |
| 13 | 4/5 | Label B if and only if the question asks for a specific person or organization by identity/name; otherwise label A. |
| 14 | 3/5 | Label B if and only if the question begins with “Who” or asks “What is/are a person called,” otherwise label A. |
| 15 | 5/5 | Label A if and only if the question begins with “What” or “How many”; otherwise label B. |
| 16 | 3/5 | Label A if and only if the question begins with “What” (including “What book/flower/ocean…”), and Label B if it begins with another wh-word or imperative form like “Who,” “Where,” or “Name.” |
| 17 | 4/5 | Label A if and only if the question begins with “What,” “In what,” or “How”; otherwise label B. |
| 18 | 5/5 | Label A if and only if the question asks for a non-person answer such as a place, number, event, explanation, or title; Label B if and only if it asks for a person’s identity. |
| 19 | 4/5 | Label A if and only if the question begins with “What” or “In what/What year,” while Label B if and only if it begins with “Who,” “Which,” or “What” asking for a specific named person or characters. |
| 20 | 5/5 | Label A if and only if the question begins with “What” or “When”; otherwise label B. |
| 21 | 3/5 | Label A if and only if the question begins with “What” or “How”; otherwise label B. |
| 22 | 3/5 | Label A if and only if the question begins with “What,” “Where,” or “How many”; otherwise label B. |
| 23 | 1/5 | Label A if and only if the question begins with an interrogative word other than “who” or “what”; otherwise label B. |
| 24 | 5/5 | Label A if and only if the question asks for a non-person answer; Label B if only if it asks for a person or group of people. |
| 25 | 4/5 | Label B if and only if the question asks for a specific named entity or person’s name; otherwise label A. |
| 26 | 2/5 | Label A if and only if the question begins with “What” or “Name”; otherwise label B. |
| 27 | 3/5 | Label A if and only if the question is asking for a definition, explanation, or identification of a general thing or concept, rather than asking for a specific named person, organization, or other particular entity. |
| 28 | 3/5 | Label A if and only if the question asks for objective factual or explanatory information, rather than a subjective, vague, or quiz-trivia-style identification. |
| 29 | 4/5 | Label A if and only if the question asks for a non-person answer; Label B if and only if it asks for a person’s identity or name. |
| 30 | 5/5 | Label A if and only if the question is generic or explanatory rather than asking for a specific named person, group, or fictional character identity. |
| 31 | 3/5 | Label B if and only if the question asks for a specific named person, organization, or school; otherwise label A. |
| 32 | 5/5 | Label A if and only if the question begins with “What” or “How”; otherwise label B. |
| 33 | 3/5 | Label A if and only if the question begins with “What,” “When,” or “How many”; otherwise label B. |
| 34 | 2/5 | Label A if and only if the question begins with an interrogative word other than “who/whom” (e.g. what, where, how, in what year); otherwise label B. |
| 35 | 4/5 | Label A if and only if the question word is not “who/whom,” and label B if and only if it begins with “who” or “whom.” |
| 36 | 4/5 | Label A if and only if the question begins with a wh-word other than “who”; otherwise label B. |
| 37 | 4/5 | Label A if and only if the question is not asking for a specific named person; otherwise label B. |
| 38 | 3/5 | Label A if and only if the question begins with “What” or “How many”; otherwise label B. |
| 39 | 4/5 | Label A if and only if the question begins with “What” or “Which”; otherwise label B. |
| 40 | 3/5 | Label A if and only if the question asks for a definition, explanation, property, or general fact, rather than asking for a specific person, quote source, or named entity. |
| 41 | 3/5 | Label A if and only if the question begins with “What,” “When,” “How many,” or “Name”; otherwise label B. |
| 42 | 4/5 | Label A if and only if the question word is not asking for a person—i.e., it begins with what, where, when, or which rather than who. |
| 43 | 3/5 | Label A if and only if the question begins with an interrogative other than “who” or “name”; otherwise label B. |
| 44 | 4/5 | Label A if and only if the question begins with “What” or “How”; otherwise label B. |
| 45 | 3/5 | Label A if and only if the question starts with “What”; otherwise label B. |
| 46 | 3/5 | Label A if and only if the question begins with a wh-word other than “who” or asks “how many”; otherwise label B. |
| 47 | 5/5 | Label A if and only if the question is a general how/what/which-information query rather than asking for a specific person’s name or identity. |
| 48 | 5/5 | Label A if and only if the question begins with “What,” “How,” or “In what year”; otherwise label B. |
| 49 | 5/5 | Label A if and only if the question begins with “What,” “Which,” or “How”; otherwise label B. |
| 50 | 5/5 | Label A if and only if the question asks for a definition, explanation, quantity, or other non-person answer; Label B if and only if it asks for a person’s identity or name. |

## Detailed Evaluations

### Rule 1: 2/5

Articulated rule: Label A if and only if the question has 7 or fewer words; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0375 | In what film did Steven Spielberg 's dog star as the main character 's dog ? | A | B | no |
| 2 | trec_human_answer_pool_0345 | How old do you have to be in order to rent a car in Italy ? | A | B | no |
| 3 | trec_human_answer_pool_0104 | How many quarters equal a pound ? | A | A | yes |
| 4 | trec_human_answer_pool_0417 | In what ways did Ivan IV support Russian expansion ? | A | B | no |
| 5 | trec_human_answer_pool_0035 | What Polynesian people inhabit New Zealand ? | B | B | yes |

### Rule 2: 4/5

Articulated rule: Label A if and only if the question begins with a wh-word other than “who” or asks “how many/how often,” while Label B if and only if it is a “who/whose/name which person” question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0136 | What is the last name of Lucy and Linus from the Peanut 's comic strip ? | B | A | no |
| 2 | trec_human_answer_pool_0272 | What song did Patti Page set people dancing to in 1950 ? | A | A | yes |
| 3 | trec_human_answer_pool_0128 | What countries have the highest ratio of university students ? | A | A | yes |
| 4 | trec_human_answer_pool_0483 | Who was the first female United States Representative ? | B | B | yes |
| 5 | trec_human_answer_pool_0430 | How many home runs did Lou Gehrig have during his career ? | A | A | yes |

### Rule 3: 4/5

Articulated rule: Label A if and only if the question begins with a wh-word other than “who”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0048 | Dialing , 900 , 740-TREE to have a tree planted will cost how much ? | A | B | no |
| 2 | trec_human_answer_pool_0254 | Why shouldn 't you remove a bee stinger with tweezers ? | A | A | yes |
| 3 | trec_human_answer_pool_0414 | Where are diamonds mined ? | A | A | yes |
| 4 | trec_human_answer_pool_0008 | Who invented the pull-tab opener on cans ? | B | B | yes |
| 5 | trec_human_answer_pool_0362 | What is the Peloponnesian League ? | A | A | yes |

### Rule 4: 5/5

Articulated rule: Label A if and only if the question is a general knowledge or definitional query, rather than asking about a specific named person’s identity, relation, or ownership.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0377 | How do I install a tile floor ? | A | A | yes |
| 2 | trec_human_answer_pool_0297 | Whose cupboard was bare ? | B | B | yes |
| 3 | trec_human_answer_pool_0145 | What is the federal minimum wage ? | A | A | yes |
| 4 | trec_human_answer_pool_0124 | What are the two languages of Malta ? | A | A | yes |
| 5 | trec_human_answer_pool_0380 | What Grand Slam golf tournament wasn 't held between 1940 and 1945 ? | A | A | yes |

### Rule 5: 2/5

Articulated rule: Label A if and only if the question begins with “What,” “How,” or “Why”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0039 | What does a phobophobe fear ? | A | A | yes |
| 2 | trec_human_answer_pool_0193 | What organization has a Security Council ? | B | A | no |
| 3 | trec_human_answer_pool_0010 | What company was the original sponsor of TV 's Superman ? | B | A | no |
| 4 | trec_human_answer_pool_0157 | What is the Internet2 ? | A | A | yes |
| 5 | trec_human_answer_pool_0177 | What celebrity couple , when going through a divorce , divided their toilet paper into two equal piles ? | B | A | no |

### Rule 6: 4/5

Articulated rule: Label A if and only if the question begins with a wh-word other than “who”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0258 | What is hydrogen ? | A | A | yes |
| 2 | trec_human_answer_pool_0292 | When was the battle of the Somme fought ? | A | A | yes |
| 3 | trec_human_answer_pool_0361 | What South Vietnamese president was assassinated by his generals in 1963 ? | B | A | no |
| 4 | trec_human_answer_pool_0410 | Who was the captain of the tanker , Exxon Valdez , involved in the oil spill in Prince William Sound , Alaska , 1989 ? | B | B | yes |
| 5 | trec_human_answer_pool_0472 | What is the 401 , K , plan ? | A | A | yes |

### Rule 7: 2/5

Articulated rule: Label A if and only if the question begins with “What”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0156 | How many times a year does the American Gourd Society publish The Gourd ? | A | B | no |
| 2 | trec_human_answer_pool_0328 | How can you tell when figs are ripe ? | A | B | no |
| 3 | trec_human_answer_pool_0330 | Who was Buffalo Bill ? | B | B | yes |
| 4 | trec_human_answer_pool_0435 | What is the only animal that can turn its stomach inside out ? | A | A | yes |
| 5 | trec_human_answer_pool_0369 | Why does sound travel quicker through water than air ? | A | B | no |

### Rule 8: 5/5

Articulated rule: Label A if and only if the question is asking for a definition, explanation, or general fact, rather than asking to identify a specific person.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0411 | Who was Galileo ? | B | B | yes |
| 2 | trec_human_answer_pool_0277 | Who 's the only president buried in Washington | B | B | yes |
| 3 | trec_human_answer_pool_0463 | What English queen had six fingers on one hand ? | B | B | yes |
| 4 | trec_human_answer_pool_0027 | What is the origin of the word ` posh ' ? | A | A | yes |
| 5 | trec_human_answer_pool_0104 | How many quarters equal a pound ? | A | A | yes |

### Rule 9: 3/5

Articulated rule: Label A if and only if the question begins with “What” or “How”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0103 | What character did Tex Avery first create upon arriving at MGM ? | B | A | no |
| 2 | trec_human_answer_pool_0122 | Why do girls have to wear training bras ? | A | B | no |
| 3 | trec_human_answer_pool_0063 | What is Garry Kasparov famous for ? | A | A | yes |
| 4 | trec_human_answer_pool_0487 | What is an auto-commentary ? | A | A | yes |
| 5 | trec_human_answer_pool_0340 | How do they find or choose witnesses to an execution ? | A | A | yes |

### Rule 10: 4/5

Articulated rule: Label A if and only if the question asks for the meaning, definition, classification, quantity, or identity of a thing rather than asking for a specific named person, team, or institution.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0040 | When was Queen Victoria born ? | A | B | no |
| 2 | trec_human_answer_pool_0298 | What part of Britain comprises the Highlands , Central Lowlands , and Southern Uplands ? | A | A | yes |
| 3 | trec_human_answer_pool_0300 | What do bats eat ? | A | A | yes |
| 4 | trec_human_answer_pool_0177 | What celebrity couple , when going through a divorce , divided their toilet paper into two equal piles ? | B | B | yes |
| 5 | trec_human_answer_pool_0409 | How do I e-mail someone at aol.com from yahoo.com ? | A | A | yes |

### Rule 11: 2/5

Articulated rule: Label A if and only if the question begins with “What” or “How”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0068 | When did CNN go on the air ? | A | B | no |
| 2 | trec_human_answer_pool_0050 | What NFL team did Vince Lombardi end his coaching career with ? | B | A | no |
| 3 | trec_human_answer_pool_0300 | What do bats eat ? | A | A | yes |
| 4 | trec_human_answer_pool_0209 | What non-alcoholic syrup is made from pomegranate juice ? | A | A | yes |
| 5 | trec_human_answer_pool_0162 | What South African producer had a 1988 profit of $836 million ? | B | A | no |

### Rule 12: 3/5

Articulated rule: Label A if and only if the question begins with “What” or “Why”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0244 | What is the treatment for depression ? | A | A | yes |
| 2 | trec_human_answer_pool_0011 | How many people die of tuberculosis yearly ? | A | B | no |
| 3 | trec_human_answer_pool_0413 | Who is the actress Bette Davis once said she wished she looked like ? | B | B | yes |
| 4 | trec_human_answer_pool_0291 | What 's the most popular four-player game of all time ? | A | A | yes |
| 5 | trec_human_answer_pool_0482 | What famed clown appeared on an early Howdy Doody Show and insisted that Clarabell be made up as a real clown ? | B | A | no |

### Rule 13: 4/5

Articulated rule: Label B if and only if the question asks for a specific person or organization by identity/name; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0086 | Who led the Normans to victory in the Battle of Hastings ? | B | B | yes |
| 2 | trec_human_answer_pool_0046 | What Pulitzer Prize-winning novelist ran for mayor of New York City ? | B | B | yes |
| 3 | trec_human_answer_pool_0183 | Which NBA players had jersey number 0 ? | B | A | no |
| 4 | trec_human_answer_pool_0023 | Name the ship Beany and Cecil sailed . | A | A | yes |
| 5 | trec_human_answer_pool_0482 | What famed clown appeared on an early Howdy Doody Show and insisted that Clarabell be made up as a real clown ? | B | B | yes |

### Rule 14: 3/5

Articulated rule: Label B if and only if the question begins with “Who” or asks “What is/are a person called,” otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0038 | How many calories are there in soy sauce ? | A | A | yes |
| 2 | trec_human_answer_pool_0238 | What would you add to the clay mixture to produce bone china ? | A | A | yes |
| 3 | trec_human_answer_pool_0260 | Which is the only Dick Tracy villain to appear three times ? | B | A | no |
| 4 | trec_human_answer_pool_0140 | What President served for five years , six months and 2 days ? | B | A | no |
| 5 | trec_human_answer_pool_0362 | What is the Peloponnesian League ? | A | A | yes |

### Rule 15: 5/5

Articulated rule: Label A if and only if the question begins with “What” or “How many”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0388 | What are vermicilli , rigati , zitoni , and tubetti ? | A | A | yes |
| 2 | trec_human_answer_pool_0456 | What 's the closest G2 Spectrum Yellow Dwarf to Earth ? | A | A | yes |
| 3 | trec_human_answer_pool_0297 | Whose cupboard was bare ? | B | B | yes |
| 4 | trec_human_answer_pool_0442 | How many colleges are in Wyoming ? | A | A | yes |
| 5 | trec_human_answer_pool_0151 | What is the origin of `` jiggy '' as in getting jiggy with it ? | A | A | yes |

### Rule 16: 3/5

Articulated rule: Label A if and only if the question begins with “What” (including “What book/flower/ocean…”), and Label B if it begins with another wh-word or imperative form like “Who,” “Where,” or “Name.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0151 | What is the origin of `` jiggy '' as in getting jiggy with it ? | A | A | yes |
| 2 | trec_human_answer_pool_0458 | Who was elected president of South Africa in 1994 ? | B | B | yes |
| 3 | trec_human_answer_pool_0343 | Who was the lawyer for Randy Craft ? | B | B | yes |
| 4 | trec_human_answer_pool_0377 | How do I install a tile floor ? | A | B | no |
| 5 | trec_human_answer_pool_0240 | What Soviet leader owned a Rolls-Royce ? | B | A | no |

### Rule 17: 4/5

Articulated rule: Label A if and only if the question begins with “What,” “In what,” or “How”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0155 | What year did Apartheid start ? | A | A | yes |
| 2 | trec_human_answer_pool_0186 | What is the name of a Greek god ? | B | A | no |
| 3 | trec_human_answer_pool_0341 | What is the cause of endangered species ? | A | A | yes |
| 4 | trec_human_answer_pool_0116 | Who portrayed W.C. Fields in the film W.C. Fields and Me ? | B | B | yes |
| 5 | trec_human_answer_pool_0337 | How can I get some free technical information on Electric Vehicle ? | A | A | yes |

### Rule 18: 5/5

Articulated rule: Label A if and only if the question asks for a non-person answer such as a place, number, event, explanation, or title; Label B if and only if it asks for a person’s identity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0089 | How do I register a trade name in North Carolina ? | A | A | yes |
| 2 | trec_human_answer_pool_0096 | Who was chief engineer of the Starship Enterprise ? | B | B | yes |
| 3 | trec_human_answer_pool_0154 | The Orange Bowl is located in what city ? | A | A | yes |
| 4 | trec_human_answer_pool_0011 | How many people die of tuberculosis yearly ? | A | A | yes |
| 5 | trec_human_answer_pool_0374 | What is the largest city in Connecticut ? | A | A | yes |

### Rule 19: 4/5

Articulated rule: Label A if and only if the question begins with “What” or “In what/What year,” while Label B if and only if it begins with “Who,” “Which,” or “What” asking for a specific named person or characters.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0037 | What diminutive American female gymnast stole the show at the 1984 Olympics ? | B | B | yes |
| 2 | trec_human_answer_pool_0387 | How many member states are in the UN ? | A | B | no |
| 3 | trec_human_answer_pool_0291 | What 's the most popular four-player game of all time ? | A | A | yes |
| 4 | trec_human_answer_pool_0233 | What concerts are held in New York this week ? | A | A | yes |
| 5 | trec_human_answer_pool_0078 | What powdered soft drink mix went into space ? | A | A | yes |

### Rule 20: 5/5

Articulated rule: Label A if and only if the question begins with “What” or “When”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0347 | Who is the prime minister of Australia ? | B | B | yes |
| 2 | trec_human_answer_pool_0204 | Who won Oscars for her roles in Gone with the Wind and A Streetcar Named Desire ? | B | B | yes |
| 3 | trec_human_answer_pool_0021 | What was Mark Johnson referring to when he said : `` I still can 't believe it- we beat the Russians ? '' | A | A | yes |
| 4 | trec_human_answer_pool_0269 | Who was the first governor of West Virginia ? | B | B | yes |
| 5 | trec_human_answer_pool_0258 | What is hydrogen ? | A | A | yes |

### Rule 21: 3/5

Articulated rule: Label A if and only if the question begins with “What” or “How”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0470 | What TV comedian worked with White Fang , Black Tooth and Pookie the Lion ? | B | A | no |
| 2 | trec_human_answer_pool_0095 | What is the virus HIV ? | A | A | yes |
| 3 | trec_human_answer_pool_0079 | Name a novel written by John Steinbeck . | A | B | no |
| 4 | trec_human_answer_pool_0484 | What is artificial intelligence ? | A | A | yes |
| 5 | trec_human_answer_pool_0004 | What are field effect transistors ? | A | A | yes |

### Rule 22: 3/5

Articulated rule: Label A if and only if the question begins with “What,” “Where,” or “How many”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0471 | Who directed Citizen Kane ? | B | B | yes |
| 2 | trec_human_answer_pool_0168 | What writer-journalist made his mark describing colorful Broadway and underworld characters ? | B | A | no |
| 3 | trec_human_answer_pool_0184 | Where did the saying `` rule of thumb '' come from ? | A | A | yes |
| 4 | trec_human_answer_pool_0177 | What celebrity couple , when going through a divorce , divided their toilet paper into two equal piles ? | B | A | no |
| 5 | trec_human_answer_pool_0151 | What is the origin of `` jiggy '' as in getting jiggy with it ? | A | A | yes |

### Rule 23: 1/5

Articulated rule: Label A if and only if the question begins with an interrogative word other than “who” or “what”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0338 | What are the most albums sold by one artist or band ? | A | B | no |
| 2 | trec_human_answer_pool_0367 | What are Quaaludes ? | A | B | no |
| 3 | trec_human_answer_pool_0286 | What is a baby lion called ? | A | B | no |
| 4 | trec_human_answer_pool_0003 | Who did Sara Jane Moore try to assassinate ? | B | B | yes |
| 5 | trec_human_answer_pool_0457 | What river in the US is known as the Big Muddy ? | A | B | no |

### Rule 24: 5/5

Articulated rule: Label A if and only if the question asks for a non-person answer; Label B if only if it asks for a person or group of people.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0288 | What cigar-chewing comedian observed : `` You 're only as old as the woman you feel '' ? | B | B | yes |
| 2 | trec_human_answer_pool_0152 | What was archy , and mehitabel ? | A | A | yes |
| 3 | trec_human_answer_pool_0364 | How many colonies did Germany get to keep after World War I ? | A | A | yes |
| 4 | trec_human_answer_pool_0058 | What spy novelist served as Moscow correspondent for Reuter and The Times of London ? | B | B | yes |
| 5 | trec_human_answer_pool_0149 | What is the name of the highest mountain in Africa ? | A | A | yes |

### Rule 25: 4/5

Articulated rule: Label B if and only if the question asks for a specific named entity or person’s name; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0034 | What Ivy League school plays its home games at Palmer Stadium ? | B | A | no |
| 2 | trec_human_answer_pool_0451 | What 19th-century painter died in the Marquesas Islands ? | B | B | yes |
| 3 | trec_human_answer_pool_0230 | What future deer hunter portrayed Annie Hall 's neurotic brother , Duane ? | B | B | yes |
| 4 | trec_human_answer_pool_0309 | Who said , `` I shall return . '' during World War Two ? | B | B | yes |
| 5 | trec_human_answer_pool_0428 | How many bones are there in the human hand ? | A | A | yes |

### Rule 26: 2/5

Articulated rule: Label A if and only if the question begins with “What” or “Name”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0106 | When was Nostradamus born ? | A | B | no |
| 2 | trec_human_answer_pool_0092 | Where can I find a large list of 5 to 6 letter words ? | A | B | no |
| 3 | trec_human_answer_pool_0221 | What was the longest war in U.S. history ? | A | A | yes |
| 4 | trec_human_answer_pool_0289 | What was the name of Randy Steven Craft 's lawyer ? | B | A | no |
| 5 | trec_human_answer_pool_0277 | Who 's the only president buried in Washington | B | B | yes |

### Rule 27: 3/5

Articulated rule: Label A if and only if the question is asking for a definition, explanation, or identification of a general thing or concept, rather than asking for a specific named person, organization, or other particular entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0068 | When did CNN go on the air ? | A | B | no |
| 2 | trec_human_answer_pool_0345 | How old do you have to be in order to rent a car in Italy ? | A | B | no |
| 3 | trec_human_answer_pool_0005 | Who is the creator of `` The Muppets '' ? | B | B | yes |
| 4 | trec_human_answer_pool_0071 | What is the name of the American swimmer who won seven gold medals in the 1972 Olympics ? | B | B | yes |
| 5 | trec_human_answer_pool_0003 | Who did Sara Jane Moore try to assassinate ? | B | B | yes |

### Rule 28: 3/5

Articulated rule: Label A if and only if the question asks for objective factual or explanatory information, rather than a subjective, vague, or quiz-trivia-style identification.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0113 | What country is the largest diamond producer ? | A | A | yes |
| 2 | trec_human_answer_pool_0139 | Who was the oldest U.S. president ? | B | A | no |
| 3 | trec_human_answer_pool_0339 | What caused Shea & Gould to close their L.A. office ? | A | A | yes |
| 4 | trec_human_answer_pool_0073 | Who invented television ? | B | A | no |
| 5 | trec_human_answer_pool_0063 | What is Garry Kasparov famous for ? | A | A | yes |

### Rule 29: 4/5

Articulated rule: Label A if and only if the question asks for a non-person answer; Label B if and only if it asks for a person’s identity or name.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0475 | What percentage of children between the ages of two and eleven watch ` The Simpsons ' ? | A | A | yes |
| 2 | trec_human_answer_pool_0263 | What fool is not so wise To lose an oath to win a paradise ? | B | B | yes |
| 3 | trec_human_answer_pool_0053 | Who made the first airplane ? | B | B | yes |
| 4 | trec_human_answer_pool_0366 | What card company sells Christmas ornaments ? | B | A | no |
| 5 | trec_human_answer_pool_0295 | Which of the following celebrities was not born in Philadelphia ? | B | B | yes |

### Rule 30: 5/5

Articulated rule: Label A if and only if the question is generic or explanatory rather than asking for a specific named person, group, or fictional character identity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0217 | Who runs Andy Capp 's favorite pub ? | B | B | yes |
| 2 | trec_human_answer_pool_0139 | Who was the oldest U.S. president ? | B | B | yes |
| 3 | trec_human_answer_pool_0296 | What baseball player was known as Charley Hustle ? | B | B | yes |
| 4 | trec_human_answer_pool_0257 | Who founded the Unification Church ? | B | B | yes |
| 5 | trec_human_answer_pool_0319 | What is the population in India ? | A | A | yes |

### Rule 31: 3/5

Articulated rule: Label B if and only if the question asks for a specific named person, organization, or school; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0172 | CNN is the abbreviation for what ? | A | A | yes |
| 2 | trec_human_answer_pool_0123 | What Indian tribe is F Troop perpetually doing battle with ? | B | A | no |
| 3 | trec_human_answer_pool_0299 | What is a fear of speaking ? | A | A | yes |
| 4 | trec_human_answer_pool_0321 | Name of heroine in `` Scruples '' ? | B | A | no |
| 5 | trec_human_answer_pool_0085 | What is the term for someone who hates mankind ? | A | A | yes |

### Rule 32: 5/5

Articulated rule: Label A if and only if the question begins with “What” or “How”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0330 | Who was Buffalo Bill ? | B | B | yes |
| 2 | trec_human_answer_pool_0301 | What did the ancients call the four great elements ? | A | A | yes |
| 3 | trec_human_answer_pool_0225 | What city is wiener schnitzel named for ? | A | A | yes |
| 4 | trec_human_answer_pool_0265 | Who is Malaysia 's 43rd prime minister ? | B | B | yes |
| 5 | trec_human_answer_pool_0054 | Who retired with 755 home runs to his credit ? | B | B | yes |

### Rule 33: 3/5

Articulated rule: Label A if and only if the question begins with “What,” “When,” or “How many”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0082 | Who received the Will Rogers Award in 1989 ? | B | B | yes |
| 2 | trec_human_answer_pool_0366 | What card company sells Christmas ornaments ? | B | A | no |
| 3 | trec_human_answer_pool_0413 | Who is the actress Bette Davis once said she wished she looked like ? | B | B | yes |
| 4 | trec_human_answer_pool_0208 | Who wrote the book , `` The Grinch Who Stole Christmas '' ? | B | B | yes |
| 5 | trec_human_answer_pool_0009 | How is it correct to say ` qigong ' ? | A | B | no |

### Rule 34: 2/5

Articulated rule: Label A if and only if the question begins with an interrogative word other than “who/whom” (e.g. what, where, how, in what year); otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0439 | What company has built more than 2.5 billion little green houses since 1935 ? | B | A | no |
| 2 | trec_human_answer_pool_0282 | Whom did Lauren Bacall marry after her husband Humphrey Bogart died ? | B | B | yes |
| 3 | trec_human_answer_pool_0211 | Who is the `` Queen Mother '' ? | B | B | yes |
| 4 | trec_human_answer_pool_0065 | What baseball player was walked the most times ? | B | A | no |
| 5 | trec_human_answer_pool_0230 | What future deer hunter portrayed Annie Hall 's neurotic brother , Duane ? | B | A | no |

### Rule 35: 4/5

Articulated rule: Label A if and only if the question word is not “who/whom,” and label B if and only if it begins with “who” or “whom.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0233 | What concerts are held in New York this week ? | A | A | yes |
| 2 | trec_human_answer_pool_0302 | What schools in the Washington , DC NN NN VBP NN NN NN NN . | B | A | no |
| 3 | trec_human_answer_pool_0074 | How big is the Electoral College ? | A | A | yes |
| 4 | trec_human_answer_pool_0417 | In what ways did Ivan IV support Russian expansion ? | A | A | yes |
| 5 | trec_human_answer_pool_0464 | Who is the worst US President ever ? | B | B | yes |

### Rule 36: 4/5

Articulated rule: Label A if and only if the question begins with a wh-word other than “who”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0001 | Name the company that used the line , `` Even your best friend won 't tell you '' in its ad ? | B | B | yes |
| 2 | trec_human_answer_pool_0040 | When was Queen Victoria born ? | A | A | yes |
| 3 | trec_human_answer_pool_0354 | Who is the prophet of the religion of Islam ? | B | B | yes |
| 4 | trec_human_answer_pool_0414 | Where are diamonds mined ? | A | A | yes |
| 5 | trec_human_answer_pool_0420 | What businesses or agencies would do an employment verification ? | B | A | no |

### Rule 37: 4/5

Articulated rule: Label A if and only if the question is not asking for a specific named person; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0497 | Who famously rode to warn the people of Massachusetts that the British were coming ? | B | B | yes |
| 2 | trec_human_answer_pool_0000 | What is her husband 's name ? | B | A | no |
| 3 | trec_human_answer_pool_0109 | Who played Emperor Palpatine in Star Wars ? | B | B | yes |
| 4 | trec_human_answer_pool_0281 | What made the Finger Lakes in western New York state ? | A | A | yes |
| 5 | trec_human_answer_pool_0241 | What British monarch 's lap did P.T. Barnum 's Tom Thumb sit in ? | B | B | yes |

### Rule 38: 3/5

Articulated rule: Label A if and only if the question begins with “What” or “How many”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0150 | What were Babe Ruth 's Christian names ? | B | A | no |
| 2 | trec_human_answer_pool_0116 | Who portrayed W.C. Fields in the film W.C. Fields and Me ? | B | B | yes |
| 3 | trec_human_answer_pool_0154 | The Orange Bowl is located in what city ? | A | B | no |
| 4 | trec_human_answer_pool_0070 | What are the seven wonders of the world ? | A | A | yes |
| 5 | trec_human_answer_pool_0486 | Who were the only two bald U.S. Presidents ? | B | B | yes |

### Rule 39: 4/5

Articulated rule: Label A if and only if the question begins with “What” or “Which”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0048 | Dialing , 900 , 740-TREE to have a tree planted will cost how much ? | A | B | no |
| 2 | trec_human_answer_pool_0261 | What is the softest part of the body ? | A | A | yes |
| 3 | trec_human_answer_pool_0384 | Who was the 16th President of the United States ? | B | B | yes |
| 4 | trec_human_answer_pool_0429 | Who was Confucius ? | B | B | yes |
| 5 | trec_human_answer_pool_0311 | What is the best hospital for orthopedics in the country ? | A | A | yes |

### Rule 40: 3/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, property, or general fact, rather than asking for a specific person, quote source, or named entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0344 | Who lived on the shores of the Gitchee Gumee River ? | B | B | yes |
| 2 | trec_human_answer_pool_0328 | How can you tell when figs are ripe ? | A | A | yes |
| 3 | trec_human_answer_pool_0150 | What were Babe Ruth 's Christian names ? | B | B | yes |
| 4 | trec_human_answer_pool_0088 | What William Styron book is about a black preacher who leads a slave revolt ? | A | B | no |
| 5 | trec_human_answer_pool_0418 | What U.S. state has the second-longest coastline ? | A | B | no |

### Rule 41: 3/5

Articulated rule: Label A if and only if the question begins with “What,” “When,” “How many,” or “Name”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0088 | What William Styron book is about a black preacher who leads a slave revolt ? | A | A | yes |
| 2 | trec_human_answer_pool_0305 | Who created the comic strip , `` Garfield '' ? | B | B | yes |
| 3 | trec_human_answer_pool_0408 | What is the origin of thank you notes ? | A | A | yes |
| 4 | trec_human_answer_pool_0112 | Where was the first golf course in the United States ? | A | B | no |
| 5 | trec_human_answer_pool_0424 | What is the present Pope named ? | B | A | no |

### Rule 42: 4/5

Articulated rule: Label A if and only if the question word is not asking for a person—i.e., it begins with what, where, when, or which rather than who.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0478 | What is an example of a famous rock band from the sixties ? | B | A | no |
| 2 | trec_human_answer_pool_0171 | What is the first book of the Old Testament ? | A | A | yes |
| 3 | trec_human_answer_pool_0475 | What percentage of children between the ages of two and eleven watch ` The Simpsons ' ? | A | A | yes |
| 4 | trec_human_answer_pool_0487 | What is an auto-commentary ? | A | A | yes |
| 5 | trec_human_answer_pool_0125 | Where can I find a review of Nightmare on Elm Street in a film journal ? | A | A | yes |

### Rule 43: 3/5

Articulated rule: Label A if and only if the question begins with an interrogative other than “who” or “name”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0005 | Who is the creator of `` The Muppets '' ? | B | B | yes |
| 2 | trec_human_answer_pool_0020 | What is Shakespeare 's nickname ? | B | A | no |
| 3 | trec_human_answer_pool_0092 | Where can I find a large list of 5 to 6 letter words ? | A | A | yes |
| 4 | trec_human_answer_pool_0307 | What Louisiana Senator won a seat that had been held by his father and mother ? | B | A | no |
| 5 | trec_human_answer_pool_0047 | Who is the Queen of Holland ? | B | B | yes |

### Rule 44: 4/5

Articulated rule: Label A if and only if the question begins with “What” or “How”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0042 | Who developed the first polio vaccine ? | B | B | yes |
| 2 | trec_human_answer_pool_0038 | How many calories are there in soy sauce ? | A | A | yes |
| 3 | trec_human_answer_pool_0098 | Name the story by Chris Van Allsburg in the which a boy tries to become a great sailor ? | A | B | no |
| 4 | trec_human_answer_pool_0204 | Who won Oscars for her roles in Gone with the Wind and A Streetcar Named Desire ? | B | B | yes |
| 5 | trec_human_answer_pool_0438 | Who else was considered for the role of Luke Skywalker when George Lucas was casting for Star Wars ? | B | B | yes |

### Rule 45: 3/5

Articulated rule: Label A if and only if the question starts with “What”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0066 | Where does the opera singer Ileana Cotrubas come from ? | A | B | no |
| 2 | trec_human_answer_pool_0352 | What is the full name of the man who invented the multicolored game cube that has 42.3 quintillion potential combinations ? | B | A | no |
| 3 | trec_human_answer_pool_0205 | What state is the Filenes store located in ? | A | A | yes |
| 4 | trec_human_answer_pool_0415 | Which college did Dikembe Mutombo attend ? | B | B | yes |
| 5 | trec_human_answer_pool_0022 | Which German president was pressured into appointing Hitler chancellor in 1933 ? | B | B | yes |

### Rule 46: 3/5

Articulated rule: Label A if and only if the question begins with a wh-word other than “who” or asks “how many”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0336 | What daughter of Henry VIII and Anne Boleyn became queen of England ? | B | A | no |
| 2 | trec_human_answer_pool_0314 | What American poet wrote : `` Good fences make good neighbors '' ? | B | A | no |
| 3 | trec_human_answer_pool_0357 | What are values ? | A | A | yes |
| 4 | trec_human_answer_pool_0184 | Where did the saying `` rule of thumb '' come from ? | A | A | yes |
| 5 | trec_human_answer_pool_0393 | Name one of King Henry VIII 's wives . | B | B | yes |

### Rule 47: 5/5

Articulated rule: Label A if and only if the question is a general how/what/which-information query rather than asking for a specific person’s name or identity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0416 | Who sang about Desmond and Molly Jones ? | B | B | yes |
| 2 | trec_human_answer_pool_0222 | What movie has made the most money ? | A | A | yes |
| 3 | trec_human_answer_pool_0450 | Who said : `` Old soldiers never die ; they just fade away '' ? | B | B | yes |
| 4 | trec_human_answer_pool_0255 | What poet wrote : `` ... I have promises to keep , and miles to go before I sleep '' ? | B | B | yes |
| 5 | trec_human_answer_pool_0114 | Who is the leader of Brunei ? | B | B | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if the question begins with “What,” “How,” or “In what year”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0385 | Who is the fastest guitarist ? | B | B | yes |
| 2 | trec_human_answer_pool_0455 | How much do tuberculosis combatting drugs cost ? | A | A | yes |
| 3 | trec_human_answer_pool_0179 | What will a compass do in outer space ? | A | A | yes |
| 4 | trec_human_answer_pool_0171 | What is the first book of the Old Testament ? | A | A | yes |
| 5 | trec_human_answer_pool_0453 | CNN is owned by whom ? | B | B | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if the question begins with “What,” “Which,” or “How”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0189 | Who was the first Prime Minister of Canada ? | B | B | yes |
| 2 | trec_human_answer_pool_0498 | Who 's baby was Sweet Pea on the Popeye cartoon ? | B | B | yes |
| 3 | trec_human_answer_pool_0234 | How do birds find their way back to the same place every year ? | A | A | yes |
| 4 | trec_human_answer_pool_0456 | What 's the closest G2 Spectrum Yellow Dwarf to Earth ? | A | A | yes |
| 5 | trec_human_answer_pool_0365 | What country is home to Heineken beer ? | A | A | yes |

### Rule 50: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, quantity, or other non-person answer; Label B if and only if it asks for a person’s identity or name.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0485 | How many varieties of twins are there ? | A | A | yes |
| 2 | trec_human_answer_pool_0237 | What is a geoscientist ? | A | A | yes |
| 3 | trec_human_answer_pool_0287 | What day is August 13 , 1971 ? | A | A | yes |
| 4 | trec_human_answer_pool_0304 | How does a chick breathe inside an egg ? | A | A | yes |
| 5 | trec_human_answer_pool_0386 | What U.S. President showed a fondness for munching on bee pollen bars ? | B | B | yes |

