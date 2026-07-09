import {
  Users,
  GraduationCap,
  Building2,
  BriefcaseBusiness,
} from "lucide-react";

import DashboardLayout from "./DashboardLayout";
import StatCard from "./StatCard";
import TaskCard from "./TaskCard";
import ActivityCard from "./ActivityCard";

function InstituteDashboard() {
  const tasks = [
    {
      id: 1,
      title: "Schedule Campus Drive",
      completed: true,
    },
    {
      id: 2,
      title: "Review Student Profiles",
      completed: false,
    },
    {
      id: 3,
      title: "Approve New Recruiter",
      completed: false,
    },
    {
      id: 4,
      title: "Publish Placement Report",
      completed: true,
    },
  ];

  const activities = [
    {
      id: 1,
      title: "TCS Campus Drive Created",
      time: "20 minutes ago",
    },
    {
      id: 2,
      title: "150 Student Profiles Updated",
      time: "Today",
    },
    {
      id: 3,
      title: "Infosys Recruitment Approved",
      time: "Yesterday",
    },
    {
      id: 4,
      title: "Monthly Placement Report Generated",
      time: "2 days ago",
    },
  ];

  return (
    <DashboardLayout>

      <div className="mb-8">

        <h2 className="text-3xl font-bold text-slate-900">
          Welcome Back 👋
        </h2>

        <p className="mt-2 text-slate-600">
          Manage students, recruiters and placement activities.
        </p>

      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        <StatCard
          title="Total Students"
          value="2,450"
          subtitle="Active Students"
          icon={Users}
        />

        <StatCard
          title="Placement Rate"
          value="87%"
          subtitle="Current Year"
          icon={GraduationCap}
          color="bg-green-100 text-green-600"
        />

        <StatCard
          title="Recruiters"
          value="58"
          subtitle="Active Companies"
          icon={Building2}
          color="bg-blue-100 text-blue-600"
        />

        <StatCard
          title="Campus Drives"
          value="12"
          subtitle="This Month"
          icon={BriefcaseBusiness}
          color="bg-purple-100 text-purple-600"
        />

      </div>

      <div className="mt-8 grid gap-6 xl:grid-cols-2">

        <TaskCard tasks={tasks} />

        <ActivityCard activities={activities} />

      </div>

    </DashboardLayout>
  );
}

export default InstituteDashboard;