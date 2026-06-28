from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central application configuration.

    Every configurable value in the application
    should live here.
    """

    APP_NAME: str = "Enterprise RAG Platform"

    APP_VERSION: str = "0.3.0"

    EMBEDDING_PROVIDER: str = "sentence-transformers"

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    VECTOR_DIMENSION: int = 384

    # ---------------------------------------------------------------------
    # PostgreSQL
    # ---------------------------------------------------------------------

    POSTGRES_HOST: str = "localhost"

    POSTGRES_PORT: int = 5432

    POSTGRES_DATABASE: str = "enterprise_rag"

    POSTGRES_USER: str = "nitinm"

    POSTGRES_PASSWORD: str = ""

    CHUNK_SIZE: int = 300

    CHUNK_OVERLAP: int = 50

    TOP_K_RESULTS: int = 3

    LLM_PROVIDER: str = "mlx"

    LLM_MODEL: str = "Llama-3.2-1B-Instruct"

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    """
    Singleton settings object.

    The configuration is loaded only once
    and reused throughout the application.
    """

    return Settings()

