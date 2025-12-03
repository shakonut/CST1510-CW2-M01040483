# app/data/users.py

from pathlib import Path
from .db import connect_database

DATA_USERS_FILE = Path(__file__).resolve().parents[2] / "DATA" / "users.txt"


def get_user_by_username(username: str):
    conn = connect_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    return row


def insert_user(username: str, password_hash: str, role: str = "user"):
    conn = connect_database()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
        (username, password_hash, role),
    )
    conn.commit()
    conn.close()


def migrate_users_from_file(filepath: Path = DATA_USERS_FILE) -> int:
    if not filepath.exists():
        print(f" users.txt not found at {filepath}")
        return 0

    conn = connect_database()
    cur = conn.cursor()
    migrated = 0

    with filepath.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) < 2:
                continue

            username, password_hash = parts[0], parts[1]

            cur.execute("SELECT 1 FROM users WHERE username = ?", (username,))
            if cur.fetchone():
                continue  # already there

            cur.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                (username, password_hash, "user"),
            )
            migrated += 1

    conn.commit()
    conn.close()
    print(f" Migrated {migrated} user(s) from {filepath.name}")
    return migrated