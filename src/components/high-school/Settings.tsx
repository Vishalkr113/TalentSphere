import { useState } from "react";
import {
    User,
    Bell,
    Moon,
    Shield,
    Save,
} from "lucide-react";

function Settings() {
    const [settings, setSettings] = useState({
        notifications: true,
        darkMode: false,
        emailUpdates: true,
        twoFactor: false,
    });

    const handleToggle = (
        key: keyof typeof settings
    ) => {
        setSettings((prev) => ({
            ...prev,
            [key]: !prev[key],
        }));
    };

    const Toggle = ({
        value,
        onClick,
    }: {
        value: boolean;
        onClick: () => void;
    }) => (
        <button
            onClick={onClick}
            className={`relative h-7 w-14 rounded-full transition ${value
                    ? "bg-cyan-600"
                    : "bg-slate-300"
                }`}
        >
            <span
                className={`absolute top-1 h-5 w-5 rounded-full bg-white transition ${value
                        ? "left-8"
                        : "left-1"
                    }`}
            />
        </button>
    );

    return (
        <div className="space-y-10">

            {/* Heading */}

            <div>

                <h1 className="text-4xl font-bold text-slate-900">
                    Settings
                </h1>

                <p className="mt-3 text-lg text-slate-600">
                    Manage your account preferences and application settings.
                </p>

            </div>

            {/* Account */}

            <div className="rounded-3xl bg-white p-8 shadow-sm">

                <div className="mb-8 flex items-center gap-4">

                    <div className="rounded-2xl bg-cyan-100 p-4 text-cyan-600">

                        <User size={28} />

                    </div>

                    <div>

                        <h2 className="text-2xl font-bold">
                            Account Settings
                        </h2>

                        <p className="text-slate-500">
                            Manage your personal information.
                        </p>

                    </div>

                </div>

                <div className="grid gap-6 md:grid-cols-2">

                    <div>

                        <label className="mb-2 block font-medium">
                            Full Name
                        </label>

                        <input
                            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-cyan-600"
                            defaultValue="Vishal Kumar"
                        />

                    </div>

                    <div>

                        <label className="mb-2 block font-medium">
                            Email
                        </label>

                        <input
                            className="w-full rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-cyan-600"
                            defaultValue="vishal@gmail.com"
                        />

                    </div>

                </div>

            </div>

            {/* Preferences */}

            <div className="rounded-3xl bg-white p-8 shadow-sm">

                <div className="mb-8 flex items-center gap-4">

                    <div className="rounded-2xl bg-cyan-100 p-4 text-cyan-600">

                        <Bell size={28} />

                    </div>

                    <div>

                        <h2 className="text-2xl font-bold">
                            Preferences
                        </h2>

                        <p className="text-slate-500">
                            Customize your TalentSphere experience.
                        </p>

                    </div>

                </div>

                <div className="space-y-6">

                    <div className="flex items-center justify-between">

                        <div>

                            <h3 className="font-semibold">
                                Notifications
                            </h3>

                            <p className="text-sm text-slate-500">
                                Receive important updates.
                            </p>

                        </div>

                        <Toggle
                            value={settings.notifications}
                            onClick={() =>
                                handleToggle("notifications")
                            }
                        />

                    </div>

                    <div className="flex items-center justify-between">

                        <div>

                            <h3 className="font-semibold">
                                Email Updates
                            </h3>

                            <p className="text-sm text-slate-500">
                                Receive updates through email.
                            </p>

                        </div>

                        <Toggle
                            value={settings.emailUpdates}
                            onClick={() =>
                                handleToggle("emailUpdates")
                            }
                        />

                    </div>

                    <div className="flex items-center justify-between">

                        <div>

                            <div className="flex items-center gap-2">
                                <h3 className="font-semibold">
                                    Dark Mode
                                </h3>
                                <Moon size={16} className="text-slate-500" />
                            </div>

                            <p className="text-sm text-slate-500">
                                Enable dark appearance.
                            </p>

                        </div>

                        <Toggle
                            value={settings.darkMode}
                            onClick={() =>
                                handleToggle("darkMode")
                            }
                        />

                    </div>

                    <div className="flex items-center justify-between">

                        <div>

                            <h3 className="font-semibold">
                                Two-Factor Authentication
                            </h3>

                            <p className="text-sm text-slate-500">
                                Improve account security.
                            </p>

                        </div>

                        <Toggle
                            value={settings.twoFactor}
                            onClick={() =>
                                handleToggle("twoFactor")
                            }
                        />

                    </div>

                </div>

            </div>

            {/* Security */}

            <div className="rounded-3xl bg-white p-8 shadow-sm">

                <div className="mb-8 flex items-center gap-4">

                    <div className="rounded-2xl bg-cyan-100 p-4 text-cyan-600">

                        <Shield size={28} />

                    </div>

                    <div>

                        <h2 className="text-2xl font-bold">
                            Security
                        </h2>

                        <p className="text-slate-500">
                            Manage your password and account protection.
                        </p>

                    </div>

                </div>

                <button className="rounded-xl bg-slate-900 px-6 py-3 font-semibold text-white transition hover:bg-slate-800">

                    Change Password

                </button>

            </div>

            {/* Save */}

            <div className="flex justify-end">

                <button className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700">

                    <Save size={18} />

                    Save Changes

                </button>

            </div>

        </div>
    );
}

export default Settings;