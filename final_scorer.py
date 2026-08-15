def calculate_final_score(skill_score, semantic_score):

    final_score = (
        (skill_score * 0.60)
        + (semantic_score * 0.40)
    )

    return round(final_score, 2)