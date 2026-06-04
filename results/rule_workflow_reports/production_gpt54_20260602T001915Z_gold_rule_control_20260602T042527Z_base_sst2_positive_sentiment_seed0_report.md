# Gold-Rule Application Control: sst2_positive_sentiment

Run ID: `production_gpt54_20260602T001915Z_gold_rule_control_20260602T042527Z_base_sst2_positive_sentiment_seed0`

Correct canonical rule: Label A iff the sentence expresses positive sentiment.

Correct prompt-facing rule: Label B iff the sentence expresses positive sentiment; Label A otherwise.

## Summary

- Gold rules tested: `1`
- Rule-application calls: `50`
- Rule-application accuracy: `46/50` = `0.920`
- Nonparseable rate: `0.000`

## Settings

- Rule-application model: `gpt-5.4`
- Seed: `0`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Detailed Evaluations

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0362 | what the director ca n't do is make either of val kilmer 's two personas interesting or worth caring about . | A | A | yes |
| 2 | sst2_positive_sentiment_pool_0336 | it moves quickly , adroitly , and without fuss ; it does n't give you time to reflect on the inanity -- and the cold war datedness -- of its premise . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0100 | but it could have been worse . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0403 | there 's no emotional pulse to solaris . | A | A | yes |
| 5 | sst2_positive_sentiment_pool_0034 | ultimately feels empty and unsatisfying , like swallowing a communion wafer without the wine . | A | A | yes |
| 6 | sst2_positive_sentiment_pool_0276 | as a rumor of angels reveals itself to be a sudsy tub of supernatural hokum , not even ms. redgrave 's noblest efforts can redeem it from hopeless sentimentality . | A | A | yes |
| 7 | sst2_positive_sentiment_pool_0464 | ` easily my choice for one of the year 's best films . ' | B | B | yes |
| 8 | sst2_positive_sentiment_pool_0470 | ( d ) oes n't bother being as cloying or preachy as equivalent evangelical christian movies -- maybe the filmmakers know that the likely audience will already be among the faithful . | B | A | no |
| 9 | sst2_positive_sentiment_pool_0499 | further proof that the epicenter of cool , beautiful , thought-provoking foreign cinema is smack-dab in the middle of dubya 's axis of evil . | B | B | yes |
| 10 | sst2_positive_sentiment_pool_0413 | the piece plays as well as it does thanks in large measure to anspaugh 's three lead actresses . | B | B | yes |
| 11 | sst2_positive_sentiment_pool_0253 | it 's a cookie-cutter movie , a cut-and-paste job . | A | A | yes |
| 12 | sst2_positive_sentiment_pool_0265 | puts a human face on a land most westerners are unfamiliar with . | B | B | yes |
| 13 | sst2_positive_sentiment_pool_0234 | feels too formulaic and too familiar to produce the transgressive thrills of early underground work . | A | A | yes |
| 14 | sst2_positive_sentiment_pool_0021 | it 's hard to like a film about a guy who is utterly unlikeable , and shiner , starring michael caine as an aging british boxing promoter desperate for a taste of fame and fortune , is certainly that . | A | A | yes |
| 15 | sst2_positive_sentiment_pool_0149 | a pleasant enough romance with intellectual underpinnings , the kind of movie that entertains even as it turns maddeningly predictable . | B | B | yes |
| 16 | sst2_positive_sentiment_pool_0354 | ... plot holes so large and obvious a marching band might as well be stomping through them in clown clothes , playing a college football fight song on untuned instruments . | A | A | yes |
| 17 | sst2_positive_sentiment_pool_0223 | ... an otherwise intense , twist-and-turn thriller that certainly should n't hurt talented young gaghan 's resume . | B | B | yes |
| 18 | sst2_positive_sentiment_pool_0023 | the jabs it employs are short , carefully placed and dead-center . | B | B | yes |
| 19 | sst2_positive_sentiment_pool_0480 | it takes a strange kind of laziness to waste the talents of robert forster , anne meara , eugene levy , and reginald veljohnson all in the same movie . | A | A | yes |
| 20 | sst2_positive_sentiment_pool_0004 | it seems like i have been waiting my whole life for this movie and now i ca n't wait for the sequel . | B | B | yes |
| 21 | sst2_positive_sentiment_pool_0057 | a dumb movie with dumb characters doing dumb things and you have to be really dumb not to see where this is going . | A | A | yes |
| 22 | sst2_positive_sentiment_pool_0212 | kinnear does n't aim for our sympathy , but rather delivers a performance of striking skill and depth . | B | B | yes |
| 23 | sst2_positive_sentiment_pool_0446 | it 's a demented kitsch mess ( although the smeary digital video does match the muddled narrative ) , but it 's savvy about celebrity and has more guts and energy than much of what will open this year . | B | B | yes |
| 24 | sst2_positive_sentiment_pool_0263 | jones ... does offer a brutal form of charisma . | B | B | yes |
| 25 | sst2_positive_sentiment_pool_0118 | a fitfully amusing romp that , if nothing else , will appeal to fans of malcolm in the middle and its pubescent star , frankie muniz . | B | B | yes |
| 26 | sst2_positive_sentiment_pool_0497 | complete lack of originality , cleverness or even visible effort | A | A | yes |
| 27 | sst2_positive_sentiment_pool_0044 | even the finest chef ca n't make a hotdog into anything more than a hotdog , and robert de niro ca n't make this movie anything more than a trashy cop buddy comedy . | A | A | yes |
| 28 | sst2_positive_sentiment_pool_0062 | the son 's room is a triumph of gentility that earns its moments of pathos . | B | B | yes |
| 29 | sst2_positive_sentiment_pool_0315 | ( director ) o'fallon manages to put some lovely pictures up on the big screen , but his skill at telling a story -- he also contributed to the screenplay -- falls short . | A | A | yes |
| 30 | sst2_positive_sentiment_pool_0222 | while the resident evil games may have set new standards for thrills , suspense , and gore for video games , the movie really only succeeds in the third of these . | A | A | yes |
| 31 | sst2_positive_sentiment_pool_0165 | it inspires a continuing and deeply satisfying awareness of the best movies as monumental ` picture shows . ' | B | B | yes |
| 32 | sst2_positive_sentiment_pool_0063 | for the most part , it 's a work of incendiary genius , steering clear of knee-jerk reactions and quick solutions . | B | B | yes |
| 33 | sst2_positive_sentiment_pool_0233 | the vitality of the actors keeps the intensity of the film high , even as the strafings blend together . | B | B | yes |
| 34 | sst2_positive_sentiment_pool_0277 | another in-your-face wallow in the lower depths made by people who have never sung those blues . | A | A | yes |
| 35 | sst2_positive_sentiment_pool_0334 | this surreal gilliam-esque film is also a troubling interpretation of ecclesiastes . | B | A | no |
| 36 | sst2_positive_sentiment_pool_0075 | chabrol has taken promising material for a black comedy and turned it instead into a somber chamber drama . | A | A | yes |
| 37 | sst2_positive_sentiment_pool_0495 | vera 's technical prowess ends up selling his film short ; he smoothes over hard truths even as he uncovers them . | A | A | yes |
| 38 | sst2_positive_sentiment_pool_0193 | the quality of the art combined with the humor and intelligence of the script allow the filmmakers to present the biblical message of forgiveness without it ever becoming preachy or syrupy . | B | B | yes |
| 39 | sst2_positive_sentiment_pool_0415 | something akin to a japanese alice through the looking glass , except that it seems to take itself far more seriously . | B | A | no |
| 40 | sst2_positive_sentiment_pool_0058 | a spellbinding african film about the modern condition of rootlessness , a state experienced by millions around the globe . | B | B | yes |
| 41 | sst2_positive_sentiment_pool_0101 | every time you look , sweet home alabama is taking another bummer of a wrong turn . | A | A | yes |
| 42 | sst2_positive_sentiment_pool_0134 | ( lawrence bounces ) all over the stage , dancing , running , sweating , mopping his face and generally displaying the wacky talent that brought him fame in the first place . | B | B | yes |
| 43 | sst2_positive_sentiment_pool_0115 | it haunts you , you ca n't forget it , you admire its conception and are able to resolve some of the confusions you had while watching it . | B | B | yes |
| 44 | sst2_positive_sentiment_pool_0348 | woody allen 's latest is an ambling , broad comedy about all there is to love -- and hate -- about the movie biz . | B | A | no |
| 45 | sst2_positive_sentiment_pool_0486 | sit through this one , and you wo n't need a magic watch to stop time ; your dvd player will do it for you . | A | A | yes |
| 46 | sst2_positive_sentiment_pool_0294 | if steven soderbergh 's ` solaris ' is a failure it is a glorious failure . | B | B | yes |
| 47 | sst2_positive_sentiment_pool_0498 | ... plays like somebody spliced random moments of a chris rock routine into what is otherwise a cliche-riddled but self-serious spy thriller . | A | A | yes |
| 48 | sst2_positive_sentiment_pool_0387 | so unassuming and pure of heart , you ca n't help but warmly extend your arms and yell ` safe ! ' | B | B | yes |
| 49 | sst2_positive_sentiment_pool_0252 | burns never really harnesses to full effect the energetic cast . | A | A | yes |
| 50 | sst2_positive_sentiment_pool_0091 | it 's clear the filmmakers were n't sure where they wanted their story to go , and even more clear that they lack the skills to get us to this undetermined destination . | A | A | yes |
