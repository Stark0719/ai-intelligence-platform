import faiss
import numpy as np

class FaissIndex:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatIP(dimension)
        self.metadata = []

    def add(self, embeddings, metadata):
        embeddings = np.array(embeddings).astype("float32")
        self.index.add(embeddings)
        self.metadata.extend(metadata)

    def search(self, query_embedding, top_k=5):
        query_embedding = np.array([query_embedding]).astype("float32")
        scores, indices = self.index.search(query_embedding, top_k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            # FAISS uses -1 index or extremely negative score for empty slots
            if idx < 0 or score < 0:
                continue

            results.append({
                "score": float(score),
                "metadata": self.metadata[idx]
            })

        return results
