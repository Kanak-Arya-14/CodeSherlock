from pathlib import Path


class ImportanceRanker:

    def calculate_score(
        self,
        file_path: str,
        dependency_graph: list[dict]
    ):

        score = 0
        reasons = []

        path = Path(file_path)

        # ------------------------
        # Rule 1 : Root level file
        # ------------------------
        if len(path.parts) == 1:
            score += 10
            reasons.append("Root level file")

        # ------------------------
        # Rule 2 : Service layer
        # ------------------------
        if "services" in path.parts:
            score += 10
            reasons.append("Service layer")

        # ------------------------
        # Rule 3 : Models
        # ------------------------
        if "models" in path.parts:
            score += 5
            reasons.append("Model layer")

        # ------------------------
        # Rule 4 : Entry point
        # ------------------------
        if path.name in [
            "main.py",
            "app.py",
            "server.py",
            "run.py"
        ]:
            score += 30
            reasons.append("Application entry point")

        # ------------------------
        # Rule 5 : Incoming edges
        # ------------------------
        incoming = 0

        for edge in dependency_graph:

            if edge["target"] == file_path:
                incoming += 1

        if incoming:

            score += incoming * 15

            reasons.append(
                f"Imported by {incoming} file(s)"
            )

        # ------------------------
        # Rule 6 : Outgoing edges
        # ------------------------
        outgoing = 0

        for edge in dependency_graph:

            if edge["source"] == file_path:
                outgoing += 1

        if outgoing:

            score += outgoing * 5

            reasons.append(
                f"Depends on {outgoing} internal file(s)"
            )

        return {
            "file": file_path,
            "score": score,
            "reasons": reasons
        }

    def rank_files(
        self,
        project_structure,
        dependency_graph
    ):

        files = []

        self.collect_files(
            project_structure["tree"],
            "",
            files
        )

        ranked = []

        for file in files:

            ranked.append(

                self.calculate_score(
                    file,
                    dependency_graph
                )

            )

        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked[:10]

    def collect_files(
        self,
        tree,
        current_path,
        files
    ):

        for key, value in tree.items():

            if key == "__files__":

                for file in value:

                    if current_path:

                        files.append(
                            f"{current_path}/{file}"
                        )

                    else:

                        files.append(file)

            else:

                next_path = (
                    f"{current_path}/{key}"
                    if current_path
                    else key
                )

                self.collect_files(
                    value,
                    next_path,
                    files
                )