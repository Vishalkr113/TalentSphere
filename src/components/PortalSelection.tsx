import { useLocation, useNavigate } from "react-router-dom";
import {
  GraduationCap,
  School,
  Briefcase,
  ArrowRight,
} from "lucide-react";

import Card from "./ui/Card";
import Button from "./ui/Button";
import Logo from "./ui/Logo";

type PortalRole =
  | "high-school-student"
  | "college-student"
  | "working-professional";

const portals = [
  {
    role: "high-school-student" as PortalRole,
    title: "High School Student",
    description:
      "Explore careers, choose the right stream, build future skills and prepare for success.",
    icon: School,
  },
  {
    role: "college-student" as PortalRole,
    title: "College Student",
    description:
      "Build resumes, practice coding, prepare for placements and grow your career.",
    icon: GraduationCap,
  },
  {
    role: "working-professional" as PortalRole,
    title: "Working Professional",
    description:
      "Advance your career, gain certifications, switch jobs and achieve promotion goals.",
    icon: Briefcase,
  },
];

function PortalSelection() {
  const navigate = useNavigate();
  const location = useLocation();

  const mode =
    new URLSearchParams(location.search).get("mode") ?? "login";

  const handleContinue = (role: PortalRole) => {
    navigate(`/${role}/${mode}`);
  };

  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-100 px-6 py-16">
      <div className="w-full max-w-7xl">

        <div className="mb-10 flex justify-center">
          <Logo size="md" />
        </div>

        <div className="text-center">

          <h1 className="text-[38px] font-bold text-slate-900">
            Choose Your Portal
          </h1>

          <p className="mx-auto mt-4 max-w-3xl text-lg text-slate-600">
            Select your learning stage to access personalized features and career guidance.
          </p>

        </div>

        <div className="mt-14 grid gap-8 md:grid-cols-3">

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
    </main>
  );
}

export default PortalSelection;