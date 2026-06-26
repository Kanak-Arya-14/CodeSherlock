from pathlib import Path
import ast

from app.services.import_visitor import ImportVisitor


class ImportAnalyzer:

    def analyze(self, repo_path):

        repo_path = Path(repo_path)

        repository_imports = {}

        for python_file in repo_path.rglob("*.py"):

            with open(
                python_file,
                "r",
                encoding="utf-8"
            ) as file:

                source_code = file.read()

            tree = ast.parse(source_code)

            visitor = ImportVisitor()

            visitor.visit(tree)

            relative_path = (
                python_file
                .relative_to(repo_path)
                .as_posix()
            )

            repository_imports[
                relative_path
            ] = visitor.imports

        return repository_imports