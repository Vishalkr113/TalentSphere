import { GraduationCap } from "lucide-react";

type LogoProps = {
  size?: "sm" | "md" | "lg";
};

function Logo({
  size = "md",
}: LogoProps) {
  const styles = {
    sm: {
      icon: 22,
      title: "text-xl",
      subtitle: "text-[10px]",
      box: "h-10 w-10",
    },
    md: {
      icon: 28,
      title: "text-2xl",
      subtitle: "text-xs",
      box: "h-12 w-12",
    },
    lg: {
      icon: 36,
      title: "text-3xl",
      subtitle: "text-sm",
      box: "h-14 w-14",
    },
  };

  const current = styles[size];

  return (
    <div className="flex items-center gap-3">

      <div
        className={`flex ${current.box} items-center justify-center rounded-2xl bg-cyan-600 text-white shadow-md`}
      >
        <GraduationCap size={current.icon} />
      </div>

      <div>

        <h1
          className={`font-bold text-slate-900 ${current.title}`}
        >
          TalentSphere
        </h1>

        <p
          className={`font-medium tracking-wide text-cyan-600 ${current.subtitle}`}
        >
          AI Career Development Platform
        </p>

      </div>

    </div>
  );
}

export default Logo;