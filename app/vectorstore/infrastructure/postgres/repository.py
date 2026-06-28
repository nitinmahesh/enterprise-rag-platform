"""
PostgreSQL implementation of the Vector Store repository.
"""

from __future__ import annotations

import json

from app.vectorstore.domain import (
    StoredEmbedding,
    VectorStoreRepository,
)

from .connection import PostgresConnectionFactory
from .schema import PostgresSchemaManager


class PostgresVectorStoreRepository(VectorStoreRepository):
    """
    PostgreSQL implementation of the repository contract.
    """

    def __init__(self) -> None:
        PostgresSchemaManager.initialize()

    def save(
        self,
        embedding: StoredEmbedding,
    ) -> None:

        connection = PostgresConnectionFactory.create()

        try:

            with connection.cursor() as cursor:

                cursor.execute(
                    """
                    INSERT INTO embeddings (
                        id,
                        document_id,
                        embedding,
                        metadata,
                        created_at
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (id)
                    DO UPDATE
                    SET
                        document_id = EXCLUDED.document_id,
                        embedding = EXCLUDED.embedding,
                        metadata = EXCLUDED.metadata,
                        created_at = EXCLUDED.created_at;
                    """,
                    (
                        embedding.id,
                        embedding.document_id,
                        embedding.vector,
                        json.dumps(embedding.metadata),
                        embedding.created_at,
                    ),
                )

            connection.commit()

        finally:

            connection.close()

    def find_by_id(
        self,
        embedding_id: str,
    ) -> StoredEmbedding | None:

        connection = PostgresConnectionFactory.create()

        try:

            with connection.cursor() as cursor:

                cursor.execute(
                    """
                    SELECT
                        id,
                        document_id,
                        embedding,
                        metadata,
                        created_at
                    FROM embeddings
                    WHERE id=%s;
                    """,
                    (embedding_id,),
                )

                row = cursor.fetchone()

                if row is None:
                    return None

        finally:

            connection.close()

        if row is None:
            return None

        vector = [
            float(value)
            for value in row[2].strip("[]").split(",")
        ]	

        return StoredEmbedding(
            id=row[0],
            document_id=row[1],
            vector=vector,
            metadata=row[3],
            created_at=row[4],
        )

    def delete(
        self,
        embedding_id: str,
    ) -> None:

        connection = PostgresConnectionFactory.create()

        try:

            with connection.cursor() as cursor:

                cursor.execute(
                    "DELETE FROM embeddings WHERE id=%s;",
                    (embedding_id,),
                )

            connection.commit()

        finally:

            connection.close()

    def count(self) -> int:

        connection = PostgresConnectionFactory.create()

        try:

            with connection.cursor() as cursor:

                cursor.execute(
                    "SELECT COUNT(*) FROM embeddings;"
                )

                result = cursor.fetchone()

        finally:

            connection.close()

        assert result is not None

        return int(result[0])

    def search(
        self,
        query_vector: list[float],
        limit: int = 5,
    ) -> list[StoredEmbedding]:
        """
        Return the nearest embeddings using pgvector.
        """

        connection = PostgresConnectionFactory.create()

        try:

            with connection.cursor() as cursor:

                cursor.execute(
                    """
                    SELECT
                        id,
                        document_id,
                        embedding,
                        metadata,
                        created_at
                    FROM embeddings
                    ORDER BY embedding <=> %s::vector
                    LIMIT %s;
                    """,
                    (
                        str(query_vector),
                        limit,
                    ),
                )

                rows = cursor.fetchall()

        finally:

            connection.close()

        results: list[StoredEmbedding] = []

        for row in rows:

            vector = [
                float(value)
                for value in row[2].strip("[]").split(",")
            ]

            results.append(
                StoredEmbedding(
                    id=row[0],
                    document_id=row[1],
                    vector=vector,
                    metadata=row[3],
                    created_at=row[4],
                )
            )

        return results 
