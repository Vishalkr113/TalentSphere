import { useMemo, useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import {
    getProfessionalEvidence,
    professionalStats,
    roleSkills,
    saveProfessionalEvidence,
} from '../../services/professionalService';

type Kind =
    | 'assessment'
    | 'career'
    | 'resume'
    | 'interview'
    | 'job'
    | 'salary'
    | 'learning'
    | 'certificates'
    | 'achievements';

const titles: Record<Kind, string> = {
    assessment: 'Professional Skill Assessment',
    career: 'Career Growth & Promotion Readiness',
    resume: 'Resume Update Assistant',
    interview: 'Interview & Leadership Evaluation',
    job: 'Advanced Job Matching',
    salary: 'Salary Benchmark Insights',
    learning: 'Industry Trends & Learning Hub',
    certificates: 'Certification Suggestions',
    achievements: 'Growth Opportunity Analysis',
};

export default function ProfessionalEvidenceModule({
    kind,
}: {
    kind: Kind;
}) {
    const { user } = useAuth();

    const id = user?.id || 'guest';

    const [tick, setTick] = useState(0);

    const stats = useMemo(
        () =>
            professionalStats(
                id,
                user?.name || '',
                user?.email || ''
            ),
        [id, user?.name, user?.email, tick]
    );

    const [text, setText] = useState(stats.e.resumeText);
    const [company, setCompany] = useState('');
    const [role, setRole] = useState('');

    const update = (
        fn: (
            e: ReturnType<typeof getProfessionalEvidence>
        ) => void
    ) => {
        const e = getProfessionalEvidence(id);

        fn(e);

        saveProfessionalEvidence(id, e);
        setTick((x) => x + 1);
    };

    const missing = roleSkills(stats.p.targetRole).filter(
        (s) =>
            !stats.p.skills
                .toLowerCase()
                .includes(s.toLowerCase())
    );

    const assessment = () => {
        const qs = [
            'I can explain the core concepts used in my current role.',
            'I can solve unfamiliar work problems independently.',
            'I communicate decisions clearly to teammates.',
            'I can plan and prioritize work against deadlines.',
            'I actively learn skills relevant to my target role.',
        ];

        return (
            <div className="space-y-4">
                <p className="text-slate-600">
                    Complete a practical self-assessment. Results are
                    saved as evidence; no score is pre-filled.
                </p>

                {qs.map((q, i) => (
                    <button
                        key={q}
                        onClick={() => {
                            const score = [40, 55, 70, 85, 100][i];

                            update((e) =>
                                e.assessmentScores.push(score)
                            );
                        }}
                        className="block w-full rounded-xl border p-4 text-left hover:border-cyan-500"
                    >
                        {q}

                        <span className="float-right text-sm text-cyan-700">
                            Record evidence
                        </span>
                    </button>
                ))}

                <p className="font-semibold">
                    Current skill evidence: {stats.skill}%
                </p>
            </div>
        );
    };

    return (
        <div className="space-y-5">
            <div>
                <h1 className="text-3xl font-bold text-slate-900">
                    {titles[kind]}
                </h1>

                <p className="mt-1 text-slate-600">
                    Personalized from your saved professional profile
                    and completed activity.
                </p>
            </div>

            <section className="rounded-2xl border bg-white p-6 shadow-sm">
                {kind === 'assessment' ? (
                    assessment()
                ) : kind === 'career' ? (
                    <div className="grid gap-4 md:grid-cols-3">
                        <Metric
                            n="Promotion readiness"
                            v={stats.promotion}
                        />
                        <Metric
                            n="Career growth score"
                            v={stats.career}
                        />
                        <Metric
                            n="Skill evidence"
                            v={stats.skill}
                        />

                        <div className="rounded-xl bg-slate-50 p-4 md:col-span-3">
                            <b>Priority gaps:</b>{' '}
                            {missing.length
                                ? missing.join(', ')
                                : 'No target-role gap detected from saved skills.'}
                        </div>
                    </div>
                ) : kind === 'resume' ? (
                    <div className="space-y-4">
                        <textarea
                            value={text}
                            onChange={(e) =>
                                setText(e.target.value)
                            }
                            className="min-h-64 w-full rounded-xl border p-4"
                            placeholder="Paste or write your professional resume content..."
                        />

                        <button
                            onClick={() =>
                                update((e) => (e.resumeText = text))
                            }
                            className="rounded-xl bg-cyan-600 px-5 py-3 font-semibold text-white"
                        >
                            Save & analyze resume
                        </button>

                        <p>
                            Evidence-based resume score:{' '}
                            <b>{stats.resume}%</b>
                        </p>
                    </div>
                ) : kind === 'interview' ? (
                    <div className="space-y-4">
                        <p>
                            Target role:{' '}
                            <b>
                                {stats.p.targetRole ||
                                    'Not selected in profile'}
                            </b>
                        </p>

                        <p>
                            Practice prompt: Explain a difficult work
                            problem, your action, measurable result, and
                            what you learned.
                        </p>

                        {[40, 60, 80, 100].map((v) => (
                            <button
                                key={v}
                                onClick={() =>
                                    update((e) =>
                                        e.interviewScores.push(v)
                                    )
                                }
                                className="mr-3 rounded-xl border px-4 py-2"
                            >
                                Record {v}% evidence
                            </button>
                        ))}

                        <p>
                            Interview/leadership evidence:{' '}
                            <b>{stats.interview}%</b>
                        </p>
                    </div>
                ) : kind === 'job' ? (
                    <div className="space-y-4">
                        <p>
                            Matches use target role, skills and saved
                            application evidence. No fake company
                            recommendations are preloaded.
                        </p>

                        <div className="grid gap-3 md:grid-cols-2">
                            <input
                                className="rounded-xl border p-3"
                                value={company}
                                onChange={(e) =>
                                    setCompany(e.target.value)
                                }
                                placeholder="Company"
                            />

                            <input
                                className="rounded-xl border p-3"
                                value={role}
                                onChange={(e) =>
                                    setRole(e.target.value)
                                }
                                placeholder="Role"
                            />
                        </div>

                        <button
                            onClick={() => {
                                if (company && role) {
                                    update((e) =>
                                        e.applications.push({
                                            company,
                                            role,
                                            status: 'Interested',
                                        })
                                    );
                                }

                                setCompany('');
                                setRole('');
                            }}
                            className="rounded-xl bg-cyan-600 px-5 py-3 text-white"
                        >
                            Track opportunity
                        </button>

                        {stats.e.applications.map((a, i) => (
                            <div
                                key={i}
                                className="rounded-xl bg-slate-50 p-3"
                            >
                                {a.company} · {a.role} · {a.status}
                            </div>
                        ))}
                    </div>
                ) : kind === 'salary' ? (
                    <div className="space-y-3">
                        <p>
                            Salary insights require a real benchmark
                            API/data source. The app will not invent ₹12
                            LPA or a 32% hike.
                        </p>

                        <p>
                            Saved expected salary:{' '}
                            <b>
                                {stats.p.expectedSalary ||
                                    'Not provided'}
                            </b>
                        </p>

                        <p>
                            Current role:{' '}
                            <b>
                                {stats.p.designation ||
                                    'Not provided'}
                            </b>{' '}
                            · Experience:{' '}
                            <b>
                                {stats.p.experience ||
                                    'Not provided'}
                            </b>
                        </p>
                    </div>
                ) : kind === 'learning' ? (
                    <div className="space-y-3">
                        <p>
                            Recommended focus:{' '}
                            <b>
                                {missing[0] ||
                                    'Keep strengthening your current role skills'}
                            </b>
                        </p>

                        {[
                            'Industry trend review',
                            'Target-role skill practice',
                            'Case study / project evidence',
                            'Communication practice',
                        ].map((x) => (
                            <button
                                key={x}
                                onClick={() =>
                                    update((e) => {
                                        if (
                                            !e.learningCompleted.includes(x)
                                        ) {
                                            e.learningCompleted.push(x);
                                        }
                                    })
                                }
                                className="block w-full rounded-xl border p-3 text-left"
                            >
                                {stats.e.learningCompleted.includes(x)
                                    ? '✓ '
                                    : ''}
                                {x}
                            </button>
                        ))}

                        <p>
                            Learning progress:{' '}
                            <b>{stats.learning}%</b>
                        </p>
                    </div>
                ) : kind === 'certificates' ? (
                    <div className="space-y-3">
                        <p>
                            Suggested certification area:{' '}
                            <b>
                                {missing[0] ||
                                    stats.p.industry ||
                                    'Complete your profile for a suggestion'}
                            </b>
                        </p>

                        <input
                            className="w-full rounded-xl border p-3"
                            placeholder="Certification completed"
                            onKeyDown={(ev) => {
                                if (
                                    ev.key === 'Enter' &&
                                    ev.currentTarget.value
                                ) {
                                    const v = ev.currentTarget.value;

                                    update((e) =>
                                        e.certifications.push(v)
                                    );

                                    ev.currentTarget.value = '';
                                }
                            }}
                        />

                        {stats.e.certifications.map((x, i) => (
                            <p
                                key={i}
                                className="rounded-xl bg-slate-50 p-3"
                            >
                                ✓ {x}
                            </p>
                        ))}
                    </div>
                ) : (
                    <div className="grid gap-4 md:grid-cols-2">
                        <Metric
                            n="Career evidence"
                            v={stats.career}
                        />

                        <Metric
                            n="Promotion readiness"
                            v={stats.promotion}
                        />

                        <p className="rounded-xl bg-slate-50 p-4 md:col-span-2">
                            Growth opportunity:{' '}
                            {missing.length
                                ? `Build evidence in ${missing[0]} and reassess.`
                                : 'Continue learning and record measurable outcomes.'}
                        </p>
                    </div>
                )}
            </section>
        </div>
    );
}

function Metric({
    n,
    v,
}: {
    n: string;
    v: number;
}) {
    return (
        <div className="rounded-xl bg-slate-50 p-5">
            <p className="text-sm text-slate-500">
                {n}
            </p>

            <p className="mt-2 text-3xl font-bold">
                {v}%
            </p>

            <div className="mt-3 h-2 rounded bg-slate-200">
                <div
                    className="h-2 rounded bg-cyan-600"
                    style={{ width: `${v}%` }}
                />
            </div>
        </div>
    );
}