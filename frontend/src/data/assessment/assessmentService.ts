import { api } from "../../services/api";

export interface AssessmentResult {
    attempt_id: number;
    assessment_type: string;
    total_questions: number;
    correct_answers: number;
    score: number;
    percentage: number;
    grade?: string | null;
    strengths: string[];
    weaknesses: string[];
    recommendation?: {
        career: string;
        learning_path: string[];
        recommended_projects: string[];
        recommended_certifications: string[];
        skill_gaps: string[];
        next_goal?: string | null;
    } | null;
    report?: {
        summary?: Record<string, unknown>;
        performance?: Record<string, unknown>;
        skill_matrix?: Array<Record<string, unknown>>;
        career?: Record<string, unknown> | null;
        placement_readiness?: string | null;
        interview_readiness?: string | null;
        next_steps?: string[];
    } | null;
    status: string;
    completed_at?: string | null;
}

export interface AssessmentAttempt {
    id: number;
    assessment_type: string;
    total_questions: number;
    correct_answers: number;
    score: number;
    status: string;
    started_at: string;
    completed_at?: string | null;
}

export interface AssessmentQuestion {
    id: number;
    question_text: string;
    option_a?: string | null;
    option_b?: string | null;
    option_c?: string | null;
    option_d?: string | null;
    difficulty: string;
    category?: string | null;
    skill?: string | null;
}

export interface AssessmentStartResponse {
    attempt: AssessmentAttempt;
    questions: AssessmentQuestion[];
}

export async function startAssessment(assessmentType: string): Promise<AssessmentStartResponse> {
    return api.post<AssessmentStartResponse>(`/assessment/${assessmentType}/start`, {});
}

export async function getActiveAssessment(assessmentType: string): Promise<AssessmentStartResponse> {
    return api.get<AssessmentStartResponse>(`/assessment/${assessmentType}/active`);
}

export async function submitAssessment(
    attemptId: number,
    answers: Array<{ question_id: number; selected_answer: string }>
): Promise<AssessmentResult> {
    const response = await api.post<AssessmentResult>(
        `/assessment/${attemptId}/submit`,
        { answers },
    );
    return response;
}

export async function getAssessmentHistory(limit = 50): Promise<AssessmentAttempt[]> {
    const response = await api.get<{ attempts: Array<AssessmentAttempt & { attempt_id?: number }> }>(
        `/assessment/results?limit=${Math.min(50, Math.max(1, limit))}`,
    );
    return (response.attempts ?? []).map((item) => ({
        ...item,
        id: item.attempt_id ?? item.id,
    }));
}

export async function getAssessmentResult(attemptId: number): Promise<AssessmentResult> {
    const response = await api.get<AssessmentResult>(`/assessment/results/${attemptId}`);
    return response;
}

export function getHighSchoolAssessmentType(
    studentClass: string,
    stream?: string | null,
): string {
    if (studentClass === "9" || studentClass === "10") {
        return "high_school_foundation";
    }

    const value = (stream ?? "").trim().toLowerCase();
    if (value.includes("pcmb")) return "high_school_pcm";
    if (value.includes("pcm") || (value.includes("physics") && value.includes("chemistry") && value.includes("mathematics"))) {
        return "high_school_pcm";
    }
    if (value.includes("pcb") || (value.includes("physics") && value.includes("chemistry") && value.includes("biology"))) {
        return "high_school_pcb";
    }
    if (value.includes("commerce") || value.includes("business")) return "high_school_commerce";
    if (value === "science" || value.startsWith("science ")) return "high_school_pcm";
    if (value.includes("humanities") || value.includes("arts")) return "high_school_arts";
    return "";
}

export function getUserAssessmentResults(_userId: string): AssessmentResult[] {
    // Results are now authoritative in the backend database.
    return [];
}

export function saveAssessmentResult(): never {
    throw new Error("Assessment results must be submitted to the backend.");
}
