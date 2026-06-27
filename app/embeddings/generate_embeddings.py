import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vector = embeddings.embed_query(
    "What is MT103?"
)

print(f"Vector Length: {len(vector)}")
print(vector[:5])
