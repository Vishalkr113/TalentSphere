import {
  CalendarDays,
  Clock3,
  MapPin,
  BookOpen,
} from "lucide-react";

const exams = [
  {
    subject: "Mathematics",
    date: "15 Aug 2026",
    time: "09:00 AM",
    room: "Room 101",
  },
  {
    subject: "Science",
    date: "18 Aug 2026",
    time: "09:00 AM",
    room: "Room 203",
  },
  {
    subject: "English",
    date: "21 Aug 2026",
    time: "09:00 AM",
    room: "Room 105",
  },
  {
    subject: "Social Science",
    date: "24 Aug 2026",
    time: "09:00 AM",
    room: "Room 109",
  },
];

function UpcomingExams() {
  return (
    <div className="space-y-10">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Upcoming Exams
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Stay prepared with your upcoming examination schedule.
        </p>

      </div>

      {/* Exam Cards */}

      <div className="grid gap-6">

        {exams.map((exam) => (

          <div
            key={exam.subject}
            className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition hover:shadow-lg"
          >

            <div className="flex flex-col justify-between gap-6 lg:flex-row lg:items-center">

              <div>

                <div className="flex items-center gap-3">

                  <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                    <BookOpen size={28} />

                  </div>

                  <div>

                    <h2 className="text-2xl font-bold text-slate-900">
                      {exam.subject}
                    </h2>

                    <p className="text-slate-500">
                      Final Examination
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

                  <span>{exam.date}</span>

                </div>

                <div className="flex items-center gap-2">

                  <Clock3
                    size={18}
                    className="text-cyan-600"
                  />

                  <span>{exam.time}</span>

                </div>

                <div className="flex items-center gap-2">

                  <MapPin
                    size={18}
                    className="text-cyan-600"
                  />

                  <span>{exam.room}</span>

                </div>

              </div>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}

export default UpcomingExams;