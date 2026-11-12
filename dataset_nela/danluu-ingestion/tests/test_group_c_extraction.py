from pathlib import Path

from danluu_ingestion.extractor import extract_document
from danluu_ingestion.storage import read_document
from danluu_ingestion.validator import validate_document


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


def test_dan_137_is_complete_and_block_alert_is_false_positive():
    document = validate_document(extract_local("DAN-137"))
    text = document.extracted_text
    assert "login_paywall_or_block_page" not in document.review_reason
    for section in [
        "### The events of July 2", "### WAF Threats", "### What’s happened since last Tuesday",
        "### Appendix: About Regular Expression Backtracking", "This algorithm is linear in the size of its input",
    ]:
        assert section in text
    assert "Related Posts" not in text


def test_dan_118_preserves_pir_lists_recovery_and_figure_limitations():
    document = validate_document(extract_local("DAN-118"))
    text = document.extracted_text
    assert "login_paywall_or_block_page" not in document.review_reason
    for section in [
        "## Executive summary", "### Timeline of the incident", "### High-level overview of recovery workstreams",
        "## Incident communications", "## How will we improve?", "## Closing remarks",
    ]:
        assert section in text
    assert text.count("Figure ") >= 8
    assert sum(line.lstrip().startswith(("- ", "1. ", "2. ", "3. ", "4. ")) for line in text.splitlines()) >= 25
    assert "Subscribe to continue" not in text


def test_dan_086_normalizes_superscript_dates_without_losing_details():
    text = extract_local("DAN-086").extracted_text
    assert "<sup>" not in text and "</sup>" not in text
    assert "February 28th" in text
    assert "February 29th" in text
    assert "29th" in text
    assert "certificate" in text and "Guest Agent" in text


def test_dan_230_converts_mail_pre_and_separates_signature_metadata():
    text = extract_local("DAN-230").extracted_text
    assert not text.startswith("```")
    for section in ["## Timeline of events (times in UTC)", "## Lessons learned", "## Final words", "## Footnotes"]:
        assert section in text
    assert "2016-07-24 10:15:19" in text and "2016-07-24 11:40:59" in text
    assert r"\[1\] It is not yet clear" in text and r"\[2\] Internal monitoring" in text
    assert "## Message signature" in text
    assert "## OpenPGP signature metadata" in text
    assert text.index("## Message signature") > text.index("## Footnotes")


def test_dan_050_preserves_html_defined_five_whys_relationships():
    text = extract_local("DAN-050").extracted_text
    section = text[text.index("## Root cause identification: The Five Whys"):text.index("## Root causes")]
    expected_pairs = [
        ("Why were the redirect URLs broken?", "There was a bug introduced in pull request #6834"),
        ("Why was there a bug introduced in this pull request?", "The pull request introduced tests"),
        ("Why was the potential impact misjudged?", "The developer forgot to think"),
        ("Why did the bug make it into production?", "The crate download endpoint was not tested"),
        ("Why was the crate download not tested?", "The test plan for the staging environment"),
    ]
    for question, answer in expected_pairs:
        assert question in section and answer in section
        assert section.index(question) < section.index(answer)
    assert section.count("**Why") == 13
    assert "the\ncrates.io team" not in section
    for line in section.splitlines():
        if line.startswith("**Why"):
            raise AssertionError(f"Five Whys question lost its list hierarchy: {line}")
