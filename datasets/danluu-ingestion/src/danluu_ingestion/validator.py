from __future__ import annotations

import re
from collections import defaultdict
from urllib.parse import urlsplit

from .models import Document, ProcessingStatus

ERROR_PATTERNS = re.compile(r"\b(page not found|404 not found|internal server error|bad gateway)\b", re.I)
BLOCK_PATTERNS = re.compile(r"\b(sign in|log in|access denied|captcha|verify you are human|subscribe to continue)\b", re.I)
MENU_PATTERN = re.compile(r"\b(home|about|contact|privacy|terms|menu)\b", re.I)
POSTMORTEM_TERMS = re.compile(r"\b(incident|outage|impact|root cause|timeline|mitigat|recover|prevent|remediat)\w*\b", re.I)

COMPLETENESS_PATTERNS = {
    "summary_context": r"\b(summary|overview|context|incident)\b",
    "symptoms": r"\b(symptom|alert|detect|observed|error)\w*\b",
    "impact": r"\b(impact|affected|unavailable|downtime)\b",
    "timeline": r"\b(timeline|chronology|\d{1,2}:\d{2}\s*(?:am|pm|utc)?)\b",
    "root_cause": r"\b(root cause|caused by|contributing factor)\b",
    "mitigation_recovery": r"\b(mitigat|recover|restor|resolv)\w*\b",
    "prevention": r"\b(prevent|action item|follow[- ]?up|remediat|lesson)\w*\b",
}


def validate_document(document: Document, catalog_description: str = "") -> Document:
    text = document.extracted_text or ""
    reasons: list[str] = []
    if not text.strip():
        reasons.append("empty_extraction")
    elif document.word_count < 100:
        reasons.append("short_extraction")
    if document.http_status == 200 and ERROR_PATTERNS.search(text):
        reasons.append("soft_http_error")
    # A single phrase is not evidence of a block page inside a substantial
    # incident report: e.g. Cloudflare discusses a regex which can "sign in"
    # a state, and Atlassian describes users unable to "log in" during the
    # incident. Genuine extracted interstitials remain short or lack incident
    # signals and are still flagged.
    if BLOCK_PATTERNS.search(text) and (document.word_count < 250 or not POSTMORTEM_TERMS.search(text)):
        reasons.append("login_paywall_or_block_page")
    terms = MENU_PATTERN.findall(text[:1500])
    if document.word_count < 250 and len(terms) >= 4:
        reasons.append("possible_navigation_instead_of_article")
    if document.source_url and document.final_url:
        source_host = (urlsplit(document.source_url).hostname or "").removeprefix("www.")
        final_host = (urlsplit(document.final_url).hostname or "").removeprefix("www.")
        if source_host != final_host:
            reasons.append("cross_domain_redirect")
    document.completeness = {
        key: bool(re.search(pattern, text, re.I)) for key, pattern in COMPLETENESS_PATTERNS.items()
    }
    if sum(document.completeness.values()) < 3:
        reasons.append("insufficient_postmortem_signals")
    if not POSTMORTEM_TERMS.search(text):
        reasons.append("content_may_not_match_catalog_reference")
    description_terms = {
        token.lower() for token in re.findall(r"[A-Za-z]{5,}", catalog_description)
        if token.lower() not in {"which", "their", "after", "during", "caused", "system", "service"}
    }
    text_terms = {token.lower() for token in re.findall(r"[A-Za-z]{5,}", text)}
    if len(description_terms) >= 8 and len(description_terms & text_terms) < 2:
        reasons.append("low_overlap_with_catalog_description")
    document.review_reason = sorted(set(document.review_reason + reasons))
    if document.status not in {ProcessingStatus.FAILED, ProcessingStatus.SKIPPED}:
        document.status = ProcessingStatus.NEEDS_REVIEW if document.review_reason else ProcessingStatus.EXTRACTED
    return document


def mark_duplicates(documents: list[Document]) -> dict[str, list[str]]:
    groups: dict[str, list[Document]] = defaultdict(list)
    for document in documents:
        if document.content_hash:
            groups[document.content_hash].append(document)
    duplicates: dict[str, list[str]] = {}
    for digest, members in groups.items():
        if len(members) > 1:
            ids = [member.catalog_id for member in members]
            duplicates[digest] = ids
            for member in members:
                member.review_reason = sorted(set(member.review_reason + ["possible_duplicate"]))
                if member.status not in {ProcessingStatus.FAILED, ProcessingStatus.SKIPPED}:
                    member.status = ProcessingStatus.NEEDS_REVIEW
    return duplicates


def approve(document: Document, *, reviewer_confirmed: bool) -> Document:
    if not reviewer_confirmed:
        raise ValueError("approval requires explicit reviewer confirmation")
    document.editorial_approved = True
    document.status = ProcessingStatus.APPROVED
    return document
