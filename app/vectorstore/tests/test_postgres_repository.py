from app.vectorstore.domain import StoredEmbedding
from app.vectorstore.infrastructure.postgres import (
    PostgresVectorStoreRepository,
)


def test_postgres_repository() -> None:

    repository = PostgresVectorStoreRepository()

    embedding = StoredEmbedding(
        id="postgres-test",
        document_id="doc-1",
        vector=[0.1] * 384,
    )

    repository.save(embedding)

    stored = repository.find_by_id("postgres-test")

    assert stored is not None

    assert stored.document_id == "doc-1"

    repository.delete("postgres-test")

    assert repository.find_by_id("postgres-test") is None
