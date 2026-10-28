from pathlib import Path

from danluu_ingestion.extractor import extract_document, extract_html
from danluu_ingestion.storage import read_document


ROOT = Path(__file__).parents[1]


def extract_local(catalog_id: str):
    document = read_document(ROOT / "data" / "raw" / f"{catalog_id}.json")
    immutable = {
        "source_url": document.source_url,
        "final_url": document.final_url,
        "redirects": document.redirects.copy(),
        "redirect_history": [hop.copy() for hop in document.redirect_history],
        "content_hash": document.content_hash,
        "editorial_approved": document.editorial_approved,
    }
    extracted = extract_document(document, ROOT)
    assert {key: getattr(extracted, key) for key in immutable} == immutable
    return extracted


def test_dan_183_keeps_technical_account_and_removes_promotions():
    text = extract_local("DAN-183").extracted_text
    for technical in [
        "Postgres connection timeouts", "memcached", "connection pool",
        "in parallel", "goroutines", "dropped packets", "anetd",
    ]:
        assert technical.lower() in text.lower()
    # Preserve uncertainty and hypotheses as stated by the source.
    assert "We weren’t quite sure what was happening" in text
    assert "we still didn’t fully and confidently understand" in text
    for contamination in [
        "See related articles", "So good, you’ll break things on purpose",
        "Ready for modern incident management? Book a call",
        "We gave cloud agents a phone to QA", "Check out the job posting",
    ]:
        assert contamination.lower() not in text.lower()


def test_dan_183_preserves_all_thirteen_technical_list_items():
    text = extract_local("DAN-183").extracted_text.lower()
    expected_items = [
        "doubling the maximum connection lifespan from 15m to 30m",
        "making connection pools static",
        "calls to update the cache happen abruptly and concurrently",
        "duration of the calls starts at around \\~1 ms or less",
        "fixed the db timeouts",
        "fixed the cache timeouts",
        "runaway query incident made things worse",
        "regardless of our mitigations, the problem persisted",
        "patching over an issue that we were triggering",
        "not a simple switch to flick",
        "dataplane v2 becomes a non-optional default",
        "remember to not focus your hypotheses too quickly",
        "limit outbound network concurrency",
    ]
    for item in expected_items:
        assert item in text, f"missing technical list item: {item}"
    assert sum(line.startswith("- ") for line in text.splitlines()) >= 13


def test_dan_001_normalizes_inline_html_without_losing_timeline_or_cause():
    document = extract_local("DAN-001")
    text = document.extracted_text
    assert "July 18th, 2018" in text
    assert "Outage timeline" in text
    assert "At 11:50" in text and "at 12:05" in text
    assert "Excessive resource reservations were a major cause" in text
    assert "<sup>" not in text and "</sup>" not in text
    assert document.redirect_history


def test_dan_009_preserves_authentication_tokens_and_code_fences():
    text = extract_local("DAN-009").extracted_text
    assert "service tokens come in two parts: a Client ID and a Client Secret" in text
    assert "empty text string" in text
    assert "```" in text


def test_dan_134_preserves_rabbitmq_failure_mechanism():
    text = extract_local("DAN-134").extracted_text
    for term in ["RabbitMQ", "acknowledgment timeout", "consumers", "queue"]:
        assert term.lower() in text.lower()


def test_dan_143_preserves_network_failure_and_recovery():
    text = extract_local("DAN-143").extracted_text
    for term in ["systemd-networkd", "Cilium", "recovery", "routing table"]:
        assert term.lower() in text.lower()


def test_residual_html_inside_fenced_code_is_not_modified():
    markup = b"""<article><p>On July 18<sup>th</sup> the incident began.</p>
    <pre><code>&lt;sup&gt;literal&lt;/sup&gt;</code></pre>
    <p>This sufficiently long technical incident account contains impact, timeline,
    mitigation, recovery, root cause, and prevention details for extraction.</p></article>"""
    _, text, _ = extract_html(markup)
    assert "18th" in text
    assert "<sup>literal</sup>" in text
