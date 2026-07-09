import {
  Briefcase,
  UserCheck,
  CalendarDays,
  TrendingUp,
} from "lucide-react";

import DashboardLayout from "./DashboardLayout";
import StatCard from "./StatCard";
import TaskCard from "./TaskCard";
import ActivityCard from "./ActivityCard";

function ProfessionalDashboard() {
  const tasks = [
    {
      id: 1,
      title: "Update Professional Resume",
      completed: true,
    },
    {
      id: 2,
      title: "Apply for 3 Jobs",
      completed: false,
    },
    {
      id: 3,
      title: "Prepare for Interview",
      completed: false,
    },
    {
      id: 4,
      title: "Complete AI Career Analysis",
      completed: true,
    },
  ];

  const activities = [
    {
      id: 1,
      title: "Applied for Frontend Developer",
      time: "30 minutes ago",
    },
    {
      id: 2,
      title: "Resume updated",
      time: "Today",
    },
    {
      id: 3,
      title: "Interview scheduled",
      time: "Yesterday",
    },
    {
      id: 4,
      title: "AI suggested 5 new jobs",
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
          Track your career growth and job applications.
        </p>

      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        <StatCard
          title="Career Progress"
          value="84%"
          subtitle="Excellent"
          icon={TrendingUp}
        />

        <StatCard
          title="Profile Score"
          value="91%"
          subtitle="Almost Complete"
          icon={UserCheck}
          color="bg-green-100 text-green-600"
        />

        <StatCard
          title="Applied Jobs"
          value="24"
          subtitle="This Month"
          icon={Briefcase}
          color="bg-blue-100 text-blue-600"
        />

        <StatCard
          title="Interviews"
          value="5"
          subtitle="Upcoming"
          icon={CalendarDays}
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

export default ProfessionalDashboard;