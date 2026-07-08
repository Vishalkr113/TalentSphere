import {
  GraduationCap,
  Building2,
  Briefcase,
  ArrowRight,
} from "lucide-react";

import { Link } from "react-router-dom";

import Card from "./ui/Card";

const portals = [
  {
    title: "Student",
    description:
      "Build your resume, improve your skills, prepare for interviews and get AI career guidance.",
    icon: GraduationCap,
    color: "bg-cyan-600",
    route: "/student/login",
  },
  {
    title: "Institute",
    description:
      "Manage students, departments, placements and academic performance efficiently.",
    icon: Building2,
    color: "bg-violet-600",
    route: "/institute/login",
  },
  {
    title: "Professional",
    description:
      "Track career growth, manage your profile and explore new opportunities.",
    icon: Briefcase,
    color: "bg-emerald-600",
    route: "/professional/login",
  },
];

function PortalSection() {
  return (
    <section className="bg-white py-24">

      <div className="mx-auto max-w-7xl px-6">

        <div className="text-center">

          <span className="rounded-full bg-cyan-100 px-4 py-2 text-sm font-semibold text-cyan-700">
            Choose Your Portal
          </span>

          <h2 className="mt-6 text-4xl font-bold text-slate-900">

            One Platform

            <span className="text-cyan-600">
              {" "}Three Experiences
            </span>

          </h2>

          <p className="mx-auto mt-5 max-w-2xl text-lg text-slate-600">

            TalentSphere provides dedicated portals
            for Students, Institutes and Professionals.

          </p>

        </div>

        <div className="mt-16 grid gap-8 md:grid-cols-2 xl:grid-cols-3">

          {portals.map((portal) => {
            const Icon = portal.icon;

            return (
              <Card
                key={portal.title}
                className="group hover:-translate-y-2"
              >

                <div
                  className={`flex h-16 w-16 items-center justify-center rounded-2xl ${portal.color} text-white`}
                >
                  <Icon size={34} />
                </div>

                <h3 className="mt-6 text-2xl font-bold text-slate-900">
                  {portal.title}
                </h3>

                <p className="mt-4 leading-7 text-slate-600">
                  {portal.description}
                </p>

                <Link
                  to={portal.route}
                  className="mt-8 inline-flex items-center gap-2 font-semibold text-cyan-600 transition hover:gap-3"
                >
                  Continue

                  <ArrowRight size={18} />

                </Link>

              </Card>
            );
          })}

        </div>

      </div>

    </section>
  );
}

export default PortalSection;