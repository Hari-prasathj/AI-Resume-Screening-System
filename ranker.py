def rank_candidates(candidates):

    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: candidate["final_score"],
        reverse=True
    )

    for rank, candidate in enumerate(
        ranked_candidates,
        start=1
    ):
        candidate["rank"] = rank

    return ranked_candidates