# app/data/datasets.py

from pathlib import Path
import pandas as pd
from .db import get_connection

DATA_DIR = Path("DATA")
DATASETS_CSV = DATA_DIR / "datasets_metadata.csv"
TABLE_NAME = "datasets"


def load_datasets_from_csv():
    if not DATASETS_CSV.exists():
        raise FileNotFoundError(f"CSV not found: {DATASETS_CSV}")

    df = pd.read_csv(DATASETS_CSV)

    conn = get_connection()
    try:
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    finally:
        conn.close()


def get_dataset_count() -> int:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
        (count,) = cur.fetchone()
        return count
    finally:
        conn.close()


def get_sample_datasets(limit: int = 5):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {TABLE_NAME} LIMIT ?", (limit,))
        return cur.fetchall()
    finally:
        conn.close()