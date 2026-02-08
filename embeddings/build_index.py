from ingestion.ingest import ingest_directory
from embeddings.embedder import TextEmbedder
from embeddings.faiss_index import FaissIndex

def build_index(data_dir, label):
    docs = ingest_directory(data_dir)

    texts = []
    metadata = []

    for doc in docs:
        for chunk in doc["chunks"]:
            texts.append(chunk)
            metadata.append({
                "source": doc["source"],
                "type": label
            })

    embedder = TextEmbedder()
    embeddings = embedder.embed(texts)

    index = FaissIndex(dimension=len(embeddings[0]))
    index.add(embeddings, metadata)

    return index, embedder


if __name__ == "__main__":
    resume_index, embedder = build_index("data/resumes", "resume")
    job_index, _ = build_index("data/jobs", "job")

    query = "machine learning engineer with python and NLP experience"
    query_embedding = embedder.embed([query])[0]

    results = resume_index.search(query_embedding)
    print(results)
