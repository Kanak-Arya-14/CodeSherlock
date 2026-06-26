class RepositorySummaryGenerator:

    def generate(
        self,
        repo_data,
        scan_result,
        tech_stack
    ):

        language = (
            repo_data.get("language")
            or "Unknown"
        )

        description = (
            repo_data.get("description")
            or "No description available."
        )

        technologies = [
            tech.name
            for tech in tech_stack
        ]

        technologies = technologies[:5]

        summary = (
            f"This repository is primarily written in "
            f"{language}. "
            f"It contains "
            f"{scan_result['files']} files and "
            f"{scan_result['folders']} folders. "
            f"The project uses "
            f"{', '.join(technologies)}. "
            f"Repository description: {description}"
        )

        return summary