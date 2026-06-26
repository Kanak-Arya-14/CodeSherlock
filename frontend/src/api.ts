import type { RepositoryResponse, ChatResponse } from "./types";

const BASE_URL = "http://127.0.0.1:8000";

export async function analyzeRepository(repoUrl: string) {

    const response = await fetch(`${BASE_URL}/analyze`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            repo_url: repoUrl
        })

    });

    const data = await response.json();

    return {

        owner: data.repository.owner,

        repository: data.repository.name,

        stars: data.repository.stars,

        language: data.repository.language,

        description: data.repository.description,

        summary: data.analysis.summary,

        tech_stack: data.analysis.tech_stack,

    } as RepositoryResponse;
}

export async function askAI(
    repoUrl: string,
    question: string
) {

    const response = await fetch(`${BASE_URL}/chat`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            repo_url: repoUrl,
            question
        })

    });

    return response.json() as Promise<ChatResponse>;
}