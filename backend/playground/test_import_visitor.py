import ast

from backend.app.services.import_visitor import ImportVisitor

code = """
import os
import math
import numpy as np
"""

tree = ast.parse(code)

visitor = ImportVisitor()

visitor.visit(tree)

for imp in visitor.imports:
    print(imp)