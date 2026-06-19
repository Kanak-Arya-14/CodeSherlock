from urllib.parse import urlparse


class RepositoryService:

    def analyze(self, repo_url):

        repo_url = str(repo_url)

        parsed_url = urlparse(repo_url)

        path_parts = parsed_url.path.strip("/").split("/")

        owner = path_parts[0]
        repository = path_parts[1]

        return {
            "status": "received",
            "owner": owner,
            "repository": repository,
            "repo_url": repo_url
        }