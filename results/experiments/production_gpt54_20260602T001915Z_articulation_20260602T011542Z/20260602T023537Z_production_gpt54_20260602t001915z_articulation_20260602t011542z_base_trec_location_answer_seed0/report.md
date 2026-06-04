# Rule Articulation Workflow: trec_location_answer

Run ID: `production_gpt54_20260602T001915Z_articulation_20260602T011542Z_base_trec_location_answer_seed0`

Correct prompt-facing rule: Label B iff the question asks for a location; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.756
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.756
- Rules with all evals correct: 17
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
| 1 | 4/5 | Label A if and only if the question asks for a person, organization/team, language, garment, or operating system, rather than asking for a place, landmark, natural feature, direction, or other location-like/physical answer. |
| 2 | 4/5 | Label A if and only if the question does not ask for a specific place or location; otherwise label B. |
| 3 | 2/5 | Label A if and only if the question contains obvious tokenization/quotation/POS-tag noise or other malformed wording; otherwise label B. |
| 4 | 2/5 | Label A if and only if the question word is who, what, or what’s; otherwise label B. |
| 5 | 3/5 | Label A if and only if the question begins with “How,” “Who,” or “Which”; otherwise label B. |
| 6 | 4/5 | Label B if and only if the question explicitly asks for a place or country/city/location; otherwise label A. |
| 7 | 5/5 | Label A if and only if the question is not asking for a location/place; Label B if and only if it is asking about a place or location. |
| 8 | 2/5 | Label A if and only if the question begins with “What” or “Who”; otherwise label B. |
| 9 | 5/5 | Label A if and only if the question is asking for a definition, explanation, manner, quantity, or specific identifying fact other than a location/nationality/political region; Label B if only if it asks for a place, country, state, city, nationality, or other geographic/political location. |
| 10 | 4/5 | Label A if and only if the question asks for a definition, meaning, name, cause, or amount rather than asking for a place, country, city, or other geographic entity. |
| 11 | 3/5 | Label A if and only if the question begins with a wh-word other than “where”; otherwise label B. |
| 12 | 2/5 | Label A if and only if the question starts with “What” or “Who”; otherwise label B. |
| 13 | 4/5 | Label B if and only if the question is asking for a place or geographic location (country, state, city, continent, capital, seaport, or similar). |
| 14 | 4/5 | Label B if and only if the question asks for a location/place or explicitly asks where to find something; otherwise label A. |
| 15 | 3/5 | Label A if and only if the question asks for a definition, identity, origin, quantity, or other fact not tied to a specific location; otherwise label B. |
| 16 | 4/5 | Label A if and only if the question begins with “What” or “Who”; otherwise label B. |
| 17 | 4/5 | Label A if and only if the question asks for a definition, explanation, age/number, or other descriptive information rather than asking for a specific place or named entity. |
| 18 | 5/5 | Label A if and only if the question asks for a definition, name, quantity, or identifying fact rather than a geographic location or place. |
| 19 | 1/5 | Label A if and only if the question contains a first- or second-person reference (such as I, you, your, we) or asks about a specific named individual/entity; otherwise label B. |
| 20 | 5/5 | Label B if and only if the question asks for a location, place, country, city, capital, or origin/from-where answer. |
| 21 | 5/5 | Label A if and only if the question asks for a definition, composition, quantity, person, or title/name, rather than asking for a location or geopolitical entity. |
| 22 | 5/5 | Label A if and only if the question is general/definitional or explanatory, rather than asking for a specific named entity, place, title, or factual lookup. |
| 23 | 4/5 | Label A if and only if the question is subjective, malformed, or otherwise not a straightforward factual geography/trivia query; otherwise label B. |
| 24 | 3/5 | Label B if and only if the question is asking for a place, location, or geographic entity. |
| 25 | 5/5 | Label B if and only if the question is asking for a location or place. |
| 26 | 3/5 | Label A if and only if the question can be answered with a specific named entity or definition, rather than asking for a location or place. |
| 27 | 5/5 | Label B if and only if the question asks for a place or country/location-based answer; otherwise label A. |
| 28 | 4/5 | Label B if and only if the question asks for a place name or geographic/political location; otherwise label A. |
| 29 | 5/5 | Label B if and only if the question is asking for a place, location, nationality, or geographic entity; otherwise label A. |
| 30 | 2/5 | Label A if and only if the question asks for a person, a specific number, a date/time, or a named title/name; otherwise label B. |
| 31 | 4/5 | Label A if and only if the question begins with an interrogative word other than “What” or “Where”; otherwise label B. |
| 32 | 4/5 | Label A if and only if the question begins with Who, When, Name, or What does/do; otherwise label B. |
| 33 | 2/5 | Label A if and only if the question begins with “What,” “Who,” or “How”; otherwise label B. |
| 34 | 4/5 | Label A if and only if the question contains an apostrophe; otherwise label B. |
| 35 | 4/5 | Label A if and only if the question asks for a person, title/name, or descriptive category, rather than for a place or country. |
| 36 | 5/5 | Label A if and only if the question asks for a person, number/distance, animal, term, or title/name, rather than for a place or country/city/location. |
| 37 | 2/5 | Label A if and only if the question contains a grammatical error or awkward wording; otherwise label B. |
| 38 | 4/5 | Label B if and only if the question asks for a specific named entity such as a country, city, capital, street, or airport, rather than asking for a date, person identity, list of people, definition, method, or general fact. |
| 39 | 5/5 | Label B if and only if the question is asking about a place or geopolitical entity (such as a country, state, capital, border, or location). |
| 40 | 5/5 | Label A if and only if the question’s answer is not a place; otherwise label B. |
| 41 | 2/5 | Label A if and only if the question begins with “What” or “How many”; otherwise label B. |
| 42 | 5/5 | Label B if and only if the question asks for a location, direction, or superlative/ranking fact; otherwise label A. |
| 43 | 4/5 | Label A if and only if the question word is not “where” or “what”; otherwise label B. |
| 44 | 5/5 | Label A if and only if the question asks for a definition, explanation, identification, or quoted/textual content rather than a location or place. |
| 45 | 5/5 | Label B if and only if the question asks about a location or place. |
| 46 | 4/5 | Label A if and only if the question is asking for a specific named entity or term, rather than for a location/country/continent/place. |
| 47 | 2/5 | Label A if and only if the question starts with a wh-word other than “where/what country/what city/what province/what nationality”; otherwise label B. |
| 48 | 5/5 | Label A if and only if the question asks for a person, thing, title, or concept, rather than asking for a location or place. |
| 49 | 5/5 | Label A if and only if the question asks for a non-location fact, and Label B if and only if it asks for a place or location. |
| 50 | 2/5 | Label A if and only if the question ends with a question mark. |

## Detailed Evaluations

### Rule 1: 4/5

Articulated rule: Label A if and only if the question asks for a person, organization/team, language, garment, or operating system, rather than asking for a place, landmark, natural feature, direction, or other location-like/physical answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0375 | What is the deepest area of the Arctic Ocean ? | B | B | yes |
| 2 | trec_location_answer_pool_0347 | Where do people mountain climb in Nepal ? | B | B | yes |
| 3 | trec_location_answer_pool_0104 | What are dingoes ? | A | B | no |
| 4 | trec_location_answer_pool_0417 | What Colorado city owns its own glacier ? | B | B | yes |
| 5 | trec_location_answer_pool_0035 | What city 's newspaper is called `` The Star '' ? | B | B | yes |

### Rule 2: 4/5

Articulated rule: Label A if and only if the question does not ask for a specific place or location; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0136 | What Metropolis landmark was first introduced in the Superman cartoons of the 1940 's ? | B | B | yes |
| 2 | trec_location_answer_pool_0271 | What 's the middle name of movie producer Joseph E. Levine ? | A | A | yes |
| 3 | trec_location_answer_pool_0128 | What mystery writer penned `` ...the glory that was Greece , and the grandeur that was Rome '' ? | A | A | yes |
| 4 | trec_location_answer_pool_0484 | Who was known as the Time Master in comic books ? | A | A | yes |
| 5 | trec_location_answer_pool_0430 | Why did the Shea & Gould law firm leave Los Angeles ? | A | B | no |

### Rule 3: 2/5

Articulated rule: Label A if and only if the question contains obvious tokenization/quotation/POS-tag noise or other malformed wording; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0048 | What are amicable numbers ? | A | B | no |
| 2 | trec_location_answer_pool_0254 | Name the story by Chris Van Allsburg in the which a boy tries to become a great sailor ? | A | A | yes |
| 3 | trec_location_answer_pool_0414 | Where is Natick ? | B | B | yes |
| 4 | trec_location_answer_pool_0008 | What is DTMF ? | A | B | no |
| 5 | trec_location_answer_pool_0363 | What Asian city boasts the world 's biggest bowling alley ? | B | A | no |

### Rule 4: 2/5

Articulated rule: Label A if and only if the question word is who, what, or what’s; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0378 | Name a technique widely used to detect birth defects ? | A | B | no |
| 2 | trec_location_answer_pool_0297 | Where did the ukulele originate ? | B | B | yes |
| 3 | trec_location_answer_pool_0145 | Where are the Haversian canals ? | B | B | yes |
| 4 | trec_location_answer_pool_0124 | Name the soft drink that is `` number one in the sun . '' | A | B | no |
| 5 | trec_location_answer_pool_0381 | Mississippi has what name for a state nickname ? | B | A | no |

### Rule 5: 3/5

Articulated rule: Label A if and only if the question begins with “How,” “Who,” or “Which”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0039 | What two countries is Andorra nestled between ? | B | B | yes |
| 2 | trec_location_answer_pool_0193 | What is the name of the song that Dracula plays on the organ ? | A | B | no |
| 3 | trec_location_answer_pool_0010 | What 's the Fahrenheit equivalent of zero degrees centigrade ? | A | B | no |
| 4 | trec_location_answer_pool_0157 | Where do apple snails live ? | B | B | yes |
| 5 | trec_location_answer_pool_0177 | Where can I find the names of all the 15 Pokemon ? | B | B | yes |

### Rule 6: 4/5

Articulated rule: Label B if and only if the question explicitly asks for a place or country/city/location; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0259 | What is the most important nation in the world , historically ? | B | B | yes |
| 2 | trec_location_answer_pool_0292 | What 's the largest island in the West Indies ? | B | A | no |
| 3 | trec_location_answer_pool_0361 | How big is a quart ? | A | A | yes |
| 4 | trec_location_answer_pool_0411 | What is the best place to live in the world , considering climate , civilization ? | B | B | yes |
| 5 | trec_location_answer_pool_0472 | What is the largest city in the world ? | B | B | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the question is not asking for a location/place; Label B if and only if it is asking about a place or location.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0156 | Where is the Henry Ford Museum ? | B | B | yes |
| 2 | trec_location_answer_pool_0328 | How many children under 18 are victims of some sort of Physical Abuse each year ? | A | A | yes |
| 3 | trec_location_answer_pool_0330 | How many wings does a flea have ? | A | A | yes |
| 4 | trec_location_answer_pool_0435 | What is the world 's population ? | A | A | yes |
| 5 | trec_location_answer_pool_0369 | Name the country which Honecker lived in . | B | B | yes |

### Rule 8: 2/5

Articulated rule: Label A if and only if the question begins with “What” or “Who”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0412 | How far can you see ? | A | B | no |
| 2 | trec_location_answer_pool_0277 | What ocean does Mauritania border ? | B | A | no |
| 3 | trec_location_answer_pool_0463 | How many equal sides are there on a scalene triangle ? | A | B | no |
| 4 | trec_location_answer_pool_0027 | What was the Ventura County police department that seized the county 's largest amount of cocaine ever ? | A | A | yes |
| 5 | trec_location_answer_pool_0104 | What are dingoes ? | A | A | yes |

### Rule 9: 5/5

Articulated rule: Label A if and only if the question is asking for a definition, explanation, manner, quantity, or specific identifying fact other than a location/nationality/political region; Label B if only if it asks for a place, country, state, city, nationality, or other geographic/political location.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0103 | What does the abbreviation SOS mean ? | A | A | yes |
| 2 | trec_location_answer_pool_0122 | Who is the only prime minister of Canada to serve 22 years but not necessarily consecutively ? | A | A | yes |
| 3 | trec_location_answer_pool_0063 | What was the name of the U.S. 's first manned space program ? | A | A | yes |
| 4 | trec_location_answer_pool_0487 | Where could I go to take a ride on a steam locomotive ? | B | B | yes |
| 5 | trec_location_answer_pool_0341 | What 's the capital of Monaco ? | B | B | yes |

### Rule 10: 4/5

Articulated rule: Label A if and only if the question asks for a definition, meaning, name, cause, or amount rather than asking for a place, country, city, or other geographic entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0040 | What London street claims to be the world center for men 's tailoring ? | B | B | yes |
| 2 | trec_location_answer_pool_0298 | What is after death ? | A | A | yes |
| 3 | trec_location_answer_pool_0300 | What are the names of all the seas in the world and what ocean do they drain into ? | B | A | no |
| 4 | trec_location_answer_pool_0177 | Where can I find the names of all the 15 Pokemon ? | B | B | yes |
| 5 | trec_location_answer_pool_0409 | What state did Anita Bryant represent in the 1959 Miss America contest ? | B | B | yes |

### Rule 11: 3/5

Articulated rule: Label A if and only if the question begins with a wh-word other than “where”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0068 | What detective lives on Punchbowl Hill and has 11 children ? | A | A | yes |
| 2 | trec_location_answer_pool_0050 | What are the short- and long-term effects of underage drinking ? | A | A | yes |
| 3 | trec_location_answer_pool_0300 | What are the names of all the seas in the world and what ocean do they drain into ? | B | A | no |
| 4 | trec_location_answer_pool_0209 | What 's the only East european country not tied to the ruble ? | B | A | no |
| 5 | trec_location_answer_pool_0162 | What are the rules to `` snow golf '' ? | A | A | yes |

### Rule 12: 2/5

Articulated rule: Label A if and only if the question starts with “What” or “Who”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0244 | What were the three prophecies the witches make to Macbeth ? | A | A | yes |
| 2 | trec_location_answer_pool_0011 | How did the jack-o '-lantern get it 's name ? | A | B | no |
| 3 | trec_location_answer_pool_0412 | How far can you see ? | A | B | no |
| 4 | trec_location_answer_pool_0291 | Where can I find the schematics to the windshield wiper mechanism ? | B | B | yes |
| 5 | trec_location_answer_pool_0482 | What country has the port of Haifa ? | B | A | no |

### Rule 13: 4/5

Articulated rule: Label B if and only if the question is asking for a place or geographic location (country, state, city, continent, capital, seaport, or similar).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0086 | What is pasta ? | A | A | yes |
| 2 | trec_location_answer_pool_0046 | On what T.V. show could Tom Terrific be found ? | A | A | yes |
| 3 | trec_location_answer_pool_0183 | What arch can you see from the Place de la Concorde ? | B | A | no |
| 4 | trec_location_answer_pool_0023 | What ice creams contain seaweed ? | A | A | yes |
| 5 | trec_location_answer_pool_0482 | What country has the port of Haifa ? | B | B | yes |

### Rule 14: 4/5

Articulated rule: Label B if and only if the question asks for a location/place or explicitly asks where to find something; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0038 | Where does chocolate come from ? | B | B | yes |
| 2 | trec_location_answer_pool_0238 | What nationality is Ileana Cotrubas ? | B | A | no |
| 3 | trec_location_answer_pool_0260 | What is the meaning of caliente , in English , ? | A | A | yes |
| 4 | trec_location_answer_pool_0140 | What bordering country is due north of Costa Rica ? | B | B | yes |
| 5 | trec_location_answer_pool_0363 | What Asian city boasts the world 's biggest bowling alley ? | B | B | yes |

### Rule 15: 3/5

Articulated rule: Label A if and only if the question asks for a definition, identity, origin, quantity, or other fact not tied to a specific location; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0388 | What kind of education would you need to become an athletic trainer for the NFL ? | A | B | no |
| 2 | trec_location_answer_pool_0456 | The second most popular sport worldwide is what ? | A | A | yes |
| 3 | trec_location_answer_pool_0297 | Where did the ukulele originate ? | B | B | yes |
| 4 | trec_location_answer_pool_0444 | What 's the world 's largest cathedral ? | B | A | no |
| 5 | trec_location_answer_pool_0151 | Where is Milan ? | B | B | yes |

### Rule 16: 4/5

Articulated rule: Label A if and only if the question begins with “What” or “Who”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0151 | Where is Milan ? | B | B | yes |
| 2 | trec_location_answer_pool_0459 | How do you reference a website ? | A | B | no |
| 3 | trec_location_answer_pool_0343 | Who is Ishmael in Moby Dick ? | A | A | yes |
| 4 | trec_location_answer_pool_0377 | What do opposite faces of a die always add up to ? | A | A | yes |
| 5 | trec_location_answer_pool_0241 | What is `` the computer for the rest of us '' ? | A | A | yes |

### Rule 17: 4/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, age/number, or other descriptive information rather than asking for a specific place or named entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0156 | Where is the Henry Ford Museum ? | B | B | yes |
| 2 | trec_location_answer_pool_0186 | Where is the human skin least sensitive ? | A | B | no |
| 3 | trec_location_answer_pool_0341 | What 's the capital of Monaco ? | B | B | yes |
| 4 | trec_location_answer_pool_0116 | What are the ages in comic book lingo ? | A | A | yes |
| 5 | trec_location_answer_pool_0337 | What nation boarders Mozambique ? | B | B | yes |

### Rule 18: 5/5

Articulated rule: Label A if and only if the question asks for a definition, name, quantity, or identifying fact rather than a geographic location or place.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0089 | What countries have the highest ratio of university students ? | B | B | yes |
| 2 | trec_location_answer_pool_0096 | What European country 's monarchy was restored in 1975 ? | B | B | yes |
| 3 | trec_location_answer_pool_0154 | What California desert is dubbed High Desert ? | B | B | yes |
| 4 | trec_location_answer_pool_0012 | What is the principal river of Ireland ? | B | B | yes |
| 5 | trec_location_answer_pool_0374 | Where did makeup originate ? | B | B | yes |

### Rule 19: 1/5

Articulated rule: Label A if and only if the question contains a first- or second-person reference (such as I, you, your, we) or asks about a specific named individual/entity; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0037 | What ocean did the Titanic sink in ? | B | B | yes |
| 2 | trec_location_answer_pool_0387 | What is an eclipse ? | A | B | no |
| 3 | trec_location_answer_pool_0291 | Where can I find the schematics to the windshield wiper mechanism ? | B | A | no |
| 4 | trec_location_answer_pool_0233 | Why do they call a hamburger a hamburger when there is no ham ? | A | B | no |
| 5 | trec_location_answer_pool_0078 | What is June 's birthstone ? | A | B | no |

### Rule 20: 5/5

Articulated rule: Label B if and only if the question asks for a location, place, country, city, capital, or origin/from-where answer.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0348 | What U.S. state is Mammoth Cave National Park in ? | B | B | yes |
| 2 | trec_location_answer_pool_0204 | Who was the author of `` John Brown 's Body '' ? | A | A | yes |
| 3 | trec_location_answer_pool_0021 | What are faults in the earth 's crust ? | A | A | yes |
| 4 | trec_location_answer_pool_0269 | What city is the Kentucky Horse Park near ? | B | B | yes |
| 5 | trec_location_answer_pool_0258 | How does a bill become law ? | A | A | yes |

### Rule 21: 5/5

Articulated rule: Label A if and only if the question asks for a definition, composition, quantity, person, or title/name, rather than asking for a location or geopolitical entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0470 | What phenomenon would you expect to read about in the monthly publication The Bigfoot News ? | A | A | yes |
| 2 | trec_location_answer_pool_0095 | What did Cool Hand Luke go to jail for ? | A | A | yes |
| 3 | trec_location_answer_pool_0079 | Where is Dartmouth College ? | B | B | yes |
| 4 | trec_location_answer_pool_0484 | Who was known as the Time Master in comic books ? | A | A | yes |
| 5 | trec_location_answer_pool_0004 | What year did the Andy Griffith show begin ? | A | A | yes |

### Rule 22: 5/5

Articulated rule: Label A if and only if the question is general/definitional or explanatory, rather than asking for a specific named entity, place, title, or factual lookup.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0471 | What is the Home Rule Act ? | A | A | yes |
| 2 | trec_location_answer_pool_0168 | How many pairs of wings does a tsetse fly have ? | A | A | yes |
| 3 | trec_location_answer_pool_0184 | What North American city sprouts the most parking meters ? | B | B | yes |
| 4 | trec_location_answer_pool_0177 | Where can I find the names of all the 15 Pokemon ? | B | B | yes |
| 5 | trec_location_answer_pool_0151 | Where is Milan ? | B | B | yes |

### Rule 23: 4/5

Articulated rule: Label A if and only if the question is subjective, malformed, or otherwise not a straightforward factual geography/trivia query; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0338 | When will the millennium officially begin ? | A | A | yes |
| 2 | trec_location_answer_pool_0367 | Which leg does a cat move with its left front leg when walking - its left rear or right rear leg ? | A | A | yes |
| 3 | trec_location_answer_pool_0286 | How old is the universe ? | A | A | yes |
| 4 | trec_location_answer_pool_0003 | Where do quality drinks begin ? | B | A | no |
| 5 | trec_location_answer_pool_0457 | What does Robin Williams do ? | A | A | yes |

### Rule 24: 3/5

Articulated rule: Label B if and only if the question is asking for a place, location, or geographic entity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0288 | What is the word for love of pain or abuse ? | A | A | yes |
| 2 | trec_location_answer_pool_0153 | What is the web address at which I can find the e-mail address of a member of the US House of Representatives ? | B | A | no |
| 3 | trec_location_answer_pool_0365 | What actor has a tattoo on his right wrist reading Scotland Forever ? | A | B | no |
| 4 | trec_location_answer_pool_0058 | What are the numbers that fit into Fermont 's last theorem ? | A | A | yes |
| 5 | trec_location_answer_pool_0149 | What North American city would you visit to see Cleopatra 's Needle ? | B | B | yes |

### Rule 25: 5/5

Articulated rule: Label B if and only if the question is asking for a location or place.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0034 | What U.S. state comes last in an alphabetical list ? | B | B | yes |
| 2 | trec_location_answer_pool_0450 | What is the seafaring name for the southern tip of South America ? | B | B | yes |
| 3 | trec_location_answer_pool_0230 | What country was Hitler the chancellor of ? | B | B | yes |
| 4 | trec_location_answer_pool_0309 | Who lives at 39 Stone Canyon Way ? | A | A | yes |
| 5 | trec_location_answer_pool_0428 | Who is the governor of Alaska ? | A | A | yes |

### Rule 26: 3/5

Articulated rule: Label A if and only if the question can be answered with a specific named entity or definition, rather than asking for a location or place.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0106 | How do you say `` fresh '' in Spanish ? | A | A | yes |
| 2 | trec_location_answer_pool_0092 | What do we call the imaginary line along the top of the Rocky Mountains ? | B | A | no |
| 3 | trec_location_answer_pool_0221 | What was the nationality of Jackson Pollock ? | B | A | no |
| 4 | trec_location_answer_pool_0289 | What TV character sired a horse named Thunder ? | A | A | yes |
| 5 | trec_location_answer_pool_0277 | What ocean does Mauritania border ? | B | B | yes |

### Rule 27: 5/5

Articulated rule: Label B if and only if the question asks for a place or country/location-based answer; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0068 | What detective lives on Punchbowl Hill and has 11 children ? | A | A | yes |
| 2 | trec_location_answer_pool_0345 | What state in the United States covers the largest area ? | B | B | yes |
| 3 | trec_location_answer_pool_0005 | What two countries contain Sierra Nevada mountains ? | B | B | yes |
| 4 | trec_location_answer_pool_0071 | Where is Amsterdam ? | B | B | yes |
| 5 | trec_location_answer_pool_0003 | Where do quality drinks begin ? | B | B | yes |

### Rule 28: 4/5

Articulated rule: Label B if and only if the question asks for a place name or geographic/political location; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0113 | Where do the Blackhawks maintain their operations ? | B | A | no |
| 2 | trec_location_answer_pool_0139 | Who is the sexiest women in the world ? | A | A | yes |
| 3 | trec_location_answer_pool_0339 | What Japanese city was once called Edo ? | B | B | yes |
| 4 | trec_location_answer_pool_0073 | What city is sometimes called The Athens of Switzerland ? | B | B | yes |
| 5 | trec_location_answer_pool_0063 | What was the name of the U.S. 's first manned space program ? | A | A | yes |

### Rule 29: 5/5

Articulated rule: Label B if and only if the question is asking for a place, location, nationality, or geographic entity; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0475 | Where can I find an Ask An Expert site ? | B | B | yes |
| 2 | trec_location_answer_pool_0263 | What is the temperature of the sun 's surface ? | A | A | yes |
| 3 | trec_location_answer_pool_0053 | What country has been called The Queen of the Antilles ? | B | B | yes |
| 4 | trec_location_answer_pool_0365 | What actor has a tattoo on his right wrist reading Scotland Forever ? | A | A | yes |
| 5 | trec_location_answer_pool_0296 | Who wrote the book , `` Song of Solomon '' ? | A | A | yes |

### Rule 30: 2/5

Articulated rule: Label A if and only if the question asks for a person, a specific number, a date/time, or a named title/name; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0217 | What is splatterpunk ? | A | B | no |
| 2 | trec_location_answer_pool_0139 | Who is the sexiest women in the world ? | A | A | yes |
| 3 | trec_location_answer_pool_0296 | Who wrote the book , `` Song of Solomon '' ? | A | A | yes |
| 4 | trec_location_answer_pool_0257 | How much will the California be in the year 2000 ? | A | B | no |
| 5 | trec_location_answer_pool_0320 | Why is it called `` hamburger '' if there is no ham in it ? | A | B | no |

### Rule 31: 4/5

Articulated rule: Label A if and only if the question begins with an interrogative word other than “What” or “Where”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0172 | Who was the bandleader mentor of Ella Fitzgerald with whom she cowrote `` A_Tisket , A-Tasket '' ? | A | A | yes |
| 2 | trec_location_answer_pool_0123 | What is the Ohio state bird ? | A | B | no |
| 3 | trec_location_answer_pool_0299 | What is the longest suspension bridge in the U.S. ? | B | B | yes |
| 4 | trec_location_answer_pool_0323 | What bay sparkles next to Miami , Florida ? | B | B | yes |
| 5 | trec_location_answer_pool_0085 | How much money was the minimum wage in 1991 ? | A | A | yes |

### Rule 32: 4/5

Articulated rule: Label A if and only if the question begins with Who, When, Name, or What does/do; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0330 | How many wings does a flea have ? | A | B | no |
| 2 | trec_location_answer_pool_0300 | What are the names of all the seas in the world and what ocean do they drain into ? | B | B | yes |
| 3 | trec_location_answer_pool_0225 | What body of water does the Yukon River empty into ? | B | B | yes |
| 4 | trec_location_answer_pool_0265 | What ocean is the largest in the world ? | B | B | yes |
| 5 | trec_location_answer_pool_0054 | Who sings the song `` Drink to me with thine eyes '' by Ben Johnson ? | A | A | yes |

### Rule 33: 2/5

Articulated rule: Label A if and only if the question begins with “What,” “Who,” or “How”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0082 | Where does tuberculosis come from ? | B | B | yes |
| 2 | trec_location_answer_pool_0364 | What country was Sir Edmund Hillary born in ? | B | A | no |
| 3 | trec_location_answer_pool_0413 | Who portrayed George M. Cohan in 1942 's Yankee Doodle Dandy ? | A | A | yes |
| 4 | trec_location_answer_pool_0209 | What 's the only East european country not tied to the ruble ? | B | A | no |
| 5 | trec_location_answer_pool_0009 | What city is the setting for Puccini 's opera La Boheme ? | B | A | no |

### Rule 34: 4/5

Articulated rule: Label A if and only if the question contains an apostrophe; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0439 | What city was Martin Luther King Jr. assassinated in ? | B | B | yes |
| 2 | trec_location_answer_pool_0282 | The Kentucky Horse Park is close to which American city ? | B | B | yes |
| 3 | trec_location_answer_pool_0211 | How big is our galaxy in diameter ? | A | B | no |
| 4 | trec_location_answer_pool_0066 | Where on the Internet can I find information on laundry detergent ? | B | B | yes |
| 5 | trec_location_answer_pool_0231 | Where can I buy a hat like the kind Jay Kay from Jamiroquai wears ? | B | B | yes |

### Rule 35: 4/5

Articulated rule: Label A if and only if the question asks for a person, title/name, or descriptive category, rather than for a place or country.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0234 | What English word contains the most letters ? | A | A | yes |
| 2 | trec_location_answer_pool_0302 | What 's the term for an organism that lives on or in another ? | A | A | yes |
| 3 | trec_location_answer_pool_0074 | How much of the nation 's children between the ages of two and eleven watch ` The Simpsons ' ? | A | B | no |
| 4 | trec_location_answer_pool_0417 | What Colorado city owns its own glacier ? | B | B | yes |
| 5 | trec_location_answer_pool_0464 | What canal does the Thatcher Ferry Bridge span ? | B | B | yes |

### Rule 36: 5/5

Articulated rule: Label A if and only if the question asks for a person, number/distance, animal, term, or title/name, rather than for a place or country/city/location.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0001 | Who was Whitcomb Judson ? | A | A | yes |
| 2 | trec_location_answer_pool_0040 | What London street claims to be the world center for men 's tailoring ? | B | B | yes |
| 3 | trec_location_answer_pool_0353 | What colorful sea 's region does Greek legend say the Amazons lived near ? | B | B | yes |
| 4 | trec_location_answer_pool_0414 | Where is Natick ? | B | B | yes |
| 5 | trec_location_answer_pool_0420 | What city has the world 's longest subway system ? | B | B | yes |

### Rule 37: 2/5

Articulated rule: Label A if and only if the question contains a grammatical error or awkward wording; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0497 | Which country has the most water pollution ? | B | A | no |
| 2 | trec_location_answer_pool_0000 | What New York City landmark has 168 steps to its crown ? | B | A | no |
| 3 | trec_location_answer_pool_0109 | What did Aaron Hass write ? | A | A | yes |
| 4 | trec_location_answer_pool_0281 | What Rocky Mountain ridge separates North America 's eastward and westward-flowing rivers ? | B | A | no |
| 5 | trec_location_answer_pool_0241 | What is `` the computer for the rest of us '' ? | A | A | yes |

### Rule 38: 4/5

Articulated rule: Label B if and only if the question asks for a specific named entity such as a country, city, capital, street, or airport, rather than asking for a date, person identity, list of people, definition, method, or general fact.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0150 | What actress starred in `` The Lion in Winter '' ? | A | A | yes |
| 2 | trec_location_answer_pool_0116 | What are the ages in comic book lingo ? | A | A | yes |
| 3 | trec_location_answer_pool_0154 | What California desert is dubbed High Desert ? | B | B | yes |
| 4 | trec_location_answer_pool_0070 | What is the capital of Seattle ? | B | B | yes |
| 5 | trec_location_answer_pool_0485 | What is the name of the tallest mountain in the world ? | B | A | no |

### Rule 39: 5/5

Articulated rule: Label B if and only if the question is asking about a place or geopolitical entity (such as a country, state, capital, border, or location).

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0048 | What are amicable numbers ? | A | A | yes |
| 2 | trec_location_answer_pool_0262 | How many layers of yellow paint is a Faber Mongol pencil lucky enough to be sprayed with ? | A | A | yes |
| 3 | trec_location_answer_pool_0384 | When did beethoven die ? | A | A | yes |
| 4 | trec_location_answer_pool_0429 | What developed a crack in 1835 while tolling the death of U.S. Chief Justice John Marshall ? | A | A | yes |
| 5 | trec_location_answer_pool_0311 | Where did Bill Gates go to college ? | B | B | yes |

### Rule 40: 5/5

Articulated rule: Label A if and only if the question’s answer is not a place; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0344 | What are the words to the Canadian National anthem ? | A | A | yes |
| 2 | trec_location_answer_pool_0327 | What are semiconductors ? | A | A | yes |
| 3 | trec_location_answer_pool_0150 | What actress starred in `` The Lion in Winter '' ? | A | A | yes |
| 4 | trec_location_answer_pool_0088 | What happened to Moon Maiden ? | A | A | yes |
| 5 | trec_location_answer_pool_0418 | Where do you find the answers for all these questions ? | B | B | yes |

### Rule 41: 2/5

Articulated rule: Label A if and only if the question begins with “What” or “How many”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0088 | What happened to Moon Maiden ? | A | A | yes |
| 2 | trec_location_answer_pool_0305 | What nationality is Pope John Paul II ? | B | A | no |
| 3 | trec_location_answer_pool_0408 | How do you get rid on woodpeckers ? | A | B | no |
| 4 | trec_location_answer_pool_0112 | Name Pittsburgh 's baseball team . | A | B | no |
| 5 | trec_location_answer_pool_0424 | What kind of women gave Sigmund Freud erotic dreams ? | A | A | yes |

### Rule 42: 5/5

Articulated rule: Label B if and only if the question asks for a location, direction, or superlative/ranking fact; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0478 | What two countries ' coastlines border the Bay of Biscay ? | B | B | yes |
| 2 | trec_location_answer_pool_0171 | How many frames does a disk camera shoot ? | A | A | yes |
| 3 | trec_location_answer_pool_0475 | Where can I find an Ask An Expert site ? | B | B | yes |
| 4 | trec_location_answer_pool_0487 | Where could I go to take a ride on a steam locomotive ? | B | B | yes |
| 5 | trec_location_answer_pool_0125 | In what city is the US Declaration of Independence located ? | B | B | yes |

### Rule 43: 4/5

Articulated rule: Label A if and only if the question word is not “where” or “what”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0005 | What two countries contain Sierra Nevada mountains ? | B | B | yes |
| 2 | trec_location_answer_pool_0020 | Where did the Battle of the Bulge take place ? | B | A | no |
| 3 | trec_location_answer_pool_0092 | What do we call the imaginary line along the top of the Rocky Mountains ? | B | B | yes |
| 4 | trec_location_answer_pool_0306 | Who portrayed Fatman in the television show , `` Jake and the Fatman '' ? | A | A | yes |
| 5 | trec_location_answer_pool_0047 | How many engines does a Boeing 737 have ? | A | A | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if the question asks for a definition, explanation, identification, or quoted/textual content rather than a location or place.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0042 | What building are British monarchs crowned in ? | B | B | yes |
| 2 | trec_location_answer_pool_0038 | Where does chocolate come from ? | B | B | yes |
| 3 | trec_location_answer_pool_0098 | What four tournaments make up tennis ' Grand Slam ? | A | A | yes |
| 4 | trec_location_answer_pool_0204 | Who was the author of `` John Brown 's Body '' ? | A | A | yes |
| 5 | trec_location_answer_pool_0437 | What city 's theatrical district has been dubbed The Roaring Forties ? | B | B | yes |

### Rule 45: 5/5

Articulated rule: Label B if and only if the question asks about a location or place.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0066 | Where on the Internet can I find information on laundry detergent ? | B | B | yes |
| 2 | trec_location_answer_pool_0351 | How long does it take for Spider-Man 's web to evaporate ? | A | A | yes |
| 3 | trec_location_answer_pool_0205 | What country did the Nazis occupy for 1 , CD NNS IN NNP NNP NNP . | B | B | yes |
| 4 | trec_location_answer_pool_0415 | What season begins with the vernal equinox ? | A | A | yes |
| 5 | trec_location_answer_pool_0022 | What Frenchman claimed the following ? If God did not exist , it would be necessary to invent him . '' | A | A | yes |

### Rule 46: 4/5

Articulated rule: Label A if and only if the question is asking for a specific named entity or term, rather than for a location/country/continent/place.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0336 | How many times a day should you take a prescription marked `` q.i.d . '' ? | A | A | yes |
| 2 | trec_location_answer_pool_0314 | How many consecutive baseball games did Lou Gehrig play ? | A | A | yes |
| 3 | trec_location_answer_pool_0358 | In what year was De Gaulle elected president of France ? | A | B | no |
| 4 | trec_location_answer_pool_0184 | What North American city sprouts the most parking meters ? | B | B | yes |
| 5 | trec_location_answer_pool_0392 | What 's the traditional drink at the Kentucky Derby ? | A | A | yes |

### Rule 47: 2/5

Articulated rule: Label A if and only if the question starts with a wh-word other than “where/what country/what city/what province/what nationality”; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0416 | What is the nickname of Pennsylvania ? | B | A | no |
| 2 | trec_location_answer_pool_0220 | What is a Certified Nurse Midwife ? | A | A | yes |
| 3 | trec_location_answer_pool_0450 | What is the seafaring name for the southern tip of South America ? | B | A | no |
| 4 | trec_location_answer_pool_0255 | What do the names Neil , Mary , and Anthony mean ? | A | A | yes |
| 5 | trec_location_answer_pool_0114 | What 's the tallest building in New York City ? | B | A | no |

### Rule 48: 5/5

Articulated rule: Label A if and only if the question asks for a person, thing, title, or concept, rather than asking for a location or place.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0386 | In which Kevin Costner movie did Sioux Indians play a role ? | A | A | yes |
| 2 | trec_location_answer_pool_0455 | What German city do Italians call The Monaco of Bavaria ? | B | B | yes |
| 3 | trec_location_answer_pool_0179 | What is the capital of Zimbabwe ? | B | B | yes |
| 4 | trec_location_answer_pool_0171 | How many frames does a disk camera shoot ? | A | A | yes |
| 5 | trec_location_answer_pool_0453 | What river does the Grand Coulee Dam dam ? | B | B | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if the question asks for a non-location fact, and Label B if and only if it asks for a place or location.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0188 | Where do lobsters like to live ? | B | B | yes |
| 2 | trec_location_answer_pool_0498 | In 1990 , what day of the week did Christmas fall on ? | A | A | yes |
| 3 | trec_location_answer_pool_0235 | Who says , `` If you don 't look good , we don 't look good '' ? | A | A | yes |
| 4 | trec_location_answer_pool_0455 | What German city do Italians call The Monaco of Bavaria ? | B | B | yes |
| 5 | trec_location_answer_pool_0364 | What country was Sir Edmund Hillary born in ? | B | B | yes |

### Rule 50: 2/5

Articulated rule: Label A if and only if the question ends with a question mark.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | trec_location_answer_pool_0485 | What is the name of the tallest mountain in the world ? | B | A | no |
| 2 | trec_location_answer_pool_0237 | What net game sees its women 's world amateur champions receive the Uber Cup ? | A | A | yes |
| 3 | trec_location_answer_pool_0287 | What country has problems with hooligans ? | B | A | no |
| 4 | trec_location_answer_pool_0304 | What 's the closest G2 Spectrum Yellow Dwarf to Earth ? | B | A | no |
| 5 | trec_location_answer_pool_0385 | What is the primary language in Iceland ? | A | A | yes |

