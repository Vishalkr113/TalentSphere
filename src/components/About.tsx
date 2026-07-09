import {
  Brain,
  FileText,
  Briefcase,
  GraduationCap,
} from "lucide-react";

import Card from "./ui/Card";

const features = [
  {
    title: "AI Resume Builder",
    description:
      "Create professional ATS-friendly resumes within minutes.",
    icon: FileText,
  },
  {
    title: "AI Career Guidance",
    description:
      "Get personalized career recommendations based on your skills.",
    icon: Brain,
  },
  {
    title: "Placement Preparation",
    description:
      "Prepare for aptitude tests, interviews and placement drives.",
    icon: Briefcase,
  },
  {
    title: "Learning Roadmap",
    description:
      "Follow a personalized roadmap to achieve your career goals.",
    icon: GraduationCap,
  },
];

function About() {
  return (
    <section
      id="about"
      className="bg-white py-24"
    >
      <div className="mx-auto max-w-7xl px-6">

        {/* Heading */}

        <div className="mx-auto max-w-4xl text-center">

          <span className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-semibold text-cyan-700">
            About TalentSphere
          </span>

          <h2 className="mt-6 text-4xl font-bold text-slate-900 md:text-5xl">
            Everything You Need For
            <span className="text-cyan-600">
              {" "}Career Success
            </span>
          </h2>

          <p className="mt-6 text-lg leading-8 text-slate-600">
            TalentSphere is an AI-powered Career Development Platform
            designed for Students, Institutes and Professionals.
            It brings Resume Building, Resume Analysis,
            Skill Assessment, Mock Interviews,
            Career Recommendations and Placement Preparation
            into one unified platform.
          </p>

          <p className="mt-4 text-lg leading-8 text-slate-600">
            Instead of using multiple websites,
            TalentSphere helps users manage
            their entire career journey from
            learning new skills to getting placed
            through one intelligent platform.
          </p>

        </div>

        {/* Feature Cards */}

        <div className="mt-20 grid gap-8 md:grid-cols-2 lg:grid-cols-4">

          {features.map((item) => {

            const Icon = item.icon;

            return (

              <Card key={item.title}>

                <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                  <Icon size={30} />

                </div>

                <h3 className="mt-6 text-xl font-bold text-slate-900">
                  {item.title}
                </h3>

                <p className="mt-4 leading-7 text-slate-600">
                  {item.description}
                </p>

              </Card>

            );

          })}

        </div>

      </div>
    </section>
  );
}

export default About;