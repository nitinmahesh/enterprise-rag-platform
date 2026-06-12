from pathlib import Path

DATA_DIR = Path("data")


def load_documents():
    docs = []

    for file in DATA_DIR.glob("*.txt"):
        with open(file, "r") as f:
            docs.append(
                {
                    "filename": file.name,
                    "content": f.read()
                }
            )

    return docs


if __name__ == "__main__":
    documents = load_documents()

    print(f"Loaded {len(documents)} documents")

    for doc in documents:
        print(doc["filename"])
