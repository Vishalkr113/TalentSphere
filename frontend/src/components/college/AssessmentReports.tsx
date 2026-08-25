import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { getAssessmentHistory, getAssessmentResult } from '../../services/dashboardService';

type HistoryItem = Awaited<ReturnType<typeof getAssessmentHistory>>['attempts'][number];
type Result = Awaited<ReturnType<typeof getAssessmentResult>>;

export default function AssessmentReports() {
    const nav = useNavigate();
    const [history, setHistory] = useState<HistoryItem[]>([]);
    const [latestResult, setLatestResult] = useState<Result | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        let cancelled = false;
        const load = async () => {
            try {
                const response = await getAssessmentHistory();
                const completed = response.attempts.filter((x) => x.status === 'completed');
                if (!cancelled) setHistory(completed);
                if (completed.length) {
                    const result = await getAssessmentResult(completed[0].attempt_id);
                    if (!cancelled) setLatestResult(result);
                }
            } catch (e) {
                if (!cancelled) setError(e instanceof Error ? e.message : 'Unable to load assessment reports.');
            } finally {
                if (!cancelled) setLoading(false);
            }
        };
        void load();
        return () => { cancelled = true; };
    }, []);

    if (loading) return <div className="p-6 text-slate-500">Loading assessment reports...</div>;
    if (error) return <div className="rounded-xl border border-red-200 bg-red-50 p-5 text-red-700">{error}</div>;

    const avg = history.length
        ? Math.round(history.reduce((sum, x) => sum + (x.percentage ?? 0), 0) / history.length)
        : 0;

    return (
        <div className="space-y-6">
            <div>
                <h1 className="text-3xl font-bold">Assessment Reports</h1>
                <p className="mt-1 text-slate-600">Backend-saved assessment history and result evidence.</p>
            </div>

            <div className="grid gap-3 sm:grid-cols-3">
                <Stat title="Average" value={`${avg}%`} />
                <Stat title="Completed" value={String(history.length)} />
                <Stat title="Latest" value={`${latestResult?.percentage ?? 0}%`} />
            </div>

            {latestResult ? (
                <section className="rounded-2xl border bg-white p-6">
                    <h2 className="text-xl font-bold">Latest Result</h2>
                    <div className="mt-4 grid gap-4 md:grid-cols-3">
                        <Stat title="Assessment" value={latestResult.assessment_type.replaceAll('_', ' ')} />
                        <Stat title="Score" value={`${latestResult.correct_answers}/${latestResult.total_questions}`} />
                        <Stat title="Grade" value={latestResult.grade ?? '-'} />
                    </div>

                    <div className="mt-6 grid gap-5 md:grid-cols-2">
                        <List title="Strengths" items={latestResult.strengths} />
                        <List title="Improvement Areas" items={latestResult.weaknesses} />
                    </div>

                    {latestResult.recommendation && (
                        <div className="mt-6 rounded-xl bg-cyan-50 p-5">
                            <p className="font-semibold">Recommendation</p>
                            <p className="mt-2 text-slate-700">{latestResult.recommendation.career}</p>
                        </div>
                    )}
                </section>
            ) : (
                <Empty on={() => nav('/college_student/assessment')} />
            )}

            <section className="rounded-2xl border bg-white p-6">
                <h2 className="text-xl font-bold">Assessment History</h2>
                <div className="mt-4 space-y-3">
                    {history.length ? [...history].map((item) => (
                        <div key={item.attempt_id} className="flex flex-wrap items-center justify-between gap-3 rounded-xl bg-slate-50 p-4">
                            <div>
                                <p className="font-semibold capitalize">{item.assessment_type.replaceAll('_', ' ')}</p>
                                <p className="text-sm text-slate-500">{item.correct_answers}/{item.total_questions} correct · {new Date(item.completed_at || item.started_at).toLocaleDateString()}</p>
                            </div>
                            <p className="text-2xl font-bold text-cyan-700">{item.percentage ?? 0}%</p>
                        </div>
                    )) : <p className="text-slate-500">No completed assessment yet.</p>}
                </div>
            </section>
        </div>
    );
}

function Stat({ title, value }: { title: string; value: string }) {
    return <div className="rounded-2xl border bg-white p-4"><p className="text-xs text-slate-500">{title}</p><p className="mt-1 text-xl font-bold">{value}</p></div>;
}

function List({ title, items }: { title: string; items: string[] }) {
    return <div><h3 className="font-semibold">{title}</h3><ul className="mt-3 space-y-2">{items.length ? items.map((x, i) => <li key={`${x}-${i}`} className="rounded-xl bg-slate-50 p-3 text-sm">{x}</li>) : <li className="text-sm text-slate-500">No data recorded.</li>}</ul></div>;
}

function Empty({ on }: { on: () => void }) {
    return <div className="rounded-2xl border bg-white p-8 text-center"><h2 className="text-xl font-bold">No assessment evidence yet</h2><p className="mt-2 text-slate-500">Complete an assessment to generate a report.</p><button onClick={on} className="mt-4 rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white">Start Assessment</button></div>;
}
