import {
  Clock3,
  ArrowRight,
} from "lucide-react";

interface Activity {
  id: number;
  title: string;
  time: string;
}

interface ActivityCardProps {
  activities: Activity[];
}

function ActivityCard({
  activities,
}: ActivityCardProps) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

      {/* Header */}

      <div className="mb-6 flex items-center justify-between">

        <div>

          <h2 className="text-xl font-bold text-slate-900">
            Recent Activity
          </h2>

          <p className="mt-1 text-sm text-slate-500">
            Your latest progress and updates.
          </p>

        </div>

        <button className="flex items-center gap-2 text-sm font-semibold text-cyan-600 hover:text-cyan-700">

          View All

          <ArrowRight size={16} />

        </button>

      </div>

      {/* Activity List */}

      <div className="space-y-4">

        {activities.map((activity) => (

          <div
            key={activity.id}
            className="flex items-start gap-4 rounded-xl border border-slate-200 p-4 transition hover:bg-slate-50"
          >

            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-cyan-100">

              <Clock3
                size={18}
                className="text-cyan-600"
              />

            </div>

            <div className="flex-1">

              <p className="font-medium text-slate-800">

                {activity.title}

              </p>

              <p className="mt-1 text-sm text-slate-500">

                {activity.time}

              </p>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}

export default ActivityCard;