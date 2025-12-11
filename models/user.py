class User:
    def __init__(self, user_id: int | None, username: str, role: str = "user"):
        # user_id optional
        self._user_id = user_id
        self._username = username
        self._role = role

    def get_id(self) -> int | None:
        return self._user_id

    def get_username(self) -> str:
        return self._username

    def get_role(self) -> str:
        return self._role

    def is_admin(self) -> bool:
        # Simple helper
        return self._role.lower() in ("admin", "administrator")

    def __str__(self) -> str:
        # useful for debugging and printing
        return f"User(id={self._user_id}, username='{self._username}', role='{self._role}')"