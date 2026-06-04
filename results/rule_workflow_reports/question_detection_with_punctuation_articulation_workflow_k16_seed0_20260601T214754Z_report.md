# Rule Articulation Workflow: question_detection_with_punctuation

Run ID: `question_detection_with_punctuation_articulation_workflow_k16_seed0_20260601T214754Z`

Correct prompt-facing rule: Label B iff the input is an actual question; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.944
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.944
- Rules with all evals correct: 42
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
| 1 | 5/5 | Label B if and only if the input is a question asking for factual information; otherwise label A. |
| 2 | 5/5 | Label A if and only if the input is a movie review expressing an opinion or sentiment; otherwise label B for factual or informational questions. |
| 3 | 5/5 | Label A if and only if the input is a subjective opinion or review, and Label B if it is a factual question asking for information. |
| 4 | 3/5 | Label A if and only if the input is a negative, critical, or unfavorable movie-review style sentence; otherwise label B. |
| 5 | 5/5 | Label A if and only if the input is a movie review or opinion about a film; otherwise label B. |
| 6 | 5/5 | Label A if and only if the input is a subjective opinion or review-like statement; label B if it is an objective factual question or informational query. |
| 7 | 5/5 | Label A if and only if the input is a movie review or other opinionated descriptive statement; otherwise label B. |
| 8 | 5/5 | Label A if and only if the input is a movie/review-style opinion or sentiment statement, and label B if it is a factual question. |
| 9 | 1/5 | Label A if and only if the input is a negative or critical movie review; otherwise label B. |
| 10 | 5/5 | Label A if and only if the input is a movie/review-style opinion or sentiment statement; otherwise label B. |
| 11 | 5/5 | Label A if and only if the input is a movie-review style opinion or sentiment statement, and Label B if it is a factual question asking for information. |
| 12 | 5/5 | Label A if and only if the input is a subjective opinion or review-like statement, and Label B if it is a factual question or information-seeking query. |
| 13 | 5/5 | Label A if and only if the input is a subjective opinion or review-like statement; label B if it is a factual question asking for information. |
| 14 | 5/5 | Label A if and only if the input is a movie review or opinion about a film; otherwise label B. |
| 15 | 5/5 | Label A if and only if the input is a subjective opinion or review-like statement expressing sentiment, while Label B if it is a factual question asking for information. |
| 16 | 5/5 | Label A if and only if the input is a movie review or other opinionated sentiment statement, while Label B if it is a factual question or neutral informational query. |
| 17 | 5/5 | Label A if and only if the input is a movie review or other opinionated statement expressing sentiment; label B if it is a factual question or neutral informational query. |
| 18 | 5/5 | Label A if and only if the input is a movie review or opinionated statement, and Label B if it is a factual question. |
| 19 | 3/5 | Label A if and only if the input is a negative or critical movie review; otherwise label B. |
| 20 | 5/5 | Label A if and only if the input is a movie-review-style opinion or sentiment phrase, rather than a factual question. |
| 21 | 5/5 | Label A if and only if the input is a subjective opinion or review, and Label B if it is a factual question asking for information. |
| 22 | 5/5 | Label A if and only if the input is a subjective, opinionated movie/book review-style statement; otherwise label B for factual or informational questions/statements. |
| 23 | 5/5 | Label A if and only if the input is a subjective opinion or review, and Label B if it is a factual question asking for information. |
| 24 | 5/5 | Label A if and only if the input is a movie review or other subjective opinion; label B if it is a factual question. |
| 25 | 5/5 | Label A if and only if the input is a movie review or other subjective opinion text; Label B if it is a factual question. |
| 26 | 5/5 | Label A if and only if the input is a movie review or opinionated description; label B if it is a factual question asking for information. |
| 27 | 5/5 | Label A if and only if the input is a subjective opinion or review-like statement; label B if it is an objective factual question. |
| 28 | 5/5 | Label A if and only if the input is a subjective, opinionated movie-review style statement; otherwise label B. |
| 29 | 5/5 | Label A if and only if the input is a subjective opinion or review-like statement, and Label B if it is a factual question or objective information-seeking sentence. |
| 30 | 5/5 | Label A if and only if the input is a movie review or opinionated critique; otherwise label B. |
| 31 | 5/5 | Label A if and only if the sentence is a positive, subjective opinion or sentiment; otherwise label B. |
| 32 | 5/5 | Label A if and only if the input is a movie review or other subjective opinion statement; label B if it is a factual question or objective information request. |
| 33 | 5/5 | Label A if and only if the input is a negative, critical, or opinionated movie-review-style statement; otherwise label B for factual question-style queries. |
| 34 | 5/5 | Label A if and only if the input is a movie review expressing a positive or negative opinion; label B if it is a factual question. |
| 35 | 5/5 | Label A if and only if the input is a subjective opinion or review sentiment, while Label B if it is a factual question or neutral informational query. |
| 36 | 4/5 | Label A if and only if the input is a movie review or opinion about a film; otherwise label B. |
| 37 | 5/5 | Label B if and only if the input is a factual, information-seeking question; otherwise label A. |
| 38 | 5/5 | Label A if and only if the input is a movie review or other subjective opinion text; otherwise label B. |
| 39 | 4/5 | Label A if and only if the input is a subjective, opinionated movie-review-style statement; otherwise label B. |
| 40 | 4/5 | Label A if and only if the input is a movie review or opinion about a film; otherwise label B. |
| 41 | 5/5 | Label A if and only if the input is a subjective movie review or opinion about a film; label B if it is a factual question or other informational query. |
| 42 | 5/5 | Label A if and only if the input is a subjective, opinionated movie-review style statement; otherwise label B. |
| 43 | 5/5 | Label A if and only if the input is a movie review or opinionated critique; label B if it is a factual question or general knowledge query. |
| 44 | 3/5 | Label A if and only if the input is a negative or critical movie review; otherwise label B. |
| 45 | 5/5 | Label A if and only if the input is a movie review or other opinionated statement expressing sentiment; otherwise label B. |
| 46 | 5/5 | Label A if and only if the input is a subjective movie-review style opinion, and label B if it is a factual question. |
| 47 | 5/5 | Label A if and only if the input is a subjective opinion or review-like statement rather than a factual question. |
| 48 | 5/5 | Label B if and only if the input is a factual information-seeking question; Label A if it is a subjective opinion or review statement. |
| 49 | 4/5 | Label A if and only if the input is a positive movie review; otherwise label B for factual questions. |
| 50 | 5/5 | Label A if and only if the input is a movie review or opinionated critique, and Label B if it is a factual question asking for information. |

## Detailed Evaluations

### Rule 1: 5/5

Articulated rule: Label B if and only if the input is a question asking for factual information; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0375 | Who was the famous door-to-door brush salesman ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0346 | What is the biggest `` thing '' humans have made ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0105 | too much of the humor falls flat . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0417 | What celestial body has a diameter of 864 , 000 miles ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0035 | minority report is exactly what the title indicates , a report . | A | A | yes |

### Rule 2: 5/5

Articulated rule: Label A if and only if the input is a movie review expressing an opinion or sentiment; otherwise label B for factual or informational questions.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0136 | not exactly the bees knees | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0271 | Why is the word `` abbreviation '' so long ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0128 | a valueless kiddie paean to pro basketball underwritten by the nba . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0483 | What Caribbean island is sometimes called Little England ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0430 | During which season do most thunderstorms occur ? | B | B | yes |

### Rule 3: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review, and Label B if it is a factual question asking for information.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0048 | Where did he get the title ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0254 | What is the nature of learning ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0414 | a better title , for all concerned , might be swept under the rug . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0008 | How do you make dumplings ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0363 | What disease plagued Europe , Africa and Asia ? | B | B | yes |

### Rule 4: 3/5

Articulated rule: Label A if and only if the input is a negative, critical, or unfavorable movie-review style sentence; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0378 | at its worst , it implodes in a series of very bad special effects . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0297 | How often does Old Faithful erupt at Yellowstone National Park ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0145 | nothing is sacred in this gut-buster . | A | B | no |
| 4 | question_detection_with_punctuation_pool_0124 | it all adds up to good fun . | A | B | no |
| 5 | question_detection_with_punctuation_pool_0381 | What lake in Scotland is said to hold one or more monsters ? | B | B | yes |

### Rule 5: 5/5

Articulated rule: Label A if and only if the input is a movie review or opinion about a film; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0039 | How do I know someone is truly in love with me ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0193 | if your taste runs to ` difficult ' films you absolutely ca n't miss it . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0010 | What woman has carried the most multiple births , twins , triplets , etc. , ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0157 | How is water treated to make it safe to drink ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0177 | What is the average weight for a man ? | B | B | yes |

### Rule 6: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review-like statement; label B if it is an objective factual question or informational query.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0259 | one of the most significant moviegoing pleasures of the year . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0292 | puts a human face on a land most westerners are unfamiliar with . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0361 | Where can I find lyrics for R&B ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0411 | What color tennis balls are used at Wimbledon ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0472 | there are plot holes big enough for shamu the killer whale to swim through . | A | A | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if the input is a movie review or other opinionated descriptive statement; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0156 | Who won the rugby world cup in ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0328 | huston nails both the glad-handing and the choking sense of hollow despair . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0330 | my reaction in a word : disappointment . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0436 | Which president was unmarried ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0369 | among the year 's most intriguing explorations of alientation . | A | A | yes |

### Rule 8: 5/5

Articulated rule: Label A if and only if the input is a movie/review-style opinion or sentiment statement, and label B if it is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0412 | How does the tail affect the flight of a kite ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0277 | the humor is forced and heavy-handed , and occasionally simply unpleasant . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0463 | add yet another hat to a talented head , clooney 's a good director . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0027 | Why does sound travel quicker through water than air ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0104 | What is the width of a football field ? | B | B | yes |

### Rule 9: 1/5

Articulated rule: Label A if and only if the input is a negative or critical movie review; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0103 | but it still jingles in the pocket . | A | B | no |
| 2 | question_detection_with_punctuation_pool_0122 | scooby dooby doo / and shaggy too / you both look and sound great . | A | B | no |
| 3 | question_detection_with_punctuation_pool_0063 | for movie lovers as well as opera lovers , tosca is a real treat . | A | B | no |
| 4 | question_detection_with_punctuation_pool_0488 | it is amusing , and that 's all it needs to be . | A | B | no |
| 5 | question_detection_with_punctuation_pool_0341 | How long was the longest hiccup attack ? | B | B | yes |

### Rule 10: 5/5

Articulated rule: Label A if and only if the input is a movie/review-style opinion or sentiment statement; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0040 | What comic of TV 's golden age went by the motto `` Anything for a laugh '' ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0298 | Where are the British crown jewels kept ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0300 | What was the first TV set to include a remote control ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0177 | What is the average weight for a man ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0409 | What are names of two old men who appear in the serial tv Muppets Show ? | B | B | yes |

### Rule 11: 5/5

Articulated rule: Label A if and only if the input is a movie-review style opinion or sentiment statement, and Label B if it is a factual question asking for information.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0068 | a study in shades of gray , offering itself up in subtle plot maneuvers ... | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0051 | overall very good for what it 's trying to do . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0300 | What was the first TV set to include a remote control ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0209 | What is the population of Mozambique ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0162 | ... routine , harmless diversion and little else . | A | A | yes |

### Rule 12: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review-like statement, and Label B if it is a factual question or information-seeking query.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0244 | turns potentially forgettable formula into something strangely diverting . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0011 | falls neatly into the category of good stupid fun . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0412 | How does the tail affect the flight of a kite ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0291 | beautifully observed , miraculously unsentimental comedy-drama . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0482 | How many milligrams are in a gram ? | B | B | yes |

### Rule 13: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review-like statement; label B if it is a factual question asking for information.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0086 | What are the Nordic nations ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0047 | What clause in the U.S. Constitution may not be changed , altered or amended ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0183 | if you 're hard up for raunchy college humor , this is your ticket right here . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0023 | What shape-shifting menace did Rom come to Earth to fight ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0482 | How many milligrams are in a gram ? | B | B | yes |

### Rule 14: 5/5

Articulated rule: Label A if and only if the input is a movie review or opinion about a film; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0038 | What are the biggest Indian airports ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0238 | What is the geographical center of the US including Alaska and Hawaii ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0259 | one of the most significant moviegoing pleasures of the year . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0140 | What animals can live the longest without food ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0362 | What was known as the Spice Island ? | B | B | yes |

### Rule 15: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review-like statement expressing sentiment, while Label B if it is a factual question asking for information.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0388 | the film tunes into a grief that could lead a man across centuries . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0456 | no way i can believe this load of junk . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0297 | How often does Old Faithful erupt at Yellowstone National Park ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0444 | there 's a wickedly subversive bent to the best parts of birthday girl . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0151 | What hemisphere is the Philippines in ? | B | B | yes |

### Rule 16: 5/5

Articulated rule: Label A if and only if the input is a movie review or other opinionated sentiment statement, while Label B if it is a factual question or neutral informational query.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0151 | What hemisphere is the Philippines in ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0460 | When did the vesuvius last erupt ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0343 | How can I get someone 's email address ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0377 | that is a compliment to kuras and miller . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0240 | What are two plants that clothes are made from ? | B | B | yes |

### Rule 17: 5/5

Articulated rule: Label A if and only if the input is a movie review or other opinionated statement expressing sentiment; label B if it is a factual question or neutral informational query.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0156 | Who won the rugby world cup in ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0186 | a painfully funny ode to bad behavior . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0341 | How long was the longest hiccup attack ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0117 | if the first men in black was money , the second is small change . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0337 | a beguiling splash of pastel colors and prankish comedy from disney . | A | A | yes |

### Rule 18: 5/5

Articulated rule: Label A if and only if the input is a movie review or opinionated statement, and Label B if it is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0089 | and that 's a big part of why we go to the movies . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0097 | it made me want to wrench my eyes out of my head and toss them at the screen . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0154 | How do you make the color purple ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0012 | makes for a pretty unpleasant viewing experience . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0374 | What is the chemical symbol for nitrogen ? | B | B | yes |

### Rule 19: 3/5

Articulated rule: Label A if and only if the input is a negative or critical movie review; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0036 | How much money does the Sultan of Brunei have ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0387 | it treats women like idiots . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0291 | beautifully observed , miraculously unsentimental comedy-drama . | A | B | no |
| 4 | question_detection_with_punctuation_pool_0233 | What was Joe Namath 's first contract worth ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0078 | and that leaves a hole in the center of the salton sea . | A | B | no |

### Rule 20: 5/5

Articulated rule: Label A if and only if the input is a movie-review-style opinion or sentiment phrase, rather than a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0347 | but this films lacks the passion required to sell the material . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0204 | the best film about baseball to hit theaters since field of dreams . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0021 | a solid film ... but more conscientious than it is truly stirring . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0269 | leigh 's film is full of memorable performances from top to bottom . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0258 | How many years ago did Led Zeppelin release its last album ? | B | B | yes |

### Rule 21: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review, and Label B if it is a factual question asking for information.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0470 | but it 's too long and too convoluted and it ends in a muddle . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0095 | Who was the first African American to play for the Brooklyn Dodgers ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0080 | it 's a lovely film with lovely performances by buy and accorsi . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0485 | but it could have been worse . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0004 | What California bridge was Don Brown the first to cross , on May 27 , 1937 ? | B | B | yes |

### Rule 22: 5/5

Articulated rule: Label A if and only if the input is a subjective, opinionated movie/book review-style statement; otherwise label B for factual or informational questions/statements.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0471 | so much facile technique , such cute ideas , so little movie . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0168 | What is the literal meaning of `` D-DAY '' ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0184 | What 's the American dollar equivalent for 8 pounds in the U.K. ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0177 | What is the average weight for a man ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0151 | What hemisphere is the Philippines in ? | B | B | yes |

### Rule 23: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review, and Label B if it is a factual question asking for information.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0338 | How much did Lucy Van Pelt originally charge for psychiatric sessions ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0367 | that 's pure pr hype . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0286 | it 's a charming and often affecting journey . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0003 | good film , but very glum . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0457 | the second coming of harry potter is a film far superior to its predecessor . | A | A | yes |

### Rule 24: 5/5

Articulated rule: Label A if and only if the input is a movie review or other subjective opinion; label B if it is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0288 | What does the abbreviation AIDS stand for ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0152 | How is digital audio used ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0365 | What is Britain 's possession on the Chinese mainland ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0058 | verbinski implements every hack-artist trick to give us the ooky-spookies . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0149 | the film 's tone and pacing are off almost from the get-go . | A | A | yes |

### Rule 25: 5/5

Articulated rule: Label A if and only if the input is a movie review or other subjective opinion text; Label B if it is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0033 | a sequel that 's much too big for its britches . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0450 | old-form moviemaking at its best . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0230 | What did John Hinckley do to impress Jodie Foster ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0309 | the film tries too hard to be funny and tries too hard to be hip . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0429 | a tender , heartfelt family drama . | A | A | yes |

### Rule 26: 5/5

Articulated rule: Label A if and only if the input is a movie review or opinionated description; label B if it is a factual question asking for information.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0106 | What does a chef coddle eggs in ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0092 | directed in a paint-by-numbers manner . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0221 | it 's also , clearly , great fun . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0289 | the heavy-handed film is almost laughable as a consequence . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0277 | the humor is forced and heavy-handed , and occasionally simply unpleasant . | A | A | yes |

### Rule 27: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review-like statement; label B if it is an objective factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0068 | a study in shades of gray , offering itself up in subtle plot maneuvers ... | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0345 | How do you pronounce `` Tzimisce '' ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0005 | the film is quiet , threatening and unforgettable . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0071 | How do hermit crabs reproduce ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0003 | good film , but very glum . | A | A | yes |

### Rule 28: 5/5

Articulated rule: Label A if and only if the input is a subjective, opinionated movie-review style statement; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0113 | What color of Monopoly properties are landed on most often ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0139 | What are the first and last letters of the Greek alphabet ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0339 | a by-the-numbers effort that wo n't do much to enhance the franchise . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0073 | manages to be sweet and wickedly satisfying at the same time . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0063 | for movie lovers as well as opera lovers , tosca is a real treat . | A | A | yes |

### Rule 29: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review-like statement, and Label B if it is a factual question or objective information-seeking sentence.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0475 | What is the largest city in Germany ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0262 | a movie with a real anarchic flair . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0053 | What country borders the most others ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0365 | What is Britain 's possession on the Chinese mainland ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0295 | Which of the following men was not married to Rita Hayworth ? | B | B | yes |

### Rule 30: 5/5

Articulated rule: Label A if and only if the input is a movie review or opinionated critique; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0217 | this is human comedy at its most amusing , interesting and confirming . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0138 | Who made the first surfboard ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0296 | holm ... embodies the character with an effortlessly regal charisma . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0257 | enormously entertaining for moviegoers of any age . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0319 | expect the same-old , lame-old slasher nonsense , just with different scenery . | A | A | yes |

### Rule 31: 5/5

Articulated rule: Label A if and only if the sentence is a positive, subjective opinion or sentiment; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0172 | even in its most tedious scenes , russian ark is mesmerizing . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0123 | What London street is the home of British journalism ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0299 | When was Algeria colonized ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0323 | Where do the adventures of `` The Swiss Family Robinson '' take place ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0085 | What South Korean city is served by Kimpo International Airport ? | B | B | yes |

### Rule 32: 5/5

Articulated rule: Label A if and only if the input is a movie review or other subjective opinion statement; label B if it is a factual question or objective information request.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0330 | my reaction in a word : disappointment . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0300 | What was the first TV set to include a remote control ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0225 | comes ... uncomfortably close to coasting in the treads of the bicycle thief . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0265 | one of the smartest takes on singles culture i 've seen in a long time . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0054 | What is the largest U.S. state east of the Mississippi ? | B | B | yes |

### Rule 33: 5/5

Articulated rule: Label A if and only if the input is a negative, critical, or opinionated movie-review-style statement; otherwise label B for factual question-style queries.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0082 | prurient playthings aside , there 's little to love about this english trifle . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0364 | seldom has a movie so closely matched the spirit of a man and his work . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0413 | What is an Angelus ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0209 | What is the population of Mozambique ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0009 | it 's not the ultimate depression-era gangster movie . | A | A | yes |

### Rule 34: 5/5

Articulated rule: Label A if and only if the input is a movie review expressing a positive or negative opinion; label B if it is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0440 | it 's slow -- very , very slow . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0282 | Who was America 's first Public Enemy No. 1 ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0211 | a woman 's pic directed with resonance by ilya chaiken . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0066 | What 's the maximum length , in inches , of a first baseman 's glove ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0230 | What did John Hinckley do to impress Jodie Foster ? | B | B | yes |

### Rule 35: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review sentiment, while Label B if it is a factual question or neutral informational query.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0233 | What was Joe Namath 's first contract worth ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0302 | Who portrayed Sherlock Holmes in 14 films between 1939 and 1946 ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0073 | manages to be sweet and wickedly satisfying at the same time . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0417 | What celestial body has a diameter of 864 , 000 miles ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0464 | we have n't seen such hilarity since say it is n't so ! | A | A | yes |

### Rule 36: 4/5

Articulated rule: Label A if and only if the input is a movie review or opinion about a film; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0001 | a broad , melodramatic estrogen opera that 's pretty toxic in its own right . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0039 | How do I know someone is truly in love with me ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0354 | How many people are taller than 7 feet ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0414 | a better title , for all concerned , might be swept under the rug . | A | B | no |
| 5 | question_detection_with_punctuation_pool_0420 | What does MSG stand for ? | B | B | yes |

### Rule 37: 5/5

Articulated rule: Label B if and only if the input is a factual, information-seeking question; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0497 | like you could n't smell this turkey rotting from miles away . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0000 | one of the more irritating cartoons you will see this , or any , year . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0109 | this one is definitely one to skip , even for horror movie fanatics . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0281 | When were the Olympic Games in which Nadia Comaneci became popular played ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0241 | a warm but realistic meditation on friendship , family and affection . | A | A | yes |

### Rule 38: 5/5

Articulated rule: Label A if and only if the input is a movie review or other subjective opinion text; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0150 | it 's dumb , but more importantly , it 's just not scary . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0116 | Who portrayed Carl Bernstein in All the President 's Men ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0154 | How do you make the color purple ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0068 | a study in shades of gray , offering itself up in subtle plot maneuvers ... | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0485 | but it could have been worse . | A | A | yes |

### Rule 39: 4/5

Articulated rule: Label A if and only if the input is a subjective, opinionated movie-review-style statement; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0050 | What 's the singular of dice ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0262 | a movie with a real anarchic flair . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0384 | too much of it feels unfocused and underdeveloped . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0429 | a tender , heartfelt family drama . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0311 | the film will play equally well on both the standard and giant screens . | A | B | no |

### Rule 40: 4/5

Articulated rule: Label A if and only if the input is a movie review or opinion about a film; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0344 | How much did a McDonald 's hamburger cost in 1963 ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0328 | huston nails both the glad-handing and the choking sense of hollow despair . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0150 | it 's dumb , but more importantly , it 's just not scary . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0088 | forced , familiar and thoroughly condescending . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0418 | one long string of cliches . | A | B | no |

### Rule 41: 5/5

Articulated rule: Label A if and only if the input is a subjective movie review or opinion about a film; label B if it is a factual question or other informational query.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0088 | forced , familiar and thoroughly condescending . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0305 | Why were red M&Ms discontinued then brought back ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0408 | What is the difference between Neoclassical art and Romanticism art ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0112 | What is Jell-O made from ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0425 | What monastery was raided by Vikings in the late eighth century ? | B | B | yes |

### Rule 42: 5/5

Articulated rule: Label A if and only if the input is a subjective, opinionated movie-review style statement; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0478 | How close a cousin was Franklin D. to Theodore Roosevelt ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0171 | it proves quite compelling as an intense , brooding character study . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0475 | What is the largest city in Germany ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0487 | Who was Bonnie Blue Butler 's father ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0125 | What is a fear of machinery ? | B | B | yes |

### Rule 43: 5/5

Articulated rule: Label A if and only if the input is a movie review or opinionated critique; label B if it is a factual question or general knowledge query.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0005 | the film is quiet , threatening and unforgettable . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0019 | Which high schools are included in the South Florida Ice Hockey league ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0091 | the performances take the movie to a higher level . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0306 | as unseemly as its title suggests . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0047 | What clause in the U.S. Constitution may not be changed , altered or amended ? | B | B | yes |

### Rule 44: 3/5

Articulated rule: Label A if and only if the input is a negative or critical movie review; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0042 | his healthy sense of satire is light and fun ... | A | B | no |
| 2 | question_detection_with_punctuation_pool_0038 | What are the biggest Indian airports ? | B | B | yes |
| 3 | question_detection_with_punctuation_pool_0099 | What do you call a group of geese ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0204 | the best film about baseball to hit theaters since field of dreams . | A | B | no |
| 5 | question_detection_with_punctuation_pool_0437 | What state is the geographic center of the lower 48 states ? | B | B | yes |

### Rule 45: 5/5

Articulated rule: Label A if and only if the input is a movie review or other opinionated statement expressing sentiment; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0065 | i do n't mind having my heartstrings pulled , but do n't treat me like a fool . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0352 | indifferently implausible popcorn programmer of a movie . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0205 | looks and feels like a project better suited for the small screen . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0415 | Where is the Rose Bowl played ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0022 | less dizzying than just dizzy , the jaunt is practically over before it begins . | A | A | yes |

### Rule 46: 5/5

Articulated rule: Label A if and only if the input is a subjective movie-review style opinion, and label B if it is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0336 | What baseball team was the first to make numbers part of their uniform ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0314 | dense with characters and contains some thrilling moments . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0357 | What does the term 3 mean to a newspaper editor ? | B | B | yes |
| 4 | question_detection_with_punctuation_pool_0185 | it 's fascinating to see how bettany and mcdowell play off each other . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0392 | good old-fashioned slash-and-hack is back ! | A | A | yes |

### Rule 47: 5/5

Articulated rule: Label A if and only if the input is a subjective opinion or review-like statement rather than a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0416 | a by-the-numbers patient/doctor pic that covers all the usual ground | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0221 | it 's also , clearly , great fun . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0450 | old-form moviemaking at its best . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0255 | against all odds in heaven and hell , it creeped me out just fine . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0114 | How do you write a correct critical analysis of a poem ? | B | B | yes |

### Rule 48: 5/5

Articulated rule: Label B if and only if the input is a factual information-seeking question; Label A if it is a subjective opinion or review statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0386 | Who wrote NN DT NNP NNP '' ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0456 | no way i can believe this load of junk . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0179 | a deep and meaningful film . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0171 | it proves quite compelling as an intense , brooding character study . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0453 | What are Halloween 's colors ? | B | B | yes |

### Rule 49: 4/5

Articulated rule: Label A if and only if the input is a positive movie review; otherwise label B for factual questions.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0188 | What is the size of Argentina ? | B | B | yes |
| 2 | question_detection_with_punctuation_pool_0498 | plays like a volatile and overlong w magazine fashion spread . | A | B | no |
| 3 | question_detection_with_punctuation_pool_0234 | a quiet treasure -- a film to be savored . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0455 | What are the languages spoken by the natives in Afghanistan ? | B | B | yes |
| 5 | question_detection_with_punctuation_pool_0365 | What is Britain 's possession on the Chinese mainland ? | B | B | yes |

### Rule 50: 5/5

Articulated rule: Label A if and only if the input is a movie review or opinionated critique, and Label B if it is a factual question asking for information.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | question_detection_with_punctuation_pool_0485 | but it could have been worse . | A | A | yes |
| 2 | question_detection_with_punctuation_pool_0236 | you wo n't like roger , but you will quickly recognize him . | A | A | yes |
| 3 | question_detection_with_punctuation_pool_0287 | i had to look away - this was god awful . | A | A | yes |
| 4 | question_detection_with_punctuation_pool_0304 | it 's a grab bag of genres that do n't add up to a whole lot of sense . | A | A | yes |
| 5 | question_detection_with_punctuation_pool_0385 | What does the acronym CPR mean ? | B | B | yes |

