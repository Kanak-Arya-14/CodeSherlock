from fastapi import FastAPI

from app.models.repository import RepositoryRequest
from app.services.repository_service import RepositoryService
from app.routes.ai_routes import router as ai_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://code-sherlock.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_router)


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