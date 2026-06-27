# Enterprise RAG Platform

## Overview

Enterprise Retrieval-Augmented Generation (RAG) platform demonstrating how organizations can safely expose internal knowledge to Large Language Models.

This project focuses on enterprise-grade retrieval architecture rather than chatbot functionality.

## Business Problem

Organizations store knowledge across:

* Policies
* Procedures
* Operational Runbooks
* Technical Documentation
* Regulatory Guidelines

Traditional keyword search often fails to provide relevant answers.

This platform demonstrates semantic retrieval using embeddings and vector databases.

## Features

### Document Ingestion

* PDF Processing
* Text Extraction
* Metadata Enrichment
* Chunking

### Retrieval

* Semantic Search
* Metadata Filtering
* Hybrid Search
* Top-K Retrieval

### Vector Databases

* pgvector
* Pinecone
* Weaviate

### LLM Integration

* OpenAI
* Retrieval-Augmented Generation
* Source Attribution

## Architecture

Documents
→ Chunking
→ Embeddings
→ Vector Database
→ Retriever
→ LLM
→ Response

## Future Roadmap

* Re-ranking
* Multi-index Retrieval
* Knowledge Graph Integration
* Agentic Retrieval

## Author

Nitin Mahesh

## Progress

### Day 1

Implemented:

- Document Loader
- Banking Knowledge Dataset
- Text Chunking Pipeline
- Chunk Persistence (JSON)

Output:

```bash
python -m ingestion.ingest_pipeline
```

Result:

- Documents Loaded: 3
- Chunks Generated: 3

## Sprint 0

Project Foundation

- Package Structure
- Configuration Module
- Logging Module
- ADR

## Sprint 1 – Configuration Foundation

### Completed

- Centralized application configuration
- Typed settings using Pydantic
- Environment variable support
- Logging framework
- Configuration singleton

