from pathlib import Path


class ProjectStructureAnalyzer:

    def analyze(self, repo_path):

        repo_path = Path(repo_path)

        tree = {}

        self.build_tree(
            repo_path,
            tree
        )

        return tree

    def build_tree(
        self,
        current_path: Path,
        current_tree: dict
    ):

        for item in sorted(current_path.iterdir()):

            if item.name.startswith("."):
                continue

            if item.is_dir():

                current_tree[item.name] = {}

                self.build_tree(
                    item,
                    current_tree[item.name]
                )

            else:

                current_tree.setdefault(
                    "__files__",
                    []
                ).append(
                    item.name
                )