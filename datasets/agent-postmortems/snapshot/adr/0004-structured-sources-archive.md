# ADR-0004 — Structured source objects + required/auto archive_url

**Status:** Accepted

## Decision
`sources` are structured objects (`url`, `title`, `publisher`, `type`, `date_accessed`, `archive_url`), not bare strings. Missing `archive_url` values are backfilled with Wayback snapshots by CI on merge (REQ-C5).

## Rationale
Citability and permanence are the moat; bare links rot. CVE reference objects are the precedent. Source `type` (including `vendor-response`) also encodes the right-of-reply neutrality mechanism.

## Alternatives rejected
- Bare URI strings (v0) — brittle, unarchivable, uncitable.
