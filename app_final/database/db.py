from pathlib import Path
from app_final.services.database_manager import DatabaseManager


DB_PATH = Path(__file__).resolve().parent.parent / "intelligence_platform.db"


def get_db() -> DatabaseManager:
    return DatabaseManager(DB_PATH)