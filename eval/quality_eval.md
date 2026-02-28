# Reply Quality Evaluation (Rubric)

Each generated reply is scored from 0–5 on each dimension:

1. Relevance (0–5): Addresses the email’s main request/question.
2. Tone (0–5): Matches expected professional tone; polite and appropriate.
3. Clarity (0–5): Clear, readable, minimal ambiguity.
4. Completeness (0–5): Includes necessary details / next steps.
5. Safety (0–5): No hallucinated facts, no sensitive info leakage.

## Aggregate metrics reported
- Mean score per dimension
- Overall mean score (average of the 5 dimensions)
- % of replies with overall score ≥ 4.0

## Notes
- This rubric is designed to be model-agnostic and reproducible.
- In future iterations, scoring can be automated using an LLM-as-a-judge or human annotation.
