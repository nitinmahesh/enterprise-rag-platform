"""
Public SDK client.

Primary entry point into the Enterprise AI Platform.
"""

from app.embeddings.application.embedding_service import (
    EmbeddingService,
)
from app.embeddings.sdk.models import (
    EmbeddingRequest,
    EmbeddingResponse,
)


class EmbeddingClient:
    """
    Public SDK client.
    """

    def __init__(self) -> None:
        self._service = EmbeddingService()

    def embed(
        self,
        request: EmbeddingRequest,
    ) -> EmbeddingResponse:
        """
        Generate embeddings.
        """

        return self._service.generate_embedding(
            request
        )
