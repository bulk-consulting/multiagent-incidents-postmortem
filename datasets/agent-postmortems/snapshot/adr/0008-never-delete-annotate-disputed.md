# ADR-0008 — Never delete a sourced incident; annotate with `confidence: disputed`

**Status:** Accepted

## Decision
A sourced incident is never removed on complaint. If facts are contested, the record is downgraded to `confidence: disputed`, a `vendor-response` source is added where one exists, and the dispute itself becomes part of the record.

## Rationale
Neutrality and trust: the record of a dispute is data. Deletion breaks permalinks and invites censorship pressure.

## Alternatives rejected
- Delete on vendor complaint — censorship, broken permalinks, dead citations.
