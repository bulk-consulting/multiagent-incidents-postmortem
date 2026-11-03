# ADR-0006 — Export contract lives here; siblings only consume

**Status:** Accepted

## Decision
The machine-readable export contract (`export/incidents.json`, `scenarios.json`, `seeds.json` + their schemas under `schema/export/`) is defined and generated in this repo. Sibling repos (stampede, costbomb) consume it; this project never edits them.

## Rationale
Single source of truth; a versioned contract (`export_schema_version`) decouples release cadence; honors AC7 ("don't modify siblings").

## Alternatives rejected
- Pushing data into sibling repos — coupling and drift.
