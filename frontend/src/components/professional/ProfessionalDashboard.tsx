import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { getDashboard, type DashboardData } from '../../services/dashboardService';

export default function ProfessionalDashboard() {
    const { user } = useAuth();
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
    const assessment = data?.assessment.professional;

    return (
        <div className="space-y-4">
            {error && <div className="rounded-xl border border-red-200 bg-red-50 p-4 text-red-700">{error}</div>}

            <div className="rounded-2xl bg-gradient-to-r from-cyan-600 to-blue-700 p-5 text-white">
                <p className="text-sm font-semibold uppercase tracking-wider text-cyan-100">Working Professional Workspace</p>
                <h1 className="mt-2 text-3xl font-bold">Welcome, {data?.user.full_name || user.full_name} </h1>
                <p className="mt-2 text-cyan-100">
                    {p?.job_title || 'Complete your professional profile'}
                    {p?.company_name ? ` at ${p.company_name}` : ''}
                </p>
            </div>

            <div className="grid gap-3 md:grid-cols-3">
                <Metric title="Profile readiness" value={`${p?.profile_completion ?? 0}%`} />
                <Metric title="Skill assessment" value={`${assessment?.completed ? assessment.percentage ?? 0 : 0}%`} />
                <Metric title="Career readiness" value={`${data?.progress.placement ?? 0}%`} />
            </div>

            <div className="grid gap-5 lg:grid-cols-2">
                <section className="rounded-xl border bg-white p-5">
                    <h2 className="text-xl font-bold">Career Recommendation</h2>
                    <p className="mt-3 text-2xl font-bold text-cyan-700">
                        {data?.career.recommended_role ?? p?.target_role ?? 'Select a target role'}
                    </p>
                    <p className="mt-2 text-slate-600">
                        {data?.career.confidence != null
                            ? `${data.career.confidence}% confidence based on your latest evidence.`
                            : 'Complete the professional skill assessment to generate evidence.'}
                    </p>
                    {data?.career.skill_gaps.length ? (
                        <div className="mt-4">
                            <p className="font-semibold">Priority growth gaps</p>
                            <p className="mt-2 text-slate-600">{data.career.skill_gaps.slice(0, 5).join(' · ')}</p>
                        </div>
                    ) : null}
                </section>

                <section className="rounded-xl border bg-white p-5">
                    <h2 className="text-xl font-bold">Next Best Action</h2>
                    <p className="mt-3 text-slate-600">
                        {!p?.target_role
                            ? 'Select a target role in your profile.'
                            : !assessment?.completed
                                ? 'Complete the professional skill assessment.'
                                : data?.career.skill_gaps[0]
                                    ? `Build evidence in ${data.career.skill_gaps[0]}.`
                                    : 'Keep building measurable evidence for your target role.'}
                    </p>
                    <Link to="/working_professional/skill-assessment" className="mt-5 inline-block rounded-xl bg-cyan-600 px-5 py-3 font-semibold text-white">
                        {assessment?.completed ? 'Retake Skill Assessment' : 'Take Skill Assessment'}
                    </Link>
                </section>
            </div>

            <section className="rounded-xl border bg-white p-5">
                <h2 className="text-xl font-bold">Recent Assessment Activity</h2>
                <div className="mt-4 space-y-3">
                    {data?.assessment.recent_attempts.length ? data.assessment.recent_attempts.slice(0, 5).map((item) => (
                        <div key={item.attempt_id} className="flex flex-wrap items-center justify-between gap-3 rounded-xl bg-slate-50 p-4">
                            <div>
                                <p className="font-semibold capitalize">{item.assessment_type?.replaceAll('_', ' ')}</p>
                                <p className="text-sm text-slate-500">{item.correct_answers}/{item.total_questions} correct</p>
                            </div>
                            <p className="text-2xl font-bold text-cyan-700">{item.percentage ?? 0}%</p>
                        </div>
                    )) : <p className="text-slate-500">No completed assessment yet.</p>}
                </div>
            </section>
        </div>
    );
}

function Metric({ title, value }: { title: string; value: string }) {
    return <div className="rounded-xl border bg-white p-4 shadow-sm"><p className="text-slate-500">{title}</p><p className="mt-2 text-3xl font-bold">{value}</p></div>;
}
