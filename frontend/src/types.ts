export interface TechStack {
    name: string;
    category: string;
}

export interface RepositoryResponse {

    owner: string;

    repository: string;

    stars: number;

    language: string;

    description: string;

    summary: string;

    tech_stack: TechStack[];
}

export interface ChatResponse {

    intent: string;

    answer: string;

}