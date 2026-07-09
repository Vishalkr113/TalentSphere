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
  Settings,
  LogOut,
  GraduationCap,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

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

function HighSchoolSidebar() {
  const { logout } = useAuth();

  const handleLogout = () => {
    logout();
    window.location.href = "/";
  };

  return (
    <aside className="fixed left-0 top-0 flex h-screen w-72 flex-col border-r border-slate-200 bg-white">

      {/* Logo */}

      <div className="border-b border-slate-200 p-6">

        <div className="flex items-center gap-3">

          <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-cyan-600 text-white">

            <GraduationCap size={26} />

          </div>

          <div>

            <h2 className="text-xl font-bold text-slate-900">
              TalentSphere
            </h2>

            <p className="text-sm text-slate-500">
              High School Portal
            </p>

          </div>

        </div>

      </div>

      {/* Navigation */}

      <nav className="flex-1 overflow-y-auto px-4 py-6">

        <ul className="space-y-2">

          {menuItems.map((item) => {

            const Icon = item.icon;

            return (

              <li key={item.title}>

                <NavLink
                  to={item.path}
                  className={({ isActive }) =>
                    `flex items-center gap-3 rounded-xl px-4 py-3 transition ${
                      isActive
                        ? "bg-cyan-600 text-white"
                        : "text-slate-600 hover:bg-slate-100"
                    }`
                  }
                >

                  <Icon size={20} />

                  <span className="font-medium">
                    {item.title}
                  </span>

                </NavLink>

              </li>

            );

          })}

        </ul>

      </nav>

      {/* Logout */}

      <div className="border-t border-slate-200 p-4">

        <button
          onClick={handleLogout}
          className="flex w-full items-center justify-center gap-2 rounded-xl bg-red-600 px-4 py-3 font-semibold text-white transition hover:bg-red-700"
        >

          <LogOut size={18} />

          Logout

        </button>

      </div>

    </aside>
  );
}

export default HighSchoolSidebar;