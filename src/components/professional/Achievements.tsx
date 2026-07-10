import {
  Trophy,
  Award,
  Medal,
  Star,
  BadgeCheck,
  TrendingUp,
} from "lucide-react";

const achievements = [
  {
    title: "Promotion Achieved",
    description:
      "Successfully received a promotion based on outstanding performance.",
    icon: Trophy,
    color: "text-yellow-600",
    bg: "bg-yellow-100",
  },
  {
    title: "Top Performer",
    description:
      "Recognized as a top performer for exceptional project delivery.",
    icon: Medal,
    color: "text-cyan-600",
    bg: "bg-cyan-100",
  },
  {
    title: "Certification Expert",
    description:
      "Earned multiple industry-recognized professional certifications.",
    icon: Award,
    color: "text-green-600",
    bg: "bg-green-100",
  },
  {
    title: "Interview Success",
    description:
      "Successfully cleared multiple technical and HR interviews.",
    icon: BadgeCheck,
    color: "text-purple-600",
    bg: "bg-purple-100",
  },
  {
    title: "Skill Master",
    description:
      "Completed advanced learning paths and mastered new technologies.",
    icon: Star,
    color: "text-orange-500",
    bg: "bg-orange-100",
  },
  {
    title: "Career Growth",
    description:
      "Consistently improved career score and professional development.",
    icon: TrendingUp,
    color: "text-pink-600",
    bg: "bg-pink-100",
  },
];

function Achievements() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Achievements
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Celebrate your professional milestones, certifications
          and career accomplishments.
        </p>

      </div>

      {/* Summary */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="grid gap-6 md:grid-cols-4">

          <div>

            <p className="text-cyan-100">
              Total Achievements
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              32
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Badges Earned
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              18
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Certifications
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              24
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Career Score
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              91%
            </h2>

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
              className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
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

                Achieved

              </span>

            </div>

          );

        })}

      </div>

    </div>
  );
}

export default Achievements;