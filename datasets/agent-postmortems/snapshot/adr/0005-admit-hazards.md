# ADR-0005 — Admit hazards/near-misses, labeled `incident_type: hazard`

**Status:** Accepted

## Decision
Demonstrated PoCs and near-misses (e.g. EchoLeak, the WhatsApp-MCP tool-poisoning demo) are admitted to the corpus, labeled `incident_type: hazard`, distinct from realized `incident`s.

## Rationale
Many of the most instructive agent failures are researcher PoCs caught before wild exploitation. Recording them honestly — labeled, not dramatized — is a neutrality feature (OECD AIM precedent).

## Alternatives rejected
- Realized-incidents-only — drops the most instructive security cases.
