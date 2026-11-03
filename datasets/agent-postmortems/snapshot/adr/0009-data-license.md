# ADR-0009 — Data license for the corpus

**Status:** Accepted

## Decision
The incident data (`incidents/`, `export/`) is licensed **CC-BY-4.0** (see `LICENSE-DATA`); code and schema stay Apache-2.0 (`LICENSE`).

## Rationale
CC-BY encourages reuse-with-attribution — attribution is exactly the citability signal the project optimizes for. Apache-2.0 is an awkward fit for data.

## Alternatives rejected
- CC0 — no attribution requirement, weaker citability signal.
- Apache-2.0 on data — awkward fit.
