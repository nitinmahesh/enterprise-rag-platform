from app.vectorstore.application import VectorStoreService
from app.vectorstore.domain import StoredEmbedding
from app.vectorstore.infrastructure.memory import (
    InMemoryVectorStoreRepository,
)


def test_vector_store_service() -> None:
    repository = InMemoryVectorStoreRepository()

    service = VectorStoreService(repository)

    embedding = StoredEmbedding(
        id="1",
        document_id="doc-1",
        vector=[1.0, 2.0],
    )

    service.store(embedding)

    assert service.count() == 1

    stored = service.retrieve("1")

    assert stored is not None
    assert stored.document_id == "doc-1"

    service.delete("1")

    assert service.count() == 0
