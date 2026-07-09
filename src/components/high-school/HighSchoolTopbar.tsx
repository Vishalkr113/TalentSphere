import { Bell, Search } from "lucide-react";
import { useAuth } from "../../contexts/AuthContext";

function HighSchoolTopbar() {
  const { user } = useAuth();

  return (
    <header className="sticky top-0 z-30 flex h-20 items-center justify-between border-b border-slate-200 bg-white px-8">

      {/* Left */}

      <div>

        <h1 className="text-2xl font-bold text-slate-900">
          Welcome, {user?.name ?? "Student"} 👋
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          High School Student Dashboard
        </p>

      </div>

      {/* Right */}

      <div className="flex items-center gap-5">

        {/* Search */}

        <div className="relative hidden md:block">

          <Search
            size={18}
            className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400"
          />

          <input
            type="text"
            placeholder="Search..."
            className="w-72 rounded-xl border border-slate-300 py-3 pl-11 pr-4 outline-none transition focus:border-cyan-600"
          />

        </div>

        {/* Notification */}

        <button className="relative rounded-xl border border-slate-200 p-3 transition hover:bg-slate-100">

          <Bell size={22} />

          <span className="absolute right-2 top-2 h-2.5 w-2.5 rounded-full bg-red-500"></span>

        </button>

        {/* Profile */}

        <div className="flex items-center gap-3 rounded-xl border border-slate-200 px-4 py-2">

          <div className="flex h-11 w-11 items-center justify-center rounded-full bg-cyan-600 text-lg font-bold text-white">

            {user?.name?.charAt(0).toUpperCase() ?? "S"}

          </div>

          <div>

            <h3 className="font-semibold text-slate-900">
              {user?.name ?? "Student"}
            </h3>

            <p className="text-xs text-slate-500">
              High School Student
            </p>

          </div>

        </div>

      </div>

    </header>
  );
}

export default HighSchoolTopbar;