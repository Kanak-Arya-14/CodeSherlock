from urllib.parse import urlparse

from app.services.github_service import GitHubService
from app.services.repository_cloner import RepositoryCloner
from app.services.repository_scanner import RepositoryScanner

class RepositoryService:

    def __init__(self):
        self.github_service = GitHubService()
        self.repository_cloner = RepositoryCloner()
        self.repository_scanner = RepositoryScanner()

    def analyze(self, repo_url):

        repo_url = str(repo_url)

        parsed_url = urlparse(repo_url)

        path_parts = parsed_url.path.strip("/").split("/")

        owner = path_parts[0]
        repository = path_parts[1]

        repo_path = self.repository_cloner.clone_repository(
            repo_url,
            repository
        )

        scan_result = (
            self.repository_scanner
            .count_files_and_folders(
                repo_path
            )
        )

        return {
            "owner": owner,
            "repository": repository,
            "stars": repo_data["stargazers_count"],
            "language": repo_data["language"],
            "description": repo_data["description"],
            "files": scan_result["files"],
            "folders": scan_result["folders"]
        
        }