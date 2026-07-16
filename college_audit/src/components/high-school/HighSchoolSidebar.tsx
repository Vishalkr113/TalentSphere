import { NavLink } from "react-router-dom";

import {
  LayoutDashboard,
  User,
  BookOpen,
  Compass,
  Map,
  Bot,
  BarChart3,
  CalendarDays,
  ClipboardList,
  Target,
  Trophy,
  FileCheck2,
  Settings,
  LogOut,
  GraduationCap,
  X,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

interface HighSchoolSidebarProps {
  isOpen: boolean;
  onClose: () => void;
}

const menuItems = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    path: "/high-school-student/dashboard",
  },
  {
    title: "My Profile",
    icon: User,
    path: "/high-school-student/profile",
  },
  {
    title: "Assessment",
    icon: ClipboardList,
    path: "/high-school-student/assessment",
  },
  {
    title: "Assessment Reports",
    icon: BarChart3,
    path: "/high-school-student/assessment-reports",
  },
  {
    title: "Final Guidance",
    icon: FileCheck2,
    path: "/high-school-student/final-guidance",
  },
  {
    title: "Subject Guidance",
    icon: BookOpen,
    path: "/high-school-student/subject-guidance",
  },
  {
    title: "Career Explorer",
    icon: Compass,
    path: "/high-school-student/career-explorer",
  },
  {
    title: "Learning Roadmap",
    icon: Map,
    path: "/high-school-student/learning-roadmap",
  },
  {
    title: "AI Learning Support",
    icon: Bot,
    path: "/high-school-student/ai-learning-support",
  },
  {
    title: "Academic Progress",
    icon: BarChart3,
    path: "/high-school-student/academic-progress",
  },
  {
    title: "Upcoming Exams",
    icon: CalendarDays,
    path: "/high-school-student/upcoming-exams",
  },
  {
    title: "Assignments",
    icon: ClipboardList,
    path: "/high-school-student/assignments",
  },
  {
    title: "Daily Goal",
    icon: Target,
    path: "/high-school-student/daily-goal",
  },
  {
    title: "Achievements",
    icon: Trophy,
    path: "/high-school-student/achievements",
  },
  {
    title: "Settings",
    icon: Settings,
    path: "/high-school-student/settings",
  },
];

function HighSchoolSidebar({
  isOpen,
  onClose,
}: HighSchoolSidebarProps) {
  const { logout } = useAuth();

  const handleLogout = () => {
    logout();
    window.location.replace("/");
  };

  return (
    <aside
      className={`fixed left-0 top-0 z-50 flex h-dvh w-64 flex-col border-r border-slate-200 bg-white shadow-xl transition-transform duration-300 ease-in-out lg:z-40 lg:h-screen lg:translate-x-0 lg:shadow-none ${isOpen
          ? "translate-x-0"
          : "-translate-x-full"
        }`}
    >
      {/* Logo */}

      <div className="flex min-h-20 items-center justify-between border-b border-slate-200 px-5 py-4">
        <div className="flex min-w-0 items-center gap-3">
          <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-cyan-600 text-white">
            <GraduationCap size={24} />
          </div>

          <div className="min-w-0">
            <h2 className="truncate text-lg font-bold text-slate-900">
              TalentSphere
            </h2>

            <p className="truncate text-sm text-slate-500">
              High School Portal
            </p>
          </div>
        </div>

        {/* Mobile / Tablet Close Button */}

        <button
          type="button"
          onClick={onClose}
          aria-label="Close sidebar"
          className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl text-slate-600 transition hover:bg-slate-100 lg:hidden"
        >
          <X size={22} />
        </button>
      </div>

      {/* Navigation */}

      <nav className="min-h-0 flex-1 overflow-y-auto overscroll-contain px-3 py-4">
        <ul className="space-y-1">
          {menuItems.map((item) => {
            const Icon = item.icon;

            return (
              <li key={item.title}>
                <NavLink
                  to={item.path}
                  onClick={onClose}
                  className={({ isActive }) =>
                    `flex min-h-11 items-center gap-3 rounded-xl px-4 py-2.5 transition ${isActive
                      ? "bg-cyan-600 text-white shadow-sm"
                      : "text-slate-600 hover:bg-slate-100 hover:text-slate-900"
                    }`
                  }
                >
                  <Icon
                    size={19}
                    className="shrink-0"
                  />

                  <span className="truncate text-sm font-medium">
                    {item.title}
                  </span>
                </NavLink>
              </li>
            );
          })}
        </ul>
      </nav>

      {/* Logout */}

      <div className="shrink-0 border-t border-slate-200 bg-white p-3">
        <button
          type="button"
          onClick={handleLogout}
          className="flex w-full items-center justify-center gap-2 rounded-xl bg-red-600 px-4 py-3 text-sm font-semibold text-white transition hover:bg-red-700"
        >
          <LogOut size={18} />

          Logout
        </button>
      </div>
    </aside>
  );
}

export default HighSchoolSidebar;