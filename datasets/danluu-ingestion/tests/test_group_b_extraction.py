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


def test_dan_234_keeps_billing_postmortem_and_removes_external_sections():
    text = extract_local("DAN-234").extracted_text
    required = [
        "1:35 AM PDT / 8:35 UTC",
        "request full synchronization with the master",
        "boot as a slave of itself",
        "read-only mode",
        "incorrect charges and suspensions",
        "Redis restarts on redis-master are disabled",
        "validate against our double-bookkeeping databases in real-time",
    ]
    for item in required:
        assert item.lower() in text.lower()
    assert sum(line.startswith(("- ", "1. ", "2. ", "3. ", "4. ")) for line in text.splitlines()) >= 17
    for contamination in [
        "Related Posts", "Related Resources", "From APIs to SDKs to sample apps",
        "Twilio's developer community hub",
    ]:
        assert contamination.lower() not in text.lower()


def test_dan_026_keeps_dns_postmortem_and_six_prevention_items():
    text = extract_local("DAN-026").extracted_text
    required = [
        "bug in our Puppet manifests",
        "internal provisioning system",
        "incorrectly returning `NXDOMAIN`",
        "failing fileservers",
        "What we’re doing about it",
        "Linux `cgroups`",
    ]
    for item in required:
        assert item.lower() in text.lower()
    numbered = [line for line in text.splitlines() if line.startswith(tuple(f"{n}. " for n in range(1, 7)))]
    assert len(numbered) == 6
    assert "Written by" not in text
    assert "Related posts" not in text
    assert "AI, agents, voice, and physical controls" not in text
