import { useEffect, useRef, useState } from 'react';
import { Camera, Pencil, Save, Trash2 } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import {
    getCollegeProfile,
    saveCollegeProfile,
    type CollegeProfileData,
} from '../../services/collegeService';

const degrees = [
    'B.Tech',
    'B.E.',
    'BCA',
    'B.Sc',
    'BBA',
    'B.Com',
    'Diploma',
    'MCA',
    'M.Tech',
    'MBA',
];

const branches = [
    'Computer Science Engineering',
    'Information Technology',
    'Mechanical Engineering',
    'Civil Engineering',
    'Electronics and Communication Engineering',
    'Electrical Engineering',
    'Computer Applications',
    'Business Administration',
    'Commerce',
];

const states = [
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Tamil Nadu',
    'Telangana',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal',
    'Delhi',
];

const roles = [
    'Software Developer',
    'Data Analyst',
    'AI Engineer',
    'Cloud Engineer',
    'Cybersecurity Analyst',
    'Core Engineering Role',
    'Management Trainee',
];

export default function CollegeProfile() {
    const { user } = useAuth();

    const id = user?.id || 'guest';

    const input = useRef<HTMLInputElement>(null);

    const [data, setData] = useState<CollegeProfileData>(() =>
        getCollegeProfile(id)
    );

    const [edit, setEdit] = useState(false);
    const [msg, setMsg] = useState('');

    useEffect(() => {
        setData((d) => ({
            ...getCollegeProfile(id),
            fullName:
                getCollegeProfile(id).fullName || user?.name || '',
            email:
                getCollegeProfile(id).email || user?.email || '',
        }));
    }, [id, user]);

    const set = (
        k: keyof CollegeProfileData,
        v: string
    ) => setData((x) => ({ ...x, [k]: v }));

    const save = () => {
        saveCollegeProfile(id, data);
        setEdit(false);
        setMsg(
            'College profile saved. Future assessments and recommendations now use this context.'
        );
    };

    const photo = (
        e: React.ChangeEvent<HTMLInputElement>
    ) => {
        const f = e.target.files?.[0];
        if (!f) return;

        const r = new FileReader();

        r.onload = () => set('photo', String(r.result));

        r.readAsDataURL(f);
    };

    return (
        <div className="mx-auto max-w-5xl space-y-5">
            <div className="flex items-center justify-between">
                <div>
                    <h1 className="text-3xl font-bold text-slate-900">
                        My College Profile
                    </h1>

                    <p className="mt-1 text-slate-600">
                        Degree, branch and semester control your College
                        experience.
                    </p>
                </div>

                <button
                    onClick={() => setEdit(!edit)}
                    className="flex items-center gap-2 rounded-xl border bg-white px-4 py-2 font-semibold"
                >
                    <Pencil size={17} />
                    {edit ? 'Cancel' : 'Edit Profile'}
                </button>
            </div>

            <section className="rounded-2xl border bg-white p-5 shadow-sm">
                <div className="flex flex-wrap items-center gap-5">
                    <div className="relative flex h-24 w-24 items-center justify-center rounded-full bg-cyan-50 text-3xl font-bold text-cyan-700">
                        {data.photo ? (
                            <img
                                src={data.photo}
                                alt="Profile"
                                className="h-full w-full rounded-full object-cover"
                            />
                        ) : (
                            data.fullName?.[0] || 'C'
                        )}

                        <button
                            onClick={() => input.current?.click()}
                            className="absolute -bottom-1 -right-1 rounded-full border-4 border-white bg-cyan-600 p-2 text-white shadow"
                        >
                            <Camera size={15} />
                        </button>
                    </div>

                    <input
                        ref={input}
                        type="file"
                        accept="image/*"
                        className="hidden"
                        onChange={photo}
                    />

                    <div>
                        <h2 className="text-xl font-bold">
                            {data.fullName || 'College Student'}
                        </h2>

                        <p className="text-slate-500">
                            {data.degree || 'Degree not selected'} ·{' '}
                            {data.branch || 'Branch not selected'}{' '}
                            {data.semester
                                ? `· Semester ${data.semester}`
                                : '· Semester not selected'}
                        </p>

                        {data.photo && (
                            <button
                                onClick={() => set('photo', '')}
                                className="mt-2 flex items-center gap-1 text-sm text-red-600"
                            >
                                <Trash2 size={14} />
                                Remove photo
                            </button>
                        )}
                    </div>
                </div>
            </section>

            <section className="rounded-2xl border bg-white p-5 shadow-sm">
                <div className="grid gap-4 md:grid-cols-2">
                    {[
                        ['fullName', 'Full Name'],
                        ['email', 'Email'],
                        ['college', 'College Name'],
                        ['university', 'University'],
                        ['cgpa', 'CGPA'],
                        ['phone', 'Phone'],
                        ['city', 'City / District'],
                        ['linkedin', 'LinkedIn'],
                        ['github', 'GitHub'],
                        ['portfolio', 'Portfolio'],
                        ['careerGoal', 'Career Goal'],
                        ['skills', 'Skills (comma separated)'],
                    ].map(([k, l]) => (
                        <label
                            key={k}
                            className="text-sm font-semibold text-slate-700"
                        >
                            {l}

                            <input
                                disabled={!edit}
                                value={String(
                                    data[k as keyof CollegeProfileData] || ''
                                )}
                                onChange={(e) =>
                                    set(
                                        k as keyof CollegeProfileData,
                                        e.target.value
                                    )
                                }
                                placeholder={`Enter ${l.toLowerCase()}`}
                                className="mt-1 w-full rounded-xl border px-4 py-2.5 disabled:bg-slate-50"
                            />
                        </label>
                    ))}

                    <label className="text-sm font-semibold">
                        Degree

                        <select
                            disabled={!edit}
                            value={data.degree}
                            onChange={(e) =>
                                set('degree', e.target.value)
                            }
                            className="mt-1 w-full rounded-xl border px-4 py-2.5 disabled:bg-slate-50"
                        >
                            <option value="">Select degree</option>

                            {degrees.map((x) => (
                                <option key={x}>{x}</option>
                            ))}
                        </select>
                    </label>

                    <label className="text-sm font-semibold">
                        Branch / Specialization

                        <select
                            disabled={!edit}
                            value={data.branch}
                            onChange={(e) =>
                                set('branch', e.target.value)
                            }
                            className="mt-1 w-full rounded-xl border px-4 py-2.5 disabled:bg-slate-50"
                        >
                            <option value="">
                                Select branch / specialization
                            </option>

                            {branches.map((x) => (
                                <option key={x}>{x}</option>
                            ))}
                        </select>
                    </label>

                    <label className="text-sm font-semibold">
                        Semester

                        <select
                            disabled={!edit}
                            value={data.semester}
                            onChange={(e) =>
                                set('semester', e.target.value)
                            }
                            className="mt-1 w-full rounded-xl border px-4 py-2.5 disabled:bg-slate-50"
                        >
                            <option value="">Select semester</option>

                            {Array.from(
                                { length: 8 },
                                (_, i) => i + 1
                            ).map((x) => (
                                <option key={x}>{x}</option>
                            ))}
                        </select>
                    </label>

                    <label className="text-sm font-semibold">
                        State

                        <select
                            disabled={!edit}
                            value={data.state}
                            onChange={(e) =>
                                set('state', e.target.value)
                            }
                            className="mt-1 w-full rounded-xl border px-4 py-2.5 disabled:bg-slate-50"
                        >
                            <option value="">Select state</option>

                            {states.map((x) => (
                                <option key={x}>{x}</option>
                            ))}
                        </select>
                    </label>

                    <label className="text-sm font-semibold">
                        Target Role

                        <select
                            disabled={!edit}
                            value={data.targetRole}
                            onChange={(e) =>
                                set('targetRole', e.target.value)
                            }
                            className="mt-1 w-full rounded-xl border px-4 py-2.5 disabled:bg-slate-50"
                        >
                            <option value="">
                                Select target role
                            </option>

                            {roles.map((x) => (
                                <option key={x}>{x}</option>
                            ))}
                        </select>
                    </label>
                </div>

                {edit && (
                    <button
                        onClick={save}
                        className="mt-5 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white"
                    >
                        <Save size={17} />
                        Save Changes
                    </button>
                )}

                {msg && (
                    <p className="mt-4 rounded-xl bg-cyan-50 p-3 text-sm font-medium text-cyan-800">
                        {msg}
                    </p>
                )}
            </section>
        </div>
    );
}