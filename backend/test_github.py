from app.services.github_service import GitHubService

github_service = GitHubService()

data = github_service.get_repository(
    "fastapi",
    "fastapi"
)

print("Repository:", data["name"])
print("Owner:", data["owner"]["login"])
print("Stars:", data["stargazers_count"])
print("Language:", data["language"])