from app.vectorstore.infrastructure.postgres import (
    PostgresConnectionFactory,
)


def test_postgres_connection() -> None:
    connection = PostgresConnectionFactory.create()

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")

        version = cursor.fetchone()

    connection.close()

    assert version is not None
