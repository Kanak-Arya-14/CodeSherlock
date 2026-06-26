from pathlib import Path
import tomllib

from app.models.tech_stack import TechStack


TECH_MAPPING = {
    "fastapi": ("FastAPI", "framework"),
    "starlette": ("Starlette", "framework"),
    "uvicorn": ("Uvicorn", "server"),
    "pydantic": ("Pydantic", "library"),
    "numpy": ("NumPy", "library"),
    "pandas": ("Pandas", "library"),
    "scikit-learn": ("Scikit-learn", "library"),
    "sklearn": ("Scikit-learn", "library"),
    "torch": ("PyTorch", "library"),
    "tensorflow": ("TensorFlow", "library"),
    "django": ("Django", "framework"),
    "flask": ("Flask", "framework"),
    "sqlalchemy": ("SQLAlchemy", "library"),
    "redis": ("Redis", "database"),
}


class TechStackDetector:

    def detect(self, repo_path):

        repo_path = Path(repo_path)

        tech_stack = []

        self.detect_requirements(
            repo_path,
            tech_stack
        )

        self.detect_pyproject(
            repo_path,
            tech_stack
        )

        return tech_stack

    def detect_requirements(
        self,
        repo_path: Path,
        tech_stack: list[TechStack]
    ):

        requirements = repo_path / "requirements.txt"

        if not requirements.exists():
            return

        with open(requirements, "r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                if (
                    not line
                    or line.startswith("#")
                ):
                    continue

                package = (
                    line.lower()
                    .split("==")[0]
                    .split(">=")[0]
                    .split("<=")[0]
                    .split("~=")[0]
                    .split("[")[0]
                    .strip()
                )

                self.add_package(
                    package,
                    tech_stack
                )

    def detect_project_identity(
         self,
         data: dict,
         tech_stack: list[TechStack]
    ):

         project_name = None

          # PEP 621
         project = data.get(
         "project",
         {}
    )

         project_name = project.get(
         "name"
    )

    # Poetry
         if project_name is None:

           poetry = (
            data.get("tool", {})
            .get("poetry", {})
           )

           project_name = poetry.get(
            "name"
           )

         if project_name:

           self.add_package(
            project_name.lower(),
            tech_stack
           )            

    def detect_pyproject(
        self,
        repo_path: Path,
        tech_stack: list[TechStack]
    ):

        pyproject = repo_path / "pyproject.toml"

        if not pyproject.exists():
            return

        with open(pyproject, "rb") as file:

            data = tomllib.load(file)

        #detect what this project actually is
        self.detect_project_identity(
            data,
            tech_stack
        )

        dependencies=[]

        # PEP 621 projects
        project = data.get("project", {})
        dependencies.extend(
            project.get("dependencies", [])
        )

        # Poetry projects
        poetry = (
            data.get("tool", {})
            .get("poetry", {})
        )

        poetry_dependencies = poetry.get(
            "dependencies",
            {}
        )

        if isinstance(poetry_dependencies, dict):

            dependencies.extend(
                poetry_dependencies.keys()
            )

        for dependency in dependencies:

            if isinstance(dependency, str):

                package = (
                    dependency.lower()
                    .split("==")[0]
                    .split(">=")[0]
                    .split("<=")[0]
                    .split("~=")[0]
                    .split("[")[0]
                    .strip()
                )

                self.add_package(
                    package,
                    tech_stack
                )

    def add_package(
        self,
        package: str,
        tech_stack: list[TechStack]
    ):

        if not package:
            return

        # Avoid duplicates
        for tech in tech_stack:

            if tech.name.lower() == package.lower():

                return

        if package in TECH_MAPPING:

            name, category = TECH_MAPPING[package]

            tech_stack.append(

                TechStack(

                    name=name,

                    category=category,

                    confidence=1.0,

                    detected_by="mapping"

                )

            )

        else:

            tech_stack.append(

                TechStack(

                    name=package,

                    category="unknown",

                    confidence=0.0,

                    detected_by="mapping"

                )

            )