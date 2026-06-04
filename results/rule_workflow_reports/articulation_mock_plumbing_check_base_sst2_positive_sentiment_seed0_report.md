# Rule Articulation Workflow: sst2_positive_sentiment

Run ID: `articulation_mock_plumbing_check_base_sst2_positive_sentiment_seed0`

Correct prompt-facing rule: Label B iff the sentence expresses positive sentiment; Label A otherwise.

## Summary

- Articulated rules: 50
- Evaluation examples per rule: 5
- Total rule-application calls: 250
- Rule-application accuracy: 0.456
- Nonparseable rate: 0.000
- Mean per-rule accuracy: 0.456
- Rules with all evals correct: 1
- Rules with any eval correct: 48

## Settings

- Articulation model: `mock`
- Rule-application model: `mock`
- k-shot examples per articulated rule: `16`
- Seed: `0`
- Articulation prompt template: `minimal_rule_description`
- Rule-application prompt template: `minimal_rule_application`
- Label assignment: `random_per_seed`, swap=`True`

## Rule-Level Results

| Rule | Rule Accuracy | Articulated Rule |
|---:|---:|---|
| 1 | 2/5 | B |
| 2 | 1/5 | A |
| 3 | 3/5 | A |
| 4 | 2/5 | B |
| 5 | 2/5 | A |
| 6 | 4/5 | A |
| 7 | 2/5 | A |
| 8 | 1/5 | A |
| 9 | 2/5 | B |
| 10 | 3/5 | A |
| 11 | 2/5 | B |
| 12 | 0/5 | A |
| 13 | 3/5 | A |
| 14 | 3/5 | A |
| 15 | 4/5 | A |
| 16 | 2/5 | B |
| 17 | 5/5 | A |
| 18 | 2/5 | B |
| 19 | 2/5 | B |
| 20 | 1/5 | A |
| 21 | 4/5 | A |
| 22 | 2/5 | A |
| 23 | 4/5 | B |
| 24 | 2/5 | A |
| 25 | 3/5 | B |
| 26 | 2/5 | B |
| 27 | 3/5 | B |
| 28 | 1/5 | A |
| 29 | 3/5 | B |
| 30 | 2/5 | A |
| 31 | 1/5 | B |
| 32 | 2/5 | B |
| 33 | 2/5 | A |
| 34 | 3/5 | B |
| 35 | 2/5 | A |
| 36 | 0/5 | A |
| 37 | 4/5 | B |
| 38 | 3/5 | A |
| 39 | 3/5 | B |
| 40 | 2/5 | B |
| 41 | 2/5 | B |
| 42 | 1/5 | A |
| 43 | 1/5 | A |
| 44 | 2/5 | B |
| 45 | 3/5 | A |
| 46 | 2/5 | B |
| 47 | 2/5 | B |
| 48 | 1/5 | A |
| 49 | 4/5 | A |
| 50 | 2/5 | A |

## Detailed Evaluations

### Rule 1: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0375 | the inspirational screenplay by mike rich covers a lot of ground , perhaps too much , but ties things together , neatly , by the end . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0346 | it 's so mediocre , despite the dynamic duo on the marquee , that we just ca n't get no satisfaction . | A | A | yes |
| 3 | sst2_positive_sentiment_pool_0104 | feels haphazard , as if the writers mistakenly thought they could achieve an air of frantic spontaneity by simply tossing in lots of characters doing silly stuff and stirring the pot . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0417 | despite its title , punch-drunk love is never heavy-handed . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0035 | neither parker nor donovan is a typical romantic lead , but they bring a fresh , quirky charm to the formula . | B | A | no |

### Rule 2: 1/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0136 | very special effects , brilliantly bold colors and heightened reality ca n't hide the giant achilles ' heel in `` stuart little 2 `` : there 's just no story , folks . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0272 | the iditarod lasts for days - this just felt like it did . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0129 | allows us to hope that nolan is poised to embark a major career as a commercial yet inventive filmmaker . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0483 | as vulgar as it is banal . | A | A | yes |
| 5 | sst2_positive_sentiment_pool_0430 | escaping the studio , piccoli is warmly affecting and so is this adroitly minimalist movie . | B | A | no |

### Rule 3: 3/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0048 | you do n't have to know about music to appreciate the film 's easygoing blend of comedy and romance . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0254 | the story and structure are well-honed . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0414 | so much facile technique , such cute ideas , so little movie . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0008 | i can take infantile humor ... but this is the sort of infantile that makes you wonder about changing the director and writer 's diapers . | A | A | yes |
| 5 | sst2_positive_sentiment_pool_0362 | what the director ca n't do is make either of val kilmer 's two personas interesting or worth caring about . | A | B | no |

### Rule 4: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0378 | ... a hollow joke told by a cinematic gymnast having too much fun embellishing the misanthropic tale to actually engage it . | A | A | yes |
| 2 | sst2_positive_sentiment_pool_0297 | i sympathize with the plight of these families , but the movie does n't do a very good job conveying the issue at hand . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0144 | moody , heartbreaking , and filmed in a natural , unforced style that makes its characters seem entirely convincing even when its script is not . | B | B | yes |
| 4 | sst2_positive_sentiment_pool_0125 | the talented and clever robert rodriguez perhaps put a little too much heart into his first film and did n't reserve enough for his second . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0381 | that is a compliment to kuras and miller . | B | A | no |

### Rule 5: 2/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0039 | nervous breakdowns are not entertaining . | A | A | yes |
| 2 | sst2_positive_sentiment_pool_0193 | the quality of the art combined with the humor and intelligence of the script allow the filmmakers to present the biblical message of forgiveness without it ever becoming preachy or syrupy . | B | A | no |
| 3 | sst2_positive_sentiment_pool_0010 | if you believe any of this , i can make you a real deal on leftover enron stock that will double in value a week from friday . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0157 | this nickleby thing might have more homosexual undertones than an eddie murphy film . | A | A | yes |
| 5 | sst2_positive_sentiment_pool_0176 | davis ... is so enamored of her own creation that she ca n't see how insufferable the character is . | A | B | no |

### Rule 6: 4/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0258 | it has charm to spare , and unlike many romantic comedies , it does not alienate either gender in the audience . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0292 | immersing us in the endlessly inventive , fiercely competitive world of hip-hop djs , the project is sensational and revelatory , even if scratching makes you itch . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0361 | it 's refreshing to see a girl-power movie that does n't feel it has to prove anything . | B | B | yes |
| 4 | sst2_positive_sentiment_pool_0411 | the socio-histo-political treatise is told in earnest strides ... ( and ) personal illusion is deconstructed with poignancy . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0472 | / but daphne , you 're too buff / fred thinks he 's tough / and velma - wow , you 've lost weight ! | A | A | yes |

### Rule 7: 2/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0156 | for anyone unfamiliar with pentacostal practices in general and theatrical phenomenon of hell houses in particular , it 's an eye-opener . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0328 | cq 's reflection of artists and the love of cinema-and-self suggests nothing less than a new voice that deserves to be considered as a possible successor to the best european directors . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0330 | a gripping movie , played with performances that are all understated and touching . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0436 | not an objectionable or dull film ; it merely lacks everything except good intentions . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0369 | add yet another hat to a talented head , clooney 's a good director . | B | A | no |

### Rule 8: 1/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0412 | so unremittingly awful that labeling it a dog probably constitutes cruelty to canines . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0277 | another in-your-face wallow in the lower depths made by people who have never sung those blues . | A | A | yes |
| 3 | sst2_positive_sentiment_pool_0463 | scooby dooby doo / and shaggy too / you both look and sound great . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0027 | stephen rea , aidan quinn , and alan bates play desmond 's legal eagles , and when joined by brosnan , the sight of this grandiloquent quartet lolling in pretty irish settings is a pleasant enough thing , ` tis . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0104 | feels haphazard , as if the writers mistakenly thought they could achieve an air of frantic spontaneity by simply tossing in lots of characters doing silly stuff and stirring the pot . | A | B | no |

### Rule 9: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0103 | for the most part , director anne-sophie birot 's first feature is a sensitive , extraordinarily well-acted drama . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0122 | nothing is sacred in this gut-buster . | A | A | yes |
| 3 | sst2_positive_sentiment_pool_0063 | for the most part , it 's a work of incendiary genius , steering clear of knee-jerk reactions and quick solutions . | B | B | yes |
| 4 | sst2_positive_sentiment_pool_0488 | not since japanese filmmaker akira kurosawa 's ran have the savagery of combat and the specter of death been visualized with such operatic grandeur . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0341 | the director knows how to apply textural gloss , but his portrait of sex-as-war is strictly sitcom . | A | B | no |

### Rule 10: 3/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0041 | the special effects and many scenes of weightlessness look as good or better than in the original , while the oscar-winning sound and james horner 's rousing score make good use of the hefty audio system . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0298 | slick piece of cross-promotion . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0300 | i got a headache watching this meaningless downer . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0177 | does little more than play an innocuous game of fill-in - the-blanks with a tragic past . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0409 | i 'll bet the video game is a lot more fun than the film . | A | A | yes |

### Rule 11: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0068 | as ` chick flicks ' go , this one is pretty miserable , resorting to string-pulling rather than legitimate character development and intelligent plotting . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0050 | an operatic , sprawling picture that 's entertainingly acted , magnificently shot and gripping enough to sustain most of its 170-minute length . | B | A | no |
| 3 | sst2_positive_sentiment_pool_0300 | i got a headache watching this meaningless downer . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0209 | of course , by more objective measurements it 's still quite bad . | A | A | yes |
| 5 | sst2_positive_sentiment_pool_0162 | a wildly inconsistent emotional experience . | A | A | yes |

### Rule 12: 0/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0244 | the overall effect is less like a children 's movie than a recruitment film for future hollywood sellouts . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0011 | care deftly captures the wonder and menace of growing up , but he never really embraces the joy of fuhrman 's destructive escapism or the grace-in-rebellion found by his characters . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0412 | so unremittingly awful that labeling it a dog probably constitutes cruelty to canines . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0291 | director andrew niccol ... demonstrates a wry understanding of the quirks of fame . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0482 | i thought my own watch had stopped keeping time as i slogged my way through clockstoppers . | A | B | no |

### Rule 13: 3/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0086 | there 's enough melodrama in this magnolia primavera to make pta proud yet director muccino 's characters are less worthy of puccini than they are of daytime television . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0046 | there 's a wickedly subversive bent to the best parts of birthday girl . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0182 | the lower your expectations , the more you 'll enjoy it . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0023 | the jabs it employs are short , carefully placed and dead-center . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0482 | i thought my own watch had stopped keeping time as i slogged my way through clockstoppers . | A | B | no |

### Rule 14: 3/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0038 | what distinguishes time of favor from countless other thrillers is its underlying concern with the consequences of words and with the complicated emotions fueling terrorist acts . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0238 | a poignant , artfully crafted meditation on mortality . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0260 | a sequel that 's much too big for its britches . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0140 | coughs and sputters on its own postmodern conceit . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0362 | what the director ca n't do is make either of val kilmer 's two personas interesting or worth caring about . | A | B | no |

### Rule 15: 4/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0387 | so unassuming and pure of heart , you ca n't help but warmly extend your arms and yell ` safe ! ' | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0456 | it proves quite compelling as an intense , brooding character study . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0297 | i sympathize with the plight of these families , but the movie does n't do a very good job conveying the issue at hand . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0444 | professionally speaking , it 's tempting to jump ship in january to avoid ridiculous schlock like this shoddy suspense thriller . | A | A | yes |
| 5 | sst2_positive_sentiment_pool_0151 | generally , clockstoppers will fulfill your wildest fantasies about being a different kind of time traveler , while happily killing 94 minutes . | B | B | yes |

### Rule 16: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0151 | generally , clockstoppers will fulfill your wildest fantasies about being a different kind of time traveler , while happily killing 94 minutes . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0460 | if you are an actor who can relate to the search for inner peace by dramatically depicting the lives of others onstage , then esther 's story is a compelling quest for truth . | B | A | no |
| 3 | sst2_positive_sentiment_pool_0343 | i am sorry that i was unable to get the full brunt of the comedy . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0377 | a grimly competent and stolid and earnest military courtroom drama . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0240 | this is a shameless sham , calculated to cash in on the popularity of its stars . | A | A | yes |

### Rule 17: 5/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0157 | this nickleby thing might have more homosexual undertones than an eddie murphy film . | A | A | yes |
| 2 | sst2_positive_sentiment_pool_0186 | awesome creatures , breathtaking scenery , and epic battle scenes add up to another ` spectacular spectacle . ' | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0341 | the director knows how to apply textural gloss , but his portrait of sex-as-war is strictly sitcom . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0116 | a rewarding work of art for only the most patient and challenge-hungry moviegoers . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0337 | the notion that bombing buildings is the funniest thing in the world goes entirely unexamined in this startlingly unfunny comedy . | A | A | yes |

### Rule 18: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0089 | it provides an honest look at a community striving to anchor itself in new grounds . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0096 | in the end , we are left with something like two ships passing in the night rather than any insights into gay love , chinese society or the price one pays for being dishonest . | A | A | yes |
| 3 | sst2_positive_sentiment_pool_0155 | it made me want to wrench my eyes out of my head and toss them at the screen . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0012 | if you enjoy more thoughtful comedies with interesting conflicted characters ; this one is for you . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0374 | while ( hill ) has learned new tricks , the tricks alone are not enough to salvage this lifeless boxing film . | A | B | no |

### Rule 19: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0037 | its story may be a thousand years old , but why did it have to seem like it took another thousand to tell it to us ? | A | B | no |
| 2 | sst2_positive_sentiment_pool_0387 | so unassuming and pure of heart , you ca n't help but warmly extend your arms and yell ` safe ! ' | B | A | no |
| 3 | sst2_positive_sentiment_pool_0291 | director andrew niccol ... demonstrates a wry understanding of the quirks of fame . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0233 | the vitality of the actors keeps the intensity of the film high , even as the strafings blend together . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0078 | whether writer-director anne fontaine 's film is a ghost story , an account of a nervous breakdown , a trip down memory lane , all three or none of the above , it is as seductive as it is haunting . | B | B | yes |

### Rule 20: 1/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0347 | while its careful pace and seemingly opaque story may not satisfy every moviegoer 's appetite , the film 's final scene is soaringly , transparently moving . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0204 | there are plot holes big enough for shamu the killer whale to swim through . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0021 | it 's hard to like a film about a guy who is utterly unlikeable , and shiner , starring michael caine as an aging british boxing promoter desperate for a taste of fame and fortune , is certainly that . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0269 | the script is n't very good ; not even someone as gifted as hoffman ( the actor ) can make it work . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0258 | it has charm to spare , and unlike many romantic comedies , it does not alienate either gender in the audience . | B | A | no |

### Rule 21: 4/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0470 | ( d ) oes n't bother being as cloying or preachy as equivalent evangelical christian movies -- maybe the filmmakers know that the likely audience will already be among the faithful . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0095 | at the very least , if you do n't know anything about derrida when you walk into the theater , you wo n't know much more when you leave . | A | A | yes |
| 3 | sst2_positive_sentiment_pool_0079 | sustains its dreamlike glide through a succession of cheesy coincidences and voluptuous cheap effects , not the least of which is rebecca romijn-stamos . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0485 | a marvel like none you 've seen . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0004 | it seems like i have been waiting my whole life for this movie and now i ca n't wait for the sequel . | B | B | yes |

### Rule 22: 2/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0471 | or doing last year 's taxes with your ex-wife . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0168 | rarely has so much money delivered so little entertainment . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0184 | corpus collosum -- while undeniably interesting -- wore out its welcome well before the end credits rolled about 45 minutes in . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0177 | does little more than play an innocuous game of fill-in - the-blanks with a tragic past . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0152 | an exquisitely crafted and acted tale . | B | B | yes |

### Rule 23: 4/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0338 | broomfield turns his distinctive ` blundering ' style into something that could really help clear up the case . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0367 | dragonfly has no atmosphere , no tension -- nothing but costner , flailing away . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0286 | no one but a convict guilty of some truly heinous crime should have to sit through the master of disguise . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0003 | once the 50 year old benigni appears as the title character , we find ourselves longing for the block of wood to come back . | A | A | yes |
| 5 | sst2_positive_sentiment_pool_0457 | looks and feels like a project better suited for the small screen . | A | A | yes |

### Rule 24: 2/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0288 | verbinski implements every hack-artist trick to give us the ooky-spookies . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0152 | an exquisitely crafted and acted tale . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0365 | exquisitely nuanced in mood tics and dialogue , this chamber drama is superbly acted by the deeply appealing veteran bouquet and the chilling but quite human berling . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0058 | a spellbinding african film about the modern condition of rootlessness , a state experienced by millions around the globe . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0149 | a pleasant enough romance with intellectual underpinnings , the kind of movie that entertains even as it turns maddeningly predictable . | B | A | no |

### Rule 25: 3/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0034 | ultimately feels empty and unsatisfying , like swallowing a communion wafer without the wine . | A | A | yes |
| 2 | sst2_positive_sentiment_pool_0450 | this is the sort of burly action flick where one coincidence pummels another , narrative necessity is a drunken roundhouse , and whatever passes for logic is a factor of the last plot device left standing . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0230 | fun , flip and terribly hip bit of cinematic entertainment . | B | B | yes |
| 4 | sst2_positive_sentiment_pool_0309 | determined to be fun , and bouncy , with energetic musicals , the humor did n't quite engage this adult . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0429 | despite the 2-d animation , the wild thornberrys movie makes for a surprisingly cinematic experience . | B | B | yes |

### Rule 26: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0106 | has all the depth of a wading pool . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0092 | paid in full is so stale , in fact , that its most vibrant scene is one that uses clips from brian de palma 's scarface . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0221 | with tightly organized efficiency , numerous flashbacks and a constant edge of tension , miller 's film is one of 2002 's involvingly adult surprises . | B | B | yes |
| 4 | sst2_positive_sentiment_pool_0289 | worth watching for dong jie 's performance -- and for the way it documents a culture in the throes of rapid change . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0277 | another in-your-face wallow in the lower depths made by people who have never sung those blues . | A | B | no |

### Rule 27: 3/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0068 | as ` chick flicks ' go , this one is pretty miserable , resorting to string-pulling rather than legitimate character development and intelligent plotting . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0345 | the chateau cleverly probes the cross-cultural differences between gauls and yanks . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0005 | it wants to tweak them with a taste of tangy new humor . | B | B | yes |
| 4 | sst2_positive_sentiment_pool_0071 | jaglom ... put ( s ) the audience in the privileged position of eavesdropping on his characters | B | A | no |
| 5 | sst2_positive_sentiment_pool_0003 | once the 50 year old benigni appears as the title character , we find ourselves longing for the block of wood to come back . | A | A | yes |

### Rule 28: 1/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0113 | ... a magnificent drama well worth tracking down . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0139 | on the whole , the movie lacks wit , feeling and believability to compensate for its incessant coarseness and banality . | A | A | yes |
| 3 | sst2_positive_sentiment_pool_0339 | it takes a certain kind of horror movie to qualify as ` worse than expected , ' but ghost ship somehow manages to do exactly that . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0073 | i 'd have to say the star and director are the big problems here . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0063 | for the most part , it 's a work of incendiary genius , steering clear of knee-jerk reactions and quick solutions . | B | A | no |

### Rule 29: 3/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0475 | affleck and jackson are good sparring partners . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0263 | jones ... does offer a brutal form of charisma . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0053 | richard gere and diane lane put in fine performances as does french actor oliver martinez . | B | B | yes |
| 4 | sst2_positive_sentiment_pool_0366 | an exhilarating futuristic thriller-noir , minority report twists the best of technology around a gripping story , delivering a riveting , pulse intensifying escapist adventure of the first order | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0295 | wince-inducing dialogue , thrift-shop costumes , prosthetic makeup by silly putty and kmart blue-light-special effects all conspire to test trekkie loyalty . | A | B | no |

### Rule 30: 2/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0217 | at its worst , it implodes in a series of very bad special effects . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0139 | on the whole , the movie lacks wit , feeling and believability to compensate for its incessant coarseness and banality . | A | A | yes |
| 3 | sst2_positive_sentiment_pool_0296 | a valueless kiddie paean to pro basketball underwritten by the nba . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0257 | huston nails both the glad-handing and the choking sense of hollow despair . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0319 | an effectively creepy , fear-inducing ( not fear-reducing ) film from japanese director hideo nakata , who takes the superstitious curse on chain letters and actually applies it . | B | A | no |

### Rule 31: 1/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0171 | while it 's genuinely cool to hear characters talk about early rap records ( sugar hill gang , etc. ) , the constant referencing of hip-hop arcana can alienate even the savviest audiences . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0121 | too restrained to be a freak show , too mercenary and obvious to be cerebral , too dull and pretentious to be engaging ... the isle defies an easy categorization . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0299 | the humor is n't as sharp , the effects not as innovative , nor the story as imaginative as in the original . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0323 | trite , banal , cliched , mostly inoffensive . | A | A | yes |
| 5 | sst2_positive_sentiment_pool_0085 | sometimes seems less like storytelling than something the otherwise compelling director needed to get off his chest . | A | B | no |

### Rule 32: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0330 | a gripping movie , played with performances that are all understated and touching . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0300 | i got a headache watching this meaningless downer . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0225 | when the film ended , i felt tired and drained and wanted to lie on my own deathbed for a while . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0265 | puts a human face on a land most westerners are unfamiliar with . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0054 | american chai encourages rueful laughter at stereotypes only an indian-american would recognize . | A | A | yes |

### Rule 33: 2/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0082 | there are simply too many ideas floating around -- part farce , part sliding doors , part pop video -- and yet failing to exploit them . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0364 | dazzling in its complexity , disturbing for its extraordinary themes , the piano teacher is a film that defies categorisation . | B | A | no |
| 3 | sst2_positive_sentiment_pool_0413 | the piece plays as well as it does thanks in large measure to anspaugh 's three lead actresses . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0209 | of course , by more objective measurements it 's still quite bad . | A | A | yes |
| 5 | sst2_positive_sentiment_pool_0009 | `` the time machine '' is a movie that has no interest in itself . | A | A | yes |

### Rule 34: 3/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0440 | ( e ) ventually , every idea in this film is flushed down the latrine of heroism . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0282 | the words , ` frankly , my dear , i do n't give a damn , ' have never been more appropriate . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0211 | irwin is a man with enough charisma and audacity to carry a dozen films , but this particular result is ultimately held back from being something greater . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0066 | holm ... embodies the character with an effortlessly regal charisma . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0230 | fun , flip and terribly hip bit of cinematic entertainment . | B | B | yes |

### Rule 35: 2/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0233 | the vitality of the actors keeps the intensity of the film high , even as the strafings blend together . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0302 | anchored by friel and williams 's exceptional performances , the film 's power lies in its complexity . | B | A | no |
| 3 | sst2_positive_sentiment_pool_0074 | and that 's a big part of why we go to the movies . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0417 | despite its title , punch-drunk love is never heavy-handed . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0464 | ` easily my choice for one of the year 's best films . ' | B | A | no |

### Rule 36: 0/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0001 | it 's just disappointingly superficial -- a movie that has all the elements necessary to be a fascinating , involving character study , but never does more than scratch the surface . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0040 | stultifyingly , dumbfoundingly , mind-numbingly bad . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0354 | ... plot holes so large and obvious a marching band might as well be stomping through them in clown clothes , playing a college football fight song on untuned instruments . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0414 | so much facile technique , such cute ideas , so little movie . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0420 | how do you spell cliché ? | A | B | no |

### Rule 37: 4/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0497 | complete lack of originality , cleverness or even visible effort | A | A | yes |
| 2 | sst2_positive_sentiment_pool_0000 | a simple , but gritty and well-acted ensemble drama that encompasses a potent metaphor for a country still dealing with its fascist past . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0110 | martin and barbara are complex characters -- sometimes tender , sometimes angry -- and the delicate performances by sven wollter and viveka seldahl make their hopes and frustrations vivid . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0281 | there 's something auspicious , and daring , too , about the artistic instinct that pushes a majority-oriented director like steven spielberg to follow a.i. with this challenging report so liable to unnerve the majority . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0241 | perceptive in its vision of nascent industrialized world politics as a new art form , but far too clunky , didactic and saddled with scenes that seem simply an ill fit for this movie . | A | A | yes |

### Rule 38: 3/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0150 | the movie , directed by mick jackson , leaves no cliche unturned , from the predictable plot to the characters straight out of central casting . | A | B | no |
| 2 | sst2_positive_sentiment_pool_0116 | a rewarding work of art for only the most patient and challenge-hungry moviegoers . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0155 | it made me want to wrench my eyes out of my head and toss them at the screen . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0070 | leigh 's film is full of memorable performances from top to bottom . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0485 | a marvel like none you 've seen . | B | B | yes |

### Rule 39: 3/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0048 | you do n't have to know about music to appreciate the film 's easygoing blend of comedy and romance . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0261 | we root for ( clara and paul ) , even like them , though perhaps it 's an emotion closer to pity . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0384 | impostor has a handful of thrilling moments and a couple of good performances , but the movie does n't quite fly . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0429 | despite the 2-d animation , the wild thornberrys movie makes for a surprisingly cinematic experience . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0311 | it 's great escapist fun that recreates a place and time that will never happen again . | B | A | no |

### Rule 40: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0344 | bogdanovich tantalizes by offering a peep show into the lives of the era 's creme de la celluloid . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0328 | cq 's reflection of artists and the love of cinema-and-self suggests nothing less than a new voice that deserves to be considered as a possible successor to the best european directors . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0149 | a pleasant enough romance with intellectual underpinnings , the kind of movie that entertains even as it turns maddeningly predictable . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0088 | a densely constructed , highly referential film , and an audacious return to form that can comfortably sit among jean-luc godard 's finest work . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0418 | it 's hampered by a lifetime-channel kind of plot and a lead actress who is out of her depth . | A | B | no |

### Rule 41: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0088 | a densely constructed , highly referential film , and an audacious return to form that can comfortably sit among jean-luc godard 's finest work . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0305 | the draw ( for `` big bad love '' ) is a solid performance by arliss howard . | B | A | no |
| 3 | sst2_positive_sentiment_pool_0408 | the only excitement comes when the credits finally roll and you get to leave the theater . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0112 | it 's also , clearly , great fun . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0424 | the movie is what happens when you blow up small potatoes to 10 times their natural size , and it ai n't pretty . | A | B | no |

### Rule 42: 1/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0478 | there is nothing outstanding about this film , but it is good enough and will likely be appreciated most by sailors and folks who know their way around a submarine . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0171 | while it 's genuinely cool to hear characters talk about early rap records ( sugar hill gang , etc. ) , the constant referencing of hip-hop arcana can alienate even the savviest audiences . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0475 | affleck and jackson are good sparring partners . | B | A | no |
| 4 | sst2_positive_sentiment_pool_0487 | the film is beautifully mounted , but , more to the point , the issues are subtly presented , managing to walk a fine line with regard to the question of joan 's madness . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0125 | the talented and clever robert rodriguez perhaps put a little too much heart into his first film and did n't reserve enough for his second . | A | A | yes |

### Rule 43: 1/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0005 | it wants to tweak them with a taste of tangy new humor . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0020 | hit and miss as far as the comedy goes and a big ole ' miss in the way of story . | A | B | no |
| 3 | sst2_positive_sentiment_pool_0092 | paid in full is so stale , in fact , that its most vibrant scene is one that uses clips from brian de palma 's scarface . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0307 | in a way , the film feels like a breath of fresh air , but only to those that allow it in . | B | A | no |
| 5 | sst2_positive_sentiment_pool_0047 | dense with characters and contains some thrilling moments . | B | A | no |

### Rule 44: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0042 | mr. tsai is a very original artist in his medium , and what time is it there ? | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0038 | what distinguishes time of favor from countless other thrillers is its underlying concern with the consequences of words and with the complicated emotions fueling terrorist acts . | B | A | no |
| 3 | sst2_positive_sentiment_pool_0098 | in an effort , i suspect , not to offend by appearing either too serious or too lighthearted , it offends by just being wishy-washy . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0204 | there are plot holes big enough for shamu the killer whale to swim through . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0437 | on this tricky topic , tadpole is very much a step in the right direction , with its blend of frankness , civility and compassion . | B | B | yes |

### Rule 45: 3/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0066 | holm ... embodies the character with an effortlessly regal charisma . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0352 | audrey tatou has a knack for picking roles that magnify her outrageous charm , and in this literate french comedy , she 's as morning-glory exuberant as she was in amélie . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0205 | it 's the chemistry between the women and the droll scene-stealing wit and wolfish pessimism of anna chancellor that makes this `` two weddings and a funeral '' fun . | B | B | yes |
| 4 | sst2_positive_sentiment_pool_0415 | something akin to a japanese alice through the looking glass , except that it seems to take itself far more seriously . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0022 | it has its moments of swaggering camaraderie , but more often just feels generic , derivative and done to death . | A | B | no |

### Rule 46: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0336 | it moves quickly , adroitly , and without fuss ; it does n't give you time to reflect on the inanity -- and the cold war datedness -- of its premise . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0314 | a bloated gasbag thesis grotesquely impressed by its own gargantuan aura of self-importance ... | A | A | yes |
| 3 | sst2_positive_sentiment_pool_0357 | it 's inoffensive , cheerful , built to inspire the young people , set to an unending soundtrack of beach party pop numbers and aside from its remarkable camerawork and awesome scenery , it 's about as exciting as a sunburn . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0185 | instead of hiding pinocchio from critics , miramax should have hidden it from everyone . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0392 | big fat waste of time . | A | A | yes |

### Rule 47: 2/5

Articulated rule: B

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0416 | the film 's welcome breeziness and some unbelievably hilarious moments -- most portraying the idiocy of the film industry -- make it mostly worth the trip . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0221 | with tightly organized efficiency , numerous flashbacks and a constant edge of tension , miller 's film is one of 2002 's involvingly adult surprises . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0450 | this is the sort of burly action flick where one coincidence pummels another , narrative necessity is a drunken roundhouse , and whatever passes for logic is a factor of the last plot device left standing . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0255 | the story and the friendship proceeds in such a way that you 're watching a soap opera rather than a chronicle of the ups and downs that accompany lifelong friendships . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0114 | a giggle-inducing comedy with snappy dialogue and winning performances by an unlikely team of oscar-winners : susan sarandon and goldie hawn . | B | B | yes |

### Rule 48: 1/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0386 | as unseemly as its title suggests . | B | A | no |
| 2 | sst2_positive_sentiment_pool_0455 | it 's a remarkably solid and subtly satirical tour de force . | B | B | yes |
| 3 | sst2_positive_sentiment_pool_0179 | the plot convolutions ultimately add up to nothing more than jerking the audience 's chain . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0171 | while it 's genuinely cool to hear characters talk about early rap records ( sugar hill gang , etc. ) , the constant referencing of hip-hop arcana can alienate even the savviest audiences . | A | B | no |
| 5 | sst2_positive_sentiment_pool_0453 | characters still need to function according to some set of believable and comprehensible impulses , no matter how many drugs they do or how much artistic license avary employs . | A | B | no |

### Rule 49: 4/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0188 | ... the movie is just a plain old monster . | A | A | yes |
| 2 | sst2_positive_sentiment_pool_0498 | ... plays like somebody spliced random moments of a chris rock routine into what is otherwise a cliche-riddled but self-serious spy thriller . | A | A | yes |
| 3 | sst2_positive_sentiment_pool_0234 | feels too formulaic and too familiar to produce the transgressive thrills of early underground work . | A | A | yes |
| 4 | sst2_positive_sentiment_pool_0455 | it 's a remarkably solid and subtly satirical tour de force . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0365 | exquisitely nuanced in mood tics and dialogue , this chamber drama is superbly acted by the deeply appealing veteran bouquet and the chilling but quite human berling . | B | A | no |

### Rule 50: 2/5

Articulated rule: A

| Eval | Example ID | Input | True | Predicted | Correct |
|---:|---|---|:---:|:---:|:---:|
| 1 | sst2_positive_sentiment_pool_0485 | a marvel like none you 've seen . | B | B | yes |
| 2 | sst2_positive_sentiment_pool_0237 | the movie understands like few others how the depth and breadth of emotional intimacy give the physical act all of its meaning and most of its pleasure . | B | A | no |
| 3 | sst2_positive_sentiment_pool_0287 | makes for a pretty unpleasant viewing experience . | A | B | no |
| 4 | sst2_positive_sentiment_pool_0304 | an artful , intelligent film that stays within the confines of a well-established genre . | B | B | yes |
| 5 | sst2_positive_sentiment_pool_0385 | its well of thorn and vinegar ( and simple humanity ) has long been plundered by similar works featuring the insight and punch this picture so conspicuously lacks . | A | B | no |

