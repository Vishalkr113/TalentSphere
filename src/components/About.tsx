import {
  Briefcase,
  GraduationCap,
  School,
} from "lucide-react";

import Card from "./ui/Card";

import { Link } from "react-router-dom";

const userTypes = [
  {
    title: "High School Student",
    description:
      "Career Guidance • Subject Guidance • Scholarships • Stream Selection",
    icon: School,
    login: "/high-school-student/login",
    register: "/high-school-student/register",
  },
  {
    title: "College Student",
    description:
      "Resume Builder • Coding Practice • Placement Preparation • Skill Assessment",
    icon: GraduationCap,
    login: "/college-student/login",
    register: "/college-student/register",
  },
  {
    title: "Working Professional",
    description:
      "Career Growth • Promotion • Resume Upgrade • AI Mentor",
    icon: Briefcase,
    login: "/working-professional/login",
    register: "/working-professional/register",
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
            About TalentSphere Elevate
          </span>

          <h2 className="mt-6 text-4xl font-bold text-slate-900 md:text-5xl">

            One Intelligent Platform

            <span className="block text-cyan-600">
              For Every Career Stage
            </span>

          </h2>

          <p className="mt-6 text-lg leading-8 text-slate-600">

            TalentSphere Elevate is an AI-powered career development
            platform built for <strong>High School Students</strong>,
            <strong> College Students</strong> and
            <strong> Working Professionals</strong>.

          </p>

          <p className="mt-5 text-lg leading-8 text-slate-600">

            Whether you are choosing your first career path,
            preparing for placements or planning your next promotion,
            TalentSphere provides AI-powered guidance,
            assessments, learning roadmaps and career support
            at every stage.

          </p>

        </div>

        {/* Who Can Use */}

        <div className="mt-20">

          <h3 className="text-center text-3xl font-bold text-slate-900">

            Who Can Use TalentSphere?

          </h3>

          <div className="mt-12 grid gap-8 md:grid-cols-3">

            {userTypes.map((item) => {

              const Icon = item.icon;

              return (
                <Card
                  key={item.title}
                  className="text-center transition duration-300 hover:-translate-y-2 hover:shadow-2xl"
                >
                  <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">
                    <Icon size={30} />
                  </div>

                  <h4 className="mt-6 text-xl font-bold text-slate-900">
                    {item.title}
                  </h4>

                  <p className="mt-4 min-h-[90px] leading-7 text-slate-600">
                    {item.description}
                  </p>

                  <div className="mt-8 flex gap-3">

                    <Link
                      to={item.login}
                      className="flex-1 rounded-xl bg-cyan-600 px-4 py-3 text-center font-semibold text-white transition hover:bg-cyan-700"
                    >
                      Login
                    </Link>

                    <Link
                      to={item.register}
                      className="flex-1 rounded-xl border border-cyan-600 px-4 py-3 text-center font-semibold text-cyan-600 transition hover:bg-cyan-50"
                    >
                      Register
                    </Link>

                  </div>
                </Card>
              );
            })}

          </div>

        </div>

      </div>
    </section>
  );
}

export default About;