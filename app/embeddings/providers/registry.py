"""
Registry for embedding providers.
"""

from collections.abc import Callable

from app.embeddings.domain.contracts import EmbeddingProvider
from app.embeddings.domain.exceptions import (
    ProviderNotFoundError,
)


class ProviderRegistry:
    """
    Stores available embedding providers.
    """

    def __init__(self) -> None:
        self._providers: dict[
            str,
            Callable[[], EmbeddingProvider],
        ] = {}

    def register(
        self,
        name: str,
        factory: Callable[[], EmbeddingProvider],
    ) -> None:

        self._providers[name.lower()] = factory

    def create(
        self,
        name: str,
    ) -> EmbeddingProvider:

        provider = self._providers.get(name.lower())

        if provider is None:
            raise ProviderNotFoundError(
                f"Unknown provider: {name}"
            )

        return provider()

    @property
    def available_providers(
        self,
    ) -> tuple[str, ...]:

        return tuple(sorted(self._providers.keys()))
