import { useMemo, useState } from 'react';
import { Brain, ChevronRight, RotateCcw } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import {
    getCollegeProfile,
    getCollegeQuestions,
    isCollegeProfileReady,
    saveAssessmentAttempt,
    type AssessmentAttempt,
} from '../../services/collegeService';
import CollegeProfileRequired from './CollegeProfileRequired';

export default function SkillAssessment() {
    const { user } = useAuth();

    const id = user?.id || 'guest',
        p = getCollegeProfile(id);

    const [cat, setCat] = useState<string | null>(null);
    const [idx, setIdx] = useState(0);
    const [ans, setAns] = useState<number[]>([]);
    const [result, setResult] =
        useState<AssessmentAttempt | null>(null);

    const qs = useMemo(
        () =>
            cat
                ? getCollegeQuestions(p, cat)
                : [],
        [cat, p.degree, p.branch, p.semester]
    );

    if (!isCollegeProfileReady(p)) {
        return (
            <CollegeProfileRequired title="Academic profile required" />
        );
    }

    if (result) {
        return (
            <div className="mx-auto max-w-3xl rounded-2xl border bg-white p-6 text-center shadow-sm">
                <div className="text-5xl">🎉</div>

                <h1 className="mt-4 text-3xl font-bold">
                    Assessment Completed
                </h1>

                <p className="mt-2 text-slate-500">
                    {result.branch} · Semester {result.semester}{' '}
                    context saved with this attempt.
                </p>

                <div className="mt-6 grid gap-3 sm:grid-cols-3">
                    <Stat
                        t="Score"
                        v={`${result.score}/${result.total}`}
                    />

                    <Stat
                        t="Percentage"
                        v={`${result.percentage}%`}
                    />

                    <Stat
                        t="Performance"
                        v={
                            result.percentage >= 70
                                ? 'Strong'
                                : result.percentage >= 50
                                    ? 'Improving'
                                    : 'Needs Focus'
                        }
                    />
                </div>

                <div className="mt-6 grid gap-2 text-left sm:grid-cols-2">
                    {Object.entries(result.skillScores).map(
                        ([k, v]) => (
                            <div
                                key={k}
                                className="rounded-xl bg-slate-50 p-3"
                            >
                                <b>{k}</b>

                                <span className="float-right">
                                    {v}%
                                </span>
                            </div>
                        )
                    )}
                </div>

                <button
                    onClick={() => {
                        setCat(null);
                        setResult(null);
                        setIdx(0);
                        setAns([]);
                    }}
                    className="mx-auto mt-6 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white"
                >
                    <RotateCcw size={17} />
                    Continue Assessment Journey
                </button>
            </div>
        );
    }

    if (cat) {
        if (!qs.length) {
            return (
                <div className="rounded-2xl border bg-white p-8 text-center">
                    <h2 className="text-2xl font-bold">
                        Question bank is not available for this branch yet
                    </h2>

                    <p className="mt-2 text-slate-600">
                        Your profile remains unchanged. Choose Aptitude
                        or update the branch only if your saved profile
                        is incorrect.
                    </p>

                    <button
                        onClick={() => setCat(null)}
                        className="mt-4 rounded-xl border px-5 py-2.5 font-semibold"
                    >
                        Back
                    </button>
                </div>
            );
        }

        const q = qs[idx];

        return (
            <div className="mx-auto max-w-4xl space-y-5">
                <div>
                    <p className="font-semibold text-cyan-600">
                        {cat.toUpperCase()} ASSESSMENT
                    </p>

                    <h1 className="text-3xl font-bold">
                        {p.branch}
                    </h1>

                    <p className="text-slate-500">
                        Question {idx + 1} of {qs.length}
                    </p>
                </div>

                <div className="h-2 rounded-full bg-slate-200">
                    <div
                        className="h-2 rounded-full bg-cyan-600"
                        style={{
                            width: `${((idx + 1) / qs.length) * 100}%`,
                        }}
                    />
                </div>

                <section className="rounded-2xl border bg-white p-6 shadow-sm">
                    <h2 className="text-xl font-bold">
                        {q.question}
                    </h2>

                    <div className="mt-5 space-y-3">
                        {q.options.map((o, i) => (
                            <button
                                key={o}
                                onClick={() =>
                                    setAns((a) => {
                                        const n = [...a];
                                        n[idx] = i;
                                        return n;
                                    })
                                }
                                className={`w-full rounded-xl border p-4 text-left ${ans[idx] === i
                                        ? 'border-cyan-600 bg-cyan-50'
                                        : 'hover:bg-slate-50'
                                    }`}
                            >
                                {String.fromCharCode(65 + i)}. {o}
                            </button>
                        ))}
                    </div>

                    <button
                        disabled={ans[idx] === undefined}
                        onClick={() =>
                            idx < qs.length - 1
                                ? setIdx(idx + 1)
                                : setResult(
                                    saveAssessmentAttempt(
                                        id,
                                        cat,
                                        p,
                                        qs,
                                        ans
                                    )
                                )
                        }
                        className="mt-6 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white disabled:opacity-40"
                    >
                        {idx < qs.length - 1
                            ? 'Next Question'
                            : 'Submit Assessment'}

                        <ChevronRight size={17} />
                    </button>
                </section>
            </div>
        );
    }

    return (
        <div className="space-y-5">
            <div>
                <h1 className="text-3xl font-bold">
                    College Assessment
                </h1>

                <p className="mt-1 text-slate-600">
                    Questions adapt to {p.degree}, {p.branch},
                    semester {p.semester} and your career context.
                </p>
            </div>

            <div className="grid gap-4 md:grid-cols-3">
                {[
                    {
                        k: 'aptitude',
                        t: 'Aptitude & Reasoning',
                        d: 'Quantitative, logical and communication foundations.',
                    },
                    {
                        k: 'technical',
                        t: 'Branch Technical',
                        d: `Technical questions for ${p.branch}.`,
                    },
                    {
                        k: 'combined',
                        t: 'Placement Readiness',
                        d: 'Combined common and technical evidence.',
                    },
                ].map((x) => (
                    <button
                        key={x.k}
                        onClick={() => {
                            setCat(x.k);
                            setIdx(0);
                            setAns([]);
                        }}
                        className="rounded-2xl border bg-white p-5 text-left shadow-sm hover:border-cyan-500"
                    >
                        <Brain className="text-cyan-600" />

                        <h2 className="mt-4 text-xl font-bold">
                            {x.t}
                        </h2>

                        <p className="mt-2 text-sm text-slate-600">
                            {x.d}
                        </p>

                        <span className="mt-5 inline-flex items-center gap-1 font-semibold text-cyan-700">
                            Start Assessment
                            <ChevronRight size={16} />
                        </span>
                    </button>
                ))}
            </div>
        </div>
    );
}

function Stat({
    t,
    v,
}: {
    t: string;
    v: string;
}) {
    return (
        <div className="rounded-xl bg-slate-50 p-4">
            <p className="text-sm text-slate-500">
                {t}
            </p>

            <p className="mt-1 text-2xl font-bold">
                {v}
            </p>
        </div>
    );
}