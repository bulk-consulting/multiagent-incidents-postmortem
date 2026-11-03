#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml"]
# ///
"""Migrate v0 incident records to schema v1. Idempotent: v1 files are left untouched.

Mechanical mapping from the legacy 11-field format:
  failure_class            -> primary_failure_class + failure_classes[0]
  blast_radius.cost_usd    -> blast_radius.cost.amount_usd
  blast_radius.data        -> blast_radius.data.description
  blast_radius.user_harm   -> blast_radius.user_harm.description
  sources: [uri]           -> sources: [{url, type: other}]

Editorial fields the schema now requires but v0 lacked (title, incident_type) are
stubbed with TODO markers — a human must fill them before the record validates.

Usage: uv run scripts/migrate_v0_to_v1.py [incidents/*.yaml]
"""
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent


def migrate(record: dict) -> dict | None:
    """Return the migrated record, or None if it is already v1."""
    if record.get("schema_version") == "1.0":
        return None

    out: dict = {"schema_version": "1.0", "taxonomy_version": "1.0"}
    out["incident_id"] = record["incident_id"]
    out["title"] = record.get("title") or "TODO: neutral factual one-line title"
    out["date"] = str(record["date"])
    out["incident_type"] = record.get("incident_type") or "incident"  # TODO: verify vs hazard
    out["system"] = record.get("system") or {}

    v0_class = record.get("failure_class", "other")
    out["primary_failure_class"] = v0_class
    out["failure_classes"] = [{"class": v0_class}]

    for key in ("trigger", "root_cause", "detection", "recovery", "prevention"):
        out[key] = record.get(key, "")

    br = record.get("blast_radius") or {}
    out["blast_radius"] = {
        "cost": {"amount_usd": br.get("cost_usd"), "estimated": False},
        "data": {"description": str(br.get("data") or "")},
        "user_harm": {"description": str(br.get("user_harm") or "")},
    }

    out["sources"] = [
        src if isinstance(src, dict) else {"url": src, "type": "other"}
        for src in record.get("sources", [])
    ]
    return out


def main(paths: list[str]) -> int:
    files = [Path(p) for p in paths] or sorted((REPO / "incidents").glob("2*.yaml"))
    changed = 0
    for path in files:
        record = yaml.safe_load(path.read_text())
        migrated = migrate(record)
        if migrated is None:
            print(f"skip (already v1): {path.name}")
            continue
        path.write_text(yaml.safe_dump(migrated, sort_keys=False, allow_unicode=True, width=88))
        print(f"migrated: {path.name}")
        changed += 1
    print(f"done — {changed} file(s) migrated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
