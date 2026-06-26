from pathlib import Path

from git import Repo


class RepositoryCloner:

    def clone_repository(
        self,
        repo_url: str,
        repository_name: str
    ):

        clone_path = (
            Path("temp_repos")
            / repository_name
        )

        if clone_path.exists():
            return str(clone_path)

        Repo.clone_from(
            repo_url,
            clone_path
        )

        return str(clone_path)