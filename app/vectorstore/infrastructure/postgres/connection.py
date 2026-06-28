"""
PostgreSQL connection management.
"""

from __future__ import annotations

import psycopg
from psycopg import Connection

from .config import load_postgres_config


class PostgresConnectionFactory:
    """
    Creates PostgreSQL connections.
    """

    @staticmethod
    def create() -> Connection:
        """
        Create a PostgreSQL connection.
        """

        config = load_postgres_config()

        return psycopg.connect(
            host=config.host,
            port=config.port,
            dbname=config.database,
            user=config.user,
            password=config.password,
        )
