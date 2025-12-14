class SecurityIncident:
    def __init__(
        self,
        incident_id: int,
        incident_type: str,
        severity: str,
        status: str,
        description: str,
    ):
        self._incident_id = incident_id
        self._incident_type = incident_type
        self._severity = severity
        self._status = status
        self._description = description

    def get_id(self) -> int:
        return self._incident_id

    def get_type(self) -> str:
        return self._incident_type

    def get_severity(self) -> str:
        return self._severity

    def get_status(self) -> str:
        return self._status

    def get_description(self) -> str:
        return self._description

    def is_high_severity(self) -> bool:
        # helpful later for dashboards
        return self._severity.lower() in ("high", "critical")

    def __str__(self) -> str:
        return (
            f"SecurityIncident(id={self._incident_id}, "
            f"type='{self._incident_type}', "
            f"severity='{self._severity}', "
            f"status='{self._status}')"
        )