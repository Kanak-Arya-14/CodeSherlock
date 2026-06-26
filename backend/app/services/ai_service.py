from google import genai

from app.config import GEMINI_API_KEY
from app.prompts.prompt_builder import PromptBuilder
from app.services.intent_detector import IntentDetector
from app.services.context_builder import ContextBuilder


class AIService:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.prompt_builder = PromptBuilder()

        self.intent_detector = IntentDetector()

        self.context_builder = ContextBuilder()

    def answer_question(
        self,
        analysis: dict,
        question: str
    ):

        intent = self.intent_detector.detect(
            question
        )

        context = self.context_builder.build(
            analysis,
            intent
        )

        prompt = self.prompt_builder.build_repository_prompt(
            context,
            question
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {

            "intent": intent,

            "answer": response.text

        }