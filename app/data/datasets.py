# app/data/datasets.py

import pandas as pd
from pathlib import Path
from .db import connect_database

DATA_DIR = Path(__file__).resolve().parents[2] / "DATA"
DATASETS_CSV = DATA_DIR / "datasets_metadata.csv"


def load_datasets_from_csv(csv_path: Path = DATASETS_CSV) -> int:
    if not csv_path.exists():
        print(f" CSV not found: {csv_path}")
        return 0

    conn = connect_database()
    df = pd.read_csv(csv_path)
    df.to_sql("datasets_metadata", conn, if_exists="append", index=False)
    count = len(df)
    conn.close()
    print(f" Loaded {count} datasets from {csv_path.name}")
    return count