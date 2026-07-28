import { getCollegeProfile } from './collegeProfileService';
import {
    getCurrentContextAttempts,
} from './collegeAssessmentService';
import {
    analyzeResume,
    getResume,
} from './collegeResumeService';

export type PlacementItem = {
    id: string;
    company: string;
    role: string;
    type: string;
    status: string;
    date: string;
};

export type PracticeAttempt = {
    id: string;
    questionId: string;
    skill: string;
    correct: boolean;
    completedAt: string;
};

const get = <T,>(
    k: string,
    d: T
): T => {
    try {
        return JSON.parse(
            localStorage.getItem(k) || ''
        ) as T;
    } catch {
        return d;
    }
};

const set = (
    k: string,
    v: unknown
) =>
    localStorage.setItem(
        k,
        JSON.stringify(v)
    );

export const getPlacementItems = (
    u: string
): PlacementItem[] =>
    get(
        `college_placements_${u || 'guest'}`,
        []
    );

export const savePlacementItems = (
    u: string,
    v: PlacementItem[]
) =>
    set(
        `college_placements_${u || 'guest'}`,
        v
    );

export const getPracticeAttempts = (
    u: string
): PracticeAttempt[] =>
    get(
        `college_practice_attempts_${u || 'guest'}`,
        []
    );

export const savePracticeAttempt = (
    u: string,
    a: PracticeAttempt
) =>
    set(
        `college_practice_attempts_${u || 'guest'}`,
        [...getPracticeAttempts(u), a]
    );

export const getInterviewHistory = (
    u: string
): any[] =>
    get(
        `college_interviews_${u || 'guest'}`,
        []
    );

export const saveInterviewResult = (
    u: string,
    v: any
) =>
    set(
        `college_interviews_${u || 'guest'}`,
        [...getInterviewHistory(u), v]
    );

export function getSkillGap(
    u: string
) {
    const p = getCollegeProfile(u);

    const r = analyzeResume(
        getResume(u),
        p
    );

    const attempts =
        getCurrentContextAttempts(u, p);

    const latest = attempts.at(-1);

    const weak = latest
        ? Object.entries(
            latest.skillScores
        )
            .filter(([, v]) => v < 60)
            .sort((a, b) => a[1] - b[1])
            .map(([skill, score]) => ({
                skill,
                score,
                source:
                    'Current assessment',
            }))
        : [];

    const missing =
        r.missingRoleSkills.map(
            (skill) => ({
                skill,
                score: 0,
                source:
                    'Resume / target-role evidence',
            })
        );

    return [...weak, ...missing].filter(
        (x, i, a) =>
            a.findIndex(
                (y) =>
                    y.skill.toLowerCase() ===
                    x.skill.toLowerCase()
            ) === i
    );
}

export function getCollegeStats(
    u: string
) {
    const p = getCollegeProfile(u);

    const attempts =
        getCurrentContextAttempts(u, p);

    const resume = analyzeResume(
        getResume(u),
        p
    );

    const practice =
        getPracticeAttempts(u);

    const placements =
        getPlacementItems(u);

    const interviews =
        getInterviewHistory(u);

    const assessment = attempts.length
        ? Math.round(
            attempts.reduce(
                (s, a) => s + a.percentage,
                0
            ) / attempts.length
        )
        : 0;

    const practicePct = practice.length
        ? Math.round(
            (practice.filter(
                (x) => x.correct
            ).length /
                practice.length) *
            100
        )
        : 0;

    const interviewScore =
        interviews.length
            ? interviews.at(-1).score
            : 0;

    const readiness = Math.round(
        assessment * 0.35 +
        resume.resumeScore * 0.25 +
        practicePct * 0.15 +
        interviewScore * 0.15 +
        Math.min(
            100,
            placements.length * 10
        ) *
        0.1
    );

    return {
        assessment,
        resume,
        practicePct,
        interviewScore,
        readiness,
        attempts,
        placements,
    };
}