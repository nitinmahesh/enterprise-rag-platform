"""
Public SDK models.

These models define the public API exposed by the Enterprise AI Platform.

Internal implementation models must never be exposed directly to SDK consumers.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class EmbeddingRequest(BaseModel):
    """
    Public request model used by SDK consumers.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        str_strip_whitespace=True,
    )

    text: str = Field(
        ...,
        min_length=1,
        description="Text to generate embeddings for.",
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Optional application metadata.",
    )


class EmbeddingResponse(BaseModel):
    """
    Public response returned by the SDK.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    embedding: list[float]

    provider: str

    model: str

    dimensions: int

    latency_ms: float
