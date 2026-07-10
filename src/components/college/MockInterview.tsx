import {
  MessageSquare,
  Clock3,
  Brain,
  Video,
  Star,
  ChevronRight,
} from "lucide-react";

const interviews = [
  {
    title: "HR Interview",
    duration: "20 Minutes",
    level: "Beginner",
    mode: "Voice + Text",
  },
  {
    title: "Technical Interview",
    duration: "45 Minutes",
    level: "Intermediate",
    mode: "Coding + Voice",
  },
  {
    title: "Behavioral Interview",
    duration: "25 Minutes",
    level: "Intermediate",
    mode: "Voice",
  },
  {
    title: "System Design",
    duration: "60 Minutes",
    level: "Advanced",
    mode: "Discussion",
  },
  {
    title: "DSA Interview",
    duration: "50 Minutes",
    level: "Advanced",
    mode: "Coding",
  },
  {
    title: "Placement Interview",
    duration: "40 Minutes",
    level: "Mixed",
    mode: "Complete Round",
  },
];

function MockInterview() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Mock Interview
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Practice real interview questions with AI and improve your
          confidence before placements.
        </p>

      </div>

      {/* Score */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="flex items-center gap-4">

          <Brain size={42} />

          <div>

            <h2 className="text-3xl font-bold">
              Interview Readiness
            </h2>

            <p className="mt-2 text-cyan-100">
              Complete mock interviews to increase your confidence.
            </p>

          </div>

        </div>

        <h1 className="mt-8 text-6xl font-bold">
          81%
        </h1>

      </div>

      {/* Interview Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {interviews.map((item) => (

          <div
            key={item.title}
            className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
          >

            <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

              <MessageSquare size={30} />

            </div>

            <h2 className="mt-6 text-2xl font-bold text-slate-900">
              {item.title}
            </h2>

            <div className="mt-6 space-y-3">

              <div className="flex items-center gap-2 text-slate-600">

                <Clock3 size={18} />

                {item.duration}

              </div>

              <div className="flex items-center gap-2 text-slate-600">

                <Star size={18} />

                {item.level}

              </div>

              <div className="flex items-center gap-2 text-slate-600">

                <Video size={18} />

                {item.mode}

              </div>

            </div>

            <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

              Start Interview

              <ChevronRight size={18} />

            </button>

          </div>

        ))}

      </div>

    </div>
  );
}

export default MockInterview;