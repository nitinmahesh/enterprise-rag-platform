from app.embeddings import (
    EmbeddingClient,
    EmbeddingRequest,
)


def test_sdk_runtime() -> None:

    client = EmbeddingClient()

    response = client.embed(
        EmbeddingRequest(
            text="Enterprise AI Platform",
        )
    )

    assert response.provider == "sentence-transformers"

    assert response.dimensions == 384

    assert len(response.vector) == 384

    assert response.model
