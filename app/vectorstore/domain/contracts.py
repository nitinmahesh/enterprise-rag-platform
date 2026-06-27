"""
Repository contract for vector storage.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from .models import StoredEmbedding


class VectorStoreRepository(ABC):
    """
    Contract implemented by every vector store backend.
    """

    @abstractmethod
    def save(
        self,
        embedding: StoredEmbedding,
    ) -> None:
        """
        Persist an embedding.
        """

    @abstractmethod
    def find_by_id(
        self,
        embedding_id: str,
    ) -> StoredEmbedding | None:
        """
        Retrieve an embedding by identifier.
        """

    @abstractmethod
    def delete(
        self,
        embedding_id: str,
    ) -> None:
        """
        Delete an embedding.
        """

    @abstractmethod
    def count(self) -> int:
        """
        Return the number of stored embeddings.
        """
