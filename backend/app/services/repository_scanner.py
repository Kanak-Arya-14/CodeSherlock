from pathlib import Path

from app.utils.constants import IGNORED_FOLDERS


class RepositoryScanner:

    def count_files_and_folders(
        self,
        repo_path: str
    ):

        repo = Path(repo_path)

        file_count = 0
        folder_count = 0

        for item in repo.rglob("*"):

            if any(
                ignored in item.parts
                for ignored in IGNORED_FOLDERS
            ):
                continue

            if item.is_file():
                file_count += 1

            elif item.is_dir():
                folder_count += 1

        return {
            "files": file_count,
            "folders": folder_count
        }