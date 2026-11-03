#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml", "jsonschema"]
# ///
"""Build the machine-readable export contract from incidents/*.yaml.

Produces three artifacts, each versioned and validated
against schema/export/*.schema.json:
  export/incidents.json  full corpus (researcher dataset)          — REQ-A1
  export/scenarios.json  stampede replayable-chaos contract         — REQ-A2
  export/seeds.json      costbomb denial-of-wallet fuzz contract    — REQ-A3

Safety boundary: scenarios/seeds carry natural-language trigger/seed *shapes*
and success criteria, never runnable exploit payloads. A lint refuses to emit an
entry whose shape contains a fenced code block or obvious payload markers.

Usage:
  uv run scripts/build_exports.py            # write export/*.json
  uv run scripts/build_exports.py --check    # build in memory, validate, and fail
                                             # if committed files are stale (CI, deterministic)
"""
from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

REPO = Path(__file__).resolve().parent.parent
INCIDENTS_DIR = REPO / "incidents"
EXPORT_DIR = REPO / "export"
EXPORT_SCHEMA_DIR = REPO / "schema" / "export"
EXPORT_SCHEMA_VERSION = "1.0"

# Cost/loop classes that qualify an incident for the costbomb seed contract (TS-24).
COST_CLASSES = {"cost-blowup", "runaway-loop", "double-side-effect"}
PAYLOAD_MARKERS = re.compile(r"```|<script|rm -rf|DROP TABLE|;\s*--", re.IGNORECASE)


def normalize(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: normalize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [normalize(v) for v in obj]
    return obj


def load_incidents() -> list[dict]:
    files = sorted(p for p in INCIDENTS_DIR.glob("*.yaml") if not p.name.startswith("_"))
    return [normalize(yaml.safe_load(p.read_text())) for p in files]


def assert_no_payload(text: str, where: str) -> None:
    if PAYLOAD_MARKERS.search(text or ""):
        raise SystemExit(f"NG5 violation: possible payload in {where}: {text!r}")


def primary_source(record: dict) -> str:
    """Prefer the primary-research/vendor-disclosure source, else the first."""
    sources = record.get("sources", [])
    for pref in ("primary-research", "vendor-disclosure", "regulatory-court"):
        for s in sources:
            if s.get("type") == pref:
                return s["url"]
    return sources[0]["url"] if sources else ""


def taxonomy_version(incidents: list[dict]) -> str:
    for rec in incidents:
        if rec.get("taxonomy_version"):
            return rec["taxonomy_version"]
    return "1.0"


def build_incidents(incidents, tax_v, stamp) -> dict:
    return {
        "export_schema_version": EXPORT_SCHEMA_VERSION,
        "generated_at": stamp,
        "taxonomy_version": tax_v,
        "count": len(incidents),
        "incidents": incidents,
    }


def build_scenarios(incidents, tax_v, stamp) -> dict:
    scenarios = []
    for rec in incidents:
        me = rec.get("machine_export") or {}
        if me.get("replayable") is False:
            continue
        shape = me.get("stampede_scenario_hint")
        if not shape:
            continue  # only project incidents that supplied a shape
        assert_no_payload(shape, f"{rec['incident_id']} stampede_scenario_hint")
        system = rec.get("system") or {}
        scenarios.append({
            "incident_id": rec["incident_id"],
            "failure_class": rec["primary_failure_class"],
            "attack_vector": rec.get("attack_vector", "n-a"),
            "system_profile": {
                "framework": system.get("framework", "any"),
                "tools": system.get("tools", []),
                "autonomy_level": system.get("autonomy_level", "unknown"),
            },
            "trigger_shape": shape,
            "expected_failure": f"agent exhibits {rec['primary_failure_class']}",
            "success_criteria": "system refuses / isolates untrusted input / requires approval before the unsafe action",
            "source": primary_source(rec),
        })
    return {
        "export_schema_version": EXPORT_SCHEMA_VERSION,
        "generated_at": stamp,
        "taxonomy_version": tax_v,
        "count": len(scenarios),
        "scenarios": scenarios,
    }


def has_cost_dimension(rec: dict) -> bool:
    classes = {c.get("class") for c in rec.get("failure_classes", [])}
    classes.add(rec.get("primary_failure_class"))
    if classes & COST_CLASSES:
        return True
    cost = (rec.get("blast_radius") or {}).get("cost") or {}
    return cost.get("amount_usd") is not None


def build_seeds(incidents, tax_v, stamp) -> dict:
    seeds = []
    for rec in incidents:
        if not has_cost_dimension(rec):
            continue  # keep the costbomb contract clean (TS-24)
        me = rec.get("machine_export") or {}
        shape = me.get("costbomb_seed_hint") or me.get("stampede_scenario_hint") or rec.get("trigger", "")
        assert_no_payload(shape, f"{rec['incident_id']} costbomb_seed_hint")
        cost = (rec.get("blast_radius") or {}).get("cost") or {}
        seeds.append({
            "incident_id": rec["incident_id"],
            "failure_class": rec["primary_failure_class"],
            "cost_dimension": rec.get("summary") or rec["title"],
            "observed_cost_usd": cost.get("amount_usd"),
            "seed_shape": shape,
            "guardrail_under_test": "spend caps / margin floor / action budget / loop budget",
            "source": primary_source(rec),
        })
    return {
        "export_schema_version": EXPORT_SCHEMA_VERSION,
        "generated_at": stamp,
        "taxonomy_version": tax_v,
        "count": len(seeds),
        "seeds": seeds,
    }


def validate(name: str, doc: dict) -> None:
    schema = json.loads((EXPORT_SCHEMA_DIR / f"{name}.schema.json").read_text())
    errors = list(Draft202012Validator(schema).iter_errors(doc))
    if errors:
        for e in errors:
            print(f"  export {name}: {'/'.join(str(p) for p in e.absolute_path)}: {e.message}")
        raise SystemExit(f"export {name}.json failed its schema")


def stable_json(doc: dict) -> str:
    """Serialize with generated_at blanked so --check ignores the timestamp (TS-29)."""
    clone = dict(doc)
    clone["generated_at"] = ""
    return json.dumps(clone, indent=2, ensure_ascii=False, sort_keys=False)


def main() -> int:
    check = "--check" in sys.argv
    incidents = load_incidents()
    tax_v = taxonomy_version(incidents)
    # Deterministic timestamp: Date.now() is unavailable/undesired; use a fixed
    # placeholder for --check and the newest incident date otherwise.
    stamp = max((r["date"] for r in incidents), default="") + "T00:00:00Z"

    artifacts = {
        "incidents": build_incidents(incidents, tax_v, stamp),
        "scenarios": build_scenarios(incidents, tax_v, stamp),
        "seeds": build_seeds(incidents, tax_v, stamp),
    }

    EXPORT_DIR.mkdir(exist_ok=True)
    stale = 0
    for name, doc in artifacts.items():
        validate(name, doc)
        path = EXPORT_DIR / f"{name}.json"
        rendered = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
        if check:
            existing = path.read_text() if path.exists() else ""
            if stable_json(json.loads(existing)) != stable_json(doc) if existing else True:
                print(f"STALE {path.relative_to(REPO)} — run build_exports.py")
                stale += 1
            else:
                print(f"ok   {path.relative_to(REPO)} ({doc['count']} entries)")
        else:
            path.write_text(rendered)
            print(f"wrote {path.relative_to(REPO)} ({doc['count']} entries)")

    if check and stale:
        return 1
    print(f"\nexports: {artifacts['incidents']['count']} incidents, "
          f"{artifacts['scenarios']['count']} scenarios, {artifacts['seeds']['count']} seeds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
