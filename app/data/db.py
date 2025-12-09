# app/data/db.py

from pathlib import Path
import sqlite3

# Path to the SQLite database file
DB_PATH = Path("DATA") / "week8_cw2.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    # Return rows as dictionaries (optional, but nice)
    conn.row_factory = sqlite3.Row
    return conn