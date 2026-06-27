import json

from app.ingestion.document_loader import load_documents
from app.ingestion.chunker import chunk_text

documents = load_documents()

all_chunks = []

print("\nLoading Documents...\n")

for doc in documents:

    print(f"Processing: {doc['filename']}")

    chunks = chunk_text(doc["content"])

    print(f"Generated {len(chunks)} chunks")

    for idx, chunk in enumerate(chunks):

        all_chunks.append(
            {
                "source": doc["filename"],
                "chunk_id": idx,
                "content": chunk
            }
        )

with open("data/chunks.json", "w") as f:
    json.dump(all_chunks, f, indent=2)

print("\nSummary")
print("--------------------")
print(f"Documents: {len(documents)}")
print(f"Chunks: {len(all_chunks)}")
print("Output: data/chunks.json")
