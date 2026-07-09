import {
  LayoutDashboard,
  FileText,
  Brain,
  Code2,
  Mic,
  Sparkles,
  Award,
  Settings,
  LogOut,
} from "lucide-react";

const menuItems = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    active: true,
  },
  {
    title: "Resume",
    icon: FileText,
  },
  {
    title: "Skill Assessment",
    icon: Brain,
  },
  {
    title: "Coding Practice",
    icon: Code2,
  },
  {
    title: "Mock Interview",
    icon: Mic,
  },
  {
    title: "AI Career Advisor",
    icon: Sparkles,
  },
  {
    title: "Certifications",
    icon: Award,
  },
  {
    title: "Settings",
    icon: Settings,
  },
];

function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 hidden h-screen w-72 border-r border-slate-200 bg-white lg:flex lg:flex-col">

      {/* Logo */}

      <div className="border-b border-slate-200 p-6">

        <h1 className="text-2xl font-bold text-cyan-600">
          TalentSphere
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          Student Portal
        </p>

      </div>

      {/* Menu */}

      <nav className="flex-1 px-4 py-6">

        <ul className="space-y-2">

          {menuItems.map((item) => {
            const Icon = item.icon;

            return (
              <li key={item.title}>

                <button
                  className={`flex w-full items-center gap-3 rounded-xl px-4 py-3 text-left transition ${
                    item.active
                      ? "bg-cyan-600 text-white"
                      : "text-slate-600 hover:bg-slate-100"
                  }`}
                >
                  <Icon size={20} />

                  <span className="font-medium">
                    {item.title}
                  </span>

                </button>

              </li>
            );
          })}

        </ul>

      </nav>

      {/* Logout */}

      <div className="border-t border-slate-200 p-4">

        <button className="flex w-full items-center gap-3 rounded-xl px-4 py-3 text-red-600 transition hover:bg-red-50">

          <LogOut size={20} />

          <span className="font-medium">
            Logout
          </span>

        </button>

      </div>

    </aside>
  );
}

export default Sidebar;