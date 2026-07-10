import {
  CheckCircle2,
  Brain,
  FileText,
  Code2,
  MessageSquare,
  Briefcase,
  Award,
} from "lucide-react";

const roadmap = [
  {
    step: "Step 1",
    title: "Complete Your Profile",
    description:
      "Fill in your academic details, skills and career goals.",
    icon: Brain,
    status: "Completed",
  },
  {
    step: "Step 2",
    title: "Build ATS Resume",
    description:
      "Create a professional ATS-friendly resume.",
    icon: FileText,
    status: "Current",
  },
  {
    step: "Step 3",
    title: "Coding Practice",
    description:
      "Solve coding challenges and improve DSA skills.",
    icon: Code2,
    status: "Upcoming",
  },
  {
    step: "Step 4",
    title: "Mock Interview",
    description:
      "Practice HR and Technical interviews with AI.",
    icon: MessageSquare,
    status: "Upcoming",
  },
  {
    step: "Step 5",
    title: "Apply for Internships",
    description:
      "Start applying for internships and placement opportunities.",
    icon: Briefcase,
    status: "Upcoming",
  },
  {
    step: "Step 6",
    title: "Get Placement Ready",
    description:
      "Complete assessments and become industry ready.",
    icon: Award,
    status: "Goal",
  },
];

function LearningRoadmap() {
  return (
    <div className="space-y-8">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          Learning Roadmap
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Follow your personalized roadmap from student to
          successful professional.
        </p>

      </div>

      {/* Progress Card */}

      <div className="rounded-3xl bg-gradient-to-r from-cyan-600 to-blue-700 p-8 text-white">

        <h2 className="text-3xl font-bold">
          Overall Progress
        </h2>

        <div className="mt-6 h-4 rounded-full bg-white/20">

          <div className="h-4 w-2/5 rounded-full bg-white"></div>

        </div>

        <p className="mt-3 text-cyan-100">

          40% Roadmap Completed

        </p>

      </div>

      {/* Timeline */}

      <div className="space-y-6">

        {roadmap.map((item) => {

          const Icon = item.icon;

          return (

            <div
              key={item.title}
              className="rounded-3xl bg-white p-6 shadow-sm transition hover:shadow-lg"
            >

              <div className="flex gap-6">

                <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                  <Icon size={30} />

                </div>

                <div className="flex-1">

                  <div className="flex flex-wrap items-center justify-between gap-4">

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

                    <span className="font-medium">
                      Continue Learning
                    </span>

                  </div>

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