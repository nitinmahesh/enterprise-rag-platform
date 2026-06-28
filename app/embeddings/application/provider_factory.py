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
from app.embeddings.providers.sentence_transformer_provider import (
    SentenceTransformerProvider,
)
from app.embeddings.domain.contracts import EmbeddingProvider

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

        self._registry.register(
           "sentence-transformers",
           SentenceTransformerProvider,
        )

    def create(
        self,
        provider_name: str,
    ) -> EmbeddingProvider:
        return self._registry.create(provider_name)
