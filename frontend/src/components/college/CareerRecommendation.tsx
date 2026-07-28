import { useAuth } from '../../contexts/AuthContext';
import {
    getCollegeProfile,
    getCollegeStats,
    getSkillGap,
    isCollegeProfileReady,
} from '../../services/collegeService';
import CollegeProfileRequired from './CollegeProfileRequired';

const branchRoles: Record<string, string[]> = {
    'Computer Science Engineering': [
        'Software Developer',
        'Data Analyst',
        'AI Engineer',
        'Cloud Engineer',
        'Cybersecurity Analyst',
    ],
    'Information Technology': [
        'Software Developer',
        'Cloud Engineer',
        'Cybersecurity Analyst',
    ],
    'Mechanical Engineering': [
        'Design Engineer',
        'Manufacturing Engineer',
        'Quality Engineer',
    ],
    'Civil Engineering': [
        'Site Engineer',
        'Structural Engineer',
        'Project Engineer',
    ],
    'Electronics and Communication Engineering': [
        'Embedded Engineer',
        'Electronics Engineer',
        'Network Engineer',
    ],
    'Electrical Engineering': [
        'Electrical Engineer',
        'Power Systems Engineer',
        'Control Engineer',
    ],
    'Business Administration': [
        'Management Trainee',
        'Business Analyst',
        'Marketing Associate',
    ],
    Commerce: [
        'Financial Analyst',
        'Accountant',
        'Business Analyst',
    ],
};

export default function CareerRecommendation() {
    const { user } = useAuth();

    const id = user?.id || 'guest',
        p = getCollegeProfile(id),
        s = getCollegeStats(id),
        g = getSkillGap(id);

    if (!isCollegeProfileReady(p)) {
        return <CollegeProfileRequired />;
    }

    const roles = branchRoles[p.branch] || [];

    return (
        <div className="space-y-5">
            <div>
                <h1 className="text-3xl font-bold">Career Guidance</h1>
                <p className="mt-1 text-slate-600">
                    Practical role direction from your branch and current evidence.
                </p>
            </div>

            <section className="rounded-2xl bg-gradient-to-r from-cyan-600 to-blue-700 p-6 text-white">
                <p className="text-cyan-100">Current Target</p>

                <h2 className="mt-1 text-3xl font-bold">
                    {p.targetRole || 'Not selected'}
                </h2>

                <p className="mt-3">
                    Current placement readiness: {s.readiness}%. Priority evidence gap:{' '}
                    {g[0]?.skill || 'complete more evidence activities'}.
                </p>
            </section>

            <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
                {roles.map((r) => (
                    <section
                        key={r}
                        className="rounded-2xl border bg-white p-5"
                    >
                        <h2 className="text-xl font-bold">{r}</h2>

                        <p className="mt-2 text-sm text-slate-600">
                            {r === p.targetRole
                                ? 'Current selected target role.'
                                : 'Relevant path for your saved branch context.'}
                        </p>

                        <p className="mt-4 font-semibold text-cyan-700">
                            Use assessment, resume and practice evidence to improve readiness.
                        </p>
                    </section>
                ))}
            </div>
        </div>
    );
}