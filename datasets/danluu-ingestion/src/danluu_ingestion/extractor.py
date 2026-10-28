from __future__ import annotations

import re
from html import escape
from pathlib import Path
from urllib.parse import urlsplit

import pymupdf
import trafilatura
from bs4 import BeautifulSoup, NavigableString, Tag

from .models import Document, ProcessingStatus


def _html_fallback(content: bytes) -> tuple[str | None, str]:
    soup = BeautifulSoup(content, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else None
    for element in soup.select("script, style, nav, footer, header, aside, form, noscript"):
        element.decompose()
    root = soup.find("article") or soup.find("main") or soup.body or soup
    lines: list[str] = []
    for element in root.find_all(["h1", "h2", "h3", "p", "li", "pre", "code"]):
        text = element.get_text(" ", strip=True)
        if not text or (element.name == "code" and element.parent and element.parent.name == "pre"):
            continue
        if element.name in {"h1", "h2", "h3"}:
            text = f"{'#' * int(element.name[1])} {text}"
        elif element.name == "li":
            text = f"- {text}"
        elif element.name in {"pre", "code"}:
            text = f"```\n{text}\n```"
        lines.append(text)
    return title, "\n\n".join(lines)


def _semantic_article(fragment: Tag) -> str:
    return f"<html><body><article>{fragment}</article></body></html>"


def _flatten_lists(fragment: Tag, soup: BeautifulSoup) -> None:
    """Make link-heavy lists visible to precision extraction, in original order."""
    for listing in list(fragment.find_all(["ul", "ol"])):
        for index, item in enumerate(listing.find_all("li", recursive=False), start=1):
            paragraph = soup.new_tag("p")
            marker = f"{index}. " if listing.name == "ol" else "- "
            paragraph.append(NavigableString(marker))
            for child in list(item.contents):
                paragraph.append(child.extract() if isinstance(child, Tag) else child.extract())
            listing.insert_before(paragraph)
        listing.decompose()


def _google_status_report(soup: BeautifulSoup) -> str | None:
    rows = soup.select("table.status-updates tr")
    entries: list[tuple[str, str, Tag]] = []
    for row in rows:
        date = row.select_one(".date")
        time = row.select_one("td.time")
        description = row.select_one("td.description")
        if date and time and description:
            entries.append((date.get_text(" ", strip=True), time.get_text(" ", strip=True), description))
    if not entries:
        return None
    final_date, final_time, final_description = entries[0]
    parts = [
        "<html><body><article>",
        "<section><h1>Final incident report</h1>",
        f"<p>Published: {escape(final_date)} {escape(final_time)}</p>",
        str(final_description),
        "</section><section><h1>Status updates</h1>",
    ]
    for date, update_time, description in entries[1:]:
        parts.extend([
            "<section>", f"<h2>{escape(date)} — {escape(update_time)}</h2>",
            str(description), "</section>",
        ])
    parts.append("</section></article></body></html>")
    return "".join(parts)


def _tarsnap_message(soup: BeautifulSoup) -> str | None:
    """Turn an mharc plain-text message into semantic HTML without rewriting it."""
    message = soup.find("pre")
    if message is None:
        return None
    body = message.get_text("", strip=False).strip()
    signature = ""
    if "\n-- \n" in body:
        body, signature = body.rsplit("\n-- \n", 1)

    # The archive stores prose in a PRE with hard-wrapped mail lines. Blank
    # lines and underlined headings are the message's actual structure.
    blocks = re.split(r"\n\s*\n", body)
    parts = ["<html><body><article>"]
    index = 0
    while index < len(blocks):
        block = blocks[index].strip()
        lines = block.splitlines()
        if len(lines) == 2 and re.fullmatch(r"-+", lines[1].strip()):
            parts.append(f"<h2>{escape(lines[0].strip())}</h2>")
        else:
            # Preserve emphasis markers and factual wording; only undo the
            # transport-level hard wrapping used by the mailing-list archive.
            paragraph = re.sub(r"\s*\n\s*", " ", block)
            parts.append(f"<p>{escape(paragraph)}</p>")
        index += 1

    if signature:
        signature_lines = [line.strip() for line in signature.splitlines() if line.strip()]
        parts.append("<section><h2>Message signature</h2>")
        parts.extend(f"<p>{escape(line)}</p>" for line in signature_lines)
        parts.append("</section>")

    attachment = message.find_next_sibling("p")
    if attachment is not None and "signature.asc" in attachment.get_text(" ", strip=True):
        parts.append("<section><h2>OpenPGP signature metadata</h2>")
        parts.append(f"<p>{escape(attachment.get_text(' ', strip=True))}</p></section>")
    parts.append("</article></body></html>")
    return "".join(parts)


def _nest_five_whys_questions(soup: BeautifulSoup) -> None:
    """Keep each Five Whys question attached to its HTML-defined answer."""
    heading = soup.select_one("#root-cause-identification-the-five-whys")
    if heading is None:
        return
    root = heading.find_next_sibling("ul")
    if root is None:
        return
    # In the source, a question paragraph is immediately followed by the UL
    # containing its answer. Move that paragraph into the answer LI so the
    # relationship survives Markdown serialization at every nesting depth.
    # Deepest-first prevents moving an outer answer paragraph from detaching
    # a still-unprocessed nested question.
    for question in reversed(root.find_all("p")):
        strong = question.find("strong", recursive=False)
        answer_list = question.find_next_sibling("ul")
        if strong is None or answer_list is None or not strong.get_text(" ", strip=True).startswith("Why"):
            continue
        answers = answer_list.find_all("li", recursive=False)
        if len(answers) != 1:
            # A branching question has multiple source-defined answers. Keep
            # it on its parent list item, immediately before those branches.
            previous = question.find_previous_sibling("p")
            if previous is not None:
                previous.append(NavigableString(" "))
                for child in list(question.contents):
                    previous.append(child.extract() if isinstance(child, Tag) else child.extract())
                question.decompose()
            continue
        question.extract()
        answer = answers[0]
        first_paragraph = answer.find("p", recursive=False)
        combined = soup.new_tag("p")
        for child in list(question.contents):
            combined.append(child.extract() if isinstance(child, Tag) else child.extract())
        combined.append(NavigableString(" "))
        if first_paragraph is not None:
            for child in list(first_paragraph.contents):
                combined.append(child.extract() if isinstance(child, Tag) else child.extract())
            first_paragraph.replace_with(combined)
        else:
            # The deepest answer is a bare text node rather than a P.
            for child in list(answer.contents):
                if isinstance(child, Tag) and child.name in {"ul", "ol"}:
                    break
                combined.append(child.extract() if isinstance(child, Tag) else child.extract())
            answer.insert(0, combined)


def _article_html(content: bytes, url: str | None) -> tuple[BeautifulSoup, str]:
    soup = BeautifulSoup(content, "html.parser")
    parsed = urlsplit(url or "")
    host = (parsed.hostname or "").removeprefix("www.")
    path = parsed.path
    if host == "incident.io":
        article = soup.select_one("#content-top .prose")
        if article is not None:
            # The recruiting paragraph is inside the prose container, but is
            # structurally identifiable by its external job-board link.
            for link in article.select('a[href*="boards.eu.greenhouse.io/incidentio/jobs/"]'):
                paragraph = link.find_parent("p")
                if paragraph is not None:
                    paragraph.decompose()
            # Trafilatura's precision heuristics treat lists in an isolated
            # div fragment as navigation. A complete semantic article keeps
            # technical ul/ol elements classified as article content.
            return soup, _semantic_article(article)
    if host == "about.gitlab.com" and "postmortem-of-database-outage-of-january-31" in path:
        article = soup.select_one(".content .body")
        if article is not None:
            _flatten_lists(article, soup)
            return soup, _semantic_article(article)
    if host == "status.circleci.com" and path.endswith("/dcqb3fykhgvg"):
        # Statuspage renders the later operational updates as sibling rows.
        # The first direct row is the independently published postmortem.
        article = soup.select_one(".incident-updates-container > .update-row:first-of-type")
        if article is not None:
            return soup, _semantic_article(article)
    if host == "aws.amazon.com" and path.rstrip("/").endswith("/message/5467D2"):
        container = soup.select_one(
            "#summary-of-the-amazon-dynamodb-service-disruption-and-related-impacts-in-the-us-east-region"
        )
        if container is not None:
            return soup, _semantic_article(container)
    if host == "status.cloud.google.com" and path.endswith("/ow5i3PPK96RduMcb1SsW"):
        report = _google_status_report(soup)
        if report is not None:
            return soup, report
    if host == "web.archive.org" and "joyent.com/blog/manta-postmortem-7-27-2015" in path:
        article = soup.select_one("div.article")
        if article is not None:
            return soup, _semantic_article(article)
    if host == "twilio.com" and "billing-incident-post-mortem-breakdown-analysis-and-root-cause" in path:
        article = soup.select_one(".cmp-blog__body")
        if article is not None:
            return soup, _semantic_article(article)
    if host == "github.blog" and path.endswith("/dns-outage-post-mortem/"):
        article = soup.select_one("section.post__content")
        if article is not None:
            author = article.select_one(":scope > div.mt-8.mb-8.mb-md-0")
            if author is not None:
                author.decompose()
            return soup, _semantic_article(article)
    if host == "mail.tarsnap.com" and path.endswith("/msg00035.html"):
        message = _tarsnap_message(soup)
        if message is not None:
            return soup, message
    if host == "blog.rust-lang.org" and path.endswith("/crates-io-postmortem/"):
        _nest_five_whys_questions(soup)
        return soup, str(soup)
    return soup, content.decode("utf-8", errors="replace")


def _normalize_residual_html(text: str) -> str:
    # Trafilatura can leave simple typographic tags in Markdown. Do not touch
    # fenced code blocks, where angle-bracket syntax may be meaningful.
    parts = re.split(r"(```[\s\S]*?```)", text)
    for index in range(0, len(parts), 2):
        parts[index] = re.sub(r"</?(?:sup|sub)\b[^>]*>", "", parts[index], flags=re.I)
        parts[index] = re.sub(r"(\d)\s+(st|nd|rd|th)\b", r"\1\2", parts[index], flags=re.I)
    return "".join(parts)


def _deduplicate_exact_blocks(text: str) -> str:
    seen: set[str] = set()
    result: list[str] = []
    for block in re.split(r"\n\s*\n", text):
        normalized = re.sub(r"\s+", " ", block).strip()
        if normalized and normalized in seen:
            continue
        if normalized:
            seen.add(normalized)
            result.append(block.strip())
    return "\n\n".join(result)


def extract_html(content: bytes, url: str | None = None) -> tuple[str | None, str, str]:
    soup, decoded = _article_html(content, url)
    title = soup.title.get_text(" ", strip=True) if soup.title else None
    parsed = urlsplit(url or "")
    is_gitlab_database_postmortem = (
        (parsed.hostname or "").removeprefix("www.") == "about.gitlab.com"
        and "postmortem-of-database-outage-of-january-31" in parsed.path
    )
    text = trafilatura.extract(
        decoded, output_format="markdown", include_links=False, include_tables=True,
        include_formatting=True, favor_precision=not is_gitlab_database_postmortem,
        favor_recall=is_gitlab_database_postmortem,
    )
    if text and len(text.split()) >= 30:
        text = _normalize_residual_html(text.strip())
        if (parsed.hostname or "").removeprefix("www.") == "aws.amazon.com" and parsed.path.rstrip("/").endswith("/message/5467D2"):
            text = _deduplicate_exact_blocks(text)
        if (parsed.hostname or "").removeprefix("www.") == "about.gitlab.com" and "postmortem-of-database-outage-of-january-31" in parsed.path:
            text = re.sub(r"(?m)^(\d+)\\\. ", r"\1. ", text)
            text = re.sub(r"(?m)^\\- ", "- ", text)
        return title, text, "trafilatura"
    fallback_title, fallback = _html_fallback(content)
    return title or fallback_title, _normalize_residual_html(fallback.strip()), "beautifulsoup4"


def extract_pdf(content: bytes) -> tuple[str | None, str, str]:
    with pymupdf.open(stream=content, filetype="pdf") as pdf:
        metadata = pdf.metadata or {}
        title = metadata.get("title") or None
        pages = [page.get_text("text", sort=True).strip() for page in pdf]
    return title, "\n\n".join(page for page in pages if page), "pymupdf"


def extract_document(document: Document, project_root: Path) -> Document:
    if not document.raw_path:
        document.status = ProcessingStatus.FAILED
        document.error = "raw_path is missing"
        return document
    content = (project_root / document.raw_path).read_bytes()
    try:
        if document.content_type == "application/pdf":
            title, text, method = extract_pdf(content)
        else:
            title, text, method = extract_html(content, document.final_url or document.source_url)
        document.title = title
        document.extracted_text = re.sub(r"[ \t]+\n", "\n", text).strip()
        document.extraction_method = method
        document.word_count = len(document.extracted_text.split())
        document.status = ProcessingStatus.EXTRACTED
        document.error = None
    except Exception as exc:
        document.status = ProcessingStatus.FAILED
        document.error = f"{type(exc).__name__}: {exc}"
    return document

