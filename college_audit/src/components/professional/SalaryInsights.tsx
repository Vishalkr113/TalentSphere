import {
  IndianRupee,
  TrendingUp,
  Briefcase,
  BarChart3,
  ArrowRight,
  Target,
} from "lucide-react";

const salaries = [
  {
    role: "Software Engineer",
    experience: "2-4 Years",
    average: "₹14 LPA",
    top: "₹24 LPA",
  },
  {
    role: "Senior Software Engineer",
    experience: "4-6 Years",
    average: "₹24 LPA",
    top: "₹40 LPA",
  },
  {
    role: "Full Stack Developer",
    experience: "3-5 Years",
    average: "₹20 LPA",
    top: "₹36 LPA",
  },
  {
    role: "AI / ML Engineer",
    experience: "2-5 Years",
    average: "₹22 LPA",
    top: "₹45 LPA",
  },
  {
    role: "Cloud Engineer",
    experience: "3-6 Years",
    average: "₹21 LPA",
    top: "₹38 LPA",
  },
  {
    role: "DevOps Engineer",
    experience: "3-5 Years",
    average: "₹19 LPA",
    top: "₹35 LPA",
  },
];

function SalaryInsights() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Salary Insights
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Compare salary trends based on role, experience
          and industry with AI-powered insights.
        </p>

      </div>

      {/* Salary Summary */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="grid gap-6 md:grid-cols-3">

          <div>

            <p className="text-cyan-100">

              Current Estimated Salary

            </p>

            <h2 className="mt-2 text-4xl font-bold">

              ₹12 LPA

            </h2>

          </div>

          <div>

            <p className="text-cyan-100">

              Market Average

            </p>

            <h2 className="mt-2 text-4xl font-bold">

              ₹16 LPA

            </h2>

          </div>

          <div>

            <p className="text-cyan-100">

              Expected Hike

            </p>

            <h2 className="mt-2 text-4xl font-bold">

              +32%

            </h2>

          </div>

        </div>

      </div>

      {/* Salary Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {salaries.map((salary) => (

          <div
            key={salary.role}
            className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
          >

            <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

              <Briefcase size={30} />

            </div>

            <h2 className="mt-6 text-2xl font-bold text-slate-900">

              {salary.role}

            </h2>

            <div className="mt-6 space-y-3 text-slate-600">

              <div>

                Experience : {salary.experience}

              </div>

              <div className="flex items-center gap-2">

                <IndianRupee size={18} />

                Average : {salary.average}

              </div>

              <div className="flex items-center gap-2">

                <TrendingUp size={18} />

                Top Salary : {salary.top}

              </div>

            </div>

            <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

              View Details

              <ArrowRight size={18} />

            </button>

          </div>

        ))}

      </div>

      {/* AI Recommendation */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <div className="flex items-center gap-4">

          <Target
            size={34}
            className="text-cyan-600"
          />

          <div>

            <h2 className="text-3xl font-bold text-slate-900">

              AI Salary Recommendation

            </h2>

            <p className="mt-3 text-slate-600">

              Upskilling in <strong>AWS</strong>,
              <strong> System Design</strong> and
              <strong> Generative AI</strong> can increase
              your expected salary by
              <strong> 30% - 45%</strong> within the next
              12 months.

            </p>

          </div>

        </div>

      </div>

      {/* Salary Growth */}

      <div className="rounded-3xl bg-slate-900 p-8 text-white">

        <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">

          <div>

            <div className="flex items-center gap-3">

              <BarChart3 size={32} />

              <h2 className="text-3xl font-bold">

                Salary Growth Tracker

              </h2>

            </div>

            <p className="mt-4 text-slate-300">

              Track your salary growth and compare it
              with current industry standards.

            </p>

          </div>

          <button className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold transition hover:bg-cyan-700">

            View Analytics

            <ArrowRight size={18} />

          </button>

        </div>

      </div>

    </div>
  );
}

export default SalaryInsights;