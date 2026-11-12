from __future__ import annotations

import csv
import os
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path


REVIEW_FIELDS = (
    "catalog_id",
    "company",
    "source_url",
    "document_type",
    "technical_topics",
    "causal_status",
    "evidence_notes",
    "quality_limitations",
    "editorial_decision",
    "reviewed_by",
    "reviewed_at",
)
VALID_EDITORIAL_DECISIONS = {
    "pending_review",
    "approved",
    "rejected",
    "needs_revision",
}
HUMAN_FINAL_DECISIONS = {"approved", "rejected"}


def validate_reviewed_at_utc(value: str) -> datetime:
    """Parse an ISO-8601 review timestamp and require an explicit UTC offset."""
    candidate = value.strip()
    if not candidate:
        raise ValueError("reviewed_at is required")
    try:
        parsed = datetime.fromisoformat(candidate.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("reviewed_at must be a valid ISO-8601 UTC timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        raise ValueError("reviewed_at must be in UTC")
    return parsed


def validate_editorial_reviews(path: Path) -> list[dict[str, str]]:
    """Read and validate the independent editorial-review register."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != REVIEW_FIELDS:
            raise ValueError("editorial review CSV has an invalid schema")
        rows = list(reader)

    seen: set[str] = set()
    for line_number, row in enumerate(rows, start=2):
        catalog_id = row["catalog_id"].strip()
        if not catalog_id:
            raise ValueError(f"line {line_number}: catalog_id is required")
        if catalog_id in seen:
            raise ValueError(f"line {line_number}: duplicate catalog_id: {catalog_id}")
        seen.add(catalog_id)

        decision = row["editorial_decision"].strip()
        if decision not in VALID_EDITORIAL_DECISIONS:
            raise ValueError(f"line {line_number}: invalid editorial_decision: {decision}")
        if decision == "pending_review" and (row["reviewed_by"].strip() or row["reviewed_at"].strip()):
            raise ValueError(
                f"line {line_number}: pending_review must not have reviewer or review date"
            )
        if decision != "pending_review":
            if not row["reviewed_by"].strip():
                raise ValueError(f"line {line_number}: {decision} requires reviewed_by")
            try:
                validate_reviewed_at_utc(row["reviewed_at"])
            except ValueError as exc:
                raise ValueError(f"line {line_number}: {exc}") from exc
    return rows


def _write_reviews_atomic(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent, text=True)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=REVIEW_FIELDS)
            writer.writeheader()
            writer.writerows(rows)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def _backup_reviews(path: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    backup = path.parent / "backups" / f"{path.stem}-{stamp}{path.suffix}"
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, backup)
    return backup


def record_editorial_decision(
    path: Path,
    *,
    catalog_id: str,
    editorial_decision: str,
    reviewed_by: str,
    reviewed_at: str,
    revise_existing: bool = False,
) -> Path:
    """Record one explicit human decision and return the pre-change backup."""
    rows = validate_editorial_reviews(path)
    identifier = catalog_id.strip()
    decision = editorial_decision.strip()
    reviewer = reviewed_by.strip()
    if decision not in HUMAN_FINAL_DECISIONS:
        raise ValueError("editorial_decision must be approved or rejected")
    if not reviewer:
        raise ValueError("reviewed_by is required")
    validate_reviewed_at_utc(reviewed_at)

    matches = [row for row in rows if row["catalog_id"] == identifier]
    if not matches:
        raise ValueError(f"catalog_id not found: {identifier}")
    target = matches[0]
    if target["editorial_decision"] != "pending_review" and not revise_existing:
        raise ValueError(
            f"{identifier} already has decision {target['editorial_decision']}; "
            "use --revise-existing to replace it"
        )

    target["editorial_decision"] = decision
    target["reviewed_by"] = reviewer
    target["reviewed_at"] = reviewed_at.strip()
    backup = _backup_reviews(path)
    _write_reviews_atomic(path, rows)
    return backup


def eligible_for_rag(path: Path) -> list[dict[str, str]]:
    """Return only human-approved rows with valid review metadata."""
    rows = validate_editorial_reviews(path)
    return [row for row in rows if row["editorial_decision"] == "approved"]
