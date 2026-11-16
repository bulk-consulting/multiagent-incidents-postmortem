import csv
from pathlib import Path

import pytest

from danluu_ingestion.reviews import (
    REVIEW_FIELDS,
    eligible_for_rag,
    record_editorial_decision,
    validate_editorial_reviews,
)


PROJECT_ROOT = Path(__file__).parents[1]


def write_reviews(path, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REVIEW_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def row(catalog_id="DAN-001", decision="pending_review"):
    value = {field: "value" for field in REVIEW_FIELDS}
    value.update({
        "catalog_id": catalog_id,
        "editorial_decision": decision,
        "reviewed_by": "",
        "reviewed_at": "",
    })
    return value


def test_consolidated_editorial_register_has_all_authorized_approvals():
    rows = validate_editorial_reviews(
        PROJECT_ROOT / "data" / "reviews" / "editorial_reviews.csv"
    )
    ids = [item["catalog_id"] for item in rows]
    assert len(ids) == 20
    assert len(set(ids)) == 20
    assert ids[:5] == [
        "DAN-001", "DAN-009", "DAN-134", "DAN-143", "DAN-183"
    ]
    assert set(ids[5:]) == {
        "DAN-164", "DAN-135", "DAN-109", "DAN-169", "DAN-188",
        "DAN-066", "DAN-234", "DAN-026", "DAN-115", "DAN-218",
        "DAN-137", "DAN-118", "DAN-086", "DAN-230", "DAN-050",
    }
    approved = [item for item in rows if item["editorial_decision"] == "approved"]
    pending = [item for item in rows if item["editorial_decision"] == "pending_review"]
    assert {item["catalog_id"] for item in approved} == set(ids)
    assert not pending
    assert all(item["reviewed_by"] and item["reviewed_at"] for item in approved)


def test_duplicate_catalog_id_is_rejected(tmp_path):
    path = tmp_path / "reviews.csv"
    write_reviews(path, [row(), row()])
    with pytest.raises(ValueError, match="duplicate catalog_id"):
        validate_editorial_reviews(path)


def test_invalid_editorial_decision_is_rejected(tmp_path):
    path = tmp_path / "reviews.csv"
    write_reviews(path, [row(decision="maybe")])
    with pytest.raises(ValueError, match="invalid editorial_decision"):
        validate_editorial_reviews(path)


def test_pending_review_cannot_claim_reviewer_or_date(tmp_path):
    path = tmp_path / "reviews.csv"
    value = row()
    value["reviewed_by"] = "someone"
    write_reviews(path, [value])
    with pytest.raises(ValueError, match="must not have reviewer"):
        validate_editorial_reviews(path)


def test_valid_approval_is_atomic_and_preserves_technical_fields(tmp_path):
    path = tmp_path / "reviews.csv"
    original = row()
    write_reviews(path, [original])
    backup = record_editorial_decision(
        path, catalog_id="DAN-001", editorial_decision="approved",
        reviewed_by="editor@example.com", reviewed_at="2026-10-28T12:30:00Z",
    )
    assert backup.read_bytes() != path.read_bytes()
    approved = validate_editorial_reviews(path)[0]
    assert approved["editorial_decision"] == "approved"
    assert approved["reviewed_by"] == "editor@example.com"
    assert approved["reviewed_at"] == "2026-10-28T12:30:00Z"
    for field in REVIEW_FIELDS:
        if field not in {"editorial_decision", "reviewed_by", "reviewed_at"}:
            assert approved[field] == original[field]


def test_valid_rejection(tmp_path):
    path = tmp_path / "reviews.csv"
    write_reviews(path, [row()])
    record_editorial_decision(
        path, catalog_id="DAN-001", editorial_decision="rejected",
        reviewed_by="editor", reviewed_at="2026-10-28T12:30:00+00:00",
    )
    assert validate_editorial_reviews(path)[0]["editorial_decision"] == "rejected"
    assert eligible_for_rag(path) == []


def test_decision_requires_reviewer(tmp_path):
    path = tmp_path / "reviews.csv"
    write_reviews(path, [row()])
    with pytest.raises(ValueError, match="reviewed_by is required"):
        record_editorial_decision(
            path, catalog_id="DAN-001", editorial_decision="approved",
            reviewed_by=" ", reviewed_at="2026-10-28T12:30:00Z",
        )


@pytest.mark.parametrize("timestamp", ["not-a-date", "2026-10-28T12:30:00", "2026-10-28T09:30:00-03:00"])
def test_decision_requires_valid_utc_date(tmp_path, timestamp):
    path = tmp_path / "reviews.csv"
    write_reviews(path, [row()])
    with pytest.raises(ValueError, match="reviewed_at"):
        record_editorial_decision(
            path, catalog_id="DAN-001", editorial_decision="approved",
            reviewed_by="editor", reviewed_at=timestamp,
        )


def test_decision_rejects_unknown_id_and_invalid_decision(tmp_path):
    path = tmp_path / "reviews.csv"
    write_reviews(path, [row()])
    with pytest.raises(ValueError, match="catalog_id not found"):
        record_editorial_decision(
            path, catalog_id="DAN-999", editorial_decision="approved",
            reviewed_by="editor", reviewed_at="2026-10-28T12:30:00Z",
        )
    with pytest.raises(ValueError, match="must be approved or rejected"):
        record_editorial_decision(
            path, catalog_id="DAN-001", editorial_decision="pending_review",
            reviewed_by="editor", reviewed_at="2026-10-28T12:30:00Z",
        )


def test_existing_decision_requires_explicit_revision(tmp_path):
    path = tmp_path / "reviews.csv"
    write_reviews(path, [row()])
    common = dict(
        path=path, catalog_id="DAN-001", reviewed_by="editor",
        reviewed_at="2026-10-28T12:30:00Z",
    )
    record_editorial_decision(editorial_decision="approved", **common)
    with pytest.raises(ValueError, match="--revise-existing"):
        record_editorial_decision(editorial_decision="rejected", **common)
    record_editorial_decision(
        editorial_decision="rejected", revise_existing=True, **common
    )
    assert validate_editorial_reviews(path)[0]["editorial_decision"] == "rejected"


def test_rag_eligibility_requires_valid_human_approval(tmp_path):
    path = tmp_path / "reviews.csv"
    write_reviews(path, [row("DAN-001"), row("DAN-002"), row("DAN-003")])
    record_editorial_decision(
        path, catalog_id="DAN-001", editorial_decision="approved",
        reviewed_by="editor", reviewed_at="2026-10-28T12:30:00Z",
    )
    record_editorial_decision(
        path, catalog_id="DAN-002", editorial_decision="rejected",
        reviewed_by="editor", reviewed_at="2026-10-28T12:31:00Z",
    )
    assert [item["catalog_id"] for item in eligible_for_rag(path)] == ["DAN-001"]
