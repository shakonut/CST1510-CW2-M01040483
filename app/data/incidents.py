# app/data/incidents.py

import pandas as pd
from pathlib import Path
from .db import connect_database

DATA_DIR = Path(__file__).resolve().parents[2] / "DATA"
CYBER_CSV = DATA_DIR / "cyber_incidents.csv"


def load_incidents_from_csv(csv_path: Path = CYBER_CSV) -> int:
    if not csv_path.exists():
        print(f" CSV not found: {csv_path}")
        return 0

    conn = connect_database()
    df = pd.read_csv(csv_path)
    df.to_sql("cyber_incidents", conn, if_exists="append", index=False)
    count = len(df)
    conn.close()
    print(f" Loaded {count} cyber incidents from {csv_path.name}")
    return count


def insert_incident(date, incident_type, severity, status, description, reported_by=None) -> int:
    conn = connect_database()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO cyber_incidents
        (date, incident_type, severity, status, description, reported_by)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (date, incident_type, severity, status, description, reported_by),
    )
    conn.commit()
    incident_id = cur.lastrowid
    conn.close()
    return incident_id


def get_all_incidents():
    conn = connect_database()
    df = pd.read_sql_query("SELECT * FROM cyber_incidents", conn)
    conn.close()
    return df


def update_incident_status(incident_id: int, new_status: str) -> int:
    conn = connect_database()
    cur = conn.cursor()
    cur.execute(
        "UPDATE cyber_incidents SET status = ? WHERE id = ?",
        (new_status, incident_id),
    )
    conn.commit()
    changed = cur.rowcount
    conn.close()
    return changed


def delete_incident(incident_id: int) -> int:
    conn = connect_database()
    cur = conn.cursor()
    cur.execute("DELETE FROM cyber_incidents WHERE id = ?", (incident_id,))
    conn.commit()
    deleted = cur.rowcount
    conn.close()
    return deleted