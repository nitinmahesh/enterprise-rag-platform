import json
import psycopg2

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

conn = psycopg2.connect(
    host="localhost",
    database="ragdb",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

with open("data/chunks.json") as f:
    chunks = json.load(f)

for chunk in chunks:

    vector = embeddings.embed_query(
        chunk["content"]
    )

    cur.execute(
        """
        INSERT INTO document_chunks
        (
            source,
            chunk_id,
            content,
            embedding
        )
        VALUES (%s,%s,%s,%s)
        """,
        (
            chunk["source"],
            chunk["chunk_id"],
            chunk["content"],
            vector
        )
    )

conn.commit()

print(f"Loaded {len(chunks)} chunks")
