# ADR-0007 — `additionalProperties: false` + small required core

**Status:** Accepted

## Decision
The schema rejects unknown top-level fields, while keeping the required core small (15 fields) and everything else optional.

## Rationale
Corpus hygiene without raising contribution cost: typos and invented fields fail fast, but a contributor can still file a valid record from the template in minutes (REQ-S15, REQ-S16).

## Alternatives rejected
- Open objects — silent drift.
- Everything-required — kills contribution.
