import { useAuth } from '../../contexts/AuthContext';
import {
    getCollegeProfile,
    getCollegeStats,
    getSkillGap,
} from '../../services/collegeService';

export default function SkillGapAnalysis() {
    const { user } = useAuth();

    const id = user?.id || 'guest',
        p = getCollegeProfile(id),
        s = getCollegeStats(id),
        g = getSkillGap(id);

    return (
        <div className="space-y-5">
            <div>
                <h1 className="text-3xl font-bold">
                    Skill Gap Analysis
                </h1>

                <p className="mt-1 text-slate-600">
                    Current-context assessment + resume evidence
                    compared with {p.targetRole || 'your target role'}.
                </p>
            </div>

            {!s.attempts.length ? (
                <section className="rounded-2xl border bg-white p-6 text-slate-600">
                    Complete a College assessment first. Skill gaps will use actual
                    assessment evidence. Add your branch and target role in your profile
                    for more personalized gap analysis.
                </section>
            ) : (
                <section className="rounded-2xl border bg-white p-5">
                    {g.length ? (
                        <div className="space-y-3">
                            {g.map((x, i) => (
                                <div
                                    key={x.skill}
                                    className="flex items-center justify-between rounded-xl bg-slate-50 p-4"
                                >
                                    <div>
                                        <b>
                                            {i + 1}. {x.skill}
                                        </b>

                                        <p className="text-sm text-slate-500">
                                            Source: {x.source}
                                        </p>
                                    </div>

                                    <span className="font-bold text-amber-700">
                                        {x.score
                                            ? `${x.score}% evidence`
                                            : 'Evidence missing'}
                                    </span>
                                </div>
                            ))}
                        </div>
                    ) : (
                        <p className="text-slate-500">
                            No critical evidence gap detected in the
                            latest context. Continue practice and resume
                            improvement.
                        </p>
                    )}
                </section>
            )}
        </div>
    );
}