# Rule Articulation Workflow: trec_human_answer

Run ID: `trec_human_answer_articulation_workflow_k16_seed0_20260601T212446Z`

Correct prompt-facing rule: Label B iff the question asks for a person or human entity; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.788
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.788
- Rules with all evals correct: 16
- Rules with any eval correct: 50

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
| 1 | 3/5 | Label A if and only if the question asks for a fact about a place, date, quantity, or definition rather than a person or named entity. |
| 2 | 3/5 | Label A if and only if the question asks for a count, date, definition, or other factual information that can be answered directly; label B otherwise. |
| 3 | 5/5 | Label A if and only if the question asks for a general fact, definition, quantity, location, or current/list-style information rather than a specific named person, event, or entity. |
| 4 | 4/5 | Label A if and only if the question asks for a definition, explanation, or general fact rather than identifying a specific named person, object, or entity. |
| 5 | 4/5 | Label A if and only if the question asks for a definition, explanation, or general factual information rather than a specific named entity or person. |
| 6 | 5/5 | Label A if and only if the question asks for a factual answer that is directly stated or definitional, rather than a specific named entity, person, or title. |
| 7 | 4/5 | Label A if and only if the question asks for a definition, explanation, description, or general fact rather than a specific named person, place, work, or event. |
| 8 | 5/5 | Label A if and only if the question asks for a fact, definition, explanation, or how-to answer rather than identifying a specific person or named entity. |
| 9 | 4/5 | Label A if and only if the question asks for a definition, explanation, or general fact rather than a specific named entity or person. |
| 10 | 2/5 | Label A if and only if the question asks for a definition, explanation, or general fact about a thing, rather than asking for a specific person, place, or named entity. |
| 11 | 5/5 | Label A if and only if the question asks about a thing, fact, event, or quantity, while Label B if it asks about a person or people. |
| 12 | 2/5 | Label A if and only if the question asks for the origin, meaning, or explanation of a term or phrase rather than a specific named entity or fact. |
| 13 | 4/5 | Label A if and only if the question asks for a definition, explanation, or general information rather than a specific named person, place, or entity. |
| 14 | 4/5 | Label A if and only if the question asks about a thing, concept, event, or process rather than asking who/which person held a role, identity, or performed an action. |
| 15 | 4/5 | Label A if and only if the question asks for a definition, translation, or factual explanation rather than a specific named person or entity. |
| 16 | 5/5 | Label A if and only if the question asks for a thing, fact, or object rather than a person, and Label B otherwise. |
| 17 | 4/5 | Label A if and only if the question asks for a direct fact or definition rather than identifying a specific person, company, or other named entity. |
| 18 | 3/5 | Label A if and only if the question asks for a count, quantity, or other factual detail rather than a specific named person or entity. |
| 19 | 4/5 | Label A if and only if the question asks for a definition, description, or factual explanation rather than a specific named person, quote source, or entertainment-related trivia. |
| 20 | 2/5 | Label A if and only if the question asks for a fact that can be answered by a single specific entity, value, or definition rather than a list of multiple items or people. |
| 21 | 4/5 | Label A if and only if the question asks about a thing, concept, object, place, or event rather than a specific person. |
| 22 | 4/5 | Label A if and only if the question asks for a definition, explanation, or general fact rather than a specific named entity or person. |
| 23 | 1/5 | Label A if and only if the question asks for a direct factual answer about a specific entity or quantity, rather than asking for a name, list, or broader explanatory/relational fact. |
| 24 | 4/5 | Label A if and only if the question is asking for a factual answer about a thing, person, place, or quantity rather than a specific named entity or identity. |
| 25 | 5/5 | Label A if and only if the question is asking for a definition, explanation, or general fact rather than a specific named entity, person, or title. |
| 26 | 4/5 | Label A if and only if the question asks for a definition, description, or general fact; label B if it asks for a specific named person or entity. |
| 27 | 3/5 | Label A if and only if the question asks for a definition, explanation, or general fact about a thing, rather than asking for a specific named entity, person, place, or answer to a factual trivia question. |
| 28 | 3/5 | Label A if and only if the question asks for a factual, objective answer that can be directly verified; label B if it asks for a subjective, opinion-based, or ambiguous answer. |
| 29 | 3/5 | Label A if and only if the question asks for a factual answer that is not about a named person or entity’s identity, while Label B if it asks who someone is, who did something, or otherwise seeks a specific named person/entity. |
| 30 | 5/5 | Label A if and only if the question asks for a definition, explanation, cause, process, or other factual information rather than a specific named entity or person. |
| 31 | 5/5 | Label A if and only if the question asks for a fact that can be answered directly from general knowledge without needing to identify a specific named person, while Label B if it asks about a particular named person or celebrity. |
| 32 | 4/5 | Label A if and only if the question asks for a definition, explanation, description, or general factual information; label B if it asks for a specific named person, thing, or answer. |
| 33 | 4/5 | Label A if and only if the question asks for a definition, explanation, location, time, or other factual description rather than a specific person or named entity. |
| 34 | 4/5 | Label A if and only if the question asks for a definition, explanation, origin, count, or other factual attribute rather than a specific named person, place, or entity. |
| 35 | 4/5 | Label A if and only if the question asks for a definition, explanation, method, or other non-entity fact; label B if it asks for a specific named person, place, group, or other entity. |
| 36 | 5/5 | Label A if and only if the question asks for a fact about a specific thing, place, time, or explanation, while Label B if it asks for a person, group, or entity. |
| 37 | 3/5 | Label A if and only if the question asks for a fact, definition, count, or other direct information, while Label B if it asks for a person, source, author, or similar named entity. |
| 38 | 3/5 | Label A if and only if the question asks for a definition, explanation, count, or other factual description rather than a specific named person or entity. |
| 39 | 5/5 | Label A if and only if the question asks for a factual answer that is not a named person or title, while Label B if it asks for a person, nickname, or other proper-name-style entity. |
| 40 | 4/5 | Label A if and only if the question asks for a factual definition, description, explanation, or general information rather than asking about a specific person, especially a named individual or a biographical/detail-oriented fact. |
| 41 | 3/5 | Label A if and only if the question asks for a definition, description, or factual explanation rather than a specific named person, place, or title. |
| 42 | 4/5 | Label A if and only if the question asks for a thing, fact, or concept rather than a person. |
| 43 | 5/5 | Label A if and only if the question asks for a definition, explanation, fact, or general information rather than a specific named entity or trivia-style identification. |
| 44 | 5/5 | Label A if and only if the question asks for a thing, place, or concept rather than a person. |
| 45 | 3/5 | Label A if and only if the question asks for a general fact, definition, list, or explanation rather than a specific named person, place, or event. |
| 46 | 5/5 | Label A if and only if the question is about a general fact, definition, or quantity rather than a specific named person, place, organization, or historical entity. |
| 47 | 5/5 | Label A if and only if the question asks about a general fact, definition, explanation, or how-to information rather than identifying a specific named entity or person. |
| 48 | 4/5 | Label A if and only if the question asks for a fact whose answer is a specific named entity, number, or date rather than a person/title-like identity. |
| 49 | 5/5 | Label A if and only if the question asks for a definition, explanation, amount, or other factual information rather than asking who a specific person is or was. |
| 50 | 5/5 | Label A if and only if the question asks for a definition, explanation, quantity, or “how/why” information rather than asking for a specific named person, title, or entity. |

## Detailed Evaluations

### Rule 1: 3/5

Articulated rule: Label A if and only if the question asks for a fact about a place, date, quantity, or definition rather than a person or named entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0375 | In what film did Steven Spielberg 's dog star as the main character 's dog ? | A | B | no |
| 2 | trec_human_answer_pool_0345 | How old do you have to be in order to rent a car in Italy ? | A | A | yes |
| 3 | trec_human_answer_pool_0104 | How many quarters equal a pound ? | A | A | yes |
| 4 | trec_human_answer_pool_0417 | In what ways did Ivan IV support Russian expansion ? | A | B | no |
| 5 | trec_human_answer_pool_0035 | What Polynesian people inhabit New Zealand ? | B | B | yes |

### Rule 2: 3/5

Articulated rule: Label A if and only if the question asks for a count, date, definition, or other factual information that can be answered directly; label B otherwise.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0136 | What is the last name of Lucy and Linus from the Peanut 's comic strip ? | B | A | no |
| 2 | trec_human_answer_pool_0272 | What song did Patti Page set people dancing to in 1950 ? | A | A | yes |
| 3 | trec_human_answer_pool_0128 | What countries have the highest ratio of university students ? | A | A | yes |
| 4 | trec_human_answer_pool_0483 | Who was the first female United States Representative ? | B | A | no |
| 5 | trec_human_answer_pool_0430 | How many home runs did Lou Gehrig have during his career ? | A | A | yes |

### Rule 3: 5/5

Articulated rule: Label A if and only if the question asks for a general fact, definition, quantity, location, or current/list-style information rather than a specific named person, event, or entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0048 | Dialing , 900 , 740-TREE to have a tree planted will cost how much ? | A | A | yes |
| 2 | trec_human_answer_pool_0254 | Why shouldn 't you remove a bee stinger with tweezers ? | A | A | yes |
| 3 | trec_human_answer_pool_0414 | Where are diamonds mined ? | A | A | yes |
| 4 | trec_human_answer_pool_0008 | Who invented the pull-tab opener on cans ? | B | B | yes |
| 5 | trec_human_answer_pool_0362 | What is the Peloponnesian League ? | A | A | yes |

### Rule 4: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or general fact rather than identifying a specific named person, object, or entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0377 | How do I install a tile floor ? | A | A | yes |
| 2 | trec_human_answer_pool_0297 | Whose cupboard was bare ? | B | B | yes |
| 3 | trec_human_answer_pool_0145 | What is the federal minimum wage ? | A | A | yes |
| 4 | trec_human_answer_pool_0124 | What are the two languages of Malta ? | A | A | yes |
| 5 | trec_human_answer_pool_0380 | What Grand Slam golf tournament wasn 't held between 1940 and 1945 ? | A | B | no |

### Rule 5: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or general factual information rather than a specific named entity or person.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0039 | What does a phobophobe fear ? | A | A | yes |
| 2 | trec_human_answer_pool_0193 | What organization has a Security Council ? | B | A | no |
| 3 | trec_human_answer_pool_0010 | What company was the original sponsor of TV 's Superman ? | B | B | yes |
| 4 | trec_human_answer_pool_0157 | What is the Internet2 ? | A | A | yes |
| 5 | trec_human_answer_pool_0177 | What celebrity couple , when going through a divorce , divided their toilet paper into two equal piles ? | B | B | yes |

### Rule 6: 5/5

Articulated rule: Label A if and only if the question asks for a factual answer that is directly stated or definitional, rather than a specific named entity, person, or title.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0258 | What is hydrogen ? | A | A | yes |
| 2 | trec_human_answer_pool_0292 | When was the battle of the Somme fought ? | A | A | yes |
| 3 | trec_human_answer_pool_0361 | What South Vietnamese president was assassinated by his generals in 1963 ? | B | B | yes |
| 4 | trec_human_answer_pool_0410 | Who was the captain of the tanker , Exxon Valdez , involved in the oil spill in Prince William Sound , Alaska , 1989 ? | B | B | yes |
| 5 | trec_human_answer_pool_0472 | What is the 401 , K , plan ? | A | A | yes |

### Rule 7: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, description, or general fact rather than a specific named person, place, work, or event.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0156 | How many times a year does the American Gourd Society publish The Gourd ? | A | B | no |
| 2 | trec_human_answer_pool_0328 | How can you tell when figs are ripe ? | A | A | yes |
| 3 | trec_human_answer_pool_0330 | Who was Buffalo Bill ? | B | B | yes |
| 4 | trec_human_answer_pool_0435 | What is the only animal that can turn its stomach inside out ? | A | A | yes |
| 5 | trec_human_answer_pool_0369 | Why does sound travel quicker through water than air ? | A | A | yes |

### Rule 8: 5/5

Articulated rule: Label A if and only if the question asks for a fact, definition, explanation, or how-to answer rather than identifying a specific person or named entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0411 | Who was Galileo ? | B | B | yes |
| 2 | trec_human_answer_pool_0277 | Who 's the only president buried in Washington | B | B | yes |
| 3 | trec_human_answer_pool_0463 | What English queen had six fingers on one hand ? | B | B | yes |
| 4 | trec_human_answer_pool_0027 | What is the origin of the word ` posh ' ? | A | A | yes |
| 5 | trec_human_answer_pool_0104 | How many quarters equal a pound ? | A | A | yes |

### Rule 9: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or general fact rather than a specific named entity or person.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0103 | What character did Tex Avery first create upon arriving at MGM ? | B | B | yes |
| 2 | trec_human_answer_pool_0122 | Why do girls have to wear training bras ? | A | A | yes |
| 3 | trec_human_answer_pool_0063 | What is Garry Kasparov famous for ? | A | B | no |
| 4 | trec_human_answer_pool_0487 | What is an auto-commentary ? | A | A | yes |
| 5 | trec_human_answer_pool_0340 | How do they find or choose witnesses to an execution ? | A | A | yes |

### Rule 10: 2/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or general fact about a thing, rather than asking for a specific person, place, or named entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0040 | When was Queen Victoria born ? | A | B | no |
| 2 | trec_human_answer_pool_0298 | What part of Britain comprises the Highlands , Central Lowlands , and Southern Uplands ? | A | B | no |
| 3 | trec_human_answer_pool_0300 | What do bats eat ? | A | A | yes |
| 4 | trec_human_answer_pool_0177 | What celebrity couple , when going through a divorce , divided their toilet paper into two equal piles ? | B | B | yes |
| 5 | trec_human_answer_pool_0409 | How do I e-mail someone at aol.com from yahoo.com ? | A | B | no |

### Rule 11: 5/5

Articulated rule: Label A if and only if the question asks about a thing, fact, event, or quantity, while Label B if it asks about a person or people.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0068 | When did CNN go on the air ? | A | A | yes |
| 2 | trec_human_answer_pool_0050 | What NFL team did Vince Lombardi end his coaching career with ? | B | B | yes |
| 3 | trec_human_answer_pool_0300 | What do bats eat ? | A | A | yes |
| 4 | trec_human_answer_pool_0209 | What non-alcoholic syrup is made from pomegranate juice ? | A | A | yes |
| 5 | trec_human_answer_pool_0162 | What South African producer had a 1988 profit of $836 million ? | B | B | yes |

### Rule 12: 2/5

Articulated rule: Label A if and only if the question asks for the origin, meaning, or explanation of a term or phrase rather than a specific named entity or fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0244 | What is the treatment for depression ? | A | B | no |
| 2 | trec_human_answer_pool_0011 | How many people die of tuberculosis yearly ? | A | B | no |
| 3 | trec_human_answer_pool_0413 | Who is the actress Bette Davis once said she wished she looked like ? | B | B | yes |
| 4 | trec_human_answer_pool_0291 | What 's the most popular four-player game of all time ? | A | B | no |
| 5 | trec_human_answer_pool_0482 | What famed clown appeared on an early Howdy Doody Show and insisted that Clarabell be made up as a real clown ? | B | B | yes |

### Rule 13: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or general information rather than a specific named person, place, or entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0086 | Who led the Normans to victory in the Battle of Hastings ? | B | B | yes |
| 2 | trec_human_answer_pool_0046 | What Pulitzer Prize-winning novelist ran for mayor of New York City ? | B | B | yes |
| 3 | trec_human_answer_pool_0183 | Which NBA players had jersey number 0 ? | B | B | yes |
| 4 | trec_human_answer_pool_0023 | Name the ship Beany and Cecil sailed . | A | B | no |
| 5 | trec_human_answer_pool_0482 | What famed clown appeared on an early Howdy Doody Show and insisted that Clarabell be made up as a real clown ? | B | B | yes |

### Rule 14: 4/5

Articulated rule: Label A if and only if the question asks about a thing, concept, event, or process rather than asking who/which person held a role, identity, or performed an action.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0038 | How many calories are there in soy sauce ? | A | A | yes |
| 2 | trec_human_answer_pool_0238 | What would you add to the clay mixture to produce bone china ? | A | A | yes |
| 3 | trec_human_answer_pool_0260 | Which is the only Dick Tracy villain to appear three times ? | B | A | no |
| 4 | trec_human_answer_pool_0140 | What President served for five years , six months and 2 days ? | B | B | yes |
| 5 | trec_human_answer_pool_0362 | What is the Peloponnesian League ? | A | A | yes |

### Rule 15: 4/5

Articulated rule: Label A if and only if the question asks for a definition, translation, or factual explanation rather than a specific named person or entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0388 | What are vermicilli , rigati , zitoni , and tubetti ? | A | A | yes |
| 2 | trec_human_answer_pool_0456 | What 's the closest G2 Spectrum Yellow Dwarf to Earth ? | A | B | no |
| 3 | trec_human_answer_pool_0297 | Whose cupboard was bare ? | B | B | yes |
| 4 | trec_human_answer_pool_0442 | How many colleges are in Wyoming ? | A | A | yes |
| 5 | trec_human_answer_pool_0151 | What is the origin of `` jiggy '' as in getting jiggy with it ? | A | A | yes |

### Rule 16: 5/5

Articulated rule: Label A if and only if the question asks for a thing, fact, or object rather than a person, and Label B otherwise.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0151 | What is the origin of `` jiggy '' as in getting jiggy with it ? | A | A | yes |
| 2 | trec_human_answer_pool_0458 | Who was elected president of South Africa in 1994 ? | B | B | yes |
| 3 | trec_human_answer_pool_0343 | Who was the lawyer for Randy Craft ? | B | B | yes |
| 4 | trec_human_answer_pool_0377 | How do I install a tile floor ? | A | A | yes |
| 5 | trec_human_answer_pool_0240 | What Soviet leader owned a Rolls-Royce ? | B | B | yes |

### Rule 17: 4/5

Articulated rule: Label A if and only if the question asks for a direct fact or definition rather than identifying a specific person, company, or other named entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0155 | What year did Apartheid start ? | A | A | yes |
| 2 | trec_human_answer_pool_0186 | What is the name of a Greek god ? | B | A | no |
| 3 | trec_human_answer_pool_0341 | What is the cause of endangered species ? | A | A | yes |
| 4 | trec_human_answer_pool_0116 | Who portrayed W.C. Fields in the film W.C. Fields and Me ? | B | B | yes |
| 5 | trec_human_answer_pool_0337 | How can I get some free technical information on Electric Vehicle ? | A | A | yes |

### Rule 18: 3/5

Articulated rule: Label A if and only if the question asks for a count, quantity, or other factual detail rather than a specific named person or entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0089 | How do I register a trade name in North Carolina ? | A | B | no |
| 2 | trec_human_answer_pool_0096 | Who was chief engineer of the Starship Enterprise ? | B | B | yes |
| 3 | trec_human_answer_pool_0154 | The Orange Bowl is located in what city ? | A | A | yes |
| 4 | trec_human_answer_pool_0011 | How many people die of tuberculosis yearly ? | A | A | yes |
| 5 | trec_human_answer_pool_0374 | What is the largest city in Connecticut ? | A | B | no |

### Rule 19: 4/5

Articulated rule: Label A if and only if the question asks for a definition, description, or factual explanation rather than a specific named person, quote source, or entertainment-related trivia.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0037 | What diminutive American female gymnast stole the show at the 1984 Olympics ? | B | B | yes |
| 2 | trec_human_answer_pool_0387 | How many member states are in the UN ? | A | A | yes |
| 3 | trec_human_answer_pool_0291 | What 's the most popular four-player game of all time ? | A | B | no |
| 4 | trec_human_answer_pool_0233 | What concerts are held in New York this week ? | A | A | yes |
| 5 | trec_human_answer_pool_0078 | What powdered soft drink mix went into space ? | A | A | yes |

### Rule 20: 2/5

Articulated rule: Label A if and only if the question asks for a fact that can be answered by a single specific entity, value, or definition rather than a list of multiple items or people.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0347 | Who is the prime minister of Australia ? | B | A | no |
| 2 | trec_human_answer_pool_0204 | Who won Oscars for her roles in Gone with the Wind and A Streetcar Named Desire ? | B | A | no |
| 3 | trec_human_answer_pool_0021 | What was Mark Johnson referring to when he said : `` I still can 't believe it- we beat the Russians ? '' | A | A | yes |
| 4 | trec_human_answer_pool_0269 | Who was the first governor of West Virginia ? | B | A | no |
| 5 | trec_human_answer_pool_0258 | What is hydrogen ? | A | A | yes |

### Rule 21: 4/5

Articulated rule: Label A if and only if the question asks about a thing, concept, object, place, or event rather than a specific person.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0470 | What TV comedian worked with White Fang , Black Tooth and Pookie the Lion ? | B | B | yes |
| 2 | trec_human_answer_pool_0095 | What is the virus HIV ? | A | A | yes |
| 3 | trec_human_answer_pool_0079 | Name a novel written by John Steinbeck . | A | B | no |
| 4 | trec_human_answer_pool_0484 | What is artificial intelligence ? | A | A | yes |
| 5 | trec_human_answer_pool_0004 | What are field effect transistors ? | A | A | yes |

### Rule 22: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or general fact rather than a specific named entity or person.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0471 | Who directed Citizen Kane ? | B | B | yes |
| 2 | trec_human_answer_pool_0168 | What writer-journalist made his mark describing colorful Broadway and underworld characters ? | B | B | yes |
| 3 | trec_human_answer_pool_0184 | Where did the saying `` rule of thumb '' come from ? | A | B | no |
| 4 | trec_human_answer_pool_0177 | What celebrity couple , when going through a divorce , divided their toilet paper into two equal piles ? | B | B | yes |
| 5 | trec_human_answer_pool_0151 | What is the origin of `` jiggy '' as in getting jiggy with it ? | A | A | yes |

### Rule 23: 1/5

Articulated rule: Label A if and only if the question asks for a direct factual answer about a specific entity or quantity, rather than asking for a name, list, or broader explanatory/relational fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0338 | What are the most albums sold by one artist or band ? | A | B | no |
| 2 | trec_human_answer_pool_0367 | What are Quaaludes ? | A | B | no |
| 3 | trec_human_answer_pool_0286 | What is a baby lion called ? | A | B | no |
| 4 | trec_human_answer_pool_0003 | Who did Sara Jane Moore try to assassinate ? | B | B | yes |
| 5 | trec_human_answer_pool_0457 | What river in the US is known as the Big Muddy ? | A | B | no |

### Rule 24: 4/5

Articulated rule: Label A if and only if the question is asking for a factual answer about a thing, person, place, or quantity rather than a specific named entity or identity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0288 | What cigar-chewing comedian observed : `` You 're only as old as the woman you feel '' ? | B | B | yes |
| 2 | trec_human_answer_pool_0152 | What was archy , and mehitabel ? | A | A | yes |
| 3 | trec_human_answer_pool_0364 | How many colonies did Germany get to keep after World War I ? | A | A | yes |
| 4 | trec_human_answer_pool_0058 | What spy novelist served as Moscow correspondent for Reuter and The Times of London ? | B | B | yes |
| 5 | trec_human_answer_pool_0149 | What is the name of the highest mountain in Africa ? | A | B | no |

### Rule 25: 5/5

Articulated rule: Label A if and only if the question is asking for a definition, explanation, or general fact rather than a specific named entity, person, or title.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0034 | What Ivy League school plays its home games at Palmer Stadium ? | B | B | yes |
| 2 | trec_human_answer_pool_0451 | What 19th-century painter died in the Marquesas Islands ? | B | B | yes |
| 3 | trec_human_answer_pool_0230 | What future deer hunter portrayed Annie Hall 's neurotic brother , Duane ? | B | B | yes |
| 4 | trec_human_answer_pool_0309 | Who said , `` I shall return . '' during World War Two ? | B | B | yes |
| 5 | trec_human_answer_pool_0428 | How many bones are there in the human hand ? | A | A | yes |

### Rule 26: 4/5

Articulated rule: Label A if and only if the question asks for a definition, description, or general fact; label B if it asks for a specific named person or entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0106 | When was Nostradamus born ? | A | B | no |
| 2 | trec_human_answer_pool_0092 | Where can I find a large list of 5 to 6 letter words ? | A | A | yes |
| 3 | trec_human_answer_pool_0221 | What was the longest war in U.S. history ? | A | A | yes |
| 4 | trec_human_answer_pool_0289 | What was the name of Randy Steven Craft 's lawyer ? | B | B | yes |
| 5 | trec_human_answer_pool_0277 | Who 's the only president buried in Washington | B | B | yes |

### Rule 27: 3/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or general fact about a thing, rather than asking for a specific named entity, person, place, or answer to a factual trivia question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0068 | When did CNN go on the air ? | A | B | no |
| 2 | trec_human_answer_pool_0345 | How old do you have to be in order to rent a car in Italy ? | A | B | no |
| 3 | trec_human_answer_pool_0005 | Who is the creator of `` The Muppets '' ? | B | B | yes |
| 4 | trec_human_answer_pool_0071 | What is the name of the American swimmer who won seven gold medals in the 1972 Olympics ? | B | B | yes |
| 5 | trec_human_answer_pool_0003 | Who did Sara Jane Moore try to assassinate ? | B | B | yes |

### Rule 28: 3/5

Articulated rule: Label A if and only if the question asks for a factual, objective answer that can be directly verified; label B if it asks for a subjective, opinion-based, or ambiguous answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0113 | What country is the largest diamond producer ? | A | A | yes |
| 2 | trec_human_answer_pool_0139 | Who was the oldest U.S. president ? | B | A | no |
| 3 | trec_human_answer_pool_0339 | What caused Shea & Gould to close their L.A. office ? | A | A | yes |
| 4 | trec_human_answer_pool_0073 | Who invented television ? | B | A | no |
| 5 | trec_human_answer_pool_0063 | What is Garry Kasparov famous for ? | A | A | yes |

### Rule 29: 3/5

Articulated rule: Label A if and only if the question asks for a factual answer that is not about a named person or entity’s identity, while Label B if it asks who someone is, who did something, or otherwise seeks a specific named person/entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0475 | What percentage of children between the ages of two and eleven watch ` The Simpsons ' ? | A | A | yes |
| 2 | trec_human_answer_pool_0263 | What fool is not so wise To lose an oath to win a paradise ? | B | A | no |
| 3 | trec_human_answer_pool_0053 | Who made the first airplane ? | B | B | yes |
| 4 | trec_human_answer_pool_0366 | What card company sells Christmas ornaments ? | B | A | no |
| 5 | trec_human_answer_pool_0295 | Which of the following celebrities was not born in Philadelphia ? | B | B | yes |

### Rule 30: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, cause, process, or other factual information rather than a specific named entity or person.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0217 | Who runs Andy Capp 's favorite pub ? | B | B | yes |
| 2 | trec_human_answer_pool_0139 | Who was the oldest U.S. president ? | B | B | yes |
| 3 | trec_human_answer_pool_0296 | What baseball player was known as Charley Hustle ? | B | B | yes |
| 4 | trec_human_answer_pool_0257 | Who founded the Unification Church ? | B | B | yes |
| 5 | trec_human_answer_pool_0319 | What is the population in India ? | A | A | yes |

### Rule 31: 5/5

Articulated rule: Label A if and only if the question asks for a fact that can be answered directly from general knowledge without needing to identify a specific named person, while Label B if it asks about a particular named person or celebrity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0172 | CNN is the abbreviation for what ? | A | A | yes |
| 2 | trec_human_answer_pool_0123 | What Indian tribe is F Troop perpetually doing battle with ? | B | B | yes |
| 3 | trec_human_answer_pool_0299 | What is a fear of speaking ? | A | A | yes |
| 4 | trec_human_answer_pool_0321 | Name of heroine in `` Scruples '' ? | B | B | yes |
| 5 | trec_human_answer_pool_0085 | What is the term for someone who hates mankind ? | A | A | yes |

### Rule 32: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, description, or general factual information; label B if it asks for a specific named person, thing, or answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0330 | Who was Buffalo Bill ? | B | B | yes |
| 2 | trec_human_answer_pool_0301 | What did the ancients call the four great elements ? | A | A | yes |
| 3 | trec_human_answer_pool_0225 | What city is wiener schnitzel named for ? | A | B | no |
| 4 | trec_human_answer_pool_0265 | Who is Malaysia 's 43rd prime minister ? | B | B | yes |
| 5 | trec_human_answer_pool_0054 | Who retired with 755 home runs to his credit ? | B | B | yes |

### Rule 33: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, location, time, or other factual description rather than a specific person or named entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0082 | Who received the Will Rogers Award in 1989 ? | B | B | yes |
| 2 | trec_human_answer_pool_0366 | What card company sells Christmas ornaments ? | B | A | no |
| 3 | trec_human_answer_pool_0413 | Who is the actress Bette Davis once said she wished she looked like ? | B | B | yes |
| 4 | trec_human_answer_pool_0208 | Who wrote the book , `` The Grinch Who Stole Christmas '' ? | B | B | yes |
| 5 | trec_human_answer_pool_0009 | How is it correct to say ` qigong ' ? | A | A | yes |

### Rule 34: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, origin, count, or other factual attribute rather than a specific named person, place, or entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0439 | What company has built more than 2.5 billion little green houses since 1935 ? | B | A | no |
| 2 | trec_human_answer_pool_0282 | Whom did Lauren Bacall marry after her husband Humphrey Bogart died ? | B | B | yes |
| 3 | trec_human_answer_pool_0211 | Who is the `` Queen Mother '' ? | B | B | yes |
| 4 | trec_human_answer_pool_0065 | What baseball player was walked the most times ? | B | B | yes |
| 5 | trec_human_answer_pool_0230 | What future deer hunter portrayed Annie Hall 's neurotic brother , Duane ? | B | B | yes |

### Rule 35: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, method, or other non-entity fact; label B if it asks for a specific named person, place, group, or other entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0233 | What concerts are held in New York this week ? | A | B | no |
| 2 | trec_human_answer_pool_0302 | What schools in the Washington , DC NN NN VBP NN NN NN NN . | B | B | yes |
| 3 | trec_human_answer_pool_0074 | How big is the Electoral College ? | A | A | yes |
| 4 | trec_human_answer_pool_0417 | In what ways did Ivan IV support Russian expansion ? | A | A | yes |
| 5 | trec_human_answer_pool_0464 | Who is the worst US President ever ? | B | B | yes |

### Rule 36: 5/5

Articulated rule: Label A if and only if the question asks for a fact about a specific thing, place, time, or explanation, while Label B if it asks for a person, group, or entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0001 | Name the company that used the line , `` Even your best friend won 't tell you '' in its ad ? | B | B | yes |
| 2 | trec_human_answer_pool_0040 | When was Queen Victoria born ? | A | A | yes |
| 3 | trec_human_answer_pool_0354 | Who is the prophet of the religion of Islam ? | B | B | yes |
| 4 | trec_human_answer_pool_0414 | Where are diamonds mined ? | A | A | yes |
| 5 | trec_human_answer_pool_0420 | What businesses or agencies would do an employment verification ? | B | B | yes |

### Rule 37: 3/5

Articulated rule: Label A if and only if the question asks for a fact, definition, count, or other direct information, while Label B if it asks for a person, source, author, or similar named entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0497 | Who famously rode to warn the people of Massachusetts that the British were coming ? | B | B | yes |
| 2 | trec_human_answer_pool_0000 | What is her husband 's name ? | B | A | no |
| 3 | trec_human_answer_pool_0109 | Who played Emperor Palpatine in Star Wars ? | B | B | yes |
| 4 | trec_human_answer_pool_0281 | What made the Finger Lakes in western New York state ? | A | A | yes |
| 5 | trec_human_answer_pool_0241 | What British monarch 's lap did P.T. Barnum 's Tom Thumb sit in ? | B | A | no |

### Rule 38: 3/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, count, or other factual description rather than a specific named person or entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0150 | What were Babe Ruth 's Christian names ? | B | A | no |
| 2 | trec_human_answer_pool_0116 | Who portrayed W.C. Fields in the film W.C. Fields and Me ? | B | B | yes |
| 3 | trec_human_answer_pool_0154 | The Orange Bowl is located in what city ? | A | A | yes |
| 4 | trec_human_answer_pool_0070 | What are the seven wonders of the world ? | A | A | yes |
| 5 | trec_human_answer_pool_0486 | Who were the only two bald U.S. Presidents ? | B | A | no |

### Rule 39: 5/5

Articulated rule: Label A if and only if the question asks for a factual answer that is not a named person or title, while Label B if it asks for a person, nickname, or other proper-name-style entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0048 | Dialing , 900 , 740-TREE to have a tree planted will cost how much ? | A | A | yes |
| 2 | trec_human_answer_pool_0261 | What is the softest part of the body ? | A | A | yes |
| 3 | trec_human_answer_pool_0384 | Who was the 16th President of the United States ? | B | B | yes |
| 4 | trec_human_answer_pool_0429 | Who was Confucius ? | B | B | yes |
| 5 | trec_human_answer_pool_0311 | What is the best hospital for orthopedics in the country ? | A | A | yes |

### Rule 40: 4/5

Articulated rule: Label A if and only if the question asks for a factual definition, description, explanation, or general information rather than asking about a specific person, especially a named individual or a biographical/detail-oriented fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0344 | Who lived on the shores of the Gitchee Gumee River ? | B | B | yes |
| 2 | trec_human_answer_pool_0328 | How can you tell when figs are ripe ? | A | A | yes |
| 3 | trec_human_answer_pool_0150 | What were Babe Ruth 's Christian names ? | B | B | yes |
| 4 | trec_human_answer_pool_0088 | What William Styron book is about a black preacher who leads a slave revolt ? | A | B | no |
| 5 | trec_human_answer_pool_0418 | What U.S. state has the second-longest coastline ? | A | A | yes |

### Rule 41: 3/5

Articulated rule: Label A if and only if the question asks for a definition, description, or factual explanation rather than a specific named person, place, or title.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0088 | What William Styron book is about a black preacher who leads a slave revolt ? | A | B | no |
| 2 | trec_human_answer_pool_0305 | Who created the comic strip , `` Garfield '' ? | B | B | yes |
| 3 | trec_human_answer_pool_0408 | What is the origin of thank you notes ? | A | A | yes |
| 4 | trec_human_answer_pool_0112 | Where was the first golf course in the United States ? | A | B | no |
| 5 | trec_human_answer_pool_0424 | What is the present Pope named ? | B | B | yes |

### Rule 42: 4/5

Articulated rule: Label A if and only if the question asks for a thing, fact, or concept rather than a person.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0478 | What is an example of a famous rock band from the sixties ? | B | A | no |
| 2 | trec_human_answer_pool_0171 | What is the first book of the Old Testament ? | A | A | yes |
| 3 | trec_human_answer_pool_0475 | What percentage of children between the ages of two and eleven watch ` The Simpsons ' ? | A | A | yes |
| 4 | trec_human_answer_pool_0487 | What is an auto-commentary ? | A | A | yes |
| 5 | trec_human_answer_pool_0125 | Where can I find a review of Nightmare on Elm Street in a film journal ? | A | A | yes |

### Rule 43: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, fact, or general information rather than a specific named entity or trivia-style identification.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0005 | Who is the creator of `` The Muppets '' ? | B | B | yes |
| 2 | trec_human_answer_pool_0020 | What is Shakespeare 's nickname ? | B | B | yes |
| 3 | trec_human_answer_pool_0092 | Where can I find a large list of 5 to 6 letter words ? | A | A | yes |
| 4 | trec_human_answer_pool_0307 | What Louisiana Senator won a seat that had been held by his father and mother ? | B | B | yes |
| 5 | trec_human_answer_pool_0047 | Who is the Queen of Holland ? | B | B | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if the question asks for a thing, place, or concept rather than a person.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0042 | Who developed the first polio vaccine ? | B | B | yes |
| 2 | trec_human_answer_pool_0038 | How many calories are there in soy sauce ? | A | A | yes |
| 3 | trec_human_answer_pool_0098 | Name the story by Chris Van Allsburg in the which a boy tries to become a great sailor ? | A | A | yes |
| 4 | trec_human_answer_pool_0204 | Who won Oscars for her roles in Gone with the Wind and A Streetcar Named Desire ? | B | B | yes |
| 5 | trec_human_answer_pool_0438 | Who else was considered for the role of Luke Skywalker when George Lucas was casting for Star Wars ? | B | B | yes |

### Rule 45: 3/5

Articulated rule: Label A if and only if the question asks for a general fact, definition, list, or explanation rather than a specific named person, place, or event.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0066 | Where does the opera singer Ileana Cotrubas come from ? | A | B | no |
| 2 | trec_human_answer_pool_0352 | What is the full name of the man who invented the multicolored game cube that has 42.3 quintillion potential combinations ? | B | B | yes |
| 3 | trec_human_answer_pool_0205 | What state is the Filenes store located in ? | A | B | no |
| 4 | trec_human_answer_pool_0415 | Which college did Dikembe Mutombo attend ? | B | B | yes |
| 5 | trec_human_answer_pool_0022 | Which German president was pressured into appointing Hitler chancellor in 1933 ? | B | B | yes |

### Rule 46: 5/5

Articulated rule: Label A if and only if the question is about a general fact, definition, or quantity rather than a specific named person, place, organization, or historical entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0336 | What daughter of Henry VIII and Anne Boleyn became queen of England ? | B | B | yes |
| 2 | trec_human_answer_pool_0314 | What American poet wrote : `` Good fences make good neighbors '' ? | B | B | yes |
| 3 | trec_human_answer_pool_0357 | What are values ? | A | A | yes |
| 4 | trec_human_answer_pool_0184 | Where did the saying `` rule of thumb '' come from ? | A | A | yes |
| 5 | trec_human_answer_pool_0393 | Name one of King Henry VIII 's wives . | B | B | yes |

### Rule 47: 5/5

Articulated rule: Label A if and only if the question asks about a general fact, definition, explanation, or how-to information rather than identifying a specific named entity or person.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0416 | Who sang about Desmond and Molly Jones ? | B | B | yes |
| 2 | trec_human_answer_pool_0222 | What movie has made the most money ? | A | A | yes |
| 3 | trec_human_answer_pool_0450 | Who said : `` Old soldiers never die ; they just fade away '' ? | B | B | yes |
| 4 | trec_human_answer_pool_0255 | What poet wrote : `` ... I have promises to keep , and miles to go before I sleep '' ? | B | B | yes |
| 5 | trec_human_answer_pool_0114 | Who is the leader of Brunei ? | B | B | yes |

### Rule 48: 4/5

Articulated rule: Label A if and only if the question asks for a fact whose answer is a specific named entity, number, or date rather than a person/title-like identity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0385 | Who is the fastest guitarist ? | B | B | yes |
| 2 | trec_human_answer_pool_0455 | How much do tuberculosis combatting drugs cost ? | A | A | yes |
| 3 | trec_human_answer_pool_0179 | What will a compass do in outer space ? | A | A | yes |
| 4 | trec_human_answer_pool_0171 | What is the first book of the Old Testament ? | A | B | no |
| 5 | trec_human_answer_pool_0453 | CNN is owned by whom ? | B | B | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, amount, or other factual information rather than asking who a specific person is or was.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0189 | Who was the first Prime Minister of Canada ? | B | B | yes |
| 2 | trec_human_answer_pool_0498 | Who 's baby was Sweet Pea on the Popeye cartoon ? | B | B | yes |
| 3 | trec_human_answer_pool_0234 | How do birds find their way back to the same place every year ? | A | A | yes |
| 4 | trec_human_answer_pool_0456 | What 's the closest G2 Spectrum Yellow Dwarf to Earth ? | A | A | yes |
| 5 | trec_human_answer_pool_0365 | What country is home to Heineken beer ? | A | A | yes |

### Rule 50: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, quantity, or “how/why” information rather than asking for a specific named person, title, or entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_human_answer_pool_0485 | How many varieties of twins are there ? | A | A | yes |
| 2 | trec_human_answer_pool_0237 | What is a geoscientist ? | A | A | yes |
| 3 | trec_human_answer_pool_0287 | What day is August 13 , 1971 ? | A | A | yes |
| 4 | trec_human_answer_pool_0304 | How does a chick breathe inside an egg ? | A | A | yes |
| 5 | trec_human_answer_pool_0386 | What U.S. President showed a fondness for munching on bee pollen bars ? | B | B | yes |

