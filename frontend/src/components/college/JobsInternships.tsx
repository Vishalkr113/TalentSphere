import { useState } from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { getCollegeProfile } from '../../services/college/collegeProfileService';
import {
    getPlacementItems,
    savePlacementItems,
} from '../../services/college/collegeWorkspaceService';

export default function JobsInternships() {
    const { user } = useAuth();

    if (!user) return null;

    const profile = getCollegeProfile(user.id);

    const [company, setCompany] = useState('');
    const [role, setRole] = useState('');
    const [location, setLocation] = useState('');
    const [tick, setTick] = useState(0);

    const items = getPlacementItems(user.id);

    const target = (profile.targetRole || '').toLowerCase();
    const skills = (profile.skills || '').toLowerCase();

    const add = () => {
        if (!company.trim() || !role.trim()) return;

        savePlacementItems(user.id, [
            ...items,
            {
                id: crypto.randomUUID(),
                company: company.trim(),
                role: role.trim(),
                type: 'Opportunity',
                status: 'Saved',
                date: new Date().toISOString(),
            },
        ]);

        setCompany('');
        setRole('');
        setLocation('');
        setTick(tick + 1);
    };

    return (
        <div className="space-y-6">
            <div>
                <h1 className="text-3xl font-bold">
                    Internship & Job Matching
                </h1>

                <p className="mt-2 text-slate-600">
                    Track real opportunities and compare them with your target
                    role and saved skills. TalentSphere does not fabricate live
                    vacancies.
                </p>
            </div>

            <section className="rounded-2xl border bg-white p-6">
                <h2 className="text-xl font-bold">
                    Add an opportunity
                </h2>

                <div className="mt-4 grid gap-3 md:grid-cols-3">
                    <input
                        className="rounded-xl border p-3"
                        placeholder="Company"
                        value={company}
                        onChange={(e) => setCompany(e.target.value)}
                    />

                    <input
                        className="rounded-xl border p-3"
                        placeholder="Role"
                        value={role}
                        onChange={(e) => setRole(e.target.value)}
                    />

                    <input
                        className="rounded-xl border p-3"
                        placeholder="Location preference"
                        value={location}
                        onChange={(e) => setLocation(e.target.value)}
                    />
                </div>

                <div className="mt-4 rounded-xl bg-slate-50 p-4 text-sm text-slate-600">
                    Target role:{' '}
                    <b>{profile.targetRole || 'Not selected'}</b> · Saved
                    skills: <b>{skills || 'None'}</b>

                    {role && (
                        <p className="mt-2">
                            Role-title match:{' '}
                            <b>
                                {target &&
                                    role.toLowerCase().includes(target)
                                    ? 'Strong'
                                    : 'Needs profile/skill review'}
                            </b>
                        </p>
                    )}
                </div>

                <button
                    onClick={add}
                    className="mt-4 rounded-xl bg-cyan-600 px-5 py-3 font-semibold text-white"
                >
                    Save opportunity
                </button>
            </section>

            <section className="space-y-3">
                {items.length ? (
                    items.map((a) => (
                        <div
                            key={a.id}
                            className="rounded-2xl border bg-white p-5"
                        >
                            <b>{a.role}</b>

                            <p className="text-slate-600">
                                {a.company} · {a.type} · {a.status}
                            </p>
                        </div>
                    ))
                ) : (
                    <div className="rounded-2xl border bg-white p-6 text-slate-600">
                        No opportunity saved yet.
                    </div>
                )}
            </section>
        </div>
    );
}