class RepositoryService:

    def analyze(self, repo_url: str):

        return {
            "status": "received",
            "repo_url": repo_url,
            "message": "Repository queued for analysis"
        }