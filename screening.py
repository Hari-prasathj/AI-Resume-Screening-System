from resume_parser import (
    extract_text_from_pdf,
    extract_name,
    extract_email,
    extract_phone,
    extract_skills
)

from job_parser import extract_required_skills
from matcher import calculate_match
from semantic_matcher import calculate_semantic_similarity
from final_scorer import calculate_final_score


def screen_resume(pdf_path, job_description):

    resume_text = extract_text_from_pdf(pdf_path)

    name = extract_name(resume_text)
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)

    resume_skills = extract_skills(resume_text)

    required_skills = extract_required_skills(
        job_description
    )

    match_result = calculate_match(
        resume_skills,
        required_skills
    )

    skill_score = match_result["score"]

    semantic_score = calculate_semantic_similarity(
        resume_text,
        job_description
    )

    final_score = calculate_final_score(
        skill_score,
        semantic_score
    )

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skill_score": skill_score,
        "semantic_score": semantic_score,
        "final_score": final_score,
        "matched_skills": match_result["matched_skills"],
        "missing_skills": match_result["missing_skills"]
    }
