# Rule Articulation Workflow: pairwise_same_sst2_positive_sentiment

Run ID: `production_gpt54_20260602T001915Z_articulation_20260602T011542Z_pairwise_same_sst2_positive_sentiment_seed0`

Correct prompt-facing rule: Label B iff the two items have the same base-task category: either both satisfy the base rule or neither satisfies it. The base rule is: an item satisfies the base rule iff the sentence expresses positive sentiment; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.616
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.616
- Rules with all evals correct: 10
- Rules with any eval correct: 49

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
| 1 | 3/5 | Label A if and only if the second review is more positive than the first. |
| 2 | 3/5 | Label A if and only if the second review sentence is more positive than the first; otherwise label B. |
| 3 | 4/5 | Label A if and only if the second review is more negative than the first; otherwise label B. |
| 4 | 2/5 | Label A if and only if the second review snippet is negative; otherwise label B. |
| 5 | 2/5 | Label A if and only if the second review snippet is more positive than the first; otherwise label B. |
| 6 | 3/5 | Label B if and only if both quoted movie-review snippets are positive overall; otherwise label A. |
| 7 | 2/5 | Label A if and only if the second review snippet is more positive than the first; otherwise label B. |
| 8 | 1/5 | Label B if and only if the second review sentence is more positive than the first; otherwise label A. |
| 9 | 3/5 | Label A if and only if the second review snippet is more positive than the first; otherwise label B. |
| 10 | 2/5 | Label A if and only if the second review snippet is more positive than the first; otherwise label B. |
| 11 | 2/5 | Label A if and only if the second review sentence is more positive than the first; otherwise label B. |
| 12 | 4/5 | Label A if and only if the second review is more positive than the first. |
| 13 | 3/5 | Label A if and only if the second review sentence is more positive than the first; otherwise label B. |
| 14 | 5/5 | Label B if and only if both sentences in the input have the same sentiment polarity; otherwise label A. |
| 15 | 2/5 | Label A if and only if the first review snippet is more positive than the second; otherwise label B. |
| 16 | 2/5 | Label A if and only if the second review sentence is more positive than the first; otherwise label B. |
| 17 | 5/5 | Label A if and only if the second review snippet is more positive than the first; otherwise label B. |
| 18 | 5/5 | Label A if and only if the first review sentence is more positive than the second; otherwise label B. |
| 19 | 5/5 | Label A if and only if exactly one of the two sentences is positive and the other is negative. |
| 20 | 3/5 | Label A if and only if the first sentence is more negative than the second; otherwise label B. |
| 21 | 2/5 | Label B if and only if the second review snippet is more positive than the first; otherwise label A. |
| 22 | 5/5 | Label A if and only if the two reviews have opposite sentiment polarity, while Label B if and only if they have the same sentiment polarity. |
| 23 | 4/5 | Label A if and only if exactly one of the two sentences is positive and the other is negative. |
| 24 | 2/5 | Label A if and only if the second review snippet is more positive than the first; otherwise label B. |
| 25 | 0/5 | Label A if and only if the second review snippet is more positive than the first; otherwise label B. |
| 26 | 3/5 | Label A if and only if the second review is more positive than the first; otherwise label B. |
| 27 | 1/5 | Label B if and only if the second review sentence is more positive than the first; otherwise label A. |
| 28 | 1/5 | Label A if and only if the first review snippet is more negative than the second; otherwise label B. |
| 29 | 1/5 | Label B if and only if the second review snippet is more positive than the first; otherwise label A. |
| 30 | 2/5 | Label A if and only if the second review sentence is more positive than the first; otherwise label B. |
| 31 | 1/5 | Label A if and only if the first review snippet is more positive than the second; otherwise label B. |
| 32 | 4/5 | Label A if and only if the second review snippet is more positive than the first; otherwise label B. |
| 33 | 2/5 | Label B if and only if the second review snippet is more positive than the first; otherwise label A. |
| 34 | 5/5 | Label A if and only if the two reviews have opposite sentiment polarity, whereas Label B if and only if they have the same sentiment polarity. |
| 35 | 3/5 | Label B if and only if the second review sentence is more positive than the first; otherwise label A. |
| 36 | 2/5 | Label A if and only if the second review snippet is more positive than the first; otherwise label B. |
| 37 | 5/5 | Label A if and only if exactly one of the two sentences is positive and the other is negative. |
| 38 | 2/5 | Label B if and only if the second review snippet is more positive than the first; otherwise label A. |
| 39 | 5/5 | Label B if and only if both sentences have the same sentiment polarity; otherwise label A. |
| 40 | 4/5 | Label A if and only if the second review is more positive than the first. |
| 41 | 4/5 | Label A if and only if the second review sentence is more positive than the first; otherwise label B. |
| 42 | 3/5 | Label A if and only if the second review snippet is more positive than the first. |
| 43 | 4/5 | Label A if and only if the second review is more negative than the first. |
| 44 | 3/5 | Label A if and only if the second review snippet is more positive than the first; otherwise label B. |
| 45 | 4/5 | Label A if and only if the second review snippet is more negative than the first; otherwise label B. |
| 46 | 3/5 | Label A if and only if the first review snippet is more positive than the second; otherwise label B. |
| 47 | 5/5 | Label A if and only if exactly one of the two sentences is negative and the other is positive. |
| 48 | 4/5 | Label A if and only if the two sentences have opposite sentiment polarity, while Label B if and only if they have the same overall sentiment polarity. |
| 49 | 5/5 | Label A if and only if exactly one of the two sentences is positive and the other is negative; otherwise label B. |
| 50 | 4/5 | Label A if and only if the first review snippet is more positive than the second; otherwise label B. |

## Detailed Evaluations

### Rule 1: 3/5

Articulated rule: Label A if and only if the second review is more positive than the first.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0375 | this re-do is so dumb and so exploitative in its violence that , ironically , it becomes everything that the rather clumsy original was railing against . once the 50 year old benigni appears as the title character , we find ourselves longing for the block of wood to come back . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0348 | if you are an actor who can relate to the search for inner peace by dramatically depicting the lives of others onstage , then esther 's story is a compelling quest for truth . this is human comedy at its most amusing , interesting and confirming . | B | A | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0103 | travels a fascinating arc from hope and euphoria to reality and disillusionment . what better message than ` love thyself ' could young women of any size receive ? | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0417 | or doing last year 's taxes with your ex-wife . ` de niro ... is a veritable source of sincere passion that this hollywood contrivance orbits around . ' | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0035 | something akin to a japanese alice through the looking glass , except that it seems to take itself far more seriously . ... the movie is just a plain old monster . | A | B | no |

### Rule 2: 3/5

Articulated rule: Label A if and only if the second review sentence is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0136 | it confirms fincher 's status as a film maker who artfully bends technical know-how to the service of psychological insight . the reality of the new live-action pinocchio he directed , cowrote and starred in borders on the grotesque . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0271 | the primitive force of this film seems to bubble up from the vast collective memory of the combatants . care deftly captures the wonder and menace of growing up , but he never really embraces the joy of fuhrman 's destructive escapism or the grace-in-rebellion found by his characters . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0128 | when leguizamo finally plugged an irritating character late in the movie . characters still need to function according to some set of believable and comprehensible impulses , no matter how many drugs they do or how much artistic license avary employs . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0484 | two hours fly by -- opera 's a pleasure when you do n't have to endure intermissions -- and even a novice to the form comes away exhilarated . a poignant , artfully crafted meditation on mortality . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0430 | a nightmare date with a half-formed wit done a great disservice by a lack of critical distance and a sad trust in liberal arts college bumper sticker platitudes . what distinguishes time of favor from countless other thrillers is its underlying concern with the consequences of words and with the complicated emotions fueling terrorist acts . | A | A | yes |

### Rule 3: 4/5

Articulated rule: Label A if and only if the second review is more negative than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0048 | a painfully funny ode to bad behavior . or doing last year 's taxes with your ex-wife . | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0253 | the movie 's relatively simple plot and uncomplicated morality play well with the affable cast . i sympathize with the plight of these families , but the movie does n't do a very good job conveying the issue at hand . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0414 | this is human comedy at its most amusing , interesting and confirming . the lower your expectations , the more you 'll enjoy it . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0008 | a full world has been presented onscreen , not some series of carefully structured plot points building to a pat resolution . even with a green mohawk and a sheet of fire-red flame tattoos covering his shoulder , however , kilmer seems to be posing , rather than acting . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0363 | they should have called it gutterball . an exquisitely crafted and acted tale . | A | B | no |

### Rule 4: 2/5

Articulated rule: Label A if and only if the second review snippet is negative; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0378 | it has its moments of swaggering camaraderie , but more often just feels generic , derivative and done to death . this flick is about as cool and crowd-pleasing as a documentary can get . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0297 | the film 's hackneyed message is not helped by the thin characterizations , nonexistent plot and pretentious visual style . a gripping movie , played with performances that are all understated and touching . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0145 | without ever becoming didactic , director carlos carrera expertly weaves this novelistic story of entangled interrelationships and complex morality . my big fat greek wedding uses stereotypes in a delightful blend of sweet romance and lovingly dished out humor . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0124 | worth watching for dong jie 's performance -- and for the way it documents a culture in the throes of rapid change . an occasionally funny , but overall limp , fish-out-of-water story . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0381 | irwin is a man with enough charisma and audacity to carry a dozen films , but this particular result is ultimately held back from being something greater . there seems to be no clear path as to where the story 's going , or how long it 's going to take to get there . | B | A | no |

### Rule 5: 2/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0039 | there has always been something likable about the marquis de sade . trademark american triteness and simplicity are tossed out the window with the intelligent french drama that deftly explores the difficult relationship between a father and son . | B | A | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0193 | scorsese does n't give us a character worth giving a damn about . the sort of film that makes me miss hitchcock , but also feel optimistic that there 's hope for popular cinema yet . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0010 | a romantic comedy enriched by a sharp eye for manners and mores . with rabbit-proof fence , noyce has tailored an epic tale into a lean , economical movie . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0157 | it 's refreshing to see a girl-power movie that does n't feel it has to prove anything . based on a devilishly witty script by heather mcgowan and niels mueller , the film gets great laughs , but never at the expense of its characters | B | A | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0176 | the fly-on-the-wall method used to document rural french school life is a refreshing departure from the now more prevalent technique of the docu-makers being a visible part of their work . the quality of the art combined with the humor and intelligence of the script allow the filmmakers to present the biblical message of forgiveness without it ever becoming preachy or syrupy . | B | A | no |

### Rule 6: 3/5

Articulated rule: Label B if and only if both quoted movie-review snippets are positive overall; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0258 | so unremittingly awful that labeling it a dog probably constitutes cruelty to canines . you really have to wonder how on earth anyone , anywhere could have thought they 'd make audiences guffaw with a script as utterly diabolical as this . | B | A | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0292 | a taut psychological thriller that does n't waste a moment of its two-hour running time . what distinguishes time of favor from countless other thrillers is its underlying concern with the consequences of words and with the complicated emotions fueling terrorist acts . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0361 | i thought my own watch had stopped keeping time as i slogged my way through clockstoppers . an unwise amalgam of broadcast news and vibes . | B | A | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0411 | but this films lacks the passion required to sell the material . there 's really only one good idea in this movie , but the director runs with it and presents it with an unforgettable visual panache . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0472 | the movie achieves as great an impact by keeping these thoughts hidden as ... ( quills ) did by showing them . on the whole , the movie lacks wit , feeling and believability to compensate for its incessant coarseness and banality . | A | A | yes |

### Rule 7: 2/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0156 | with rabbit-proof fence , noyce has tailored an epic tale into a lean , economical movie . the movie 's relatively simple plot and uncomplicated morality play well with the affable cast . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0329 | a marvel like none you 've seen . it 's inoffensive , cheerful , built to inspire the young people , set to an unending soundtrack of beach party pop numbers and aside from its remarkable camerawork and awesome scenery , it 's about as exciting as a sunburn . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0331 | ... a hollow joke told by a cinematic gymnast having too much fun embellishing the misanthropic tale to actually engage it . an effectively creepy , fear-inducing ( not fear-reducing ) film from japanese director hideo nakata , who takes the superstitious curse on chain letters and actually applies it . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0436 | the format gets used best ... to capture the dizzying heights achieved by motocross and bmx riders , whose balletic hotdogging occasionally ends in bone-crushing screwups . vera 's technical prowess ends up selling his film short ; he smoothes over hard truths even as he uncovers them . | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0369 | in a way , the film feels like a breath of fresh air , but only to those that allow it in . a compelling spanish film about the withering effects of jealousy in the life of a young monarch whose sexual passion for her husband becomes an obsession . | B | A | no |

### Rule 8: 1/5

Articulated rule: Label B if and only if the second review sentence is more positive than the first; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0412 | the son 's room is a triumph of gentility that earns its moments of pathos . davis ... is so enamored of her own creation that she ca n't see how insufferable the character is . | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0277 | sustains its dreamlike glide through a succession of cheesy coincidences and voluptuous cheap effects , not the least of which is rebecca romijn-stamos . for all its impressive craftsmanship , and despite an overbearing series of third-act crescendos , lily chou-chou never really builds up a head of emotional steam . | B | A | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0463 | visually imaginative , thematically instructive and thoroughly delightful , it takes us on a roller-coaster ride from innocence to experience without even a hint of that typical kiddie-flick sentimentality . the minor figures surrounding ( bobby ) ... form a gritty urban mosaic . | B | A | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0027 | the moviegoing equivalent of going to a dinner party and being forced to watch the host and hostess 's home video of their baby 's birth . it 's the chemistry between the women and the droll scene-stealing wit and wolfish pessimism of anna chancellor that makes this `` two weddings and a funeral '' fun . | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0104 | this piece of channel 5 grade trash is , quite frankly , an insult to the intelligence of the true genre enthusiast . a rarity among recent iranian films : it 's a comedy full of gentle humor that chides the absurdity of its protagonist 's plight . | A | B | no |

### Rule 9: 3/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0103 | travels a fascinating arc from hope and euphoria to reality and disillusionment . what better message than ` love thyself ' could young women of any size receive ? | B | A | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0122 | it does nothing new with the old story , except to show fisticuffs in this sort of stop-go slow motion that makes the gang rumbles look like they 're being streamed over a 28k modem . director of photography benoit delhomme shot the movie in delicious colors , and the costumes and sets are grand . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0063 | while there 's something intrinsically funny about sir anthony hopkins saying ` get in the car , bitch , ' this jerry bruckheimer production has little else to offer you really have to wonder how on earth anyone , anywhere could have thought they 'd make audiences guffaw with a script as utterly diabolical as this . | A | B | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0488 | an occasionally funny , but overall limp , fish-out-of-water story . the weight of the piece , the unerring professionalism of the chilly production , and the fascination embedded in the lurid topic prove recommendation enough . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0341 | there is no pleasure in watching a child suffer . a densely constructed , highly referential film , and an audacious return to form that can comfortably sit among jean-luc godard 's finest work . | A | A | yes |

### Rule 10: 2/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0041 | an exhilarating futuristic thriller-noir , minority report twists the best of technology around a gripping story , delivering a riveting , pulse intensifying escapist adventure of the first order maud and roland 's search for an unknowable past makes for a haunting literary detective story , but labute pulls off a neater trick in possession : he makes language sexy . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0298 | puts a human face on a land most westerners are unfamiliar with . despite the evocative aesthetics evincing the hollow state of modern love life , the film never percolates beyond a monotonous whine . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0300 | a poignant , artfully crafted meditation on mortality . ... a magnificent drama well worth tracking down . | B | A | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0177 | it 's also , clearly , great fun . ( t ) his beguiling belgian fable , very much its own droll and delicate little film , has some touching things to say about what is important in life and why . | B | A | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0410 | the movie is what happens when you blow up small potatoes to 10 times their natural size , and it ai n't pretty . do not see this film . | B | B | yes |

### Rule 11: 2/5

Articulated rule: Label A if and only if the second review sentence is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0068 | the primitive force of this film seems to bubble up from the vast collective memory of the combatants . nervous breakdowns are not entertaining . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0050 | old-form moviemaking at its best . there 's really only one good idea in this movie , but the director runs with it and presents it with an unforgettable visual panache . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0300 | a poignant , artfully crafted meditation on mortality . ... a magnificent drama well worth tracking down . | B | A | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0209 | one of the best films of the year with its exploration of the obstacles to happiness faced by five contemporary individuals ... a psychological masterpiece . so unremittingly awful that labeling it a dog probably constitutes cruelty to canines . | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0162 | what the director ca n't do is make either of val kilmer 's two personas interesting or worth caring about . if you are an actor who can relate to the search for inner peace by dramatically depicting the lives of others onstage , then esther 's story is a compelling quest for truth . | A | A | yes |

### Rule 12: 4/5

Articulated rule: Label A if and only if the second review is more positive than the first.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0243 | something akin to a japanese alice through the looking glass , except that it seems to take itself far more seriously . there is a fabric of complex ideas here , and feelings that profoundly deepen them . | B | A | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0011 | the plot convolutions ultimately add up to nothing more than jerking the audience 's chain . there 's really only one good idea in this movie , but the director runs with it and presents it with an unforgettable visual panache . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0413 | falls neatly into the category of good stupid fun . while there 's something intrinsically funny about sir anthony hopkins saying ` get in the car , bitch , ' this jerry bruckheimer production has little else to offer | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0291 | highbrow self-appointed guardians of culture need not apply , but those who loved cool as ice have at last found a worthy follow-up . reign of fire looks as if it was made without much thought -- and is best watched that way . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0482 | dragonfly has no atmosphere , no tension -- nothing but costner , flailing away . it 's a demented kitsch mess ( although the smeary digital video does match the muddled narrative ) , but it 's savvy about celebrity and has more guts and energy than much of what will open this year . | A | A | yes |

### Rule 13: 3/5

Articulated rule: Label A if and only if the second review sentence is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0087 | you do n't have to know about music to appreciate the film 's easygoing blend of comedy and romance . from the opening scenes , it 's clear that all about the benjamins is a totally formulaic movie . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0046 | the longer the movie goes , the worse it gets , but it 's actually pretty good in the first few minutes . a spellbinding african film about the modern condition of rootlessness , a state experienced by millions around the globe . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0183 | excessive , profane , packed with cartoonish violence and comic-strip characters . a poignant , artfully crafted meditation on mortality . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0023 | that is a compliment to kuras and miller . falls neatly into the category of good stupid fun . | B | A | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0482 | dragonfly has no atmosphere , no tension -- nothing but costner , flailing away . it 's a demented kitsch mess ( although the smeary digital video does match the muddled narrative ) , but it 's savvy about celebrity and has more guts and energy than much of what will open this year . | A | A | yes |

### Rule 14: 5/5

Articulated rule: Label B if and only if both sentences in the input have the same sentiment polarity; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0038 | dense with characters and contains some thrilling moments . like being trapped at a perpetual frat party ... how can something so gross be so boring ? | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0238 | and if you 're not nearly moved to tears by a couple of scenes , you 've got ice water in your veins . a gripping movie , played with performances that are all understated and touching . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0259 | the script is n't very good ; not even someone as gifted as hoffman ( the actor ) can make it work . shaky close-ups of turkey-on-rolls , stubbly chins , liver spots , red noses and the filmmakers new bobbed do draw easy chuckles but lead nowhere . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0140 | you really have to wonder how on earth anyone , anywhere could have thought they 'd make audiences guffaw with a script as utterly diabolical as this . all the amped-up tony hawk-style stunts and thrashing rap-metal ca n't disguise the fact that , really , we 've been here , done that . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0362 | while the resident evil games may have set new standards for thrills , suspense , and gore for video games , the movie really only succeeds in the third of these . a literate presentation that wonderfully weaves a murderous event in 1873 with murderous rage in 2002 . | A | A | yes |

### Rule 15: 2/5

Articulated rule: Label A if and only if the first review snippet is more positive than the second; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0387 | it is great summer fun to watch arnold and his buddy gerald bounce off a quirky cast of characters . scorsese does n't give us a character worth giving a damn about . | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0456 | it is great summer fun to watch arnold and his buddy gerald bounce off a quirky cast of characters . generally , clockstoppers will fulfill your wildest fantasies about being a different kind of time traveler , while happily killing 94 minutes . | B | A | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0297 | the film 's hackneyed message is not helped by the thin characterizations , nonexistent plot and pretentious visual style . a gripping movie , played with performances that are all understated and touching . | A | B | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0444 | visually rather stunning , but ultimately a handsome-looking bore , the true creativity would have been to hide treasure planet entirely and completely reimagine it . if you enjoy more thoughtful comedies with interesting conflicted characters ; this one is for you . | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0151 | fun , flip and terribly hip bit of cinematic entertainment . made with no discernible craft and monstrously sanctimonious in dealing with childhood loss . | A | A | yes |

### Rule 16: 2/5

Articulated rule: Label A if and only if the second review sentence is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0151 | fun , flip and terribly hip bit of cinematic entertainment . made with no discernible craft and monstrously sanctimonious in dealing with childhood loss . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0460 | it 's dumb , but more importantly , it 's just not scary . the film 's hackneyed message is not helped by the thin characterizations , nonexistent plot and pretentious visual style . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0343 | so unassuming and pure of heart , you ca n't help but warmly extend your arms and yell ` safe ! ' the minor figures surrounding ( bobby ) ... form a gritty urban mosaic . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0377 | audrey tatou has a knack for picking roles that magnify her outrageous charm , and in this literate french comedy , she 's as morning-glory exuberant as she was in amélie . may reawaken discussion of the kennedy assassination but this fictional film looks made for cable rather than for the big screen . | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0241 | director andrew niccol ... demonstrates a wry understanding of the quirks of fame . ( w ) hile long on amiable monkeys and worthy environmentalism , jane goodall 's wild chimpanzees is short on the thrills the oversize medium demands . | A | B | no |

### Rule 17: 5/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0156 | with rabbit-proof fence , noyce has tailored an epic tale into a lean , economical movie . the movie 's relatively simple plot and uncomplicated morality play well with the affable cast . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0186 | coughs and sputters on its own postmodern conceit . add yet another hat to a talented head , clooney 's a good director . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0341 | there is no pleasure in watching a child suffer . a densely constructed , highly referential film , and an audacious return to form that can comfortably sit among jean-luc godard 's finest work . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0117 | determined to be fun , and bouncy , with energetic musicals , the humor did n't quite engage this adult . feels too formulaic and too familiar to produce the transgressive thrills of early underground work . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0337 | impostor has a handful of thrilling moments and a couple of good performances , but the movie does n't quite fly . while the resident evil games may have set new standards for thrills , suspense , and gore for video games , the movie really only succeeds in the third of these . | B | B | yes |

### Rule 18: 5/5

Articulated rule: Label A if and only if the first review sentence is more positive than the second; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0089 | a marvel like none you 've seen . ( a ) n utterly charming and hilarious film that reminded me of the best of the disney comedies from the 60s . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0097 | as the latest bid in the tv-to-movie franchise game , i spy makes its big-screen entry with little of the nervy originality of its groundbreaking small-screen progenitor . the reality of the new live-action pinocchio he directed , cowrote and starred in borders on the grotesque . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0154 | if you enjoy more thoughtful comedies with interesting conflicted characters ; this one is for you . ... the movie is just a plain old monster . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0012 | the socio-histo-political treatise is told in earnest strides ... ( and ) personal illusion is deconstructed with poignancy . leigh 's film is full of memorable performances from top to bottom . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0373 | although german cooking does not come readily to mind when considering the world 's best cuisine , mostly martha could make deutchland a popular destination for hungry tourists . the story and structure are well-honed . | B | B | yes |

### Rule 19: 5/5

Articulated rule: Label A if and only if exactly one of the two sentences is positive and the other is negative.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0037 | the film flat lines when it should peak and is more missed opportunity and trifle than dark , decadent truffle . i do n't think i laughed out loud once . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0387 | it is great summer fun to watch arnold and his buddy gerald bounce off a quirky cast of characters . scorsese does n't give us a character worth giving a damn about . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0290 | not since japanese filmmaker akira kurosawa 's ran have the savagery of combat and the specter of death been visualized with such operatic grandeur . i 'll bet the video game is a lot more fun than the film . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0233 | as ` chick flicks ' go , this one is pretty miserable , resorting to string-pulling rather than legitimate character development and intelligent plotting . complete lack of originality , cleverness or even visible effort | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0078 | affleck and jackson are good sparring partners . if you dig on david mamet 's mind tricks ... rent this movie and enjoy ! | B | B | yes |

### Rule 20: 3/5

Articulated rule: Label A if and only if the first sentence is more negative than the second; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0347 | all the amped-up tony hawk-style stunts and thrashing rap-metal ca n't disguise the fact that , really , we 've been here , done that . not really bad so much as distasteful : we need kidnapping suspense dramas right now like we need doomsday thrillers . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0204 | coughs and sputters on its own postmodern conceit . perceptive in its vision of nascent industrialized world politics as a new art form , but far too clunky , didactic and saddled with scenes that seem simply an ill fit for this movie . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0021 | a film about a young man finding god that is accessible and touching to the marrow . directed in a paint-by-numbers manner . | A | B | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0269 | the words , ` frankly , my dear , i do n't give a damn , ' have never been more appropriate . may reawaken discussion of the kennedy assassination but this fictional film looks made for cable rather than for the big screen . | B | A | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0258 | so unremittingly awful that labeling it a dog probably constitutes cruelty to canines . you really have to wonder how on earth anyone , anywhere could have thought they 'd make audiences guffaw with a script as utterly diabolical as this . | B | B | yes |

### Rule 21: 2/5

Articulated rule: Label B if and only if the second review snippet is more positive than the first; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0470 | broomfield turns his distinctive ` blundering ' style into something that could really help clear up the case . perceptive in its vision of nascent industrialized world politics as a new art form , but far too clunky , didactic and saddled with scenes that seem simply an ill fit for this movie . | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0095 | stultifyingly , dumbfoundingly , mind-numbingly bad . an exhilarating futuristic thriller-noir , minority report twists the best of technology around a gripping story , delivering a riveting , pulse intensifying escapist adventure of the first order | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0079 | having had the good sense to cast actors who are , generally speaking , adored by the movie-going public , khouri then gets terrific performances from them all . the volatile dynamics of female friendship is the subject of this unhurried , low-key film that is so off-hollywood that it seems positively french in its rhythms and resonance . | B | A | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0485 | it 's clear the filmmakers were n't sure where they wanted their story to go , and even more clear that they lack the skills to get us to this undetermined destination . in execution , this clever idea is far less funny than the original , killers from space . | B | A | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0004 | escaping the studio , piccoli is warmly affecting and so is this adroitly minimalist movie . the action switches between past and present , but the material link is too tenuous to anchor the emotional connections that purport to span a 125-year divide . | A | A | yes |

### Rule 22: 5/5

Articulated rule: Label A if and only if the two reviews have opposite sentiment polarity, while Label B if and only if they have the same sentiment polarity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0471 | not only unfunny , but downright repellent . makes for a pretty unpleasant viewing experience . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0168 | given how heavy-handed and portent-heavy it is , this could be the worst thing soderbergh has ever done . in exactly 89 minutes , most of which passed as slowly as if i 'd been sitting naked on an igloo , formula 51 sank from quirky to jerky to utter turkey . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0184 | people cinema at its finest . it 's so mediocre , despite the dynamic duo on the marquee , that we just ca n't get no satisfaction . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0177 | it 's also , clearly , great fun . ( t ) his beguiling belgian fable , very much its own droll and delicate little film , has some touching things to say about what is important in life and why . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0151 | fun , flip and terribly hip bit of cinematic entertainment . made with no discernible craft and monstrously sanctimonious in dealing with childhood loss . | A | A | yes |

### Rule 23: 4/5

Articulated rule: Label A if and only if exactly one of the two sentences is positive and the other is negative.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0338 | while it 's genuinely cool to hear characters talk about early rap records ( sugar hill gang , etc. ) , the constant referencing of hip-hop arcana can alienate even the savviest audiences . a moody , multi-dimensional love story and sci-fi mystery , solaris is a thought-provoking , haunting film that allows the seeds of the imagination to germinate . | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0367 | the film flat lines when it should peak and is more missed opportunity and trifle than dark , decadent truffle . ... an otherwise intense , twist-and-turn thriller that certainly should n't hurt talented young gaghan 's resume . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0286 | cq 's reflection of artists and the love of cinema-and-self suggests nothing less than a new voice that deserves to be considered as a possible successor to the best european directors . it showcases carvey 's talent for voices , but not nearly enough and not without taxing every drop of one 's patience to get to the good stuff . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0003 | i got a headache watching this meaningless downer . it 's an offbeat treat that pokes fun at the democratic exercise while also examining its significance for those who take part . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0457 | a psychological thriller with a genuinely spooky premise and an above-average cast , actor bill paxton 's directing debut is a creepy slice of gothic rural americana . it provides the grand , intelligent entertainment of a superior cast playing smart people amid a compelling plot . | B | B | yes |

### Rule 24: 2/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0287 | what distinguishes time of favor from countless other thrillers is its underlying concern with the consequences of words and with the complicated emotions fueling terrorist acts . the plot convolutions ultimately add up to nothing more than jerking the audience 's chain . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0153 | it proves quite compelling as an intense , brooding character study . cq 's reflection of artists and the love of cinema-and-self suggests nothing less than a new voice that deserves to be considered as a possible successor to the best european directors . | B | A | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0365 | i can take infantile humor ... but this is the sort of infantile that makes you wonder about changing the director and writer 's diapers . we have n't seen such hilarity since say it is n't so ! | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0058 | ( w ) hile long on amiable monkeys and worthy environmentalism , jane goodall 's wild chimpanzees is short on the thrills the oversize medium demands . it 's too bad that the helping hand he uses to stir his ingredients is also a heavy one . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0149 | huston nails both the glad-handing and the choking sense of hollow despair . the overall effect is less like a children 's movie than a recruitment film for future hollywood sellouts . | A | B | no |

### Rule 25: 0/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0034 | blanchett 's performance confirms her power once again . it 's so mediocre , despite the dynamic duo on the marquee , that we just ca n't get no satisfaction . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0450 | looking aristocratic , luminous yet careworn in jane hamilton 's exemplary costumes , rampling gives a performance that could not be improved upon . ' try as i may , i ca n't think of a single good reason to see this movie , even though everyone in my group extemporaneously shouted , ` thank you ! ' | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0230 | that is a compliment to kuras and miller . what is 100 % missing here is a script of even the most elemental literacy , an inkling of genuine wit , and anything resembling acting . | A | B | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0309 | the magic of the film lies not in the mysterious spring but in the richness of its performances . it inspires a continuing and deeply satisfying awareness of the best movies as monumental ` picture shows . ' | B | A | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0429 | generally , clockstoppers will fulfill your wildest fantasies about being a different kind of time traveler , while happily killing 94 minutes . this movie seems to have been written using mad-libs . | A | B | no |

### Rule 26: 3/5

Articulated rule: Label A if and only if the second review is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0106 | it does nothing new with the old story , except to show fisticuffs in this sort of stop-go slow motion that makes the gang rumbles look like they 're being streamed over a 28k modem . sit through this one , and you wo n't need a magic watch to stop time ; your dvd player will do it for you . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0091 | ... a magnificent drama well worth tracking down . impostor has a handful of thrilling moments and a couple of good performances , but the movie does n't quite fly . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0220 | while the resident evil games may have set new standards for thrills , suspense , and gore for video games , the movie really only succeeds in the third of these . what was once original has been co-opted so frequently that it now seems pedestrian . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0288 | escaping the studio , piccoli is warmly affecting and so is this adroitly minimalist movie . it just may inspire a few younger moviegoers to read stevenson 's book , which is a treasure in and of itself . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0276 | it inspires a continuing and deeply satisfying awareness of the best movies as monumental ` picture shows . ' i just loved every minute of this film . | B | A | no |

### Rule 27: 1/5

Articulated rule: Label B if and only if the second review sentence is more positive than the first; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0068 | the primitive force of this film seems to bubble up from the vast collective memory of the combatants . nervous breakdowns are not entertaining . | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0345 | this re-do is so dumb and so exploitative in its violence that , ironically , it becomes everything that the rather clumsy original was railing against . for the most part stevens glides through on some solid performances and witty dialogue . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0005 | it 's like every bad idea that 's ever gone into an after-school special compiled in one place , minus those daytime programs ' slickness and sophistication ( and who knew they even had any ? ) . manages to show life in all of its banality when the intention is quite the opposite . | B | A | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0071 | it seems like i have been waiting my whole life for this movie and now i ca n't wait for the sequel . it just may inspire a few younger moviegoers to read stevenson 's book , which is a treasure in and of itself . | B | A | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0003 | i got a headache watching this meaningless downer . it 's an offbeat treat that pokes fun at the democratic exercise while also examining its significance for those who take part . | A | B | no |

### Rule 28: 1/5

Articulated rule: Label A if and only if the first review snippet is more negative than the second; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0113 | there is no pleasure in watching a child suffer . there is nothing outstanding about this film , but it is good enough and will likely be appreciated most by sailors and folks who know their way around a submarine . | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0139 | lapaglia 's ability to convey grief and hope works with weaver 's sensitive reactions to make this a two-actor master class . a dumb movie with dumb characters doing dumb things and you have to be really dumb not to see where this is going . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0339 | a delightful coming-of-age story . a disappointment for those who love alternate versions of the bard , particularly ones that involve deep fryers and hamburgers . | A | B | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0073 | it 's great escapist fun that recreates a place and time that will never happen again . for all its impressive craftsmanship , and despite an overbearing series of third-act crescendos , lily chou-chou never really builds up a head of emotional steam . | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0063 | while there 's something intrinsically funny about sir anthony hopkins saying ` get in the car , bitch , ' this jerry bruckheimer production has little else to offer you really have to wonder how on earth anyone , anywhere could have thought they 'd make audiences guffaw with a script as utterly diabolical as this . | A | B | no |

### Rule 29: 1/5

Articulated rule: Label B if and only if the second review snippet is more positive than the first; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0475 | if looking for a thrilling sci-fi cinematic ride , do n't settle for this imposter . ... a magnificent drama well worth tracking down . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0262 | it 's dumb , but more importantly , it 's just not scary . true tale of courage -- and complicity -- at auschwitz is a harrowing drama that tries to tell of the unspeakable . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0053 | the movie understands like few others how the depth and breadth of emotional intimacy give the physical act all of its meaning and most of its pleasure . thanks to haynes ' absolute control of the film 's mood , and buoyed by three terrific performances , far from heaven actually pulls off this stylistic juggling act . | B | A | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0365 | i can take infantile humor ... but this is the sort of infantile that makes you wonder about changing the director and writer 's diapers . we have n't seen such hilarity since say it is n't so ! | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0296 | the best revenge may just be living well because this film , unlike other dumas adaptations , is far more likened to a treasure than a lengthy jail sentence . there is no pleasure in watching a child suffer . | A | A | yes |

### Rule 30: 2/5

Articulated rule: Label A if and only if the second review sentence is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0217 | a rewarding work of art for only the most patient and challenge-hungry moviegoers . we root for ( clara and paul ) , even like them , though perhaps it 's an emotion closer to pity . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0138 | anchored by friel and williams 's exceptional performances , the film 's power lies in its complexity . the story and the friendship proceeds in such a way that you 're watching a soap opera rather than a chronicle of the ups and downs that accompany lifelong friendships . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0296 | the best revenge may just be living well because this film , unlike other dumas adaptations , is far more likened to a treasure than a lengthy jail sentence . there is no pleasure in watching a child suffer . | A | B | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0255 | `` the time machine '' is a movie that has no interest in itself . it 's a grab bag of genres that do n't add up to a whole lot of sense . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0320 | you will emerge with a clearer view of how the gears of justice grind on and the death report comes to share airtime alongside the farm report . with rabbit-proof fence , noyce has tailored an epic tale into a lean , economical movie . | B | A | no |

### Rule 31: 1/5

Articulated rule: Label A if and only if the first review snippet is more positive than the second; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0172 | green might want to hang onto that ski mask , as robbery may be the only way to pay for his next project . so much facile technique , such cute ideas , so little movie . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0123 | its well of thorn and vinegar ( and simple humanity ) has long been plundered by similar works featuring the insight and punch this picture so conspicuously lacks . a painfully funny ode to bad behavior . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0300 | a poignant , artfully crafted meditation on mortality . ... a magnificent drama well worth tracking down . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0324 | does little more than play an innocuous game of fill-in - the-blanks with a tragic past . jones ... does offer a brutal form of charisma . | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0085 | it takes a strange kind of laziness to waste the talents of robert forster , anne meara , eugene levy , and reginald veljohnson all in the same movie . looking aristocratic , luminous yet careworn in jane hamilton 's exemplary costumes , rampling gives a performance that could not be improved upon . ' | A | B | no |

### Rule 32: 4/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0330 | too often , the viewer is n't reacting to humor so much as they are wincing back in repugnance . visually rather stunning , but ultimately a handsome-looking bore , the true creativity would have been to hide treasure planet entirely and completely reimagine it . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0300 | a poignant , artfully crafted meditation on mortality . ... a magnificent drama well worth tracking down . | B | A | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0225 | an unwise amalgam of broadcast news and vibes . with the exception of some fleetingly amusing improvisations by cedric the entertainer as perry 's boss , there is n't a redeeming moment here . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0265 | a movie that reminds us of just how exciting and satisfying the fantasy cinema can be when it 's approached with imagination and flair . there 's really only one good idea in this movie , but the director runs with it and presents it with an unforgettable visual panache . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0054 | not since japanese filmmaker akira kurosawa 's ran have the savagery of combat and the specter of death been visualized with such operatic grandeur . the jabs it employs are short , carefully placed and dead-center . | B | B | yes |

### Rule 33: 2/5

Articulated rule: Label B if and only if the second review snippet is more positive than the first; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0082 | chabrol has taken promising material for a black comedy and turned it instead into a somber chamber drama . a gorgeous , witty , seductive movie . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0364 | an entertaining , colorful , action-filled crime story with an intimate heart . a gorgeous , witty , seductive movie . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0413 | falls neatly into the category of good stupid fun . while there 's something intrinsically funny about sir anthony hopkins saying ` get in the car , bitch , ' this jerry bruckheimer production has little else to offer | B | A | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0209 | one of the best films of the year with its exploration of the obstacles to happiness faced by five contemporary individuals ... a psychological masterpiece . so unremittingly awful that labeling it a dog probably constitutes cruelty to canines . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0009 | it 's a lovely film with lovely performances by buy and accorsi . a subtle and well-crafted ( for the most part ) chiller . | B | A | no |

### Rule 34: 5/5

Articulated rule: Label A if and only if the two reviews have opposite sentiment polarity, whereas Label B if and only if they have the same sentiment polarity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0440 | charles ' entertaining film chronicles seinfeld 's return to stand-up comedy after the wrap of his legendary sitcom , alongside wannabe comic adams ' attempts to get his shot at the big time . as the latest bid in the tv-to-movie franchise game , i spy makes its big-screen entry with little of the nervy originality of its groundbreaking small-screen progenitor . | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0283 | its well of thorn and vinegar ( and simple humanity ) has long been plundered by similar works featuring the insight and punch this picture so conspicuously lacks . it 's a lovely film with lovely performances by buy and accorsi . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0211 | as ` chick flicks ' go , this one is pretty miserable , resorting to string-pulling rather than legitimate character development and intelligent plotting . something like scrubbing the toilet . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0066 | puts a human face on a land most westerners are unfamiliar with . not only unfunny , but downright repellent . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0231 | serving sara does n't serve up a whole lot of laughs . it provides the grand , intelligent entertainment of a superior cast playing smart people amid a compelling plot . | A | A | yes |

### Rule 35: 3/5

Articulated rule: Label B if and only if the second review sentence is more positive than the first; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0234 | the talented and clever robert rodriguez perhaps put a little too much heart into his first film and did n't reserve enough for his second . the notion that bombing buildings is the funniest thing in the world goes entirely unexamined in this startlingly unfunny comedy . | B | A | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0302 | the lower your expectations , the more you 'll enjoy it . displaying about equal amounts of naiveté , passion and talent , beneath clouds establishes sen as a filmmaker of considerable potential . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0074 | binoche makes it interesting trying to find out . it 's just disappointingly superficial -- a movie that has all the elements necessary to be a fascinating , involving character study , but never does more than scratch the surface . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0416 | exquisitely nuanced in mood tics and dialogue , this chamber drama is superbly acted by the deeply appealing veteran bouquet and the chilling but quite human berling . a quiet treasure -- a film to be savored . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0464 | lapaglia 's ability to convey grief and hope works with weaver 's sensitive reactions to make this a two-actor master class . my big fat greek wedding uses stereotypes in a delightful blend of sweet romance and lovingly dished out humor . | B | B | yes |

### Rule 36: 2/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0001 | this is not the undisputed worst boxing movie ever , but it 's certainly not a champion - the big loser is the audience . generally , clockstoppers will fulfill your wildest fantasies about being a different kind of time traveler , while happily killing 94 minutes . | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0040 | people cinema at its finest . does little more than play an innocuous game of fill-in - the-blanks with a tragic past . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0354 | ... a story we have n't seen on the big screen before , and it 's a story that we as americans , and human beings , should know . but it could have been worse . | A | B | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0414 | this is human comedy at its most amusing , interesting and confirming . the lower your expectations , the more you 'll enjoy it . | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0420 | ... the movie is just a plain old monster . if you dig on david mamet 's mind tricks ... rent this movie and enjoy ! | A | A | yes |

### Rule 37: 5/5

Articulated rule: Label A if and only if exactly one of the two sentences is positive and the other is negative.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0497 | the movie , directed by mick jackson , leaves no cliche unturned , from the predictable plot to the characters straight out of central casting . awesome creatures , breathtaking scenery , and epic battle scenes add up to another ` spectacular spectacle . ' | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0000 | a movie that reminds us of just how exciting and satisfying the fantasy cinema can be when it 's approached with imagination and flair . manages to show life in all of its banality when the intention is quite the opposite . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0109 | a woman 's pic directed with resonance by ilya chaiken . an exhilarating futuristic thriller-noir , minority report twists the best of technology around a gripping story , delivering a riveting , pulse intensifying escapist adventure of the first order | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0281 | the action switches between past and present , but the material link is too tenuous to anchor the emotional connections that purport to span a 125-year divide . i can take infantile humor ... but this is the sort of infantile that makes you wonder about changing the director and writer 's diapers . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0241 | director andrew niccol ... demonstrates a wry understanding of the quirks of fame . ( w ) hile long on amiable monkeys and worthy environmentalism , jane goodall 's wild chimpanzees is short on the thrills the oversize medium demands . | A | A | yes |

### Rule 38: 2/5

Articulated rule: Label B if and only if the second review snippet is more positive than the first; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0150 | comes ... uncomfortably close to coasting in the treads of the bicycle thief . the longer the movie goes , the worse it gets , but it 's actually pretty good in the first few minutes . | B | A | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0116 | majidi is an unconventional storyteller , capable of finding beauty in the most depressing places . a simple , but gritty and well-acted ensemble drama that encompasses a potent metaphor for a country still dealing with its fascist past . | B | A | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0154 | if you enjoy more thoughtful comedies with interesting conflicted characters ; this one is for you . ... the movie is just a plain old monster . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0070 | it inspires a continuing and deeply satisfying awareness of the best movies as monumental ` picture shows . ' instead of hiding pinocchio from critics , miramax should have hidden it from everyone . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0485 | it 's clear the filmmakers were n't sure where they wanted their story to go , and even more clear that they lack the skills to get us to this undetermined destination . in execution , this clever idea is far less funny than the original , killers from space . | B | A | no |

### Rule 39: 5/5

Articulated rule: Label B if and only if both sentences have the same sentiment polarity; otherwise label A.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0050 | old-form moviemaking at its best . there 's really only one good idea in this movie , but the director runs with it and presents it with an unforgettable visual panache . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0262 | it 's dumb , but more importantly , it 's just not scary . true tale of courage -- and complicity -- at auschwitz is a harrowing drama that tries to tell of the unspeakable . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0384 | and that 's a big part of why we go to the movies . ( a ) n utterly charming and hilarious film that reminded me of the best of the disney comedies from the 60s . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0429 | generally , clockstoppers will fulfill your wildest fantasies about being a different kind of time traveler , while happily killing 94 minutes . this movie seems to have been written using mad-libs . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0311 | director uwe boll and the actors provide scant reason to care in this crude '70s throwback . trademark american triteness and simplicity are tossed out the window with the intelligent french drama that deftly explores the difficult relationship between a father and son . | A | A | yes |

### Rule 40: 4/5

Articulated rule: Label A if and only if the second review is more positive than the first.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0343 | so unassuming and pure of heart , you ca n't help but warmly extend your arms and yell ` safe ! ' the minor figures surrounding ( bobby ) ... form a gritty urban mosaic . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0327 | slick piece of cross-promotion . the jabs it employs are short , carefully placed and dead-center . | B | A | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0150 | comes ... uncomfortably close to coasting in the treads of the bicycle thief . the longer the movie goes , the worse it gets , but it 's actually pretty good in the first few minutes . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0088 | despite all evidence to the contrary , this clunker has somehow managed to pose as an actual feature movie , the kind that charges full admission and gets hyped on tv and purports to amuse small children and ostensible adults . awesome creatures , breathtaking scenery , and epic battle scenes add up to another ` spectacular spectacle . ' | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0418 | thanks to haynes ' absolute control of the film 's mood , and buoyed by three terrific performances , far from heaven actually pulls off this stylistic juggling act . the sort of film that makes me miss hitchcock , but also feel optimistic that there 's hope for popular cinema yet . | B | B | yes |

### Rule 41: 4/5

Articulated rule: Label A if and only if the second review sentence is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0088 | despite all evidence to the contrary , this clunker has somehow managed to pose as an actual feature movie , the kind that charges full admission and gets hyped on tv and purports to amuse small children and ostensible adults . awesome creatures , breathtaking scenery , and epic battle scenes add up to another ` spectacular spectacle . ' | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0305 | as the latest bid in the tv-to-movie franchise game , i spy makes its big-screen entry with little of the nervy originality of its groundbreaking small-screen progenitor . like being trapped at a perpetual frat party ... how can something so gross be so boring ? | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0408 | you do n't have to know about music to appreciate the film 's easygoing blend of comedy and romance . a delightful coming-of-age story . | B | A | no |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0112 | at the very least , if you do n't know anything about derrida when you walk into the theater , you wo n't know much more when you leave . a great ensemble cast ca n't lift this heartfelt enterprise out of the familiar . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0425 | the movie fails to live up to the sum of its parts . thanks to haynes ' absolute control of the film 's mood , and buoyed by three terrific performances , far from heaven actually pulls off this stylistic juggling act . | A | A | yes |

### Rule 42: 3/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0478 | for all its technical virtuosity , the film is so mired in juvenile and near-xenophobic pedagogy that it 's enough to make one pine for the day when godard can no longer handle the rigors of filmmaking . a bloated gasbag thesis grotesquely impressed by its own gargantuan aura of self-importance ... | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0171 | fun , flip and terribly hip bit of cinematic entertainment . instead of hiding pinocchio from critics , miramax should have hidden it from everyone . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0475 | if looking for a thrilling sci-fi cinematic ride , do n't settle for this imposter . ... a magnificent drama well worth tracking down . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0487 | the very definition of the ` small ' movie , but it is a good stepping stone for director sprecher . not only unfunny , but downright repellent . | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0125 | this nickleby thing might have more homosexual undertones than an eddie murphy film . ( director ) o'fallon manages to put some lovely pictures up on the big screen , but his skill at telling a story -- he also contributed to the screenplay -- falls short . | B | B | yes |

### Rule 43: 4/5

Articulated rule: Label A if and only if the second review is more negative than the first.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0005 | it 's like every bad idea that 's ever gone into an after-school special compiled in one place , minus those daytime programs ' slickness and sophistication ( and who knew they even had any ? ) . manages to show life in all of its banality when the intention is quite the opposite . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0020 | although huppert 's intensity and focus has a raw exhilaration about it , the piano teacher is anything but fun . wince-inducing dialogue , thrift-shop costumes , prosthetic makeup by silly putty and kmart blue-light-special effects all conspire to test trekkie loyalty . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0091 | ... a magnificent drama well worth tracking down . impostor has a handful of thrilling moments and a couple of good performances , but the movie does n't quite fly . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0306 | it all adds up to good fun . from the opening scenes , it 's clear that all about the benjamins is a totally formulaic movie . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0047 | it 's dumb , but more importantly , it 's just not scary . not since freddy got fingered has a major release been so painful to sit through . | B | A | no |

### Rule 44: 3/5

Articulated rule: Label A if and only if the second review snippet is more positive than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0042 | feels haphazard , as if the writers mistakenly thought they could achieve an air of frantic spontaneity by simply tossing in lots of characters doing silly stuff and stirring the pot . the film flat lines when it should peak and is more missed opportunity and trifle than dark , decadent truffle . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0038 | dense with characters and contains some thrilling moments . like being trapped at a perpetual frat party ... how can something so gross be so boring ? | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0099 | it seems to me the film is about the art of ripping people off without ever letting them consciously know you have done so ... the movie is just a plain old monster . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0203 | while it 's genuinely cool to hear characters talk about early rap records ( sugar hill gang , etc. ) , the constant referencing of hip-hop arcana can alienate even the savviest audiences . old-form moviemaking at its best . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0437 | jaglom ... put ( s ) the audience in the privileged position of eavesdropping on his characters scooby dooby doo / and shaggy too / you both look and sound great . | B | A | no |

### Rule 45: 4/5

Articulated rule: Label A if and only if the second review snippet is more negative than the first; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0066 | puts a human face on a land most westerners are unfamiliar with . not only unfunny , but downright repellent . | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0351 | a bloated gasbag thesis grotesquely impressed by its own gargantuan aura of self-importance ... an exhilarating futuristic thriller-noir , minority report twists the best of technology around a gripping story , delivering a riveting , pulse intensifying escapist adventure of the first order | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0206 | the jabs it employs are short , carefully placed and dead-center . it 's too bad that the helping hand he uses to stir his ingredients is also a heavy one . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0415 | the jabs it employs are short , carefully placed and dead-center . smart , provocative and blisteringly funny . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0022 | while its careful pace and seemingly opaque story may not satisfy every moviegoer 's appetite , the film 's final scene is soaringly , transparently moving . it 's a remarkably solid and subtly satirical tour de force . | B | B | yes |

### Rule 46: 3/5

Articulated rule: Label A if and only if the first review snippet is more positive than the second; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0337 | impostor has a handful of thrilling moments and a couple of good performances , but the movie does n't quite fly . while the resident evil games may have set new standards for thrills , suspense , and gore for video games , the movie really only succeeds in the third of these . | B | A | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0314 | we have n't seen such hilarity since say it is n't so ! a sequel that 's much too big for its britches . | A | A | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0358 | a painfully funny ode to bad behavior . a densely constructed , highly referential film , and an audacious return to form that can comfortably sit among jean-luc godard 's finest work . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0185 | makes for a pretty unpleasant viewing experience . the movie understands like few others how the depth and breadth of emotional intimacy give the physical act all of its meaning and most of its pleasure . | A | B | no |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0392 | the socio-histo-political treatise is told in earnest strides ... ( and ) personal illusion is deconstructed with poignancy . sam mendes has become valedictorian at the school for soft landings and easy ways out . | A | A | yes |

### Rule 47: 5/5

Articulated rule: Label A if and only if exactly one of the two sentences is negative and the other is positive.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0417 | or doing last year 's taxes with your ex-wife . ` de niro ... is a veritable source of sincere passion that this hollywood contrivance orbits around . ' | A | A | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0220 | while the resident evil games may have set new standards for thrills , suspense , and gore for video games , the movie really only succeeds in the third of these . what was once original has been co-opted so frequently that it now seems pedestrian . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0450 | looking aristocratic , luminous yet careworn in jane hamilton 's exemplary costumes , rampling gives a performance that could not be improved upon . ' try as i may , i ca n't think of a single good reason to see this movie , even though everyone in my group extemporaneously shouted , ` thank you ! ' | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0255 | `` the time machine '' is a movie that has no interest in itself . it 's a grab bag of genres that do n't add up to a whole lot of sense . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0114 | the primitive force of this film seems to bubble up from the vast collective memory of the combatants . feels too formulaic and too familiar to produce the transgressive thrills of early underground work . | A | A | yes |

### Rule 48: 4/5

Articulated rule: Label A if and only if the two sentences have opposite sentiment polarity, while Label B if and only if they have the same overall sentiment polarity.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0385 | ` easily my choice for one of the year 's best films . ' perceptive in its vision of nascent industrialized world politics as a new art form , but far too clunky , didactic and saddled with scenes that seem simply an ill fit for this movie . | A | B | no |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0456 | it is great summer fun to watch arnold and his buddy gerald bounce off a quirky cast of characters . generally , clockstoppers will fulfill your wildest fantasies about being a different kind of time traveler , while happily killing 94 minutes . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0179 | the man from elysian fields is a cold , bliss-less work that groans along thinking itself some important comment on how life throws us some beguiling curves . while ( hill ) has learned new tricks , the tricks alone are not enough to salvage this lifeless boxing film . | B | B | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0171 | fun , flip and terribly hip bit of cinematic entertainment . instead of hiding pinocchio from critics , miramax should have hidden it from everyone . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0454 | it 's refreshing to see a girl-power movie that does n't feel it has to prove anything . the quality of the art combined with the humor and intelligence of the script allow the filmmakers to present the biblical message of forgiveness without it ever becoming preachy or syrupy . | B | B | yes |

### Rule 49: 5/5

Articulated rule: Label A if and only if exactly one of the two sentences is positive and the other is negative; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0188 | it 's hard to like a film about a guy who is utterly unlikeable , and shiner , starring michael caine as an aging british boxing promoter desperate for a taste of fame and fortune , is certainly that . it has its moments of swaggering camaraderie , but more often just feels generic , derivative and done to death . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0498 | it inspires a continuing and deeply satisfying awareness of the best movies as monumental ` picture shows . ' the son 's room is a triumph of gentility that earns its moments of pathos . | B | B | yes |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0235 | nothing is sacred in this gut-buster . that is a compliment to kuras and miller . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0455 | leigh 's film is full of memorable performances from top to bottom . if you believe any of this , i can make you a real deal on leftover enron stock that will double in value a week from friday . | A | A | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0364 | an entertaining , colorful , action-filled crime story with an intimate heart . a gorgeous , witty , seductive movie . | B | B | yes |

### Rule 50: 4/5

Articulated rule: Label A if and only if the first review snippet is more positive than the second; otherwise label B.

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | pairwise_same_sst2_positive_sentiment_pool_0485 | it 's clear the filmmakers were n't sure where they wanted their story to go , and even more clear that they lack the skills to get us to this undetermined destination . in execution , this clever idea is far less funny than the original , killers from space . | B | B | yes |
| 2 | pairwise_same_sst2_positive_sentiment_pool_0237 | the notion that bombing buildings is the funniest thing in the world goes entirely unexamined in this startlingly unfunny comedy . an exquisitely crafted and acted tale . | A | B | no |
| 3 | pairwise_same_sst2_positive_sentiment_pool_0287 | what distinguishes time of favor from countless other thrillers is its underlying concern with the consequences of words and with the complicated emotions fueling terrorist acts . the plot convolutions ultimately add up to nothing more than jerking the audience 's chain . | A | A | yes |
| 4 | pairwise_same_sst2_positive_sentiment_pool_0304 | a quiet treasure -- a film to be savored . there 's something auspicious , and daring , too , about the artistic instinct that pushes a majority-oriented director like steven spielberg to follow a.i. with this challenging report so liable to unnerve the majority . | B | B | yes |
| 5 | pairwise_same_sst2_positive_sentiment_pool_0386 | a grimly competent and stolid and earnest military courtroom drama . it is great summer fun to watch arnold and his buddy gerald bounce off a quirky cast of characters . | B | B | yes |

