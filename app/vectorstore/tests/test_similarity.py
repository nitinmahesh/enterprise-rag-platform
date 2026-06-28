from app.vectorstore.domain.services import CosineSimilarity


def test_cosine_similarity_identical_vectors() -> None:
    score = CosineSimilarity.score(
        [1.0, 2.0, 3.0],
        [1.0, 2.0, 3.0],
    )

    assert score == 1.0


def test_cosine_similarity_orthogonal_vectors() -> None:
    score = CosineSimilarity.score(
        [1.0, 0.0],
        [0.0, 1.0],
    )

    assert score == 0.0
