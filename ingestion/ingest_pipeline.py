from document_loader import load_documents
from chunker import chunk_text

documents = load_documents()

all_chunks = []

for doc in documents:

    chunks = chunk_text(doc["content"])

    for idx, chunk in enumerate(chunks):

        all_chunks.append(
            {
                "source": doc["filename"],
                "chunk_id": idx,
                "content": chunk
            }
        )

print(f"Generated {len(all_chunks)} chunks")
