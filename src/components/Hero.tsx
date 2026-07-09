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

          <h1 className="mt-8 text-[38px] font-bold leading-tight text-slate-900 lg:text-[52px]">

                One Platform for

          <span className="block text-cyan-600">
              High School Students,
          </span>

          <span className="block">
            College Students
          </span>

          <span className="block">
            & Working Professionals
          </span>
          </h1>
          <p className="mt-8 text-lg leading-8 text-slate-600">

            TalentSphere Elevate is an AI-powered career development platform designed for
             High School Students,College Students, 
             and Working Professionals to learn, grow, and achieve their career goals.
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
            "Career Roadmap",
            "AI Resume Builder",
            "Skill Assessment",
            "Mock Interview",
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

          <div className="w-full rounded-3xl bg-white p-8 shadow-2xl border border-slate-200">

  <div className="flex items-center gap-3">

    <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-cyan-100 text-3xl">
      🤖
    </div>

    <div>
      <h3 className="text-xl font-bold text-slate-900">
        TalentSphere AI
      </h3>

      <p className="text-sm text-slate-500">
        Smart Career Assistant
      </p>
    </div>

  </div>

  <div className="mt-8 space-y-4">

    <div className="rounded-2xl bg-cyan-50 p-4">
      <h4 className="font-semibold text-cyan-700">
        🎓 High School Student
      </h4>

      <p className="mt-2 text-sm text-slate-600">
        Career Explorer • Subject Guidance • Scholarships
      </p>
    </div>

    <div className="rounded-2xl bg-blue-50 p-4">
      <h4 className="font-semibold text-blue-700">
        🎓 College Student
      </h4>

      <p className="mt-2 text-sm text-slate-600">
        Resume • Coding • Placement • Mock Interview
      </p>
    </div>

    <div className="rounded-2xl bg-violet-50 p-4">
      <h4 className="font-semibold text-violet-700">
        💼 Working Professional
      </h4>

      <p className="mt-2 text-sm text-slate-600">
        Career Growth • Promotion • AI Mentor
      </p>
    </div>

  </div>

  <div className="mt-8 rounded-2xl bg-slate-100 p-5">

    <div className="flex justify-between">

      <span className="font-medium">
        Career Readiness
      </span>

      <span className="font-bold text-cyan-600">
        98%
      </span>

    </div>

    <div className="mt-3 h-3 rounded-full bg-slate-300">

      <div className="h-3 w-[98%] rounded-full bg-cyan-600"></div>

    </div>

  </div>

</div>

 </div>

      </div>

    </section>
  );
}

export default Hero;