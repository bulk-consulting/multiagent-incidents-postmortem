#!/usr/bin/env python3
import argparse

from _bootstrap import ROOT
from danluu_ingestion.config import Settings
from danluu_ingestion.reporting import build_report, write_reports
from danluu_ingestion.storage import iter_documents


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate auditable CSV and JSON reports")
    parser.add_argument("--catalog-id", action="append")
    args = parser.parse_args()
    settings = Settings(root=ROOT)
    wanted = set(args.catalog_id or [])
    extracted = list(iter_documents(settings.data_dir / "extracted"))
    extracted_ids = {d.catalog_id for d in extracted}
    documents = extracted + [d for d in iter_documents(settings.data_dir / "raw") if d.catalog_id not in extracted_ids]
    if wanted:
        documents = [d for d in documents if d.catalog_id in wanted]
    summary, rows = build_report(documents)
    json_path, csv_path = write_reports(settings.data_dir / "reports", summary, rows)
    print(json_path)
    print(csv_path)


if __name__ == "__main__":
    main()
