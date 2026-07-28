import {
    assessmentQuestionBank,
    type AssessmentCategory,
    type AssessmentSkill,
    type Question,
} from "./assessmentQuestions";

import type {
    AssessmentResult,
} from "./assessmentService";

export interface SkillAnalysis {
    skill: AssessmentSkill;
    score: number;
    total: number;
    percentage: number;
    performance: string;
}

export interface IndividualAssessmentAnalysis {
    category: AssessmentCategory;
    score: number;
    total: number;
    percentage: number;
    performance: string;
    skillAnalysis: SkillAnalysis[];
    strongAreas: SkillAnalysis[];
    moderateAreas: SkillAnalysis[];
    improvementAreas: SkillAnalysis[];
    summary: string;
    recommendation: string;
}

export interface CareerMatch {
    career: string;
    matchPercentage: number;
    reason: string;
}

export interface AssessmentAnalysis {
    performanceLevel: string;
    strengths: string[];
    weaknesses: string[];
    recommendations: string[];
    careerMatches: CareerMatch[];
}

function isAssessmentCategory(
    category: string
): category is AssessmentCategory {
    return (
        category === "aptitude" ||
        category === "math" ||
        category === "science" ||
        category === "english" ||
        category === "reasoning"
    );
}

function getPerformance(
    percentage: number
): string {
    if (percentage >= 85) {
        return "Excellent";
    }

    if (percentage >= 70) {
        return "Good";
    }

    if (percentage >= 50) {
        return "Average";
    }

    return "Needs Improvement";
}

function getResultQuestions(
    questions: Question[],
    result: AssessmentResult
): Question[] {
    if (
        result.questionIds.length === 0
    ) {
        return [];
    }

    const questionMap = new Map(
        questions.map(
            (question) => [
                question.id,
                question,
            ]
        )
    );

    return result.questionIds
        .map(
            (questionId) =>
                questionMap.get(questionId)
        )
        .filter(
            (
                question
            ): question is Question =>
                question !== undefined
        );
}

function createSkillAnalysis(
    questions: Question[],
    answers: number[]
): SkillAnalysis[] {
    const skillMap = new Map<
        AssessmentSkill,
        {
            score: number;
            total: number;
        }
    >();

    questions.forEach(
        (question, questionIndex) => {
            const isCorrect =
                answers[questionIndex] ===
                question.answer;

            const existingSkill =
                skillMap.get(question.skill);

            if (existingSkill) {
                existingSkill.total += 1;

                if (isCorrect) {
                    existingSkill.score += 1;
                }

                return;
            }

            skillMap.set(question.skill, {
                score: isCorrect ? 1 : 0,
                total: 1,
            });
        }
    );

    return Array.from(
        skillMap.entries()
    ).map(
        ([skill, skillResult]) => {
            const percentage =
                skillResult.total > 0
                    ? Math.round(
                        (
                            skillResult.score /
                            skillResult.total
                        ) *
                        100
                    )
                    : 0;

            return {
                skill,
                score: skillResult.score,
                total: skillResult.total,
                percentage,
                performance:
                    getPerformance(
                        percentage
                    ),
            };
        }
    );
}

function createSummary(
    category: AssessmentCategory,
    strongAreas: SkillAnalysis[],
    improvementAreas: SkillAnalysis[]
): string {
    const strongestArea =
        strongAreas[0];

    const weakestArea =
        improvementAreas[0];

    if (
        strongestArea &&
        weakestArea
    ) {
        return `Your strongest assessed area is ${strongestArea.skill} at ${strongestArea.percentage}%. ${weakestArea.skill} currently requires more improvement at ${weakestArea.percentage}%.`;
    }

    if (strongestArea) {
        return `Your strongest assessed area is ${strongestArea.skill} at ${strongestArea.percentage}%. Your current performance shows a positive foundation in this area.`;
    }

    if (weakestArea) {
        return `${weakestArea.skill} currently requires focused improvement. Regular concept revision and targeted practice are recommended.`;
    }

    switch (category) {
        case "aptitude":
            return "Your aptitude profile is developing across numerical, logical and analytical areas.";

        case "math":
            return "Your quantitative profile is developing across numerical and problem-solving areas.";

        case "science":
            return "Your science profile is developing across core scientific areas.";

        case "english":
            return "Your English profile is developing across grammar, vocabulary and comprehension.";

        case "reasoning":
            return "Your reasoning profile is developing across logical, analytical and problem-solving areas.";
    }
}

function createRecommendation(
    improvementAreas: SkillAnalysis[]
): string {
    if (
        improvementAreas.length === 0
    ) {
        return "Continue solving mixed practice questions and retake the assessment periodically to maintain your performance.";
    }

    const weakestSkills =
        improvementAreas
            .slice(0, 2)
            .map(
                (area) => area.skill
            )
            .join(" and ");

    return `Focus on ${weakestSkills} through concept revision, targeted practice questions and regular self-assessment.`;
}

function createCareerMatches(
    category: AssessmentCategory,
    skillAnalysis: SkillAnalysis[]
): CareerMatch[] {
    const getSkillPercentage = (
        skill: AssessmentSkill
    ): number =>
        skillAnalysis.find(
            (item) =>
                item.skill === skill
        )?.percentage ?? 0;

    const average = (
        values: number[]
    ): number => {
        if (values.length === 0) {
            return 0;
        }

        return Math.round(
            values.reduce(
                (sum, value) =>
                    sum + value,
                0
            ) / values.length
        );
    };

    switch (category) {
        case "aptitude":
            return [
                {
                    career:
                        "Engineering & Technology",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Numerical Ability"
                        ),
                        getSkillPercentage(
                            "Analytical Thinking"
                        ),
                        getSkillPercentage(
                            "Problem Solving"
                        ),
                    ]),
                    reason:
                        "Numerical, analytical and problem-solving ability support technical academic pathways.",
                },
                {
                    career:
                        "Data & Analytics",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Numerical Ability"
                        ),
                        getSkillPercentage(
                            "Analytical Thinking"
                        ),
                        getSkillPercentage(
                            "Logical Reasoning"
                        ),
                    ]),
                    reason:
                        "Numerical interpretation and analytical thinking support data-oriented study.",
                },
                {
                    career:
                        "Business & Management",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Analytical Thinking"
                        ),
                        getSkillPercentage(
                            "Problem Solving"
                        ),
                    ]),
                    reason:
                        "Analytical decision-making and practical problem solving support business pathways.",
                },
            ];

        case "math":
            return [
                {
                    career:
                        "Engineering & Technology",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Numerical Ability"
                        ),
                        getSkillPercentage(
                            "Arithmetic"
                        ),
                        getSkillPercentage(
                            "Problem Solving"
                        ),
                    ]),
                    reason:
                        "Quantitative and mathematical problem-solving ability supports engineering pathways.",
                },
                {
                    career:
                        "Data & Analytics",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Numerical Ability"
                        ),
                        getSkillPercentage(
                            "Problem Solving"
                        ),
                    ]),
                    reason:
                        "Numerical ability and structured problem solving support analytical study.",
                },
                {
                    career:
                        "Finance & Economics",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Numerical Ability"
                        ),
                        getSkillPercentage(
                            "Arithmetic"
                        ),
                    ]),
                    reason:
                        "Quantitative ability is useful for finance and economics pathways.",
                },
            ];

        case "science":
            return [
                {
                    career:
                        "Engineering & Technology",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Physics"
                        ),
                        getSkillPercentage(
                            "Chemistry"
                        ),
                    ]),
                    reason:
                        "Physics and Chemistry performance can support technical pathways.",
                },
                {
                    career:
                        "Health & Life Sciences",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Biology"
                        ),
                        getSkillPercentage(
                            "Chemistry"
                        ),
                    ]),
                    reason:
                        "Biology and Chemistry are important foundations for life-science pathways.",
                },
                {
                    career:
                        "Science & Research",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Physics"
                        ),
                        getSkillPercentage(
                            "Chemistry"
                        ),
                        getSkillPercentage(
                            "Biology"
                        ),
                    ]),
                    reason:
                        "Balanced scientific understanding supports science and research-oriented study.",
                },
            ];

        case "english":
            return [
                {
                    career:
                        "Communication & Media",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Grammar"
                        ),
                        getSkillPercentage(
                            "Vocabulary"
                        ),
                        getSkillPercentage(
                            "Reading Comprehension"
                        ),
                    ]),
                    reason:
                        "Language accuracy and comprehension support communication pathways.",
                },
                {
                    career:
                        "Humanities & Social Sciences",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Vocabulary"
                        ),
                        getSkillPercentage(
                            "Reading Comprehension"
                        ),
                    ]),
                    reason:
                        "Reading and verbal understanding support humanities-oriented study.",
                },
                {
                    career:
                        "Business & Management",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Grammar"
                        ),
                        getSkillPercentage(
                            "Reading Comprehension"
                        ),
                    ]),
                    reason:
                        "Clear communication is useful in professional environments.",
                },
            ];

        case "reasoning":
            return [
                {
                    career:
                        "Computer Science",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Logical Reasoning"
                        ),
                        getSkillPercentage(
                            "Analytical Thinking"
                        ),
                    ]),
                    reason:
                        "Logical and analytical thinking support computing pathways.",
                },
                {
                    career:
                        "Engineering & Technology",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Logical Reasoning"
                        ),
                        getSkillPercentage(
                            "Problem Solving"
                        ),
                    ]),
                    reason:
                        "Structured reasoning and problem solving support technical pathways.",
                },
                {
                    career:
                        "Data & Analytics",
                    matchPercentage: average([
                        getSkillPercentage(
                            "Analytical Thinking"
                        ),
                        getSkillPercentage(
                            "Logical Reasoning"
                        ),
                        getSkillPercentage(
                            "Problem Solving"
                        ),
                    ]),
                    reason:
                        "Analytical reasoning supports data-oriented pathways.",
                },
            ];
    }
}

export function analyzeAssessmentResult({
    category,
    questions,
    result,
}: {
    category: AssessmentCategory;
    questions: Question[];
    result: AssessmentResult;
}): IndividualAssessmentAnalysis {
    const resultQuestions =
        getResultQuestions(
            questions,
            result
        );

    const skillAnalysis =
        createSkillAnalysis(
            resultQuestions,
            result.answers
        );

    const calculatedScore =
        skillAnalysis.reduce(
            (score, skill) =>
                score + skill.score,
            0
        );

    const calculatedTotal =
        skillAnalysis.reduce(
            (total, skill) =>
                total + skill.total,
            0
        );

    const calculatedPercentage =
        calculatedTotal > 0
            ? Math.round(
                (
                    calculatedScore /
                    calculatedTotal
                ) *
                100
            )
            : 0;

    const sortedSkills = [
        ...skillAnalysis,
    ].sort(
        (firstSkill, secondSkill) =>
            secondSkill.percentage -
            firstSkill.percentage
    );

    const strongAreas =
        sortedSkills.filter(
            (skill) =>
                skill.percentage >= 70
        );

    const moderateAreas =
        sortedSkills.filter(
            (skill) =>
                skill.percentage >= 50 &&
                skill.percentage < 70
        );

    const improvementAreas =
        [...skillAnalysis]
            .filter(
                (skill) =>
                    skill.percentage < 50
            )
            .sort(
                (
                    firstSkill,
                    secondSkill
                ) =>
                    firstSkill.percentage -
                    secondSkill.percentage
            );

    return {
        category,
        score: calculatedScore,
        total: calculatedTotal,
        percentage:
            calculatedPercentage,
        performance: getPerformance(
            calculatedPercentage
        ),
        skillAnalysis,
        strongAreas,
        moderateAreas,
        improvementAreas,
        summary: createSummary(
            category,
            strongAreas,
            improvementAreas
        ),
        recommendation:
            createRecommendation(
                improvementAreas
            ),
    };
}

export function analyzeAssessment(
    result: AssessmentResult
): AssessmentAnalysis {
    if (
        !isAssessmentCategory(
            result.category
        )
    ) {
        return {
            performanceLevel:
                getPerformance(
                    result.percentage
                ),
            strengths: [],
            weaknesses: [
                "Assessment category could not be analyzed.",
            ],
            recommendations: [
                "Complete a supported assessment section.",
            ],
            careerMatches: [],
        };
    }

    const category = result.category;

    const questions =
        assessmentQuestionBank[category];

    const analysis =
        analyzeAssessmentResult({
            category,
            questions,
            result,
        });

    return {
        performanceLevel:
            analysis.performance,
        strengths:
            analysis.strongAreas.map(
                (area) =>
                    `${area.skill} — ${area.percentage}%`
            ),
        weaknesses:
            analysis.improvementAreas.map(
                (area) =>
                    `${area.skill} — ${area.percentage}%`
            ),
        recommendations: [
            analysis.recommendation,
            analysis.summary,
            "Review your skill-level performance and practice weaker areas before retaking this assessment.",
        ],
        careerMatches:
            createCareerMatches(
                category,
                analysis.skillAnalysis
            ),
    };
}