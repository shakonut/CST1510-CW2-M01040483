# app/services/user_service.py

import bcrypt
from app.data.users import get_user_by_username, insert_user, migrate_users_from_file


def register_user(username: str, password: str, role: str = "user"):
    existing = get_user_by_username(username)
    if existing:
        return False, f"Username '{username}' already exists."

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"), bcrypt.gensalt()
    ).decode("utf-8")

    insert_user(username, password_hash, role)
    return True, f"User '{username}' registered successfully."


def login_user(username: str, password: str):
    user = get_user_by_username(username)
    if not user:
        return False, "User not found."

    stored_hash = user[2]  # (id, username, password_hash, role, created_at)
    ok = bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode("utf-8"),
    )
    if ok:
        return True, f"Welcome, {username}!"
    return False, "Incorrect password."


def migrate_from_users_txt() -> int:
    return migrate_users_from_file()