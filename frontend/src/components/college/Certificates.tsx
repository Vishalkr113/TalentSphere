import {
  Award,
  CalendarDays,
  Download,
  ExternalLink,
  BadgeCheck,
  Plus,
} from "lucide-react";

const certificates = [
  {
    title: "Python Programming",
    issuer: "Infosys Springboard",
    date: "15 Jan 2026",
    status: "Verified",
  },
  {
    title: "Java Fundamentals",
    issuer: "Oracle Academy",
    date: "20 Feb 2026",
    status: "Verified",
  },
  {
    title: "Google Cloud Arcade",
    issuer: "Google Cloud",
    date: "10 Mar 2026",
    status: "Verified",
  },
  {
    title: "Frontend Development",
    issuer: "CodeAlpha",
    date: "12 Apr 2026",
    status: "Pending",
  },
  {
    title: "Machine Learning",
    issuer: "Coursera",
    date: "05 May 2026",
    status: "Verified",
  },
  {
    title: "Data Structures & Algorithms",
    issuer: "GeeksforGeeks",
    date: "28 May 2026",
    status: "Pending",
  },
];

function Certificates() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Certificates
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Manage and showcase all your professional
          certifications in one place.
        </p>

      </div>

      {/* Summary */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="grid gap-6 md:grid-cols-3">

          <div>

            <p className="text-cyan-100">
              Total Certificates
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              18
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Verified
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              15
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Pending Review
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              3
            </h2>

          </div>

        </div>

      </div>

      {/* Upload Button */}

      <div className="flex justify-end">

        <button className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700">

          <Plus size={18} />

          Upload Certificate

        </button>

      </div>

      {/* Certificate Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {certificates.map((certificate) => (

          <div
            key={certificate.title}
            className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
          >

            <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

              <Award size={30} />

            </div>

            <h2 className="mt-6 text-2xl font-bold text-slate-900">

              {certificate.title}

            </h2>

            <p className="mt-2 text-slate-600">

              {certificate.issuer}

            </p>

            <div className="mt-6 space-y-3">

              <div className="flex items-center gap-2 text-slate-600">

                <CalendarDays size={18} />

                {certificate.date}

              </div>

              <div className="flex items-center gap-2">

                <BadgeCheck
                  size={18}
                  className={
                    certificate.status === "Verified"
                      ? "text-green-600"
                      : "text-orange-500"
                  }
                />

                <span
                  className={
                    certificate.status === "Verified"
                      ? "font-medium text-green-600"
                      : "font-medium text-orange-500"
                  }
                >
                  {certificate.status}
                </span>

              </div>

            </div>

            <div className="mt-8 flex gap-3">

              <button className="flex flex-1 items-center justify-center gap-2 rounded-xl border border-slate-300 py-3 font-medium hover:bg-slate-100">

                <ExternalLink size={18} />

                View

              </button>

              <button className="flex flex-1 items-center justify-center gap-2 rounded-xl bg-cyan-600 py-3 font-medium text-white hover:bg-cyan-700">

                <Download size={18} />

                Download

              </button>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}

export default Certificates;