import { useMemo } from "react";
import { useLocation, useNavigate } from "react-router-dom";

import {
  GraduationCap,
  Building2,
  Briefcase,
  ArrowRight,
} from "lucide-react";

import Card from "./ui/Card";
import Button from "./ui/Button";

type Portal =
  | "student"
  | "institute"
  | "professional";

const portals = [
  {
    role: "student" as Portal,
    title: "Student",
    icon: GraduationCap,
    description:
      "Resume Builder, Mock Interview, Skill Assessment and Career Guidance.",
  },
  {
    role: "institute" as Portal,
    title: "Institute",
    icon: Building2,
    description:
      "Student Management, Placements and Performance Analytics.",
  },
  {
    role: "professional" as Portal,
    title: "Professional",
    icon: Briefcase,
    description:
      "Portfolio, Career Growth and Job Opportunities.",
  },
];

function PortalSelection() {
  const navigate = useNavigate();
  const location = useLocation();

  const mode = useMemo(() => {
    const params = new URLSearchParams(location.search);
    return params.get("mode") === "register"
      ? "register"
      : "login";
  }, [location.search]);

  const handleContinue = (role: Portal) => {
    navigate(`/${role}/${mode}`);
  };

  return (
    <section className="min-h-screen bg-slate-100 py-20">

      <div className="mx-auto max-w-6xl px-6">

        <div className="text-center">

          <h1 className="text-4xl font-bold text-slate-900">

            Choose Your Portal

          </h1>

          <p className="mt-4 text-base text-slate-600">

            Select the portal that best matches your profile.

          </p>

        </div>

        <div className="mt-16 grid gap-8 md:grid-cols-3">

          {portals.map((portal) => {

            const Icon = portal.icon;

            return (

              <Card key={portal.role}>

                <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                  <Icon size={30} />

                </div>

                <h2 className="mt-6 text-xl font-bold text-slate-900">

                  {portal.title}

                </h2>

                <p className="mt-4 leading-7 text-slate-600">

                  {portal.description}

                </p>

                <div className="mt-8">

                  <Button
                    className="w-full"
                    onClick={() =>
                      handleContinue(portal.role)
                    }
                  >

                    Continue

                    <ArrowRight size={18} />

                  </Button>

                </div>

              </Card>

            );

          })}

        </div>

      </div>

    </section>
  );
}

export default PortalSelection;