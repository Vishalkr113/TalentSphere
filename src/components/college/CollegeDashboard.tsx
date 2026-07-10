import {
  FileText,
  ScanSearch,
  Code2,
  Brain,
  MessageSquare,
  Compass,
  Trophy,
  Target,
  Briefcase,
  CalendarDays,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

const features = [
  {
    title: "Resume Builder",
    description: "Create an ATS-friendly professional resume.",
    icon: FileText,
    path: "/college-student/resume-builder",
  },
  {
    title: "Resume Analyzer",
    description: "Analyze and improve your resume using AI.",
    icon: ScanSearch,
    path: "/college-student/resume-analyzer",
  },
  {
    title: "Coding Assessment",
    description: "Practice coding and improve problem-solving.",
    icon: Code2,
    path: "/college-student/coding-assessment",
  },
  {
    title: "Skill Assessment",
    description: "Evaluate technical and aptitude skills.",
    icon: Brain,
    path: "/college-student/skill-assessment",
  },
  {
    title: "Mock Interview",
    description: "Prepare with AI-powered mock interviews.",
    icon: MessageSquare,
    path: "/college-student/mock-interview",
  },
  {
    title: "Career Recommendation",
    description: "Get personalized AI career guidance.",
    icon: Compass,
    path: "/college-student/career-recommendation",
  },
];

function CollegeDashboard() {
  const { user } = useAuth();

  return (
    <div className="space-y-8">

      {/* Welcome */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white shadow-lg">

        <h1 className="text-4xl font-bold">

          Welcome, {user?.name} 👋

        </h1>

        <p className="mt-3 text-cyan-100">

          College Student Dashboard

        </p>

        <div className="mt-8 grid gap-6 md:grid-cols-4">

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-sm text-cyan-100">

              Semester

            </p>

            <h2 className="mt-2 text-3xl font-bold">

              6th

            </h2>

          </div>

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-sm text-cyan-100">

              CGPA

            </p>

            <h2 className="mt-2 text-3xl font-bold">

              8.25

            </h2>

          </div>

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-sm text-cyan-100">

              Placement Score

            </p>

            <h2 className="mt-2 text-3xl font-bold">

              78%

            </h2>

          </div>

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-sm text-cyan-100">

              Resume Score

            </p>

            <h2 className="mt-2 text-3xl font-bold">

              82%

            </h2>

          </div>

        </div>

      </div>

      {/* Main Features */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {features.map((item) => {

          const Icon = item.icon;

          return (

            <div
              key={item.title}
              className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
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

              <button className="mt-6 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

                Open Module

              </button>

            </div>

          );

        })}

      </div>

      {/* Analytics */}

      <div className="grid gap-6 lg:grid-cols-2">

        <div className="rounded-3xl bg-white p-8 shadow-sm">

          <h2 className="mb-6 text-2xl font-bold text-slate-900">

            Weekly Progress

          </h2>

          <div className="space-y-5">

            <div>

              <div className="mb-2 flex justify-between">

                <span>Coding Practice</span>

                <span>75%</span>

              </div>

              <div className="h-3 rounded-full bg-slate-200">

                <div className="h-3 w-3/4 rounded-full bg-cyan-600"></div>

              </div>

            </div>

            <div>

              <div className="mb-2 flex justify-between">

                <span>Resume Completion</span>

                <span>90%</span>

              </div>

              <div className="h-3 rounded-full bg-slate-200">

                <div className="h-3 w-[90%] rounded-full bg-green-600"></div>

              </div>

            </div>

            <div>

              <div className="mb-2 flex justify-between">

                <span>Mock Interview</span>

                <span>45%</span>

              </div>

              <div className="h-3 rounded-full bg-slate-200">

                <div className="h-3 w-[45%] rounded-full bg-orange-500"></div>

              </div>

            </div>

          </div>

        </div>

        <div className="rounded-3xl bg-white p-8 shadow-sm">

          <h2 className="mb-6 text-2xl font-bold text-slate-900">

            Quick Overview

          </h2>

          <div className="space-y-5">

            <div className="flex items-center gap-4">

              <Target className="text-cyan-600" />

              <span>Daily Goal Completed</span>

            </div>

            <div className="flex items-center gap-4">

              <CalendarDays className="text-cyan-600" />

              <span>Next Assessment Tomorrow</span>

            </div>

            <div className="flex items-center gap-4">

              <Briefcase className="text-cyan-600" />

              <span>5 Internship Opportunities</span>

            </div>

            <div className="flex items-center gap-4">

              <Trophy className="text-cyan-600" />

              <span>12 Achievements Earned</span>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default CollegeDashboard;