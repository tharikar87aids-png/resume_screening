job_skills = [
    "python", "java", "sql", "machine learning",
    "html", "css", "flask"
]
def match_resume(resume_text):
    matched = 0
    for skill in job_skills:
        if skill in resume_text:
            matched += 1
    score = (matched / len(job_skills)) * 100
    return round(score, 2)
