from pathlib import Path
import ast

from app.models.import_info import ImportInfo


class ImportVisitor(ast.NodeVisitor):
    """
    Visits one Python file and collects
    all import statements.
    """

    def __init__(self):
        self.imports: list[ImportInfo] = []

    def visit_Import(self, node):
        """
        Handles:
            import os
            import numpy as np
        """

        for alias in node.names:

            info = ImportInfo(
                module=alias.name,
                imported_name=None,
                alias=alias.asname
            )

            self.imports.append(info)

        self.generic_visit(node)