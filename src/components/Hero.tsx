import { CheckCircle } from "lucide-react";

import Button from "./ui/Button";

function Hero() {
  return (
    <section className="bg-slate-100">

      <div className="mx-auto flex min-h-[calc(100vh-80px)] max-w-7xl flex-col items-center justify-between gap-12 px-6 py-20 lg:flex-row">

        {/* Left */}

        <div className="max-w-2xl">

          <span className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-semibold text-cyan-700">
            AI Career Development Platform
          </span>

          <h1 className="mt-8 text-5xl font-bold leading-tight text-slate-900 lg:text-6xl">

            One Platform for

            <span className="block text-cyan-600">
              Students,
            </span>

            <span className="block">
              Institutes &
            </span>

            <span className="block">
              Professionals
            </span>

          </h1>

          <p className="mt-8 text-lg leading-8 text-slate-600">

            TalentSphere helps you build your resume,
            assess your skills, prepare for interviews
            and receive AI-powered career guidance
            through one unified platform.

          </p>

          <div className="mt-10 flex flex-col gap-4 sm:flex-row">

            <div className="w-48">
              <Button>
                Get Started
              </Button>
            </div>

            <button className="rounded-xl border border-slate-300 px-6 py-3 font-semibold transition hover:bg-white">
              Learn More
            </button>

          </div>

          <div className="mt-12 grid gap-4 sm:grid-cols-2">

            {[
              "AI Resume Builder",
              "Resume Analyzer",
              "Mock Interview",
              "Career Recommendation",
            ].map((item) => (

              <div
                key={item}
                className="flex items-center gap-3"
              >

                <CheckCircle
                  size={20}
                  className="text-cyan-600"
                />

                <span className="font-medium text-slate-700">
                  {item}
                </span>

              </div>

            ))}

          </div>

        </div>

        {/* Right */}

        <div className="flex w-full max-w-lg items-center justify-center">

          <div className="flex h-[420px] w-full items-center justify-center rounded-3xl border border-dashed border-cyan-300 bg-white shadow-lg">

            <div className="text-center">

              <h2 className="text-2xl font-bold text-cyan-600">
                TalentSphere
              </h2>

              <p className="mt-3 text-slate-500">
                AI Illustration
              </p>

            </div>

          </div>

        </div>

      </div>

    </section>
  );
}

export default Hero;