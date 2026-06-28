"""
PostgreSQL schema management.

Responsible for creating and validating the
database schema required by the Vector Store.
"""

from __future__ import annotations

from .connection import PostgresConnectionFactory


class PostgresSchemaManager:
    """
    Creates the required PostgreSQL schema.
    """

    @staticmethod
    def initialize() -> None:

        connection = PostgresConnectionFactory.create()

        try:

            with connection.cursor() as cursor:

                cursor.execute(
                    """
                    CREATE EXTENSION IF NOT EXISTS vector;
                    """
                )

                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS embeddings (

                        id TEXT PRIMARY KEY,

                        document_id TEXT NOT NULL,

                        embedding VECTOR(384) NOT NULL,

                        metadata JSONB NOT NULL,

                        created_at TIMESTAMP NOT NULL

                    );
                    """
                )

            connection.commit()

        finally:

            connection.close()
