from pathlib import Path

from danluu_ingestion.extractor import extract_document
from danluu_ingestion.storage import read_document


ROOT = Path(__file__).parents[1]


def extract_local(catalog_id: str):
    document = read_document(ROOT / "data" / "raw" / f"{catalog_id}.json")
    protected = {
        "source_url": document.source_url,
        "final_url": document.final_url,
        "content_hash": document.content_hash,
        "redirects": document.redirects.copy(),
        "redirect_history": [hop.copy() for hop in document.redirect_history],
        "editorial_approved": document.editorial_approved,
    }
    extracted = extract_document(document, ROOT)
    assert {key: getattr(extracted, key) for key in protected} == protected
    return extracted


def test_dan_164_preserves_backup_snapshot_and_recovery_lists():
    text = extract_local("DAN-164").extracted_text
    required_items = [
        "Every 24 hours a backup is generated",
        "Every 24 hours we generate an LVM snapshot",
        "Azure disk snapshots",
        "Replication between PostgreSQL hosts",
        "A snapshot created for our staging environment",
        "A snapshot created manually",
        "Generate a snapshot of production",
        "Copy the snapshot to staging",
        "Create a new disk using this snapshot",
        "Remove all webhooks",
        "Copy the existing staging database to production",
        "Set up a separate database using the snapshot",
        "Restore webhooks",
        "Gradually re-enable GitLab.com",
        "Automated testing of recovering PostgreSQL database backups",
        "Assign an owner for data durability",
    ]
    for item in required_items:
        assert item in text
    assert sum(line.startswith(("- ", "1. ", "2. ", "3. ", "4. ", "5. ", "6. ", "7. ", "8. ", "9. ")) for line in text.splitlines()) >= 45


def test_dan_188_preserves_autovacuum_and_prior_incident_lists():
    text = extract_local("DAN-188").extracted_text
    required_items = [
        "Using process microstate accounting",
        "Once we started prefetching data",
        "All Manta operations touch our sharded, PostgreSQL-backed metadata tier",
        "three-way interaction",
        "temporarily addressed the issue",
        "table bloat",
        "table fragmentation",
        "distorted query planner statistics",
    ]
    for item in required_items:
        assert item in text
    assert sum(line.startswith("- ") for line in text.splitlines()) == 8


def test_dan_109_removes_only_exact_duplicate_blocks():
    text = extract_local("DAN-109").extracted_text
    assert text.count("Early Sunday morning, September 20") == 1
    assert text.count("**Some DynamoDB Context**") == 1
    assert text.count("### Impact on Other Services") == 1
    assert text.count("**Simple Queue Service (SQS)**") == 1
    assert "EC2 Auto Scaling" in text
    assert "CloudWatch" in text
    assert "Console" in text


def test_dan_169_separates_final_report_from_timestamped_updates():
    text = extract_local("DAN-169").extracted_text
    assert "# Final incident report" in text
    assert "Published: 13 Jun 2025 16:45 PDT" in text
    assert "# Status updates" in text
    assert "## 12 Jun 2025 — 23:34 PDT" in text
    assert "Mini Incident Report" in text
    assert "## 12 Jun 2025 — 11:46 PDT" in text
    assert "blank fields" in text
    assert "us-central1" in text
    assert "Vertex AI Online Prediction" in text


def test_dan_135_removes_generic_status_boilerplate_but_keeps_logs_and_timeline():
    text = extract_local("DAN-135").extracted_text
    assert text.startswith("## Postmortem")
    assert text.rstrip().endswith("reliability of our application.")
    assert "Real-time health of CircleCI's own infrastructure and services" not in text
    assert "Incident Report: 2023-03-14 - Delays Starting Jobs" in text
    assert "Failed to execute iptables-restore" in text
    assert "Sync failed" in text
    assert "18:00 UTC" in text and "01:27 UTC" in text
    assert "version mismatch between kubelet and kubeproxy" in text
    assert "## Resolved" not in text
    assert "## Monitoring" not in text
    assert "We are still working to add capacity for machine jobs" not in text
