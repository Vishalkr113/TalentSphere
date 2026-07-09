import { NavLink } from "react-router-dom";

import {
  LayoutDashboard,
  FileText,
  Brain,
  Code2,
  LogOut,
} from "lucide-react";

const menuItems = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    path: "/student/dashboard",
  },
  {
    title: "Resume",
    icon: FileText,
    path: "/student/resume",
  },
  {
    title: "Skill Assessment",
    icon: Brain,
    path: "/student/skill-assessment",
  },
  {
    title: "Coding Assessment",
    icon: Code2,
    path: "/student/coding-assessment",
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

                <NavLink
                  to={item.path}
                  className={({ isActive }) =>
                    `flex items-center gap-3 rounded-xl px-4 py-3 font-medium transition ${
                      isActive
                        ? "bg-cyan-600 text-white"
                        : "text-slate-600 hover:bg-slate-100"
                    }`
                  }
                >
                  <Icon size={20} />

                  <span>{item.title}</span>

                </NavLink>

              </li>
            );
          })}

        </ul>
      </nav>

      {/* Logout */}
      <div className="border-t border-slate-200 p-4">

        <button className="flex w-full items-center gap-3 rounded-xl px-4 py-3 font-medium text-red-600 transition hover:bg-red-50">

          <LogOut size={20} />

          <span>Logout</span>

        </button>

      </div>

    </aside>
  );
}

export default Sidebar;