# Embedding Package

## Responsibility

Convert text into dense vector representations.

## Why is this package needed?

The retrieval engine operates on vectors rather than raw text.

Embedding generation is isolated behind an abstraction so that
different providers (Sentence Transformers, OpenAI, VoyageAI)
can be swapped without affecting the rest of the application.

## Current Provider

Sentence Transformers

## Future Providers

- OpenAI
- VoyageAI
- BGE
- E5
