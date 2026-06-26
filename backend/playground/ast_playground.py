import ast


code = """
class Student:

    def greet(self):

        print("Hello")
"""


tree = ast.parse(code)


class MyVisitor(ast.NodeVisitor):

    def visit_ClassDef(self, node):

        print("Found Class:", node.name)

        self.generic_visit(node)


visitor = MyVisitor()

visitor.visit(tree)