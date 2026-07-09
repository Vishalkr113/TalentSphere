import {
  Target,
  CheckCircle2,
  BookOpen,
  Clock3,
} from "lucide-react";

const goals = [
  {
    title: "Complete Mathematics Chapter",
    time: "1 Hour",
    completed: true,
  },
  {
    title: "Revise Science Notes",
    time: "45 Minutes",
    completed: false,
  },
  {
    title: "Practice English Grammar",
    time: "30 Minutes",
    completed: false,
  },
  {
    title: "Solve 20 MCQs",
    time: "40 Minutes",
    completed: false,
  },
];

function DailyGoal() {
  return (
    <div className="space-y-10">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Daily Goals
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Stay consistent by completing your daily learning goals.
        </p>

      </div>

      {/* Progress */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-600 p-8 text-white shadow-lg">

        <h2 className="text-2xl font-bold">
          Today's Progress
        </h2>

        <div className="mt-6 h-4 rounded-full bg-white/20">

          <div className="h-4 w-1/4 rounded-full bg-white"></div>

        </div>

        <p className="mt-3 text-cyan-100">
          1 of 4 Goals Completed (25%)
        </p>

      </div>

      {/* Goal Cards */}

      <div className="grid gap-6">

        {goals.map((goal) => (

          <div
            key={goal.title}
            className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition hover:shadow-lg"
          >

            <div className="flex flex-col gap-5 lg:flex-row lg:items-center lg:justify-between">

              <div className="flex items-center gap-4">

                <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                  <BookOpen size={28} />

                </div>

                <div>

                  <h2 className="text-xl font-bold text-slate-900">
                    {goal.title}
                  </h2>

                  <div className="mt-2 flex items-center gap-2 text-slate-500">

                    <Clock3 size={16} />

                    {goal.time}

                  </div>

                </div>

              </div>

              <div>

                {goal.completed ? (

                  <span className="flex items-center gap-2 rounded-full bg-green-100 px-4 py-2 text-sm font-semibold text-green-700">

                    <CheckCircle2 size={18} />

                    Completed

                  </span>

                ) : (

                  <button className="flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

                    <Target size={18} />

                    Start Goal

                  </button>

                )}

              </div>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}

export default DailyGoal;