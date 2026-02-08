from llm.prompts import explanation_prompt
from llm.ollama_client import run_ollama

def explain_match(job_text, resume_text, score, label):
    prompt = explanation_prompt(
        job_text=job_text,
        resume_text=resume_text,
        score=score,
        label=label
    )
    return run_ollama(prompt)
