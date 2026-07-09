import {
  Trophy,
  Star,
  Medal,
  Award,
  BadgeCheck,
} from "lucide-react";

const achievements = [
  {
    title: "Fast Learner",
    description: "Completed your first learning roadmap.",
    icon: Star,
    color: "text-yellow-500",
    bg: "bg-yellow-100",
  },
  {
    title: "Subject Master",
    description: "Scored above 90% in Mathematics.",
    icon: Medal,
    color: "text-blue-600",
    bg: "bg-blue-100",
  },
  {
    title: "Weekly Champion",
    description: "Completed all weekly learning goals.",
    icon: Trophy,
    color: "text-orange-500",
    bg: "bg-orange-100",
  },
  {
    title: "Perfect Attendance",
    description: "Maintained consistent learning for 30 days.",
    icon: BadgeCheck,
    color: "text-green-600",
    bg: "bg-green-100",
  },
  {
    title: "Top Performer",
    description: "Achieved excellent academic performance.",
    icon: Award,
    color: "text-purple-600",
    bg: "bg-purple-100",
  },
  {
    title: "Career Explorer",
    description: "Explored all available career pathways.",
    icon: Star,
    color: "text-cyan-600",
    bg: "bg-cyan-100",
  },
];

function Achievements() {
  return (
    <div className="space-y-10">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Achievements
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Celebrate your milestones and unlock new achievement badges.
        </p>

      </div>

      {/* Summary */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-600 p-8 text-white shadow-lg">

        <h2 className="text-3xl font-bold">
          Your Progress
        </h2>

        <div className="mt-8 grid gap-6 md:grid-cols-3">

          <div>

            <p className="text-cyan-100">
              Total Badges
            </p>

            <h3 className="mt-2 text-4xl font-bold">
              18
            </h3>

          </div>

          <div>

            <p className="text-cyan-100">
              Current Level
            </p>

            <h3 className="mt-2 text-4xl font-bold">
              Gold
            </h3>

          </div>

          <div>

            <p className="text-cyan-100">
              Rank
            </p>

            <h3 className="mt-2 text-4xl font-bold">
              #12
            </h3>

          </div>

        </div>

      </div>

      {/* Achievement Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {achievements.map((item) => {

          const Icon = item.icon;

          return (

            <div
              key={item.title}
              className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
            >

              <div
                className={`flex h-16 w-16 items-center justify-center rounded-2xl ${item.bg} ${item.color}`}
              >

                <Icon size={30} />

              </div>

              <h2 className="mt-6 text-2xl font-bold text-slate-900">

                {item.title}

              </h2>

              <p className="mt-4 leading-7 text-slate-600">

                {item.description}

              </p>

              <span className="mt-6 inline-block rounded-full bg-green-100 px-4 py-2 text-sm font-semibold text-green-700">

                Unlocked

              </span>

            </div>

          );

        })}

      </div>

    </div>
  );
}

export default Achievements;