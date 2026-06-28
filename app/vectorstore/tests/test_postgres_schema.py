from app.vectorstore.infrastructure.postgres import (
    PostgresConnectionFactory,
    PostgresSchemaManager,
)


def test_postgres_schema() -> None:

    PostgresSchemaManager.initialize()

    connection = PostgresConnectionFactory.create()

    try:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT EXISTS (

                    SELECT 1

                    FROM information_schema.tables

                    WHERE table_name='embeddings'

                );
                """
            )

            exists = cursor.fetchone()

    finally:

        connection.close()

    assert exists is not None

    assert exists[0] is True
