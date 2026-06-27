"""
Enterprise AI Platform

Embedding SDK Example.
"""

from app.embeddings import (
    EmbeddingClient,
    EmbeddingRequest,
)


def main() -> None:

    client = EmbeddingClient()

    request = EmbeddingRequest(
        text="Transfer money between accounts."
    )

    response = client.embed(request)

    print()

    print("=" * 60)
    print("Enterprise AI Platform")
    print("=" * 60)

    print(f"Provider    : {response.provider}")
    print(f"Model       : {response.model}")
    print(f"Dimensions  : {response.dimensions}")

    print()

    print("Vector")

    print(response.vector)

    print("=" * 60)


if __name__ == "__main__":
    main()
