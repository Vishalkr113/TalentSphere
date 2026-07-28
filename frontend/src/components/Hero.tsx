import { CheckCircle } from "lucide-react";

import Button from "./ui/Button";

function Hero() {
  return (
    <section
      id="home"
      className="bg-slate-100"
    >
      <div className="mx-auto flex min-h-[calc(100vh-80px)] max-w-7xl flex-col items-center justify-between gap-10 px-6 py-14 lg:flex-row">
        {/* Left */}

        <div className="max-w-2xl">
          <span className="rounded-full bg-cyan-100 px-3 py-1.5 text-xs font-semibold text-cyan-700">
            Career Development Platform
          </span>

          <h1 className="mt-6 text-[36px] font-bold leading-tight text-slate-900 lg:text-[48px]">
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

          <p className="mt-6 max-w-xl text-base leading-7 text-slate-600">
            TalentSphere Elevate is an AI-powered career
            development platform designed for High School
            Students, College Students, and Working
            Professionals to learn, grow, and achieve their
            career goals.
          </p>

          <div className="mt-8 flex flex-col gap-4 sm:flex-row">
            <div className="w-44">
              <Button type="button" onClick={() => window.dispatchEvent(new CustomEvent("talentsphere:open-auth", { detail: "login" }))}>
                Get Started
              </Button>
            </div>

            <button
              type="button"
              onClick={() => document.getElementById("about")?.scrollIntoView({ behavior: "smooth" })}
              className="rounded-xl border border-slate-300 px-6 py-3 font-semibold transition hover:bg-white"
            >
              Explore
            </button>
          </div>

          <div className="mt-10 grid gap-3 sm:grid-cols-2">
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
                  size={19}
                  className="text-cyan-600"
                />

                <span className="font-medium text-slate-700">
                  {item}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Right - How TalentSphere Works */}

        <div className="flex w-full max-w-[460px] items-center justify-center">
          <div className="relative w-full overflow-hidden rounded-[30px] border border-white/80 bg-white p-6 shadow-[0_24px_70px_rgba(15,23,42,0.12)]">
            {/* Background Glow */}

            <div className="pointer-events-none absolute -right-16 -top-16 h-44 w-44 rounded-full bg-cyan-300/30 blur-3xl" />

            <div className="pointer-events-none absolute -bottom-20 -left-16 h-44 w-44 rounded-full bg-violet-300/20 blur-3xl" />

            {/* Header */}

            <div className="relative flex items-start justify-between gap-4">
              <div>
                <span className="text-[11px] font-bold uppercase tracking-[0.18em] text-cyan-600">
                  HOW TALENTSPHERE WORKS
                </span>

                <h2 className="mt-2 text-2xl font-bold tracking-tight text-slate-900">
                  Build your career path ✨
                </h2>

                <p className="mt-1 text-sm leading-6 text-slate-500">
                  From self-discovery to career growth in four
                  simple steps.
                </p>
              </div>

              <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br from-cyan-500 to-violet-500 text-xl text-white shadow-lg">
                ⚡
              </div>
            </div>

            {/* Steps */}

            <div className="relative mt-6 grid grid-cols-2 gap-3">
              <div className="group rounded-2xl bg-cyan-50 p-4 transition duration-300 hover:-translate-y-1 hover:shadow-lg">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-cyan-600 text-lg text-white shadow-sm">
                  👤
                </div>

                <h3 className="mt-4 font-bold text-slate-900">
                  Create Your Profile
                </h3>

                <p className="mt-1 text-xs leading-5 text-slate-500">
                  Tell us about your interests, skills and
                  career goals.
                </p>
              </div>

              <div className="group rounded-2xl bg-blue-50 p-4 transition duration-300 hover:-translate-y-1 hover:shadow-lg">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-500 text-lg text-white shadow-sm">
                  🎯
                </div>

                <h3 className="mt-4 font-bold text-slate-900">
                  Assess Your Skills
                </h3>

                <p className="mt-1 text-xs leading-5 text-slate-500">
                  Understand your strengths through practical
                  assessments.
                </p>
              </div>

              <div className="group rounded-2xl bg-violet-50 p-4 transition duration-300 hover:-translate-y-1 hover:shadow-lg">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-violet-500 text-lg text-white shadow-sm">
                  ✦
                </div>

                <h3 className="mt-4 font-bold text-slate-900">
                  Discover Career Paths
                </h3>

                <p className="mt-1 text-xs leading-5 text-slate-500">
                  Explore career options that match your
                  profile.
                </p>
              </div>

              <div className="group rounded-2xl bg-emerald-50 p-4 transition duration-300 hover:-translate-y-1 hover:shadow-lg">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-emerald-500 text-lg text-white shadow-sm">
                  🚀
                </div>

                <h3 className="mt-4 font-bold text-slate-900">
                  Follow Your Roadmap
                </h3>

                <p className="mt-1 text-xs leading-5 text-slate-500">
                  Learn, improve and move toward your career
                  goals.
                </p>
              </div>
            </div>

            {/* Bottom CTA */}

            <div className="relative mt-4 flex items-center justify-between rounded-2xl bg-slate-950 px-5 py-4 text-white">
              <div>
                <p className="text-xs text-slate-400">
                  Your career journey
                </p>

                <p className="mt-1 text-sm font-bold">
                  Starts with the right direction
                </p>
              </div>

              <div className="flex h-10 w-10 items-center justify-center rounded-full bg-gradient-to-br from-cyan-400 to-violet-500 text-lg shadow-lg">
                →
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;