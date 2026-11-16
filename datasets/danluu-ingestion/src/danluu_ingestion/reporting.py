from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

from .models import Document
from .validator import mark_duplicates


def build_report(documents: list[Document]) -> tuple[dict, list[dict]]:
    duplicates = mark_duplicates(documents)
    status = Counter(str(document.status) for document in documents)
    domains = Counter(document.domain or "unknown" for document in documents)
    content_types = Counter(document.content_type or "unknown" for document in documents)
    summary = {
        "total_processed": len(documents),
        "fetch_successes": sum(
            1 for d in documents
            if str(d.status) in {"fetched", "extracted", "needs_review", "approved"}
        ),
        "failures": status["failed"],
        "extractions": sum(1 for d in documents if d.extracted_text is not None),
        "needs_review": status["needs_review"],
        "rag_candidates": sum(1 for d in documents if d.status == "approved" and d.editorial_approved),
        "by_domain": dict(sorted(domains.items())),
        "by_content_type": dict(sorted(content_types.items())),
        "possible_duplicates": duplicates,
    }
    rows = []
    duplicate_ids = {item for ids in duplicates.values() for item in ids}
    for document in documents:
        rows.append({
            "catalog_id": document.catalog_id,
            "company": document.company,
            "domain": document.domain,
            "content_type": document.content_type,
            "http_status": document.http_status,
            "status": document.status,
            "word_count": document.word_count,
            "needs_review": bool(document.review_reason),
            "review_reason": "|".join(document.review_reason),
            "possible_duplicate": document.catalog_id in duplicate_ids,
            "rag_candidate": document.status == "approved" and document.editorial_approved,
        })
    return summary, rows


def write_reports(directory: Path, summary: dict, rows: list[dict]) -> tuple[Path, Path]:
    directory.mkdir(parents=True, exist_ok=True)
    json_path = directory / "summary.json"
    csv_path = directory / "documents.csv"
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = list(rows[0]) if rows else ["catalog_id", "status"]
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return json_path, csv_path

