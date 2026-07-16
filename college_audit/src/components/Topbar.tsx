import {
  Bell,
  Search,
  UserCircle,
} from "lucide-react";

function Topbar() {
  return (
    <header className="sticky top-0 z-40 flex h-20 items-center justify-between border-b border-slate-200 bg-white px-8">

      {/* Left */}

      <div>

        <h1 className="text-2xl font-bold text-slate-900">
          Dashboard
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          Welcome back! Let's continue your learning journey.
        </p>

      </div>

      {/* Right */}

      <div className="flex items-center gap-4">

        {/* Search */}

        <div className="hidden items-center gap-3 rounded-xl border border-slate-200 bg-slate-50 px-4 py-2 lg:flex">

          <Search
            size={18}
            className="text-slate-500"
          />

          <input
            type="text"
            placeholder="Search..."
            className="bg-transparent text-sm outline-none placeholder:text-slate-400"
          />

        </div>

        {/* Notification */}

        <button className="relative rounded-xl border border-slate-200 p-3 transition hover:bg-slate-100">

          <Bell size={20} />

          <span className="absolute right-2 top-2 h-2 w-2 rounded-full bg-red-500" />

        </button>

        {/* User */}

        <button className="flex items-center gap-3 rounded-xl border border-slate-200 px-3 py-2 transition hover:bg-slate-100">

          <UserCircle
            size={34}
            className="text-cyan-600"
          />

          <div className="hidden text-left lg:block">

            <p className="text-sm font-semibold text-slate-900">
              Vishal Kumar
            </p>

            <p className="text-xs text-slate-500">
              Student
            </p>

          </div>

        </button>

      </div>

    </header>
  );
}

export default Topbar;