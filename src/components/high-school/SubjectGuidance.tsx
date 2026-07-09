import {
  Atom,
  Calculator,
  BookOpen,
  ChevronRight,
} from "lucide-react";

const streams = [
  {
    title: "Science",
    icon: Atom,
    description:
      "Engineering, Medical, Research, AI, Technology and more.",
    subjects: [
      "Physics",
      "Chemistry",
      "Mathematics",
      "Biology",
    ],
  },
  {
    title: "Commerce",
    icon: Calculator,
    description:
      "Finance, CA, CS, Banking, Business and Management.",
    subjects: [
      "Accountancy",
      "Economics",
      "Business Studies",
      "Mathematics",
    ],
  },
  {
    title: "Arts",
    icon: BookOpen,
    description:
      "Law, UPSC, Journalism, Design, Psychology and Humanities.",
    subjects: [
      "History",
      "Political Science",
      "Geography",
      "Psychology",
    ],
  },
];

function SubjectGuidance() {
  return (
    <div className="space-y-10">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Subject Guidance
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Explore the right stream and subjects according
          to your interests and future career goals.
        </p>

      </div>

      {/* Cards */}

      <div className="grid gap-8 lg:grid-cols-3">

        {streams.map((stream) => {

          const Icon = stream.icon;

          return (

            <div
              key={stream.title}
              className="rounded-3xl border border-slate-200 bg-white p-7 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
            >

              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                <Icon size={32} />

              </div>

              <h2 className="mt-6 text-2xl font-bold text-slate-900">

                {stream.title}

              </h2>

              <p className="mt-4 leading-7 text-slate-600">

                {stream.description}

              </p>

              <div className="mt-6 space-y-2">

                {stream.subjects.map((subject) => (

                  <div
                    key={subject}
                    className="rounded-lg bg-slate-100 px-4 py-2 text-sm font-medium text-slate-700"
                  >
                    {subject}
                  </div>

                ))}

              </div>

              <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

                Learn More

                <ChevronRight size={18} />

              </button>

            </div>

          );

        })}

      </div>

    </div>
  );
}

export default SubjectGuidance;