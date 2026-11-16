#!/usr/bin/env python3
import argparse
from pathlib import Path

from _bootstrap import ROOT
from danluu_ingestion.reviews import validate_editorial_reviews


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the editorial review CSV")
    parser.add_argument(
        "--path", type=Path, default=ROOT / "data" / "reviews" / "editorial_reviews.csv"
    )
    args = parser.parse_args()
    rows = validate_editorial_reviews(args.path)
    print(f"valid editorial review register: {len(rows)} record(s)")


if __name__ == "__main__":
    main()
