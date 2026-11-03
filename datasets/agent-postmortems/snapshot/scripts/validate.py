#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml", "jsonschema"]
# ///
"""Corpus validator — the CI gatekeeper for agent-postmortems.

Gates:
  G-SCHEMA   record matches schema/incident.schema.json
  G-TAX      classes/subclasses exist in schema/taxonomy.yaml at a known version;
             failure_classes[0] == primary_failure_class; 'other' requires tags
  G-ID       incident_id unique across corpus + filename == incident_id
  G-NEUTRAL  no blame adjectives in factual fields
  G-DRIFT    SCHEMA.md field table lists exactly the JSON Schema's top-level properties

Usage:
  uv run scripts/validate.py               # validate the whole corpus, all gates
  uv run scripts/validate.py --fixtures    # meta-test: fixtures must pass/fail as expected
"""
from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "schema" / "incident.schema.json"
TAXONOMY_PATH = REPO / "schema" / "taxonomy.yaml"
SCHEMA_MD = REPO / "SCHEMA.md"
INCIDENTS_DIR = REPO / "incidents"
FIXTURES_DIR = REPO / "tests" / "fixtures"

# Blame adjectives banned from factual fields (NFR-2). Quoted speech from sources
# belongs in `sources`/titles of sources, not in these fields.
BANNED_ADJECTIVES = [
    "grossly negligent", "idiotic", "reckless", "stupid", "incompetent",
    "careless", "clueless", "moronic", "pathetic", "shameful", "disgraceful",
    "terrible", "horrible", "awful", "braindead", "laughable",
]
FACTUAL_FIELDS = [
    "title", "summary", "trigger", "root_cause", "detection", "recovery",
    "prevention", "severity_rationale",
]


def normalize(obj):
    """YAML parses unquoted dates as date objects; the schema wants ISO strings."""
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: normalize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [normalize(v) for v in obj]
    return obj


def load_yaml(path: Path):
    return normalize(yaml.safe_load(path.read_text()))


def load_taxonomy() -> tuple[str, dict[str, set[str]]]:
    tax = load_yaml(TAXONOMY_PATH)
    classes = {c["name"]: set(c.get("subclasses") or []) for c in tax["classes"]}
    return str(tax["version"]), classes


def gate_schema(record: dict, validator: Draft202012Validator) -> list[str]:
    return [
        f"G-SCHEMA: {'/'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message}"
        for e in validator.iter_errors(record)
    ]


def gate_taxonomy(record: dict, tax_version: str, classes: dict[str, set[str]]) -> list[str]:
    errors = []
    rec_tax = record.get("taxonomy_version")
    if rec_tax is not None and rec_tax != tax_version:
        errors.append(f"G-TAX: taxonomy_version '{rec_tax}' != current '{tax_version}'")
    primary = record.get("primary_failure_class")
    chain = record.get("failure_classes") or []
    if primary and primary not in classes:
        errors.append(f"G-TAX: unknown primary_failure_class '{primary}'")
    if chain and primary and chain[0].get("class") != primary:
        errors.append(
            f"G-TAX: failure_classes[0] '{chain[0].get('class')}' must equal primary_failure_class '{primary}'"
        )
    for i, link in enumerate(chain):
        cls, sub = link.get("class"), link.get("subclass")
        if cls not in classes:
            errors.append(f"G-TAX: failure_classes[{i}]: unknown class '{cls}'")
        elif sub is not None and sub not in classes[cls]:
            errors.append(f"G-TAX: failure_classes[{i}]: '{sub}' is not a subclass of '{cls}'")
    if primary == "other" and not record.get("tags"):
        errors.append("G-TAX: primary_failure_class 'other' requires descriptive tags (REQ-T3)")
    return errors


def gate_id(record: dict, path: Path, seen: dict[str, Path]) -> list[str]:
    errors = []
    iid = record.get("incident_id", "")
    if path.stem != iid:
        errors.append(f"G-ID: filename '{path.name}' != incident_id '{iid}'")
    if iid in seen:
        errors.append(f"G-ID: duplicate incident_id '{iid}' (also in {seen[iid].name})")
    else:
        seen[iid] = path
    return errors


def gate_neutrality(record: dict) -> list[str]:
    errors = []
    texts = [(f, record.get(f) or "") for f in FACTUAL_FIELDS]
    texts += [("contributing_factors", " ".join(record.get("contributing_factors") or []))]
    for field, text in texts:
        for adj in BANNED_ADJECTIVES:
            if re.search(rf"\b{re.escape(adj)}\b", text, re.IGNORECASE):
                errors.append(f"G-NEUTRAL: banned adjective '{adj}' in '{field}'")
    return errors


def gate_drift(schema: dict) -> list[str]:
    """SCHEMA.md's Fields table must list exactly the schema's top-level properties."""
    md = SCHEMA_MD.read_text()
    fields_section = md.split("## Fields", 1)
    if len(fields_section) < 2:
        return ["G-DRIFT: SCHEMA.md has no '## Fields' section"]
    table = fields_section[1].split("## ", 1)[0]
    documented = set(re.findall(r"^\|\s*\*{0,2}`([a-z_]+)`", table, re.MULTILINE))
    actual = set(schema["properties"].keys())
    errors = []
    if missing := actual - documented:
        errors.append(f"G-DRIFT: SCHEMA.md missing fields: {sorted(missing)}")
    if extra := documented - actual:
        errors.append(f"G-DRIFT: SCHEMA.md documents unknown fields: {sorted(extra)}")
    return errors


def validate_file(path: Path, validator, tax_version, classes, seen) -> list[str]:
    try:
        record = load_yaml(path)
    except yaml.YAMLError as exc:
        return [f"G-SCHEMA: YAML parse error: {exc}"]
    if not isinstance(record, dict):
        return ["G-SCHEMA: record is not a mapping"]
    errors = gate_schema(record, validator)
    errors += gate_taxonomy(record, tax_version, classes)
    errors += gate_id(record, path, seen)
    errors += gate_neutrality(record)
    return errors


def run_corpus() -> int:
    schema = json.loads(SCHEMA_PATH.read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    tax_version, classes = load_taxonomy()
    seen: dict[str, Path] = {}
    failures = 0
    files = sorted(p for p in INCIDENTS_DIR.glob("*.yaml") if not p.name.startswith("_"))
    for path in files:
        errors = validate_file(path, validator, tax_version, classes, seen)
        if errors:
            failures += 1
            print(f"FAIL {path.relative_to(REPO)}")
            for e in errors:
                print(f"     {e}")
        else:
            print(f"ok   {path.relative_to(REPO)}")
    for e in gate_drift(schema):
        failures += 1
        print(f"FAIL {e}")
    print(f"\n{len(files)} incidents checked, {failures} failure(s); taxonomy v{tax_version}")
    return 1 if failures else 0


def run_fixtures() -> int:
    """Meta-test (TEST-PLAN section 4): every fixture must pass/fail as expected."""
    schema = json.loads(SCHEMA_PATH.read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    tax_version, classes = load_taxonomy()
    expected = load_yaml(FIXTURES_DIR / "expected.yaml")
    # Seed `seen` with corpus ids so the dupe-id fixture collides as intended.
    seen = {load_yaml(p)["incident_id"]: p
            for p in INCIDENTS_DIR.glob("*.yaml") if not p.name.startswith("_")}
    bad = 0
    for name, want in sorted(expected.items()):
        path = FIXTURES_DIR / name
        errors = validate_file(path, validator, tax_version, classes, dict(seen))
        got = "fail" if errors else "pass"
        status = "ok  " if got == want else "META-FAIL"
        if got != want:
            bad += 1
        detail = f" ({errors[0]}{'; +' + str(len(errors) - 1) + ' more' if len(errors) > 1 else ''})" if errors else ""
        print(f"{status} {name}: expected {want}, got {got}{detail}")
    print(f"\n{len(expected)} fixtures, {bad} unexpected outcome(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(run_fixtures() if "--fixtures" in sys.argv else run_corpus())
