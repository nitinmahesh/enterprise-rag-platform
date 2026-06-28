"""
In-memory implementation of the Vector Store repository.
"""

from __future__ import annotations

from app.vectorstore.domain import (
    StoredEmbedding,
    VectorStoreRepository,
)

from app.vectorstore.domain.services import CosineSimilarity


class InMemoryVectorStoreRepository(VectorStoreRepository):
    """
    Reference implementation of the VectorStoreRepository.
    """

    def __init__(self) -> None:
        self._store: dict[str, StoredEmbedding] = {}

    def save(
        self,
        embedding: StoredEmbedding,
    ) -> None:
        self._store[embedding.id] = embedding

    def find_by_id(
        self,
        embedding_id: str,
    ) -> StoredEmbedding | None:
        return self._store.get(embedding_id)

    def delete(
        self,
        embedding_id: str,
    ) -> None:
        self._store.pop(embedding_id, None)

    def count(self) -> int:
        return len(self._store)

    def search(
        self,
        query_vector: list[float],
        limit: int = 5,
            ) -> list[StoredEmbedding]:
        """
        Return the nearest embeddings using cosine similarity.
        """

        scored = [
            (
                CosineSimilarity.score(
                    query_vector,
                    embedding.vector,
                ),
                embedding,
            )
            for embedding in self._store.values()
        ]

        scored.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [
            embedding
            for _, embedding in scored[:limit]
        ]
