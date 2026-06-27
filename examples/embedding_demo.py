"""
Embedding SDK demonstration.
"""

from app.embeddings import (
    EmbeddingClient,
    EmbeddingRequest,
)


def main() -> None:

    client = EmbeddingClient()

    response = client.embed(
        EmbeddingRequest(
            text="Enterprise AI Platform",
        )
    )

    print("=" * 60)
    print("Enterprise AI Platform")
    print("=" * 60)
    print()

    print(f"Provider   : {response.provider}")
    print(f"Model      : {response.model}")
    print(f"Dimensions : {response.dimensions}")
    print()

    print("Vector")

    print(response.vector[:10])

    print("=" * 60)


if __name__ == "__main__":
    main()
