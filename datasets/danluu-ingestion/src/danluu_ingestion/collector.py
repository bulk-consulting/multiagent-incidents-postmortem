from __future__ import annotations

import hashlib
import ipaddress
import logging
import mimetypes
import re
import socket
import ssl
import threading
import time
import urllib.robotparser
from collections.abc import Callable
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit

import httpcore
import httpx

from .config import Settings
from .models import CatalogRecord, Document, ProcessingStatus
from .storage import read_document, save_document

LOG = logging.getLogger(__name__)
ACCEPTED_TYPES = {"text/html", "application/xhtml+xml", "application/pdf"}
HTML_TYPES = {"text/html", "application/xhtml+xml"}
RETRY_STATUSES = {429, 500, 502, 503, 504}


class UnsafeURL(ValueError):
    pass


class _MetaRefreshParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.contents: list[str | None] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "meta":
            values = {key.lower(): value for key, value in attrs}
            if (values.get("http-equiv") or "").strip().lower() == "refresh":
                self.contents.append(values.get("content"))


def parse_meta_refresh(content: bytes, base_url: str) -> tuple[str | None, str | None]:
    """Return an unambiguous explicit target, or a reason for manual review."""
    parser = _MetaRefreshParser()
    try:
        parser.feed(content.decode("utf-8", errors="replace"))
    except Exception:
        return None, "invalid_meta_refresh"
    if not parser.contents:
        return None, None
    targets: list[str] = []
    pattern = re.compile(r"^\s*\d+(?:\.\d+)?\s*;\s*url\s*=\s*(.*?)\s*$", re.I | re.S)
    for instruction in parser.contents:
        match = pattern.fullmatch(instruction or "")
        if not match or not match.group(1).strip():
            return None, "invalid_meta_refresh"
        value = match.group(1).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1].strip()
        if not value or any(character in value for character in "\r\n\x00"):
            return None, "invalid_meta_refresh"
        try:
            targets.append(urljoin(base_url, value))
        except ValueError:
            return None, "invalid_meta_refresh"
    if len(set(targets)) != 1:
        return None, "ambiguous_meta_refresh"
    return targets[0], None


def validate_public_url(url: str, resolver: Callable = socket.getaddrinfo) -> tuple[str, ...]:
    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"} or not parts.hostname or parts.username or parts.password:
        raise UnsafeURL("only absolute HTTP/HTTPS URLs without credentials are allowed")
    host = parts.hostname.rstrip(".").lower()
    if host == "localhost" or host.endswith(".localhost"):
        raise UnsafeURL("localhost is forbidden")
    try:
        port = parts.port or (443 if parts.scheme == "https" else 80)
        addresses = {item[4][0].split("%")[0] for item in resolver(host, port, type=socket.SOCK_STREAM)}
    except (socket.gaierror, ValueError) as exc:
        raise UnsafeURL(f"DNS resolution failed: {exc}") from exc
    if not addresses:
        raise UnsafeURL("hostname resolved to no addresses")
    for address in addresses:
        ip = ipaddress.ip_address(address)
        if not ip.is_global:
            raise UnsafeURL(f"non-public address is forbidden: {ip}")
    return tuple(sorted(addresses))


class PinnedNetworkBackend(httpcore.SyncBackend):
    """Connect to validated public IPs while httpcore retains hostname TLS/SNI."""

    def __init__(self) -> None:
        super().__init__()
        self._pins: dict[str, tuple[str, ...]] = {}
        self._lock = threading.Lock()

    def pin(self, host: str, addresses: tuple[str, ...]) -> None:
        with self._lock:
            self._pins[host.rstrip(".").lower()] = addresses

    def connect_tcp(self, host: str, port: int, **kwargs):  # type: ignore[no-untyped-def]
        with self._lock:
            addresses = self._pins.get(host.rstrip(".").lower())
        if not addresses:
            raise UnsafeURL(f"connection attempted without a validated DNS pin: {host}")
        last_error: Exception | None = None
        for address in addresses:
            try:
                return super().connect_tcp(address, port, **kwargs)
            except Exception as exc:
                last_error = exc
        assert last_error is not None
        raise last_error


class PinnedHTTPTransport(httpx.HTTPTransport):
    def __init__(self, backend: PinnedNetworkBackend) -> None:
        super().__init__(trust_env=False)
        self._pool.close()
        self._pool = httpcore.ConnectionPool(
            ssl_context=ssl.create_default_context(), network_backend=backend
        )


class Collector:
    def __init__(
        self, settings: Settings, client: httpx.Client | None = None, *, sleep=time.sleep,
        resolver: Callable = socket.getaddrinfo,
    ):
        self.settings = settings
        self.resolver = resolver
        self._pinned_backend = PinnedNetworkBackend() if client is None else None
        self.client = client or httpx.Client(
            timeout=settings.timeout, headers={"User-Agent": settings.user_agent},
            follow_redirects=False, transport=PinnedHTTPTransport(self._pinned_backend),
        )
        self.sleep = sleep
        self.last_request: dict[str, float] = {}
        self.robots: dict[str, urllib.robotparser.RobotFileParser] = {}

    def _prepare_url(self, url: str) -> None:
        addresses = (
            validate_public_url(url) if self.resolver is socket.getaddrinfo
            else validate_public_url(url, self.resolver)
        )
        if self._pinned_backend is not None:
            host = urlsplit(url).hostname
            assert host is not None
            self._pinned_backend.pin(host, addresses or ())

    def _wait(self, url: str) -> None:
        domain = urlsplit(url).hostname or ""
        wait = self.settings.request_delay - (time.monotonic() - self.last_request.get(domain, 0))
        if wait > 0:
            self.sleep(wait)
        self.last_request[domain] = time.monotonic()

    def _request(self, url: str) -> httpx.Response:
        self._prepare_url(url)
        last_error: Exception | None = None
        for attempt in range(self.settings.retries + 1):
            self._wait(url)
            try:
                request = self.client.build_request("GET", url)
                response = self.client.send(request, stream=True)
                if response.status_code not in RETRY_STATUSES or attempt == self.settings.retries:
                    return response
                response.close()
            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                last_error = exc
                if attempt == self.settings.retries:
                    raise
            self.sleep(0.5 * (2**attempt))
        raise RuntimeError("request retry loop exhausted") from last_error

    def _read_limited(self, response: httpx.Response) -> bytes:
        length = response.headers.get("content-length")
        if length and int(length) > self.settings.max_download_bytes:
            response.close()
            raise ValueError("download exceeds configured size limit")
        parts: list[bytes] = []
        size = 0
        try:
            for chunk in response.iter_bytes():
                size += len(chunk)
                if size > self.settings.max_download_bytes:
                    raise ValueError("download exceeds configured size limit")
                parts.append(chunk)
        finally:
            response.close()
        return b"".join(parts)

    def _allowed_by_robots(self, url: str) -> bool:
        parts = urlsplit(url)
        origin = f"{parts.scheme}://{parts.netloc}"
        if origin not in self.robots:
            parser = urllib.robotparser.RobotFileParser()
            parser.set_url(f"{origin}/robots.txt")
            try:
                response = self._request(parser.url)
                body = self._read_limited(response)
                parser.parse(body.decode("utf-8", errors="replace").splitlines() if response.status_code == 200 else [])
            except (httpx.HTTPError, ValueError, UnsafeURL):
                parser.parse([])
            self.robots[origin] = parser
        return self.robots[origin].can_fetch(self.settings.user_agent, url)

    def _save_intermediate(self, record: CatalogRecord, content: bytes, number: int) -> str:
        directory = self.settings.data_dir / "raw"
        path = directory / f"{record.catalog_id}.redirect-{number:03d}.html"
        while path.exists():
            number += 1
            path = directory / f"{record.catalog_id}.redirect-{number:03d}.html"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return str(path.relative_to(self.settings.root))

    @staticmethod
    def _hop(source: str, destination: str, kind: str, result: str, **extra) -> dict:
        return {"source_url": source, "destination_url": destination, "type": kind, "result": result, **extra}

    def _accept_target(
        self, document: Document, source: str, target: str, kind: str,
        visited: set[str], hop_count: int, check_robots: bool,
    ) -> bool:
        if target in visited:
            document.redirect_history.append(self._hop(source, target, kind, "rejected_cycle"))
            document.status = ProcessingStatus.NEEDS_REVIEW
            document.review_reason.append("redirect_cycle")
            return False
        if hop_count >= self.settings.max_redirects:
            document.redirect_history.append(self._hop(source, target, kind, "rejected_limit"))
            document.status = ProcessingStatus.NEEDS_REVIEW
            document.review_reason.append("redirect_limit_exceeded")
            return False
        try:
            self._prepare_url(target)
        except UnsafeURL as exc:
            document.redirect_history.append(self._hop(source, target, kind, "rejected_unsafe", detail=str(exc)))
            document.status = ProcessingStatus.SKIPPED if kind == "meta_refresh" else ProcessingStatus.FAILED
            if kind == "http":
                document.error = f"UnsafeURL: {exc}"
            document.review_reason.append("unsafe_redirect_target")
            return False
        if check_robots and not self._allowed_by_robots(target):
            document.redirect_history.append(self._hop(source, target, kind, "blocked_by_robots_txt"))
            document.status = ProcessingStatus.SKIPPED
            document.review_reason.append("blocked_by_robots_txt")
            return False
        document.redirect_history.append(self._hop(source, target, kind, "followed"))
        document.redirects.append(target)
        return True

    def fetch(
        self, record: CatalogRecord, *, check_robots: bool = True,
        document: Document | None = None, start_url: str | None = None,
        visited: set[str] | None = None, hop_count: int = 0,
    ) -> Document:
        document = document or Document(
            catalog_id=record.catalog_id, company=record.company, category=record.category,
            source_url=record.url, domain=record.domain,
        )
        current = start_url or record.url
        visited = visited or set()
        try:
            while True:
                self._prepare_url(current)
                if check_robots and not self._allowed_by_robots(current):
                    document.status = ProcessingStatus.SKIPPED
                    document.review_reason = sorted(set(document.review_reason + ["blocked_by_robots_txt"]))
                    return document
                visited.add(current)
                response = self._request(current)
                document.http_status = response.status_code
                response_url = str(response.url)
                if response.is_redirect:
                    location = response.headers.get("location")
                    response.close()
                    if not location:
                        raise httpx.HTTPError("redirect without Location header")
                    target = urljoin(response_url, location)
                    if not self._accept_target(document, response_url, target, "http", visited, hop_count, check_robots):
                        return document
                    current, hop_count = target, hop_count + 1
                    continue

                document.final_url = response_url
                document.fetched_at = datetime.now(timezone.utc).isoformat()
                media_type = response.headers.get("content-type", "").split(";", 1)[0].lower().strip()
                if not media_type:
                    media_type = mimetypes.guess_type(response_url)[0] or ""
                document.content_type = media_type or None
                if response.status_code >= 400:
                    response.close()
                    raise httpx.HTTPStatusError(f"HTTP {response.status_code}", request=response.request, response=response)
                if media_type not in ACCEPTED_TYPES:
                    response.close()
                    raise ValueError(f"unsupported content type: {media_type or 'unknown'}")
                content = self._read_limited(response)

                if media_type in HTML_TYPES:
                    target, reason = parse_meta_refresh(content, response_url)
                    if reason:
                        self._save_final(record, document, content, media_type)
                        document.status = ProcessingStatus.NEEDS_REVIEW
                        document.review_reason = sorted(set(document.review_reason + [reason]))
                        return document
                    if target:
                        audit_path = self._save_intermediate(record, content, hop_count + 1)
                        if not self._accept_target(document, response_url, target, "meta_refresh", visited, hop_count, check_robots):
                            document.redirect_history[-1]["intermediate_path"] = audit_path
                            return document
                        document.redirect_history[-1]["intermediate_path"] = audit_path
                        current, hop_count = target, hop_count + 1
                        continue

                self._save_final(record, document, content, media_type)
                document.status = ProcessingStatus.FETCHED
                document.error = None
                document.review_reason = []
                return document
        except Exception as exc:
            LOG.warning("fetch failed for %s: %s", record.catalog_id, exc)
            document.status = ProcessingStatus.FAILED
            document.error = f"{type(exc).__name__}: {exc}"
            return document

    def _save_final(self, record: CatalogRecord, document: Document, content: bytes, media_type: str) -> None:
        suffix = ".pdf" if media_type == "application/pdf" else ".html"
        path = self.settings.data_dir / "raw" / f"{record.catalog_id}{suffix}"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        document.raw_path = str(path.relative_to(self.settings.root))
        document.content_hash = hashlib.sha256(content).hexdigest()

    def _resume_meta_refresh(self, record: CatalogRecord, document: Document, check_robots: bool) -> Document | None:
        if not document.raw_path or document.content_type not in HTML_TYPES:
            return None
        path = self.settings.root / document.raw_path
        if not path.exists():
            return None
        content = path.read_bytes()
        base = document.final_url or document.source_url
        target, reason = parse_meta_refresh(content, base)
        if reason or not target:
            return None
        audit_path = self._save_intermediate(record, content, len(document.redirect_history) + 1)
        visited = {document.source_url, base}
        hop_count = len(document.redirect_history)
        if not self._accept_target(document, base, target, "meta_refresh", visited, hop_count, check_robots):
            document.redirect_history[-1]["intermediate_path"] = audit_path
            return document
        document.redirect_history[-1]["intermediate_path"] = audit_path
        return self.fetch(
            record, check_robots=check_robots, document=document, start_url=target,
            visited=visited, hop_count=hop_count + 1,
        )

    def collect(self, records: list[CatalogRecord], *, resume: bool = True, check_robots: bool = True) -> list[Document]:
        output = self.settings.data_dir / "raw"
        results = []
        for record in records:
            manifest = output / f"{record.catalog_id}.json"
            if resume and manifest.exists():
                existing = read_document(manifest)
                if not existing.redirect_history and existing.redirects:
                    source = existing.source_url
                    for target in existing.redirects:
                        existing.redirect_history.append(
                            self._hop(source, target, "http", "followed", migrated_from_legacy=True)
                        )
                        source = target
                resumed = self._resume_meta_refresh(record, existing, check_robots)
                if resumed is not None:
                    save_document(output, resumed)
                    results.append(resumed)
                    continue
                if existing.status in {"fetched", "extracted", "needs_review", "approved"}:
                    results.append(existing)
                    continue
            document = self.fetch(record, check_robots=check_robots)
            save_document(output, document)
            results.append(document)
        return results
