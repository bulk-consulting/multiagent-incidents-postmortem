from pathlib import Path

import pymupdf
import pytest

from danluu_ingestion.extractor import extract_document, extract_html, extract_pdf
from danluu_ingestion.models import Document
from danluu_ingestion.validator import approve, mark_duplicates, validate_document


def test_extract_article_removes_navigation():
    html = b"""<html><head><title>Database incident</title></head><body>
    <nav>Home About Contact Privacy</nav><article><h1>Outage</h1>
    <p>During the incident, customers could not connect to the database.</p>
    <h2>Timeline</h2><ul><li>10:00 UTC alert fired</li><li>10:30 UTC service restored</li></ul>
    <h2>Root cause</h2><p>A configuration error caused the outage. We added validation to prevent recurrence.</p>
    </article><footer>Terms</footer></body></html>"""
    title, text, method = extract_html(html)
    assert title == "Database incident"
    assert "Root cause" in text
    assert "Home About" not in text
    assert method in {"trafilatura", "beautifulsoup4"}


def test_extract_text_pdf():
    pdf = pymupdf.open()
    page = pdf.new_page()
    page.insert_text((72, 72), "Incident timeline and root cause")
    content = pdf.tobytes()
    pdf.close()
    _, text, method = extract_pdf(content)
    assert "Incident timeline" in text
    assert method == "pymupdf"


def test_invalid_content_and_duplicates():
    first = Document("A", "Acme", "Outage", "https://a.test", final_url="https://b.test", http_status=200,
                     content_hash="same", extracted_text="Sign in to continue", word_count=4, status="extracted")
    second = Document("B", "Acme", "Outage", "https://a.test/2", content_hash="same",
                      extracted_text="short", word_count=1, status="extracted")
    validate_document(first)
    duplicates = mark_duplicates([first, second])
    assert "login_paywall_or_block_page" in first.review_reason
    assert "cross_domain_redirect" in first.review_reason
    assert "same" in duplicates
    assert all("possible_duplicate" in item.review_reason for item in [first, second])


def test_approval_must_be_explicit():
    document = Document("A", "Acme", "Outage", "https://example.com")
    with pytest.raises(ValueError):
        approve(document, reviewer_confirmed=False)
    approve(document, reviewer_confirmed=True)
    assert document.status == "approved"
    assert document.editorial_approved is True

