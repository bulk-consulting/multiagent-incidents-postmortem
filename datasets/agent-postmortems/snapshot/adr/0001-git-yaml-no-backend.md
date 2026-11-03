# ADR-0001 — Git + YAML files + JSON Schema, no backend

**Status:** Accepted

## Decision
The corpus is a Git repository of one-YAML-file-per-incident, validated by a JSON Schema in CI. There is no database, no backend, no submissions UI.

## Rationale
Zero ops; PRs are the submission system; diffs are the audit log; permanence comes from Git history. This matches the toolkit principle of low-maintenance, reproducible assets (NFR-4, NFR-6).

## Alternatives rejected
- DB-backed app — ops burden, violates NG3.
- Airtable/spreadsheet — not machine-first, weak versioning.
