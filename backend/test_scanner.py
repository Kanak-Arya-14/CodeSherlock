from app.services.repository_scanner import RepositoryScanner

scanner = RepositoryScanner()

result = scanner.count_files_and_folders(
    "temp_repos/fastapi"
)

print(result)