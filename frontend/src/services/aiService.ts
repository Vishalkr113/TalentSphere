import { api } from './api';

export type AIAction =
    | 'chat'
    | 'learning_support'
    | 'resume_analysis'
    | 'career_recommendation'
    | 'mock_interview';

export type AIGenerateResponse = {
    action: AIAction;
    text: string;
    model: string;
};

export async function generateAI(
    action: AIAction,
    prompt: string,
    context?: string,
): Promise<AIGenerateResponse> {
    return api.post<AIGenerateResponse>('/ai/generate', {
        action,
        prompt,
        context,
    });
}
