import { useState } from "react";
import {
  User,
  Bell,
  Moon,
  Shield,
  Lock,
  Globe,
  Mail,
  Save,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

function Settings() {
  const { user } = useAuth();

  const [notifications, setNotifications] = useState(true);
  const [darkMode, setDarkMode] = useState(false);
  const [twoFactor, setTwoFactor] = useState(false);
  const [language, setLanguage] = useState("English");

  const handleSave = () => {
    alert("Settings saved successfully.");
  };

  return (
    <div className="space-y-8">

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Settings
        </h1>

        <p className="mt-2 text-slate-600">
          Manage your account preferences and security.
        </p>

      </div>

      <div className="grid gap-6">

        {/* Profile */}

        <div className="rounded-3xl bg-white p-6 shadow-sm">

          <div className="flex items-center gap-3">

            <User className="text-cyan-600" />

            <h2 className="text-2xl font-bold">
              Profile
            </h2>

          </div>

          <div className="mt-5 space-y-2">

            <p>
              <strong>Name:</strong> {user?.name}
            </p>

            <p>
              <strong>Email:</strong> {user?.email}
            </p>

            <p>
              <strong>Role:</strong> {user?.role}
            </p>

          </div>

        </div>

        {/* Notifications */}

        <div className="rounded-3xl bg-white p-6 shadow-sm">

          <div className="flex items-center justify-between">

            <div className="flex items-center gap-3">

              <Bell className="text-cyan-600" />

              <h2 className="text-xl font-semibold">
                Notifications
              </h2>

            </div>

            <input
              type="checkbox"
              checked={notifications}
              onChange={() =>
                setNotifications(!notifications)
              }
            />

          </div>

        </div>

        {/* Dark Mode */}

        <div className="rounded-3xl bg-white p-6 shadow-sm">

          <div className="flex items-center justify-between">

            <div className="flex items-center gap-3">

              <Moon className="text-cyan-600" />

              <h2 className="text-xl font-semibold">
                Dark Mode
              </h2>

            </div>

            <input
              type="checkbox"
              checked={darkMode}
              onChange={() =>
                setDarkMode(!darkMode)
              }
            />

          </div>

        </div>

        {/* Language */}

        <div className="rounded-3xl bg-white p-6 shadow-sm">

          <div className="flex items-center gap-3">

            <Globe className="text-cyan-600" />

            <h2 className="text-xl font-semibold">
              Language
            </h2>

          </div>

          <select
            value={language}
            onChange={(e) =>
              setLanguage(e.target.value)
            }
            className="mt-4 rounded-xl border border-slate-300 px-4 py-3"
          >

            <option>English</option>

            <option>Hindi</option>

          </select>

        </div>

        {/* Email */}

        <div className="rounded-3xl bg-white p-6 shadow-sm">

          <div className="flex items-center gap-3">

            <Mail className="text-cyan-600" />

            <h2 className="text-xl font-semibold">
              Email Preferences
            </h2>

          </div>

          <p className="mt-3 text-slate-600">
            Receive important updates and weekly reports.
          </p>

        </div>

        {/* Security */}

        <div className="rounded-3xl bg-white p-6 shadow-sm">

          <div className="flex items-center gap-3">

            <Shield className="text-cyan-600" />

            <h2 className="text-xl font-semibold">
              Security
            </h2>

          </div>

          <button className="mt-5 rounded-xl bg-slate-900 px-5 py-3 text-white">

            <div className="flex items-center gap-2">

              <Lock size={18} />

              Change Password

            </div>

          </button>

        </div>

        {/* Two Factor */}

        <div className="rounded-3xl bg-white p-6 shadow-sm">

          <div className="flex items-center justify-between">

            <div className="flex items-center gap-3">

              <Shield className="text-cyan-600" />

              <h2 className="text-xl font-semibold">
                Two-Factor Authentication
              </h2>

            </div>

            <input
              type="checkbox"
              checked={twoFactor}
              onChange={() =>
                setTwoFactor(!twoFactor)
              }
            />

          </div>

        </div>

      </div>

      <button
        onClick={handleSave}
        className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white hover:bg-cyan-700"
      >

        <Save size={18} />

        Save Changes

      </button>

    </div>
  );
}

export default Settings;