import sqlite3
import csv
from pathlib import Path


# folder where this file is
PROJECT_ROOT = Path(__file__).parent

# database file will be created here
DB_PATH = PROJECT_ROOT / "multi_domain.db"

# path to the DATA folder CSV
CYBER_CSV = PROJECT_ROOT / "DATA" / "cyber_incidents.csv"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


def create_table_from_csv(conn, csv_path: Path, table_name: str):
    # read header row to get column names
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)  # first row = column names

    # build CREATE TABLE statement using header names
    columns_sql = ", ".join(f'"{h}" TEXT' for h in headers)
    create_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql});'

    cur = conn.cursor()
    cur.execute(create_sql)
    conn.commit()

    # insert all data rows
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # uses header row automatically
        rows = list(reader)

    placeholders = ", ".join("?" for _ in headers)
    insert_sql = f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES ({placeholders});'

    cur.executemany(
        insert_sql,
        [tuple(row[h] for h in headers) for row in rows]
    )
    conn.commit()

    return len(rows)


def count_rows(conn, table_name: str) -> int:
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name};")
    (count,) = cur.fetchone()
    return count


def main():
    print("Week 8 – SQLite + CSV loader")
    print(f"Database path: {DB_PATH}")

    conn = get_connection()

    # name of the table for cyber incidents
    table_name = "cyber_incidents"

    # load data from CSV into the table
    loaded = create_table_from_csv(conn, CYBER_CSV, table_name)
    print(f"Loaded {loaded} rows from {CYBER_CSV.name} into table '{table_name}'")

    # double check using SELECT COUNT(*)
    total = count_rows(conn, table_name)
    print(f"Table '{table_name}' currently has {total} rows.")

    conn.close()
    print("Done. Week 8 basic database test finished.")


if __name__ == "__main__":
    main()