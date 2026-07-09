import {
  TrendingUp,
  BookOpen,
  Target,
  Award,
} from "lucide-react";

const stats = [
  {
    title: "Overall Progress",
    value: "82%",
    icon: TrendingUp,
  },
  {
    title: "Subjects Completed",
    value: "6 / 8",
    icon: BookOpen,
  },
  {
    title: "Weekly Goal",
    value: "75%",
    icon: Target,
  },
  {
    title: "Achievements",
    value: "12",
    icon: Award,
  },
];

const subjects = [
  {
    name: "Mathematics",
    progress: 88,
  },
  {
    name: "Science",
    progress: 76,
  },
  {
    name: "English",
    progress: 92,
  },
  {
    name: "Social Science",
    progress: 70,
  },
];

function AcademicProgress() {
  return (
    <div className="space-y-10">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Academic Progress
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Track your learning progress and improve your
          academic performance.
        </p>

      </div>

      {/* Stats */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        {stats.map((item) => {

          const Icon = item.icon;

          return (

            <div
              key={item.title}
              className="rounded-3xl bg-white p-6 shadow-sm"
            >

              <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                <Icon size={28} />

              </div>

              <h3 className="mt-5 text-lg font-semibold text-slate-700">
                {item.title}
              </h3>

              <p className="mt-2 text-3xl font-bold text-slate-900">
                {item.value}
              </p>

            </div>

          );

        })}

      </div>

      {/* Subject Progress */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <h2 className="text-2xl font-bold text-slate-900">
          Subject Progress
        </h2>

        <div className="mt-8 space-y-6">

          {subjects.map((subject) => (

            <div key={subject.name}>

              <div className="mb-2 flex justify-between">

                <span className="font-medium text-slate-700">
                  {subject.name}
                </span>

                <span className="font-semibold text-cyan-600">
                  {subject.progress}%
                </span>

              </div>

              <div className="h-3 rounded-full bg-slate-200">

                <div
                  className="h-3 rounded-full bg-cyan-600"
                  style={{
                    width: `${subject.progress}%`,
                  }}
                />

              </div>

            </div>

          ))}

        </div>

      </div>

    </div>
  );
}

export default AcademicProgress;