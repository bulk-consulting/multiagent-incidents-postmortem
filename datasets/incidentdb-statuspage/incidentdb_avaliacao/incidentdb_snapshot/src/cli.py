"""
IncidentDB Command-Line Interface (2026)
Enables instant terminal search, RAG document vault export, and database validation.
"""

from __future__ import annotations
import argparse
import json
import os
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.schema import IncidentRecord
from src.validator import IncidentValidator
from src.search import IncidentSearchEngine

DEFAULT_DATA_PATH = BASE_DIR / "data" / "incident_database.jsonl"


def load_records(data_path: Path) -> list[IncidentRecord]:
    if not data_path.exists():
        print(f"[ERROR] Data file not found: {data_path}", file=sys.stderr)
        sys.exit(1)

    records: list[IncidentRecord] = []
    with open(data_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                records.append(IncidentRecord.from_dict(data))
            except Exception as e:
                print(f"[WARN] Error parsing line {line_num}: {e}", file=sys.stderr)
    return records


def cmd_search(args: argparse.Namespace) -> None:
    data_path = Path(args.data) if args.data else DEFAULT_DATA_PATH
    records = load_records(data_path)
    engine = IncidentSearchEngine(records)

    query = args.query or ""
    results = engine.search(
        query=query,
        service=args.service,
        severity=args.severity,
        category=args.category,
        limit=args.limit
    )

    print("=" * 70)
    print(f"IncidentDB Search Results for: '{query}' (Found: {len(results)})")
    print("=" * 70)

    if not results:
        print("No matching production incidents found.")
        return

    for idx, res in enumerate(results, start=1):
        rec: IncidentRecord = res["record"]
        score = res["score"]
        print(f"\n[{idx}] {rec.incident_id} | {rec.company} | {rec.date} [Score: {score}]")
        print(f"    Title   : {rec.title}")
        print(f"    Stack   : {', '.join(rec.service_stack)} | Severity: {rec.severity}")
        print(f"    Symptom : {rec.symptom_logs.splitlines()[0][:90]}...")
        print(f"    RootCause: {rec.root_cause_analysis[:110]}...")
        print("    " + "-" * 66)


def cmd_stats(args: argparse.Namespace) -> None:
    data_path = Path(args.data) if args.data else DEFAULT_DATA_PATH
    records = load_records(data_path)
    engine = IncidentSearchEngine(records)
    stats = engine.get_statistics()

    print("=" * 70)
    print("IncidentDB Production Incidents Ground-Truth Statistics (2026)")
    print("=" * 70)
    print(f"Total Indexed Incidents : {stats['total_incidents']}")
    print("\n[Severity Breakdown]")
    for sev, count in stats["severity_distribution"].items():
        print(f"  • {sev:<12} : {count:>4} incidents")

    print("\n[Top Incident Companies]")
    for comp, count in stats["top_companies"]:
        print(f"  • {comp:<18} : {count:>3} incidents")

    print("\n[Top Service Technologies]")
    for tech, count in stats["top_technologies"]:
        print(f"  • {tech:<18} : {count:>3} incidents")

    print("\n[Top Failure Categories]")
    for cat, count in stats["category_distribution"][:8]:
        print(f"  • {cat:<24} : {count:>3} incidents")
    print("=" * 70)


def cmd_export_rag(args: argparse.Namespace) -> None:
    data_path = Path(args.data) if args.data else DEFAULT_DATA_PATH
    records = load_records(data_path)
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Exporting {len(records)} incidents to RAG Markdown Vault at: {out_dir}")

    exported = 0
    for rec in records:
        # Create tech subfolder if organizing by primary technology
        primary_tech = rec.service_stack[0].lower().replace(" ", "_") if rec.service_stack else "general"
        tech_dir = out_dir / primary_tech
        tech_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{rec.incident_id}_{rec.company.lower().replace(' ', '_')}.md"
        file_path = tech_dir / filename

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rec.to_markdown())
        exported += 1

    print(f"[SUCCESS] Exported {exported} RAG Markdown runbooks.")


def cmd_validate(args: argparse.Namespace) -> None:
    data_path = Path(args.data) if args.data else DEFAULT_DATA_PATH
    records = load_records(data_path)

    print("=" * 70)
    print(f"Running 100% Census Audit on {len(records)} records in {data_path.name}")
    print("=" * 70)

    failures = 0
    for rec in records:
        valid, errors = IncidentValidator.validate_record(rec)
        if not valid:
            print(f"[FAIL] {rec.incident_id}: {'; '.join(errors)}")
            failures += 1

    if failures == 0:
        print(f"[PASS] 100% Census Passed: All {len(records)} records satisfy zero-defect criteria.")
        sys.exit(0)
    else:
        print(f"[ERROR] Found {failures} defective records.")
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="IncidentDB: Production Outages & Disaster Runbooks CLI")
    parser.add_argument("--data", default=str(DEFAULT_DATA_PATH), help="Path to incident_database.jsonl")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # search
    p_search = subparsers.add_parser("search", help="Search incidents by keyword/symptom")
    p_search.add_argument("query", nargs="?", default="", help="Search query (e.g. 'postgres lock')")
    p_search.add_argument("--service", help="Filter by technology (e.g. Redis, Kafka)")
    p_search.add_argument("--severity", help="Filter by severity (CRITICAL, HIGH)")
    p_search.add_argument("--category", help="Filter by category")
    p_search.add_argument("--limit", type=int, default=5, help="Number of results to show")
    p_search.set_defaults(func=cmd_search)

    # stats
    p_stats = subparsers.add_parser("stats", help="Show aggregated database statistics")
    p_stats.set_defaults(func=cmd_stats)

    # export-rag
    p_rag = subparsers.add_parser("export-rag", help="Export incidents to RAG Markdown directory")
    p_rag.add_argument("--output", default=str(BASE_DIR / "rag_vault"), help="Target directory")
    p_rag.set_defaults(func=cmd_export_rag)

    # validate
    p_val = subparsers.add_parser("validate", help="Run 100% census validation")
    p_val.set_defaults(func=cmd_validate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
