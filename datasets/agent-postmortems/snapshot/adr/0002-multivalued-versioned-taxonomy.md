# ADR-0002 — Multi-valued, two-level taxonomy in a versioned authority file

**Status:** Accepted

## Decision
Incidents are classified as an ordered chain of `{class, subclass}` pairs (`failure_classes`) plus a `primary_failure_class`, against `schema/taxonomy.yaml` — a versioned authority file (`taxonomy_version`).

## Rationale
Real agent incidents are causal chains (VERIS action chains); a single enum loses the story. A shared, versioned file enables cairn-protocol alignment and safe evolution (REQ-S3, REQ-S4, REQ-T1–T3).

## Alternatives rejected
- Keep single `failure_class` — loses chains.
- Free-text tags only — uncomparable across the corpus.
