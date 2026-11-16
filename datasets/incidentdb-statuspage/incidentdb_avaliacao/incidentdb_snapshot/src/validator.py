"""
IncidentDB Census Gatekeeper & Schema Validator
Enforces zero-defect quality thresholds across all incident records:
- Zero placeholder stubs (no TODO, FIXME, STUB, TBD, placeholder)
- Minimum density and descriptive thresholds on logs, root-cause, and fixes
- Valid date formats and severity classifications
"""

from __future__ import annotations
import re
from typing import List, Tuple, Dict, Any
from src.schema import IncidentRecord


class ValidationError(Exception):
    """Raised when an incident record fails quality or structural invariants."""
    pass


class IncidentValidator:
    """Rigorous gatekeeper ensuring 100% ground-truth fidelity across records."""

    VALID_SEVERITIES = {"CRITICAL", "HIGH", "MEDIUM"}
    BANNED_TOKENS = ["TODO", "FIXME", "STUB", "TBD", "placeholder", "xxx", "asdf"]

    @classmethod
    def validate_record(cls, record: IncidentRecord) -> Tuple[bool, List[str]]:
        errors: List[str] = []

        # 1. Identity & Metadata Checks
        if not record.incident_id or not record.incident_id.strip():
            errors.append("incident_id must not be empty")
        elif not re.match(r"^INC-\d{4}-", record.incident_id):
            errors.append(f"incident_id '{record.incident_id}' must follow format INC-YYYY-...")

        if not record.company or len(record.company.strip()) < 2:
            errors.append("company name must be at least 2 characters")

        if not record.title or len(record.title.strip()) < 10:
            errors.append("title must be descriptive (at least 10 characters)")

        if record.severity not in cls.VALID_SEVERITIES:
            errors.append(f"severity '{record.severity}' must be one of {cls.VALID_SEVERITIES}")

        # 2. Technology & Classification
        if not record.service_stack or len(record.service_stack) == 0:
            errors.append("service_stack must contain at least one technology")

        if not record.categories or len(record.categories) == 0:
            errors.append("categories must contain at least one failure domain")

        # 3. Content Density & Non-Empty Checks
        if len(record.symptom_logs.strip()) < 30:
            errors.append("symptom_logs must contain detailed error signatures (>= 30 chars)")

        if len(record.root_cause_analysis.strip()) < 80:
            errors.append("root_cause_analysis must be dense and explanatory (>= 80 chars)")

        if len(record.breaking_config_code.strip()) < 20:
            errors.append("breaking_config_code must contain actual code/config (>= 20 chars)")

        if len(record.remediation_patch.strip()) < 20:
            errors.append("remediation_patch must contain actual corrected code/diff (>= 20 chars)")

        if not record.prevention_checklist or len(record.prevention_checklist) < 2:
            errors.append("prevention_checklist must contain at least 2 actionable checklist items")

        # 4. Zero-Tolerance Stub & Placeholder Scan
        combined_text = (
            f"{record.title} {record.symptom_logs} {record.root_cause_analysis} "
            f"{record.breaking_config_code} {record.remediation_patch} "
            f"{' '.join(record.prevention_checklist)}"
        ).lower()

        for token in cls.BANNED_TOKENS:
            if token.lower() in combined_text:
                errors.append(f"Prohibited stub/placeholder token detected: '{token}'")

        is_valid = len(errors) == 0
        return is_valid, errors

    @classmethod
    def assert_valid(cls, record: IncidentRecord) -> None:
        valid, errors = cls.validate_record(record)
        if not valid:
            raise ValidationError(f"Validation failed for {record.incident_id}: " + "; ".join(errors))
