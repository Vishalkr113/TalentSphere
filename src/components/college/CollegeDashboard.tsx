import { useAuth } from '../../contexts/AuthContext';
import {
    getCollegeProfile,
    getCollegeProfileCompletion,
    getCollegeStats,
    getSkillGap,
    isCollegeProfileReady,
} from '../../services/collegeService';
import { useNavigate } from 'react-router-dom';
import CollegeProfileRequired from './CollegeProfileRequired';

export default function CollegeDashboard() {
    const { user } = useAuth();
    const nav = useNavigate();

    const id = user?.id || 'guest',
        p = getCollegeProfile(id),
        s = getCollegeStats(id),
        g = getSkillGap(id),
        completion = getCollegeProfileCompletion(p);

    if (!isCollegeProfileReady(p)) {
        return (
            <div className="space-y-5">
                <div>
                    <h1 className="text-3xl font-bold">
                        Welcome, {p.fullName || user?.name || 'College Student'} 👋
                    </h1>

                    <p className="mt-1 text-slate-600">
                        Build your placement journey from one connected College workspace.
                    </p>
                </div>

                <CollegeProfileRequired />
            </div>
        );
    }

    return (
        <div className="space-y-5">
            <div>
                <p className="text-sm font-semibold text-cyan-600">
                    COLLEGE STUDENT WORKSPACE
                </p>

                <h1 className="mt-1 text-3xl font-bold">
                    Welcome back, {p.fullName || user?.name || 'College Student'} 👋
                </h1>

                <p className="mt-1 text-slate-600">
                    {p.degree} · {p.branch} · Semester {p.semester}
                    {p.targetRole && ` · Target: ${p.targetRole}`}
                </p>
            </div>

            <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
                <Card
                    t="PROFILE READINESS"
                    v={`${completion}%`}
                />
                <Card
                    t="PLACEMENT READINESS"
                    v={`${s.readiness}%`}
                />
                <Card
                    t="ASSESSMENT AVERAGE"
                    v={`${s.assessment}%`}
                />
                <Card
                    t="RESUME SCORE"
                    v={`${s.resume.resumeScore}%`}
                />
            </div>

            <div className="grid gap-4 lg:grid-cols-2">
                <section className="rounded-2xl border bg-white p-5">
                    <h2 className="text-xl font-bold">
                        Priority Skill Gaps
                    </h2>

                    <div className="mt-3 space-y-2">
                        {g.slice(0, 4).map((x) => (
                            <div
                                key={x.skill}
                                className="flex justify-between rounded-xl bg-slate-50 p-3"
                            >
                                <div>
                                    <b>{x.skill}</b>
                                    <p className="text-xs text-slate-500">
                                        {x.source}
                                    </p>
                                </div>

                                <span className="text-amber-700">
                                    {x.score
                                        ? `${x.score}% evidence`
                                        : 'Evidence missing'}
                                </span>
                            </div>
                        ))}

                        {!g.length && (
                            <p className="text-slate-500">
                                Complete an assessment and build your resume
                                to calculate evidence-based gaps.
                            </p>
                        )}
                    </div>

                    <button
                        onClick={() =>
                            nav('/college-student/skill-gap')
                        }
                        className="mt-4 font-semibold text-cyan-700"
                    >
                        Open Skill Gap Analysis →
                    </button>
                </section>

                <section className="rounded-2xl border bg-white p-5">
                    <h2 className="text-xl font-bold">
                        Recommended Next Step
                    </h2>

                    <div className="mt-3 space-y-2">
                        {s.attempts.length === 0 && (
                            <Action
                                t="Complete your first College assessment"
                                on={() =>
                                    nav('/college-student/assessment')
                                }
                            />
                        )}

                        {s.resume.resumeScore < 70 && (
                            <Action
                                t="Improve your resume sections"
                                on={() =>
                                    nav('/college-student/resume-builder')
                                }
                            />
                        )}

                        <Action
                            t="Practice your priority skill gap"
                            on={() =>
                                nav('/college-student/practice')
                            }
                        />

                        <Action
                            t="Continue personalized learning roadmap"
                            on={() =>
                                nav(
                                    '/college-student/learning-roadmap'
                                )
                            }
                        />

                        <Action
                            t="Practice mock interview"
                            on={() =>
                                nav('/college-student/mock-interview')
                            }
                        />
                    </div>
                </section>
            </div>

            <div className="grid gap-4 md:grid-cols-3">
                <Card
                    t="PRACTICE EVIDENCE"
                    v={`${s.practicePct}%`}
                />

                <Card
                    t="INTERVIEW PRACTICE"
                    v={`${s.interviewScore}%`}
                />

                <Card
                    t="APPLICATIONS TRACKED"
                    v={String(s.placements.length)}
                />
            </div>
        </div>
    );
}

function Card({
    t,
    v,
}: {
    t: string;
    v: string;
}) {
    return (
        <div className="rounded-2xl border bg-white p-5 shadow-sm">
            <p className="text-xs font-semibold text-slate-500">
                {t}
            </p>

            <p className="mt-2 text-3xl font-bold text-slate-900">
                {v}
            </p>
        </div>
    );
}

function Action({
    t,
    on,
}: {
    t: string;
    on: () => void;
}) {
    return (
        <button
            onClick={on}
            className="w-full rounded-xl bg-slate-50 p-3 text-left font-semibold hover:bg-cyan-50"
        >
            {t} →
        </button>
    );
}