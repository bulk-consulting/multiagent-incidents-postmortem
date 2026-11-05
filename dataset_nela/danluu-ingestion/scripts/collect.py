#!/usr/bin/env python3
import argparse
import logging

from _bootstrap import ROOT
from danluu_ingestion.collector import Collector
from danluu_ingestion.config import Settings
from danluu_ingestion.storage import read_catalog


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect HTML/PDF post-mortems safely")
    parser.add_argument("--limit", type=int, help="maximum number of selected records")
    parser.add_argument("--catalog-id", action="append", help="select catalog ID (repeatable)")
    parser.add_argument("--no-resume", action="store_true", help="download successful records again")
    parser.add_argument("--test", action="store_true", help="show selection without network requests")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    settings = Settings(root=ROOT)
    records = read_catalog(settings.catalog_path)
    if args.catalog_id:
        wanted = set(args.catalog_id)
        records = [record for record in records if record.catalog_id in wanted]
    if args.limit is not None:
        if args.limit < 0:
            parser.error("--limit must be non-negative")
        records = records[: args.limit]
    if args.test:
        for record in records:
            print(f"{record.catalog_id}\t{record.url}")
        print(f"dry run: {len(records)} record(s)")
        return
    results = Collector(settings).collect(records, resume=not args.no_resume)
    for document in results:
        print(f"{document.catalog_id}\t{document.status}\t{document.http_status or '-'}")


if __name__ == "__main__":
    main()

