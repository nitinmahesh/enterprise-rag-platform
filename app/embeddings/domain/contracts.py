"""
Contracts for embedding providers.
"""

from abc import ABC, abstractmethod

from .models import EmbeddingDocument
from .models import EmbeddingResult


class EmbeddingProvider(ABC):
    """
    Abstract interface implemented by every provider.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Human-readable provider name."""

    @abstractmethod
    def embed(
        self,
        document: EmbeddingDocument,
    ) -> EmbeddingResult:
        """
        Generate an embedding for a document.
        """
