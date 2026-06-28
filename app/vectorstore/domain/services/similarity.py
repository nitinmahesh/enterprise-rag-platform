"""
Similarity functions used by the Vector Store.
"""

from __future__ import annotations

from math import sqrt


class CosineSimilarity:
    """
    Computes cosine similarity between two vectors.
    """

    @staticmethod
    def score(
        left: list[float],
        right: list[float],
    ) -> float:

        if len(left) != len(right):
            raise ValueError(
                "Vectors must have identical dimensions."
            )

        dot = sum(a * b for a, b in zip(left, right))

        left_norm = sqrt(sum(v * v for v in left))
        right_norm = sqrt(sum(v * v for v in right))

        if left_norm == 0 or right_norm == 0:
            return 0.0

        return dot / (left_norm * right_norm)
