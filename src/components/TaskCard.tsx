import {
  CheckCircle2,
  Circle,
} from "lucide-react";

interface Task {
  id: number;
  title: string;
  completed: boolean;
}

interface TaskCardProps {
  tasks: Task[];
}

function TaskCard({
  tasks,
}: TaskCardProps) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

      <div className="mb-6 flex items-center justify-between">

        <div>

          <h2 className="text-xl font-bold text-slate-900">
            Today's Tasks
          </h2>

          <p className="mt-1 text-sm text-slate-500">
            Complete your daily goals.
          </p>

        </div>

        <span className="rounded-full bg-cyan-100 px-3 py-1 text-sm font-semibold text-cyan-700">

          {
            tasks.filter(
              (task) => task.completed
            ).length
          }

          /

          {tasks.length}

        </span>

      </div>

      <div className="space-y-4">

        {tasks.map((task) => (

          <div
            key={task.id}
            className="flex items-center justify-between rounded-xl border border-slate-200 p-4 transition hover:bg-slate-50"
          >

            <div className="flex items-center gap-3">

              {task.completed ? (

                <CheckCircle2
                  size={22}
                  className="text-green-600"
                />

              ) : (

                <Circle
                  size={22}
                  className="text-slate-400"
                />

              )}

              <span
                className={`font-medium ${task.completed
                    ? "text-slate-400 line-through"
                    : "text-slate-800"
                  }`}
              >
                {task.title}
              </span>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}

export default TaskCard;