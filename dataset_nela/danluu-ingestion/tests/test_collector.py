import socket
from pathlib import Path

import httpx
import pytest

import danluu_ingestion.collector as collector_module
from danluu_ingestion.collector import Collector, UnsafeURL, validate_public_url
from danluu_ingestion.config import Settings
from danluu_ingestion.models import CatalogRecord


def public_resolver(host, port, type):
    address = "93.184.216.34" if host != "internal.test" else "127.0.0.1"
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (address, port))]


def record(url="https://example.com/post"):
    return CatalogRecord("DAN-T01", "Outage", "Acme", url, "example.com", "test", "")


def settings(tmp_path, **changes):
    values = dict(root=tmp_path, request_delay=0, retries=2, max_download_bytes=1024)
    values.update(changes)
    return Settings(**values)


def test_url_security_rejects_internal_and_bad_schemes():
    with pytest.raises(UnsafeURL):
        validate_public_url("http://internal.test/a", public_resolver)
    with pytest.raises(UnsafeURL):
        validate_public_url("file:///etc/passwd", public_resolver)


def test_fetch_html_and_resume(tmp_path, monkeypatch):
    monkeypatch.setattr(collector_module, "validate_public_url", lambda url: None)
    calls = 0
    def handler(request):
        nonlocal calls
        calls += 1
        return httpx.Response(200, headers={"content-type": "text/html"}, text="<h1>Incident</h1>")
    client = httpx.Client(transport=httpx.MockTransport(handler), headers={"User-Agent": "test"})
    instance = Collector(settings(tmp_path), client, sleep=lambda _: None)
    first = instance.collect([record()], check_robots=False)
    second = instance.collect([record()], check_robots=False)
    assert first[0].status == "fetched"
    assert second[0].status == "fetched"
    assert calls == 1
    assert (tmp_path / "data/raw/DAN-T01.html").exists()


def test_retry_then_success(tmp_path, monkeypatch):
    monkeypatch.setattr(collector_module, "validate_public_url", lambda url: None)
    calls = 0
    def handler(request):
        nonlocal calls
        calls += 1
        if calls < 3:
            raise httpx.ReadTimeout("slow", request=request)
        return httpx.Response(200, headers={"content-type": "application/pdf"}, content=b"%PDF-test")
    client = httpx.Client(transport=httpx.MockTransport(handler))
    result = Collector(settings(tmp_path), client, sleep=lambda _: None).fetch(record(), check_robots=False)
    assert result.status == "fetched"
    assert calls == 3


def test_http_failure_does_not_raise(tmp_path, monkeypatch):
    monkeypatch.setattr(collector_module, "validate_public_url", lambda url: None)
    client = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(503)))
    result = Collector(settings(tmp_path, retries=0), client, sleep=lambda _: None).fetch(record(), check_robots=False)
    assert result.status == "failed"
    assert "HTTPStatusError" in result.error


def test_redirect_to_internal_is_rejected(tmp_path, monkeypatch):
    def validate(url):
        if "127.0.0.1" in url:
            raise UnsafeURL("private")
    monkeypatch.setattr(collector_module, "validate_public_url", validate)
    client = httpx.Client(transport=httpx.MockTransport(
        lambda r: httpx.Response(302, headers={"location": "http://127.0.0.1/admin"})
    ))
    result = Collector(settings(tmp_path), client, sleep=lambda _: None).fetch(record(), check_robots=False)
    assert result.status == "failed"
    assert "UnsafeURL" in result.error


def test_download_limit(tmp_path, monkeypatch):
    monkeypatch.setattr(collector_module, "validate_public_url", lambda url: None)
    client = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(
        200, headers={"content-type": "text/html", "content-length": "9999"}, content=b"x"
    )))
    result = Collector(settings(tmp_path), client, sleep=lambda _: None).fetch(record(), check_robots=False)
    assert result.status == "failed"
    assert "size limit" in result.error

