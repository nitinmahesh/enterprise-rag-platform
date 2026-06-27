from app.embeddings import (
    EmbeddingClient,
    EmbeddingRequest,
)


def test_sdk_runtime():

    client = EmbeddingClient()

    request = EmbeddingRequest(
        text="Enterprise AI Platform"
    )

    response = client.embed(request)

    assert response.provider == "dummy"

    assert response.dimensions == 4

    assert len(response.vector) == 4
