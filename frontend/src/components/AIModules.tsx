import {
  Bot,
  BrainCircuit,
  FileSearch,
  MessageSquareText,
  Sparkles,
  TrendingUp,
} from "lucide-react";

import Card from "./ui/Card";

const aiModules = [
  {
    title: "AI Resume Analyzer",
    description:
      "Analyze your resume and receive ATS-friendly suggestions for improvement.",
    icon: FileSearch,
  },
  {
    title: "AI Career Recommendation",
    description:
      "Discover suitable career paths based on your skills and interests.",
    icon: BrainCircuit,
  },
  {
    title: "AI Mock Interview",
    description:
      "Practice interviews with AI-generated questions and instant feedback.",
    icon: MessageSquareText,
  },
  {
    title: "Skill Gap Analysis",
    description:
      "Identify missing skills required for your dream career.",
    icon: TrendingUp,
  },
  {
    title: "Learning Roadmap",
    description:
      "Get a personalized roadmap to improve your technical skills.",
    icon: Sparkles,
  },
  {
    title: "AI Assistant",
    description:
      "Ask career-related questions and receive intelligent guidance.",
    icon: Bot,
  },
];

function AIModules() {
  return (
    <section className="bg-white py-24">

      <div className="mx-auto max-w-7xl px-6">

        <div className="text-center">

          <span className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-semibold text-cyan-700">
            AI Modules
          </span>

          <h2 className="mt-6 text-4xl font-bold text-slate-900">
            Powered by Artificial Intelligence
          </h2>

          <p className="mx-auto mt-5 max-w-3xl text-lg text-slate-600">
            TalentSphere uses Artificial Intelligence to
            help students improve resumes, prepare for
            interviews and make better career decisions.
          </p>

        </div>

        <div className="mt-16 grid gap-8 md:grid-cols-2 xl:grid-cols-3">

          {aiModules.map((module) => {
            const Icon = module.icon;

            return (
              <Card
                key={module.title}
                className="group"
              >

                <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                  <Icon size={28} />

                </div>

                <h3 className="mt-6 text-2xl font-bold text-slate-900">
                  {module.title}
                </h3>

                <p className="mt-4 leading-7 text-slate-600">
                  {module.description}
                </p>

              </Card>
            );
          })}

        </div>

      </div>

    </section>
  );
}

export default AIModules;