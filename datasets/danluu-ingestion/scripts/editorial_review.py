#!/usr/bin/env python3
import argparse

from _bootstrap import ROOT
from danluu_ingestion.reviews import eligible_for_rag, record_editorial_decision


REGISTER = ROOT / "data" / "reviews" / "editorial_reviews.csv"


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage explicit human editorial decisions")
    subparsers = parser.add_subparsers(dest="command", required=True)

    decide = subparsers.add_parser("decide", help="record an approved or rejected decision")
    decide.add_argument("--catalog-id", required=True)
    decide.add_argument("--decision", required=True, choices=("approved", "rejected"))
    decide.add_argument("--reviewed-by", required=True)
    decide.add_argument("--reviewed-at", required=True, help="ISO-8601 timestamp in UTC")
    decide.add_argument(
        "--revise-existing", action="store_true",
        help="explicitly replace an existing non-pending decision",
    )

    subparsers.add_parser("eligible", help="list documents currently eligible for RAG")
    args = parser.parse_args()

    try:
        if args.command == "decide":
            backup = record_editorial_decision(
                REGISTER,
                catalog_id=args.catalog_id,
                editorial_decision=args.decision,
                reviewed_by=args.reviewed_by,
                reviewed_at=args.reviewed_at,
                revise_existing=args.revise_existing,
            )
            print(f"recorded {args.decision} for {args.catalog_id}")
            print(f"previous register preserved at {backup.relative_to(ROOT)}")
        else:
            rows = eligible_for_rag(REGISTER)
            for row in rows:
                print(f"{row['catalog_id']}\t{row['company']}\t{row['reviewed_by']}\t{row['reviewed_at']}")
            print(f"eligible for RAG: {len(rows)} document(s)")
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
