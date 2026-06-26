import requests


class GitHubService:

    def get_repository(self, owner: str, repository: str):

        url = f"https://api.github.com/repos/{owner}/{repository}"

        response = requests.get(url)

        return response.json()