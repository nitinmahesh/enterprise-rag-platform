from app.vectorstore.domain.models import StoredEmbedding
from app.vectorstore.infrastructure.memory import (
    InMemoryVectorStoreRepository,
)


def test_search_returns_most_similar_embedding() -> None:

    repository = InMemoryVectorStoreRepository()

    repository.save(
        StoredEmbedding(
            id="1",
            document_id="python",
            vector=[1.0, 0.0],
        )
    )

    repository.save(
        StoredEmbedding(
            id="2",
            document_id="java",
            vector=[0.0, 1.0],
        )
    )

    repository.save(
        StoredEmbedding(
            id="3",
            document_id="mixed",
            vector=[0.7, 0.7],
        )
    )

    results = repository.search(
        query_vector=[1.0, 0.0],
        limit=2,
    )

    assert len(results) == 2
    assert results[0].document_id == "python"
