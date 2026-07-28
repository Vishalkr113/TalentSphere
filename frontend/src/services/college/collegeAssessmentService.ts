import type {
    CollegeProfileData,
} from './collegeProfileService';
import type {
    AssessmentAttempt,
    CollegeQuestion,
} from '../../data/college/assessment/collegeAssessmentTypes';
import {
    commonQuestions,
    collegeQuestionBanks,
} from '../../data/college/assessment/questions/collegeQuestionBanks';

const key = (u: string) =>
    `college_assessments_${u || 'guest'}`;

export const getAssessmentAttempts = (
    u: string
): AssessmentAttempt[] => {
    try {
        return JSON.parse(
            localStorage.getItem(key(u)) || '[]'
        );
    } catch {
        return [];
    }
};

export const getCurrentContextAttempts = (
    u: string,
    p: CollegeProfileData
) =>
    getAssessmentAttempts(u).filter(
        (a) =>
            a.degree === p.degree &&
            a.branch === p.branch &&
            a.semester === p.semester
    );

export function getCollegeQuestions(
    p: CollegeProfileData,
    category: string
) {
    const technical =
        collegeQuestionBanks[
        p.branch.toLowerCase()
        ] || [];

    if (category === 'aptitude')
        return commonQuestions;

    if (category === 'technical')
        return technical;

    return [
        ...commonQuestions,
        ...technical,
    ];
}

export function saveAssessmentAttempt(
    u: string,
    category: string,
    p: CollegeProfileData,
    qs: CollegeQuestion[],
    answers: number[]
) {
    let score = 0;

    const skill: Record<
        string,
        [number, number]
    > = {};

    const topic: Record<
        string,
        [number, number]
    > = {};

    qs.forEach((q, i) => {
        const ok = answers[i] === q.answer;

        if (ok) score++;

        skill[q.skill] ??= [0, 0];
        skill[q.skill][1]++;

        if (ok) skill[q.skill][0]++;

        topic[q.topic] ??= [0, 0];
        topic[q.topic][1]++;

        if (ok) topic[q.topic][0]++;
    });

    const pct = (x: [number, number]) =>
        Math.round((x[0] / x[1]) * 100);

    const a: AssessmentAttempt = {
        id: crypto.randomUUID(),
        userId: u,
        category,
        degree: p.degree,
        branch: p.branch,
        semester: p.semester,
        targetRole: p.targetRole,
        score,
        total: qs.length,
        percentage: qs.length
            ? Math.round(
                (score / qs.length) * 100
            )
            : 0,
        skillScores: Object.fromEntries(
            Object.entries(skill).map(
                ([k, v]) => [k, pct(v)]
            )
        ),
        topicScores: Object.fromEntries(
            Object.entries(topic).map(
                ([k, v]) => [k, pct(v)]
            )
        ),
        completedAt:
            new Date().toISOString(),
    };

    const all = getAssessmentAttempts(u);

    all.push(a);

    localStorage.setItem(
        key(u),
        JSON.stringify(all)
    );

    return a;
}

export type {
    AssessmentAttempt,
    CollegeQuestion,
} from '../../data/college/assessment/collegeAssessmentTypes';