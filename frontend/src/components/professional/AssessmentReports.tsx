import { useEffect, useMemo, useState, type ReactNode } from 'react';
import { BarChart3, CheckCircle2, Clock3, FileText } from 'lucide-react';
import { getAssessmentHistory, getAssessmentResult, type AssessmentHistoryItem } from '../../services/dashboardService';

const PROFESSIONAL_TYPES = new Set([
  'professional_skill',
  'professional_common',
  'professional_technical',
  'professional_dsa',
  'professional_situational',
]);

export default function ProfessionalAssessmentReports() {
  const [attempts, setAttempts] = useState<AssessmentHistoryItem[]>([]);
  const [latest, setLatest] = useState<any | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        const response = await getAssessmentHistory();
        const completed = response.attempts.filter(
          (item) => item.status === 'completed' && PROFESSIONAL_TYPES.has(item.assessment_type),
        );
        if (cancelled) return;
        setAttempts(completed);
        if (completed[0]) {
          try {
            const result = await getAssessmentResult(completed[0].attempt_id);
            if (!cancelled) setLatest(result);
          } catch {
            if (!cancelled) setLatest(null);
          }
        }
      } catch (e) {
        if (!cancelled) setError(e instanceof Error ? e.message : 'Unable to load assessment reports.');
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    return () => { cancelled = true; };
  }, []);

  const average = useMemo(
    () => attempts.length ? Math.round(attempts.reduce((sum, item) => sum + item.percentage, 0) / attempts.length) : 0,
    [attempts],
  );

  if (loading) return <div className="text-sm text-slate-500">Loading assessment reports...</div>;
  if (error) return <div className="rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-700">{error}</div>;

  return (
    <div className="space-y-5">
      <div>
        <p className="text-sm font-semibold text-cyan-600">ASSESSMENT REPORTS</p>
        <h1 className="mt-1 text-2xl font-bold text-slate-900">Professional Assessment Reports</h1>
        <p className="mt-1 text-sm text-slate-500">Only submitted professional assessments are included here.</p>
      </div>

      <div className="grid gap-3 sm:grid-cols-3">
        <Stat icon={<BarChart3 size={17} />} label="Average score" value={`${average}%`} />
        <Stat icon={<CheckCircle2 size={17} />} label="Completed" value={String(attempts.length)} />
        <Stat icon={<Clock3 size={17} />} label="Latest" value={`${latest?.percentage ?? 0}%`} />
      </div>

      {latest ? (
        <section className="rounded-2xl border bg-white p-5 shadow-sm">
          <div className="flex items-center gap-2">
            <FileText size={19} className="text-cyan-600" />
            <h2 className="text-lg font-bold">Latest Submitted Result</h2>
          </div>
          <div className="mt-4 grid gap-3 sm:grid-cols-3">
            <Stat label="Assessment" value={latest.assessment_type?.replaceAll('_', ' ') ?? '-'} />
            <Stat label="Score" value={`${latest.correct_answers ?? 0}/${latest.total_questions ?? 0}`} />
            <Stat label="Grade" value={latest.grade ?? '-'} />
          </div>
          <div className="mt-4 grid gap-4 md:grid-cols-2">
            <ResultList title="Strengths" items={latest.strengths ?? []} />
            <ResultList title="Improvement areas" items={latest.weaknesses ?? []} />
          </div>
        </section>
      ) : (
        <section className="rounded-2xl border bg-white p-6 text-center shadow-sm">
          <h2 className="font-bold text-slate-900">No submitted professional assessment yet</h2>
          <p className="mt-1 text-sm text-slate-500">Complete and submit an assessment to generate a report.</p>
        </section>
      )}

      <section className="rounded-2xl border bg-white p-5 shadow-sm">
        <h2 className="text-lg font-bold">Assessment History</h2>
        <div className="mt-3 space-y-2">
          {attempts.length ? attempts.map((item) => (
            <div key={item.attempt_id} className="flex flex-wrap items-center justify-between gap-3 rounded-xl bg-slate-50 px-4 py-3">
              <div>
                <p className="font-semibold capitalize">{item.assessment_type.replaceAll('_', ' ')}</p>
                <p className="text-xs text-slate-500">{item.correct_answers}/{item.total_questions} correct · {new Date(item.completed_at || item.started_at).toLocaleDateString()}</p>
              </div>
              <p className="font-bold text-cyan-700">{item.percentage}%</p>
            </div>
          )) : <p className="text-sm text-slate-500">No completed professional assessments.</p>}
        </div>
      </section>
    </div>
  );
}

function Stat({ label, value, icon }: { label: string; value: string; icon?: ReactNode }) {
  return <div className="rounded-xl border bg-white p-3"><div className="flex items-center gap-2 text-xs text-slate-500">{icon}{label}</div><p className="mt-1 text-xl font-bold text-slate-900 capitalize">{value}</p></div>;
}

function ResultList({ title, items }: { title: string; items: string[] }) {
  return <div><h3 className="text-sm font-semibold">{title}</h3><div className="mt-2 space-y-1.5">{items.length ? items.map((x, i) => <p key={`${x}-${i}`} className="rounded-lg bg-slate-50 px-3 py-2 text-sm">{x}</p>) : <p className="text-sm text-slate-500">No data recorded.</p>}</div></div>;
}
