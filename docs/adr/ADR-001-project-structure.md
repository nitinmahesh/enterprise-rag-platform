# ADR-001

## Status

Accepted

## Decision

Use package-based architecture.

## Context

The application will continue growing.

Keeping Python modules in the project root
does not scale.

## Consequences

Cleaner imports

Better testing

Supports FastAPIWe adopted a package-based architecture using an app/ root to improve modularity, testing, and long-term maintainability as the project evolves.
