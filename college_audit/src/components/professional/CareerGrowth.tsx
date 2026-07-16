import {
  TrendingUp,
  Target,
  Briefcase,
  Award,
  ArrowRight,
  CheckCircle2,
} from "lucide-react";

const goals = [
  {
    title: "Promotion Readiness",
    description:
      "Improve leadership, communication and technical expertise.",
    progress: 82,
  },
  {
    title: "Leadership Skills",
    description:
      "Develop management and decision-making capabilities.",
    progress: 68,
  },
  {
    title: "Technical Expertise",
    description:
      "Master advanced technologies for career growth.",
    progress: 76,
  },
  {
    title: "Industry Networking",
    description:
      "Expand your professional network and opportunities.",
    progress: 54,
  },
];

const milestones = [
  "Complete Advanced Technical Certification",
  "Lead a Project Successfully",
  "Improve Communication Skills",
  "Build Strong Professional Network",
  "Prepare for Promotion Review",
];

function CareerGrowth() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Career Growth
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Track your professional growth and achieve
          your long-term career goals.
        </p>

      </div>

      {/* Career Score */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="flex items-center gap-4">

          <TrendingUp size={42} />

          <div>

            <h2 className="text-3xl font-bold">

              Career Growth Score

            </h2>

            <p className="mt-2 text-cyan-100">

              Based on skills, experience and career progress.

            </p>

          </div>

        </div>

        <h1 className="mt-8 text-6xl font-bold">
          87%
        </h1>

      </div>

      {/* Growth Cards */}

      <div className="grid gap-6 md:grid-cols-2">

        {goals.map((goal) => (

          <div
            key={goal.title}
            className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
          >

            <div className="flex items-center gap-4">

              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                <Target size={30} />

              </div>

              <div>

                <h2 className="text-2xl font-bold text-slate-900">
                  {goal.title}
                </h2>

                <p className="mt-2 text-slate-600">
                  {goal.description}
                </p>

              </div>

            </div>

            <div className="mt-6">

              <div className="mb-2 flex justify-between">

                <span className="font-medium">
                  Progress
                </span>

                <span className="font-semibold text-cyan-600">
                  {goal.progress}%
                </span>

              </div>

              <div className="h-3 rounded-full bg-slate-200">

                <div
                  className="h-3 rounded-full bg-cyan-600"
                  style={{
                    width: `${goal.progress}%`,
                  }}
                />

              </div>

            </div>

            <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

              Continue

              <ArrowRight size={18} />

            </button>

          </div>

        ))}

      </div>

      {/* Career Milestones */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <div className="mb-8 flex items-center gap-4">

          <div className="rounded-2xl bg-cyan-100 p-4 text-cyan-600">

            <Award size={30} />

          </div>

          <div>

            <h2 className="text-2xl font-bold">
              Career Milestones
            </h2>

            <p className="text-slate-500">
              Recommended next steps for your career.
            </p>

          </div>

        </div>

        <div className="space-y-5">

          {milestones.map((item) => (

            <div
              key={item}
              className="flex items-center gap-4 rounded-2xl border border-slate-200 p-5"
            >

              <CheckCircle2
                size={22}
                className="text-green-600"
              />

              <span className="font-medium text-slate-700">
                {item}
              </span>

            </div>

          ))}

        </div>

      </div>

      {/* Promotion Card */}

      <div className="rounded-3xl bg-slate-900 p-8 text-white">

        <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">

          <div>

            <h2 className="text-3xl font-bold">

              Ready for Your Next Promotion?

            </h2>

            <p className="mt-3 text-slate-300">

              Complete your career roadmap and improve your
              promotion readiness score.

            </p>

          </div>

          <button className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold transition hover:bg-cyan-700">

            <Briefcase size={20} />

            Explore Opportunities

          </button>

        </div>

      </div>

    </div>
  );
}

export default CareerGrowth;