import {
  Code2,
  Clock3,
  Trophy,
  ChevronRight,
  CheckCircle2,
  Terminal,
} from "lucide-react";

const challenges = [
  {
    title: "Arrays & Strings",
    questions: "20 Problems",
    duration: "45 Minutes",
    difficulty: "Easy",
  },
  {
    title: "Linked List",
    questions: "15 Problems",
    duration: "40 Minutes",
    difficulty: "Medium",
  },
  {
    title: "Stacks & Queues",
    questions: "15 Problems",
    duration: "35 Minutes",
    difficulty: "Medium",
  },
  {
    title: "Trees & Graphs",
    questions: "20 Problems",
    duration: "60 Minutes",
    difficulty: "Hard",
  },
  {
    title: "Dynamic Programming",
    questions: "15 Problems",
    duration: "60 Minutes",
    difficulty: "Hard",
  },
  {
    title: "SQL Assessment",
    questions: "25 Questions",
    duration: "30 Minutes",
    difficulty: "Easy",
  },
];

function CodingAssessment() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Coding Assessment
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Practice coding challenges, improve problem-solving skills
          and prepare for technical interviews.
        </p>

      </div>

      {/* Overall Progress */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="flex items-center gap-4">

          <Trophy size={42} />

          <div>

            <h2 className="text-3xl font-bold">
              Coding Score
            </h2>

            <p className="mt-2 text-cyan-100">
              Solve more challenges to improve your ranking.
            </p>

          </div>

        </div>

        <h1 className="mt-8 text-6xl font-bold">
          74%
        </h1>

      </div>

      {/* Challenge Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {challenges.map((challenge) => (

          <div
            key={challenge.title}
            className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
          >

            <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

              <Code2 size={30} />

            </div>

            <h2 className="mt-6 text-2xl font-bold text-slate-900">
              {challenge.title}
            </h2>

            <div className="mt-6 space-y-3">

              <div className="flex items-center gap-2 text-slate-600">

                <CheckCircle2 size={18} />

                {challenge.questions}

              </div>

              <div className="flex items-center gap-2 text-slate-600">

                <Clock3 size={18} />

                {challenge.duration}

              </div>

              <div className="flex items-center gap-2 text-slate-600">

                <Terminal size={18} />

                {challenge.difficulty}

              </div>

            </div>

            <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

              Start Coding

              <ChevronRight size={18} />

            </button>

          </div>

        ))}

      </div>

    </div>
  );
}

export default CodingAssessment;