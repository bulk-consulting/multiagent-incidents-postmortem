from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from typing import Any


class ProcessingStatus(StrEnum):
    PENDING = "pending"
    FETCHED = "fetched"
    EXTRACTED = "extracted"
    NEEDS_REVIEW = "needs_review"
    FAILED = "failed"
    SKIPPED = "skipped"
    APPROVED = "approved"


@dataclass
class CatalogRecord:
    catalog_id: str
    category: str
    company: str
    url: str
    domain: str
    description: str
    priority: str | None = None


@dataclass
class Document:
    catalog_id: str
    company: str
    category: str
    source_url: str
    final_url: str | None = None
    domain: str | None = None
    title: str | None = None
    content_type: str | None = None
    fetched_at: str | None = None
    http_status: int | None = None
    content_hash: str | None = None
    extraction_method: str | None = None
    extracted_text: str | None = None
    word_count: int = 0
    status: str = ProcessingStatus.PENDING
    review_reason: list[str] = field(default_factory=list)
    error: str | None = None
    redirects: list[str] = field(default_factory=list)
    redirect_history: list[dict[str, Any]] = field(default_factory=list)
    raw_path: str | None = None
    completeness: dict[str, bool] = field(default_factory=dict)
    editorial_approved: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

