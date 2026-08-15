def calculate_match(resume_skills, required_skills):

    resume_skills_set = {
        skill.lower()
        for skill in resume_skills
    }

    required_skills_set = {
        skill.lower()
        for skill in required_skills
    }

    matched_skills = resume_skills_set.intersection(
        required_skills_set
    )

    missing_skills = required_skills_set.difference(
        resume_skills_set
    )

    if len(required_skills_set) == 0:
        score = 0
    else:
        score = (
            len(matched_skills)
            / len(required_skills_set)
        ) * 100

    return {
        "score": round(score, 2),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills)
    }