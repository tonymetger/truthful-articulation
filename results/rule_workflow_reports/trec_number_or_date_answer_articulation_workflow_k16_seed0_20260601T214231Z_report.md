# Rule Articulation Workflow: trec_number_or_date_answer

Run ID: `trec_number_or_date_answer_articulation_workflow_k16_seed0_20260601T214231Z`

Correct prompt-facing rule: Label B iff the question asks for a number, quantity, date, or other numeric answer; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.900
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.900
- Rules with all evals correct: 33
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
| 1 | 5/5 | Label A if and only if the question asks for a definition, explanation, or general fact rather than a specific date, number, or other exact value. |
| 2 | 4/5 | Label A if and only if the question asks for a definition, explanation, or identification of a thing/person, rather than a specific factual value like a date, number, rate, or conversion. |
| 3 | 5/5 | Label A if and only if the question asks for a definition, explanation, identification, or other non-numeric fact; label B if it asks for a quantity, count, measurement, or conversion. |
| 4 | 4/5 | Label A if and only if the question asks for a definition, identification, or explanation of a thing/person/event, rather than a specific factual value like a date, number, or location. |
| 5 | 4/5 | Label A if and only if the question asks for a definition, entity, or specific fact, while Label B if it asks for a quantity, date, time, number, measurement, or other numeric answer. |
| 6 | 5/5 | Label A if and only if the question asks for a name, identity, explanation, or other non-numeric fact; label B if it asks for a quantity, amount, measurement, percentage, or other numeric answer. |
| 7 | 5/5 | Label A if and only if the question asks for a person, place, thing, or how-to explanation rather than a numeric quantity, date, or other measurable fact. |
| 8 | 5/5 | Label A if and only if the question asks for a definition, origin, identity, or other factual explanation rather than a numeric amount, date, or measurement. |
| 9 | 4/5 | Label A if and only if the question asks for a definition, explanation, or identity of a thing/person, rather than a specific factual quantity, date, or measurement. |
| 10 | 4/5 | Label A if and only if the question asks for a person, thing, reason, or explanation rather than a numeric fact like a count, size, date, population, length, or score. |
| 11 | 5/5 | Label A if and only if the question asks for a description, definition, explanation, list, or other non-time/non-number factual information; label B if it asks for a specific date, year, quantity, measurement, or other numeric answer. |
| 12 | 5/5 | Label A if and only if the question asks for a definition, explanation, expansion, or identification of a thing/person; label B if it asks for a specific factual value such as a date, number, measurement, or other exact quantity. |
| 13 | 5/5 | Label A if and only if the question asks for a person, place, thing, or event-specific fact rather than a numeric quantity, time, measurement, or count. |
| 14 | 5/5 | Label A if and only if the question asks for a definition, description, or identification of a thing/person, while Label B if it asks for a date, time, number, or other factual measurement. |
| 15 | 3/5 | Label A if and only if the question asks for a definition, identification, or explanation of a thing or person rather than a specific fact like a date, number, or measurement. |
| 16 | 3/5 | Label A if and only if the question asks for a definition, explanation, or description rather than a specific fact like a date, number, or person. |
| 17 | 3/5 | Label A if and only if the question asks for an explanation, reason, or descriptive fact rather than a specific date, number, or other short factual answer. |
| 18 | 5/5 | Label A if and only if the question asks for a definition, explanation, or identification of a named thing; label B if it asks for a count, date, or other specific factual quantity. |
| 19 | 5/5 | Label A if and only if the question asks for a specific fact or entity, while Label B if it asks for a count, date, time, or other numeric/quantitative answer. |
| 20 | 5/5 | Label A if and only if the question asks for a definition, origin, pronunciation, meaning, or other non-numeric fact rather than a specific number, date, measurement, or count. |
| 21 | 5/5 | Label A if and only if the question asks for a definition, meaning, name, or identity of something; label B if it asks for a specific fact such as a date, number, time, or other measurable detail. |
| 22 | 3/5 | Label A if and only if the question is asking for an explanation, reason, comparison, or other non-factual/subjective information rather than a direct factual answer. |
| 23 | 4/5 | Label A if and only if the question asks for a specific fact about a named entity or object, while Label B if it asks for a count, quantity, or other broad numerical total. |
| 24 | 5/5 | Label A if and only if the question asks for a thing, person, place, or concept; label B if it asks for a date, year, time, number, or other quantitative answer. |
| 25 | 5/5 | Label A if and only if the question asks for a definition, description, name, or identification of something; label B if it asks for a quantity, measurement, conversion, or other numeric/factual amount. |
| 26 | 5/5 | Label A if and only if the question asks for a definition, explanation, or other non-numeric fact, while Label B if it asks for a specific quantity, date, measurement, or count. |
| 27 | 5/5 | Label A if and only if the question asks for a named entity, fact, or description rather than a number, date, or other quantitative answer. |
| 28 | 5/5 | Label A if and only if the question asks for a named entity, definition, or identification rather than a numeric quantity or measurement. |
| 29 | 4/5 | Label A if and only if the question asks for a definition, identity, explanation, or general fact, rather than a specific number, date, count, or other quantitative answer. |
| 30 | 4/5 | Label A if and only if the question asks for a definition, explanation, or identification of a thing’s nature or meaning rather than a specific fact like a date, number, or other measurable detail. |
| 31 | 3/5 | Label A if and only if the question asks for a definition, explanation, or other descriptive/qualitative information rather than a specific fact like a date, number, or named entity. |
| 32 | 5/5 | Label A if and only if the question asks about a specific named entity or fact, while Label B if it asks for a count, date, amount, or other numeric/quantitative answer. |
| 33 | 5/5 | Label A if and only if the question asks for a named entity, title, or specific factual object rather than a number, date, or quantity. |
| 34 | 5/5 | Label A if and only if the question asks for a person, thing, or definition rather than a specific numeric/date/measurement answer. |
| 35 | 5/5 | Label A if and only if the question asks for a name, definition, or other non-numeric fact; label B if it asks for a quantity, amount, date, or other numeric answer. |
| 36 | 4/5 | Label A if and only if the question asks about a definition, explanation, or non-numeric fact; label B if it asks for a specific numeric value, date, count, or measurement. |
| 37 | 5/5 | Label A if and only if the question asks for an entity’s identity or name, while Label B if it asks for a date, number, amount, or other factual quantity. |
| 38 | 5/5 | Label A if and only if the question asks for a definition, identification, or explanation rather than a specific fact like a date, number, or other exact measurement. |
| 39 | 5/5 | Label A if and only if the question asks for a named entity, definition, or identification rather than a numeric fact or quantity. |
| 40 | 5/5 | Label A if and only if the question asks for a definition, expansion, or identification of a named thing; label B if it asks for a numeric amount, date, measurement, or other factual quantity. |
| 41 | 5/5 | Label A if and only if the question asks for a definition, explanation, or identification of something, while Label B if it asks for a specific factual value such as a date, amount, year, or quantity. |
| 42 | 4/5 | Label A if and only if the question asks for a definition, explanation, identification, or other factual description rather than a specific date, number, or count. |
| 43 | 5/5 | Label A if and only if the question asks for a definition, explanation, or general fact rather than a specific quantity, date, distance, or count. |
| 44 | 5/5 | Label A if and only if the question asks for a definition, identification, or explanation rather than a specific fact like a number, date, age, population, or count. |
| 45 | 5/5 | Label A if and only if the question asks for a definition, explanation, identity, or other factual information that is not a direct quantity/measurement/count/size/time answer. |
| 46 | 2/5 | Label A if and only if the question asks for a definition, identification, or explanation of a thing or person rather than a specific numeric fact like time, distance, date, amount, or population. |
| 47 | 5/5 | Label A if and only if the question asks for a name, identity, definition, location, or other factual description rather than a numeric quantity, measurement, date, age, or count. |
| 48 | 5/5 | Label A if and only if the question asks for a definition, identification, or list of a thing’s name/type, rather than a numeric, date, rate, or other factual quantity. |
| 49 | 3/5 | Label A if and only if the question asks for an explanation, definition, reason, or subjective/qualitative description rather than a specific fact, number, date, or name. |
| 50 | 5/5 | Label A if and only if the question asks for a definition, identity, location, or other factual entity, while Label B if it asks for a quantity, measurement, time, or other numeric answer. |

## Detailed Evaluations

### Rule 1: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or general fact rather than a specific date, number, or other exact value.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0375 | Where is the massive North Korean nuclear complex located ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0345 | What is the origin of the candy cane at Christmas ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0104 | What is the name of the inventor of silly putty ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0417 | What is `` the computer for the rest of us '' ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0035 | What date did man first land on the moon ? | B | B | yes |

### Rule 2: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or identification of a thing/person, rather than a specific factual value like a date, number, rate, or conversion.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0136 | What month did the Edmund Fitzgerald sink ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0272 | Who is Dear Abby ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0128 | What TV series featured Neal , a martini-drinking St. Bernard ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0483 | On average , how many miles are there to the moon ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0430 | Where can I find up-to-date coastal ocean surface temperature information , preferably along North America and the Caribbean ? | A | B | no |

### Rule 3: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, identification, or other non-numeric fact; label B if it asks for a quantity, count, measurement, or conversion.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0048 | What is the capital of Italy ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0254 | Who manufactures the software , `` PhotoShop '' ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0414 | What group starred in the movie Rock Around the Clock ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0008 | How many years make up a lustrum ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0362 | Who was the first African American to play for the Brooklyn Dodgers ? | A | A | yes |

### Rule 4: 4/5

Articulated rule: Label A if and only if the question asks for a definition, identification, or explanation of a thing/person/event, rather than a specific factual value like a date, number, or location.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0377 | Who invented the pull-tab opener on cans ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0297 | What is the federal minimum wage ? | B | A | no |
| 3 | trec_number_or_date_answer_pool_0145 | How does one correctly pronounce ` qigong ' ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0124 | What kind of people took part in Shays ' Rebellion in Massachusetts in 1787 ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0380 | What 's an auberge in France ? | A | A | yes |

### Rule 5: 4/5

Articulated rule: Label A if and only if the question asks for a definition, entity, or specific fact, while Label B if it asks for a quantity, date, time, number, measurement, or other numeric answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0039 | What building are British monarchs crowned in ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0193 | How many bones are there in the human hand ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0010 | What is the student population at the University of Massachusetts in Amherst ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0157 | What Shakespeare play opens with the line : `` Now is the winter of our discontent.. . '' ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0177 | What geological time do we live in ? | B | A | no |

### Rule 6: 5/5

Articulated rule: Label A if and only if the question asks for a name, identity, explanation, or other non-numeric fact; label B if it asks for a quantity, amount, measurement, percentage, or other numeric answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0258 | What 's the distinction of U.S. Supreme Court Justice Thurgood Marshall ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0292 | What country was A Terrible Beauty to Leon Uris ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0361 | How many web servers are there ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0410 | How many colors are there in the spectrum ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0472 | What is a fear of being cold ? | A | A | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the question asks for a person, place, thing, or how-to explanation rather than a numeric quantity, date, or other measurable fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0156 | Who made the rotary engine automobile ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0328 | What sign is the best love match for a horoscope sign ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0330 | How many copies of an album must be sold for it to be a gold album ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0435 | What racehorse won an Associated Press poll as the greatest horse of the 20th century ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0369 | Who runs Andy Capp 's favorite pub ? | A | A | yes |

### Rule 8: 5/5

Articulated rule: Label A if and only if the question asks for a definition, origin, identity, or other factual explanation rather than a numeric amount, date, or measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0411 | How many cards is each player dealt in Contract Bridge ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0277 | When did the Chernobyl nuclear accident occur ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0463 | What is the sales tax rate in New York ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0027 | What 's the home of the Rockettes ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0104 | What is the name of the inventor of silly putty ? | A | A | yes |

### Rule 9: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or identity of a thing/person, rather than a specific factual quantity, date, or measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0103 | In what year did China and the Republic of Korea establish diplomatic relations ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0122 | Who protects DC Comics ' realm of dreams ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0063 | What is genocide ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0487 | Who is Olive Oyl 's brother ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0340 | What 's the farthest planet from the sun ? | A | B | no |

### Rule 10: 4/5

Articulated rule: Label A if and only if the question asks for a person, thing, reason, or explanation rather than a numeric fact like a count, size, date, population, length, or score.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0040 | What flag flies over Wake Island ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0298 | What non-alcoholic syrup is made from pomegranate juice ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0300 | What two vegetables are combined in succotash ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0177 | What geological time do we live in ? | B | A | no |
| 5 | trec_number_or_date_answer_pool_0409 | What was the orca 's name that died of a fungal infection at Sea World ? | A | A | yes |

### Rule 11: 5/5

Articulated rule: Label A if and only if the question asks for a description, definition, explanation, list, or other non-time/non-number factual information; label B if it asks for a specific date, year, quantity, measurement, or other numeric answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0068 | What is the abbreviation of the National Bureau of Investigation ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0050 | What month , date , and year did Charles I die ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0300 | What two vegetables are combined in succotash ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0209 | What does the T.S. stand for in T.S. Eliot 's name ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0162 | How many meters are in a mile ? | B | B | yes |

### Rule 12: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, expansion, or identification of a thing/person; label B if it asks for a specific factual value such as a date, number, measurement, or other exact quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0244 | What famous British actor lost his voice after an operation in 1966 ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0011 | Whose video is titled Shape Up with Arnold ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0413 | When was the NFL established ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0291 | What animal migrates the farthest ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0482 | How much folic acid should an expectant mother get daily ? | B | B | yes |

### Rule 13: 5/5

Articulated rule: Label A if and only if the question asks for a person, place, thing, or event-specific fact rather than a numeric quantity, time, measurement, or count.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0086 | How large is Missouri 's population ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0046 | When did CNN go on the air ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0183 | When was the Triangle Shirtwaist fire ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0023 | What is the weather like on the moon ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0482 | How much folic acid should an expectant mother get daily ? | B | B | yes |

### Rule 14: 5/5

Articulated rule: Label A if and only if the question asks for a definition, description, or identification of a thing/person, while Label B if it asks for a date, time, number, or other factual measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0038 | Where is Burma ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0238 | What happened to Moon Maiden ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0260 | How many earthworms are in a single pasture ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0140 | What is the diameter of a golf ball ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0362 | Who was the first African American to play for the Brooklyn Dodgers ? | A | A | yes |

### Rule 15: 3/5

Articulated rule: Label A if and only if the question asks for a definition, identification, or explanation of a thing or person rather than a specific fact like a date, number, or measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0388 | What is the website for the USA journal ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0456 | What 1956 Grace Metalious novel was on the best-seller list for two years ? | A | B | no |
| 3 | trec_number_or_date_answer_pool_0297 | What is the federal minimum wage ? | B | A | no |
| 4 | trec_number_or_date_answer_pool_0442 | Where can I find information on becoming a journalist ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0151 | What does SIDS stand for ? | A | A | yes |

### Rule 16: 3/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or description rather than a specific fact like a date, number, or person.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0151 | What does SIDS stand for ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0458 | What is the recomended age to switch a child from a crib to a bed ? | B | A | no |
| 3 | trec_number_or_date_answer_pool_0343 | How long does it take the moon to revolve around the Earth ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0377 | Who invented the pull-tab opener on cans ? | A | B | no |
| 5 | trec_number_or_date_answer_pool_0240 | How high is the city of Denver ? | B | B | yes |

### Rule 17: 3/5

Articulated rule: Label A if and only if the question asks for an explanation, reason, or descriptive fact rather than a specific date, number, or other short factual answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0155 | What was the name of the Titanic 's captain ? | A | B | no |
| 2 | trec_number_or_date_answer_pool_0186 | What is the population of Nigeria ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0341 | What singer 's theme song was When the Moon Comes over the Mountain ? | A | B | no |
| 4 | trec_number_or_date_answer_pool_0116 | How much in miles is a ten K run ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0337 | What format was VHS 's main competition ? | A | A | yes |

### Rule 18: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or identification of a named thing; label B if it asks for a count, date, or other specific factual quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0089 | Who was the first Prime Minister of Canada ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0096 | What is the average cost for four years of medical school ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0154 | Garry Kasparov plays what game ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0011 | Whose video is titled Shape Up with Arnold ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0374 | Name the country which Honecker lived in . | A | A | yes |

### Rule 19: 5/5

Articulated rule: Label A if and only if the question asks for a specific fact or entity, while Label B if it asks for a count, date, time, or other numeric/quantitative answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0037 | What is the size of Argentina ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0387 | What country has the port of Haifa ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0291 | What animal migrates the farthest ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0233 | What is the world 's deadliest infectious disease ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0078 | What is a fear of hell ? | A | A | yes |

### Rule 20: 5/5

Articulated rule: Label A if and only if the question asks for a definition, origin, pronunciation, meaning, or other non-numeric fact rather than a specific number, date, measurement, or count.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0347 | What year was the Mona Lisa painted ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0204 | When did North Carolina enter the union ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0021 | Who is the actress known for her role in the movie `` Gypsy '' ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0269 | How much salt is in the oceans ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0258 | What 's the distinction of U.S. Supreme Court Justice Thurgood Marshall ? | A | A | yes |

### Rule 21: 5/5

Articulated rule: Label A if and only if the question asks for a definition, meaning, name, or identity of something; label B if it asks for a specific fact such as a date, number, time, or other measurable detail.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0470 | How much did Lucy Van Pelt originally charge for psychiatric sessions ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0095 | What landmark Italian restaurant can be found at 239 West 48th Street , New York City ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0079 | What does the word LASER mean ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0484 | What country was Erich Honecker the leader of ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0004 | Why is Jane Goodall famous ? | A | A | yes |

### Rule 22: 3/5

Articulated rule: Label A if and only if the question is asking for an explanation, reason, comparison, or other non-factual/subjective information rather than a direct factual answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0471 | How many points is a bullseye worth in darts ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0168 | How many colored squares are there on a Rubik 's Cube ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0184 | What letter adorns the flag of Rwanda ? | A | B | no |
| 4 | trec_number_or_date_answer_pool_0177 | What geological time do we live in ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0151 | What does SIDS stand for ? | A | B | no |

### Rule 23: 4/5

Articulated rule: Label A if and only if the question asks for a specific fact about a named entity or object, while Label B if it asks for a count, quantity, or other broad numerical total.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0338 | Who gave us the `` Rolling Writer '' ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0367 | Who won the Superbowl in ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0286 | What 's the name of the actress who starred in the movie , `` Silence of the Lambs '' ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0003 | When was Nostradamus born ? | B | A | no |
| 5 | trec_number_or_date_answer_pool_0457 | Which came first , according to Genesis 1 : 2 : 22 - the chicken or the egg ? | A | A | yes |

### Rule 24: 5/5

Articulated rule: Label A if and only if the question asks for a thing, person, place, or concept; label B if it asks for a date, year, time, number, or other quantitative answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0288 | What does an average daycare provider get paid in New England ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0152 | Where in the United States do people live the longest ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0364 | What are the only players eligible to score points in Roller Derby called ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0058 | What will the California gas tax be in the year 2000 ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0149 | What company markets a shampoo `` for brunettes only '' ? | A | A | yes |

### Rule 25: 5/5

Articulated rule: Label A if and only if the question asks for a definition, description, name, or identification of something; label B if it asks for a quantity, measurement, conversion, or other numeric/factual amount.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0034 | What year did the United States abolish the draft ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0451 | What is the average age a horse lives ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0230 | How far is it from Denver to Aspen ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0309 | How fast is alcohol absorbed ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0428 | What is a Canada two-penny black ? | A | A | yes |

### Rule 26: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or other non-numeric fact, while Label B if it asks for a specific quantity, date, measurement, or count.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0106 | What is Margaret Thatcher known for ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0092 | Why is Indiglo called Indiglo ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0221 | Who was chief engineer of the Starship Enterprise ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0289 | How many films are made by the major studios in a year ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0277 | When did the Chernobyl nuclear accident occur ? | B | B | yes |

### Rule 27: 5/5

Articulated rule: Label A if and only if the question asks for a named entity, fact, or description rather than a number, date, or other quantitative answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0068 | What is the abbreviation of the National Bureau of Investigation ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0345 | What is the origin of the candy cane at Christmas ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0005 | How many species of sharks are there ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0071 | How long do you have to pay back debt after claiming chapter 11 bankruptcy ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0003 | When was Nostradamus born ? | B | B | yes |

### Rule 28: 5/5

Articulated rule: Label A if and only if the question asks for a named entity, definition, or identification rather than a numeric quantity or measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0113 | What is a group of turkeys called ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0139 | What year was the Avery Dennison company founded ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0339 | What is the procedure called for drilling a hole in your skull to acheive a higher consciousness ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0073 | How tall is the giraffe ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0063 | What is genocide ? | A | A | yes |

### Rule 29: 4/5

Articulated rule: Label A if and only if the question asks for a definition, identity, explanation, or general fact, rather than a specific number, date, count, or other quantitative answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0475 | What was the first TV set to include a remote control ? | A | B | no |
| 2 | trec_number_or_date_answer_pool_0263 | What percentage of Americans own their homes ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0053 | How many times more than 3 | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0366 | What year did Oklahoma become a state ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0295 | What year was the first automobile manufactured ? | B | B | yes |

### Rule 30: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or identification of a thing’s nature or meaning rather than a specific fact like a date, number, or other measurable detail.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0217 | How many boys play the game in Winslow Homer 's 1872 painting Snap the Whip ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0139 | What year was the Avery Dennison company founded ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0296 | How much did the minimum wage amount to in 1991 ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0257 | When was Richard Nixon born ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0319 | Who stopped making diary entries on May 31 , 1669 , because he thought he was going blind ? | A | B | no |

### Rule 31: 3/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or other descriptive/qualitative information rather than a specific fact like a date, number, or named entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0172 | What 's the main vegetable in vichyssoise ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0123 | How much pizza do Americans eat in a day ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0299 | Where is the Virtual Desk Reference ? | A | B | no |
| 4 | trec_number_or_date_answer_pool_0321 | How many cables support the main span of the Golden Gate Bridge ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0085 | What is the full name of the man who invented the multicolored game cube that has 42.3 quintillion potential combinations ? | A | B | no |

### Rule 32: 5/5

Articulated rule: Label A if and only if the question asks about a specific named entity or fact, while Label B if it asks for a count, date, amount, or other numeric/quantitative answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0330 | How many copies of an album must be sold for it to be a gold album ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0301 | How does salt melt ice and snow ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0225 | What does a pedometer measure ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0265 | When did Hitler come to power in Germany ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0054 | When is the official first day of summer ? | B | B | yes |

### Rule 33: 5/5

Articulated rule: Label A if and only if the question asks for a named entity, title, or specific factual object rather than a number, date, or quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0082 | How fast must a spacecraft travel to escape Earth 's gravity ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0366 | What year did Oklahoma become a state ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0413 | When was the NFL established ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0208 | How many people are taller than 7 feet ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0009 | Where is McCarren Airport ? | A | A | yes |

### Rule 34: 5/5

Articulated rule: Label A if and only if the question asks for a person, thing, or definition rather than a specific numeric/date/measurement answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0439 | How many CDs has Garth Brooks sold ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0282 | What is the population of Mexico ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0211 | How many rows of whiskers does a cat have ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0065 | How many logarithmic scales are there on a slide rule ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0230 | How far is it from Denver to Aspen ? | B | B | yes |

### Rule 35: 5/5

Articulated rule: Label A if and only if the question asks for a name, definition, or other non-numeric fact; label B if it asks for a quantity, amount, date, or other numeric answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0233 | What is the world 's deadliest infectious disease ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0302 | How much caffeine is in a 16 oz cup of coffee ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0074 | How does rabies spread ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0417 | What is `` the computer for the rest of us '' ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0464 | How much was the minimum wage in 1991 ? | B | B | yes |

### Rule 36: 4/5

Articulated rule: Label A if and only if the question asks about a definition, explanation, or non-numeric fact; label B if it asks for a specific numeric value, date, count, or measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0001 | How much snow equals an inch of rain ? | B | A | no |
| 2 | trec_number_or_date_answer_pool_0040 | What flag flies over Wake Island ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0354 | When is Father 's Day ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0414 | What group starred in the movie Rock Around the Clock ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0420 | What is Judy Garland 's date of birth ? | B | B | yes |

### Rule 37: 5/5

Articulated rule: Label A if and only if the question asks for an entity’s identity or name, while Label B if it asks for a date, number, amount, or other factual quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0497 | How long does it take for your body to restore blood after you donate your blood ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0000 | What 's the American dollar equivalent for 8 pounds in the U.K. ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0109 | When does the average teenager first have intercourse ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0281 | What major airline has the best safety record in the world ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0241 | What is the length of the coastline of the state of Alaska ? | B | B | yes |

### Rule 38: 5/5

Articulated rule: Label A if and only if the question asks for a definition, identification, or explanation rather than a specific fact like a date, number, or other exact measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0150 | How many revolutions does a standard LP make in three minutes ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0116 | How much in miles is a ten K run ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0154 | Garry Kasparov plays what game ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0070 | What 's Mrs. Bridges 's job on TV 's Upstairs , Downstairs ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0486 | How many people in the USA say their number one source of information is the newspaper ? | B | B | yes |

### Rule 39: 5/5

Articulated rule: Label A if and only if the question asks for a named entity, definition, or identification rather than a numeric fact or quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0048 | What is the capital of Italy ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0261 | What film ends with the line : `` This is Mrs. Norman Maine '' ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0384 | What time of year is air travel the heaviest ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0429 | Hitler came to power in Germany in what year ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0311 | What is SVHS ? | A | A | yes |

### Rule 40: 5/5

Articulated rule: Label A if and only if the question asks for a definition, expansion, or identification of a named thing; label B if it asks for a numeric amount, date, measurement, or other factual quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0344 | When did Spielberg direct `` Jaws '' ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0328 | What sign is the best love match for a horoscope sign ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0150 | How many revolutions does a standard LP make in three minutes ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0088 | Where in the Bible does it tell about Jesus Christ 's brothers and sisters ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0418 | What is the name given to a group of geese ? | A | A | yes |

### Rule 41: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or identification of something, while Label B if it asks for a specific factual value such as a date, amount, year, or quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0088 | Where in the Bible does it tell about Jesus Christ 's brothers and sisters ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0305 | How many consecutive baseball games did Lou Gehrig play ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0408 | Who is the actress Bette Davis once said she wished she looked like ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0112 | What does IQ stand for ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0424 | What chapter of the Bible has the most verses ? | B | B | yes |

### Rule 42: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, identification, or other factual description rather than a specific date, number, or count.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0478 | How many different kinds of ice cream are there ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0171 | What company produces Spumante ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0475 | What was the first TV set to include a remote control ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0487 | Who is Olive Oyl 's brother ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0125 | Who was president in 1913 ? | A | B | no |

### Rule 43: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or general fact rather than a specific quantity, date, distance, or count.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0005 | How many species of sharks are there ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0020 | When did President Kennedy , Lee Harvey Oswald , and Jack Ruby all die ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0092 | Why is Indiglo called Indiglo ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0307 | What is the pig population of the world ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0047 | When was Dick Clark born ? | B | B | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if the question asks for a definition, identification, or explanation rather than a specific fact like a number, date, age, population, or count.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0042 | How many more weeks of winter are there if a ground hog sees his shadow ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0038 | Where is Burma ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0098 | What is HDLC ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0204 | When did North Carolina enter the union ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0438 | In which year was the cartoon character Chilly Willy created ? | B | B | yes |

### Rule 45: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, identity, or other factual information that is not a direct quantity/measurement/count/size/time answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0066 | Tell me what city the Kentucky Horse Park is near ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0352 | When was the internal combustion engine developed ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0205 | What new middle school was built in Philadelphia , Pennsylvania last year ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0415 | What year was the NAACP founded ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0022 | How many visitors go to the Vatican each year ? | B | B | yes |

### Rule 46: 2/5

Articulated rule: Label A if and only if the question asks for a definition, identification, or explanation of a thing or person rather than a specific numeric fact like time, distance, date, amount, or population.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0336 | What is the chemical reactivity of neon ? | B | A | no |
| 2 | trec_number_or_date_answer_pool_0314 | How many pairs of legs does a lobster have ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0357 | Who killed more people , Hitler or Stalin ? | A | B | no |
| 4 | trec_number_or_date_answer_pool_0184 | What letter adorns the flag of Rwanda ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0393 | What is the conversion rate between dollars and pounds ? | B | A | no |

### Rule 47: 5/5

Articulated rule: Label A if and only if the question asks for a name, identity, definition, location, or other factual description rather than a numeric quantity, measurement, date, age, or count.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0416 | How many John Deere tractors have been manufactured ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0222 | Who invented the radio ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0450 | When did they canonize the Bible ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0255 | What day was Pearl Harbor attacked in 1942 ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0114 | How big is the Electoral College ? | B | B | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if the question asks for a definition, identification, or list of a thing’s name/type, rather than a numeric, date, rate, or other factual quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0385 | What is the population of Mozambique ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0455 | What is the greatest hiking Web site ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0179 | What 's another word that means `` knows all '' ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0171 | What company produces Spumante ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0453 | How many liberty bells have there been ? | B | B | yes |

### Rule 49: 3/5

Articulated rule: Label A if and only if the question asks for an explanation, definition, reason, or subjective/qualitative description rather than a specific fact, number, date, or name.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0189 | When was Franklin D. Roosevelt stricken with polio ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0498 | How many letters appear with the numbers 2 to 9 on a telephone dial ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0234 | Who did Napolean defeat at Jena and Auerstadt ? | A | B | no |
| 4 | trec_number_or_date_answer_pool_0456 | What 1956 Grace Metalious novel was on the best-seller list for two years ? | A | B | no |
| 5 | trec_number_or_date_answer_pool_0365 | How do I impress a guy ? | A | A | yes |

### Rule 50: 5/5

Articulated rule: Label A if and only if the question asks for a definition, identity, location, or other factual entity, while Label B if it asks for a quantity, measurement, time, or other numeric answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0485 | Name the person who burst through the screen in the Lite beer commercials . | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0237 | How can I trace my family roots ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0287 | What is the origin of the peace symbol ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0304 | What program do I need to run a .tbk file ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0386 | How many home runs did Lou Gehrig have during his career ? | B | B | yes |

