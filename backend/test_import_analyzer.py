from app.services.import_analyzer import ImportAnalyzer

analyzer = ImportAnalyzer()

imports = analyzer.analyze("temp_repos/fastapi")

for file_name, import_list in imports.items():

    print(file_name)

    for imp in import_list:

        print(
            "   ",
            imp
        )

    print()