interface Props {
  role: string;
  setRole: (
    role: "student" | "professional" | "institute"
  ) => void;
}

function PortalTabs({
  role,
  setRole,
}: Props) {
  const tabs = [
    {
      id: "student",
      label: "🎓 Student",
    },
    {
      id: "professional",
      label: "💼 Professional",
    },
    {
      id: "institute",
      label: "🏢 Institute",
    },
  ];

  return (
    <div className="mb-8 flex rounded-xl bg-slate-100 p-1">
      {tabs.map((tab) => (
        <button
          key={tab.id}
          onClick={() =>
            setRole(
              tab.id as
              | "student"
              | "professional"
              | "institute"
            )
          }
          className={`flex-1 rounded-lg py-3 text-sm font-semibold transition ${role === tab.id
            ? "bg-cyan-600 text-white shadow"
            : "text-slate-600 hover:bg-white"
            }`}
        >
          {tab.label}
        </button>
      ))}
    </div>
  );
}

export default PortalTabs;