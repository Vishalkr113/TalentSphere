import {
  Brain,
  Clock3,
  Trophy,
  Target,
  ChevronRight,
  CheckCircle2,
} from "lucide-react";

const assessments = [
  {
    title: "Aptitude Test",
    questions: "30 Questions",
    duration: "30 Minutes",
    level: "Beginner",
  },
  {
    title: "Logical Reasoning",
    questions: "25 Questions",
    duration: "25 Minutes",
    level: "Intermediate",
  },
  {
    title: "Quantitative Aptitude",
    questions: "30 Questions",
    duration: "35 Minutes",
    level: "Intermediate",
  },
  {
    title: "Verbal Ability",
    questions: "20 Questions",
    duration: "20 Minutes",
    level: "Beginner",
  },
  {
    title: "Technical MCQ",
    questions: "40 Questions",
    duration: "45 Minutes",
    level: "Advanced",
  },
  {
    title: "Problem Solving",
    questions: "15 Questions",
    duration: "30 Minutes",
    level: "Advanced",
  },
];

function SkillAssessment() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Skill Assessment
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Assess your aptitude, logical reasoning, technical knowledge
          and problem-solving skills.
        </p>

      </div>

      {/* Overall Score */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="flex items-center gap-4">

          <Trophy size={42} />

          <div>

            <h2 className="text-3xl font-bold">
              Overall Skill Score
            </h2>

            <p className="mt-2 text-cyan-100">
              Keep practicing to improve your placement readiness.
            </p>

          </div>

        </div>

        <h1 className="mt-8 text-6xl font-bold">
          78%
        </h1>

      </div>

      {/* Assessment Cards */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {assessments.map((item) => (

          <div
            key={item.title}
            className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
          >

            <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

              <Brain size={30} />

            </div>

            <h2 className="mt-6 text-2xl font-bold text-slate-900">
              {item.title}
            </h2>

            <div className="mt-6 space-y-3">

              <div className="flex items-center gap-2 text-slate-600">

                <CheckCircle2 size={18} />

                {item.questions}

              </div>

              <div className="flex items-center gap-2 text-slate-600">

                <Clock3 size={18} />

                {item.duration}

              </div>

              <div className="flex items-center gap-2 text-slate-600">

                <Target size={18} />

                {item.level}

              </div>

            </div>

            <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

              Start Test

              <ChevronRight size={18} />

            </button>

          </div>

        ))}

      </div>

    </div>
  );
}

export default SkillAssessment;