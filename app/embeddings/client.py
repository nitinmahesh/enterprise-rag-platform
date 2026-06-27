"""
Public SDK client.
"""

from __future__ import annotations

from app.embeddings.application.embedding_service import (
    EmbeddingService,
)
from app.embeddings.sdk.models import (
    EmbeddingRequest,
    EmbeddingResponse,
)


class EmbeddingClient:
    """
    Public SDK entry point.
    """

    def __init__(
        self,
        provider_name: str = "sentence-transformers",
    ) -> None:

        self._service = EmbeddingService(provider_name)

    def embed(
        self,
        request: EmbeddingRequest,
    ) -> EmbeddingResponse:

        return self._service.embed(request)
