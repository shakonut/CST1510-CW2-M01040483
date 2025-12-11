from typing import Optional
import bcrypt

from services.database_manager import DatabaseManager
from models.user import User


class AuthManager:
    def __init__(self, db: DatabaseManager):
        # Storing the DatabaseManager so all DB access goes through it
        self._db = db

    def _hash_password(self, plain_password: str) -> str:
        """Hash a plain text password using bcrypt."""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
        return hashed.decode("utf-8")

    def _check_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a plain text password against a stored hash."""
        try:
            return bcrypt.checkpw(
                plain_password.encode("utf-8"),
                hashed_password.encode("utf-8"),
            )
        except ValueError:
            # If something is wrong with the stored hash just fail safely
            return False

    def register_user(self, username: str, password: str, role: str = "user") -> tuple[bool, str]:
        """
        Register a new user.

        """
        # Simple input checks
        if not username or not password:
            return False, "Username and password cannot be empty."

        # Check if username already exists
        row = self._db.fetch_one(
            "SELECT id FROM users WHERE username = ?",
            (username,),
        )
        if row is not None:
            return False, "Username already exists."

        password_hash = self._hash_password(password)

        self._db.execute(
            """
            INSERT INTO users (username, password_hash, role)
            VALUES (?, ?, ?)
            """,
            (username, password_hash, role),
            commit=True,
        )

        return True, "User registered successfully."

    def login_user(self, username: str, password: str) -> Optional[User]:
        """
        Attempt to log in a user.

        """
        row = self._db.fetch_one(
            "SELECT id, username, password_hash, role FROM users WHERE username = ?",
            (username,),
        )

        if row is None:
            return None

        user_id, db_username, db_password_hash, role = row

        if not self._check_password(password, db_password_hash):
            return None

        # Return a User model 
        return User(user_id=user_id, username=db_username, role=role)