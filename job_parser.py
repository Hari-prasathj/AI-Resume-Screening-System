from resume_parser import SKILLS


def extract_required_skills(job_description):

    required_skills = []

    job_text = job_description.lower()

    for skill in SKILLS:

        if skill.lower() in job_text:
            required_skills.append(skill)

    return required_skills