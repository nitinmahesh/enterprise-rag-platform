"""
Sentence Transformers embedding provider.
"""

from __future__ import annotations

from app.embeddings.domain.models import (
    EmbeddingDocument,
    EmbeddingMetadata,
    EmbeddingResult,
    EmbeddingVector,
)

from app.embeddings.infrastructure.sentence_transformers import (
    SentenceTransformerAdapter,
)

from .base_provider import BaseEmbeddingProvider


class SentenceTransformerProvider(BaseEmbeddingProvider):
    """
    Production embedding provider backed by Sentence Transformers.
    """

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ) -> None:
        self._adapter = SentenceTransformerAdapter(model_name)

    @property
    def provider_name(self) -> str:
        return "sentence-transformers"

    def embed(
        self,
        document: EmbeddingDocument,
    ) -> EmbeddingResult:

        values = self._adapter.encode(document.text)

        vector = EmbeddingVector(values=values)

        metadata = EmbeddingMetadata(
            provider=self.provider_name,
            model=self._adapter.model_name,
            latency_ms=0.0,
        )

        return EmbeddingResult(
            document=document,
            vector=vector,
            metadata=metadata,
        )
