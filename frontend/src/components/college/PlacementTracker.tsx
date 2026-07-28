import { useState } from 'react';
import { Plus, Trash2 } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import {
    getPlacementItems,
    savePlacementItems,
    type PlacementItem,
} from '../../services/collegeService';

export default function PlacementTracker() {
    const { user } = useAuth();

    const id = user?.id || 'guest';

    const [items, setItems] = useState(() =>
        getPlacementItems(id)
    );

    const [form, setForm] = useState({
        company: '',
        role: '',
        type: 'Internship',
        status: 'Applied',
    });

    const save = (v: PlacementItem[]) => {
        setItems(v);
        savePlacementItems(id, v);
    };

    return (
        <div className="space-y-5">
            <div>
                <h1 className="text-3xl font-bold">
                    Placement Tracker
                </h1>

                <p className="mt-1 text-slate-600">
                    Track internship and job applications with real
                    status updates.
                </p>
            </div>

            <section className="rounded-2xl border bg-white p-5">
                <div className="grid gap-3 md:grid-cols-4">
                    <input
                        placeholder="Company"
                        value={form.company}
                        onChange={(e) =>
                            setForm({
                                ...form,
                                company: e.target.value,
                            })
                        }
                        className="rounded-xl border px-3 py-2"
                    />

                    <input
                        placeholder="Role"
                        value={form.role}
                        onChange={(e) =>
                            setForm({
                                ...form,
                                role: e.target.value,
                            })
                        }
                        className="rounded-xl border px-3 py-2"
                    />

                    <select
                        value={form.type}
                        onChange={(e) =>
                            setForm({
                                ...form,
                                type: e.target.value,
                            })
                        }
                        className="rounded-xl border px-3 py-2"
                    >
                        <option>Internship</option>
                        <option>Job</option>
                    </select>

                    <button
                        disabled={!form.company || !form.role}
                        onClick={() => {
                            save([
                                ...items,
                                {
                                    ...form,
                                    id: crypto.randomUUID(),
                                    date: new Date().toISOString(),
                                },
                            ]);

                            setForm({
                                ...form,
                                company: '',
                                role: '',
                            });
                        }}
                        className="flex items-center justify-center gap-2 rounded-xl bg-cyan-600 px-4 py-2 font-semibold text-white disabled:opacity-40"
                    >
                        <Plus size={17} />
                        Add
                    </button>
                </div>
            </section>

            <section className="rounded-2xl border bg-white p-5">
                <div className="space-y-3">
                    {items.map((x) => (
                        <div
                            key={x.id}
                            className="grid items-center gap-3 rounded-xl bg-slate-50 p-4 md:grid-cols-[1fr_1fr_150px_40px]"
                        >
                            <div>
                                <b>{x.company}</b>

                                <p className="text-sm text-slate-500">
                                    {x.type}
                                </p>
                            </div>

                            <span>{x.role}</span>

                            <select
                                value={x.status}
                                onChange={(e) =>
                                    save(
                                        items.map((i) =>
                                            i.id === x.id
                                                ? {
                                                    ...i,
                                                    status: e.target.value,
                                                }
                                                : i
                                        )
                                    )
                                }
                                className="rounded-lg border px-2 py-2"
                            >
                                <option>Applied</option>
                                <option>Assessment</option>
                                <option>Interview</option>
                                <option>Offer</option>
                                <option>Rejected</option>
                            </select>

                            <button
                                onClick={() =>
                                    save(
                                        items.filter((i) => i.id !== x.id)
                                    )
                                }
                                className="text-red-600"
                            >
                                <Trash2 size={18} />
                            </button>
                        </div>
                    ))}

                    {!items.length && (
                        <p className="text-slate-500">
                            No applications added yet.
                        </p>
                    )}
                </div>
            </section>
        </div>
    );
}