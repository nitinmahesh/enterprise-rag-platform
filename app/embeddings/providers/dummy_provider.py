"""
Dummy embedding provider.

Used for development, testing and SDK validation.
"""

from app.embeddings.domain.models import (
    EmbeddingDocument,
    EmbeddingMetadata,
    EmbeddingResult,
    EmbeddingVector,
)

from .base_provider import BaseEmbeddingProvider


class DummyEmbeddingProvider(BaseEmbeddingProvider):
    """
    Deterministic provider used for testing.
    """

    @property
    def provider_name(self) -> str:
        return "dummy"

    def embed(
        self,
        document: EmbeddingDocument,
    ) -> EmbeddingResult:

        text_length = len(document.text)

        vector = EmbeddingVector(
            values=[
                float(text_length),
                float(text_length) / 2,
                float(text_length) / 4,
                float(text_length) / 8,
            ]
        )

        metadata = EmbeddingMetadata(
            provider=self.provider_name,
            model="dummy-v1",
            latency_ms=0.0,
        )

        return EmbeddingResult(
            document=document,
            vector=vector,
            metadata=metadata,
        )
