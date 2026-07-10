import {
  GraduationCap,
  Brain,
  Code2,
  FileText,
  MessageSquare,
  Trophy,
  CheckCircle2,
  ArrowRight,
} from "lucide-react";

const modules = [
  {
    title: "Aptitude Practice",
    description:
      "Practice Quantitative Aptitude, Logical Reasoning and Verbal Ability.",
    progress: 70,
    icon: Brain,
  },
  {
    title: "Coding Practice",
    description:
      "Solve DSA problems and coding challenges for placements.",
    progress: 62,
    icon: Code2,
  },
  {
    title: "Resume Preparation",
    description:
      "Create an ATS-friendly resume and improve your resume score.",
    progress: 90,
    icon: FileText,
  },
  {
    title: "Mock Interview",
    description:
      "Practice HR and Technical interviews with AI feedback.",
    progress: 58,
    icon: MessageSquare,
  },
];

const companies = [
  "Google",
  "Microsoft",
  "Amazon",
  "Adobe",
  "Infosys",
  "TCS",
  "Accenture",
  "Wipro",
];

function PlacementPreparation() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Placement Preparation
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Track your placement readiness and prepare for
          top product and service-based companies.
        </p>

      </div>

      {/* Placement Score */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="flex items-center gap-4">

          <GraduationCap size={42} />

          <div>

            <h2 className="text-3xl font-bold">

              Placement Readiness Score

            </h2>

            <p className="mt-2 text-cyan-100">

              Your current placement readiness based on
              assessments, coding and resume.

            </p>

          </div>

        </div>

        <h1 className="mt-8 text-6xl font-bold">
          84%
        </h1>

      </div>

      {/* Preparation Modules */}

      <div className="grid gap-6 md:grid-cols-2">

        {modules.map((module) => {

          const Icon = module.icon;

          return (

            <div
              key={module.title}
              className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
            >

              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                <Icon size={30} />

              </div>

              <h2 className="mt-6 text-2xl font-bold text-slate-900">

                {module.title}

              </h2>

              <p className="mt-4 leading-7 text-slate-600">

                {module.description}

              </p>

              <div className="mt-6">

                <div className="mb-2 flex justify-between">

                  <span className="font-medium text-slate-700">
                    Progress
                  </span>

                  <span className="font-semibold text-cyan-600">
                    {module.progress}%
                  </span>

                </div>

                <div className="h-3 rounded-full bg-slate-200">

                  <div
                    className="h-3 rounded-full bg-cyan-600"
                    style={{
                      width: `${module.progress}%`,
                    }}
                  />

                </div>

              </div>

              <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

                Continue

                <ArrowRight size={18} />

              </button>

            </div>

          );

        })}

      </div>

      {/* Target Companies */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <h2 className="text-2xl font-bold text-slate-900">
          Target Companies
        </h2>

        <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-4">

          {companies.map((company) => (

            <div
              key={company}
              className="flex items-center gap-3 rounded-2xl border border-slate-200 p-5"
            >

              <CheckCircle2
                size={20}
                className="text-green-600"
              />

              <span className="font-semibold text-slate-700">
                {company}
              </span>

            </div>

          ))}

        </div>

      </div>

      {/* Final CTA */}

      <div className="rounded-3xl bg-slate-900 p-8 text-white">

        <div className="flex flex-col items-start justify-between gap-6 lg:flex-row lg:items-center">

          <div>

            <h2 className="text-3xl font-bold">

              Ready for Campus Placements?

            </h2>

            <p className="mt-3 text-slate-300">

              Complete all preparation modules to maximize
              your chances of getting placed.

            </p>

          </div>

          <button className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold transition hover:bg-cyan-700">

            <Trophy size={20} />

            Start Preparation

          </button>

        </div>

      </div>

    </div>
  );
}

export default PlacementPreparation;