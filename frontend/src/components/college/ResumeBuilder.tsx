import { useState } from 'react';
import { Save, Printer } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import {
    getCollegeProfile,
    getResume,
    saveResume,
    type ResumeData,
} from '../../services/collegeService';

export default function ResumeBuilder() {
    const { user } = useAuth();

    const id = user?.id || 'guest';
    const p = getCollegeProfile(id);

    const [d, setD] = useState<ResumeData>(() => {
        const r = getResume(id);

        return {
            ...r,
            fullName: r.fullName || p.fullName || user?.name || '',
            email: r.email || p.email || user?.email || '',
            linkedin: r.linkedin || p.linkedin,
            github: r.github || p.github,
            portfolio: r.portfolio || p.portfolio,
            skills: r.skills || p.skills,
            education:
                r.education ||
                [p.degree, p.branch, p.college, p.university]
                    .filter(Boolean)
                    .join(' · '),
        };
    });

    const [msg, setMsg] = useState('');

    const set = (
        k: keyof ResumeData,
        v: string
    ) => setD((x) => ({ ...x, [k]: v }));

    const fields: [keyof ResumeData, string, number][] = [
        ['summary', 'Professional Summary', 4],
        ['skills', 'Skills', 3],
        ['education', 'Education', 4],
        ['projects', 'Projects', 5],
        ['internships', 'Internships', 4],
        ['experience', 'Work Experience', 4],
        ['certifications', 'Certifications', 3],
        ['achievements', 'Achievements', 3],
    ];

    return (
        <div className="space-y-5">
            <div>
                <h1 className="text-3xl font-bold">
                    Resume Builder
                </h1>

                <p className="mt-1 text-slate-600">
                    Create and save an ATS-friendly primary resume.
                    Profile data is reused where available.
                </p>
            </div>

            <section className="rounded-2xl border bg-white p-5">
                <div className="grid gap-4 md:grid-cols-2">
                    {(
                        [
                            'fullName',
                            'email',
                            'phone',
                            'address',
                            'linkedin',
                            'github',
                            'portfolio',
                        ] as (keyof ResumeData)[]
                    ).map((k) => (
                        <label
                            key={k}
                            className="text-sm font-semibold capitalize"
                        >
                            {k}

                            <input
                                value={d[k]}
                                onChange={(e) =>
                                    set(k, e.target.value)
                                }
                                className="mt-1 w-full rounded-xl border px-4 py-2.5"
                                placeholder={`Enter ${k}`}
                            />
                        </label>
                    ))}
                </div>

                {fields.map(([k, l, rows]) => (
                    <label
                        key={k}
                        className="mt-4 block text-sm font-semibold"
                    >
                        {l}

                        <textarea
                            rows={rows}
                            value={d[k]}
                            onChange={(e) =>
                                set(k, e.target.value)
                            }
                            className="mt-1 w-full rounded-xl border p-4"
                            placeholder={`Add ${l.toLowerCase()}...`}
                        />
                    </label>
                ))}

                <div className="mt-5 flex flex-wrap gap-3">
                    <button
                        onClick={() => {
                            saveResume(id, d, p);
                            setMsg(
                                'Resume saved and a new analysis snapshot was created.'
                            );
                        }}
                        className="flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white"
                    >
                        <Save size={17} />
                        Save Resume
                    </button>

                    <button
                        onClick={() => window.print()}
                        className="flex items-center gap-2 rounded-xl border px-5 py-2.5 font-semibold"
                    >
                        <Printer size={17} />
                        Print / Save PDF
                    </button>
                </div>

                {msg && (
                    <p className="mt-4 rounded-xl bg-green-50 p-3 text-green-800">
                        {msg}
                    </p>
                )}
            </section>
        </div>
    );
}