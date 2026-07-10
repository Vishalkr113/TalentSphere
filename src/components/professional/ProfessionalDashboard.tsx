import {
  Briefcase,
  TrendingUp,
  Brain,
  FileText,
  MessageSquare,
  IndianRupee,
  BookOpen,
  Award,
  Target,
  CalendarDays,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

const modules = [
  {
    title: "Career Growth",
    description: "Track your career progress and promotion readiness.",
    icon: TrendingUp,
  },
  {
    title: "Skill Upgrade",
    description: "Learn trending technologies and stay industry ready.",
    icon: Brain,
  },
  {
    title: "Resume Manager",
    description: "Maintain an ATS-friendly professional resume.",
    icon: FileText,
  },
  {
    title: "Interview Preparation",
    description: "Practice HR and technical interviews with AI.",
    icon: MessageSquare,
  },
  {
    title: "Job Switch",
    description: "Explore better opportunities with AI recommendations.",
    icon: Briefcase,
  },
  {
    title: "Salary Insights",
    description: "Compare salaries based on role, skills and experience.",
    icon: IndianRupee,
  },
];

function ProfessionalDashboard() {
  const { user } = useAuth();

  return (
    <div className="space-y-8">

      {/* Welcome */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white shadow-lg">

        <h1 className="text-4xl font-bold">

          Welcome, {user?.name} 👋

        </h1>

        <p className="mt-3 text-cyan-100">

          Working Professional Dashboard

        </p>

        <div className="mt-8 grid gap-6 md:grid-cols-4">

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-sm text-cyan-100">
              Experience
            </p>

            <h2 className="mt-2 text-3xl font-bold">
              2 Years
            </h2>

          </div>

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-sm text-cyan-100">
              Career Score
            </p>

            <h2 className="mt-2 text-3xl font-bold">
              87%
            </h2>

          </div>

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-sm text-cyan-100">
              Resume Score
            </p>

            <h2 className="mt-2 text-3xl font-bold">
              91%
            </h2>

          </div>

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-sm text-cyan-100">
              Skill Score
            </p>

            <h2 className="mt-2 text-3xl font-bold">
              84%
            </h2>

          </div>

        </div>

      </div>

      {/* Modules */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {modules.map((item) => {

          const Icon = item.icon;

          return (

            <div
              key={item.title}
              className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
            >

              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                <Icon size={30} />

              </div>

              <h2 className="mt-6 text-2xl font-bold text-slate-900">

                {item.title}

              </h2>

              <p className="mt-4 leading-7 text-slate-600">

                {item.description}

              </p>

              <button className="mt-8 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

                Open Module

              </button>

            </div>

          );

        })}

      </div>

      {/* Analytics */}

      <div className="grid gap-6 lg:grid-cols-2">

        <div className="rounded-3xl bg-white p-8 shadow-sm">

          <h2 className="mb-6 text-2xl font-bold">
            Career Progress
          </h2>

          <div className="space-y-6">

            <div>

              <div className="mb-2 flex justify-between">

                <span>Promotion Readiness</span>

                <span>82%</span>

              </div>

              <div className="h-3 rounded-full bg-slate-200">

                <div className="h-3 w-[82%] rounded-full bg-cyan-600"></div>

              </div>

            </div>

            <div>

              <div className="mb-2 flex justify-between">

                <span>Skill Upgrade</span>

                <span>74%</span>

              </div>

              <div className="h-3 rounded-full bg-slate-200">

                <div className="h-3 w-3/4 rounded-full bg-green-600"></div>

              </div>

            </div>

            <div>

              <div className="mb-2 flex justify-between">

                <span>Interview Readiness</span>

                <span>89%</span>

              </div>

              <div className="h-3 rounded-full bg-slate-200">

                <div className="h-3 w-[89%] rounded-full bg-orange-500"></div>

              </div>

            </div>

          </div>

        </div>

        <div className="rounded-3xl bg-white p-8 shadow-sm">

          <h2 className="mb-6 text-2xl font-bold">

            Quick Overview

          </h2>

          <div className="space-y-5">

            <div className="flex items-center gap-4">

              <Target className="text-cyan-600" />

              <span>Career Goal Updated</span>

            </div>

            <div className="flex items-center gap-4">

              <CalendarDays className="text-cyan-600" />

              <span>Interview Tomorrow</span>

            </div>

            <div className="flex items-center gap-4">

              <BookOpen className="text-cyan-600" />

              <span>3 Courses In Progress</span>

            </div>

            <div className="flex items-center gap-4">

              <Award className="text-cyan-600" />

              <span>18 Certificates Earned</span>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default ProfessionalDashboard;