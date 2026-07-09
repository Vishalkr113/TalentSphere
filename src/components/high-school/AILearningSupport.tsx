import { useState } from "react";
import {
  Bot,
  Send,
  Lightbulb,
  BookOpen,
  Brain,
} from "lucide-react";

function AILearningSupport() {
  const [question, setQuestion] = useState("");

  return (
    <div className="space-y-10">

      {/* Heading */}

      <div>

        <h1 className="text-4xl font-bold text-slate-900">
          AI Learning Support
        </h1>

        <p className="mt-3 text-lg text-slate-600">
          Ask AI your doubts, get study tips and receive
          personalized learning guidance.
        </p>

      </div>

      {/* Chat Box */}

      <div className="rounded-3xl border border-slate-200 bg-white shadow-sm">

        {/* Header */}

        <div className="flex items-center gap-4 border-b border-slate-200 p-6">

          <div className="flex h-14 w-14 items-center justify-center rounded-2xl bg-cyan-100 text-cyan-600">

            <Bot size={30} />

          </div>

          <div>

            <h2 className="text-xl font-bold text-slate-900">
              TalentSphere AI
            </h2>

            <p className="text-sm text-slate-500">
              Your Personal Learning Assistant
            </p>

          </div>

        </div>

        {/* AI Response */}

        <div className="space-y-6 p-6">

          <div className="max-w-xl rounded-2xl bg-cyan-50 p-5">

            <p className="leading-7 text-slate-700">

              👋 Hello! I'm your AI Learning Assistant.

              <br />
              <br />

              I can help you with:

              <br />
              • Subject Guidance

              <br />
              • Study Planning

              <br />
              • Career Advice

              <br />
              • Exam Preparation

              <br />
              • Learning Roadmap

            </p>

          </div>

        </div>

        {/* Input */}

        <div className="border-t border-slate-200 p-6">

          <div className="flex gap-4">

            <input
              value={question}
              onChange={(e) =>
                setQuestion(e.target.value)
              }
              placeholder="Ask anything..."
              className="flex-1 rounded-xl border border-slate-300 px-5 py-3 outline-none focus:border-cyan-600"
            />

            <button className="rounded-xl bg-cyan-600 px-6 text-white transition hover:bg-cyan-700">

              <Send size={20} />

            </button>

          </div>

        </div>

      </div>

      {/* Quick Suggestions */}

      <div>

        <h2 className="mb-6 text-2xl font-bold text-slate-900">
          Quick Learning Topics
        </h2>

        <div className="grid gap-6 md:grid-cols-3">

          <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

            <BookOpen className="text-cyan-600" size={34} />

            <h3 className="mt-5 text-xl font-bold">
              Study Tips
            </h3>

            <p className="mt-3 text-slate-600">
              Learn smart study techniques and improve
              your daily learning habits.
            </p>

          </div>

          <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

            <Brain className="text-cyan-600" size={34} />

            <h3 className="mt-5 text-xl font-bold">
              Exam Preparation
            </h3>

            <p className="mt-3 text-slate-600">
              Get personalized strategies to score
              better in school examinations.
            </p>

          </div>

          <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

            <Lightbulb className="text-cyan-600" size={34} />

            <h3 className="mt-5 text-xl font-bold">
              Career Advice
            </h3>

            <p className="mt-3 text-slate-600">
              Explore career opportunities and choose
              the right learning path.
            </p>

          </div>

        </div>

      </div>

    </div>
  );
}

export default AILearningSupport;