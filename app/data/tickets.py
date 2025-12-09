# app/data/tickets.py

from pathlib import Path
import pandas as pd
from .db import get_connection

DATA_DIR = Path("DATA")
TICKETS_CSV = DATA_DIR / "it_tickets.csv"
TABLE_NAME = "tickets"


def load_tickets_from_csv():
    if not TICKETS_CSV.exists():
        raise FileNotFoundError(f"CSV not found: {TICKETS_CSV}")

    df = pd.read_csv(TICKETS_CSV)

    conn = get_connection()
    try:
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    finally:
        conn.close()


def get_ticket_count() -> int:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
        (count,) = cur.fetchone()
        return count
    finally:
        conn.close()


def get_sample_tickets(limit: int = 5):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {TABLE_NAME} LIMIT ?", (limit,))
        return cur.fetchall()
    finally:
        conn.close()