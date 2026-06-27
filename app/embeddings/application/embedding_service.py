"""
Embedding application service.

Responsible for orchestrating embedding generation.
"""

from app.embeddings.application.provider_factory import ProviderFactory
from app.embeddings.domain.models import (
    EmbeddingDocument,
)
from app.embeddings.sdk.models import (
    EmbeddingRequest,
    EmbeddingResponse,
)


class EmbeddingService:
    """
    Application service for embedding generation.
    """

    def __init__(self) -> None:
        self._factory = ProviderFactory()

    def generate_embedding(
        self,
        request: EmbeddingRequest,
    ) -> EmbeddingResponse:
        """
        Generate an embedding using the configured provider.
        """

        provider = self._factory.create("dummy")

        document = EmbeddingDocument(
            text=request.text,
        )

        result = provider.embed(document)

        return EmbeddingResponse(
            vector=result.vector.values,
            dimensions=result.vector.dimensions,
            provider=result.metadata.provider,
            model=result.metadata.model,
        )
