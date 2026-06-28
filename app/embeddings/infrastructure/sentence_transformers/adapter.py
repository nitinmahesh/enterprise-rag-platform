"""
Infrastructure adapter for Sentence Transformers.

This module isolates the third-party dependency from the
provider layer.
"""

from __future__ import annotations

from typing import Sequence

from sentence_transformers import SentenceTransformer


class SentenceTransformerAdapter:
    """
    Thin wrapper around SentenceTransformer.

    Responsible only for model loading and encoding.
    """

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ) -> None:
        self._model = SentenceTransformer(model_name)

    @property
    def model_name(self) -> str:
        return str(
            self._model._first_module().auto_model.config.name_or_path
        )

    def encode(
        self,
        text: str,
    ) -> list[float]:
        """
        Encode a single text into an embedding vector.
        """
        vector = self._model.encode(
            text,
            convert_to_numpy=True,
        )

        return list(vector.tolist())

    def encode_many(
        self,
        texts: Sequence[str],
    ) -> list[list[float]]:
        """
        Encode multiple texts.
        """
        vectors = self._model.encode(
            list(texts),
            convert_to_numpy=True,
        )

        return [list(v) for v in vectors.tolist()]
