import { useAuth } from '../../contexts/AuthContext';
import {
  getCurrentContextAttempts,
  getCollegeProfile,
  isCollegeProfileReady,
} from '../../services/collegeService';
import { useNavigate } from 'react-router-dom';
import CollegeProfileRequired from './CollegeProfileRequired';

export default function AssessmentReports() {
  const { user } = useAuth();
  const nav = useNavigate();

  const id = user?.id || 'guest';
  const p = getCollegeProfile(id);
  const a = getCurrentContextAttempts(id, p);

  const avg = a.length
    ? Math.round(a.reduce((s, x) => s + x.percentage, 0) / a.length)
    : 0;

  const latest = a.at(-1);

  if (!isCollegeProfileReady(p)) {
    return <CollegeProfileRequired />;
  }

  return (
    <div className="space-y-5">
      <div>
        <h1 className="text-3xl font-bold">Assessment Reports</h1>
        <p className="mt-1 text-slate-600">
          Attempt history and evidence-based skill breakdown. Old branch
          context remains preserved.
        </p>
      </div>

      <div className="grid gap-3 sm:grid-cols-4">
        <S t="Average" v={`${avg}%`} />
        <S t="Completed" v={String(a.length)} />
        <S t="Current Branch" v={p.branch} />
        <S
          t="Readiness"
          v={
            avg >= 70
              ? 'Good'
              : avg >= 50
              ? 'Improving'
              : 'Needs Focus'
          }
        />
      </div>

      {!a.length ? (
        <Empty on={() => nav('/college-student/assessment')} />
      ) : (
        <>
          <section className="rounded-2xl border bg-white p-5">
            <h2 className="text-xl font-bold">
              Latest Skill Evidence
            </h2>

            <div className="mt-4 grid gap-3 md:grid-cols-2">
              {Object.entries(latest?.skillScores || {})
                .sort((x, y) => y[1] - x[1])
                .map(([k, v]) => (
                  <div key={k}>
                    <div className="flex justify-between text-sm">
                      <b>{k}</b>
                      <span>{v}%</span>
                    </div>

                    <div className="mt-1 h-2 rounded bg-slate-100">
                      <div
                        className="h-2 rounded bg-cyan-600"
                        style={{ width: `${v}%` }}
                      />
                    </div>
                  </div>
                ))}
            </div>
          </section>

          <section className="rounded-2xl border bg-white p-5">
            <h2 className="text-xl font-bold">
              Assessment History
            </h2>

            <div className="mt-4 space-y-3">
              {[...a].reverse().map((x, i) => (
                <div
                  key={x.id}
                  className="flex flex-wrap items-center justify-between gap-3 rounded-xl bg-slate-50 p-4"
                >
                  <div>
                    <b className="capitalize">
                      {x.category} Assessment{' '}
                      {i === 0 && '· Latest'}
                    </b>

                    <p className="text-sm text-slate-500">
                      {x.degree} · {x.branch} · Semester{' '}
                      {x.semester || 'N/A'} ·{' '}
                      {new Date(
                        x.completedAt
                      ).toLocaleDateString()}
                    </p>
                  </div>

                  <div className="text-2xl font-bold text-cyan-700">
                    {x.percentage}%
                  </div>
                </div>
              ))}
            </div>

            <button
              onClick={() =>
                nav('/college-student/assessment')
              }
              className="mt-4 rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white"
            >
              Retake / New Assessment
            </button>
          </section>
        </>
      )}
    </div>
  );
}

function S({
  t,
  v,
}: {
  t: string;
  v: string;
}) {
  return (
    <div className="rounded-2xl border bg-white p-4">
      <p className="text-xs text-slate-500">{t}</p>
      <p className="mt-1 text-xl font-bold">{v}</p>
    </div>
  );
}

function Empty({
  on,
}: {
  on: () => void;
}) {
  return (
    <div className="rounded-2xl border bg-white p-8 text-center">
      <h2 className="text-xl font-bold">
        No assessment evidence yet
      </h2>

      <p className="mt-2 text-slate-500">
        Complete an assessment to generate real reports.
      </p>

      <button
        onClick={on}
        className="mt-4 rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white"
      >
        Start Assessment
      </button>
    </div>
  );
}