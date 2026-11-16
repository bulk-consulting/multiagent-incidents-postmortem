import zipfile
from pathlib import Path

BASE_DIR = Path(r"d:\Users\jjjj\day04_incidentdb")
DIST_DIR = BASE_DIR / "distribution"
DIST_DIR.mkdir(parents=True, exist_ok=True)
ZIP_FILE = DIST_DIR / "incidentdb_pro_vault.zip"

INCLUDE_PATHS = [
    "data/incident_database.jsonl",
    "data/incident_database_open50.jsonl",
    "rag_vault",
    "src",
    "notebook/1_click_incident_analysis.ipynb",
    "README.md",
    "LICENSE",
    "run_tests.py"
]

print(f"Creating Pro Vault package at: {ZIP_FILE}")

with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as zf:
    for item in INCLUDE_PATHS:
        path = BASE_DIR / item
        if path.is_file():
            zf.write(path, arcname=item)
            print(f"  [+] Added file: {item}")
        elif path.is_dir():
            for subpath in path.rglob("*"):
                if subpath.is_file():
                    rel = subpath.relative_to(BASE_DIR)
                    zf.write(subpath, arcname=str(rel))
                    print(f"  [+] Added file: {rel}")

print(f"\n[SUCCESS] Pro Vault zip archive created: {ZIP_FILE}")
print(f"Size: {ZIP_FILE.stat().st_size / 1024:.2f} KB")
