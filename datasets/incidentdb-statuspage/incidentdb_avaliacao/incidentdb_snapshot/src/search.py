"""
IncidentDB Search & RAG Retrieval Engine
Provides ultra-fast local keyword and semantic query matching across
production incident postmortems without external vector database dependencies.
"""

from __future__ import annotations
import math
import re
from typing import List, Dict, Any, Optional
from src.schema import IncidentRecord


class IncidentSearchEngine:
    """In-memory search and ranking index for production postmortems."""

    def __init__(self, records: List[IncidentRecord]) -> None:
        self.records: List[IncidentRecord] = records
        self._doc_tokens: List[set] = []
        self._build_index()

    def _tokenize(self, text: str) -> List[str]:
        cleaned = re.sub(r"[^\w\s-]", " ", text.lower())
        return [t for t in cleaned.split() if len(t) > 2]

    def _build_index(self) -> None:
        self._doc_tokens.clear()
        for r in self.records:
            doc_text = (
                f"{r.incident_id} {r.company} {r.title} {' '.join(r.service_stack)} "
                f"{' '.join(r.categories)} {r.symptom_logs} {r.root_cause_analysis} "
                f"{r.breaking_config_code} {r.remediation_patch}"
            )
            self._doc_tokens.append(set(self._tokenize(doc_text)))

    def search(
        self,
        query: str,
        service: Optional[str] = None,
        severity: Optional[str] = None,
        category: Optional[str] = None,
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Executes token overlap and relevance scoring against the incident index.
        Returns top-matching incidents with score and highlighted matches.
        """
        query_tokens = set(self._tokenize(query))
        if not query_tokens and not service and not severity and not category:
            return []

        results: List[Dict[str, Any]] = []

        for idx, record in enumerate(self.records):
            # Apply strict metadata filters if specified
            if service and service.lower() not in [s.lower() for s in record.service_stack]:
                continue
            if severity and record.severity.upper() != severity.upper():
                continue
            if category and category.lower() not in [c.lower() for c in record.categories]:
                continue

            doc_toks = self._doc_tokens[idx]
            overlap = query_tokens.intersection(doc_toks)
            score = len(overlap)

            # Boost exact title matches
            title_toks = set(self._tokenize(record.title))
            score += len(query_tokens.intersection(title_toks)) * 3

            # Boost company matches
            if record.company.lower() in query.lower():
                score += 5

            if score > 0 or (not query_tokens and (service or severity or category)):
                results.append({
                    "score": score,
                    "record": record,
                    "matched_tokens": list(overlap)
                })

        # Sort descending by relevance score
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:limit]

    def get_statistics(self) -> Dict[str, Any]:
        """Calculates aggregated metrics across all indexed incidents."""
        company_counts: Dict[str, int] = {}
        tech_counts: Dict[str, int] = {}
        severity_counts: Dict[str, int] = {}
        category_counts: Dict[str, int] = {}

        for r in self.records:
            company_counts[r.company] = company_counts.get(r.company, 0) + 1
            severity_counts[r.severity] = severity_counts.get(r.severity, 0) + 1
            for t in r.service_stack:
                tech_counts[t] = tech_counts.get(t, 0) + 1
            for c in r.categories:
                category_counts[c] = category_counts.get(c, 0) + 1

        return {
            "total_incidents": len(self.records),
            "top_companies": sorted(company_counts.items(), key=lambda x: x[1], reverse=True)[:10],
            "top_technologies": sorted(tech_counts.items(), key=lambda x: x[1], reverse=True)[:10],
            "severity_distribution": severity_counts,
            "category_distribution": sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
        }
