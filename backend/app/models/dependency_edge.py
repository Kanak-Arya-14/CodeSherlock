from dataclasses import dataclass


@dataclass
class DependencyEdge:

    source: str

    target: str