from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    root: Path = Path(__file__).resolve().parents[2]
    user_agent: str = os.getenv(
        "DANLUU_USER_AGENT", "danluu-ingestion/0.1 (+mailto:replace-me@example.com)"
    )
    timeout: float = float(os.getenv("DANLUU_TIMEOUT", "20"))
    request_delay: float = float(os.getenv("DANLUU_REQUEST_DELAY", "2"))
    max_download_bytes: int = int(os.getenv("DANLUU_MAX_DOWNLOAD_BYTES", "10485760"))
    retries: int = 2
    max_redirects: int = 5

    @property
    def data_dir(self) -> Path:
        return self.root / "data"

    @property
    def catalog_path(self) -> Path:
        return self.data_dir / "catalog.csv"

