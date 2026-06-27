"""
Domain models for the Vector Store capability.
"""

from __future__ import annotations

from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field


class StoredEmbedding(BaseModel):
    """
    Represents a persisted embedding.
    """

    model_config = ConfigDict(frozen=True)

    id: str

    document_id: str

    vector: list[float]

    metadata: dict[str, str] = Field(default_factory=dict)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )
