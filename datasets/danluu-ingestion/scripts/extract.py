#!/usr/bin/env python3
import argparse

from _bootstrap import ROOT
from danluu_ingestion.config import Settings
from danluu_ingestion.extractor import extract_document
from danluu_ingestion.storage import iter_documents, save_document


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract main text from collected documents")
    parser.add_argument("--catalog-id", action="append")
    parser.add_argument("--no-resume", action="store_true")
    args = parser.parse_args()
    settings = Settings(root=ROOT)
    wanted = set(args.catalog_id or [])
    for document in iter_documents(settings.data_dir / "raw"):
        if wanted and document.catalog_id not in wanted:
            continue
        destination = settings.data_dir / "extracted" / f"{document.catalog_id}.json"
        if destination.exists() and not args.no_resume:
            continue
        if document.status != "fetched":
            continue
        save_document(settings.data_dir / "extracted", extract_document(document, ROOT))
        print(f"{document.catalog_id}\t{document.status}\t{document.word_count}")


if __name__ == "__main__":
    main()

