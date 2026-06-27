"""
Domain models for the Embedding Capability.

These models are provider agnostic and form the
business language of the Enterprise AI Platform.
"""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True, frozen=True)
class EmbeddingDocument:
    """
    Represents a single document (or chunk) to be embedded.
    """

    text: str
    document_id: str = field(default_factory=lambda: str(uuid4()))
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True, frozen=True)
class EmbeddingVector:
    """
    Dense vector representation.
    """

    values: list[float]

    @property
    def dimensions(self) -> int:
        return len(self.values)


@dataclass(slots=True, frozen=True)
class EmbeddingMetadata:
    """
    Metadata describing embedding generation.
    """

    provider: str
    model: str
    latency_ms: float


@dataclass(slots=True, frozen=True)
class EmbeddingResult:
    """
    Final output from an embedding provider.
    """

    document: EmbeddingDocument
    vector: EmbeddingVector
    metadata: EmbeddingMetadata
