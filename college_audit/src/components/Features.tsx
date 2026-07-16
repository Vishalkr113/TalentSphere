import {
  Brain,
  FileText,
  Briefcase,
  GraduationCap,
  School,
  Code2,
} from "lucide-react";

import Card from "./ui/Card";
import Button from "./ui/Button";

const features = [
  {
    title: "Career Explorer",
    description:
      "Explore the right career paths based on your interests.",
    icon: Briefcase,
  },
  {
    title: "Subject Guidance",
    description:
      "Get smart guidance to choose the right subjects and streams.",
    icon: School,
  },
  {
    title: "AI Learning Support",
    description:
      "Receive AI-powered learning assistance and study recommendations.",
    icon: Brain,
  },
  {
    title: "Resume Builder",
    description:
      "Build professional ATS-friendly resumes in minutes.",
    icon: FileText,
  },
  {
    title: "Coding Assessment",
    description:
      "Practice coding challenges and improve technical skills.",
    icon: Code2,
  },
  {
    title: "Mock Interview",
    description:
      "Prepare with AI-powered interview practice and feedback.",
    icon: GraduationCap,
  },
  {
    title: "Career Growth",
    description:
      "Track your progress and achieve your career goals.",
    icon: Briefcase,
  },
  {
    title: "AI Career Advisor",
    description:
      "Receive personalized AI-powered career guidance.",
    icon: Brain,
  },
];

function Features() {
  return (
    <section
      id="features"
      className="bg-slate-100 py-24"
    >
      <div className="mx-auto max-w-7xl px-6">

        {/* Heading */}

        <div className="text-center">

          <span className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-semibold text-cyan-700">
            Core Features
          </span>

          <h2 className="mt-6 text-4xl font-bold text-slate-900 md:text-5xl">
            Everything You Need
            <span className="text-cyan-600">
              {" "}To Succeed
            </span>
          </h2>

          <p className="mx-auto mt-6 max-w-3xl text-lg leading-8 text-slate-600">
            Discover AI-powered tools designed to help you
            learn, grow and achieve your academic and
            professional goals.
          </p>

        </div>

        {/* Cards */}

        <div className="mt-20 grid gap-8 md:grid-cols-2 xl:grid-cols-4">

          {features.map((feature) => {

            const Icon = feature.icon;

            return (

              <Card
                key={feature.title}
                className="flex flex-col transition duration-300 hover:-translate-y-2 hover:shadow-2xl"
              >

                <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                  <Icon size={30} />

                </div>

                <h3 className="mt-6 min-h-[56px] text-xl font-bold text-slate-900">

                  {feature.title}

                </h3>

                <p className="min-h-[72px] leading-7 text-slate-600">

                  {feature.description}

                </p>

                <Button
                  className="mt-6 w-full"
                >
                  Explore
                </Button>

              </Card>

            );

          })}

        </div>

      </div>
    </section>
  );
}

export default Features;