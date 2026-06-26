from dataclasses import dataclass


@dataclass
class ImportInfo:

    module: str | None

    imported_name: str | None

    alias: str | None

    level: int = 0