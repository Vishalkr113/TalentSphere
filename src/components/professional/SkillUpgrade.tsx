import {
  Brain,
  Code2,
  Database,
  Cloud,
  Shield,
  BarChart3,
  ArrowRight,
  TrendingUp,
} from "lucide-react";

const skills = [
  {
    title: "Artificial Intelligence",
    description:
      "Learn AI, Machine Learning and Generative AI.",
    progress: 62,
    icon: Brain,
  },
  {
    title: "Full Stack Development",
    description:
      "Master React, Node.js and modern web technologies.",
    progress: 78,
    icon: Code2,
  },
  {
    title: "Data Engineering",
    description:
      "SQL, Big Data, ETL and Data Warehousing.",
    progress: 48,
    icon: Database,
  },
  {
    title: "Cloud Computing",
    description:
      "AWS, Azure, Docker and Kubernetes.",
    progress: 55,
    icon: Cloud,
  },
  {
    title: "Cyber Security",
    description:
      "Network Security, Ethical Hacking and SOC.",
    progress: 40,
    icon: Shield,
  },
  {
    title: "Data Analytics",
    description:
      "Power BI, Tableau, Excel and Business Analytics.",
    progress: 70,
    icon: BarChart3,
  },
];

function SkillUpgrade() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Skill Upgrade
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Upgrade your skills with trending technologies
          and stay ahead in your career.
        </p>

      </div>

      {/* Skill Score */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="flex items-center gap-4">

          <TrendingUp size={42} />

          <div>

            <h2 className="text-3xl font-bold">

              Skill Readiness

            </h2>

            <p className="mt-2 text-cyan-100">

              Overall learning progress across all technologies.

            </p>

          </div>

        </div>

        <h1 className="mt-8 text-6xl font-bold">
          76%
        </h1>

      </div>

      {/* Skill Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {skills.map((skill) => {

          const Icon = skill.icon;

          return (

            <div
              key={skill.title}
              className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
            >

              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                <Icon size={30} />

              </div>

              <h2 className="mt-6 text-2xl font-bold text-slate-900">
                {skill.title}
              </h2>

              <p className="mt-4 leading-7 text-slate-600">
                {skill.description}
              </p>

              <div className="mt-6">

                <div className="mb-2 flex justify-between">

                  <span>Progress</span>

                  <span className="font-semibold text-cyan-600">
                    {skill.progress}%
                  </span>

                </div>

                <div className="h-3 rounded-full bg-slate-200">

                  <div
                    className="h-3 rounded-full bg-cyan-600"
                    style={{
                      width: `${skill.progress}%`,
                    }}
                  />

                </div>

              </div>

              <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

                Continue Learning

                <ArrowRight size={18} />

              </button>

            </div>

          );

        })}

      </div>

    </div>
  );
}

export default SkillUpgrade;