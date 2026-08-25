import { api } from "../api";

import type {
    CollegeProfileData,
} from "./collegeProfileService";


import type {
    AssessmentAttempt,
    CollegeQuestion,
} from "../../data/assessment/collegeAssessmentTypes";


export function getCurrentContextAttempts(
    userId: string,
    profile: CollegeProfileData
): AssessmentAttempt[] {


    return getAssessmentAttempts(userId).filter(
        (a) =>
            a.degree === profile.degree &&
            a.branch === profile.branch &&
            a.semester === profile.semester
    );

}


// =====================================================
// Fetch Questions From Backend
// =====================================================

export async function getCollegeQuestions(
    profile: CollegeProfileData,
    category: string
): Promise<CollegeQuestion[]> {


    const response = await api.post<{ questions?: CollegeQuestion[] }>(
        "/assessment/college/start",
        {
            category,

            degree:
                profile.degree,

            branch:
                profile.branch,

            semester:
                profile.semester,
        }
    );


    return response?.questions || [];

}





// =====================================================
// Get Saved Attempts
// =====================================================

export function getAssessmentAttempts(
    userId: string
): AssessmentAttempt[] {


    try {


        const data =
            localStorage.getItem(
                `college_assessments_${userId}`
            );


        return data
            ?
            JSON.parse(data)
            :
            [];


    } catch {


        return [];

    }

}





// =====================================================
// Save Attempt
// =====================================================

export function saveAssessmentAttempt(
    userId: string,
    attempt: AssessmentAttempt
): void {


    const oldAttempts =
        getAssessmentAttempts(
            userId
        );



    oldAttempts.push(
        attempt
    );



    localStorage.setItem(
        `college_assessments_${userId}`,
        JSON.stringify(
            oldAttempts
        )
    );

}

export type {
    AssessmentAttempt,
    CollegeQuestion,
} from "../../data/assessment/collegeAssessmentTypes";

export async function startCollegeAssessment(type: 'college_aptitude' | 'college_coding') {
    const { startAssessment } = await import('../../data/assessment/assessmentService');
    return startAssessment(type);
}

export async function getActiveCollegeAssessment(type: 'college_aptitude' | 'college_coding') {
    const { getActiveAssessment } = await import('../../data/assessment/assessmentService');
    return getActiveAssessment(type);
}

export async function submitCollegeAssessment(attemptId: number, answers: Array<{ question_id: number; selected_answer: string }>) {
    const { submitAssessment } = await import('../../data/assessment/assessmentService');
    return submitAssessment(attemptId, answers);
}

export async function getCollegeAssessmentHistory() {
    const { getAssessmentHistory } = await import('../../data/assessment/assessmentService');
    const history = await getAssessmentHistory();
    return history.filter((item) => item.assessment_type === 'college_aptitude' || item.assessment_type === 'college_coding');
}

export async function getCollegeAssessmentResult(attemptId: number) {
    const { getAssessmentResult } = await import('../../data/assessment/assessmentService');
    return getAssessmentResult(attemptId);
}
