from urllib.parse import urlparse

from app.services.github_service import GitHubService
from app.services.repository_cloner import RepositoryCloner
from app.services.repository_scanner import RepositoryScanner
from app.services.tech_stack_detector import TechStackDetector
from app.services.import_analyzer import ImportAnalyzer
from app.services.dependency_graph_builder import DependencyGraphBuilder
from app.services.project_structure_analyzer import ProjectStructureAnalyzer
from app.services.repository_summary_generator import RepositorySummaryGenerator
from app.services.importance_ranker import ImportanceRanker


class RepositoryService:

    def __init__(self):

        self.github_service = GitHubService()

        self.repository_cloner = RepositoryCloner()

        self.repository_scanner = RepositoryScanner()

        self.tech_stack_detector = TechStackDetector()

        self.import_analyzer = ImportAnalyzer()

        self.dependency_graph_builder = DependencyGraphBuilder()

        self.project_structure_analyzer = (
            ProjectStructureAnalyzer()
        )

        self.summary_generator = (
            RepositorySummaryGenerator()
        )

        self.importance_ranker = ImportanceRanker()

    def analyze(self, repo_url):

        repo_url = str(repo_url)

        parsed_url = urlparse(repo_url)

        path_parts = parsed_url.path.strip("/").split("/")

        owner = path_parts[0]
        repository = path_parts[1]

        # -------------------------------
        # GitHub Metadata
        # -------------------------------

        repo_data = self.github_service.get_repository(
            owner,
            repository
        )

        # -------------------------------
        # Clone Repository
        # -------------------------------

        repo_path = self.repository_cloner.clone_repository(
            repo_url,
            repository
        )

        # -------------------------------
        # Repository Statistics
        # -------------------------------

        scan_result = (
            self.repository_scanner
            .count_files_and_folders(
                repo_path
            )
        )

        # -------------------------------
        # Tech Stack
        # -------------------------------

        tech_stack = (
            self.tech_stack_detector
            .detect(repo_path)
        )

        # -------------------------------
        # Repository Summary
        # -------------------------------

        summary = (
            self.summary_generator.generate(
                repo_data,
                scan_result,
                tech_stack
            )
        )

        tech_stack_response = [
            tech.to_dict()
            for tech in tech_stack
        ]

        # -------------------------------
        # Project Structure
        # -------------------------------

        project_structure = (
            self.project_structure_analyzer
            .analyze(repo_path)
        )

        # -------------------------------
        # Import Analysis
        # -------------------------------

        repository_imports = (
            self.import_analyzer.analyze(
                repo_path
            )
        )

        # -------------------------------
        # Dependency Graph
        # -------------------------------

        dependency_edges = (
            self.dependency_graph_builder.build(
                repository_imports,
                repo_path
            )
        )

        dependency_graph = [

            {
                "source": edge.source,
                "target": edge.target
            }

            for edge in dependency_edges

        ]

        # -------------------------------
        # Importance Ranking
        # -------------------------------

        important_files = (
            self.importance_ranker.rank_files(
                {
                    "tree": project_structure
                },
                dependency_graph
            )
        )

        # -------------------------------
        # Final Response
        # -------------------------------

        return {

            "repository": {

                "owner": owner,

                "name": repository,

                "stars": repo_data["stargazers_count"],

                "language": repo_data["language"],

                "description": repo_data["description"]

            },

            "statistics": {

                "files": scan_result["files"],

                "folders": scan_result["folders"]

            },

            "analysis": {

                "summary": summary,

                "tech_stack": tech_stack_response,

                "project_structure": {

                    "tree": project_structure

                },

                "dependency_summary": {

                    "nodes": len(repository_imports),

                    "edges": len(dependency_graph)

                },

                "important_files": important_files

            }

        }