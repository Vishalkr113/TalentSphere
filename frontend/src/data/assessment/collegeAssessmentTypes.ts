export interface CollegeQuestion {

    id: number;

    question: string;

    options: string[];

    answer: number;

    skill: string;

    topic: string;

    difficulty?: string;

    category?: string;

}



export interface AssessmentAttempt {

    id: string;

    userId: string;

    category: string;

    degree: string;

    branch: string;

    semester: string;

    targetRole?: string;


    score: number;

    total: number;

    percentage: number;


    skillScores: Record<string, number>;

    topicScores: Record<string, number>;


    completedAt: string;

}