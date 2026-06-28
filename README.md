# Enterprise RAG Platform

> **Production-quality RAG SDK built using Clean Architecture, Domain-Driven Design (DDD), and SDK-first engineering principles.**

This repository is the **core Retrieval-Augmented Generation (RAG) SDK** within a larger **Enterprise AI Platform Ecosystem**.

---

# Enterprise AI Platform Ecosystem

This project is intentionally split into multiple repositories, each representing an independently deployable and reusable SDK.

```text
Enterprise AI Platform Ecosystem

├── enterprise-rag-platform          ← RAG SDK (this repository)
├── genai-production-platform-mvp    ← Reference Enterprise Application
├── llm-observability-lab            ← Observability SDK
└── ragas-evaluation-framework       ← Evaluation SDK
```

Each repository has a single responsibility while sharing common engineering principles and architectural standards.

---

# Repository Responsibility

The **Enterprise RAG Platform** is responsible for providing reusable SDKs for Retrieval-Augmented Generation capabilities.

Current capabilities include:

- Embedding SDK
- Provider Framework
- Runtime Orchestration
- Configuration Management
- Vector Store (In Progress)

Future capabilities include:

- PostgreSQL + pgvector
- Semantic Retrieval
- Hybrid Search
- Document Ingestion
- Chunking
- Ranking
- Retrieval Pipelines

---

# Current Features

## Embedding SDK

- Public SDK
- Immutable Request / Response models
- Configuration-driven provider selection
- Runtime orchestration

---

## Provider Architecture

- Provider Pattern
- Factory Pattern
- Registry Pattern
- Infrastructure Adapter Pattern

Supported providers

- Dummy Provider
- Sentence Transformers

Planned

- OpenAI
- Azure OpenAI
- MLX

---

## Engineering Foundation

- Clean Architecture
- Domain-Driven Design
- SDK-first design
- Ruff
- MyPy
- Pytest
- Makefile validation

---

# Architecture

```text
                   Public SDK
                        │
                 EmbeddingClient
                        │
                 EmbeddingService
                        │
                 ProviderFactory
                        │
                 ProviderRegistry
          ┌─────────────┴─────────────┐
          │                           │
 DummyEmbeddingProvider   SentenceTransformerProvider
                                        │
                        SentenceTransformerAdapter
                                        │
                           sentence-transformers
```

---

# Repository Structure

```text
app/

├── config/
├── embeddings/
│   ├── application/
│   ├── domain/
│   ├── infrastructure/
│   ├── providers/
│   └── sdk/
├── ingestion/
├── retrieval/
├── services/
├── utils/
└── vectorstore/
```

---

# Technology Stack

### Language

- Python 3.13

### AI

- Sentence Transformers

### Architecture

- Clean Architecture
- Domain-Driven Design
- Provider Pattern
- Factory Pattern
- Registry Pattern

### Quality

- Pytest
- Ruff
- MyPy

---

# Roadmap

## Completed

- Repository Foundation
- SDK Foundation
- Provider Pattern
- Runtime
- Production Embedding Provider
- Configuration-driven Provider Selection

## In Progress

- Vector Store

## Planned

- PostgreSQL + pgvector
- Semantic Retrieval
- Hybrid Search
- Document Ingestion
- OpenAI Provider
- Azure OpenAI Provider
- FastAPI Integration

---

# Development

Clone the repository

```bash
git clone https://github.com/nitinmahesh/enterprise-rag-platform.git

cd enterprise-rag-platform
```

Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Run validation

```bash
make validate
```

Run the embedding example

```bash
python examples/embedding_demo.py
```

---

# Engineering Standards

Every Engineering Delivery Package (EDP) must satisfy:

- Successful compilation
- Passing unit tests
- Ruff validation
- MyPy validation
- Runtime verification

before merging into the `main` branch.

---

# Current Release

Version

**v0.3.0**

Current Sprint

**Sprint 04 – Vector Store**

---

# Author

**Nitin Mahesh**

Application Development Manager | Enterprise Architect | AI Platform Engineering

---

# License

MIT License
