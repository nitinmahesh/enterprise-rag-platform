from app.vectorstore.domain import StoredEmbedding


def test_stored_embedding() -> None:
    embedding = StoredEmbedding(
        id="1",
        document_id="doc-1",
        vector=[0.1, 0.2, 0.3],
    )

    assert embedding.id == "1"
    assert embedding.document_id == "doc-1"
    assert len(embedding.vector) == 3
