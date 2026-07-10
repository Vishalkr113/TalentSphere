import {
  Briefcase,
  Brain,
  TrendingUp,
  GraduationCap,
  ArrowRight,
  Star,
} from "lucide-react";

const careers = [
  {
    title: "Software Engineer",
    match: "96%",
    salary: "₹6L - ₹30L+",
    skills: "React • Java • Python • DSA",
  },
  {
    title: "Data Scientist",
    match: "91%",
    salary: "₹8L - ₹35L+",
    skills: "Python • SQL • ML • Statistics",
  },
  {
    title: "AI / ML Engineer",
    match: "89%",
    salary: "₹10L - ₹40L+",
    skills: "Deep Learning • Python • AI",
  },
  {
    title: "Full Stack Developer",
    match: "94%",
    salary: "₹7L - ₹28L+",
    skills: "React • Node • MongoDB",
  },
  {
    title: "Cyber Security Analyst",
    match: "86%",
    salary: "₹7L - ₹25L+",
    skills: "Networking • Linux • Security",
  },
  {
    title: "Cloud Engineer",
    match: "88%",
    salary: "₹8L - ₹30L+",
    skills: "AWS • Azure • Docker • DevOps",
  },
];

function CareerRecommendation() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          AI Career Recommendation
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Discover the best career paths based on your skills,
          interests, projects and assessment results.
        </p>

      </div>

      {/* AI Recommendation */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="flex items-center gap-4">

          <Brain size={44} />

          <div>

            <h2 className="text-3xl font-bold">

              Your Best Career Match

            </h2>

            <p className="mt-2 text-cyan-100">

              Based on your profile, coding performance,
              resume and assessments.

            </p>

          </div>

        </div>

        <div className="mt-10 grid gap-6 md:grid-cols-3">

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-cyan-100">

              Recommended Career

            </p>

            <h3 className="mt-2 text-2xl font-bold">

              Software Engineer

            </h3>

          </div>

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-cyan-100">

              Match Score

            </p>

            <h3 className="mt-2 text-2xl font-bold">

              96%

            </h3>

          </div>

          <div className="rounded-2xl bg-white/10 p-5">

            <p className="text-cyan-100">

              Placement Readiness

            </p>

            <h3 className="mt-2 text-2xl font-bold">

              84%

            </h3>

          </div>

        </div>

      </div>

      {/* Career Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {careers.map((career) => (

          <div
            key={career.title}
            className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
          >

            <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

              <Briefcase size={30} />

            </div>

            <h2 className="mt-6 text-2xl font-bold text-slate-900">

              {career.title}

            </h2>

            <div className="mt-5 space-y-3">

              <div className="flex items-center gap-2 text-slate-600">

                <TrendingUp size={18} />

                Match : {career.match}

              </div>

              <div className="flex items-center gap-2 text-slate-600">

                <GraduationCap size={18} />

                {career.skills}

              </div>

              <div className="flex items-center gap-2 text-slate-600">

                <Star size={18} />

                {career.salary}

              </div>

            </div>

            <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

              Explore Career

              <ArrowRight size={18} />

            </button>

          </div>

        ))}

      </div>

    </div>
  );
}

export default CareerRecommendation;