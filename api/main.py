from fastapi import FastAPI
from pydantic import BaseModel
from matching.matcher import match_resumes_to_job
from llm.explain import explain_match
from ingestion.ingest import ingest_directory


app = FastAPI(
    title="Job Matching API",
    description="LLM + ML powered resume to job matching system",
    version="1.0.0"
)

class ExplainRequest(BaseModel):
    resume_name: str
    job_description: str
    score: float
    label: str

class JobRequest(BaseModel):
    job_description: str
    top_k: int = 5


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/match")
def match_job(request: JobRequest):
    matches = match_resumes_to_job(
        job_text=request.job_description,
        top_k=request.top_k
    )
    return {
        "matches": matches,
        "total_matches": len(matches)
    }

@app.post("/explain")
def explain(request: ExplainRequest):
    resumes = ingest_directory("data/resumes")
    resume_text = ""

    for r in resumes:
        if r["source"] == request.resume_name:
            resume_text = " ".join(r["chunks"])

    explanation = explain_match(
        job_text=request.job_description,
        resume_text=resume_text,
        score=request.score,
        label=request.label
    )

    return {
        "resume": request.resume_name,
        "explanation": explanation
    }