from pydantic import BaseModel


class ChatRequest(BaseModel):

    repo_url: str

    question: str