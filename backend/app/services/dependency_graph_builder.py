from pathlib import Path

from app.models.dependency_edge import DependencyEdge
from app.services.module_resolver import ModuleResolver


class DependencyGraphBuilder:

    def __init__(self):

        self.module_resolver = ModuleResolver()

    def build(
        self,
        repository_imports:dict,
        repo_path:Path
    )-> list[DependencyEdge]:

        repo_path = Path(repo_path)

        edges: list[DependencyEdge] = []
        seen_edges = set()

        for source_file, imports in repository_imports.items():

            for imp in imports:

                target = self.module_resolver.resolve(
                    module=imp.module,
                    current_file=source_file,
                    repo_path=repo_path,
                    level=imp.level
                )

                if target is None:
                    continue

                edge_key=(
                    source_file,
                    target
                )    

                if edge_key in seen_edges:
                    continue

                seen_edges.add(edge_key)

                edge = DependencyEdge(
                    source=source_file,
                    target=target
                )

                edges.append(edge)

        return edges