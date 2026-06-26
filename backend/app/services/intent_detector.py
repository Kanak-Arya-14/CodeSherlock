class IntentDetector:

    def detect(self, question: str):

        question = question.lower()

        if any(word in question for word in [
            "tech",
            "technology",
            "framework",
            "library",
            "stack"
        ]):

            return "tech_stack"

        if any(word in question for word in [
            "architecture",
            "structure",
            "dependency",
            "design"
        ]):

            return "architecture"

        if any(word in question for word in [
            "learn",
            "roadmap",
            "start",
            "begin",
            "study"
        ]):

            return "learning"

        return "general"