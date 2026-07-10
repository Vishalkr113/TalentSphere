import { NavLink } from "react-router-dom";

import {
  LayoutDashboard,
  User,
  FileText,
  ScanSearch,
  Code2,
  Brain,
  MessageSquare,
  Compass,
  Map,
  Award,
  Briefcase,
  GraduationCap,
  Trophy,
  Settings,
  LogOut,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

const menuItems = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    path: "/college-student/dashboard",
  },
  {
    title: "My Profile",
    icon: User,
    path: "/college-student/profile",
  },
  {
    title: "Resume Builder",
    icon: FileText,
    path: "/college-student/resume-builder",
  },
  {
    title: "Resume Analyzer",
    icon: ScanSearch,
    path: "/college-student/resume-analyzer",
  },
  {
    title: "Coding Assessment",
    icon: Code2,
    path: "/college-student/coding-assessment",
  },
  {
    title: "Skill Assessment",
    icon: Brain,
    path: "/college-student/skill-assessment",
  },
  {
    title: "Mock Interview",
    icon: MessageSquare,
    path: "/college-student/mock-interview",
  },
  {
    title: "Career Recommendation",
    icon: Compass,
    path: "/college-student/career-recommendation",
  },
  {
    title: "Learning Roadmap",
    icon: Map,
    path: "/college-student/learning-roadmap",
  },
  {
    title: "Certificates",
    icon: Award,
    path: "/college-student/certificates",
  },
  {
    title: "Jobs & Internships",
    icon: Briefcase,
    path: "/college-student/jobs",
  },
  {
    title: "Placement Preparation",
    icon: GraduationCap,
    path: "/college-student/placement-preparation",
  },
  {
    title: "Achievements",
    icon: Trophy,
    path: "/college-student/achievements",
  },
  {
    title: "Settings",
    icon: Settings,
    path: "/college-student/settings",
  },
];

function CollegeSidebar() {
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
          College Student Portal
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

export default CollegeSidebar;