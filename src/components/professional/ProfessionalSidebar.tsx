import { NavLink } from "react-router-dom";

import {
  LayoutDashboard,
  User,
  TrendingUp,
  Brain,
  FileText,
  MessageSquare,
  Briefcase,
  IndianRupee,
  BookOpen,
  Award,
  Trophy,
  Settings,
  LogOut,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

const menuItems = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    path: "/working-professional/dashboard",
  },
  {
    title: "My Profile",
    icon: User,
    path: "/working-professional/profile",
  },
  {
    title: "Career Growth",
    icon: TrendingUp,
    path: "/working-professional/career-growth",
  },
  {
    title: "Skill Assessment",
    icon: Brain,
    path: "/working-professional/skill-assessment",
  },
  {
    title: "Resume Manager",
    icon: FileText,
    path: "/working-professional/resume-manager",
  },
  {
    title: "Interview Preparation",
    icon: MessageSquare,
    path: "/working-professional/interview-preparation",
  },
  {
    title: "Job Switch",
    icon: Briefcase,
    path: "/working-professional/job-switch",
  },
  {
    title: "Salary Insights",
    icon: IndianRupee,
    path: "/working-professional/salary-insights",
  },
  {
    title: "Learning Hub",
    icon: BookOpen,
    path: "/working-professional/learning-hub",
  },
  {
    title: "Certificates",
    icon: Award,
    path: "/working-professional/certificates",
  },
  {
    title: "Achievements",
    icon: Trophy,
    path: "/working-professional/achievements",
  },
  {
    title: "Settings",
    icon: Settings,
    path: "/working-professional/settings",
  },
];

function ProfessionalSidebar() {
  const { logout } = useAuth();

  const handleLogout = () => {
    logout();
    window.location.href = "/";
  };

  return (
    <aside className="fixed left-0 top-0 flex h-screen w-72 flex-col border-r border-slate-200 bg-white">

      {/* Logo */}

      <div className="border-b border-slate-200 p-6">

        <h1 className="text-2xl font-bold text-cyan-600">
          TalentSphere
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          Professional Portal
        </p>

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

export default ProfessionalSidebar;