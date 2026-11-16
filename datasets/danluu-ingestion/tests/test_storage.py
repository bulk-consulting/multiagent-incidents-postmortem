import csv
from pathlib import Path

import pytest

from danluu_ingestion.models import Document
from danluu_ingestion.storage import read_catalog, read_document, save_document


def test_catalog_imports_all_240_rows():
    catalog = Path(__file__).parents[1] / "data" / "catalog.csv"
    records = read_catalog(catalog)
    assert len(records) == 240
    assert len({record.catalog_id for record in records}) == 240


def test_catalog_requires_columns(tmp_path):
    path = tmp_path / "bad.csv"
    path.write_text("catalog_id,url\n1,https://example.com\n", encoding="utf-8")
    with pytest.raises(ValueError, match="missing columns"):
        read_catalog(path)


def test_document_metadata_round_trip(tmp_path):
    original = Document("DAN-001", "Acme", "Outage", "https://example.com/post", title=None)
    path = save_document(tmp_path, original)
    restored = read_document(path)
    assert restored.to_dict() == original.to_dict()
    assert restored.title is None

