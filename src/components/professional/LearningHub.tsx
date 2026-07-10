import {
  BookOpen,
  Brain,
  Code2,
  Cloud,
  Shield,
  BarChart3,
  Clock3,
  Star,
  ArrowRight,
} from "lucide-react";

const courses = [
  {
    title: "Generative AI",
    duration: "20 Hours",
    level: "Advanced",
    icon: Brain,
  },
  {
    title: "Full Stack Development",
    duration: "45 Hours",
    level: "Intermediate",
    icon: Code2,
  },
  {
    title: "AWS Cloud",
    duration: "30 Hours",
    level: "Intermediate",
    icon: Cloud,
  },
  {
    title: "Cyber Security",
    duration: "35 Hours",
    level: "Advanced",
    icon: Shield,
  },
  {
    title: "Data Analytics",
    duration: "28 Hours",
    level: "Beginner",
    icon: BarChart3,
  },
  {
    title: "Leadership Skills",
    duration: "15 Hours",
    level: "Professional",
    icon: BookOpen,
  },
];

function LearningHub() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Learning Hub
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Explore curated courses and AI-powered learning paths
          to advance your professional career.
        </p>

      </div>

      {/* Learning Overview */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <div className="grid gap-6 md:grid-cols-4">

          <div>

            <p className="text-cyan-100">
              Active Courses
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              6
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Completed
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              18
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Learning Hours
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              145
            </h2>

          </div>

          <div>

            <p className="text-cyan-100">
              Progress
            </p>

            <h2 className="mt-2 text-4xl font-bold">
              78%
            </h2>

          </div>

        </div>

      </div>

      {/* Courses */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">

        {courses.map((course) => {

          const Icon = course.icon;

          return (

            <div
              key={course.title}
              className="rounded-3xl bg-white p-6 shadow-sm transition hover:-translate-y-2 hover:shadow-xl"
            >

              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                <Icon size={30} />

              </div>

              <h2 className="mt-6 text-2xl font-bold text-slate-900">
                {course.title}
              </h2>

              <div className="mt-6 space-y-3">

                <div className="flex items-center gap-2 text-slate-600">

                  <Clock3 size={18} />

                  {course.duration}

                </div>

                <div className="flex items-center gap-2 text-slate-600">

                  <Star size={18} />

                  {course.level}

                </div>

              </div>

              <button className="mt-8 flex items-center gap-2 rounded-xl bg-cyan-600 px-5 py-3 font-medium text-white transition hover:bg-cyan-700">

                Continue Learning

                <ArrowRight size={18} />

              </button>

            </div>

          );

        })}

      </div>

      {/* AI Recommendation */}

      <div className="rounded-3xl bg-white p-8 shadow-sm">

        <div className="flex items-center gap-4">

          <Brain
            size={36}
            className="text-cyan-600"
          />

          <div>

            <h2 className="text-3xl font-bold text-slate-900">
              AI Learning Recommendation
            </h2>

            <p className="mt-3 text-slate-600">

              Based on your profile and career goals,
              we recommend learning <strong>Generative AI</strong>,
              <strong> AWS Cloud</strong> and
              <strong> System Design</strong> to maximize
              your career growth and salary potential.

            </p>

          </div>

        </div>

      </div>

    </div>
  );
}

export default LearningHub;