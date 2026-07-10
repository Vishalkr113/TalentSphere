import {
  ScanSearch,
  CheckCircle2,
  AlertTriangle,
  TrendingUp,
  FileText,
  Target,
  Upload,
} from "lucide-react";

const suggestions = [
  {
    title: "ATS Score",
    value: "82%",
    status: "Good",
    icon: TrendingUp,
    color: "text-green-600",
    bg: "bg-green-100",
  },
  {
    title: "Resume Length",
    value: "1 Page",
    status: "Perfect",
    icon: FileText,
    color: "text-cyan-600",
    bg: "bg-cyan-100",
  },
  {
    title: "Keywords",
    value: "68%",
    status: "Improve",
    icon: Target,
    color: "text-orange-500",
    bg: "bg-orange-100",
  },
];

const improvements = [
  "Add more technical keywords related to your skills.",
  "Quantify your project achievements using numbers.",
  "Improve the professional summary section.",
  "Add GitHub and LinkedIn profile links.",
  "Include internships or certifications.",
];

function ResumeAnalyzer() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Resume Analyzer
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Upload your resume and receive AI-powered feedback to improve
          your ATS score and placement chances.
        </p>

      </div>

      {/* Upload */}

      <div className="rounded-3xl border-2 border-dashed border-cyan-300 bg-white p-12 text-center">

        <div className="mx-auto flex h-20 w-20 items-center justify-center rounded-full bg-cyan-100 text-cyan-600">

          <Upload size={38} />

        </div>

        <h2 className="mt-6 text-2xl font-bold text-slate-900">
          Upload Resume
        </h2>

        <p className="mt-3 text-slate-600">
          PDF or DOCX (Maximum 5 MB)
        </p>

        <button className="mt-8 rounded-xl bg-cyan-600 px-8 py-3 font-semibold text-white hover:bg-cyan-700">

          Choose File

        </button>

      </div>

      {/* Analysis */}

      <div className="grid gap-6 md:grid-cols-3">

        {suggestions.map((item) => {

          const Icon = item.icon;

          return (

            <div
              key={item.title}
              className="rounded-3xl bg-white p-6 shadow-sm"
            >

              <div
                className={`flex h-16 w-16 items-center justify-center rounded-2xl ${item.bg} ${item.color}`}
              >

                <Icon size={30} />

              </div>

              <h2 className="mt-6 text-xl font-bold">
                {item.title}
              </h2>

              <h3 className="mt-3 text-3xl font-bold text-slate-900">
                {item.value}
              </h3>

              <p className="mt-2 text-sm font-medium text-slate-500">
                {item.status}
              </p>

            </div>

          );

        })}

      </div>

      {/* AI Suggestions */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <div className="mb-8 flex items-center gap-4">

          <div className="rounded-2xl bg-cyan-100 p-4 text-cyan-600">

            <ScanSearch size={30} />

          </div>

          <div>

            <h2 className="text-2xl font-bold">
              AI Suggestions
            </h2>

            <p className="text-slate-500">
              Recommended improvements for your resume.
            </p>

          </div>

        </div>

        <div className="space-y-5">

          {improvements.map((item) => (

            <div
              key={item}
              className="flex items-start gap-4 rounded-2xl border border-slate-200 p-5"
            >

              <AlertTriangle
                size={22}
                className="mt-1 text-orange-500"
              />

              <p className="leading-7 text-slate-700">
                {item}
              </p>

            </div>

          ))}

        </div>

      </div>

      {/* Overall Result */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="flex items-center gap-4">

          <CheckCircle2 size={40} />

          <div>

            <h2 className="text-3xl font-bold">
              Overall Resume Score
            </h2>

            <p className="mt-2 text-cyan-100">
              Your resume is well structured. A few improvements can
              increase your ATS score above 90%.
            </p>

          </div>

        </div>

        <h1 className="mt-8 text-6xl font-bold">
          82%
        </h1>

      </div>

    </div>
  );
}

export default ResumeAnalyzer;