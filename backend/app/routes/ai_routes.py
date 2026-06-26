from fastapi import APIRouter

from app.models.chat_request import ChatRequest
from app.services.ai_service import AIService
from app.services.repository_service import RepositoryService


router = APIRouter()

repository_service = RepositoryService()

ai_service = AIService()


@router.post("/chat")
def chat(request: ChatRequest):

    analysis = repository_service.analyze(
        request.repo_url
    )

    response = ai_service.answer_question(
        analysis,
        request.question
    )

    return response