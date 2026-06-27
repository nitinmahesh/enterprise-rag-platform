"""
Public SDK models for the Embedding Capability.
"""

from pydantic import BaseModel, ConfigDict


class EmbeddingRequest(BaseModel):
    """
    Public request model for embedding generation.
    """

    model_config = ConfigDict(frozen=True)

    text: str


class EmbeddingResponse(BaseModel):
    """
    Public response model exposed by the SDK.
    """

    model_config = ConfigDict(frozen=True)

    vector: list[float]

    dimensions: int

    provider: str

    model: str
