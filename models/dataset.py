class Dataset:
    def __init__(
        self,
        dataset_id: int,
        name: str,
        domain: str,
        owner: str,
        row_count: int | None = None,
        description: str | None = None,
    ):
        self._dataset_id = dataset_id
        self._name = name
        self._domain = domain
        self._owner = owner
        self._row_count = row_count
        self._description = description

    def get_id(self) -> int:
        return self._dataset_id

    def get_name(self) -> str:
        return self._name

    def get_domain(self) -> str:
        return self._domain

    def get_owner(self) -> str:
        return self._owner

    def get_row_count(self) -> int | None:
        return self._row_count

    def get_description(self) -> str | None:
        return self._description

    def __str__(self) -> str:
        return (
            f"Dataset(id={self._dataset_id}, name='{self._name}', "
            f"domain='{self._domain}', owner='{self._owner}')"
        )