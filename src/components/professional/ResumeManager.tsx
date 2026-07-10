import {
  FileText,
  ScanSearch,
  Download,
  Upload,
  Eye,
  Star,
  ArrowRight,
} from "lucide-react";

const resumes = [
  {
    title: "Software Engineer Resume",
    ats: 91,
    updated: "12 Jul 2026",
  },
  {
    title: "Full Stack Developer Resume",
    ats: 88,
    updated: "04 Jul 2026",
  },
  {
    title: "Frontend Developer Resume",
    ats: 94,
    updated: "28 Jun 2026",
  },
];

function ResumeManager() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Resume Manager
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Manage, analyze and optimize your professional resumes
          for better job opportunities.
        </p>

      </div>

      {/* Summary */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="grid gap-6 md:grid-cols-3">

          <div>

            <p className="text-cyan-100">
              Total Resumes
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              3
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Average ATS Score
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              91%
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Last Updated
            </p>

            <h2 className="mt-2 text-2xl font-bold">
              12 Jul 2026
            </h2>

          </div>

        </div>

      </div>

      {/* Action Buttons */}

      <div className="flex flex-wrap gap-4">

        <button className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700">

          <Upload size={18} />

          Upload Resume

        </button>

        <button className="flex items-center gap-2 rounded-xl border border-slate-300 px-6 py-3 font-semibold transition hover:bg-slate-100">

          <FileText size={18} />

          Create Resume

        </button>

      </div>

      {/* Resume Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {resumes.map((resume) => (

          <div
            key={resume.title}
            className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
          >

            <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

              <FileText size={30} />

            </div>

            <h2 className="mt-6 text-2xl font-bold text-slate-900">
              {resume.title}
            </h2>

            <div className="mt-6 space-y-3">

              <div className="flex items-center gap-2 text-slate-600">

                <Star size={18} />

                ATS Score : {resume.ats}%

              </div>

              <div className="text-slate-600">

                Updated : {resume.updated}

              </div>

            </div>

            <div className="mt-8 flex gap-3">

              <button className="flex flex-1 items-center justify-center gap-2 rounded-xl border border-slate-300 py-3 font-medium hover:bg-slate-100">

                <Eye size={18} />

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

      {/* Resume Analyzer */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">

          <div>

            <div className="flex items-center gap-3">

              <ScanSearch
                size={32}
                className="text-cyan-600"
              />

              <h2 className="text-3xl font-bold text-slate-900">

                AI Resume Analyzer

              </h2>

            </div>

            <p className="mt-4 text-slate-600">

              Analyze your resume with AI and receive ATS
              optimization suggestions to improve interview
              chances.

            </p>

          </div>

          <button className="flex items-center gap-2 rounded-xl bg-cyan-600 px-6 py-3 font-semibold text-white transition hover:bg-cyan-700">

            Analyze Resume

            <ArrowRight size={18} />

          </button>

        </div>

      </div>

    </div>
  );
}

export default ResumeManager;