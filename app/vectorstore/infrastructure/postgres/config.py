"""
PostgreSQL configuration for the Vector Store infrastructure.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.config.settings import get_settings


@dataclass(frozen=True)
class PostgresConfig:
    """
    Immutable PostgreSQL configuration.
    """

    host: str
    port: int
    database: str
    user: str
    password: str


def load_postgres_config() -> PostgresConfig:
    """
    Load PostgreSQL configuration from application settings.
    """

    settings = get_settings()

    return PostgresConfig(
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        database=settings.POSTGRES_DATABASE,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
    )
