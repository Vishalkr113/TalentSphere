import {
  CheckCircle2,
  BookOpen,
  Brain,
  Compass,
  Laptop,
  Trophy,
} from "lucide-react";

const roadmap = [
  {
    step: "Step 1",
    title: "Know Yourself",
    description:
      "Identify your interests, strengths and future goals.",
    icon: Brain,
    status: "Completed",
  },
  {
    step: "Step 2",
    title: "Choose Subjects",
    description:
      "Select the right subjects according to your career.",
    icon: BookOpen,
    status: "Current",
  },
  {
    step: "Step 3",
    title: "Explore Careers",
    description:
      "Learn about Engineering, Medical, Commerce, Arts and more.",
    icon: Compass,
    status: "Upcoming",
  },
  {
    step: "Step 4",
    title: "Build Skills",
    description:
      "Improve communication, coding and problem-solving skills.",
    icon: Laptop,
    status: "Upcoming",
  },
  {
    step: "Step 5",
    title: "Achieve Goal",
    description:
      "Prepare confidently for your dream career.",
    icon: Trophy,
    status: "Goal",
  },
];

function LearningRoadmap() {
  return (
    <div className="space-y-10">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Learning Roadmap
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Follow your personalized journey from school
          to your dream career.
        </p>

      </div>

      {/* Timeline */}

      <div className="space-y-8">

        {roadmap.map((item) => {

          const Icon = item.icon;

          return (

            <div
              key={item.title}
              className="flex gap-6 rounded-3xl border border-slate-200 bg-white p-7 shadow-sm transition hover:shadow-lg"
            >

              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                <Icon size={32} />

              </div>

              <div className="flex-1">

                <div className="flex flex-wrap items-center justify-between gap-3">

                  <div>

                    <p className="text-sm font-semibold text-cyan-600">

                      {item.step}

                    </p>

                    <h2 className="mt-1 text-2xl font-bold text-slate-900">

                      {item.title}

                    </h2>

                  </div>

                  <span className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-semibold text-cyan-700">

                    {item.status}

                  </span>

                </div>

                <p className="mt-4 leading-7 text-slate-600">

                  {item.description}

                </p>

                <div className="mt-5 flex items-center gap-2 text-green-600">

                  <CheckCircle2 size={18} />

                  <span className="text-sm font-medium">
                    Continue Learning
                  </span>

                </div>

              </div>

            </div>

          );

        })}

      </div>

    </div>
  );
}

export default LearningRoadmap;