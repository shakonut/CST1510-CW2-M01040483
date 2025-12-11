class ITTicket:
    def __init__(
        self,
        ticket_id: int,
        title: str,
        priority: str,
        status: str,
        assignee: str | None = None,
        created_at: str | None = None,
    ):
        self._ticket_id = ticket_id
        self._title = title
        self._priority = priority
        self._status = status
        self._assignee = assignee
        self._created_at = created_at

    def get_id(self) -> int:
        return self._ticket_id

    def get_title(self) -> str:
        return self._title

    def get_priority(self) -> str:
        return self._priority

    def get_status(self) -> str:
        return self._status

    def get_assignee(self) -> str | None:
        return self._assignee

    def get_created_at(self) -> str | None:
        return self._created_at

    def is_open(self) -> bool:
        return self._status.lower() in ("open", "new", "in progress")

    def __str__(self) -> str:
        return (
            f"ITTicket(id={self._ticket_id}, title='{self._title}', "
            f"priority='{self._priority}', status='{self._status}')"
        )