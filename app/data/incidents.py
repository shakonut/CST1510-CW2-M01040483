# app/data/incidents.py

from pathlib import Path
import pandas as pd
from .db import get_connection, DB_PATH


DATA_DIR = Path("DATA")
INCIDENTS_CSV = DATA_DIR / "cyber_incidents.csv"
TABLE_NAME = "cyber_incidents"


def load_incidents_from_csv():
    if not INCIDENTS_CSV.exists():
        raise FileNotFoundError(f"CSV not found: {INCIDENTS_CSV}")

    df = pd.read_csv(INCIDENTS_CSV)

    conn = get_connection()
    try:
        # replace = drop existing table and recreate with CSV columns
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    finally:
        conn.close()


def get_incident_count() -> int:
    """
    Return total number of incident records in the table.
    """
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
        (count,) = cur.fetchone()
        return count
    finally:
        conn.close()


def get_sample_incidents(limit: int = 5):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {TABLE_NAME} LIMIT ?", (limit,))
        rows = cur.fetchall()
        return rows
    finally:
        conn.close()