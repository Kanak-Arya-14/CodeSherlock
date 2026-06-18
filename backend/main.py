from fastapi import FastAPI

from models.repository import RepositoryRequest
from services.repository_service import RepositoryService

app = FastAPI()

repository_service = RepositoryService()


@app.get("/")
def root():
    return {
        "message": "Welcome to CodeSherlock"
    }


@app.post("/analyze")
def analyze_repository(repository: RepositoryRequest):

    return repository_service.analyze(
        repository.repo_url
    )