import csv
import json

from danluu_ingestion.models import Document
from danluu_ingestion.reporting import build_report, write_reports


def test_auditable_reports(tmp_path):
    documents = [
        Document("A", "Acme", "Outage", "https://a.test", domain="a.test", content_type="text/html",
                 fetched_at="2026-01-01T00:00:00Z", http_status=200, extracted_text="text", word_count=1,
                 status="approved", editorial_approved=True),
        Document("B", "Beta", "Outage", "https://b.test", domain="b.test", status="failed",
                 fetched_at="2026-01-01T00:00:00Z", http_status=200),
    ]
    summary, rows = build_report(documents)
    json_path, csv_path = write_reports(tmp_path, summary, rows)
    assert json.loads(json_path.read_text())["rag_candidates"] == 1
    assert len(list(csv.DictReader(csv_path.open()))) == 2
    assert summary["failures"] == 1
    assert summary["fetch_successes"] == 1
