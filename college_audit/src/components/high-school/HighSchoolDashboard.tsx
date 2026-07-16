import {
  useEffect,
  useState,
} from "react";

import {
  ArrowRight,
  BarChart3,
  BookOpen,
  Bot,
  CalendarDays,
  CheckCircle2,
  ClipboardList,
  Clock3,
  Compass,
  Map,
  Sparkles,
  Target,
  Trophy,
  UserRound,
} from "lucide-react";

import { useNavigate } from "react-router-dom";

import { useAuth } from "../../contexts/AuthContext";

import {
  calculateProfileCompletion,
  getHighSchoolProfile,
  type HighSchoolProfile as HighSchoolProfileData,
} from "../../services/highSchoolProfileService";

const cards = [
  {
    title: "Subject Guidance",
    description:
      "Explore subjects based on your academic profile.",
    icon: BookOpen,
    path: "/high-school-student/subject-guidance",
  },
  {
    title: "Career Explorer",
    description:
      "Discover career paths and future opportunities.",
    icon: Compass,
    path: "/high-school-student/career-explorer",
  },
  {
    title: "Learning Roadmap",
    description:
      "Follow a structured learning path for your goals.",
    icon: Map,
    path: "/high-school-student/learning-roadmap",
  },
  {
    title: "AI Learning Support",
    description:
      "Get learning support for academic questions.",
    icon: Bot,
    path: "/high-school-student/ai-learning-support",
  },
  {
    title: "Academic Progress",
    description:
      "Track your academic performance and progress.",
    icon: BarChart3,
    path: "/high-school-student/academic-progress",
  },
  {
    title: "Upcoming Exams",
    description:
      "View and manage your upcoming examinations.",
    icon: CalendarDays,
    path: "/high-school-student/upcoming-exams",
  },
  {
    title: "Assignments",
    description:
      "Manage pending and completed assignments.",
    icon: ClipboardList,
    path: "/high-school-student/assignments",
  },
  {
    title: "Daily Goal",
    description:
      "Stay focused on today's learning targets.",
    icon: Target,
    path: "/high-school-student/daily-goal",
  },
  {
    title: "Achievements",
    description:
      "View your milestones and achievements.",
    icon: Trophy,
    path: "/high-school-student/achievements",
  },
  {
    title: "Recent Activity",
    description:
      "See your latest learning and assessment activity.",
    icon: Clock3,
    path: "/high-school-student/assessment-reports",
  },
];

function HighSchoolDashboard() {
  const navigate = useNavigate();

  const { user } = useAuth();

  const [profile, setProfile] =
    useState<HighSchoolProfileData | null>(
      null
    );

  useEffect(() => {
    if (!user) {
      return;
    }

    const savedProfile =
      getHighSchoolProfile(user.id);

    setProfile(savedProfile);
  }, [user]);

  const profileCompletion =
    calculateProfileCompletion(profile);

  if (!user) {
    return null;
  }

  const currentStream = profile
    ? profile.studentClass === "10"
      ? "Not Selected Yet"
      : profile.currentStream ?? "Not Set"
    : "Not Set";

  return (
    <div className="mx-auto max-w-[1440px] space-y-6">
      {/* Welcome Section */}

      <section className="relative overflow-hidden rounded-[28px] border border-cyan-100 bg-white px-6 py-7 shadow-sm sm:px-8">
        <div className="pointer-events-none absolute -right-20 -top-24 h-64 w-64 rounded-full bg-cyan-100/60 blur-3xl" />

        <div className="pointer-events-none absolute right-32 top-10 h-32 w-32 rounded-full bg-blue-100/50 blur-3xl" />

        <div className="relative flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">
          <div className="max-w-2xl">
            <div className="mb-3 inline-flex items-center gap-2 rounded-full border border-cyan-100 bg-cyan-50 px-3 py-1.5 text-xs font-semibold text-cyan-700">
              <Sparkles size={14} />

              Student Workspace
            </div>

            <h1 className="text-3xl font-bold tracking-tight text-slate-950 sm:text-4xl">
              Welcome back, {user.name}
              <span className="ml-2">👋</span>
            </h1>

            <p className="mt-3 max-w-xl text-sm leading-6 text-slate-500 sm:text-base">
              Explore your academic progress,
              assessments and personalized career
              guidance from one place.
            </p>
          </div>

          <div className="flex flex-wrap gap-3">
            <button
              type="button"
              onClick={() =>
                navigate(
                  "/high-school-student/assessment"
                )
              }
              className="inline-flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 text-sm font-semibold text-white transition hover:bg-cyan-700"
            >
              Take Assessment

              <ArrowRight size={17} />
            </button>

            <button
              type="button"
              onClick={() =>
                navigate(
                  "/high-school-student/final-guidance"
                )
              }
              className="inline-flex items-center gap-2 rounded-xl border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 transition hover:bg-slate-50"
            >
              View Guidance
            </button>
          </div>
        </div>
      </section>

      {/* Academic Snapshot */}

      <section>
        <div className="mb-4 flex items-end justify-between">
          <div>
            <h2 className="text-xl font-bold text-slate-900">
              Academic Snapshot
            </h2>

            <p className="mt-1 text-sm text-slate-500">
              Your current academic profile at a glance.
            </p>
          </div>
        </div>

        <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-xs font-medium uppercase tracking-wide text-slate-400">
              Class
            </p>

            <h3 className="mt-2 text-xl font-bold text-slate-900">
              {profile
                ? `Class ${profile.studentClass}`
                : "Not Set"}
            </h3>
          </div>

          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-xs font-medium uppercase tracking-wide text-slate-400">
              Board
            </p>

            <h3 className="mt-2 text-xl font-bold text-slate-900">
              {profile?.board ?? "Not Set"}
            </h3>
          </div>

          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-xs font-medium uppercase tracking-wide text-slate-400">
              Current Stream
            </p>

            <h3 className="mt-2 text-lg font-bold text-slate-900">
              {currentStream}
            </h3>
          </div>

          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-xs font-medium uppercase tracking-wide text-slate-400">
              Career Goal
            </p>

            <h3 className="mt-2 text-lg font-bold text-slate-900">
              {profile?.careerGoal || "Exploring"}
            </h3>
          </div>
        </div>
      </section>

      {/* Profile Readiness */}

      <section className="grid gap-4 lg:grid-cols-[1.4fr_1fr]">
        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <div className="flex flex-col gap-5 sm:flex-row sm:items-center sm:justify-between">
            <div className="flex items-start gap-4">
              <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-cyan-50 text-cyan-600">
                <UserRound size={21} />
              </div>

              <div>
                <h2 className="font-bold text-slate-900">
                  Profile Readiness
                </h2>

                <p className="mt-1 text-sm text-slate-500">
                  Complete your academic details for
                  better guidance.
                </p>
              </div>
            </div>

            <span className="text-2xl font-bold text-slate-900">
              {profileCompletion}%
            </span>
          </div>

          <div className="mt-5 h-2 overflow-hidden rounded-full bg-slate-100">
            <div
              className="h-full rounded-full bg-cyan-500 transition-all"
              style={{
                width: `${profileCompletion}%`,
              }}
            />
          </div>

          <div className="mt-4 flex items-center justify-between gap-4">
            <div className="flex items-center gap-2 text-sm text-slate-500">
              {profileCompletion === 100 ? (
                <>
                  <CheckCircle2
                    size={17}
                    className="text-emerald-500"
                  />

                  Academic profile completed
                </>
              ) : (
                "Complete your profile to improve recommendations."
              )}
            </div>

            {profileCompletion < 100 && (
              <button
                type="button"
                onClick={() =>
                  navigate(
                    "/high-school-student/profile"
                  )
                }
                className="shrink-0 text-sm font-semibold text-cyan-700 hover:text-cyan-800"
              >
                Complete Profile
              </button>
            )}
          </div>
        </div>

        <div className="rounded-2xl border border-cyan-100 bg-cyan-50/60 p-6">
          <p className="text-xs font-semibold uppercase tracking-wide text-cyan-700">
            Recommended Next Step
          </p>

          <h2 className="mt-3 text-xl font-bold text-slate-900">
            Discover your stream direction
          </h2>

          <p className="mt-2 text-sm leading-6 text-slate-600">
            Complete subject assessments to generate
            your final stream guidance report.
          </p>

          <button
            type="button"
            onClick={() =>
              navigate(
                "/high-school-student/assessment"
              )
            }
            className="mt-5 inline-flex items-center gap-2 text-sm font-semibold text-cyan-700 hover:text-cyan-800"
          >
            Start assessment

            <ArrowRight size={16} />
          </button>
        </div>
      </section>

      {/* Explore Tools */}

      <section>
        <div className="mb-4">
          <h2 className="text-xl font-bold text-slate-900">
            Explore Your Workspace
          </h2>

          <p className="mt-1 text-sm text-slate-500">
            Tools to help you learn, track progress and
            plan your next step.
          </p>
        </div>

        <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
          {cards.map((card) => {
            const Icon = card.icon;

            return (
              <button
                key={card.title}
                type="button"
                onClick={() =>
                  navigate(card.path)
                }
                className="group rounded-2xl border border-slate-200 bg-white p-5 text-left shadow-sm transition hover:-translate-y-0.5 hover:border-cyan-200 hover:shadow-md"
              >
                <div className="flex items-start justify-between gap-4">
                  <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-slate-50 text-cyan-600 transition group-hover:bg-cyan-50">
                    <Icon size={21} />
                  </div>

                  <ArrowRight
                    size={18}
                    className="text-slate-300 transition group-hover:translate-x-1 group-hover:text-cyan-600"
                  />
                </div>

                <h3 className="mt-5 font-bold text-slate-900">
                  {card.title}
                </h3>

                <p className="mt-2 text-sm leading-6 text-slate-500">
                  {card.description}
                </p>
              </button>
            );
          })}
        </div>
      </section>
    </div>
  );
}

export default HighSchoolDashboard;