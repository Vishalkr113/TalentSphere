import { useAuth } from '../../contexts/AuthContext';
import {
    getCollegeProfile,
    getCollegeStats,
    getSkillGap,
} from '../../services/collegeService';
import { useState } from 'react';
import { generateAI } from '../../services/aiService';

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
    const [aiGuidance, setAiGuidance] = useState('');
    const [aiLoading, setAiLoading] = useState(false);

    const id = user?.id || 'guest',
        p = getCollegeProfile(id),
        s = getCollegeStats(id),
        g = getSkillGap(id);

    const roles = branchRoles[p.branch] || [
        'Software Developer', 'Data Analyst', 'AI Engineer',
        'Cloud Engineer', 'Cybersecurity Analyst'
    ];

    const getAIGuidance = async () => {
        setAiLoading(true);
        try {
            const result = await generateAI(
                'career_recommendation',
                'Give personalized career guidance from the current profile and evidence. Explain the best-fit roles, why they fit, and the next skills to build.',
                `Branch: ${p.branch}. Target role: ${p.targetRole || 'not selected'}. Career goal: ${p.careerGoal || 'not supplied'}. Skills: ${p.skills || 'none listed'}. Placement readiness: ${s.readiness}%. Top skill gap: ${g[0]?.skill || 'none identified'}. Relevant roles: ${roles.join(', ')}.`,
            );
            setAiGuidance(result.text);
        } catch (error) {
            setAiGuidance(error instanceof Error ? error.message : 'AI guidance is temporarily unavailable.');
        } finally {
            setAiLoading(false);
        }
    };

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

            <section className="rounded-2xl border bg-white p-5">
                <div className="flex flex-wrap items-center justify-between gap-3">
                    <div>
                        <h2 className="text-xl font-bold">Gemini AI Career Guidance</h2>
                        <p className="mt-1 text-sm text-slate-500">Personalized guidance based on your saved profile and assessment evidence.</p>
                    </div>
                    <button onClick={() => void getAIGuidance()} disabled={aiLoading} className="rounded-xl bg-cyan-600 px-4 py-2.5 font-semibold text-white disabled:opacity-50">
                        {aiLoading ? 'Generating…' : 'Get AI Guidance'}
                    </button>
                </div>
                {aiGuidance && <div className="mt-4 whitespace-pre-wrap rounded-xl bg-slate-50 p-4 text-sm leading-6 text-slate-700">{aiGuidance}</div>}
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