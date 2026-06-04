# Gold-Rule Application Control: pairwise_same_question_detection_with_punctuation

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_pairwise_same_question_detection_with_punctuation_seed0`

Correct canonical rule: Label A iff the two items have the same base-task category: either both satisfy the base rule or neither satisfies it. The base rule is: an item satisfies the base rule iff the input is an actual question.

Correct prompt-facing rule: Label B iff the two items have the same base-task category: either both satisfy the base rule or neither satisfies it. The base rule is: an item satisfies the base rule iff the input is an actual question; Label A otherwise.

## Summary

- Gold rules tested: `1`
- Rule-application calls: `50`
- Rule-application accuracy: `50/50` = `1.000`
- Nonparseable rate: `0.000`

## Settings

- Rule-application model: `gpt-5.4`
- Seed: `0`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Detailed Evaluations

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_question_detection_with_punctuation_pool_0362 | it 's also , clearly , great fun . What are Halloween 's colors ? | A | A | yes |
| 2 | pairwise_same_question_detection_with_punctuation_pool_0336 | Where are the British crown jewels kept ? Who is the mayor of Marbella ? | B | B | yes |
| 3 | pairwise_same_question_detection_with_punctuation_pool_0100 | How many miles is it to Ohio from North Carolina ? the most compelling wiseman epic of recent years . | A | A | yes |
| 4 | pairwise_same_question_detection_with_punctuation_pool_0403 | they should have called it gutterball . manages to be sweet and wickedly satisfying at the same time . | B | B | yes |
| 5 | pairwise_same_question_detection_with_punctuation_pool_0034 | How many people are taller than 7 feet ? but this films lacks the passion required to sell the material . | A | A | yes |
| 6 | pairwise_same_question_detection_with_punctuation_pool_0276 | Who won World War II ? What is the death toll of people dying from tuberculosis ? | B | B | yes |
| 7 | pairwise_same_question_detection_with_punctuation_pool_0464 | What is the population of Nigeria ? Who penned : `` Neither a borrower nor a lender be '' ? | B | B | yes |
| 8 | pairwise_same_question_detection_with_punctuation_pool_0470 | How can I get someone 's email address ? coughs and sputters on its own postmodern conceit . | A | A | yes |
| 9 | pairwise_same_question_detection_with_punctuation_pool_0499 | Who is the mayor of Marbella ? the film will play equally well on both the standard and giant screens . | A | A | yes |
| 10 | pairwise_same_question_detection_with_punctuation_pool_0413 | How many counties are in Indiana ? What Louisiana Senator won a seat that had been held by his father and mother ? | B | B | yes |
| 11 | pairwise_same_question_detection_with_punctuation_pool_0253 | What 's the name of the tiger that advertises for Frosted Flakes cereal ? as unseemly as its title suggests . | A | A | yes |
| 12 | pairwise_same_question_detection_with_punctuation_pool_0265 | What format was VHS 's main competition ? Which Kevin Costner movie involves the Sioux Indians ? | B | B | yes |
| 13 | pairwise_same_question_detection_with_punctuation_pool_0234 | this one is definitely one to skip , even for horror movie fanatics . my reaction in a word : disappointment . | B | B | yes |
| 14 | pairwise_same_question_detection_with_punctuation_pool_0021 | Which president was unmarried ? it 's slow -- very , very slow . | A | A | yes |
| 15 | pairwise_same_question_detection_with_punctuation_pool_0149 | How many grooves are on a dime 's edge ? against all odds in heaven and hell , it creeped me out just fine . | A | A | yes |
| 16 | pairwise_same_question_detection_with_punctuation_pool_0354 | What animals can live the longest without food ? forced , familiar and thoroughly condescending . | A | A | yes |
| 17 | pairwise_same_question_detection_with_punctuation_pool_0223 | one of the smartest takes on singles culture i 've seen in a long time . Name a South African diamond producer ? | A | A | yes |
| 18 | pairwise_same_question_detection_with_punctuation_pool_0023 | Who was the first woman to fly solo across the Atlantic ? How many counties are in Indiana ? | B | B | yes |
| 19 | pairwise_same_question_detection_with_punctuation_pool_0480 | What author landed a 468-pound marlin without harness in the early 193 's ? What attracts tourists to Reims ? | B | B | yes |
| 20 | pairwise_same_question_detection_with_punctuation_pool_0004 | What 's the second-largest island in the world ? ... the movie is just a plain old monster . | A | A | yes |
| 21 | pairwise_same_question_detection_with_punctuation_pool_0057 | What is a stratocaster ? the story and structure are well-honed . | A | A | yes |
| 22 | pairwise_same_question_detection_with_punctuation_pool_0212 | What London street is the home of British journalism ? ... nothing scary here except for some awful acting and lame special effects . | A | A | yes |
| 23 | pairwise_same_question_detection_with_punctuation_pool_0446 | this movie seems to have been written using mad-libs . What is meant by blood SED rate ? | A | A | yes |
| 24 | pairwise_same_question_detection_with_punctuation_pool_0263 | but it could have been worse . the iditarod lasts for days - this just felt like it did . | B | B | yes |
| 25 | pairwise_same_question_detection_with_punctuation_pool_0118 | What 's the U.S. Navy hymn ? the film 's tone and pacing are off almost from the get-go . | A | A | yes |
| 26 | pairwise_same_question_detection_with_punctuation_pool_0497 | not exactly the bees knees What is the size of Argentina ? | A | A | yes |
| 27 | pairwise_same_question_detection_with_punctuation_pool_0044 | Where do the adventures of `` The Swiss Family Robinson '' take place ? blanchett 's performance confirms her power once again . | A | A | yes |
| 28 | pairwise_same_question_detection_with_punctuation_pool_0062 | What 's the setting of John Le Carre 's A Small Town in Germany ? How fast is alcohol absorbed ? | B | B | yes |
| 29 | pairwise_same_question_detection_with_punctuation_pool_0315 | birthday girl is an amusing joy ride , with some surprisingly violent moments . a tender , heartfelt family drama . | B | B | yes |
| 30 | pairwise_same_question_detection_with_punctuation_pool_0222 | What attracts tourists to Reims ? What color is a giraffe 's tongue ? | B | B | yes |
| 31 | pairwise_same_question_detection_with_punctuation_pool_0165 | a quiet treasure -- a film to be savored . What country was Sir Edmund Hillary born in ? | A | A | yes |
| 32 | pairwise_same_question_detection_with_punctuation_pool_0063 | What Louisiana Senator won a seat that had been held by his father and mother ? no aspirations to social import inform the movie version . | A | A | yes |
| 33 | pairwise_same_question_detection_with_punctuation_pool_0233 | overall very good for what it 's trying to do . like you could n't smell this turkey rotting from miles away . | B | B | yes |
| 34 | pairwise_same_question_detection_with_punctuation_pool_0277 | there is no pleasure in watching a child suffer . no way i can believe this load of junk . | B | B | yes |
| 35 | pairwise_same_question_detection_with_punctuation_pool_0334 | What are the main blood vessels ? What whisky is `` known by the company it keeps '' ? | B | B | yes |
| 36 | pairwise_same_question_detection_with_punctuation_pool_0075 | What is the biggest `` thing '' humans have made ? my reaction in a word : disappointment . | A | A | yes |
| 37 | pairwise_same_question_detection_with_punctuation_pool_0495 | How is digital audio used ? Who was America 's first Public Enemy No. 1 ? | B | B | yes |
| 38 | pairwise_same_question_detection_with_punctuation_pool_0193 | the draw ( for `` big bad love '' ) is a solid performance by arliss howard . How many languages does the Pope speak ? | A | A | yes |
| 39 | pairwise_same_question_detection_with_punctuation_pool_0415 | Why does sound travel quicker through water than air ? What is the population of Mozambique ? | B | B | yes |
| 40 | pairwise_same_question_detection_with_punctuation_pool_0058 | a movie with a real anarchic flair . just embarrassment and a vague sense of shame . | B | B | yes |
| 41 | pairwise_same_question_detection_with_punctuation_pool_0101 | expect the same-old , lame-old slasher nonsense , just with different scenery . What Caribbean island is sometimes called Little England ? | A | A | yes |
| 42 | pairwise_same_question_detection_with_punctuation_pool_0134 | overall very good for what it 's trying to do . What are the main blood vessels ? | A | A | yes |
| 43 | pairwise_same_question_detection_with_punctuation_pool_0115 | What instrument does Benny Carter play ? unfortunately , it 's not silly fun unless you enjoy really bad movies . | A | A | yes |
| 44 | pairwise_same_question_detection_with_punctuation_pool_0348 | On which dates does the running of the bulls occur in Pamplona , Spain ? What term means a sexual attraction between a male and a female ? | B | B | yes |
| 45 | pairwise_same_question_detection_with_punctuation_pool_0486 | crackerjack entertainment -- nonstop romance , music , suspense and action . a woman 's pic directed with resonance by ilya chaiken . | B | B | yes |
| 46 | pairwise_same_question_detection_with_punctuation_pool_0294 | What country offered Albert Einstein its presidency in 1952 ? manages to be both repulsively sadistic and mundane . | A | A | yes |
| 47 | pairwise_same_question_detection_with_punctuation_pool_0498 | Who won World War II ? Who was the first jockey to ride two Triple Crown winners ? | B | B | yes |
| 48 | pairwise_same_question_detection_with_punctuation_pool_0387 | What was Mao , the Chinese leader 's , full name ? the draw ( for `` big bad love '' ) is a solid performance by arliss howard . | A | A | yes |
| 49 | pairwise_same_question_detection_with_punctuation_pool_0252 | How many square feet is Bill Gates ' home ? What monastery was raided by Vikings in the late eighth century ? | B | B | yes |
| 50 | pairwise_same_question_detection_with_punctuation_pool_0091 | What is the lowest level of the American judiciary ? unfortunately , it 's not silly fun unless you enjoy really bad movies . | A | A | yes |
