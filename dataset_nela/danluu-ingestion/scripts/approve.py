#!/usr/bin/env python3
import argparse

from _bootstrap import ROOT
from danluu_ingestion.config import Settings
from danluu_ingestion.storage import read_document, save_document
from danluu_ingestion.validator import approve


def main() -> None:
    parser = argparse.ArgumentParser(description="Explicitly approve a reviewed document for RAG")
    parser.add_argument("catalog_id")
    parser.add_argument("--confirm-reviewed", action="store_true", required=True)
    args = parser.parse_args()
    settings = Settings(root=ROOT)
    path = settings.data_dir / "extracted" / f"{args.catalog_id}.json"
    if not path.exists():
        parser.error(f"extracted document not found: {args.catalog_id}")
    document = read_document(path)
    approve(document, reviewer_confirmed=args.confirm_reviewed)
    save_document(settings.data_dir / "extracted", document)
    print(f"{document.catalog_id}\tapproved")


if __name__ == "__main__":
    main()

