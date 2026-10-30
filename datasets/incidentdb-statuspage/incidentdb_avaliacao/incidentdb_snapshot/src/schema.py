"""
IncidentDB Core Schema & Data Models
Defines the strict schema for real-world production incident postmortems,
root-cause configurations, and disaster remediation runbooks.
"""

from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional


@dataclass
class IncidentRecord:
    """Canonical representation of an engineering production postmortem."""

    incident_id: str
    company: str
    date: str
    title: str
    severity: str  # CRITICAL, HIGH, MEDIUM
    service_stack: List[str]
    categories: List[str]
    symptom_logs: str
    root_cause_analysis: str
    breaking_config_code: str
    remediation_patch: str
    prevention_checklist: List[str]
    source_url: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> IncidentRecord:
        return cls(
            incident_id=data["incident_id"],
            company=data["company"],
            date=data["date"],
            title=data["title"],
            severity=data["severity"],
            service_stack=list(data.get("service_stack", [])),
            categories=list(data.get("categories", [])),
            symptom_logs=data["symptom_logs"],
            root_cause_analysis=data["root_cause_analysis"],
            breaking_config_code=data["breaking_config_code"],
            remediation_patch=data["remediation_patch"],
            prevention_checklist=list(data.get("prevention_checklist", [])),
            source_url=data.get("source_url", ""),
            metadata=dict(data.get("metadata", {}))
        )

    def to_markdown(self) -> str:
        """Renders incident as a standardized, RAG-optimized Markdown document."""
        stack_str = ", ".join(self.service_stack)
        cats_str = ", ".join(self.categories)
        checklist_str = "\n".join(f"- [ ] {item}" for item in self.prevention_checklist)
        source_line = f" | **Source:** [{self.source_url}]({self.source_url})" if self.source_url else ""

        return f"""# [{self.incident_id}] {self.title}
**Company:** {self.company} | **Date:** {self.date} | **Severity:** {self.severity}{source_line}  
**Technologies:** {stack_str}  
**Categories:** {cats_str}  

---

## 1. Symptoms & Observed Errors
```text
{self.symptom_logs.strip()}
```

## 2. Root Cause Analysis
{self.root_cause_analysis.strip()}

## 3. Breaking Configuration / Problematic Code
```
{self.breaking_config_code.strip()}
```

## 4. Remediation Patch / Corrected Configuration
```
{self.remediation_patch.strip()}
```

## 5. Prevention & Hardening Checklist
{checklist_str}
"""
