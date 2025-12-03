# app/data/db.py

import sqlite3
from pathlib import Path

# project & data folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "DATA"
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "intelligence_platform.db"


def connect_database(db_path: Path = DB_PATH) -> sqlite3.Connection:
    return sqlite3.connect(str(db_path))