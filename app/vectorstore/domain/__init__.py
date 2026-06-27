"""
Vector Store domain.
"""

from .contracts import VectorStoreRepository
from .models import StoredEmbedding

__all__ = [
    "StoredEmbedding",
    "VectorStoreRepository",
]
