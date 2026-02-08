from ingestion.ingest import ingest_directory
from matching.matcher import match_resumes_to_job

if __name__ == "__main__":
    jobs = ingest_directory("data/jobs")
    job_text = jobs[0]["chunks"][0]

    matches = match_resumes_to_job(job_text)

    for m in matches:
        print(m)
