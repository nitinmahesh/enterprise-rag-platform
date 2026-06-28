"""
Application service for vector storage.
"""

from __future__ import annotations

from app.vectorstore.domain import (
    StoredEmbedding,
    VectorStoreRepository,
)


class VectorStoreService:
    """
    Coordinates vector storage operations.
    """

    def __init__(
        self,
        repository: VectorStoreRepository,
    ) -> None:
        self._repository = repository

    def store(
        self,
        embedding: StoredEmbedding,
    ) -> None:
        self._repository.save(embedding)

    def retrieve(
        self,
        embedding_id: str,
    ) -> StoredEmbedding | None:
        return self._repository.find_by_id(embedding_id)

    def delete(
        self,
        embedding_id: str,
    ) -> None:
        self._repository.delete(embedding_id)

    def count(self) -> int:
        return self._repository.count()

    def search(
        self,
        query_vector: list[float],
        limit: int = 5,
    ) -> list[StoredEmbedding]:
        """
        Search for similar embeddings.
        """

        return self._repository.search(
            query_vector,
            limit,
        )
   
