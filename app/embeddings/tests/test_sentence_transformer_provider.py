from app.embeddings.domain.models import EmbeddingDocument
from app.embeddings.providers.sentence_transformer_provider import (
    SentenceTransformerProvider,
)


def test_sentence_transformer_provider() -> None:

    provider = SentenceTransformerProvider()

    result = provider.embed(
        EmbeddingDocument(
            text="Enterprise AI Platform"
        )
    )

    assert result.metadata.provider == "sentence-transformers"

    assert len(result.vector.values) == 384

    assert result.metadata.model
