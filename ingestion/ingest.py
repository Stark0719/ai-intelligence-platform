import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from preprocessing.clean_text import clean_text
from preprocessing.chunker import chunk_text

def ingest_file(file_path: Path):
    text = file_path.read_text()
    cleaned = clean_text(text)
    chunks = chunk_text(cleaned)

    return {
        "source": file_path.name,
        "chunks": chunks
    }

def ingest_directory(dir_path: str):
    results = []
    for file in Path(dir_path).glob("*.txt"):
        results.append(ingest_file(file))
    return results


if __name__ == "__main__":
    resumes = ingest_directory("data/resumes")
    jobs = ingest_directory("data/jobs")

    print("Resumes:", resumes)
    print("Jobs:", jobs)
