import { useMemo, useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import {
    getCollegeProfile,
    getSkillGap,
    isCollegeProfileReady,
    savePracticeAttempt,
} from '../../services/collegeService';
import { practiceQuestions } from '../../data/college/practice/collegePracticeQuestions';
import CollegeProfileRequired from './CollegeProfileRequired';

export default function CodingAssessment() {
    const { user } = useAuth();

    const id = user?.id || 'guest',
        p = getCollegeProfile(id),
        gaps = getSkillGap(id);

    const recommended = gaps[0]?.skill;

    const questions = useMemo(
        () =>
            [...practiceQuestions].sort(
                (a, b) =>
                    Number(
                        b.skill.toLowerCase() === recommended?.toLowerCase()
                    ) -
                    Number(
                        a.skill.toLowerCase() === recommended?.toLowerCase()
                    )
            ),
        [recommended]
    );

    const [i, setI] = useState(0),
        [answer, setAnswer] = useState<number | null>(null),
        [result, setResult] = useState<boolean | null>(null);

    if (!isCollegeProfileReady(p)) {
        return <CollegeProfileRequired />;
    }

    const q = questions[i % questions.length];

    const submit = () => {
        if (answer === null) return;

        const ok = answer === q.answer;

        setResult(ok);

        savePracticeAttempt(id, {
            id: crypto.randomUUID(),
            questionId: q.id,
            skill: q.skill,
            correct: ok,
            completedAt: new Date().toISOString(),
        });
    };

    return (
        <div className="space-y-5">
            <div>
                <h1 className="text-3xl font-bold">
                    Coding & Skill Practice
                </h1>

                <p className="mt-1 text-slate-600">
                    Answer real practice questions. Every submitted result
                    updates your practice evidence.
                </p>
            </div>

            {recommended && (
                <section className="rounded-2xl border border-cyan-200 bg-cyan-50 p-5">
                    <p className="text-sm font-semibold text-cyan-700">
                        RECOMMENDED FOR YOU
                    </p>

                    <h2 className="mt-1 text-xl font-bold">
                        {recommended} Fundamentals
                    </h2>

                    <p className="mt-1 text-slate-600">
                        Based on your current assessment or resume evidence
                        gap.
                    </p>
                </section>
            )}

            <section className="rounded-2xl border bg-white p-6">
                <p className="text-sm font-semibold text-cyan-600">
                    PRACTICE · {q.skill}
                </p>

                <h2 className="mt-2 text-xl font-bold">
                    {q.question}
                </h2>

                <div className="mt-5 space-y-3">
                    {q.options.map((o, n) => (
                        <button
                            key={o}
                            onClick={() => {
                                setAnswer(n);
                                setResult(null);
                            }}
                            className={`w-full rounded-xl border p-4 text-left ${answer === n
                                    ? 'border-cyan-600 bg-cyan-50'
                                    : ''
                                }`}
                        >
                            {String.fromCharCode(65 + n)}. {o}
                        </button>
                    ))}
                </div>

                <div className="mt-5 flex gap-3">
                    <button
                        disabled={answer === null}
                        onClick={submit}
                        className="rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white disabled:opacity-40"
                    >
                        Submit Answer
                    </button>

                    {result !== null && (
                        <button
                            onClick={() => {
                                setI((x) => x + 1);
                                setAnswer(null);
                                setResult(null);
                            }}
                            className="rounded-xl border px-5 py-2.5 font-semibold"
                        >
                            Next Practice
                        </button>
                    )}
                </div>

                {result !== null && (
                    <p
                        className={`mt-4 rounded-xl p-4 ${result
                                ? 'bg-green-50 text-green-800'
                                : 'bg-amber-50 text-amber-800'
                            }`}
                    >
                        {result
                            ? 'Correct. This practice result was saved.'
                            : `Needs improvement. Correct answer: ${q.options[q.answer]
                            }. Review ${q.topic} and try the next question.`}
                    </p>
                )}
            </section>
        </div>
    );
}