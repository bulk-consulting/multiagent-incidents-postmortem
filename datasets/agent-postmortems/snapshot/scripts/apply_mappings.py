#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml", "ruamel.yaml"]
# ///
"""Derive each incident's external-framework `mappings` from its failure_classes.

Reads the class->framework crosswalk in schema/framework-mappings.yaml and, for every
incident, unions the framework ids across its failure classes (primary + chain) and
writes the result into the record's `mappings` field. Uses ruamel.yaml round-trip so
existing formatting, block scalars, and field order are preserved — only the `mappings`
block is inserted/updated. Idempotent.

Usage:
  uv run scripts/apply_mappings.py            # backfill all incidents
  uv run scripts/apply_mappings.py --check    # fail if any record's mappings are stale
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq

REPO = Path(__file__).resolve().parent.parent
INCIDENTS_DIR = REPO / "incidents"
CROSSWALK = REPO / "schema" / "framework-mappings.yaml"
FRAMEWORKS = ("owasp_llm", "owasp_agentic", "mitre_atlas")

rt = YAML()
rt.preserve_quotes = True
rt.width = 4096  # don't rewrap long block scalars
rt.indent(mapping=2, sequence=4, offset=2)  # match the corpus's "  - item" list style


def flow(items: list[str]) -> CommentedSeq:
    seq = CommentedSeq(items)
    seq.fa.set_flow_style()
    return seq


def agentic_key(tid: str):
    return int(tid[1:])


def derive(record: dict, classes: dict) -> dict:
    """Union framework ids across an incident's primary + chained failure classes."""
    present = {record.get("primary_failure_class")}
    for fc in record.get("failure_classes", []) or []:
        present.add(fc.get("class"))
    present.discard(None)

    out: dict[str, list[str]] = {}
    for fw in FRAMEWORKS:
        ids: set[str] = set()
        for c in present:
            ids |= set((classes.get(c) or {}).get(fw, []) or [])
        if ids:
            out[fw] = sorted(ids, key=agentic_key) if fw == "owasp_agentic" else sorted(ids)
    return out


def insertion_index(keys: list[str]) -> int:
    for k in ("cwe", "cve", "external_ids"):
        if k in keys:
            return keys.index(k) + 1
    for k in ("related_incidents", "tags", "machine_export", "sources"):
        if k in keys:
            return keys.index(k)
    return len(keys)


def main() -> int:
    check = "--check" in sys.argv
    classes = yaml.safe_load(CROSSWALK.read_text())["classes"]
    stale, updated = [], 0

    for path in sorted(INCIDENTS_DIR.glob("*.yaml")):
        if path.name.startswith("_"):
            continue
        data = rt.load(path.read_text())
        want = derive(data, classes)
        have = {k: list(v) for k, v in (data.get("mappings") or {}).items()}

        if want == have:
            continue
        if check:
            stale.append(path.name)
            continue

        if "mappings" in data:
            del data["mappings"]
        if want:
            block = CommentedMap()
            for fw in FRAMEWORKS:
                if fw in want:
                    block[fw] = flow(want[fw])
            data.insert(insertion_index(list(data.keys())), "mappings", block)

        buf = path.open("w")
        rt.dump(data, buf)
        buf.close()
        updated += 1
        print(f"mapped: {path.name}")

    if check:
        if stale:
            print(f"STALE mappings ({len(stale)}): run scripts/apply_mappings.py")
            for n in stale:
                print(f"  {n}")
            return 1
        print("mappings up to date")
        return 0
    print(f"done — {updated} file(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
