from pathlib import Path


class ImportanceEngine:

    def calculate_score(
        self,
        file_path: Path,
        repo_root: Path
    ):

        score = 0

        relative_path = file_path.relative_to(
            repo_root
        )

        # Rule 1
        if len(relative_path.parts) == 1:
            score += 10

        # Rule 2
        try:

            content = file_path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            if (
                "__main__" in content
                or "FastAPI(" in content
                or "app.listen(" in content
            ):
                score += 30

            lines = len(
                content.splitlines()
            )

            score += min(
                lines // 50,
                20
            )

        except Exception:
            pass

        return score
    
    def rank_files(
        self,
        repo_path: str
    ):

        repo = Path(repo_path)

        ranked_files = []

        for file in repo.rglob("*"):

            if not file.is_file():
                continue

            score = self.calculate_score(
                file,
                repo
            )

            ranked_files.append(
                {
                    "file": str(
                        file.relative_to(repo)
                    ),
                    "score": score
                }
            )

        ranked_files.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked_files[:10]