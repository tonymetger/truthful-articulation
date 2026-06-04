# Rule Articulation Workflow: pairwise_same_question_detection_no_punctuation

Run ID: `pairwise_same_question_detection_no_punctuation_articulation_workflow_k16_seed0_20260601T235356Z`

Correct prompt-facing rule: Label B iff the two items have the same base-task category: either both satisfy the base rule or neither satisfies it. The base rule is: an item satisfies the base rule iff the input is an actual question after punctuation has been stripped; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.972
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.972
- Rules with all evals correct: 46
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
| 1 | 5/5 | Label A if and only if exactly one of the two lines is a question. |
| 2 | 5/5 | Label A if and only if exactly one line is a question and the other is a movie-review-style sentence; otherwise label B. |
| 3 | 5/5 | Label A if and only if exactly one of the two inputs is a question and the other is a movie-review-style sentence; otherwise label B. |
| 4 | 5/5 | Label A if and only if exactly one of the two lines is a movie-review snippet/opinion and the other is a factual question. |
| 5 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement. |
| 6 | 5/5 | Label A if and only if exactly one of the two lines is a movie-review sentence and the other is a factual question. |
| 7 | 5/5 | Label A if and only if exactly one of the two lines is a question; otherwise label B. |
| 8 | 4/5 | Label A if and only if the second line is a negative movie review snippet and the first line is a general question, or vice versa; otherwise label B. |
| 9 | 5/5 | Label A if and only if exactly one of the two lines is a question; otherwise label B. |
| 10 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement. |
| 11 | 5/5 | Label A if and only if exactly one of the two lines is a question (starts with a wh-word or auxiliary), otherwise label B. |
| 12 | 5/5 | Label A if and only if exactly one of the two lines is a question. |
| 13 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is not. |
| 14 | 5/5 | Label A if and only if exactly one of the two lines is a movie-review sentence and the other is a factual question. |
| 15 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is not. |
| 16 | 5/5 | Label A if and only if exactly one of the two inputs is a question and the other is a movie-review-style statement. |
| 17 | 5/5 | Label A if and only if the two lines are from different types—one movie-review sentence and one trivia question. |
| 18 | 5/5 | Label A if and only if exactly one of the two lines is a question. |
| 19 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is a movie-review statement. |
| 20 | 5/5 | Label A if and only if exactly one of the two lines is a movie-review snippet rather than a factual question. |
| 21 | 5/5 | Label A if and only if exactly one line is a question and the other is a movie-review-style statement. |
| 22 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is a movie-review sentence. |
| 23 | 5/5 | Label A if and only if exactly one of the two lines is a question; otherwise label B. |
| 24 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement. |
| 25 | 4/5 | Label A if and only if exactly one of the two lines is a movie-review snippet and the other is a factual question. |
| 26 | 5/5 | Label A if and only if exactly one of the two lines is a natural-language question and the other is a movie-review-style statement. |
| 27 | 5/5 | Label A if and only if the two lines are of different types, with one being a question and the other a movie-review statement. |
| 28 | 5/5 | Label A if and only if exactly one of the two lines is a natural-language question and the other is not. |
| 29 | 5/5 | Label A if and only if exactly one of the two lines is a question; otherwise label B. |
| 30 | 5/5 | Label A if and only if exactly one of the two lines is a question. |
| 31 | 5/5 | Label A if and only if the two lines are of different types—one is a question and the other is a movie-review-style statement. |
| 32 | 5/5 | Label A if and only if exactly one of the two lines is a movie-review sentence and the other is a factual question. |
| 33 | 3/5 | Label A if and only if the two inputs are of different types, with one a natural-language question and the other a movie-review sentence. |
| 34 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is not. |
| 35 | 5/5 | Label A if and only if exactly one of the two inputs is a question and the other is a movie-review-style statement. |
| 36 | 5/5 | Label A if and only if exactly one of the two lines is a movie-review sentence and the other is a factual question. |
| 37 | 5/5 | Label A if and only if exactly one of the two lines is a question. |
| 38 | 5/5 | Label A if and only if exactly one of the two lines is a natural-language question and the other is a movie-review-style statement. |
| 39 | 2/5 | Label A if and only if the second input line is a question. |
| 40 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is a movie-review sentence; otherwise label B. |
| 41 | 5/5 | Label A if and only if exactly one of the two lines is a question; otherwise label B. |
| 42 | 5/5 | Label A if and only if the two lines are of different types, with one movie-review sentence and one factual question. |
| 43 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement. |
| 44 | 5/5 | Label A if and only if exactly one of the two lines is a question. |
| 45 | 5/5 | Label A if and only if exactly one of the two lines is a question; otherwise label B. |
| 46 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is not. |
| 47 | 5/5 | Label A if and only if exactly one of the two lines is a subjective movie-review snippet rather than a factual question. |
| 48 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement. |
| 49 | 5/5 | Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement. |
| 50 | 5/5 | Label A if and only if exactly one of the two inputs is a movie-review sentiment sentence and the other is a factual question. |

## Detailed Evaluations

### Rule 1: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0375 | chilling well acted and finely directed david jacobson s dahmer a broad melodramatic estrogen opera that s pretty toxic in its own right | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0348 | On which dates does the running of the bulls occur in Pamplona Spain What term means a sexual attraction between a male and a female | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0103 | What s the setting of John Le Carre s A Small Town in Germany CNN is an acronym for what | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0417 | add yet another hat to a talented head clooney s a good director How many times has Harold Stassen announced a drive for the White House | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0035 | Where is the Rose Bowl played it s fascinating to see how bettany and mcdowell play off each other | A | A | yes |

### Rule 2: 5/5

Articulated rule: Label A if and only if exactly one line is a question and the other is a movie-review-style sentence; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0136 | What comic of TV s golden age went by the motto Anything for a laugh collateral damage finally delivers the goods for schwarzenegger fans | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0271 | What is the average weight for a man a marvel like none you ve seen | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0128 | entertains by providing good lively company old form moviemaking at its best | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0484 | What attracts tourists to Reims What international amateur sports spectacle was first telecast in 1956 | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0430 | crackerjack entertainment nonstop romance music suspense and action What s the singular of dice | A | A | yes |

### Rule 3: 5/5

Articulated rule: Label A if and only if exactly one of the two inputs is a question and the other is a movie-review-style sentence; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0048 | Where in the Americas is it only 47 miles from the Atlantic to the Pacific add yet another hat to a talented head clooney s a good director | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0253 | What s the name of the tiger that advertises for Frosted Flakes cereal as unseemly as its title suggests | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0414 | What term means a sexual attraction between a male and a female it s a stunning lyrical work of considerable force and truth | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0008 | How do I know someone is truly in love with me too much of the humor falls flat | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0363 | the film will play equally well on both the standard and giant screens Why do we ask for the check and not the bill at a restaurant | A | A | yes |

### Rule 4: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a movie-review snippet/opinion and the other is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0378 | this movie seems to have been written using mad libs What is New England s highest mountain | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0297 | it s not the ultimate depression era gangster movie What did the ancients call the four great elements | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0145 | What started in 1849 when gold was discovered at Sutter s Mill Who penned Neither a borrower nor a lender be | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0124 | What Don McLean song laments the day Buddy Holly died it treats women like idiots | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0381 | the jabs it employs are short carefully placed and dead center very psychoanalytical provocatively so and also refreshingly literary | B | B | yes |

### Rule 5: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0039 | What is a fear of robbers Which high schools are included in the South Florida Ice Hockey league | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0193 | the draw for big bad love is a solid performance by arliss howard How many languages does the Pope speak | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0010 | What island is home to statues called Mauis During which season do most thunderstorms occur | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0157 | What operating system do IBM compatible machines use Whom does Uncle Duke s girl friend Honey room with | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0176 | What year did WWII begin In South Korea how many American Soldiers are there | B | B | yes |

### Rule 6: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a movie-review sentence and the other is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0258 | a better title for all concerned might be swept under the rug no aspirations to social import inform the movie version | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0292 | What country was Sir Edmund Hillary born in What s the singular of dice | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0361 | a fast funny highly enjoyable movie a quiet pure elliptical film | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0411 | so too is this comedy about mild culture clashing in today s new delhi Which Kevin Costner movie involves the Sioux Indians | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0472 | What monastery was raided by Vikings in the late eighth century a valueless kiddie paean to pro basketball underwritten by the nba | A | A | yes |

### Rule 7: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0156 | During which season do most thunderstorms occur What s the name of the tiger that advertises for Frosted Flakes cereal | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0329 | What Caribbean island is sometimes called Little England seldom has a movie so closely matched the spirit of a man and his work | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0331 | that is a compliment to kuras and miller Where do the adventures of The Swiss Family Robinson take place | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0436 | What British TV series featured Emma Peel the minor figures surrounding bobby form a gritty urban mosaic | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0369 | When was Algeria colonized What is the geographical center of the US including Alaska and Hawaii | B | B | yes |

### Rule 8: 4/5

Articulated rule: Label A if and only if the second line is a negative movie review snippet and the first line is a general question, or vice versa; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0412 | Who was the first jockey to ride two Triple Crown winners not only unfunny but downright repellent | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0277 | there is no pleasure in watching a child suffer no way i can believe this load of junk | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0463 | What is Rona Barrett s married name What is the oldest university in the US | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0027 | a solid examination of the male midlife crisis Which college did Dikembe Mutombo play basketball for | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0104 | binoche makes it interesting trying to find out What is Jell O made from | A | B | no |

### Rule 9: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0103 | What s the setting of John Le Carre s A Small Town in Germany CNN is an acronym for what | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0122 | the story and structure are well honed What does the term 3 mean to a newspaper editor | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0063 | What Louisiana Senator won a seat that had been held by his father and mother no aspirations to social import inform the movie version | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0488 | it treats women like idiots How many corners does a spritsail have | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0341 | a poignant artfully crafted meditation on mortality What does a chef coddle eggs in | A | A | yes |

### Rule 10: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0041 | What disease plagued Europe Africa and Asia When were the Olympic Games in which Nadia Comaneci became popular played | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0298 | What makes a clitoris sensitive an occasionally funny but overall limp fish out of water story | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0300 | What international amateur sports spectacle was first telecast in 1956 What is the lowest level of the American judiciary | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0177 | What is usenet for the Internet How much did Lucy Van Pelt originally charge for psychiatric sessions | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0410 | a tender heartfelt family drama the end result is a film that s neither | B | B | yes |

### Rule 11: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question (starts with a wh-word or auxiliary), otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0068 | What is the average weight for a man it has all the excitement of eating oatmeal | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0050 | What is the difference between a preface and a foreword Which Kevin Costner movie involves the Sioux Indians | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0300 | What international amateur sports spectacle was first telecast in 1956 What is the lowest level of the American judiciary | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0209 | What brand of white rum is still made in Cuba a better title for all concerned might be swept under the rug | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0162 | that s pure pr hype On which dates does the running of the bulls occur in Pamplona Spain | A | A | yes |

### Rule 12: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0243 | Where is the Rose Bowl played What magic does Mandrake employ | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0011 | it proves quite compelling as an intense brooding character study Which Kevin Costner movie involves the Sioux Indians | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0413 | How many counties are in Indiana What Louisiana Senator won a seat that had been held by his father and mother | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0291 | What does the acronym CPR mean What North American city sprouts the most parking meters | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0482 | among the year s most intriguing explorations of alientation How do they produce vitamins | A | A | yes |

### Rule 13: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is not.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0087 | What city is served by Tempelhol Airport i d have to say the star and director are the big problems here | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0046 | it wants to tweak them with a taste of tangy new humor How do hermit crabs reproduce | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0183 | a woman s pic directed with resonance by ilya chaiken What international amateur sports spectacle was first telecast in 1956 | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0023 | Who was the first woman to fly solo across the Atlantic How many counties are in Indiana | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0482 | among the year s most intriguing explorations of alientation How do they produce vitamins | A | A | yes |

### Rule 14: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a movie-review sentence and the other is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0038 | What predators exist on Antarctica turns potentially forgettable formula into something strangely diverting | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0238 | What ship did Lloyd M Bucher command What did the ancients call the four great elements | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0259 | as vulgar as it is banal just one bad idea after another | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0140 | no aspirations to social import inform the movie version it s a beautiful madness | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0362 | it s also clearly great fun What are Halloween s colors | A | A | yes |

### Rule 15: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is not.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0387 | What was Mao the Chinese leader s full name the draw for big bad love is a solid performance by arliss howard | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0456 | What was Mao the Chinese leader s full name What was William F Cody s better known name | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0297 | it s not the ultimate depression era gangster movie What did the ancients call the four great elements | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0444 | a sequence of ridiculous shoot em up scenes What does a tarantula eat | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0151 | What did John Hinckley do to impress Jodie Foster the film s tone and pacing are off almost from the get go | A | A | yes |

### Rule 16: 5/5

Articulated rule: Label A if and only if exactly one of the two inputs is a question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0151 | What did John Hinckley do to impress Jodie Foster the film s tone and pacing are off almost from the get go | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0460 | all that s missing is the spontaneity originality and delight it s not the ultimate depression era gangster movie | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0343 | How many cherubs are there on a Trivial Pursuit board What is the oldest university in the US | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0377 | What is the difference between a bottle and a jar the humor is forced and heavy handed and occasionally simply unpleasant | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0241 | Who was America s first Public Enemy No 1 a movie with a real anarchic flair | A | A | yes |

### Rule 17: 5/5

Articulated rule: Label A if and only if the two lines are from different types—one movie-review sentence and one trivia question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0156 | During which season do most thunderstorms occur What s the name of the tiger that advertises for Frosted Flakes cereal | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0186 | i ll bet the video game is a lot more fun than the film What is Britain s possession on the Chinese mainland | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0341 | a poignant artfully crafted meditation on mortality What does a chef coddle eggs in | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0117 | dense with characters and contains some thrilling moments you wo n t like roger but you will quickly recognize him | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0337 | unfortunately it s not silly fun unless you enjoy really bad movies it s also clearly great fun | B | B | yes |

### Rule 18: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0089 | What Caribbean island is sometimes called Little England What country s capital is Tirana | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0097 | the son s room is a triumph of gentility that earns its moments of pathos collateral damage finally delivers the goods for schwarzenegger fans | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0154 | What does a tarantula eat it s fascinating to see how bettany and mcdowell play off each other | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0012 | What color tennis balls are used at Wimbledon What South Korean city is served by Kimpo International Airport | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0373 | Where can I find information on becoming a journalist What are two plants that clothes are made from | B | B | yes |

### Rule 19: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is a movie-review statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0037 | birthday girl is an amusing joy ride with some surprisingly violent moments a quiet treasure a film to be savored | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0387 | What was Mao the Chinese leader s full name the draw for big bad love is a solid performance by arliss howard | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0290 | Who was Bonnie Blue Butler s father the time machine is a movie that has no interest in itself | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0233 | overall very good for what it s trying to do like you could n t smell this turkey rotting from miles away | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0078 | How close a cousin was Franklin D to Theodore Roosevelt Name a South African diamond producer | B | B | yes |

### Rule 20: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a movie-review snippet rather than a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0347 | it s a beautiful madness a warm funny engaging film | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0204 | i ll bet the video game is a lot more fun than the film coughs and sputters on its own postmodern conceit | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0021 | Which president was unmarried it s slow very very slow | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0269 | beautifully observed miraculously unsentimental comedy drama the humor is forced and heavy handed and occasionally simply unpleasant | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0258 | a better title for all concerned might be swept under the rug no aspirations to social import inform the movie version | B | B | yes |

### Rule 21: 5/5

Articulated rule: Label A if and only if exactly one line is a question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0470 | How can I get someone s email address coughs and sputters on its own postmodern conceit | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0095 | it s a buggy drag What disease plagued Europe Africa and Asia | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0079 | Who invented The Muppets What author landed a 468 pound marlin without harness in the early 193 s | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0485 | the film is powerful accessible and funny and that leaves a hole in the center of the salton sea | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0004 | What s the second largest island in the world the movie is just a plain old monster | A | A | yes |

### Rule 22: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is a movie-review sentence.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0471 | an entertaining colorful action filled crime story with an intimate heart chokes on its own depiction of upper crust decorum | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0168 | challenging intermittently engrossing and unflaggingly creative comes uncomfortably close to coasting in the treads of the bicycle thief | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0184 | What baseball team was the first to make numbers part of their uniform but this films lacks the passion required to sell the material | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0177 | What is usenet for the Internet How much did Lucy Van Pelt originally charge for psychiatric sessions | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0151 | What did John Hinckley do to impress Jodie Foster the film s tone and pacing are off almost from the get go | A | A | yes |

### Rule 23: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0338 | routine harmless diversion and little else How do you convert foot pounds to foot inches | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0367 | birthday girl is an amusing joy ride with some surprisingly violent moments How many cullions does a male have | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0286 | Where can one find Rider College just as moving uplifting and funny as ever | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0003 | the film tries too hard to be funny and tries too hard to be hip Who is the only president to serve 2 non consecutive terms | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0457 | What shape shifting menace did Rom come to Earth to fight Why do people in the upper peninsula of Michagin say eh | B | B | yes |

### Rule 24: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0287 | What s the singular of dice it proves quite compelling as an intense brooding character study | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0153 | What are the languages spoken by the natives in Afghanistan Where can one find Rider College | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0365 | good film but very glum When does menstruation begin | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0058 | a movie with a real anarchic flair just embarrassment and a vague sense of shame | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0149 | How many grooves are on a dime s edge against all odds in heaven and hell it creeped me out just fine | A | A | yes |

### Rule 25: 4/5

Articulated rule: Label A if and only if exactly one of the two lines is a movie-review snippet and the other is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0034 | How many people are taller than 7 feet but this films lacks the passion required to sell the material | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0450 | When did the Carolingian period begin a wildly inconsistent emotional experience | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0230 | Who was the first woman to fly solo across the Atlantic complete lack of originality cleverness or even visible effort | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0309 | How do you make a million bucks Who won World War II | B | A | no |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0429 | What was William F Cody s better known name no telegraphing is too obvious or simplistic for this movie | A | A | yes |

### Rule 26: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a natural-language question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0106 | the story and structure are well honed it is amusing and that s all it needs to be | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0091 | What is the lowest level of the American judiciary unfortunately it s not silly fun unless you enjoy really bad movies | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0220 | it s also clearly great fun affleck and jackson are good sparring partners | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0288 | What s the second largest island in the world How much can a person be fined for having a dog on a beach | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0276 | Who won World War II What is the death toll of people dying from tuberculosis | B | B | yes |

### Rule 27: 5/5

Articulated rule: Label A if and only if the two lines are of different types, with one being a question and the other a movie-review statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0068 | What is the average weight for a man it has all the excitement of eating oatmeal | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0345 | chilling well acted and finely directed david jacobson s dahmer What is the population in India | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0005 | a magnificent drama well worth tracking down slick piece of cross promotion | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0071 | How do you make dumplings How much can a person be fined for having a dog on a beach | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0003 | the film tries too hard to be funny and tries too hard to be hip Who is the only president to serve 2 non consecutive terms | A | A | yes |

### Rule 28: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a natural-language question and the other is not.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0113 | a poignant artfully crafted meditation on mortality How do they find an epicenter | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0139 | What is the population of Nigeria the film s performances are thrilling | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0339 | What four tournaments make up tennis Grand Slam a strangely compelling and brilliantly acted psychological drama | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0073 | Who portrayed Sherlock Holmes in 14 films between 1939 and 1946 no way i can believe this load of junk | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0063 | What Louisiana Senator won a seat that had been held by his father and mother no aspirations to social import inform the movie version | A | A | yes |

### Rule 29: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0475 | there s a wickedly subversive bent to the best parts of birthday girl What is the lowest level of the American judiciary | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0262 | all that s missing is the spontaneity originality and delight How is digital audio used | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0053 | What was Joe Namath s first contract worth How many miles are there between Tel Aviv Israel and Memphis Tennessee | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0365 | good film but very glum When does menstruation begin | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0296 | What are manifest and latent function theories a poignant artfully crafted meditation on mortality | A | A | yes |

### Rule 30: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0217 | How many miles is it to Ohio from North Carolina How many states have a lemon law for new automobiles | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0138 | Which of the following men was not married to Rita Hayworth they should have called it gutterball | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0296 | What are manifest and latent function theories a poignant artfully crafted meditation on mortality | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0255 | the film is quiet threatening and unforgettable holden caulfield did it better | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0320 | Tell me what city the Kentucky Horse Park is near During which season do most thunderstorms occur | B | B | yes |

### Rule 31: 5/5

Articulated rule: Label A if and only if the two lines are of different types—one is a question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0172 | the cold turkey would ve been a far better title What is an Angelus | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0123 | too much of it feels unfocused and underdeveloped Where in the Americas is it only 47 miles from the Atlantic to the Pacific | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0300 | What international amateur sports spectacle was first telecast in 1956 What is the lowest level of the American judiciary | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0324 | it s a remarkably solid and subtly satirical tour de force What is the mascot for Notre Dame University | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0085 | smart provocative and blisteringly funny When did the Carolingian period begin | A | A | yes |

### Rule 32: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a movie-review sentence and the other is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0330 | i m just too bored to care a sequence of ridiculous shoot em up scenes | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0300 | What international amateur sports spectacle was first telecast in 1956 What is the lowest level of the American judiciary | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0225 | a quiet pure elliptical film like leon it s frustrating and still oddly likable | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0265 | What format was VHS s main competition Which Kevin Costner movie involves the Sioux Indians | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0054 | Who was Bonnie Blue Butler s father Why does sound travel quicker through water than air | B | B | yes |

### Rule 33: 3/5

Articulated rule: Label A if and only if the two inputs are of different types, with one a natural-language question and the other a movie-review sentence.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0082 | dull lifeless and amateurishly assembled Who was the most famous food editor of The New York Times | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0364 | Who won the rugby world cup in Who was the most famous food editor of The New York Times | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0413 | How many counties are in Indiana What Louisiana Senator won a seat that had been held by his father and mother | B | A | no |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0209 | What brand of white rum is still made in Cuba a better title for all concerned might be swept under the rug | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0009 | What do sailors use to measure time How do you make the color purple | B | A | no |

### Rule 34: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is not.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0440 | How many milligrams are in a gram the son s room is a triumph of gentility that earns its moments of pathos | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0283 | too much of it feels unfocused and underdeveloped What do sailors use to measure time | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0211 | overall very good for what it s trying to do minority report is exactly what the title indicates a report | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0066 | What makes a clitoris sensitive an entertaining colorful action filled crime story with an intimate heart | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0231 | one of the more intelligent children s movies to hit theaters this year Why do people in the upper peninsula of Michagin say eh | A | A | yes |

### Rule 35: 5/5

Articulated rule: Label A if and only if exactly one of the two inputs is a question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0234 | this one is definitely one to skip even for horror movie fanatics my reaction in a word disappointment | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0302 | it s a stunning lyrical work of considerable force and truth What are the first and last letters of the Greek alphabet | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0074 | What color of Monopoly properties are landed on most often one of the more irritating cartoons you will see this or any year | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0416 | What was known as the Spice Island How is water treated to make it safe to drink | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0464 | What is the population of Nigeria Who penned Neither a borrower nor a lender be | B | B | yes |

### Rule 36: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a movie-review sentence and the other is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0001 | one long string of cliches What was William F Cody s better known name | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0040 | What baseball team was the first to make numbers part of their uniform it s a remarkably solid and subtly satirical tour de force | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0354 | What animals can live the longest without food forced familiar and thoroughly condescending | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0414 | What term means a sexual attraction between a male and a female it s a stunning lyrical work of considerable force and truth | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0420 | it s fascinating to see how bettany and mcdowell play off each other Name a South African diamond producer | A | A | yes |

### Rule 37: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0497 | not exactly the bees knees What is the size of Argentina | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0000 | What format was VHS s main competition slick piece of cross promotion | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0109 | What are names of two old men who appear in the serial tv Muppets Show What disease plagued Europe Africa and Asia | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0281 | the movie is just a plain old monster good film but very glum | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0241 | Who was America s first Public Enemy No 1 a movie with a real anarchic flair | A | A | yes |

### Rule 38: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a natural-language question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0150 | enormously entertaining for moviegoers of any age it wants to tweak them with a taste of tangy new humor | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0116 | What color is a giraffe s tongue What was the first ready to eat breakfast cereal | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0154 | What does a tarantula eat it s fascinating to see how bettany and mcdowell play off each other | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0070 | Who won World War II if you re hard up for raunchy college humor this is your ticket right here | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0485 | the film is powerful accessible and funny and that leaves a hole in the center of the salton sea | B | B | yes |

### Rule 39: 2/5

Articulated rule: Label A if and only if the second input line is a question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0050 | What is the difference between a preface and a foreword Which Kevin Costner movie involves the Sioux Indians | B | A | no |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0262 | all that s missing is the spontaneity originality and delight How is digital audio used | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0384 | What was the number of people that Randy Steven Craft was convicted of killing What country s capital is Tirana | B | A | no |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0429 | What was William F Cody s better known name no telegraphing is too obvious or simplistic for this movie | A | B | no |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0311 | it s a cookie cutter movie a cut and paste job Which high schools are included in the South Florida Ice Hockey league | A | A | yes |

### Rule 40: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is a movie-review sentence; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0343 | How many cherubs are there on a Trivial Pursuit board What is the oldest university in the US | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0327 | Where can I find information about Bob Barr representative from Georgia Why does sound travel quicker through water than air | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0150 | enormously entertaining for moviegoers of any age it wants to tweak them with a taste of tangy new humor | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0088 | manages to be sweet and wickedly satisfying at the same time What is the size of Argentina | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0418 | How many miles are there between Tel Aviv Israel and Memphis Tennessee How many languages does the Pope speak | B | B | yes |

### Rule 41: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0088 | manages to be sweet and wickedly satisfying at the same time What is the size of Argentina | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0305 | the son s room is a triumph of gentility that earns its moments of pathos turns potentially forgettable formula into something strangely diverting | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0408 | What city is served by Tempelhol Airport What four tournaments make up tennis Grand Slam | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0112 | stultifyingly dumbfoundingly mind numbingly bad something like scrubbing the toilet | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0425 | i just loved every minute of this film How many miles are there between Tel Aviv Israel and Memphis Tennessee | A | A | yes |

### Rule 42: 5/5

Articulated rule: Label A if and only if the two lines are of different types, with one movie-review sentence and one factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0478 | michael gerbosi s script is economically packed with telling scenes manages to be both repulsively sadistic and mundane | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0171 | What did John Hinckley do to impress Jodie Foster if you re hard up for raunchy college humor this is your ticket right here | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0475 | there s a wickedly subversive bent to the best parts of birthday girl What is the lowest level of the American judiciary | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0487 | What double talking professor holds a doctorate in Nothing an entertaining colorful action filled crime story with an intimate heart | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0125 | there ought to be a directing license so that ed burns can have his revoked suffers from the lack of a compelling or comprehensible narrative | B | B | yes |

### Rule 43: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0005 | a magnificent drama well worth tracking down slick piece of cross promotion | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0020 | a very well made funny and entertaining picture it appears that something has been lost in the translation to the screen | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0091 | What is the lowest level of the American judiciary unfortunately it s not silly fun unless you enjoy really bad movies | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0306 | What is the world s best selling cookie i d have to say the star and director are the big problems here | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0047 | all that s missing is the spontaneity originality and delight a string of rehashed sight gags based in insipid vulgarity | B | B | yes |

### Rule 44: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0042 | an exquisitely crafted and acted tale birthday girl is an amusing joy ride with some surprisingly violent moments | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0038 | What predators exist on Antarctica turns potentially forgettable formula into something strangely diverting | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0099 | expect the same old lame old slasher nonsense just with different scenery it s fascinating to see how bettany and mcdowell play off each other | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0203 | routine harmless diversion and little else What is the difference between a preface and a foreword | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0437 | What are the Nordic nations How big is the universe actually | B | B | yes |

### Rule 45: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0066 | What makes a clitoris sensitive an entertaining colorful action filled crime story with an intimate heart | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0351 | manages to be both repulsively sadistic and mundane What disease plagued Europe Africa and Asia | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0206 | Why does sound travel quicker through water than air just embarrassment and a vague sense of shame | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0415 | Why does sound travel quicker through water than air What is the population of Mozambique | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0022 | What is the biggest thing humans have made What time of year is air travel the heaviest | B | B | yes |

### Rule 46: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is not.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0337 | unfortunately it s not silly fun unless you enjoy really bad movies it s also clearly great fun | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0314 | When does menstruation begin a grimly competent and stolid and earnest military courtroom drama | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0358 | Where in the Americas is it only 47 miles from the Atlantic to the Pacific What does a chef coddle eggs in | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0185 | chokes on its own depiction of upper crust decorum What was Joe Namath s first contract worth | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0392 | What color tennis balls are used at Wimbledon scorsese does n t give us a character worth giving a damn about | A | A | yes |

### Rule 47: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a subjective movie-review snippet rather than a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0417 | add yet another hat to a talented head clooney s a good director How many times has Harold Stassen announced a drive for the White House | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0220 | it s also clearly great fun affleck and jackson are good sparring partners | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0450 | When did the Carolingian period begin a wildly inconsistent emotional experience | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0255 | the film is quiet threatening and unforgettable holden caulfield did it better | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0114 | What is the average weight for a man you wo n t like roger but you will quickly recognize him | A | A | yes |

### Rule 48: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0385 | Why were people recruited for the Vietnam War coughs and sputters on its own postmodern conceit | A | A | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0456 | What was Mao the Chinese leader s full name What was William F Cody s better known name | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0179 | the entire movie is about a boring sad man being boring and sad rarely has leukemia looked so shimmering and benign | B | B | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0171 | What did John Hinckley do to impress Jodie Foster if you re hard up for raunchy college humor this is your ticket right here | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0454 | What operating system do IBM compatible machines use In South Korea how many American Soldiers are there | B | B | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if exactly one of the two lines is a question and the other is a movie-review-style statement.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0188 | at once half baked and overheated this movie seems to have been written using mad libs | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0498 | Who won World War II Who was the first jockey to ride two Triple Crown winners | B | B | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0235 | but it still jingles in the pocket Who was the first woman to fly solo across the Atlantic | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0455 | What South Korean city is served by Kimpo International Airport i got a headache watching this meaningless downer | A | A | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0364 | Who won the rugby world cup in Who was the most famous food editor of The New York Times | B | B | yes |

### Rule 50: 5/5

Articulated rule: Label A if and only if exactly one of the two inputs is a movie-review sentiment sentence and the other is a factual question.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_no_punctuation_pool_0485 | the film is powerful accessible and funny and that leaves a hole in the center of the salton sea | B | B | yes |
| 2 | pairwise_same_question_detection_no_punctuation_pool_0237 | my reaction in a word disappointment Why do we ask for the check and not the bill at a restaurant | A | A | yes |
| 3 | pairwise_same_question_detection_no_punctuation_pool_0287 | What s the singular of dice it proves quite compelling as an intense brooding character study | A | A | yes |
| 4 | pairwise_same_question_detection_no_punctuation_pool_0304 | How is water treated to make it safe to drink What are the main blood vessels | B | B | yes |
| 5 | pairwise_same_question_detection_no_punctuation_pool_0386 | How much pizza do Americans eat in a day What was Mao the Chinese leader s full name | B | B | yes |

