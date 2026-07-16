import {
  Briefcase,
  Building2,
  MapPin,
  IndianRupee,
  CalendarDays,
  ArrowRight,
} from "lucide-react";

const jobs = [
  {
    company: "Google",
    role: "Software Engineering Intern",
    location: "Bangalore",
    stipend: "₹80,000 / Month",
    type: "Internship",
    deadline: "15 Aug 2026",
  },
  {
    company: "Microsoft",
    role: "Frontend Developer Intern",
    location: "Hyderabad",
    stipend: "₹70,000 / Month",
    type: "Internship",
    deadline: "20 Aug 2026",
  },
  {
    company: "Amazon",
    role: "SDE - I",
    location: "Bangalore",
    stipend: "₹18 LPA",
    type: "Full Time",
    deadline: "28 Aug 2026",
  },
  {
    company: "Infosys",
    role: "Systems Engineer",
    location: "Pune",
    stipend: "₹6.5 LPA",
    type: "Full Time",
    deadline: "05 Sep 2026",
  },
  {
    company: "TCS",
    role: "Digital Role",
    location: "Noida",
    stipend: "₹7 LPA",
    type: "Placement",
    deadline: "12 Sep 2026",
  },
  {
    company: "Accenture",
    role: "Associate Software Engineer",
    location: "Mumbai",
    stipend: "₹6 LPA",
    type: "Placement",
    deadline: "18 Sep 2026",
  },
];

function JobsInternships() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Jobs & Internships
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Explore internships and job opportunities
          recommended by AI based on your profile.
        </p>

      </div>

      {/* Summary */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <h2 className="text-3xl font-bold">

          AI Job Recommendations

        </h2>

        <div className="mt-8 grid gap-6 md:grid-cols-3">

          <div>

            <p className="text-cyan-100">

              Matching Jobs

            </p>

            <h2 className="mt-2 text-4xl font-bold">

              32

            </h2>

          </div>

          <div>

            <p className="text-cyan-100">

              Internships

            </p>

            <h2 className="mt-2 text-4xl font-bold">

              18

            </h2>

          </div>

          <div>

            <p className="text-cyan-100">

              Placement Readiness

            </p>

            <h2 className="mt-2 text-4xl font-bold">

              84%

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

                    {job.type}

                  </div>

                  <div className="flex items-center gap-2">

                    <MapPin size={18} />

                    {job.location}

                  </div>

                  <div className="flex items-center gap-2">

                    <IndianRupee size={18} />

                    {job.stipend}

                  </div>

                  <div className="flex items-center gap-2">

                    <CalendarDays size={18} />

                    {job.deadline}

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

    </div>
  );
}

export default JobsInternships;