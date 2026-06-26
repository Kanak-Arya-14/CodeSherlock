from app.services.import_analyzer import ImportAnalyzer

analyzer = ImportAnalyzer()

imports = analyzer.analyze("temp_repos/flask")

for file, values in imports.items():

    if values:

        print(file)

        for value in values:

            print(
                value.module,
                value.imported_name
            )

        print("-" * 50)