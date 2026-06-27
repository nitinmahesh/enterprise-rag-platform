"""
Public SDK client.

This is the primary entry point for consumers of the
Enterprise AI Platform.
"""

from .sdk.models import EmbeddingRequest
from .sdk.models import EmbeddingResponse


class EmbeddingClient:
    """
    Public SDK client.

    Provider integration will be added in a later Engineering
    Delivery Package.
    """

    def embed(
        self,
        request: EmbeddingRequest,
    ) -> EmbeddingResponse:
        """
        Generate embeddings.

        Implementation arrives in EDP-003.
        """

        raise NotImplementedError(
            "Embedding provider has not yet been connected."
        )
