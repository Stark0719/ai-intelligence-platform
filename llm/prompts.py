def explanation_prompt(job_text, resume_text, score, label):
    return f"""
You are an AI hiring assistant.

Job Description:
{job_text}

Resume:
{resume_text}

Match Score: {score}
Match Label: {label}

Explain in 3–5 bullet points:
- Why this resume matches or does not match the job
- Key overlapping skills
- Missing or weaker areas (if any)

Be concise and professional.
"""
