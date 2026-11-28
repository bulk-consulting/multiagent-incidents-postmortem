"""HTTP routes for incidents. Only input/output: the work is done in app/services."""
import logging

from fastapi import APIRouter, HTTPException

from app.schemas.incident import IncidentRequest, IncidentResponse
from app.services import incident_service

log = logging.getLogger(__name__)
router = APIRouter(prefix="/incidents", tags=["incidents"])


# POST /incidents
@router.post("", response_model=IncidentResponse, summary="Investiga um incidente e devolve o relatório")
def create_incident(request: IncidentRequest) -> IncidentResponse:
    try:
        return incident_service.investigate(request)
    except Exception as exc:  # the graph failed: the frontend shows the message
        log.exception("investigation failed")
        raise HTTPException(status_code=500, detail=f"A investigação falhou: {exc}") from exc

# Future endpoints
# POST /incidents/ID
# GET /incidents/ID
# GET /incidents/
