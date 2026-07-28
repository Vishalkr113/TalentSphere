import type {
    Question,
} from "./assessmentQuestions";

export interface AssessmentResult {
    id: string;
    userId: string;
    category: string;
    score: number;
    total: number;
    percentage: number;
    questionIds: number[];
    answers: number[];
    completedAt: string;
}

const STORAGE_KEY =
    "talentsphere_assessments";

function isValidAssessmentResult(
    value: unknown
): value is AssessmentResult {
    if (
        typeof value !== "object" ||
        value === null
    ) {
        return false;
    }

    const result =
        value as Partial<AssessmentResult>;

    return (
        typeof result.id === "string" &&
        typeof result.userId === "string" &&
        typeof result.category === "string" &&
        typeof result.score === "number" &&
        typeof result.total === "number" &&
        typeof result.percentage === "number" &&
        Array.isArray(result.questionIds) &&
        result.questionIds.every(
            (questionId) =>
                typeof questionId === "number"
        ) &&
        Array.isArray(result.answers) &&
        result.answers.every(
            (answer) =>
                typeof answer === "number"
        ) &&
        typeof result.completedAt === "string"
    );
}

function getAllResults():
    AssessmentResult[] {
    const data =
        localStorage.getItem(STORAGE_KEY);

    if (!data) {
        return [];
    }

    try {
        const parsedData: unknown =
            JSON.parse(data);

        if (!Array.isArray(parsedData)) {
            return [];
        }

        return parsedData.filter(
            isValidAssessmentResult
        );
    } catch {
        return [];
    }
}

function saveAllResults(
    results: AssessmentResult[]
): void {
    localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify(results)
    );
}

export function calculateScore(
    questions: Question[],
    answers: number[]
): number {
    return questions.reduce(
        (
            score,
            question,
            questionIndex
        ) => {
            if (
                answers[questionIndex] ===
                question.answer
            ) {
                return score + 1;
            }

            return score;
        },
        0
    );
}

export function saveAssessmentResult({
    userId,
    category,
    questions,
    answers,
}: {
    userId: string;
    category: string;
    questions: Question[];
    answers: number[];
}): AssessmentResult {
    const normalizedAnswers =
        questions.map(
            (_, questionIndex) =>
                answers[questionIndex] ?? -1
        );

    const questionIds =
        questions.map(
            (question) => question.id
        );

    const score = calculateScore(
        questions,
        normalizedAnswers
    );

    const total = questions.length;

    const percentage =
        total > 0
            ? Math.round(
                (score / total) * 100
            )
            : 0;

    const results = getAllResults();

    const result: AssessmentResult = {
        id: crypto.randomUUID(),
        userId,
        category,
        score,
        total,
        percentage,
        questionIds,
        answers: normalizedAnswers,
        completedAt:
            new Date().toISOString(),
    };

    results.push(result);

    saveAllResults(results);

    return result;
}

export function getUserAssessmentResults(
    userId: string
): AssessmentResult[] {
    return getAllResults()
        .filter(
            (result) =>
                result.userId === userId
        )
        .sort(
            (firstResult, secondResult) =>
                new Date(
                    firstResult.completedAt
                ).getTime() -
                new Date(
                    secondResult.completedAt
                ).getTime()
        );
}

export function getLatestAssessment(
    userId: string
): AssessmentResult | null {
    const results =
        getUserAssessmentResults(userId);

    if (results.length === 0) {
        return null;
    }

    return (
        results[results.length - 1] ??
        null
    );
}

export function getCareerReadiness(
    userId: string
): number {
    const latest =
        getLatestAssessment(userId);

    if (!latest) {
        return 0;
    }

    return latest.percentage;
}

export function clearAssessmentResults(
    userId?: string
): void {
    if (!userId) {
        localStorage.removeItem(
            STORAGE_KEY
        );

        return;
    }

    const remainingResults =
        getAllResults().filter(
            (result) =>
                result.userId !== userId
        );

    saveAllResults(remainingResults);
}