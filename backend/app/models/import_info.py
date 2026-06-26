from dataclasses import dataclass


@dataclass
class ImportInfo:
    """
    Represents one import statement found
    inside a Python file.
    """

    module: str

    imported_name: str | None

    alias: str | None