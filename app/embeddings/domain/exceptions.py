"""
Embedding domain exceptions.
"""


class EmbeddingError(Exception):
    """Base exception for embedding capability."""


class InvalidEmbeddingInputError(EmbeddingError):
    """Raised when embedding input is invalid."""


class EmbeddingProviderError(EmbeddingError):
    """Raised when a provider fails."""


class EmbeddingConfigurationError(EmbeddingError):
    """Raised when provider configuration is invalid."""
