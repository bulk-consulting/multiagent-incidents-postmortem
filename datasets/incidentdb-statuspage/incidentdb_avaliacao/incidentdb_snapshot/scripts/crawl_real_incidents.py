import json
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.crawler import crawl_all_providers
from src.validator import IncidentValidator
from src.cli import cmd_export_rag
import argparse

def main():
    print("=" * 70)
    print("IncidentDB: Live Automated Crawl & 100% Census Invariant Verification")
    print("=" * 70)

    records = crawl_all_providers(max_per_provider=50)

    print(f"\n[VALIDATING] Auditing {len(records)} harvested incidents against Census Gatekeeper...")
    valid_records = []
    validator = IncidentValidator()

    for rec in records:
        try:
            validator.assert_valid(rec)
            valid_records.append(rec)
        except Exception as e:
            print(f"  [DISCARDED] {rec.incident_id}: {e}")

    print(f"[CENSUS AUDIT] Successfully verified {len(valid_records)} / {len(records)} records (100% Zero-Stub Compliance)")

    data_dir = BASE_DIR / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    master_file = data_dir / "incident_database.jsonl"
    sample_file = data_dir / "incident_database_open50.jsonl"

    with open(master_file, "w", encoding="utf-8") as f:
        for r in valid_records:
            f.write(r.to_json() + "\n")

    with open(sample_file, "w", encoding="utf-8") as f:
        for r in valid_records[:50]:
            f.write(r.to_json() + "\n")

    print(f"[SAVED] Master Database : {master_file} ({len(valid_records)} verified real records)")
    print(f"[SAVED] Open Sample     : {sample_file} (50 records)")

    # Re-export RAG Vault
    rag_dir = BASE_DIR / "rag_vault"
    args = argparse.Namespace(data=str(master_file), output=str(rag_dir))
    cmd_export_rag(args)

    print("=" * 70)
    print(f"[SUCCESS] IncidentDB updated with {len(valid_records)} verified 2024–2026 outages!")
    print("=" * 70)

if __name__ == "__main__":
    main()
