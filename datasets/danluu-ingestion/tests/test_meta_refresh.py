import json
import socket
import urllib.robotparser
from pathlib import Path

import httpcore
import httpx
import pytest

import danluu_ingestion.collector as collector_module
from danluu_ingestion.collector import Collector, PinnedNetworkBackend, UnsafeURL
from danluu_ingestion.config import Settings
from danluu_ingestion.models import CatalogRecord, Document
from danluu_ingestion.storage import save_document


HTML_HEADERS = {"content-type": "text/html; charset=utf-8"}


def config(tmp_path, **changes):
    values = dict(root=tmp_path, request_delay=0, retries=0, max_download_bytes=4096, max_redirects=5)
    values.update(changes)
    return Settings(**values)


def record(url="https://source.test/start"):
    return CatalogRecord("DAN-META", "Outage", "Acme", url, "source.test", "test", "")


def html(body):
    return httpx.Response(200, headers=HTML_HEADERS, text=body)


def collector(tmp_path, handler, monkeypatch, **settings):
    monkeypatch.setattr(collector_module, "validate_public_url", lambda url: ("93.184.216.34",))
    client = httpx.Client(transport=httpx.MockTransport(handler))
    return Collector(config(tmp_path, **settings), client, sleep=lambda _: None)


@pytest.mark.parametrize("target", [
    "https://target.test/article",
    "/article",
])
def test_valid_absolute_and_relative_meta_refresh(tmp_path, monkeypatch, target):
    seen = []
    def handler(request):
        seen.append(str(request.url))
        if len(seen) == 1:
            return html(f'<meta http-equiv="refresh" content="0;url={target}">')
        return html("<article>Final incident report</article>")
    result = collector(tmp_path, handler, monkeypatch).fetch(record(), check_robots=False)
    expected = target if target.startswith("https") else "https://source.test/article"
    assert result.status == "fetched"
    assert result.final_url == expected
    assert result.redirect_history[0]["type"] == "meta_refresh"
    assert result.redirect_history[0]["destination_url"] == expected


def test_meta_refresh_is_case_insensitive_and_tolerates_spaces(tmp_path, monkeypatch):
    def handler(request):
        if request.url.path == "/start":
            return html("<META HTTP-EQUIV=' ReFrEsH ' CONTENT=' 0 ; URL = /next '>")
        return html("<article>done</article>")
    result = collector(tmp_path, handler, monkeypatch).fetch(record(), check_robots=False)
    assert result.status == "fetched"
    assert result.final_url == "https://source.test/next"


def test_page_without_meta_refresh_is_not_redirected(tmp_path, monkeypatch):
    calls = 0
    def handler(request):
        nonlocal calls
        calls += 1
        return html("<script>location='/never-followed'</script><article>report</article>")
    result = collector(tmp_path, handler, monkeypatch).fetch(record(), check_robots=False)
    assert result.status == "fetched"
    assert result.redirect_history == []
    assert calls == 1


@pytest.mark.parametrize("markup,reason", [
    ('<meta http-equiv="refresh" content="0">', "invalid_meta_refresh"),
    ('<meta http-equiv="refresh" content="0;url=http://[broken">', "invalid_meta_refresh"),
    ('<meta http-equiv="refresh" content="0;url=/a"><meta http-equiv="refresh" content="0;url=/b">',
     "ambiguous_meta_refresh"),
])
def test_malformed_or_ambiguous_meta_refresh_needs_review(tmp_path, monkeypatch, markup, reason):
    result = collector(tmp_path, lambda request: html(markup), monkeypatch).fetch(record(), check_robots=False)
    assert result.status == "needs_review"
    assert reason in result.review_reason


@pytest.mark.parametrize("target", ["http://localhost/admin", "http://10.0.0.1/admin"])
def test_private_meta_target_is_skipped_without_request(tmp_path, monkeypatch, target):
    calls = []
    def validate(url):
        if "localhost" in url or "10.0.0.1" in url:
            raise UnsafeURL("non-public")
        return ("93.184.216.34",)
    monkeypatch.setattr(collector_module, "validate_public_url", validate)
    def handler(request):
        calls.append(str(request.url))
        return html(f'<meta http-equiv="refresh" content="0;url={target}">')
    client = httpx.Client(transport=httpx.MockTransport(handler))
    result = Collector(config(tmp_path), client, sleep=lambda _: None).fetch(record(), check_robots=False)
    assert result.status == "skipped"
    assert result.redirect_history[-1]["result"] == "rejected_unsafe"
    assert calls == ["https://source.test/start"]


def test_http_redirect_then_meta_refresh_share_history(tmp_path, monkeypatch):
    def handler(request):
        if request.url.path == "/start":
            return httpx.Response(302, headers={"location": "/middle"})
        if request.url.path == "/middle":
            return html('<meta http-equiv="refresh" content="0;url=https://final.test/report">')
        return html("<article>final</article>")
    result = collector(tmp_path, handler, monkeypatch).fetch(record(), check_robots=False)
    assert result.status == "fetched"
    assert [hop["type"] for hop in result.redirect_history] == ["http", "meta_refresh"]
    assert all(hop["result"] == "followed" for hop in result.redirect_history)


def test_redirect_cycle_is_rejected(tmp_path, monkeypatch):
    def handler(request):
        target = "/b" if request.url.path == "/start" else "/start"
        return html(f'<meta http-equiv="refresh" content="0;url={target}">')
    result = collector(tmp_path, handler, monkeypatch).fetch(record(), check_robots=False)
    assert result.status == "needs_review"
    assert result.redirect_history[-1]["result"] == "rejected_cycle"
    assert "redirect_cycle" in result.review_reason


def test_combined_redirect_limit_is_enforced(tmp_path, monkeypatch):
    def handler(request):
        if request.url.path == "/start":
            return httpx.Response(302, headers={"location": "/middle"})
        return html('<meta http-equiv="refresh" content="0;url=/final">')
    result = collector(tmp_path, handler, monkeypatch, max_redirects=1).fetch(record(), check_robots=False)
    assert result.status == "needs_review"
    assert [hop["result"] for hop in result.redirect_history] == ["followed", "rejected_limit"]


def test_meta_target_blocked_by_robots_is_not_requested(tmp_path, monkeypatch):
    calls = []
    def handler(request):
        calls.append(str(request.url))
        return html('<meta http-equiv="refresh" content="0;url=https://blocked.test/private">')
    instance = collector(tmp_path, handler, monkeypatch)
    allow = urllib.robotparser.RobotFileParser()
    allow.parse(["User-agent: *", "Allow: /"])
    deny = urllib.robotparser.RobotFileParser()
    deny.parse(["User-agent: *", "Disallow: /private"])
    instance.robots["https://source.test"] = allow
    instance.robots["https://blocked.test"] = deny
    result = instance.fetch(record(), check_robots=True)
    assert result.status == "skipped"
    assert result.redirect_history[-1]["result"] == "blocked_by_robots_txt"
    assert calls == ["https://source.test/start"]


def test_intermediate_html_is_preserved(tmp_path, monkeypatch):
    original = b'<meta http-equiv="refresh" content="0;url=/final"><p>audit me</p>'
    def handler(request):
        return httpx.Response(200, headers=HTML_HEADERS, content=(original if request.url.path == "/start" else b"final"))
    result = collector(tmp_path, handler, monkeypatch).collect([record()], check_robots=False)[0]
    intermediate = tmp_path / result.redirect_history[0]["intermediate_path"]
    final = tmp_path / result.raw_path
    manifest = json.loads((tmp_path / "data/raw/DAN-META.json").read_text())
    assert intermediate.read_bytes() == original
    assert final.read_bytes() == b"final"
    assert intermediate != final
    assert manifest["redirect_history"] == result.redirect_history


def test_resume_reviewed_intermediate_without_refetching_source(tmp_path, monkeypatch):
    raw = tmp_path / "data/raw/DAN-META.html"
    raw.parent.mkdir(parents=True)
    raw.write_text('<meta http-equiv="refresh" content="0;url=/final">', encoding="utf-8")
    previous = Document(
        "DAN-META", "Acme", "Outage", "https://source.test/start",
        final_url="https://source.test/start", domain="source.test", content_type="text/html",
        raw_path="data/raw/DAN-META.html", status="needs_review", review_reason=["empty_extraction"],
        redirects=["https://source.test/start"],
    )
    save_document(raw.parent, previous)
    calls = []
    def handler(request):
        calls.append(str(request.url))
        assert request.url.path == "/final"
        return html("<article>recovered report</article>")
    result = collector(tmp_path, handler, monkeypatch).collect([record()], check_robots=False)[0]
    assert calls == ["https://source.test/final"]
    assert result.status == "fetched"
    assert result.review_reason == []
    assert result.redirect_history[0]["migrated_from_legacy"] is True
    assert result.redirect_history[1]["type"] == "meta_refresh"
    assert Path(tmp_path / result.redirect_history[1]["intermediate_path"]).exists()


def test_pinned_backend_connects_only_to_validated_ip(monkeypatch):
    connected = []
    sentinel = object()
    def fake_connect(self, host, port, **kwargs):
        connected.append(host)
        return sentinel
    monkeypatch.setattr(httpcore.SyncBackend, "connect_tcp", fake_connect)
    backend = PinnedNetworkBackend()
    backend.pin("example.com", ("93.184.216.34",))
    assert backend.connect_tcp("example.com", 443) is sentinel
    assert connected == ["93.184.216.34"]
