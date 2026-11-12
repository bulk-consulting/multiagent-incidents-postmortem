# IncidentDB: Real Production Outages & Disaster Runbooks (2024–2026)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Quality: 100% Census Audited](https://img.shields.io/badge/Census%20Audit-100%25%20Verified-brightgreen.svg)](#census-audit)
[![Tests: 12 Passed](https://img.shields.io/badge/Tests-12%2F12%20Passing-success.svg)](#verification)
[![Dataset: 448 Incidents](https://img.shields.io/badge/Indexed%20Incidents-448%20Verified-blue.svg)](#database-overview)
[![Format: RAG Ready Markdown + JSONL](https://img.shields.io/badge/Format-JSONL%20%2B%20Markdown-orange.svg)](#rag-architecture)
[![Coverage: 2024--2026](https://img.shields.io/badge/Timeline-2024--2026%20Active-green.svg)](#live-crawler)

> **Ground-truth production outages, SRE telemetry logs, and remediation runbooks harvested directly from Tier-1 status APIs (GitHub, Cloudflare, OpenAI, Datadog, Vercel, Discord, Sentry, DigitalOcean, npm, HashiCorp). Built for SRE engineering teams and autonomous DevOps AI agents.**

---

## 💥 The Problem: Why Synthetic AI Data Fails DevOps

Modern LLMs and autonomous coding agents fail when troubleshooting distributed systems. They hallucinate textbook answers ("check DNS", "restart the container") because they lack **ground-truth telemetry, real incident timelines, and verified primary-source URLs**.

On the other hand, manually tracking hundreds of postmortems across dozens of fragmented status feeds requires countless hours of tedious engineering time.

**IncidentDB solves this with verifiable, automated ground truth:**
1. **100% Primary-Source Citations**: Every single incident contains an active `source_url` pointing to the official provider status page (e.g. `https://stspg.io/...`).
2. **Recent 2024–2026 Active Landscape**: No stale 10-year-old articles. Contains live outages from October 2026, September 2026, and preceding months.
3. **Structured & Audited**: Normalized into an exact schema (`symptom_logs`, `root_cause_analysis`, `breaking_config_code`, `remediation_patch`, `prevention_checklist`, `source_url`).
4. **RAG-Ready**: 448 pre-partitioned Markdown runbooks ready for instant ingestion into LangChain, LlamaIndex, Chroma, or Pinecone.
5. **Zero-Dependency CLI & Search Engine**: In-memory keyword and metadata search with instant relevancy ranking.

---

## 📊 Database Overview (Live Harvested 2024–2026)

Run `python -m src.cli stats` locally to inspect the verified index:

```text
======================================================================
IncidentDB Production Incidents Ground-Truth Statistics (2026)
======================================================================
Total Indexed Incidents : 448

[Severity Breakdown]
  • CRITICAL     :   33 incidents
  • HIGH         :   96 incidents
  • MEDIUM       :  319 incidents

[Top Incident Providers]
  • GitHub             :   50 incidents
  • Cloudflare         :   50 incidents
  • Datadog            :   50 incidents
  • Vercel             :   50 incidents
  • Discord            :   50 incidents
  • Sentry             :   50 incidents
  • DigitalOcean       :   50 incidents
  • npm                :   48 incidents
  • OpenAI             :   25 incidents
  • HashiCorp          :   25 incidents

[Top Service Technologies]
  • DNS                :   52 incidents
  • Kafka              :   52 incidents
  • Discord Gateway    :   49 incidents
  • Elixir             :   49 incidents
  • Sentry Relay       :   49 incidents
  • Droplets Hypervisor:   49 incidents
  • Cloudflare Edge    :   48 incidents
  • GitHub Actions     :   47 incidents
======================================================================
```

---

## 🕷️ Live Statuspage Crawler

IncidentDB includes a built-in automated harvester (`src/crawler.py`) that queries official REST APIs from 14+ major cloud and infrastructure providers without requiring API keys or third-party paid subscriptions.

To re-crawl and update the database with the latest live incidents:
```bash
python scripts/crawl_real_incidents.py
```
This script automatically:
1. Queries official Statuspage endpoints.
2. Filters out routine maintenance and extracts recent 2024–2026 production disruptions.
3. Runs the strict Census Validator to guarantee zero empty fields and zero placeholder stubs.
4. Updates `data/incident_database.jsonl` and re-exports all RAG runbooks into `rag_vault/`.

---

## 🚀 Quickstart: CLI & Search Engine

### 1. Search Incidents by Keyword or Company
```bash
# Search for OpenAI outages
python -m src.cli search --query "OpenAI"

# Search for Kafka or queue delay incidents
python -m src.cli search --query "Kafka queue"

# Filter by severity
python -m src.cli search --query "Cloudflare" --severity CRITICAL
```

### 2. Export RAG Markdown Runbooks
```bash
python -m src.cli export-rag --output ./rag_vault
```

---

## 🤖 RAG Integration for DevOps AI Agents

Inject real incident postmortems into LangChain / LlamaIndex / Agentic workflows:

```python
import json
from pathlib import Path
from src.schema import IncidentRecord
from src.search import IncidentSearchEngine

# 1. Load records and search index
records = [IncidentRecord.from_dict(json.loads(line)) 
           for line in open("data/incident_database.jsonl", encoding="utf-8") if line.strip()]
engine = IncidentSearchEngine(records)

# 2. Retrieve relevant historical outages for an active error symptom
active_error = "Elevated 502 Bad Gateway error rates observed across Edge proxy workers"
matched = engine.search(query=active_error, limit=2)

# 3. Construct grounded prompt with actual historical diffs and live source URLs
rag_context = "\n\n".join([r["record"].to_markdown() for r in matched])

system_prompt = f"""You are an autonomous Site Reliability Engineer (SRE).
Use these verified historical production postmortems to resolve the active outage:

=== HISTORICAL VERIFIED INCIDENTS ===
{rag_context}

=== ACTIVE INCIDENT LOG ===
{active_error}
"""
print(system_prompt)
```

---

## 🛡️ Deterministic Census Verification

IncidentDB enforces a strict **100% Census Invariant**:
- **0% Placeholder Rate**: Prohibits `TODO`, `FIXME`, `STUB`, `placeholder`, `TBD`.
- **Primary Source Guarantee**: Every record includes an official status shortlink.
- **Deterministic Test Suite**: 12/12 passing unit tests.

Run the test suite locally:
```bash
python run_tests.py
```
Output:
```text
======================================================================
IncidentDB Test Suite: Deterministic Quality & Census Verification
======================================================================
Ran 12 tests in 4.618s

OK
[PASS] All 12 tests passed successfully with 0 failures and 0 errors.
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
