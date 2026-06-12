import psycopg2

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

question = input(
    "Ask Question: "
)

query_embedding = embeddings.embed_query(
    question
)

conn = psycopg2.connect(
    host="localhost",
    database="ragdb",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute(
    """
    SELECT
        source,
        content
    FROM document_chunks
    ORDER BY embedding <=> %s::vector
    LIMIT 3
    """,
    (query_embedding,)
)

results = cur.fetchall()

print("\nTop Matches\n")

for result in results:

    print("-" * 50)

    print(result[0])

    print(result[1])
