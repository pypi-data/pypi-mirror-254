from xer_reader.src.table_data import table_data


class Table:
    """A class representing a P6 table"""

    depends: list[str]
    description: str
    key: str | None

    def __init__(
        self, name: str, labels: list[str], entries: list[dict[str, str]]
    ) -> None:
        self.name: str = name
        self.entries: list[dict[str, str]] = entries
        self.labels: list[str] = labels
        try:
            self.description = table_data[name]["description"]
            self.key = table_data[name]["key"]
            self.depends = table_data[name]["depends"]
        except KeyError:
            self.description = ""
            self.key = None
            self.depends = []

    def __bool___(self) -> bool:
        return len(self.entries) > 0

    def __len__(self) -> int:
        return len(self.entries)

    def __str__(self) -> str:
        return self.name

    @property
    def values(self) -> list[list[str]]:
        return [list(entry.values()) for entry in self.entries]
