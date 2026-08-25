import { useEffect, useState } from "react";
import { Bell, Search } from "lucide-react";
import { useAuth } from "../contexts/AuthContext";
import { getCanonicalProfile, type CanonicalProfile } from "../services/canonicalProfileService";

function Topbar() {
  const { user } = useAuth();
  const [profile, setProfile] = useState<CanonicalProfile | null>(() => user ? getCanonicalProfile(String(user.id)) : null);

  useEffect(() => {
    if (!user) return;
    setProfile(getCanonicalProfile(String(user.id)));
    const onUpdate = (event: Event) => {
      const detail = (event as CustomEvent<CanonicalProfile>).detail;
      if (detail && String(detail.user_id) === String(user.id)) setProfile(detail);
      else setProfile(getCanonicalProfile(String(user.id)));
    };
    window.addEventListener("talentsphere:profile-updated", onUpdate);
    return () => window.removeEventListener("talentsphere:profile-updated", onUpdate);
  }, [user]);

  const photo = profile?.profile_photo || null;
  const name = profile?.full_name || user?.full_name || user?.name || "User";
  const role = user?.role === "working_professional" ? "Working Professional" : user?.role === "college_student" ? "College Student" : user?.role === "high_school_student" ? "High School Student" : "Student";
  const initial = name.trim().charAt(0).toUpperCase() || "U";

  return (
    <header className="sticky top-0 z-40 flex h-20 items-center justify-between border-b border-slate-200 bg-white px-8">
      <div>
        <h1 className="text-2xl font-bold text-slate-900">Dashboard</h1>
        <p className="mt-1 text-sm text-slate-500">Welcome back! Let's continue your learning journey.</p>
      </div>
      <div className="flex items-center gap-4">
        <div className="hidden items-center gap-3 rounded-xl border border-slate-200 bg-slate-50 px-4 py-2 lg:flex">
          <Search size={18} className="text-slate-500" />
          <input type="text" placeholder="Search..." className="bg-transparent text-sm outline-none placeholder:text-slate-400" />
        </div>
        <button className="relative rounded-xl border border-slate-200 p-3 transition hover:bg-slate-100"><Bell size={20}/><span className="absolute right-2 top-2 h-2 w-2 rounded-full bg-red-500"/></button>
        <button className="flex items-center gap-3 rounded-xl border border-slate-200 px-3 py-2 transition hover:bg-slate-100">
          <div className="h-[34px] w-[34px] overflow-hidden rounded-full bg-cyan-50 flex items-center justify-center font-bold text-cyan-700">
            {photo ? <img src={photo} alt="Profile" className="h-full w-full object-cover"/> : <span>{initial}</span>}
          </div>
          <div className="hidden text-left lg:block"><p className="text-sm font-semibold text-slate-900">{name}</p><p className="text-xs text-slate-500">{role}</p></div>
        </button>
      </div>
    </header>
  );
}
export default Topbar;
