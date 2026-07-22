import { useMemo, useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import {
    getCollegeProfile,
    getResume,
    getSkillGap,
    isCollegeProfileReady,
    saveInterviewResult,
} from '../../services/collegeService';
import CollegeProfileRequired from './CollegeProfileRequired';

export default function MockInterview() {
    const { user } = useAuth();

    const id = user?.id || 'guest',
        p = getCollegeProfile(id),
        r = getResume(id),
        gap = getSkillGap(id)[0];

    const qs = useMemo(
        () => [
            'Tell me about yourself and your current career goal.',
            r.projects
                ? `Explain one project from your resume and make your personal contribution clear.`
                : 'Describe a project you want to build and the problem it should solve.',
            gap
                ? `Your current evidence shows a priority gap in ${gap.skill}. Explain the fundamentals you know and how you will improve.`
                : 'Describe a technical challenge you faced and how you approached it.',
            `Why are you interested in ${p.targetRole || 'your target role'
            }?`,
        ],
        [p.targetRole, r.projects, gap?.skill]
    );

    const [i, setI] = useState(0),
        [text, setText] = useState(''),
        [feedback, setFeedback] = useState('');

    if (!isCollegeProfileReady(p)) {
        return <CollegeProfileRequired />;
    }

    const review = () => {
        const words = text
            .trim()
            .split(/\s+/)
            .filter(Boolean).length,
            score = Math.min(
                100,
                Math.round((words / 60) * 100)
            );

        saveInterviewResult(id, {
            id: crypto.randomUUID(),
            score,
            date: new Date().toISOString(),
            role: p.targetRole,
            question: qs[i],
            wordCount: words,
        });

        setFeedback(
            words < 25
                ? 'Answer is too brief. Add context, your action and a concrete outcome.'
                : words < 60
                    ? 'Good start. Improve structure using Situation → Action → Outcome.'
                    : 'Strong detail. Keep the answer concise and make your personal contribution explicit.'
        );
    };

    return (
        <div className="space-y-5">
            <div>
                <h1 className="text-3xl font-bold">
                    Mock Interview
                </h1>

                <p className="mt-1 text-slate-600">
                    Questions use your target role, resume and current
                    evidence gap. Feedback checks answer completeness; it
                    is not a hiring prediction.
                </p>
            </div>

            <section className="rounded-2xl border bg-white p-6">
                <p className="text-sm font-semibold text-cyan-600">
                    QUESTION {i + 1}/{qs.length}
                </p>

                <h2 className="mt-2 text-xl font-bold">
                    {qs[i]}
                </h2>

                <textarea
                    rows={8}
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    className="mt-5 w-full rounded-xl border p-4"
                    placeholder="Type your answer..."
                />

                <div className="mt-4 flex gap-3">
                    <button
                        disabled={!text.trim()}
                        onClick={review}
                        className="rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white disabled:opacity-40"
                    >
                        Get Feedback
                    </button>

                    <button
                        onClick={() => {
                            setI((i + 1) % qs.length);
                            setText('');
                            setFeedback('');
                        }}
                        className="rounded-xl border px-5 py-2.5 font-semibold"
                    >
                        Next Question
                    </button>
                </div>

                {feedback && (
                    <p className="mt-4 rounded-xl bg-cyan-50 p-4 text-cyan-900">
                        {feedback}
                    </p>
                )}
            </section>
        </div>
    );
}