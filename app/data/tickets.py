# app/data/tickets.py

import pandas as pd
from pathlib import Path
from .db import connect_database

DATA_DIR = Path(__file__).resolve().parents[2] / "DATA"
TICKETS_CSV = DATA_DIR / "it_tickets.csv"


def load_tickets_from_csv(csv_path: Path = TICKETS_CSV) -> int:
    if not csv_path.exists():
        print(f" CSV not found: {csv_path}")
        return 0

    conn = connect_database()
    df = pd.read_csv(csv_path)
    df.to_sql("it_tickets", conn, if_exists="append", index=False)
    count = len(df)
    conn.close()
    print(f" Loaded {count} tickets from {csv_path.name}")
    return count