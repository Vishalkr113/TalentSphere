import {
  FileText,
  ScanSearch,
  ClipboardCheck,
  MessagesSquare,
  Briefcase,
  Bot,
} from "lucide-react";

import Card from "./ui/Card";

const features = [
  {
    title: "Resume Builder",
    description:
      "Create a professional ATS-friendly resume within minutes.",
    icon: FileText,
    color: "text-cyan-600",
  },
  {
    title: "Resume Analyzer",
    description:
      "Analyze your resume and improve it with AI suggestions.",
    icon: ScanSearch,
    color: "text-violet-600",
  },
  {
    title: "Skill Assessment",
    description:
      "Evaluate your technical and aptitude skills with smart tests.",
    icon: ClipboardCheck,
    color: "text-emerald-600",
  },
  {
    title: "Mock Interview",
    description:
      "Practice interviews with AI-driven questions and feedback.",
    icon: MessagesSquare,
    color: "text-orange-500",
  },
  {
    title: "Career Recommendation",
    description:
      "Receive personalized career suggestions based on your profile.",
    icon: Briefcase,
    color: "text-pink-600",
  },
  {
    title: "AI Assistant",
    description:
      "Get instant guidance for learning, placement and career planning.",
    icon: Bot,
    color: "text-indigo-600",
  },
];

function Features() {
  return (
    <section
      id="features"
      className="bg-slate-100 py-24"
    >
      <div className="mx-auto max-w-7xl px-6">

        <div className="text-center">

          <span className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-semibold text-cyan-700">
            Features
          </span>

          <h2 className="mt-6 text-4xl font-bold text-slate-900">
            Everything You Need
          </h2>

          <p className="mx-auto mt-5 max-w-3xl text-lg text-slate-600">
            TalentSphere provides all the essential
            tools required for career development,
            placement preparation and professional
            growth.
          </p>

        </div>

        <div className="mt-16 grid gap-8 md:grid-cols-2 xl:grid-cols-3">

          {features.map((feature) => {
            const Icon = feature.icon;

            return (
              <Card
                key={feature.title}
                className="group"
              >

                <div
                  className={`flex h-14 w-14 items-center justify-center rounded-2xl bg-slate-100 ${feature.color}`}
                >
                  <Icon size={28} />
                </div>

                <h3 className="mt-6 text-2xl font-bold text-slate-900">
                  {feature.title}
                </h3>

                <p className="mt-4 leading-7 text-slate-600">
                  {feature.description}
                </p>

              </Card>
            );
          })}

        </div>

      </div>
    </section>
  );
}

export default Features;