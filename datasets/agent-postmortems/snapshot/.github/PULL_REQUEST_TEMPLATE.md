## What

<!-- One or two sentences: what does this PR add or change? -->

## Incident checklist (delete this section for non-incident PRs)

**Sourcing (the one rule)**
- [ ] Every claim in the record is supported by at least one **public, linkable source** — no rumors, no speculation, no private accounts.
- [ ] Each source has `url`, `type`, `publisher`, and `date_accessed`; the strongest available source type is used (primary research / vendor disclosure / court record > news).
- [ ] All source URLs are live (CI checks this; paywalled links warn but should be verified manually).

**Neutrality**
- [ ] Fields are factual — systems are named without editorializing; no blame adjectives; root cause is systemic, not personal (blameless).
- [ ] `incident_type` is honest: a researcher PoC or near-miss is labeled `hazard`, not `incident`.
- [ ] `confidence` reflects sourcing (single source = `reported`; independent sources = `corroborated`; first-party/vendor/court = `confirmed`).
- [ ] No individual is identified beyond what public sources already published.

**Mechanics**
- [ ] Filename equals `incident_id` (`YYYY-kebab-slug`), and the id does not already exist.
- [ ] `failure_classes` is the causal chain, first entry equals `primary_failure_class`, subclasses come from `schema/taxonomy.yaml`.
- [ ] `uv run scripts/validate.py` passes locally.
