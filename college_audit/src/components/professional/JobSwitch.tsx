import {
  Briefcase,
  Building2,
  MapPin,
  IndianRupee,
  TrendingUp,
  CalendarDays,
  ArrowRight,
} from "lucide-react";

const jobs = [
  {
    company: "Google",
    role: "Senior Software Engineer",
    location: "Bangalore",
    salary: "₹42 LPA",
    experience: "3+ Years",
    posted: "2 Days Ago",
  },
  {
    company: "Microsoft",
    role: "Full Stack Developer",
    location: "Hyderabad",
    salary: "₹38 LPA",
    experience: "2+ Years",
    posted: "1 Day Ago",
  },
  {
    company: "Amazon",
    role: "SDE II",
    location: "Bangalore",
    salary: "₹45 LPA",
    experience: "3+ Years",
    posted: "Today",
  },
  {
    company: "Adobe",
    role: "Frontend Engineer",
    location: "Noida",
    salary: "₹34 LPA",
    experience: "2+ Years",
    posted: "3 Days Ago",
  },
  {
    company: "Oracle",
    role: "Java Developer",
    location: "Pune",
    salary: "₹28 LPA",
    experience: "2+ Years",
    posted: "Today",
  },
  {
    company: "Salesforce",
    role: "Backend Engineer",
    location: "Hyderabad",
    salary: "₹36 LPA",
    experience: "3+ Years",
    posted: "Yesterday",
  },
];

function JobSwitch() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Job Switch
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Discover better career opportunities with AI-powered
          job recommendations.
        </p>

      </div>

      {/* Summary */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="grid gap-6 md:grid-cols-3">

          <div>

            <p className="text-cyan-100">
              Matching Jobs
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              56
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Average Salary Hike
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              +28%
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Profile Match
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              92%
            </h2>

          </div>

        </div>

      </div>

      {/* Job Cards */}

      <div className="grid gap-6">

        {jobs.map((job) => (

          <div
            key={`${job.company}-${job.role}`}
            className="rounded-3xl bg-white p-6 shadow-sm transition hover:shadow-xl"
          >

            <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">

              <div>

                <div className="flex items-center gap-4">

                  <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                    <Briefcase size={30} />

                  </div>

                  <div>

                    <h2 className="text-2xl font-bold text-slate-900">
                      {job.role}
                    </h2>

                    <p className="mt-1 text-slate-500">
                      {job.company}
                    </p>

                  </div>

                </div>

                <div className="mt-6 flex flex-wrap gap-6 text-slate-600">

                  <div className="flex items-center gap-2">

                    <Building2 size={18} />

                    {job.experience}

                  </div>

                  <div className="flex items-center gap-2">

                    <MapPin size={18} />

                    {job.location}

                  </div>

                  <div className="flex items-center gap-2">

                    <IndianRupee size={18} />

                    {job.salary}

                  </div>

                  <div className="flex items-center gap-2">

                    <CalendarDays size={18} />

                    {job.posted}

                  </div>

                </div>

              </div>

              <button className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700">

                Apply Now

                <ArrowRight size={18} />

              </button>

            </div>

          </div>

        ))}

      </div>

      {/* AI Suggestion */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <div className="flex items-center gap-4">

          <TrendingUp
            size={36}
            className="text-cyan-600"
          />

          <div>

            <h2 className="text-3xl font-bold text-slate-900">
              AI Recommendation
            </h2>

            <p className="mt-2 text-slate-600">
              Based on your profile, you have a high chance of
              receiving a <strong>25–35% salary hike</strong> by
              targeting Senior Software Engineer and Full Stack
              Developer roles.
            </p>

          </div>

        </div>

      </div>

    </div>
  );
}

export default JobSwitch;