import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { getDashboard, type DashboardData } from '../../services/dashboardService';

export default function CollegeDashboard() {
    const { user } = useAuth();
    const nav = useNavigate();
    const [data, setData] = useState<DashboardData | null>(null);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        if (!user) return;
        void getDashboard()
            .then(setData)
            .catch((e) => setError(e instanceof Error ? e.message : 'Unable to load dashboard.'));
    }, [user]);

    if (!user) return null;
    if (!data && !error) return <div className="p-6 text-slate-500">Loading dashboard...</div>;

    const p = data?.profile;
    const a = data?.assessment;
    const coding = a?.coding;
    const latest = a?.recent_attempts?.[0];

    const cards = [
        ['PROFILE READINESS', `${data?.progress ? data.progress.resume >= 0 ? p?.profile_completion ?? 0 : 0 : 0}%`],
        ['ASSESSMENT', `${a?.latest_score ?? 0}%`],
        ['CODING', `${coding?.completed ? coding.percentage ?? 0 : 0}%`],
        ['PLACEMENT READINESS', `${data?.progress.placement ?? 0}%`],
    ];

    return (
        <div className="space-y-6">
            {error && <div className="rounded-xl border border-red-200 bg-red-50 p-4 text-red-700">{error}</div>}

            <div>
                <p className="text-sm font-semibold text-cyan-600">COLLEGE STUDENT WORKSPACE</p>
                <h1 className="mt-1 text-3xl font-bold">
                    Welcome back, {data?.user.full_name || user.full_name}
                </h1>
                <p className="mt-1 text-slate-600">
                    {p?.course || 'Degree not set'} · {p?.branch || 'Branch not set'} · Semester {p?.semester || 'N/A'}
                    {p?.target_role && ` · Target: ${p.target_role}`}
                </p>
            </div>

            <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
                {cards.map(([title, value]) => (
                    <div key={title} className="rounded-2xl border bg-white p-5 shadow-sm">
                        <p className="text-xs font-semibold text-slate-500">{title}</p>
                        <p className="mt-2 text-3xl font-bold text-slate-900">{value}</p>
                    </div>
                ))}
            </div>

            <div className="grid gap-4 lg:grid-cols-2">
                <section className="rounded-2xl border bg-white p-5">
                    <h2 className="text-xl font-bold">Career Recommendation</h2>
                    <p className="mt-3 text-2xl font-bold text-cyan-700">
                        {data?.career.recommended_role ?? 'Complete an assessment'}
                    </p>
                    <p className="mt-2 text-slate-600">
                        {data?.career.confidence != null
                            ? `${data.career.confidence}% confidence`
                            : 'Your recommendation will appear after a completed assessment.'}
                    </p>
                    {data?.career.skill_gaps.length ? (
                        <div className="mt-4">
                            <p className="font-semibold">Priority gaps</p>
                            <div className="mt-2 flex flex-wrap gap-2">
                                {data.career.skill_gaps.slice(0, 5).map((gap) => (
                                    <span key={gap} className="rounded-full bg-amber-50 px-3 py-1 text-sm text-amber-800">{gap}</span>
                                ))}
                            </div>
                        </div>
                    ) : null}
                </section>

                <section className="rounded-2xl border bg-white p-5">
                    <h2 className="text-xl font-bold">Recent Assessment</h2>
                    {latest ? (
                        <div className="mt-4 rounded-xl bg-slate-50 p-4">
                            <p className="font-semibold capitalize">{latest.assessment_type?.replaceAll('_', ' ')}</p>
                            <p className="mt-1 text-sm text-slate-500">
                                {latest.correct_answers}/{latest.total_questions} correct
                            </p>
                            <p className="mt-2 text-3xl font-bold text-cyan-700">{latest.percentage ?? 0}%</p>
                        </div>
                    ) : (
                        <p className="mt-3 text-slate-500">No completed assessment yet.</p>
                    )}
                    <button onClick={() => nav('/college_student/assessment')} className="mt-4 rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white">
                        {latest ? 'Take New Assessment' : 'Start Assessment'}
                    </button>
                </section>
            </div>

            <section className="rounded-2xl border bg-white p-5">
                <h2 className="text-xl font-bold">Next Steps</h2>
                <div className="mt-4 grid gap-3 md:grid-cols-3">
                    <Action title="Assessment Reports" on={() => nav('/college_student/assessment-reports')} />
                    <Action title="Skill Gap Analysis" on={() => nav('/college_student/skill-gap')} />
                    <Action title="Final Career Report" on={() => nav('/college_student/final-career-report')} />
                </div>
            </section>
        </div>
    );
}

function Action({ title, on }: { title: string; on: () => void }) {
    return <button onClick={on} className="rounded-xl bg-slate-50 p-4 text-left font-semibold hover:bg-cyan-50">{title} →</button>;
}
