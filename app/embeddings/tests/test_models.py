from app.embeddings.domain.models import (
    Embedding,
    EmbeddingInput,
    EmbeddingMetadata,
    EmbeddingResult,
)


def test_embedding_result_creation():

    embedding = Embedding(
        vector=[0.1, 0.2, 0.3]
    )

    metadata = EmbeddingMetadata(
        provider="sentence-transformers",
        model="all-MiniLM-L6-v2",
        dimensions=3,
        latency_ms=15.5,
    )

    result = EmbeddingResult(
        embedding=embedding,
        metadata=metadata,
    )

    assert result.metadata.provider == "sentence-transformers"

    assert len(result.embedding.vector) == 3
