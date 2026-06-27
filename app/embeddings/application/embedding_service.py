"""
Embedding application service.
"""

from __future__ import annotations

from app.config.settings import get_settings

from app.embeddings.domain.models import EmbeddingDocument

from app.embeddings.sdk.models import (
    EmbeddingRequest,
    EmbeddingResponse,
)

from .provider_factory import ProviderFactory


class EmbeddingService:
    """
    Coordinates embedding generation.
    """

    def __init__(self) -> None:

        settings = get_settings()

        self._provider = ProviderFactory().create(
            settings.EMBEDDING_PROVIDER
    )

    def embed(
        self,
        request: EmbeddingRequest,
    ) -> EmbeddingResponse:

        document = EmbeddingDocument(
            text=request.text,
        )

        result = self._provider.embed(document)

        return EmbeddingResponse(
            vector=result.vector.values,
            dimensions=len(result.vector.values),
            provider=result.metadata.provider,
            model=result.metadata.model,
        )
