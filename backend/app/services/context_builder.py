class ContextBuilder:

    def build(
        self,
        analysis: dict,
        intent: str
    ):

        repository = analysis["repository"]

        repo_analysis = analysis["analysis"]

        context = {

            "repository": repository,

            "summary": repo_analysis["summary"]

        }

        if intent == "tech_stack":

            context["tech_stack"] = (
                repo_analysis["tech_stack"]
            )

        elif intent == "architecture":

            context["project_structure"] = (
                repo_analysis["project_structure"]
            )

            context["dependency_summary"] = (
                repo_analysis["dependency_summary"]
            )

            context["important_files"] = (
                repo_analysis["important_files"]
            )

        elif intent == "learning":

            context["important_files"] = (
                repo_analysis["important_files"]
            )

            context["tech_stack"] = (
                repo_analysis["tech_stack"]
            )

        else:

            context = analysis

        return context