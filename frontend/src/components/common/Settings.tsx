import { useEffect, useState } from "react";
import { Bell, Globe, Lock, Mail, Save, Shield, User } from "lucide-react";
import { useAuth } from "../../contexts/AuthContext";
import { isValidPassword } from "../../services/authService";

type UserSettings = {
  notifications: boolean;
  language: string;
  emailUpdates: boolean;
  weeklyReports: boolean;
  twoFactor: boolean;
};

const defaults: UserSettings = {
  notifications: true, language: "English",
  emailUpdates: true, weeklyReports: true, twoFactor: false,
};

function Settings() {
  const { user } = useAuth();
  const storageKey = `talentsphere_settings_${user?.id ?? "guest"}`;
  const [settings, setSettings] = useState<UserSettings>(defaults);
  const [showPassword, setShowPassword] = useState(false);
  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    const saved = localStorage.getItem(storageKey);
    if (saved) {
      try { setSettings({ ...defaults, ...JSON.parse(saved) }); } catch { setSettings(defaults); }
    }
  }, [storageKey]);

  useEffect(() => {
    document.documentElement.classList.remove("dark");
  }, []);

  const update = <K extends keyof UserSettings>(key: K, value: UserSettings[K]) =>
    setSettings((current) => ({ ...current, [key]: value }));

  const handleSave = () => {
    localStorage.setItem(storageKey, JSON.stringify(settings));
    setMessage("Settings saved successfully.");
  };

  const handlePasswordChange = () => {
    setMessage("");
    if (!user) return setMessage("Please login again.");
    if (!isValidPassword(newPassword)) {
      return setMessage("New password must be 8+ characters with uppercase, lowercase and a number.");
    }
    const users = JSON.parse(localStorage.getItem("talentsphere_users") || "[]");
    const index = users.findIndex((item: { id: string }) => item.id === user.id);
    if (index < 0 || users[index].password !== currentPassword) {
      return setMessage("Current password is incorrect.");
    }
    users[index].password = newPassword;
    localStorage.setItem("talentsphere_users", JSON.stringify(users));
    setCurrentPassword("");
    setNewPassword("");
    setShowPassword(false);
    setMessage("Password changed successfully.");
  };

  return (
    <div className="mx-auto max-w-5xl space-y-5">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Settings</h1>
        <p className="mt-1 text-slate-600">Manage your account preferences and security.</p>
      </div>

      <div className="grid gap-5 md:grid-cols-2">
        <Card icon={<User />} title="Profile">
          <div className="space-y-1 text-slate-700">
            <p><strong>Name:</strong> {user?.name}</p>
            <p><strong>Email:</strong> {user?.email}</p>
            <p><strong>Role:</strong> {user?.role}</p>
          </div>
        </Card>

        <Card icon={<Bell />} title="Notifications">
          <Toggle label="In-app notifications" checked={settings.notifications} onChange={(v) => update("notifications", v)} />
        </Card>

        <Card icon={<Globe />} title="Language">
          <select value={settings.language} onChange={(e) => update("language", e.target.value)}
            className="w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5">
            <option>English</option><option>Hindi</option>
          </select>
        </Card>

        <Card icon={<Mail />} title="Email Preferences">
          <div className="space-y-4">
            <Toggle label="Important account updates" checked={settings.emailUpdates} onChange={(v) => update("emailUpdates", v)} />
            <Toggle label="Weekly progress reports" checked={settings.weeklyReports} onChange={(v) => update("weeklyReports", v)} />
          </div>
        </Card>

        <Card icon={<Shield />} title="Two-Factor Authentication">
          <Toggle label="Enable two-factor preference" checked={settings.twoFactor} onChange={(v) => update("twoFactor", v)} />
          <p className="mt-2 text-sm text-amber-700">Preference is saved. Real OTP/2FA enforcement requires backend authentication integration.</p>
        </Card>

        <div className="md:col-span-2">
          <Card icon={<Lock />} title="Change Password">
            {!showPassword ? (
              <button type="button" onClick={() => setShowPassword(true)}
                className="rounded-xl bg-slate-900 px-5 py-2.5 font-semibold text-white">Change Password</button>
            ) : (
              <div className="grid gap-4 md:grid-cols-2">
                <input type="password" value={currentPassword} onChange={(e) => setCurrentPassword(e.target.value)}
                  placeholder="Current password" className="rounded-xl border border-slate-300 px-4 py-2.5" />
                <input type="password" value={newPassword} onChange={(e) => setNewPassword(e.target.value)}
                  placeholder="New password" className="rounded-xl border border-slate-300 px-4 py-2.5" />
                <div className="flex gap-3 md:col-span-2">
                  <button type="button" onClick={handlePasswordChange} className="rounded-xl bg-cyan-600 px-5 py-2.5 font-semibold text-white">Update Password</button>
                  <button type="button" onClick={() => setShowPassword(false)} className="rounded-xl border border-slate-300 px-5 py-2.5 font-semibold">Cancel</button>
                </div>
              </div>
            )}
          </Card>
        </div>
      </div>

      {message && <div className="rounded-xl border border-cyan-200 bg-cyan-50 p-4 font-medium text-cyan-800">{message}</div>}

      <button type="button" onClick={handleSave}
        className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-2.5 font-semibold text-white hover:bg-cyan-700">
        <Save size={18} /> Save Changes
      </button>
    </div>
  );
}

function Card({ icon, title, children }: { icon: React.ReactNode; title: string; children: React.ReactNode }) {
  return (
    <section className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
      <div className="mb-4 flex items-center gap-3 text-cyan-600">{icon}<h2 className="text-xl font-bold text-slate-900">{title}</h2></div>
      {children}
    </section>
  );
}

function Toggle({ label, checked, onChange }: { label: string; checked: boolean; onChange: (value: boolean) => void }) {
  return (
    <label className="flex cursor-pointer items-center justify-between gap-4">
      <span className="font-medium text-slate-700">{label}</span>
      <button type="button" role="switch" aria-checked={checked} onClick={() => onChange(!checked)}
        className={`relative h-7 w-12 rounded-full transition ${checked ? "bg-cyan-600" : "bg-slate-300"}`}>
        <span className={`absolute top-1 h-5 w-5 rounded-full bg-white transition ${checked ? "left-6" : "left-1"}`} />
      </button>
    </label>
  );
}

export default Settings;
