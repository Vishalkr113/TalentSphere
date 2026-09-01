import {
  CheckCircle,
  UserRound,
  Target,
  Sparkles,
  Rocket,
} from "lucide-react";

import Button from "./ui/Button";

function Hero() {
  return (
    <section id="home" className="bg-slate-100">
      <div
        className="
          mx-auto
          flex
          max-w-7xl
          flex-col
          items-center
          gap-10
          px-5
          py-10
          sm:px-6
          sm:py-12
          lg:min-h-[calc(100vh-80px)]
          lg:flex-row
          lg:justify-between
          lg:gap-12
          lg:py-14
        "
      >
        {/* LEFT CONTENT */}
        <div className="w-full max-w-2xl">
          <span
            className="
              inline-block
              rounded-full
              bg-cyan-100
              px-3
              py-1.5
              text-sm
              font-semibold
              text-cyan-700
              sm:text-base
            "
          >
            Career Development Platform
          </span>

          <h1
            className="
              mt-6
              text-[47px]
              font-bold
              leading-[1.08]
              tracking-tight
              text-slate-900
              sm:text-[47px]
              md:text-[47px]
              lg:text-[48px]
            "
          >
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

          <p
            className="
              mt-6
              max-w-xl
              text-[20px]
              leading-8
              text-slate-600
              sm:text-[20px]
              md:text-[21px]
              lg:text-base
              lg:leading-7
            "
          >
            TalentSphere Elevate is an AI-powered career
            development platform designed for High School
            Students, College Students, and Working
            Professionals to learn, grow, and achieve their
            career goals.
          </p>

          {/* BUTTONS */}
          <div className="mt-8 flex flex-col gap-4 sm:flex-row">
            <div className="w-full sm:w-44">
              <Button
                type="button"
                onClick={() =>
                  window.dispatchEvent(
                    new CustomEvent("talentsphere:open-auth", {
                      detail: "login",
                    })
                  )
                }
              >
                Get Started
              </Button>
            </div>

            <button
              type="button"
              onClick={() =>
                document
                  .getElementById("about")
                  ?.scrollIntoView({ behavior: "smooth" })
              }
              className="
                w-full
                rounded-xl
                border
                border-slate-300
                px-6
                py-3
                text-base
                font-semibold
                transition
                hover:bg-white
                sm:w-auto
              "
            >
              Explore
            </button>
          </div>

          {/* FEATURES */}
          <div
            className="
              mt-10
              grid
              grid-cols-1
              gap-4
              sm:grid-cols-2
            "
          >
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
                  size={22}
                  className="shrink-0 text-cyan-600"
                />

                <span
                  className="
                    text-base
                    font-medium
                    text-slate-700
                    sm:text-lg
                    lg:text-base
                  "
                >
                  {item}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* RIGHT - HOW TALENTSPHERE WORKS */}
        <div
          className="
            flex
            w-full
            max-w-[460px]
            items-center
            justify-center
            lg:shrink-0
          "
        >
          <div
            className="
              relative
              w-full
              overflow-hidden
              rounded-[26px]
              border
              border-white/80
              bg-white
              p-5
              shadow-[0_24px_70px_rgba(15,23,42,0.12)]
              sm:rounded-[30px]
              sm:p-6
            "
          >
            {/* Background Glow */}
            <div
              className="
                pointer-events-none
                absolute
                -right-16
                -top-16
                h-44
                w-44
                rounded-full
                bg-cyan-300/30
                blur-3xl
              "
            />

            <div
              className="
                pointer-events-none
                absolute
                -bottom-20
                -left-16
                h-44
                w-44
                rounded-full
                bg-violet-300/20
                blur-3xl
              "
            />

            {/* HEADER */}
            <div
              className="
                relative
                flex
                items-start
                justify-between
                gap-4
              "
            >
              <div>
                <span
                  className="
                    text-[11px]
                    font-bold
                    uppercase
                    tracking-[0.18em]
                    text-cyan-600
                    sm:text-xs
                  "
                >
                  HOW TALENTSPHERE WORKS
                </span>

                <h2
                  className="
                    mt-2
                    text-2xl
                    font-bold
                    tracking-tight
                    text-slate-900
                    sm:text-3xl
                  "
                >
                  Build your career path
                </h2>

                <p
                  className="
                    mt-1
                    text-sm
                    leading-6
                    text-slate-500
                    sm:text-base
                  "
                >
                  From self-discovery to career growth in four
                  simple steps.
                </p>
              </div>

              <div
                className="
                  flex
                  h-11
                  w-11
                  shrink-0
                  items-center
                  justify-center
                  rounded-2xl
                  bg-gradient-to-br
                  from-cyan-500
                  to-violet-500
                  text-white
                  shadow-lg
                  sm:h-12
                  sm:w-12
                "
              >
                <Sparkles size={22} />
              </div>
            </div>

            {/* STEPS */}
            <div
              className="
                relative
                mt-6
                grid
                grid-cols-1
                gap-3
                sm:grid-cols-2
              "
            >
              {/* STEP 1 */}
              <div
                className="
                  group
                  rounded-2xl
                  bg-cyan-50
                  p-4
                  transition
                  duration-300
                  hover:-translate-y-1
                  hover:shadow-lg
                "
              >
                <div
                  className="
                    flex
                    h-10
                    w-10
                    items-center
                    justify-center
                    rounded-xl
                    bg-cyan-600
                    text-white
                    shadow-sm
                  "
                >
                  <UserRound size={19} />
                </div>

                <h3 className="mt-4 text-base font-bold text-slate-900 sm:text-lg">
                  Create Your Profile
                </h3>

                <p className="mt-1 text-sm leading-5 text-slate-500">
                  Tell us about your interests, skills and career
                  goals.
                </p>
              </div>

              {/* STEP 2 */}
              <div
                className="
                  group
                  rounded-2xl
                  bg-blue-50
                  p-4
                  transition
                  duration-300
                  hover:-translate-y-1
                  hover:shadow-lg
                "
              >
                <div
                  className="
                    flex
                    h-10
                    w-10
                    items-center
                    justify-center
                    rounded-xl
                    bg-blue-500
                    text-white
                    shadow-sm
                  "
                >
                  <Target size={19} />
                </div>

                <h3 className="mt-4 text-base font-bold text-slate-900 sm:text-lg">
                  Assess Your Skills
                </h3>

                <p className="mt-1 text-sm leading-5 text-slate-500">
                  Understand your strengths through practical
                  assessments.
                </p>
              </div>

              {/* STEP 3 */}
              <div
                className="
                  group
                  rounded-2xl
                  bg-violet-50
                  p-4
                  transition
                  duration-300
                  hover:-translate-y-1
                  hover:shadow-lg
                "
              >
                <div
                  className="
                    flex
                    h-10
                    w-10
                    items-center
                    justify-center
                    rounded-xl
                    bg-violet-500
                    text-white
                    shadow-sm
                  "
                >
                  <Sparkles size={19} />
                </div>

                <h3 className="mt-4 text-base font-bold text-slate-900 sm:text-lg">
                  Discover Career Paths
                </h3>

                <p className="mt-1 text-sm leading-5 text-slate-500">
                  Explore career options that match your profile.
                </p>
              </div>

              {/* STEP 4 */}
              <div
                className="
                  group
                  rounded-2xl
                  bg-emerald-50
                  p-4
                  transition
                  duration-300
                  hover:-translate-y-1
                  hover:shadow-lg
                "
              >
                <div
                  className="
                    flex
                    h-10
                    w-10
                    items-center
                    justify-center
                    rounded-xl
                    bg-emerald-500
                    text-white
                    shadow-sm
                  "
                >
                  <Rocket size={19} />
                </div>

                <h3 className="mt-4 text-base font-bold text-slate-900 sm:text-lg">
                  Follow Your Roadmap
                </h3>

                <p className="mt-1 text-sm leading-5 text-slate-500">
                  Learn, improve and move toward your career goals.
                </p>
              </div>
            </div>

            {/* BOTTOM CTA */}
            <div
              className="
                relative
                mt-4
                flex
                items-center
                justify-between
                gap-3
                rounded-2xl
                bg-slate-950
                px-4
                py-4
                text-white
                sm:px-5
              "
            >
              <div>
                <p className="text-xs text-slate-400 sm:text-sm">
                  Your career journey
                </p>

                <p className="mt-1 text-sm font-bold sm:text-base">
                  Starts with the right direction
                </p>
              </div>

              <div
                className="
                  flex
                  h-10
                  w-10
                  shrink-0
                  items-center
                  justify-center
                  rounded-full
                  bg-gradient-to-br
                  from-cyan-400
                  to-violet-500
                  text-lg
                  shadow-lg
                "
              >
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