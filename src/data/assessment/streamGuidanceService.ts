import {
    assessmentQuestionBank,
    type AssessmentCategory,
    type AssessmentSkill,
} from "./assessmentQuestions";

import {
    getUserAssessmentResults,
    type AssessmentResult,
} from "./assessmentService";

import {
    analyzeAssessmentResult,
    type IndividualAssessmentAnalysis,
} from "./assessmentAnalysisService";

export type StreamKey =
    | "PCM"
    | "PCB"
    | "Commerce"
    | "Humanities";

export interface StreamScore {
    stream: StreamKey;
    score: number;
    rank: number;
    fitLevel: string;
    strengths: string[];
    concerns: string[];
    reason: string;
}

export interface FinalStreamGuidance {
    ready: boolean;
    completedAssessments: number;
    requiredAssessments: number;
    recommendedStream: StreamKey | null;
    recommendationScore: number;
    confidenceLevel: string;
    streamScores: StreamScore[];
    strongestSkills: SkillEvidence[];
    improvementSkills: SkillEvidence[];
    summary: string;
    recommendationReason: string;
    nextSteps: string[];
}

export interface SkillEvidence {
    skill: AssessmentSkill;
    percentage: number;
}

interface SkillScoreMap {
    [key: string]: number;
}

const categories: AssessmentCategory[] = [
    "aptitude",
    "math",
    "english",
    "science",
    "reasoning",
];

function getLatestResultByCategory(
    results: AssessmentResult[],
    category: AssessmentCategory
) {
    const categoryResults = results.filter(
        (result) =>
            result.category === category
    );

    if (categoryResults.length === 0) {
        return null;
    }

    return categoryResults.reduce(
        (latestResult, currentResult) => {
            const latestTime = new Date(
                latestResult.completedAt
            ).getTime();

            const currentTime = new Date(
                currentResult.completedAt
            ).getTime();

            return currentTime > latestTime
                ? currentResult
                : latestResult;
        }
    );
}

function getAssessmentAnalyses(
    userId: string
): IndividualAssessmentAnalysis[] {
    const results =
        getUserAssessmentResults(userId);

    return categories
        .map((category) => {
            const result =
                getLatestResultByCategory(
                    results,
                    category
                );

            if (!result) {
                return null;
            }

            return analyzeAssessmentResult({
                category,
                questions:
                    assessmentQuestionBank[category],
                result,
            });
        })
        .filter(
            (
                analysis
            ): analysis is IndividualAssessmentAnalysis =>
                analysis !== null
        );
}

function createSkillScoreMap(
    analyses: IndividualAssessmentAnalysis[]
): SkillScoreMap {
    const skillTotals = new Map<
        AssessmentSkill,
        { score: number; total: number }
    >();

    analyses.forEach((analysis) => {
        analysis.skillAnalysis.forEach((skillResult) => {
            const existing = skillTotals.get(skillResult.skill);

            if (existing) {
                existing.score += skillResult.score;
                existing.total += skillResult.total;
                return;
            }

            skillTotals.set(skillResult.skill, {
                score: skillResult.score,
                total: skillResult.total,
            });
        });
    });

    const skillScoreMap: SkillScoreMap = {};

    skillTotals.forEach((value, skill) => {
        skillScoreMap[skill] =
            value.total > 0
                ? Math.round((value.score / value.total) * 100)
                : 0;
    });

    return skillScoreMap;
}

function getSkillScore(
    skillScoreMap: SkillScoreMap,
    skill: AssessmentSkill
) {
    return skillScoreMap[skill] ?? 0;
}

function weightedScore(
    values: Array<{
        score: number;
        weight: number;
    }>
) {
    const totalWeight = values.reduce(
        (total, value) =>
            total + value.weight,
        0
    );

    if (totalWeight === 0) {
        return 0;
    }

    const score = values.reduce(
        (total, value) =>
            total +
            value.score * value.weight,
        0
    );

    return Math.round(
        score / totalWeight
    );
}

function calculatePCMScore(
    skillScoreMap: SkillScoreMap
) {
    return weightedScore([
        {
            score: getSkillScore(
                skillScoreMap,
                "Numerical Ability"
            ),
            weight: 20,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Physics"
            ),
            weight: 25,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Logical Reasoning"
            ),
            weight: 15,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Problem Solving"
            ),
            weight: 15,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Analytical Thinking"
            ),
            weight: 10,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Arithmetic"
            ),
            weight: 10,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Chemistry"
            ),
            weight: 5,
        },
    ]);
}

function calculatePCBScore(
    skillScoreMap: SkillScoreMap
) {
    return weightedScore([
        {
            score: getSkillScore(
                skillScoreMap,
                "Biology"
            ),
            weight: 35,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Chemistry"
            ),
            weight: 25,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Reading Comprehension"
            ),
            weight: 10,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Analytical Thinking"
            ),
            weight: 10,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Problem Solving"
            ),
            weight: 10,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Physics"
            ),
            weight: 10,
        },
    ]);
}

function calculateCommerceScore(
    skillScoreMap: SkillScoreMap
) {
    return weightedScore([
        {
            score: getSkillScore(
                skillScoreMap,
                "Numerical Ability"
            ),
            weight: 25,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Arithmetic"
            ),
            weight: 20,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Analytical Thinking"
            ),
            weight: 20,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Problem Solving"
            ),
            weight: 15,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Logical Reasoning"
            ),
            weight: 10,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Reading Comprehension"
            ),
            weight: 10,
        },
    ]);
}

function calculateHumanitiesScore(
    skillScoreMap: SkillScoreMap
) {
    return weightedScore([
        {
            score: getSkillScore(
                skillScoreMap,
                "Reading Comprehension"
            ),
            weight: 30,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Vocabulary"
            ),
            weight: 20,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Analytical Thinking"
            ),
            weight: 15,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Logical Reasoning"
            ),
            weight: 15,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Grammar"
            ),
            weight: 10,
        },
        {
            score: getSkillScore(
                skillScoreMap,
                "Problem Solving"
            ),
            weight: 10,
        },
    ]);
}

function getFitLevel(
    score: number
) {
    if (score >= 80) {
        return "Strong Fit";
    }

    if (score >= 65) {
        return "Good Fit";
    }

    if (score >= 50) {
        return "Developing Fit";
    }

    return "Low Current Fit";
}

function getConfidenceLevel(
    firstScore: number,
    secondScore: number
) {
    const difference =
        firstScore - secondScore;

    if (
        firstScore >= 75 &&
        difference >= 15
    ) {
        return "High";
    }

    if (
        firstScore >= 60 &&
        difference >= 8
    ) {
        return "Moderate";
    }

    return "Exploratory";
}

function getRelevantSkills(
    stream: StreamKey
): AssessmentSkill[] {
    switch (stream) {
        case "PCM":
            return [
                "Numerical Ability",
                "Physics",
                "Logical Reasoning",
                "Problem Solving",
                "Analytical Thinking",
                "Arithmetic",
                "Chemistry",
            ];

        case "PCB":
            return [
                "Biology",
                "Chemistry",
                "Reading Comprehension",
                "Analytical Thinking",
                "Problem Solving",
                "Physics",
            ];

        case "Commerce":
            return [
                "Numerical Ability",
                "Arithmetic",
                "Analytical Thinking",
                "Problem Solving",
                "Logical Reasoning",
                "Reading Comprehension",
            ];

        case "Humanities":
            return [
                "Reading Comprehension",
                "Vocabulary",
                "Analytical Thinking",
                "Logical Reasoning",
                "Grammar",
                "Problem Solving",
            ];
    }
}

function createStreamReason(
    stream: StreamKey,
    strengths: string[],
    concerns: string[]
) {
    const strengthText =
        strengths.length > 0
            ? strengths
                .slice(0, 3)
                .join(", ")
            : "the assessed foundational skills";

    const concernText =
        concerns.length > 0
            ? ` However, ${concerns
                .slice(0, 2)
                .join(
                    " and "
                )} currently need further improvement.`
            : "";

    switch (stream) {
        case "PCM":
            return `PCM alignment is supported by your current performance in ${strengthText}.${concernText}`;

        case "PCB":
            return `PCB alignment is supported by your current performance in ${strengthText}.${concernText}`;

        case "Commerce":
            return `Commerce alignment is supported by your current performance in ${strengthText}.${concernText}`;

        case "Humanities":
            return `Humanities alignment is supported by your current performance in ${strengthText}.${concernText}`;
    }
}

function createStreamScore(
    stream: StreamKey,
    score: number,
    skillScoreMap: SkillScoreMap
): StreamScore {
    const relevantSkills =
        getRelevantSkills(stream);

    const strengths =
        relevantSkills
            .filter(
                (skill) =>
                    getSkillScore(
                        skillScoreMap,
                        skill
                    ) >= 70
            )
            .sort(
                (firstSkill, secondSkill) =>
                    getSkillScore(
                        skillScoreMap,
                        secondSkill
                    ) -
                    getSkillScore(
                        skillScoreMap,
                        firstSkill
                    )
            )
            .map(
                (skill) =>
                    `${skill} (${getSkillScore(
                        skillScoreMap,
                        skill
                    )}%)`
            );

    const concerns =
        relevantSkills
            .filter(
                (skill) =>
                    getSkillScore(
                        skillScoreMap,
                        skill
                    ) < 50
            )
            .sort(
                (firstSkill, secondSkill) =>
                    getSkillScore(
                        skillScoreMap,
                        firstSkill
                    ) -
                    getSkillScore(
                        skillScoreMap,
                        secondSkill
                    )
            )
            .map(
                (skill) =>
                    `${skill} (${getSkillScore(
                        skillScoreMap,
                        skill
                    )}%)`
            );

    return {
        stream,
        score,
        rank: 0,
        fitLevel: getFitLevel(score),
        strengths,
        concerns,
        reason: createStreamReason(
            stream,
            strengths,
            concerns
        ),
    };
}

function getAllSkillEvidence(
    skillScoreMap: SkillScoreMap
): SkillEvidence[] {
    return Object.entries(
        skillScoreMap
    )
        .map(([skill, percentage]) => ({
            skill: skill as AssessmentSkill,
            percentage,
        }))
        .sort(
            (firstSkill, secondSkill) =>
                secondSkill.percentage -
                firstSkill.percentage
        );
}

function createNextSteps(
    recommendedStream: StreamKey,
    improvementSkills: SkillEvidence[]
) {
    const weakestSkills =
        improvementSkills
            .slice(0, 2)
            .map((skill) => skill.skill);

    const nextSteps = [
        `Explore the subjects, study pattern and career pathways commonly associated with ${recommendedStream}.`,
        "Discuss the assessment evidence with a teacher, mentor or parent before making a final academic decision.",
    ];

    if (weakestSkills.length > 0) {
        nextSteps.push(
            `Improve ${weakestSkills.join(
                " and "
            )} through focused concept revision and targeted practice.`
        );
    }

    nextSteps.push(
        "Use this report as guidance evidence, not as the only factor in your final stream decision."
    );

    return nextSteps;
}

export function generateFinalStreamGuidance(
    userId: string
): FinalStreamGuidance {
    const analyses =
        getAssessmentAnalyses(userId);

    if (
        analyses.length <
        categories.length
    ) {
        return {
            ready: false,
            completedAssessments:
                analyses.length,
            requiredAssessments:
                categories.length,
            recommendedStream: null,
            recommendationScore: 0,
            confidenceLevel:
                "Not Available",
            streamScores: [],
            strongestSkills: [],
            improvementSkills: [],
            summary: `Complete all ${categories.length} assessments to generate your combined stream guidance report.`,
            recommendationReason:
                "The final recommendation requires evidence from Aptitude, Mathematics, English, Science and Logical Reasoning assessments.",
            nextSteps: [
                `Complete the remaining ${categories.length -
                analyses.length
                } assessment(s).`,
            ],
        };
    }

    const skillScoreMap =
        createSkillScoreMap(analyses);

    const streamScores = [
        createStreamScore(
            "PCM",
            calculatePCMScore(
                skillScoreMap
            ),
            skillScoreMap
        ),
        createStreamScore(
            "PCB",
            calculatePCBScore(
                skillScoreMap
            ),
            skillScoreMap
        ),
        createStreamScore(
            "Commerce",
            calculateCommerceScore(
                skillScoreMap
            ),
            skillScoreMap
        ),
        createStreamScore(
            "Humanities",
            calculateHumanitiesScore(
                skillScoreMap
            ),
            skillScoreMap
        ),
    ]
        .sort(
            (firstStream, secondStream) =>
                secondStream.score -
                firstStream.score
        )
        .map((stream, index) => ({
            ...stream,
            rank: index + 1,
        }));

    const recommendedStream =
        streamScores[0];

    const secondStream =
        streamScores[1];

    const allSkillEvidence =
        getAllSkillEvidence(
            skillScoreMap
        );

    const strongestSkills =
        allSkillEvidence
            .filter(
                (skill) =>
                    skill.percentage >= 70
            )
            .slice(0, 5);

    const improvementSkills =
        [...allSkillEvidence]
            .filter(
                (skill) =>
                    skill.percentage < 50
            )
            .sort(
                (firstSkill, secondSkill) =>
                    firstSkill.percentage -
                    secondSkill.percentage
            )
            .slice(0, 5);

    const confidenceLevel =
        getConfidenceLevel(
            recommendedStream.score,
            secondStream.score
        );

    const strongestSkillText =
        strongestSkills.length > 0
            ? strongestSkills
                .slice(0, 3)
                .map(
                    (skill) =>
                        `${skill.skill} (${skill.percentage}%)`
                )
                .join(", ")
            : "your current assessment profile";

    return {
        ready: true,
        completedAssessments:
            analyses.length,
        requiredAssessments:
            categories.length,
        recommendedStream:
            recommendedStream.stream,
        recommendationScore:
            recommendedStream.score,
        confidenceLevel,
        streamScores,
        strongestSkills,
        improvementSkills,
        summary: `Based on your combined performance across all five assessments, ${recommendedStream.stream} currently shows the strongest alignment with your assessed academic and cognitive skill profile.`,
        recommendationReason: `Your recommendation is mainly supported by ${strongestSkillText}. ${recommendedStream.reason}`,
        nextSteps: createNextSteps(
            recommendedStream.stream,
            improvementSkills
        ),
    };
}