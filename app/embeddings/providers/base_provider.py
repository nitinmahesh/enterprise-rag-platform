"""
Base implementation for embedding providers.
"""

from abc import ABC

from app.embeddings.domain.contracts import EmbeddingProvider


class BaseEmbeddingProvider(
    EmbeddingProvider,
    ABC,
):
    """
    Shared functionality for embedding providers.
    """

    @property
    def provider_name(self) -> str:
        """
        Default provider name.

        Providers may override this if required.
        """
        return self.__class__.__name__
