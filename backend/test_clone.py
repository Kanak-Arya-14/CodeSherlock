from app.services.repository_cloner import RepositoryCloner

cloner = RepositoryCloner()

path = cloner.clone_repository(
    "https://github.com/fastapi/fastapi",
    "fastapi"
)

print(path)