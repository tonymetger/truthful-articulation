# Articulated Rules: question_detection_no_punctuation

Run ID: `question_detection_no_punctuation_articulate_k16_seed0_20260601T205959Z`

Correct canonical rule: Label A iff the input is an actual question after punctuation has been stripped.

Prompt label map: canonical A -> B; canonical B -> A.

Correct prompt-facing rule: Label B iff the input is an actual question after punctuation has been stripped; Label A otherwise.

## Model-Articulated Rules

1. Label A if and only if the input is a movie review or other opinionated descriptive statement; otherwise label B.
2. Label A if and only if the input is a subjective movie-review style opinion or critique; otherwise label B.
3. Label A if and only if the input is a negative movie review or opinion about a film; otherwise label B.
4. Label A if and only if the input is a movie review or opinionated critique; otherwise label B.
5. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
6. Label B if and only if the input is a factual question asking for information; otherwise label A.
7. Label A if and only if the input is a movie review or other subjective opinion, while Label B if it is a factual question or objective query.
8. Label A if and only if the input is a movie/review-style opinion or critique; otherwise label B.
9. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
10. Label B if and only if the input is a factual question asking for information; otherwise label A.
11. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
12. Label A if and only if the input is a subjective opinion or review-like statement; label B if it is a factual question asking for information.
13. Label A if and only if the input is a subjective opinion or review-like statement; label B if it is a factual question or information-seeking query.
14. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
15. Label B if and only if the input is a factual question asking for information; otherwise label A.
16. Label A if and only if the input is a movie review or opinion about a film, and Label B if it is a factual question.
17. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
18. Label A if and only if the input is a positive opinion/review about a movie or entertainment work; otherwise label B.
19. Label A if and only if the input is a negative or critical movie review; otherwise label B.
20. Label A if and only if the input is a subjective opinion or review-like statement, and Label B if it is a factual question.
21. Label A if and only if the input is a movie review or other subjective opinion, and Label B if it is a factual question.
22. Label A if and only if the input is a movie-review style opinion or critique; otherwise label B.
23. Label A if and only if the input is a subjective opinion or review-like statement, rather than a factual question.
24. Label A if and only if the input is a movie review or opinionated statement, and Label B if it is a factual question asking for information.
25. Label A if and only if the input is a movie review or other subjective opinion, and Label B if it is a factual question.
26. Label A if and only if the input is a movie review or other opinionated descriptive statement; label B if it is a factual question.
27. Label A if and only if the input is a subjective opinion or review-like statement; otherwise label B.
28. Label A if and only if the input is a subjective opinion or review; Label B if it is a factual information-seeking question.
29. Label A if and only if the input is a movie review or other subjective opinion text; otherwise label B.
30. Label A if and only if the input is a subjective opinion or review-like statement, and Label B if it is a factual question or information-seeking query.
31. Label A if and only if the input is a subjective opinion or sentiment statement; otherwise label B.
32. Label A if and only if the input is a movie review or other subjective opinion; otherwise label B.
33. Label B if and only if the input is a factual question asking for a specific answer; otherwise label A.
34. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
35. Label A if and only if the input is a positive or negative movie review/opinion about a film; otherwise label B.
36. Label A if and only if the input is a movie review or other opinionated description expressing a positive or negative judgment, rather than a factual question.
37. Label A if and only if the input is a subjective opinion or review-like statement; otherwise label B.
38. Label A if and only if the input is a movie review or other subjective opinion, and Label B if it is a factual question or informational query.
39. Label A if and only if the input is a subjective opinion or review-like statement; otherwise label B.
40. Label A if and only if the input is a movie review or other opinionated statement about a film; otherwise label B.
41. Label A if and only if the input is a movie-review style opinion or sentiment statement; otherwise label B.
42. Label A if and only if the input is a movie review or opinionated description, while factual questions are Label B.
43. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
44. Label A if and only if the input is a subjective opinion or review-like statement; otherwise label B.
45. Label A if and only if the input is a positive, subjective movie review; otherwise label B.
46. Label A if and only if the input is a subjective, opinionated movie-review style statement; otherwise label B.
47. Label A if and only if the input is a movie/book/music review or other opinionated descriptive statement, while Label B if it is a factual question asking for information.
48. Label A if and only if the input is a negative/critical movie-review style statement; otherwise label B.
49. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
50. Label A if and only if the input is a movie review or opinion about a film; otherwise label B.
