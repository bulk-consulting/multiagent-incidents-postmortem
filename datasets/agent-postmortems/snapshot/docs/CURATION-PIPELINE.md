# CURATION-PIPELINE — automated weekly incident discovery

*How new incidents get found, drafted, and reviewed — without compromising the sourcing
rigor and neutrality the corpus depends on.*

## The principle: automate the toil, keep the human gate

Unreviewed auto-publishing would undermine the corpus's credibility, which rests entirely
on sourcing rigor and neutrality. This pipeline keeps that credibility intact: it
automates **discovery, de-duplication, drafting, and validation**, but **nothing is
added to the corpus without a human approving a pull request**. The weekly job prepares
work; a maintainer decides what becomes an incident.

## The parts

```
  discover_incidents.py ──┐  DISCOVERY  weekly-discovery.yml  (Mondays, no secrets)
  (research feeds, lab     │    find + dedup ──> "Candidate incidents" issue
   disclosures, arXiv,     │
   Google News, NVD CVE    │  AUTO-DRAFT  weekly-autocurate.yml  (opt-in: ANTHROPIC_API_KEY)
   + GitHub advisories)    │    find + dedup ──> Claude drafts v1 YAML ──> validate ──> PR
                           │
  coverage_gaps.py ────────┘  COMPLETENESS CRITIC  weekly-coverage.yml  (Wednesdays, no secrets)
  (curated external lists)     diff corpus vs external lists ──> "Coverage gaps" issue
                                                        │
                                       human reviews the issue / PR ──> merges
                                       (CI gates already green; editorial review is still required)
```

### Discovery digest (always on)

`.github/workflows/discover.yml` runs `scripts/discover_incidents.py` every Monday. The
script:

- harvests candidates from public, keyless sources configured in
  `scripts/discovery_sources.yaml`: primary security-research feeds (Embrace The Red,
  Simon Willison, Brave, PortSwigger, Trail of Bits), first-party lab/vendor disclosures
  (OpenAI, Hugging Face, Google Security, Microsoft Security), the AI Incident Database,
  the arXiv API, Google News RSS queries, the **NVD CVE keyword API**, and the **GitHub
  global Security Advisory database** — because many agent incidents are CVEs first;
- **de-dupes** against the corpus by cited URL, by CVE id (against records' `cve:` field),
  and by fuzzy title overlap (conservative — a possible duplicate is shown, not hidden);
- **scores relevance** by agent-failure keyword matches, boosting curated primary sources
  and CVEs over general news, and ranks accordingly;
- posts the result as a checklist in a single reused GitHub issue labeled `candidates`.

This layer needs no secrets — it uses the default `GITHUB_TOKEN`. A maintainer picks a
candidate, drafts it from `incidents/_TEMPLATE.yaml`, and opens a PR.

Run it by hand anytime:

```bash
uv run scripts/discover_incidents.py                 # ranked summary
uv run scripts/discover_incidents.py --markdown       # issue-ready checklist
uv run scripts/discover_incidents.py --json out.json  # machine-readable
```

### Auto-draft PRs (opt-in)

`.github/workflows/autocurate.yml` goes one step further: it runs Claude Code headless
(instructions in `.github/curation-prompt.md`, standard in
`.claude/agents/incident-curator.md`) to research each new candidate, draft a full v1
record, validate it, and open a review PR labeled `needs-review`. It **never merges**.

It is dormant until you enable it:

1. Create an Anthropic API key.
2. Add it as a repository secret named `ANTHROPIC_API_KEY`
   (`Settings → Secrets and variables → Actions → New repository secret`).

Without the secret, the `guard` job logs a notice and skips — discovery keeps working.
With it, the job drafts at most 5 incidents per run (quality over volume) and every draft
still passes the full CI gate suite before the PR opens. Automated validation is not
editorial review: a human verifies sources, tone, and incident-vs-hazard labels before
merging, per the PR checklist.

### Completeness critic (always on)

`.github/workflows/coverage.yml` runs `scripts/coverage_gaps.py` every Wednesday. Where
discovery pushes *new* candidates from feeds, the critic pulls a curated, agent-specific
external list (the [awesome-ai-agent-attacks](https://github.com/webpro255/awesome-ai-agent-attacks)
index) and reports agent incidents it has that our corpus does **not** — the "what did we
miss?" review, systematized. It diffs by CVE id and by title overlap, ranks the gaps
newest-first, and files them as a `coverage`-labelled issue. (AIID is deliberately *not*
used here — it is a broad "AI harms" database that floods the critic with non-agent noise;
we cross-reference it per-incident via `external_ids` instead.)

## Tuning the pipeline

Edit `scripts/discovery_sources.yaml` — no code change needed:

- `google_news_queries` — agent-action-oriented queries (the engineering lens), not generic "AI news".
- `arxiv_queries` — for hazards / demonstrated PoCs.
- `rss_feeds` — primary security-research blogs and first-party lab/vendor disclosures.
- `cve_queries` — NVD keyword searches scoped to agent/LLM/MCP.
- `github_advisories` — toggle the GitHub advisory pull.
- `relevance_keywords` — the vocabulary that scores and filters candidates.
- `coverage_sources` — the curated external lists the completeness critic diffs against.

## What the pipeline deliberately does NOT do

- It does not merge, publish, or bypass review (ADR-0008: the human gate is the point).
- It does not scrape paywalled or private content, or fabricate detail when a candidate
  cannot be sourced — an unsourceable candidate is discarded, not guessed.
- It does not emit weaponized payloads; drafts carry natural-language trigger shapes only.
