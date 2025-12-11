import sqlite3
from pathlib import Path
from typing import Any, Iterable


class DatabaseManager:
    def __init__(self, db_path: str | Path = "DATA/intelligence_platform.db"):
        # using the same DB path as Week 8
        self._db_path = Path(db_path)
        self._conn: sqlite3.Connection | None = None

    def connect(self) -> None:
        if self._conn is None:
            self._conn = sqlite3.connect(str(self._db_path))

    def close(self) -> None:
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def execute(self, query: str, params: Iterable[Any] = (), commit: bool = False) -> sqlite3.Cursor:
        if self._conn is None:
            self.connect()

        cursor = self._conn.cursor()
        cursor.execute(query, tuple(params))

        if commit:
            self._conn.commit()

        return cursor

    def fetch_all(self, query: str, params: Iterable[Any] = ()) -> list[tuple]:
        cursor = self.execute(query, params, commit=False)
        return cursor.fetchall()

    def fetch_one(self, query: str, params: Iterable[Any] = ()) -> tuple | None:
        cursor = self.execute(query, params, commit=False)
        return cursor.fetchone()