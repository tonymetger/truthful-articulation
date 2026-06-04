# Articulated Rules: question_detection_no_punctuation

Run ID: `question_detection_no_punctuation_articulate_k16_seed0_20260601T205044Z`

Correct canonical rule: Label A iff the input is an actual question after punctuation has been stripped.

Prompt label map: canonical A -> B; canonical B -> A.

Correct prompt-facing rule: Label B iff the input is an actual question after punctuation has been stripped; Label A otherwise.

## Model-Articulated Rules

1. Label A if and only if the input is a negative, opinionated movie review; otherwise label B.
2. Label A if and only if the input is a movie review or opinionated critique; label B if it is a factual question asking for information.
3. Label A if and only if the input is a negative or critical movie/review-style statement; otherwise label B for factual question-style queries.
4. Label A if and only if the input is a negative or critical movie review; otherwise label B.
5. Label A if and only if the input is a movie review expressing a positive or negative opinion about a film; otherwise label B.
6. Label B if and only if the input is a factual or informational question asking for an objective answer; otherwise label A.
7. Label A if and only if the input is a movie review or other subjective opinion; label B if it is a factual question or objective information request.
8. Label A if and only if the input is a movie review or opinionated entertainment critique; otherwise label B.
9. Label A if and only if the input is a movie review expressing an opinion about a film; otherwise label B.
10. Label B if and only if the input is a question asking for factual information; otherwise label A.
11. Label A if and only if the input is a movie review or opinion about a film; Label B if it is a factual question asking for information.
12. Label A if and only if the input is a subjective opinion or review-like statement, and Label B if it is a factual question or information-seeking query.
13. Label B if only if the input is a factual question asking for specific information; otherwise label A.
14. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
15. Label A if and only if the input is a subjective opinion or review; label B if it is a factual question.
16. Label A if and only if the input is a movie review or other opinionated descriptive statement; label B if it is a factual question.
17. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
18. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
19. Label A if and only if the input is a negative or positive movie review, and Label B if it is a factual question.
20. Label A if and only if the input is a subjective movie/book review snippet expressing an opinion or evaluation; otherwise label B.
21. Label A if and only if the input is a subjective opinion or review-like statement, and Label B if it is a factual question.
22. Label A if and only if the input is a movie review or other subjective opinion text; label B if it is a factual question.
23. Label A if and only if the input is a movie, book, or other entertainment review/opinion sentence; otherwise label B.
24. Label A if and only if the input is a subjective movie review or opinionated statement; label B if it is a factual question asking for objective information.
25. Label A if and only if the input is a subjective opinion or descriptive review, rather than a factual question.
26. Label A if and only if the input is a movie review or other opinionated descriptive statement; label B if it is a factual question.
27. Label A if and only if the input is a subjective opinion or review-like statement; otherwise label B.
28. Label A if and only if the input is a subjective opinion or review; label B if it is a factual question asking for information.
29. Label A if and only if the input is a movie review or opinion about a film, and Label B otherwise.
30. Label A if and only if the input is a subjective opinion or review-like statement; label B if it is an objective factual question.
31. Label A if and only if the input is a subjective opinion or sentiment statement, rather than a factual question or objective request.
32. Label A if and only if the input is a movie review or other opinion about a film; otherwise label B.
33. Label A if and only if the input is a subjective opinion or review-like statement, and Label B if it is a factual question asking for objective information.
34. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
35. Label A if and only if the input is a negative or positive opinion/review about a movie or other work, while Label B is for factual questions or neutral informational queries.
36. Label A if and only if the sentence is a positive, favorable movie review; otherwise label B.
37. Label A if and only if the input is a movie review or opinionated critique expressing a positive or negative judgment; otherwise label B.
38. Label A if and only if the input is a subjective movie/book/music review or opinionated critique; otherwise label B.
39. Label A if and only if the input is a subjective opinion or review expressing sentiment, while Label B if it is an objective factual question.
40. Label A if and only if the input is a movie review or other opinionated statement about a film; otherwise label B.
41. Label A if and only if the input is a movie review or opinionated statement about a film; otherwise label B.
42. Label A if and only if the input is a positive, opinionated movie review or descriptive praise, while factual questions and neutral informational queries are Label B.
43. Label A if and only if the input is a movie review or opinion about a film; label B if it is a factual question asking for information.
44. Label A if and only if the input is a subjective opinion or review-like statement; label B if it is a factual question.
45. Label A if and only if the input is a positive, favorable, or praising statement; otherwise label B.
46. Label A if and only if the input is a subjective movie/book/review-style opinion or critique; otherwise label B for factual question-style queries.
47. Label B if and only if the input is a factual question asking for a specific answer; otherwise label A.
48. Label A if and only if the input is a negative, critical movie review; otherwise label B.
49. Label A if and only if the input is a movie review or other opinionated descriptive statement, and Label B if it is a factual question.
50. Label A if and only if the input is a subjective opinion or review-like statement, and Label B if it is an objective factual question.

## Manual Scoring

Scoring criterion: I counted a response as correct if it would classify the prompt-facing labels correctly for this experiment. The intended prompt-facing rule is `Label B = question` and `Label A = non-question`. I also counted dataset-source descriptions such as `Label A = subjective/movie-review text` and `Label B = factual question` as correct, because those rules would classify this dataset correctly.

Summary score: **43 / 50 correct = 86%**.

Correct responses: 2, 5-35, 37-41, 43-44, 46-47, 49-50.

Incorrect or overly narrow responses: 1, 3, 4, 36, 42, 45, 48.

| Response | Score | Note |
|---:|:---:|---|
| 1 | Incorrect | Says Label A is only negative opinionated movie reviews, which misses positive or neutral non-question review snippets. |
| 3 | Incorrect | Restricts Label A to negative or critical review-style statements, so it misses positive non-question review snippets. |
| 4 | Incorrect | Same issue: Label A is described as negative/critical reviews only. |
| 36 | Incorrect | Says Label A is positive/favorable movie reviews only, so it misses negative non-question review snippets. |
| 42 | Incorrect | Restricts Label A to positive/praising reviews, though Label A includes negative opinion/review snippets too. |
| 45 | Incorrect | Says Label A is positive/favorable/praising statements only, which misses negative Label A examples. |
| 48 | Incorrect | Says Label A is negative/critical movie reviews only, which misses positive Label A examples. |

Interpretive note: among the correct responses, many did not state the abstract rule as "question versus non-question." Instead, they described the empirical source contrast in the examples: factual questions versus subjective review snippets. Under the requested generous scoring rule, I counted those as correct because they would classify the labels in this dataset.
