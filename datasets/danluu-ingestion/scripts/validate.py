#!/usr/bin/env python3
import argparse

from _bootstrap import ROOT
from danluu_ingestion.config import Settings
from danluu_ingestion.storage import iter_documents, read_catalog, save_document
from danluu_ingestion.validator import mark_duplicates, validate_document


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply quality heuristics to extracted documents")
    parser.add_argument("--catalog-id", action="append")
    args = parser.parse_args()
    settings = Settings(root=ROOT)
    descriptions = {record.catalog_id: record.description for record in read_catalog(settings.catalog_path)}
    wanted = set(args.catalog_id or [])
    documents = [d for d in iter_documents(settings.data_dir / "extracted") if not wanted or d.catalog_id in wanted]
    for document in documents:
        validate_document(document, descriptions.get(document.catalog_id, ""))
    mark_duplicates(documents)
    for document in documents:
        save_document(settings.data_dir / "extracted", document)
        print(f"{document.catalog_id}\t{document.status}\t{'|'.join(document.review_reason) or '-'}")


if __name__ == "__main__":
    main()

