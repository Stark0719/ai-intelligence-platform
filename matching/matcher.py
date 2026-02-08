from embeddings.embedder import TextEmbedder
from embeddings.faiss_index import FaissIndex
from ingestion.ingest import ingest_directory
from matching.scoring import label_match

def build_resume_index():
    resumes = ingest_directory("data/resumes")

    texts = []
    metadata = []

    for doc in resumes:
        for chunk in doc["chunks"]:
            texts.append(chunk)
            metadata.append({
                "resume": doc["source"]
            })

    embedder = TextEmbedder()
    embeddings = embedder.embed(texts)

    index = FaissIndex(dimension=len(embeddings[0]))
    index.add(embeddings, metadata)

    return index, embedder


def match_resumes_to_job(job_text: str, top_k=5):
    index, embedder = build_resume_index()

    job_embedding = embedder.embed([job_text])[0]
    results = index.search(job_embedding, top_k=top_k)

    final_matches = []
    for r in results:
        final_matches.append({
            "resume": r["metadata"]["resume"],
            "score": round(r["score"], 3),
            "label": label_match(r["score"])
        })

    return sorted(final_matches, key=lambda x: x["score"], reverse=True)
