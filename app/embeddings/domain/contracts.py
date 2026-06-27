"""
Domain contracts.

Contracts define interfaces that infrastructure
must implement.
"""

from abc import ABC, abstractmethod

from .models import (
    EmbeddingInput,
    EmbeddingResult,
)


class EmbeddingProvider(ABC):
    """
    Contract implemented by every embedding provider.
    """

    @abstractmethod
    def embed(
        self,
        embedding_input: EmbeddingInput,
    ) -> EmbeddingResult:
        """
        Generate an embedding.
        """
        raise NotImplementedError
