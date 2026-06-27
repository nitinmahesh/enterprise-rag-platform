"""
Domain exceptions for the Embedding Capability.
"""


class EmbeddingError(Exception):
    """Base embedding exception."""


class ProviderConfigurationError(EmbeddingError):
    """Provider configuration is invalid."""


class ProviderNotFoundError(EmbeddingError):
    """Requested provider is unavailable."""


class EmbeddingGenerationError(EmbeddingError):
    """Embedding generation failed."""
