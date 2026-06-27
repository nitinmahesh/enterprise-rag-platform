from app.embeddings.domain.models import (
    EmbeddingDocument,
    EmbeddingMetadata,
    EmbeddingResult,
    EmbeddingVector,
)


def test_embedding_result():

    document = EmbeddingDocument(
        text="Enterprise AI Platform"
    )

    vector = EmbeddingVector(
        values=[0.1, 0.2, 0.3]
    )

    metadata = EmbeddingMetadata(
        provider="sentence-transformers",
        model="all-MiniLM-L6-v2",
        latency_ms=25.5,
    )

    result = EmbeddingResult(
        document=document,
        vector=vector,
        metadata=metadata,
    )

    assert result.vector.dimensions == 3

    assert result.metadata.provider == "sentence-transformers"

    assert result.document.text == "Enterprise AI Platform"
