import statistics

def compute_scores(scores):
    """
    scores = list of dicts like:
    {
        "relevance": 4,
        "tone": 5,
        "clarity": 4,
        "completeness": 3,
        "safety": 5
    }
    """

    overall_scores = []
    for s in scores:
        overall = statistics.mean([
            s["relevance"],
            s["tone"],
            s["clarity"],
            s["completeness"],
            s["safety"]
        ])
        overall_scores.append(overall)

    print("\n=== Quality Evaluation Summary ===")
    print(f"Number of samples: {len(scores)}")
    print(f"Average overall score: {round(statistics.mean(overall_scores), 2)}")
    print(f"% ≥ 4.0: {round(sum(1 for o in overall_scores if o >= 4.0) / len(overall_scores) * 100, 2)}%")
    print("==================================\n")


if __name__ == "__main__":
    # Example manual scores (replace with real evaluations)
    sample_scores = [
        {"relevance": 4, "tone": 5, "clarity": 4, "completeness": 4, "safety": 5},
        {"relevance": 5, "tone": 4, "clarity": 4, "completeness": 3, "safety": 5},
        {"relevance": 3, "tone": 4, "clarity": 3, "completeness": 3, "safety": 5},
    ]

    compute_scores(sample_scores)
