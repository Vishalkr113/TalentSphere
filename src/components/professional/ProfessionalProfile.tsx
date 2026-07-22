import { useEffect, useState } from 'react';
import { Save } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import {
    getProfessionalProfile,
    saveProfessionalProfile,
    type ProfessionalProfile as P,
} from '../../services/professionalService';

export default function ProfessionalProfile() {
    const { user } = useAuth();

    const id = user?.id || 'guest';

    const [form, setForm] = useState<P>(() =>
        getProfessionalProfile(
            id,
            user?.name || '',
            user?.email || ''
        )
    );

    const [msg, setMsg] = useState('');

    useEffect(() => {
        setForm(
            getProfessionalProfile(
                id,
                user?.name || '',
                user?.email || ''
            )
        );
    }, [id, user?.name, user?.email]);

    const change = (
        e: React.ChangeEvent<HTMLInputElement>
    ) =>
        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });

    return (
        <div className="space-y-5">
            <div>
                <h1 className="text-3xl font-bold">
                    Professional Profile
                </h1>

                <p className="text-slate-600">
                    Your dashboard, assessments and growth analysis
                    use this saved context.
                </p>
            </div>

            <div className="grid gap-4 rounded-2xl border bg-white p-6 md:grid-cols-2">
                {Object.entries(form).map(([k, v]) => (
                    <label
                        key={k}
                        className="text-sm font-medium capitalize text-slate-700"
                    >
                        {k.replace(/([A-Z])/g, ' $1')}

                        <input
                            name={k}
                            value={v}
                            onChange={change}
                            placeholder={`Enter ${k
                                .replace(/([A-Z])/g, ' $1')
                                .toLowerCase()}`}
                            className="mt-2 w-full rounded-xl border p-3 font-normal"
                        />
                    </label>
                ))}
            </div>

            <button
                onClick={() => {
                    saveProfessionalProfile(id, form);

                    setMsg(
                        'Professional profile saved. Dashboard evidence recalculated.'
                    );
                }}
                className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white"
            >
                <Save size={18} />
                Save Profile
            </button>

            {msg && (
                <p className="rounded-xl bg-cyan-50 p-4 text-cyan-800">
                    {msg}
                </p>
            )}
        </div>
    );
}