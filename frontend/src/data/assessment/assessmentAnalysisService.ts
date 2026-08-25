import { api } from "../../services/api";

import {
    HighSchoolClass,
    HighSchoolStream,
} from "../../services/highSchoolProfileService";


// =====================================================
// Types
// =====================================================

export type AssessmentCategory =
    | "aptitude"
    | "math"
    | "science"
    | "english"
    | "reasoning";


export interface Question {

    id: number;

    question_code?: string;

    question: string;

    options: string[];

    difficulty?: string;

    category?: string;

    topic?: string;

}



export interface AssessmentQuestionBank {

    aptitude: Question[];

    math: Question[];

    science: Question[];

    english: Question[];

    reasoning: Question[];

}



export interface SkillAnalysis {

    skill: string;

    percentage: number;

    score?: number;

    total?: number;

    performance?: string;

}



export interface IndividualAssessmentAnalysis {


    category: string;


    summary: string;


    performance: string;


    score: number;


    total: number;


    percentage: number;


    skillAnalysis: SkillAnalysis[];


    strongAreas: SkillAnalysis[];


    improvementAreas: SkillAnalysis[];


    moderateAreas: SkillAnalysis[];


    strengths: string[];


    weaknesses: string[];


    recommendation: string | null;

}


// =====================================================
// Start Assessment
// =====================================================

export const startAssessment = async (
    assessmentType: string,
    _profile?: {
        studentClass: HighSchoolClass;
        currentStream: HighSchoolStream | null;
    }
): Promise<any> => {


    const response = await api.post(
        `/assessment/${assessmentType}/start`,
        {}
    );


    return response;

};



// =====================================================
// Submit Assessment
// =====================================================

export const submitAssessment = async (
    attemptId: number,
    answers: any[]
) => {


    const response = await api.post(
        `/assessment/${attemptId}/submit`,
        { answers }
    );


    return response;

};



// =====================================================
// Question Bank
// =====================================================

export const getAssessmentQuestionBank = (
    _profile?: any
): AssessmentQuestionBank => {


    return {

        aptitude: [],

        math: [],

        science: [],

        english: [],

        reasoning: []

    };

};



// =====================================================
// Analyze
// =====================================================

export const analyzeAssessment = (
    result: any,
    _profile?: any
) => {


    return {

        percentage:
            result?.percentage || 0,


        strengths:
            result?.strengths || [],


        weaknesses:
            result?.weaknesses || [],


        recommendation:
            result?.recommendation || null

    };

};



// Backward compatibility

export const analyzeAssessmentResult = (
    result: any
): IndividualAssessmentAnalysis => {

    return {


        category:
            result?.category ||
            result?.assessmentType ||
            "",


        summary:
            result?.summary ||
            "Assessment completed.",


        performance:
            result?.performance ||
            "Average",


        score:
            result?.score ||
            0,


        total:
            result?.total ||
            0,


        percentage:
            result?.percentage ||
            0,


        skillAnalysis:
            result?.skillAnalysis ||
            [],


        strongAreas:
            result?.strongAreas ||[],


        improvementAreas:
            result?.improvementAreas ||
            [],


        moderateAreas:
            result?.moderateAreas ||
            [],


        strengths:
            result?.strengths ||
            [],


        weaknesses:
            result?.weaknesses ||
            [],


        recommendation:
            result?.recommendation ||
            null

    };

};