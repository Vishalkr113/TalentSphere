import {
  ClipboardList,
  CalendarDays,
  CircleCheck,
  Clock3,
} from "lucide-react";

const assignments = [
  {
    subject: "Mathematics",
    title: "Algebra Worksheet",
    dueDate: "12 Aug 2026",
    status: "Pending",
  },
  {
    subject: "Science",
    title: "Physics Practical Report",
    dueDate: "14 Aug 2026",
    status: "In Progress",
  },
  {
    subject: "English",
    title: "Essay Writing",
    dueDate: "16 Aug 2026",
    status: "Completed",
  },
  {
    subject: "Social Science",
    title: "History Project",
    dueDate: "18 Aug 2026",
    status: "Pending",
  },
];

function Assignments() {
  return (
    <div className="space-y-10">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Assignments
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Track all your school assignments and complete
          them before the deadline.
        </p>

      </div>

      {/* Cards */}

      <div className="grid gap-6">

        {assignments.map((item) => (

          <div
            key={item.title}
            className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition hover:shadow-lg"
          >

            <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">

              <div>

                <div className="flex items-center gap-4">

                  <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                    <ClipboardList size={28} />

                  </div>

                  <div>

                    <h2 className="text-2xl font-bold text-slate-900">
                      {item.title}
                    </h2>

                    <p className="text-slate-500">
                      {item.subject}
                    </p>

                  </div>

                </div>

              </div>

              <div className="flex flex-wrap gap-6">

                <div className="flex items-center gap-2">

                  <CalendarDays
                    size={18}
                    className="text-cyan-600"
                  />

                  <span>{item.dueDate}</span>

                </div>

                <div className="flex items-center gap-2">

                  <Clock3
                    size={18}
                    className="text-orange-500"
                  />

                  <span>{item.status}</span>

                </div>

              </div>

            </div>

            <div className="mt-6 flex justify-end">

              <button className="flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

                <CircleCheck size={18} />

                View Assignment

              </button>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}

export default Assignments;