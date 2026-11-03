# The Agent Post-Mortem Standard — v1

A schema for recording AI-agent failures in a comparable, machine-validated form.

Machine-validated by [`schema/incident.schema.json`](./schema/incident.schema.json) (JSON Schema draft 2020-12) in CI. Every record carries `schema_version: "1.0"`. The failure taxonomy lives in [`schema/taxonomy.yaml`](./schema/taxonomy.yaml), rendered as [`TAXONOMY.md`](./TAXONOMY.md).

## Design

- **Machine-first, human-readable second.** The record is valid typed data before it is prose; validation is the merge gate.
- **Small required core, large optional body.** Contribution stays cheap; power fields are opt-in.
- **Sourcing and neutrality are schema properties**, not just norms: structured `sources[]`, `confidence`, `status`, `incident_type`.
- **One incident = one file** (`incidents/<incident_id>.yaml`), atomic and permalinkable. Unknown top-level fields are rejected (`additionalProperties: false`).

## Fields

Required-core fields are **bold**; everything else is optional but encouraged.

| Field | Meaning |
|-------|---------|
| **`schema_version`** | Standard version of the record — always `"1.0"` |
| `taxonomy_version` | Version of `taxonomy.yaml` used to classify (`"1.0"`) |
| **`incident_id`** | Stable, immutable slug `<year>-<kebab>`, e.g. `2025-whatsapp-mcp-tool-poisoning`; must equal the filename |
| **`title`** | Neutral, factual one-line title (8–140 chars) |
| `summary` | Neutral 1–3 sentence factual summary (≤500 chars), no editorializing |
| **`date`** | When it happened or was first publicly disclosed (`YYYY-MM-DD`) |
| `last_updated` | Date the record was last revised |
| **`incident_type`** | `incident` (realized harm) or `hazard` (demonstrated PoC / near-miss, OECD-style) |
| `status` | Report maturity: `preliminary` / `factual` / `final` (NTSB-style) |
| `confidence` | Sourcing certainty: `reported` / `corroborated` / `confirmed` / `disputed` (VERIS-style) |
| `severity` | Impact band: `critical` / `high` / `moderate` / `low` / `informational` |
| `severity_rationale` | Why that severity band |
| **`system`** | The stack: `framework`, `models[]`, `tools[]`, `vendor`, `autonomy_level` |
| **`primary_failure_class`** | The inducing taxonomy class (see `TAXONOMY.md`) |
| **`failure_classes`** | Ordered causal chain of `{class, subclass}`; first entry equals `primary_failure_class` |
| `attack_vector` | How induced: `direct-user` / `untrusted-content` / `tool-metadata` / `supply-chain` / `multimodal` / `self-induced` / `n-a` |
| `causation` | MIT-style dimensions: `entity` (human/ai/both), `intentionality`, `timing` |
| **`trigger`** | What set it off — as (near-)reproducible input/condition where sources allow |
| **`root_cause`** | The underlying cause; blameless — systemic, not personal |
| `contributing_factors` | 2–5 systemic contributing factors (SRE blameless style) |
| **`detection`** | How it was noticed |
| **`recovery`** | How it was stopped/fixed |
| **`prevention`** | What would stop a recurrence |
| **`blast_radius`** | Structured impact: `cost` ($, estimated flag), `data` (records, classification), `user_harm` (categories, counts), `scope`, `reversibility` |
| `timeline` | Ordered `{at, event}` entries |
| `external_ids` | Cross-references: `aiid`, `oecd_aim`, `aiaaic` (de-dup, not clone) |
| `cve` | Related CVE identifiers |
| `cwe` | Related CWE identifiers |
| `mappings` | External security-framework cross-references (`owasp_llm`, `owasp_agentic`, `mitre_atlas`), derived from `failure_classes` via [`schema/framework-mappings.yaml`](./schema/framework-mappings.yaml) |
| `related_incidents` | Other `incident_id`s in this corpus |
| `tags` | Free-form tags; **required in practice when `primary_failure_class: other`** |
| `submitted_by` | Contributor handle (optional) |
| **`sources`** | **≥1 required.** Structured objects: `url`, `type`, `title`, `publisher`, `date_accessed`, `archive_url`. No rumors. |
| `machine_export` | Export hints: `replayable`, `stampede_scenario_hint`, `costbomb_seed_hint` |

## The one rule

Every incident needs at least one **public, linkable source**. Report factually. Name systems without editorializing. Hazards (researcher PoCs, near-misses) are recorded but must be labeled `incident_type: hazard`. Disputed records are annotated (`confidence: disputed`), never deleted (ADR-0008).

## What changed vs. v0

v0 was 11 flat fields with a single `failure_class` enum and bare-string sources. v1 keeps all 11 (renamed/nested where noted) and adds the optional body:

- `failure_class` (single) → `primary_failure_class` + ordered `failure_classes[]` chain against a versioned two-level taxonomy.
- `sources: [uri]` → structured source objects with `type` and archival fields.
- `blast_radius` loose strings → typed `cost` / `data` / `user_harm` / `scope` / `reversibility`.
- New: `title`, `summary`, `incident_type`, `status`, `confidence`, `severity`, `causation`, `attack_vector`, `contributing_factors`, `timeline`, cross-references, `machine_export`.
- Unknown top-level fields now rejected.

Migrate old records mechanically with [`scripts/migrate_v0_to_v1.py`](./scripts/migrate_v0_to_v1.py).
