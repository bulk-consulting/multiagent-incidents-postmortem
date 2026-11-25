"""Creates the FastAPI application. Run from the repository root:

    uvicorn app.main:app --reload

Swagger (automatic documentation): http://localhost:8000/docs
"""
import logging

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()  # .env at the repository root (NIM and database settings, used by the real agents)

from app.api import incidents  # noqa: E402  (after load_dotenv, so the settings are already read)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

app = FastAPI(
    title="Incident Copilot API",
    description="Recebe a descrição de um incidente e devolve o relatório dos agentes.",
    version="0.1.0",
)
app.include_router(incidents.router, prefix="/api/v1")


@app.get("/api/v1/health", tags=["health"], summary="Verifica se a API está no ar")
def health() -> dict:
    return {"status": "ok"}
