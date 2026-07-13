import {
  UserPlus,
  UserCircle,
  ClipboardCheck,
  Bot,
  Trophy,
} from "lucide-react";

const steps = [
  {
    title: "Create Account",
    description:
      "Sign Up as a Student, Institute or Professional to access your dedicated portal.",
    icon: UserPlus,
  },
  {
    title: "Complete Profile",
    description:
      "Fill in your personal, academic or professional details to personalize your experience.",
    icon: UserCircle,
  },
  {
    title: "Skill Assessment",
    description:
      "Take assessments to evaluate your technical knowledge and aptitude skills.",
    icon: ClipboardCheck,
  },
  {
    title: "AI Analysis",
    description:
      "Receive AI-powered resume analysis, interview preparation and career recommendations.",
    icon: Bot,
  },
  {
    title: "Achieve Your Goals",
    description:
      "Improve your skills, prepare confidently and grow your career with TalentSphere.",
    icon: Trophy,
  },
];

function HowItWorks() {
  return (
    <section className="bg-slate-100 py-24">

      <div className="mx-auto max-w-7xl px-6">

        <div className="text-center">

          <span className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-semibold text-cyan-700">
            How It Works
          </span>

          <h2 className="mt-6 text-4xl font-bold text-slate-900">
            Your Career Journey
          </h2>

          <p className="mx-auto mt-5 max-w-3xl text-lg text-slate-600">
            Follow these simple steps to unlock the
            full potential of TalentSphere and
            accelerate your career growth.
          </p>

        </div>

        <div className="mt-20 grid gap-8 md:grid-cols-2 xl:grid-cols-5">

          {steps.map((step) => {
            const Icon = step.icon;

            return (
              <div
                key={step.title}
                className="relative rounded-2xl bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-lg"
              >

                <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">
                    <Icon size={28} />
                </div>


                <h3 className="mt-6 text-xl font-bold text-slate-900">
                  {step.title}
                </h3>

                <p className="mt-4 leading-7 text-slate-600">
                  {step.description}
                </p>

              </div>
            );
          })}

        </div>

      </div>

    </section>
  );
}

export default HowItWorks;