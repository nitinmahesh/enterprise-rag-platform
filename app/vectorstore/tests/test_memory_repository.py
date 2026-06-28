from app.vectorstore.domain import StoredEmbedding
from app.vectorstore.infrastructure.memory import (
    InMemoryVectorStoreRepository,
)


def test_memory_repository() -> None:
    repository = InMemoryVectorStoreRepository()

    embedding = StoredEmbedding(
        id="1",
        document_id="doc-1",
        vector=[0.1, 0.2, 0.3],
    )

    repository.save(embedding)

    assert repository.count() == 1

    stored = repository.find_by_id("1")

    assert stored is not None
    assert stored.id == "1"

    repository.delete("1")

    assert repository.count() == 0
