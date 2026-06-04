# Rule Articulation Workflow: trec_number_or_date_answer

Run ID: `production_gpt54_20260602T001915Z_articulation_20260602T011542Z_base_trec_number_or_date_answer_seed0`

Correct prompt-facing rule: Label B iff the question asks for a number, quantity, date, or other numeric answer; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.812
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.812
- Rules with all evals correct: 23
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
| 1 | 5/5 | Label A if and only if the question does not explicitly ask for a number, year, month, day, or amount. |
| 2 | 2/5 | Label A if and only if the question begins with “what” or “who”; otherwise label B. |
| 3 | 5/5 | Label A if and only if the question asks for a definition, explanation, identification, or source of information rather than a numeric quantity or amount. |
| 4 | 4/5 | Label A if and only if the question asks for a definition/identification of a specific person, thing, or title, rather than asking for a date, number, population, or other numeric/time-based fact. |
| 5 | 4/5 | Label A if and only if the question asks for a definition, identity, or named entity/class, rather than a numeric value, date, time, rate, amount, or other measurable fact. |
| 6 | 5/5 | Label A if and only if the question asks for a person, thing, group, or explanation/definition, rather than a numeric quantity, amount, length, weight, cost, percentage, or count. |
| 7 | 5/5 | Label A if and only if the question asks for a person, place, thing, or method/name, rather than a numeric quantity, amount, year, or measurement. |
| 8 | 4/5 | Label A if and only if the question begins with “what” (including “what does/what is/what singer/what sign/etc.”); otherwise label B. |
| 9 | 4/5 | Label A if and only if the question asks for a definition, explanation, or identity, rather than a specific numeric fact, date, amount, or record. |
| 10 | 1/5 | Label A if and only if the question is open-ended and not asking for a specific numeric/date-style fact; otherwise label B. |
| 11 | 4/5 | Label A if and only if the question begins with a wh-word other than “when/how many/how often/how tall/in what year”; otherwise label B. |
| 12 | 3/5 | Label A if and only if the question asks for a definition, identity, explanation, manufacturer, or expansion of a term/person, rather than a numeric/date/measurement fact. |
| 13 | 4/5 | Label A if and only if the question asks for a person, title/name, or other specific entity, rather than a numeric/measure/time-based fact. |
| 14 | 2/5 | Label A if and only if the question asks for a definition, synonym, identity, or name of something, rather than a date, number, age, or other quantitative fact. |
| 15 | 4/5 | Label A if and only if the question asks for a definition, identity, inventor, role, or qualitative description, rather than a specific date, number, amount, probability, or day. |
| 16 | 4/5 | Label A if and only if the question asks for a definition, explanation, identity, or meaning, rather than a specific fact like a date, number, or measurement. |
| 17 | 2/5 | Label B if and only if the question begins with an explicit wh-word/phrase asking for a specific fact (e.g. what year, how many, when, how often); otherwise label A. |
| 18 | 1/5 | Label A if and only if the question is a “what”-type question rather than a “how many/how big” or “when” question. |
| 19 | 5/5 | Label A if and only if the question asks for a person, thing, or definition, rather than for a number, date, speed, or day. |
| 20 | 2/5 | Label A if and only if the question does not begin with “What” or “How many/how tall/about how many/what year/what population”-style quantity requests; otherwise label B. |
| 21 | 5/5 | Label A if and only if the question asks for a person, thing, name, or definition rather than a number, date, time, or quantity. |
| 22 | 4/5 | Label A if and only if the question asks for an explanation, identity, or method rather than a specific numeric/date measurement or count. |
| 23 | 5/5 | Label A if and only if the question is a wh-question other than a “how many” or “when” question. |
| 24 | 2/5 | Label A if and only if the question begins with “what,” “in what,” “whose,” “who,” or a person-name + verb form, rather than asking “when/what year/how many/what day/what’s the first day.” |
| 25 | 4/5 | Label B if and only if the question asks for a numerical quantity, measurement, rate, or amount; otherwise label A. |
| 26 | 5/5 | Label B if and only if the question explicitly asks for a number, amount, size, distance, date, or other measurable quantity. |
| 27 | 4/5 | Label A if and only if the question asks for a person, place/country/city, game, or named term/title, rather than a number, date, time, or other quantitative value. |
| 28 | 5/5 | Label A if and only if the question asks for a specific named entity or definition, rather than a numeric quantity, date, rate, length, or population. |
| 29 | 5/5 | Label A if and only if the question asks for an entity, definition, reason, or category name rather than a numeric/date/amount value. |
| 30 | 4/5 | Label A if and only if the question asks for a definition, identity, or name/list, rather than a date, time, quantity, or measurement. |
| 31 | 5/5 | Label B if and only if the question asks for a number, amount, or year; otherwise label A. |
| 32 | 3/5 | Label A if and only if the question is missing essential information or is otherwise incomplete/underspecified; otherwise label B. |
| 33 | 5/5 | Label B if and only if the question asks for a number, amount, duration, frequency, year, or other quantitative value. |
| 34 | 5/5 | Label A if and only if the question asks for a person, thing, place, or comparison/identity, rather than a numeric measurement or a date/time. |
| 35 | 5/5 | Label B if and only if the question asks for a number, amount, date, height, weight, population, or other quantitative value. |
| 36 | 5/5 | Label B if and only if the question asks for a numeric value, date, time, amount, or measurement; otherwise label A. |
| 37 | 3/5 | Label A if and only if the question begins with a wh-word other than “How” or “When” (e.g. What/Who/Where); otherwise label B. |
| 38 | 5/5 | Label B if and only if the question asks for a number, amount, or date/time; otherwise label A. |
| 39 | 5/5 | Label A if and only if the question asks for an identity, name, meaning, type, place, or organization; label B if and only if it asks for a number, amount, date, time, distance, speed, or size. |
| 40 | 5/5 | Label A if and only if the question asks for a person, thing, place, title, or definition, rather than asking for a numeric amount, date, duration, length, or quantity. |
| 41 | 4/5 | Label A if and only if the question asks for a definition, identity, or named fact, rather than a numeric amount, date/year, age, or payment/value. |
| 42 | 5/5 | Label A if and only if the question begins with a wh-word other than “how many/much” or “when”; otherwise label B. |
| 43 | 5/5 | Label B if and only if the question asks for a number, amount, distance, speed, date, or count; otherwise label A. |
| 44 | 5/5 | Label A if and only if the question begins with “what,” “where,” or “how” but not with a quantity/age/size sense of “how”; otherwise label B. |
| 45 | 5/5 | Label B if and only if the question asks for a number, amount, size, length, time, or other quantitative measurement. |
| 46 | 3/5 | Label A if and only if the question begins with “What” or “Who”; otherwise label B. |
| 47 | 4/5 | Label A if and only if the question is subjective, vague, or asks for a name/identity/explanation rather than a specific numeric fact. |
| 48 | 5/5 | Label A if and only if the question asks for a name, term, kind, or identity rather than a numeric value, date/time, percentage/rate, or duration. |
| 49 | 4/5 | Label A if and only if the question is asking for an explanation, meaning, reason, identity, or qualitative description rather than a specific date, number, amount, or other precise factual value. |
| 50 | 4/5 | Label A if and only if the question asks for a definition, identity, name, location, or type of thing, rather than a numeric amount, date, age, distance, speed, frequency, or other measurable value. |

## Detailed Evaluations

### Rule 1: 5/5

Articulated rule: Label A if and only if the question does not explicitly ask for a number, year, month, day, or amount.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0375 | Where is the massive North Korean nuclear complex located ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0345 | What is the origin of the candy cane at Christmas ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0104 | What is the name of the inventor of silly putty ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0417 | What is `` the computer for the rest of us '' ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0035 | What date did man first land on the moon ? | B | B | yes |

### Rule 2: 2/5

Articulated rule: Label A if and only if the question begins with “what” or “who”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0136 | What month did the Edmund Fitzgerald sink ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0272 | Who is Dear Abby ? | A | B | no |
| 3 | trec_number_or_date_answer_pool_0128 | What TV series featured Neal , a martini-drinking St. Bernard ? | A | B | no |
| 4 | trec_number_or_date_answer_pool_0483 | On average , how many miles are there to the moon ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0430 | Where can I find up-to-date coastal ocean surface temperature information , preferably along North America and the Caribbean ? | A | B | no |

### Rule 3: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, identification, or source of information rather than a numeric quantity or amount.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0048 | What is the capital of Italy ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0254 | Who manufactures the software , `` PhotoShop '' ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0414 | What group starred in the movie Rock Around the Clock ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0008 | How many years make up a lustrum ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0362 | Who was the first African American to play for the Brooklyn Dodgers ? | A | A | yes |

### Rule 4: 4/5

Articulated rule: Label A if and only if the question asks for a definition/identification of a specific person, thing, or title, rather than asking for a date, number, population, or other numeric/time-based fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0377 | Who invented the pull-tab opener on cans ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0297 | What is the federal minimum wage ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0145 | How does one correctly pronounce ` qigong ' ? | A | B | no |
| 4 | trec_number_or_date_answer_pool_0124 | What kind of people took part in Shays ' Rebellion in Massachusetts in 1787 ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0380 | What 's an auberge in France ? | A | A | yes |

### Rule 5: 4/5

Articulated rule: Label A if and only if the question asks for a definition, identity, or named entity/class, rather than a numeric value, date, time, rate, amount, or other measurable fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0039 | What building are British monarchs crowned in ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0193 | How many bones are there in the human hand ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0010 | What is the student population at the University of Massachusetts in Amherst ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0157 | What Shakespeare play opens with the line : `` Now is the winter of our discontent.. . '' ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0177 | What geological time do we live in ? | B | A | no |

### Rule 6: 5/5

Articulated rule: Label A if and only if the question asks for a person, thing, group, or explanation/definition, rather than a numeric quantity, amount, length, weight, cost, percentage, or count.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0258 | What 's the distinction of U.S. Supreme Court Justice Thurgood Marshall ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0292 | What country was A Terrible Beauty to Leon Uris ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0361 | How many web servers are there ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0410 | How many colors are there in the spectrum ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0472 | What is a fear of being cold ? | A | A | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the question asks for a person, place, thing, or method/name, rather than a numeric quantity, amount, year, or measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0156 | Who made the rotary engine automobile ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0328 | What sign is the best love match for a horoscope sign ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0330 | How many copies of an album must be sold for it to be a gold album ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0435 | What racehorse won an Associated Press poll as the greatest horse of the 20th century ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0369 | Who runs Andy Capp 's favorite pub ? | A | A | yes |

### Rule 8: 4/5

Articulated rule: Label A if and only if the question begins with “what” (including “what does/what is/what singer/what sign/etc.”); otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0411 | How many cards is each player dealt in Contract Bridge ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0277 | When did the Chernobyl nuclear accident occur ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0463 | What is the sales tax rate in New York ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0027 | What 's the home of the Rockettes ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0104 | What is the name of the inventor of silly putty ? | A | B | no |

### Rule 9: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, or identity, rather than a specific numeric fact, date, amount, or record.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0103 | In what year did China and the Republic of Korea establish diplomatic relations ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0122 | Who protects DC Comics ' realm of dreams ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0063 | What is genocide ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0487 | Who is Olive Oyl 's brother ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0340 | What 's the farthest planet from the sun ? | A | B | no |

### Rule 10: 1/5

Articulated rule: Label A if and only if the question is open-ended and not asking for a specific numeric/date-style fact; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0040 | What flag flies over Wake Island ? | A | B | no |
| 2 | trec_number_or_date_answer_pool_0298 | What non-alcoholic syrup is made from pomegranate juice ? | A | B | no |
| 3 | trec_number_or_date_answer_pool_0300 | What two vegetables are combined in succotash ? | A | B | no |
| 4 | trec_number_or_date_answer_pool_0177 | What geological time do we live in ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0409 | What was the orca 's name that died of a fungal infection at Sea World ? | A | B | no |

### Rule 11: 4/5

Articulated rule: Label A if and only if the question begins with a wh-word other than “when/how many/how often/how tall/in what year”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0068 | What is the abbreviation of the National Bureau of Investigation ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0050 | What month , date , and year did Charles I die ? | B | A | no |
| 3 | trec_number_or_date_answer_pool_0300 | What two vegetables are combined in succotash ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0209 | What does the T.S. stand for in T.S. Eliot 's name ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0162 | How many meters are in a mile ? | B | B | yes |

### Rule 12: 3/5

Articulated rule: Label A if and only if the question asks for a definition, identity, explanation, manufacturer, or expansion of a term/person, rather than a numeric/date/measurement fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0244 | What famous British actor lost his voice after an operation in 1966 ? | A | B | no |
| 2 | trec_number_or_date_answer_pool_0011 | Whose video is titled Shape Up with Arnold ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0413 | When was the NFL established ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0291 | What animal migrates the farthest ? | A | B | no |
| 5 | trec_number_or_date_answer_pool_0482 | How much folic acid should an expectant mother get daily ? | B | B | yes |

### Rule 13: 4/5

Articulated rule: Label A if and only if the question asks for a person, title/name, or other specific entity, rather than a numeric/measure/time-based fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0086 | How large is Missouri 's population ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0046 | When did CNN go on the air ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0183 | When was the Triangle Shirtwaist fire ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0023 | What is the weather like on the moon ? | A | B | no |
| 5 | trec_number_or_date_answer_pool_0482 | How much folic acid should an expectant mother get daily ? | B | B | yes |

### Rule 14: 2/5

Articulated rule: Label A if and only if the question asks for a definition, synonym, identity, or name of something, rather than a date, number, age, or other quantitative fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0038 | Where is Burma ? | A | B | no |
| 2 | trec_number_or_date_answer_pool_0238 | What happened to Moon Maiden ? | A | B | no |
| 3 | trec_number_or_date_answer_pool_0260 | How many earthworms are in a single pasture ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0140 | What is the diameter of a golf ball ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0362 | Who was the first African American to play for the Brooklyn Dodgers ? | A | B | no |

### Rule 15: 4/5

Articulated rule: Label A if and only if the question asks for a definition, identity, inventor, role, or qualitative description, rather than a specific date, number, amount, probability, or day.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0388 | What is the website for the USA journal ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0456 | What 1956 Grace Metalious novel was on the best-seller list for two years ? | A | B | no |
| 3 | trec_number_or_date_answer_pool_0297 | What is the federal minimum wage ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0442 | Where can I find information on becoming a journalist ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0151 | What does SIDS stand for ? | A | A | yes |

### Rule 16: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, identity, or meaning, rather than a specific fact like a date, number, or measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0151 | What does SIDS stand for ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0458 | What is the recomended age to switch a child from a crib to a bed ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0343 | How long does it take the moon to revolve around the Earth ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0377 | Who invented the pull-tab opener on cans ? | A | B | no |
| 5 | trec_number_or_date_answer_pool_0240 | How high is the city of Denver ? | B | B | yes |

### Rule 17: 2/5

Articulated rule: Label B if and only if the question begins with an explicit wh-word/phrase asking for a specific fact (e.g. what year, how many, when, how often); otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0155 | What was the name of the Titanic 's captain ? | A | B | no |
| 2 | trec_number_or_date_answer_pool_0186 | What is the population of Nigeria ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0341 | What singer 's theme song was When the Moon Comes over the Mountain ? | A | B | no |
| 4 | trec_number_or_date_answer_pool_0116 | How much in miles is a ten K run ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0337 | What format was VHS 's main competition ? | A | B | no |

### Rule 18: 1/5

Articulated rule: Label A if and only if the question is a “what”-type question rather than a “how many/how big” or “when” question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0089 | Who was the first Prime Minister of Canada ? | A | B | no |
| 2 | trec_number_or_date_answer_pool_0096 | What is the average cost for four years of medical school ? | B | A | no |
| 3 | trec_number_or_date_answer_pool_0154 | Garry Kasparov plays what game ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0011 | Whose video is titled Shape Up with Arnold ? | A | B | no |
| 5 | trec_number_or_date_answer_pool_0374 | Name the country which Honecker lived in . | A | B | no |

### Rule 19: 5/5

Articulated rule: Label A if and only if the question asks for a person, thing, or definition, rather than for a number, date, speed, or day.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0037 | What is the size of Argentina ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0387 | What country has the port of Haifa ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0291 | What animal migrates the farthest ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0233 | What is the world 's deadliest infectious disease ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0078 | What is a fear of hell ? | A | A | yes |

### Rule 20: 2/5

Articulated rule: Label A if and only if the question does not begin with “What” or “How many/how tall/about how many/what year/what population”-style quantity requests; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0347 | What year was the Mona Lisa painted ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0204 | When did North Carolina enter the union ? | B | A | no |
| 3 | trec_number_or_date_answer_pool_0021 | Who is the actress known for her role in the movie `` Gypsy '' ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0269 | How much salt is in the oceans ? | B | A | no |
| 5 | trec_number_or_date_answer_pool_0258 | What 's the distinction of U.S. Supreme Court Justice Thurgood Marshall ? | A | B | no |

### Rule 21: 5/5

Articulated rule: Label A if and only if the question asks for a person, thing, name, or definition rather than a number, date, time, or quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0470 | How much did Lucy Van Pelt originally charge for psychiatric sessions ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0095 | What landmark Italian restaurant can be found at 239 West 48th Street , New York City ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0079 | What does the word LASER mean ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0484 | What country was Erich Honecker the leader of ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0004 | Why is Jane Goodall famous ? | A | A | yes |

### Rule 22: 4/5

Articulated rule: Label A if and only if the question asks for an explanation, identity, or method rather than a specific numeric/date measurement or count.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0471 | How many points is a bullseye worth in darts ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0168 | How many colored squares are there on a Rubik 's Cube ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0184 | What letter adorns the flag of Rwanda ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0177 | What geological time do we live in ? | B | A | no |
| 5 | trec_number_or_date_answer_pool_0151 | What does SIDS stand for ? | A | A | yes |

### Rule 23: 5/5

Articulated rule: Label A if and only if the question is a wh-question other than a “how many” or “when” question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0338 | Who gave us the `` Rolling Writer '' ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0367 | Who won the Superbowl in ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0286 | What 's the name of the actress who starred in the movie , `` Silence of the Lambs '' ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0003 | When was Nostradamus born ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0457 | Which came first , according to Genesis 1 : 2 : 22 - the chicken or the egg ? | A | A | yes |

### Rule 24: 2/5

Articulated rule: Label A if and only if the question begins with “what,” “in what,” “whose,” “who,” or a person-name + verb form, rather than asking “when/what year/how many/what day/what’s the first day.”

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0288 | What does an average daycare provider get paid in New England ? | B | A | no |
| 2 | trec_number_or_date_answer_pool_0152 | Where in the United States do people live the longest ? | A | B | no |
| 3 | trec_number_or_date_answer_pool_0364 | What are the only players eligible to score points in Roller Derby called ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0058 | What will the California gas tax be in the year 2000 ? | B | A | no |
| 5 | trec_number_or_date_answer_pool_0149 | What company markets a shampoo `` for brunettes only '' ? | A | A | yes |

### Rule 25: 4/5

Articulated rule: Label B if and only if the question asks for a numerical quantity, measurement, rate, or amount; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0034 | What year did the United States abolish the draft ? | B | A | no |
| 2 | trec_number_or_date_answer_pool_0451 | What is the average age a horse lives ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0230 | How far is it from Denver to Aspen ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0309 | How fast is alcohol absorbed ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0428 | What is a Canada two-penny black ? | A | A | yes |

### Rule 26: 5/5

Articulated rule: Label B if and only if the question explicitly asks for a number, amount, size, distance, date, or other measurable quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0106 | What is Margaret Thatcher known for ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0092 | Why is Indiglo called Indiglo ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0221 | Who was chief engineer of the Starship Enterprise ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0289 | How many films are made by the major studios in a year ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0277 | When did the Chernobyl nuclear accident occur ? | B | B | yes |

### Rule 27: 4/5

Articulated rule: Label A if and only if the question asks for a person, place/country/city, game, or named term/title, rather than a number, date, time, or other quantitative value.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0068 | What is the abbreviation of the National Bureau of Investigation ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0345 | What is the origin of the candy cane at Christmas ? | A | B | no |
| 3 | trec_number_or_date_answer_pool_0005 | How many species of sharks are there ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0071 | How long do you have to pay back debt after claiming chapter 11 bankruptcy ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0003 | When was Nostradamus born ? | B | B | yes |

### Rule 28: 5/5

Articulated rule: Label A if and only if the question asks for a specific named entity or definition, rather than a numeric quantity, date, rate, length, or population.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0113 | What is a group of turkeys called ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0139 | What year was the Avery Dennison company founded ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0339 | What is the procedure called for drilling a hole in your skull to acheive a higher consciousness ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0073 | How tall is the giraffe ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0063 | What is genocide ? | A | A | yes |

### Rule 29: 5/5

Articulated rule: Label A if and only if the question asks for an entity, definition, reason, or category name rather than a numeric/date/amount value.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0475 | What was the first TV set to include a remote control ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0263 | What percentage of Americans own their homes ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0053 | How many times more than 3 | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0366 | What year did Oklahoma become a state ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0295 | What year was the first automobile manufactured ? | B | B | yes |

### Rule 30: 4/5

Articulated rule: Label A if and only if the question asks for a definition, identity, or name/list, rather than a date, time, quantity, or measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0217 | How many boys play the game in Winslow Homer 's 1872 painting Snap the Whip ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0139 | What year was the Avery Dennison company founded ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0296 | How much did the minimum wage amount to in 1991 ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0257 | When was Richard Nixon born ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0319 | Who stopped making diary entries on May 31 , 1669 , because he thought he was going blind ? | A | B | no |

### Rule 31: 5/5

Articulated rule: Label B if and only if the question asks for a number, amount, or year; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0172 | What 's the main vegetable in vichyssoise ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0123 | How much pizza do Americans eat in a day ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0299 | Where is the Virtual Desk Reference ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0321 | How many cables support the main span of the Golden Gate Bridge ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0085 | What is the full name of the man who invented the multicolored game cube that has 42.3 quintillion potential combinations ? | A | A | yes |

### Rule 32: 3/5

Articulated rule: Label A if and only if the question is missing essential information or is otherwise incomplete/underspecified; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0330 | How many copies of an album must be sold for it to be a gold album ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0301 | How does salt melt ice and snow ? | A | B | no |
| 3 | trec_number_or_date_answer_pool_0225 | What does a pedometer measure ? | A | B | no |
| 4 | trec_number_or_date_answer_pool_0265 | When did Hitler come to power in Germany ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0054 | When is the official first day of summer ? | B | B | yes |

### Rule 33: 5/5

Articulated rule: Label B if and only if the question asks for a number, amount, duration, frequency, year, or other quantitative value.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0082 | How fast must a spacecraft travel to escape Earth 's gravity ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0366 | What year did Oklahoma become a state ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0413 | When was the NFL established ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0208 | How many people are taller than 7 feet ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0009 | Where is McCarren Airport ? | A | A | yes |

### Rule 34: 5/5

Articulated rule: Label A if and only if the question asks for a person, thing, place, or comparison/identity, rather than a numeric measurement or a date/time.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0439 | How many CDs has Garth Brooks sold ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0282 | What is the population of Mexico ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0211 | How many rows of whiskers does a cat have ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0065 | How many logarithmic scales are there on a slide rule ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0230 | How far is it from Denver to Aspen ? | B | B | yes |

### Rule 35: 5/5

Articulated rule: Label B if and only if the question asks for a number, amount, date, height, weight, population, or other quantitative value.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0233 | What is the world 's deadliest infectious disease ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0302 | How much caffeine is in a 16 oz cup of coffee ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0074 | How does rabies spread ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0417 | What is `` the computer for the rest of us '' ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0464 | How much was the minimum wage in 1991 ? | B | B | yes |

### Rule 36: 5/5

Articulated rule: Label B if and only if the question asks for a numeric value, date, time, amount, or measurement; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0001 | How much snow equals an inch of rain ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0040 | What flag flies over Wake Island ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0354 | When is Father 's Day ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0414 | What group starred in the movie Rock Around the Clock ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0420 | What is Judy Garland 's date of birth ? | B | B | yes |

### Rule 37: 3/5

Articulated rule: Label A if and only if the question begins with a wh-word other than “How” or “When” (e.g. What/Who/Where); otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0497 | How long does it take for your body to restore blood after you donate your blood ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0000 | What 's the American dollar equivalent for 8 pounds in the U.K. ? | B | A | no |
| 3 | trec_number_or_date_answer_pool_0109 | When does the average teenager first have intercourse ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0281 | What major airline has the best safety record in the world ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0241 | What is the length of the coastline of the state of Alaska ? | B | A | no |

### Rule 38: 5/5

Articulated rule: Label B if and only if the question asks for a number, amount, or date/time; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0150 | How many revolutions does a standard LP make in three minutes ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0116 | How much in miles is a ten K run ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0154 | Garry Kasparov plays what game ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0070 | What 's Mrs. Bridges 's job on TV 's Upstairs , Downstairs ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0486 | How many people in the USA say their number one source of information is the newspaper ? | B | B | yes |

### Rule 39: 5/5

Articulated rule: Label A if and only if the question asks for an identity, name, meaning, type, place, or organization; label B if and only if it asks for a number, amount, date, time, distance, speed, or size.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0048 | What is the capital of Italy ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0261 | What film ends with the line : `` This is Mrs. Norman Maine '' ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0384 | What time of year is air travel the heaviest ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0429 | Hitler came to power in Germany in what year ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0311 | What is SVHS ? | A | A | yes |

### Rule 40: 5/5

Articulated rule: Label A if and only if the question asks for a person, thing, place, title, or definition, rather than asking for a numeric amount, date, duration, length, or quantity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0344 | When did Spielberg direct `` Jaws '' ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0328 | What sign is the best love match for a horoscope sign ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0150 | How many revolutions does a standard LP make in three minutes ? | B | B | yes |
| 4 | trec_number_or_date_answer_pool_0088 | Where in the Bible does it tell about Jesus Christ 's brothers and sisters ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0418 | What is the name given to a group of geese ? | A | A | yes |

### Rule 41: 4/5

Articulated rule: Label A if and only if the question asks for a definition, identity, or named fact, rather than a numeric amount, date/year, age, or payment/value.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0088 | Where in the Bible does it tell about Jesus Christ 's brothers and sisters ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0305 | How many consecutive baseball games did Lou Gehrig play ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0408 | Who is the actress Bette Davis once said she wished she looked like ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0112 | What does IQ stand for ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0424 | What chapter of the Bible has the most verses ? | B | A | no |

### Rule 42: 5/5

Articulated rule: Label A if and only if the question begins with a wh-word other than “how many/much” or “when”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0478 | How many different kinds of ice cream are there ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0171 | What company produces Spumante ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0475 | What was the first TV set to include a remote control ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0487 | Who is Olive Oyl 's brother ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0125 | Who was president in 1913 ? | A | A | yes |

### Rule 43: 5/5

Articulated rule: Label B if and only if the question asks for a number, amount, distance, speed, date, or count; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0005 | How many species of sharks are there ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0020 | When did President Kennedy , Lee Harvey Oswald , and Jack Ruby all die ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0092 | Why is Indiglo called Indiglo ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0307 | What is the pig population of the world ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0047 | When was Dick Clark born ? | B | B | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if the question begins with “what,” “where,” or “how” but not with a quantity/age/size sense of “how”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0042 | How many more weeks of winter are there if a ground hog sees his shadow ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0038 | Where is Burma ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0098 | What is HDLC ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0204 | When did North Carolina enter the union ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0438 | In which year was the cartoon character Chilly Willy created ? | B | B | yes |

### Rule 45: 5/5

Articulated rule: Label B if and only if the question asks for a number, amount, size, length, time, or other quantitative measurement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0066 | Tell me what city the Kentucky Horse Park is near ? | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0352 | When was the internal combustion engine developed ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0205 | What new middle school was built in Philadelphia , Pennsylvania last year ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0415 | What year was the NAACP founded ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0022 | How many visitors go to the Vatican each year ? | B | B | yes |

### Rule 46: 3/5

Articulated rule: Label A if and only if the question begins with “What” or “Who”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0336 | What is the chemical reactivity of neon ? | B | A | no |
| 2 | trec_number_or_date_answer_pool_0314 | How many pairs of legs does a lobster have ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0357 | Who killed more people , Hitler or Stalin ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0184 | What letter adorns the flag of Rwanda ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0393 | What is the conversion rate between dollars and pounds ? | B | A | no |

### Rule 47: 4/5

Articulated rule: Label A if and only if the question is subjective, vague, or asks for a name/identity/explanation rather than a specific numeric fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0416 | How many John Deere tractors have been manufactured ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0222 | Who invented the radio ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0450 | When did they canonize the Bible ? | B | A | no |
| 4 | trec_number_or_date_answer_pool_0255 | What day was Pearl Harbor attacked in 1942 ? | B | B | yes |
| 5 | trec_number_or_date_answer_pool_0114 | How big is the Electoral College ? | B | B | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if the question asks for a name, term, kind, or identity rather than a numeric value, date/time, percentage/rate, or duration.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0385 | What is the population of Mozambique ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0455 | What is the greatest hiking Web site ? | A | A | yes |
| 3 | trec_number_or_date_answer_pool_0179 | What 's another word that means `` knows all '' ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0171 | What company produces Spumante ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0453 | How many liberty bells have there been ? | B | B | yes |

### Rule 49: 4/5

Articulated rule: Label A if and only if the question is asking for an explanation, meaning, reason, identity, or qualitative description rather than a specific date, number, amount, or other precise factual value.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0189 | When was Franklin D. Roosevelt stricken with polio ? | B | B | yes |
| 2 | trec_number_or_date_answer_pool_0498 | How many letters appear with the numbers 2 to 9 on a telephone dial ? | B | B | yes |
| 3 | trec_number_or_date_answer_pool_0234 | Who did Napolean defeat at Jena and Auerstadt ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0456 | What 1956 Grace Metalious novel was on the best-seller list for two years ? | A | B | no |
| 5 | trec_number_or_date_answer_pool_0365 | How do I impress a guy ? | A | A | yes |

### Rule 50: 4/5

Articulated rule: Label A if and only if the question asks for a definition, identity, name, location, or type of thing, rather than a numeric amount, date, age, distance, speed, frequency, or other measurable value.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_number_or_date_answer_pool_0485 | Name the person who burst through the screen in the Lite beer commercials . | A | A | yes |
| 2 | trec_number_or_date_answer_pool_0237 | How can I trace my family roots ? | A | B | no |
| 3 | trec_number_or_date_answer_pool_0287 | What is the origin of the peace symbol ? | A | A | yes |
| 4 | trec_number_or_date_answer_pool_0304 | What program do I need to run a .tbk file ? | A | A | yes |
| 5 | trec_number_or_date_answer_pool_0386 | How many home runs did Lou Gehrig have during his career ? | B | B | yes |

