import {
  BookOpen,
  Compass,
  Map,
  Bot,
  BarChart3,
  CalendarDays,
  ClipboardList,
  Target,
  Trophy,
  Clock3,
} from "lucide-react";

import { useAuth } from "../../contexts/AuthContext";

const cards = [
  {
    title: "Subject Guidance",
    description: "Choose subjects with AI-powered recommendations.",
    icon: BookOpen,
  },
  {
    title: "Career Explorer",
    description: "Explore Engineering, Medical, Commerce and more.",
    icon: Compass,
  },
  {
    title: "Learning Roadmap",
    description: "Personalized roadmap based on your goals.",
    icon: Map,
  },
  {
    title: "AI Learning Support",
    description: "Get instant AI help for your studies.",
    icon: Bot,
  },
  {
    title: "Academic Progress",
    description: "Track your overall academic performance.",
    icon: BarChart3,
  },
  {
    title: "Upcoming Exams",
    description: "View your upcoming school examinations.",
    icon: CalendarDays,
  },
  {
    title: "Assignments",
    description: "Manage pending and completed assignments.",
    icon: ClipboardList,
  },
  {
    title: "Daily Goal",
    description: "Complete today's learning targets.",
    icon: Target,
  },
  {
    title: "Achievements",
    description: "Earn badges and celebrate milestones.",
    icon: Trophy,
  },
  {
    title: "Recent Activity",
    description: "See your latest learning activities.",
    icon: Clock3,
  },
];

function HighSchoolDashboard() {
  const { user } = useAuth();

  return (
    <div className="space-y-8">

      {/* Welcome Card */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-600 p-8 text-white shadow-lg">

        <h1 className="text-3xl font-bold">
          Welcome, {user?.name} 👋
        </h1>

        <p className="mt-3 text-cyan-100">
          High School Student Dashboard
        </p>

        <div className="mt-8 grid gap-6 md:grid-cols-4">

          <div className="rounded-2xl bg-white/10 p-5">
            <p className="text-sm text-cyan-100">
              Class
            </p>
            <h3 className="mt-2 text-2xl font-bold">
              10
            </h3>
          </div>

          <div className="rounded-2xl bg-white/10 p-5">
            <p className="text-sm text-cyan-100">
              Board
            </p>
            <h3 className="mt-2 text-2xl font-bold">
              CBSE
            </h3>
          </div>

          <div className="rounded-2xl bg-white/10 p-5">
            <p className="text-sm text-cyan-100">
              Career Goal
            </p>
            <h3 className="mt-2 text-lg font-bold">
              Software Engineer
            </h3>
          </div>

          <div className="rounded-2xl bg-white/10 p-5">
            <p className="text-sm text-cyan-100">
              Profile Completion
            </p>

            <div className="mt-3 h-3 overflow-hidden rounded-full bg-white/20">
              <div className="h-full w-3/5 rounded-full bg-white"></div>
            </div>

            <p className="mt-2 font-semibold">
              60%
            </p>

          </div>

        </div>

      </div>

      {/* Feature Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {cards.map((card) => {

          const Icon = card.icon;

          return (

            <div
              key={card.title}
              className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-lg"
            >

              <div className="flex h-14 w-14 items-center justify-center rounded-xl bg-cyan-100 text-cyan-600">

                <Icon size={28} />

              </div>

              <h2 className="mt-6 text-xl font-bold text-slate-900">

                {card.title}

              </h2>

              <p className="mt-3 text-slate-600 leading-7">

                {card.description}

              </p>

              <button className="mt-6 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

                Open

              </button>

            </div>

          );

        })}

      </div>

    </div>
  );
}

export default HighSchoolDashboard;