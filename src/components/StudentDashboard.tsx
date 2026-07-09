import {
  Target,
  FileText,
  Code2,
  Brain,
} from "lucide-react";

import DashboardLayout from "./DashboardLayout";
import StatCard from "./StatCard";
import TaskCard from "./TaskCard";
import ActivityCard from "./ActivityCard";

function StudentDashboard() {
  const tasks = [
    {
      id: 1,
      title: "Complete Resume",
      completed: true,
    },
    {
      id: 2,
      title: "Practice Aptitude",
      completed: false,
    },
    {
      id: 3,
      title: "Complete Java Quiz",
      completed: false,
    },
    {
      id: 4,
      title: "AI Career Recommendation",
      completed: true,
    },
  ];

  const activities = [
    {
      id: 1,
      title: "Resume updated successfully",
      time: "10 minutes ago",
    },
    {
      id: 2,
      title: "Java Quiz completed",
      time: "1 hour ago",
    },
    {
      id: 3,
      title: "Skill Assessment finished",
      time: "Yesterday",
    },
    {
      id: 4,
      title: "AI Career Report generated",
      time: "2 days ago",
    },
  ];

  return (
    <DashboardLayout>

      {/* Welcome */}

      <div className="mb-8">

        <h2 className="text-3xl font-bold text-slate-900">
          Welcome Back 👋
        </h2>

        <p className="mt-2 text-slate-600">
          Keep learning and improve your career every day.
        </p>

      </div>

      {/* Statistics */}

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">

        <StatCard
          title="Placement Score"
          value="82%"
          subtitle="Excellent Progress"
          icon={Target}
        />

        <StatCard
          title="Resume Score"
          value="76%"
          subtitle="Needs Improvement"
          icon={FileText}
          color="bg-green-100 text-green-600"
        />

        <StatCard
          title="Coding Progress"
          value="68%"
          subtitle="Keep Practicing"
          icon={Code2}
          color="bg-blue-100 text-blue-600"
        />

        <StatCard
          title="Skill Score"
          value="73%"
          subtitle="Above Average"
          icon={Brain}
          color="bg-purple-100 text-purple-600"
        />

      </div>

      {/* Bottom Section */}

      <div className="mt-8 grid gap-6 xl:grid-cols-2">

        <TaskCard tasks={tasks} />

        <ActivityCard activities={activities} />

      </div>

    </DashboardLayout>
  );
}

export default StudentDashboard;