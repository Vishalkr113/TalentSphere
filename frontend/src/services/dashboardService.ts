import { api } from './api';

export type DashboardAssessmentItem = {
    completed: boolean;
    score: number | null;
    percentage: number | null;
    grade: string | null;
    correct_answers: number | null;
    total_questions: number | null;
    attempt_id: number | null;
    completed_at: string | null;
    assessment_type: string | null;
};

export type DashboardData = {
    dashboard_type: string;
    user: { id: number; full_name: string; email: string; role: string };
    profile: {
        exists: boolean;
        profile_completion: number;
        profile_photo: string | null;
        resume_url: string | null;
        student_class: string | null;
        stream: string | null;
        board: string | null;
        school_name: string | null;
        college_name: string | null;
        course: string | null;
        branch: string | null;
        semester: string | null;
        cgpa: string | null;
        company_name: string | null;
        job_title: string | null;
        target_role: string | null;
        skills: string[];
    };
    assessment: {
        available: boolean;
        total_completed: number;
        latest_score: number | null;
        latest_grade: string | null;
        latest_assessment: string | null;
        latest_completed_at: string | null;
        aptitude: DashboardAssessmentItem;
        coding: DashboardAssessmentItem;
        professional: DashboardAssessmentItem;
        high_school: DashboardAssessmentItem;
        recent_attempts: DashboardAssessmentItem[];
    };
    career: {
        available: boolean;
        recommended_role: string | null;
        confidence: number | null;
        strengths: string[];
        skill_gaps: string[];
        learning_path: string[];
    };
    progress: {
        resume: number;
        assessment: number;
        coding: number;
        placement: number;
    };
    sections: { key: string; title: string; available: boolean }[];
};

export function getDashboard(): Promise<DashboardData> {
    return api.get<DashboardData>('/dashboard');
}

/**
 * Canonical frontend percentage contract: user-facing percentages are 0-100.
 * Assessment history score is already a percentage (not a raw correct count).
 */
export function normalizePercentage(value: number | null | undefined): number | null {
    if (value == null || !Number.isFinite(value)) return null;
    if (value < 0 || value > 100) return null;
    return Math.round(value);
}

export type AssessmentHistoryItem = {
    attempt_id: number;
    assessment_type: string;
    total_questions: number;
    correct_answers: number;
    score: number;
    percentage: number;
    status: string;
    started_at: string;
    completed_at: string | null;
    id: number;
    category: string;
    total: number;
    correct: number;
    startedAt: string;
    completedAt: string | null;
};

export async function getAssessmentHistory(): Promise<{
    total_attempts: number;
    attempts: AssessmentHistoryItem[];
}> {
    const response = await api.get<{
        total_attempts: number;
        attempts: {
            attempt_id: number;
            assessment_type: string;
            total_questions: number;
            correct_answers: number;
            score: number;
            percentage?: number;
            status: string;
            started_at: string;
            completed_at: string | null;
        }[];
    }>('/assessment/results');

    return {
        total_attempts: response.total_attempts,
        attempts: response.attempts.map((item) => {
            // Backend contract: score is already the normalized percentage.
            // Never divide score by total_questions here.
            const percentage = normalizePercentage(item.percentage) ?? normalizePercentage(item.score) ?? 0;
            return {
                ...item,
                percentage,
                id: item.attempt_id,
                category: item.assessment_type,
                total: item.total_questions,
                correct: item.correct_answers,
                startedAt: item.started_at,
                completedAt: item.completed_at,
            };
        }),
    };
}

export function getAssessmentResult(attemptId: number) {
    return api.get<any>(`/assessment/results/${attemptId}`);
}
