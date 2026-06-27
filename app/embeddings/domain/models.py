"""
Domain models for the Embedding capability.

These models are provider-agnostic and represent the
core business objects used throughout the platform.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class EmbeddingInput:
    """
    Represents text that needs to be embedded.
    """

    text: str
    document_id: str | None = None
    chunk_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True, frozen=True)
class Embedding:
    """
    Represents a dense vector.
    """

    vector: list[float]


@dataclass(slots=True, frozen=True)
class EmbeddingMetadata:
    """
    Metadata describing how an embedding was generated.
    """

    provider: str
    model: str
    dimensions: int
    latency_ms: float


@dataclass(slots=True, frozen=True)
class EmbeddingResult:
    """
    Final result returned by an embedding provider.
    """

    embedding: Embedding
    metadata: EmbeddingMetadata
