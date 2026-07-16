import {
  MessageSquare,
  Brain,
  Video,
  Clock3,
  Star,
  CheckCircle2,
  ArrowRight,
} from "lucide-react";

const interviews = [
  {
    title: "HR Interview",
    duration: "20 Minutes",
    level: "Beginner",
    completed: true,
  },
  {
    title: "Technical Interview",
    duration: "45 Minutes",
    level: "Intermediate",
    completed: true,
  },
  {
    title: "Managerial Round",
    duration: "30 Minutes",
    level: "Intermediate",
    completed: false,
  },
  {
    title: "System Design",
    duration: "60 Minutes",
    level: "Advanced",
    completed: false,
  },
  {
    title: "Leadership Round",
    duration: "40 Minutes",
    level: "Advanced",
    completed: false,
  },
  {
    title: "Behavioral Interview",
    duration: "25 Minutes",
    level: "Intermediate",
    completed: true,
  },
];

function InterviewPreparation() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Interview Preparation
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Prepare for HR, Technical and Leadership interviews
          with AI-powered mock interview sessions.
        </p>

      </div>

      {/* Summary */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="flex items-center gap-4">

          <Brain size={42} />

          <div>

            <h2 className="text-3xl font-bold">

              Interview Readiness

            </h2>

            <p className="mt-2 text-cyan-100">

              AI evaluates your communication, confidence
              and technical knowledge.

            </p>

          </div>

        </div>

        <div className="mt-8 grid gap-6 md:grid-cols-3">

          <div>

            <p className="text-cyan-100">

              Readiness Score

            </p>

            <h2 className="mt-2 text-4xl font-bold">

              89%

            </h2>

          </div>

          <div>

            <p className="text-cyan-100">

              Interviews Completed

            </p>

            <h2 className="mt-2 text-4xl font-bold">

              18

            </h2>

          </div>

          <div>

            <p className="text-cyan-100">

              Average Rating

            </p>

            <h2 className="mt-2 text-4xl font-bold">

              4.8★

            </h2>

          </div>

        </div>

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

              <div className="flex items-center gap-2">

                <CheckCircle2
                  size={18}
                  className={
                    item.completed
                      ? "text-green-600"
                      : "text-orange-500"
                  }
                />

                <span
                  className={
                    item.completed
                      ? "font-medium text-green-600"
                      : "font-medium text-orange-500"
                  }
                >
                  {item.completed
                    ? "Completed"
                    : "Pending"}
                </span>

              </div>

            </div>

            <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

              <Video size={18} />

              Start Interview

              <ArrowRight size={18} />

            </button>

          </div>

        ))}

      </div>

    </div>
  );
}

export default InterviewPreparation;