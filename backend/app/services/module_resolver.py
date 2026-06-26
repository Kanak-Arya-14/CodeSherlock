from pathlib import Path


class ModuleResolver:

    def __init__(self):

        self.package_index = {}

    def build_index(
        self,
        repo_path: Path
    ):

        self.package_index.clear()

        for init_file in repo_path.rglob("__init__.py"):

            package_name = init_file.parent.name

            if package_name not in self.package_index:

                self.package_index[package_name] = []

            self.package_index[package_name].append(
                init_file.parent
            )

    def resolve(
        self,
        module: str | None,
        current_file: str,
        repo_path: Path,
        level: int = 0
    ):

        if not module:
            return None

        # ---------------------------------
        # Build package index once
        # ---------------------------------

        if not self.package_index:

            self.build_index(repo_path)

        # ---------------------------------
        # Relative imports
        # ---------------------------------

        if level > 0:

            current = (
                repo_path / current_file
            ).parent

            # Go up (level - 1) directories
            for _ in range(level - 1):

                current = current.parent

            relative = current / (
                module.replace(".", "/") + ".py"
            )

            if relative.exists():

                return (
                    relative
                    .relative_to(repo_path)
                    .as_posix()
                )

        # ---------------------------------
        # Direct lookup
        # ---------------------------------

        candidate = repo_path / (
            module.replace(".", "/") + ".py"
        )

        if candidate.exists():

            return (
                candidate
                .relative_to(repo_path)
                .as_posix()
            )

        # ---------------------------------
        # Package lookup
        # ---------------------------------

        parts = module.split(".")

        package = parts[0]

        remaining = parts[1:]

        if package not in self.package_index:

            return None

        for package_dir in self.package_index[package]:

            candidate = package_dir

            for part in remaining:

                candidate = candidate / part

            candidate = candidate.with_suffix(".py")

            if candidate.exists():

                return (
                    candidate
                    .relative_to(repo_path)
                    .as_posix()
                )

        return None