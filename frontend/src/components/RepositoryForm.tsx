import { useState } from "react";

interface Props {

    onAnalyze: (repo: string) => void;

}

export default function RepositoryForm({

    onAnalyze

}: Props) {

    const [repoUrl, setRepoUrl] = useState("");

    return (

        <div>

            <input

                value={repoUrl}

                onChange={(e) =>

                    setRepoUrl(e.target.value)

                }

                placeholder="Paste GitHub Repository URL"

            />

            <button

                onClick={() =>

                    onAnalyze(repoUrl)

                }

            >

                Analyze Repository

            </button>

        </div>

    );

}