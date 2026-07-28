import { useMemo } from "react";
import { useLocation, useNavigate } from "react-router-dom";

import {
  GraduationCap,
  School,
  Briefcase,
  ArrowRight,
} from "lucide-react";

import Card from "./ui/Card";
import Button from "./ui/Button";

type Portal =
  | "high-school-student"
  | "college-student"
  | "working-professional";

const portals = [
  {
    role: "high-school-student" as Portal,
    title: "High School Student",
    icon: School,
    description:
      "Career guidance, stream recommendation, scholarships and future planning.",
  },
  {
    role: "college-student" as Portal,
    title: "College Student",
    icon: GraduationCap,
    description:
      "Resume Builder, Skill Assessment, Coding Practice and Placement Preparation.",
  },
  {
    role: "working-professional" as Portal,
    title: "Working Professional",
    icon: Briefcase,
    description:
      "Career Growth, Resume Upgrade, AI Mentor and Promotion Readiness.",
  },
];

function PortalSelection() {
  const navigate = useNavigate();
  const location = useLocation();

  const mode = useMemo(() => {
    const params = new URLSearchParams(location.search);
    return params.get("mode") === "signup"
      ? "signup"
      : "login";
  }, [location.search]);

  const handleContinue = (role: Portal) => {
    navigate(`/${role}/${mode}`);
  };

  return (
    <section className="min-h-screen bg-slate-100 py-20">

      <div className="mx-auto max-w-6xl px-6">

        <div className="text-center">

          <h1 className="text-[38px] font-bold text-slate-900">
            Choose Your Learning Portal
          </h1>

          <p className="mt-4 text-lg text-slate-600">
            Select the portal that best matches your current learning journey.
          </p>

        </div>

        <div className="mt-16 grid gap-8 md:grid-cols-3">

          {portals.map((portal) => {

            const Icon = portal.icon;

            return (

              <Card
                key={portal.role}
                className="flex flex-col justify-between p-8"
              >

                <div>

                  <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

                    <Icon size={30} />

                  </div>

                  <h2 className="mt-6 text-2xl font-bold text-slate-900">

                    {portal.title}

                  </h2>

                  <p className="mt-4 leading-7 text-slate-600">

                    {portal.description}

                  </p>

                </div>

                <Button
                  className="mt-8 w-full"
                  onClick={() => handleContinue(portal.role)}
                >

                  Explore

                  <ArrowRight size={18} />

                </Button>

              </Card>

            );

          })}

        </div>

      </div>

    </section>
  );
}

export default PortalSelection;