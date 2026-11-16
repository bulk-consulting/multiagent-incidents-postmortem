from __future__ import annotations

import csv
import json
import os
import tempfile
from pathlib import Path
from typing import Iterable

from .models import CatalogRecord, Document


REQUIRED_COLUMNS = {"catalog_id", "category", "company", "url", "domain", "description", "priority"}


def read_catalog(path: Path) -> list[CatalogRecord]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"catalog missing columns: {', '.join(sorted(missing))}")
        records = [CatalogRecord(**{key: row.get(key, "") for key in REQUIRED_COLUMNS}) for row in reader]
    ids = [record.catalog_id for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("catalog_id values must be unique")
    return records


def write_json_atomic(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, path)
    except BaseException:
        Path(temporary).unlink(missing_ok=True)
        raise


def read_document(path: Path) -> Document:
    return Document(**json.loads(path.read_text(encoding="utf-8")))


def iter_documents(directory: Path) -> Iterable[Document]:
    for path in sorted(directory.glob("*.json")):
        yield read_document(path)


def save_document(directory: Path, document: Document) -> Path:
    path = directory / f"{document.catalog_id}.json"
    write_json_atomic(path, document.to_dict())
    return path
