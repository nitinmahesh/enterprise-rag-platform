"""
Provider Factory.

Creates embedding providers.
"""

from app.embeddings.providers.dummy_provider import (
    DummyEmbeddingProvider,
)
from app.embeddings.providers.registry import (
    ProviderRegistry,
)


class ProviderFactory:
    """
    Factory responsible for creating providers.
    """

    def __init__(self) -> None:

        self._registry = ProviderRegistry()

        self._registry.register(
            "dummy",
            DummyEmbeddingProvider,
        )

    def create(
        self,
        provider_name: str,
    ):
        return self._registry.create(provider_name)
