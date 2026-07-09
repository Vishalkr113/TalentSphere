import { useLocation, useNavigate } from "react-router-dom";
import {
  GraduationCap,
  Building2,
  Briefcase,
  ArrowRight,
} from "lucide-react";

import Card from "./ui/Card";
import Button from "./ui/Button";
import Logo from "./ui/Logo";

type PortalRole = "student" | "institute" | "professional";

const portals = [
  {
    role: "student" as PortalRole,
    title: "Student",
    description:
      "Build resumes, practice mock interviews and improve your skills.",
    icon: GraduationCap,
  },
  {
    role: "institute" as PortalRole,
    title: "Institute",
    description:
      "Manage students, monitor performance and placement activities.",
    icon: Building2,
  },
  {
    role: "professional" as PortalRole,
    title: "Professional",
    description:
      "Grow your career, build your portfolio and explore opportunities.",
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

        <div className="mb-14 flex justify-center">
          <Logo size="md" />
        </div>

        <div className="text-center">

          <h1 className="text-4xl font-bold text-slate-900">
            Choose Your Portal
          </h1>

          <p className="mx-auto mt-4 max-w-2xl text-base text-slate-600">
            Continue with the portal that best matches your profile.
          </p>

        </div>

        <div className="mt-14 grid gap-8 md:grid-cols-3">

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

                <p className="mt-4 text-slate-600 leading-7">
                  {portal.description}
                </p>

                <Button
                  className="mt-8 w-full"
                  onClick={() => handleContinue(portal.role)}
                >
                  Continue
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