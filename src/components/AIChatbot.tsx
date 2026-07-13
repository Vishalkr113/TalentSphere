import { useState } from "react";
import { AudioLines, X, Send } from "lucide-react";

function AIChatbot() {
  const [isOpen, setIsOpen] = useState(false);
  const [message, setMessage] = useState("");

  const [reply, setReply] = useState(
    "👋 Hello! I'm TalentSphere AI. How can I help you today?"
  );

  const quickSuggestions = [
    "Career Explorer",
    "Resume Builder",
    "Coding Assessment",
    "Mock Interview",
    "Subject Guidance",
    "AI Career Advisor",
  ];

  const handleSuggestion = (text: string) => {
    setMessage(text);

    switch (text) {
      case "Career Explorer":
        setReply(
          "🎓 I can help you explore Engineering, Medical, Commerce, Arts, Law and many more career options."
        );
        break;

      case "Resume Builder":
        setReply(
          "📄 Our AI Resume Builder helps College Students and Working Professionals create ATS-friendly resumes."
        );
        break;

      case "Coding Assessment":
        setReply(
          "💻 Practice coding questions, improve problem solving skills and prepare for placements."
        );
        break;

      case "Mock Interview":
        setReply(
          "🎤 Take AI-powered mock interviews with instant feedback and improvement tips."
        );
        break;

      case "Subject Guidance":
        setReply(
          "📚 High School Students can get guidance for Science, Commerce and Arts streams."
        );
        break;

      case "AI Career Advisor":
        setReply(
          "🤖 Get personalized career recommendations based on your interests, skills and goals."
        );
        break;

      default:
        setReply("How can I help you?");
    }
  };

  return (
    <>
      {/* Modern AI Voice Button */}

      <button
        type="button"
        onClick={() => setIsOpen(true)}
        aria-label="Open AI Assistant"
        className="group fixed bottom-6 right-6 z-50 flex h-14 w-14 items-center justify-center rounded-full bg-gradient-to-br from-cyan-500 via-blue-500 to-violet-600 text-white shadow-xl transition-all duration-300 hover:-translate-y-1 hover:scale-110 hover:shadow-2xl"
      >
        <span className="absolute inset-0 animate-ping rounded-full bg-cyan-400 opacity-20" />

        <span className="relative flex h-11 w-11 items-center justify-center rounded-full bg-white/15 backdrop-blur">
          <AudioLines
            size={27}
            strokeWidth={2.4}
          />
        </span>

        <span className="pointer-events-none absolute right-16 whitespace-nowrap rounded-lg bg-slate-900 px-3 py-2 text-xs font-medium text-white opacity-0 shadow-lg transition-opacity duration-200 group-hover:opacity-100">
          TalentSphere AI
        </span>
      </button>

      {/* Chat Window */}

      {isOpen && (
        <div className="fixed bottom-24 right-6 z-50 w-[370px] overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-2xl">

          {/* Header */}

          <div className="flex items-center justify-between bg-cyan-600 px-6 py-4 text-white">

            <div>
              <h2 className="text-lg font-bold">
                TalentSphere AI
              </h2>

              <p className="text-sm text-cyan-100">
                Your Career Assistant
              </p>
            </div>

            <button onClick={() => setIsOpen(false)}>
              <X size={22} />
            </button>

          </div>

          {/* Body */}

          <div className="space-y-5 p-6">

            <div className="rounded-2xl bg-slate-100 p-4 text-sm leading-7">
              {reply}
            </div>

            <div>

              <h3 className="mb-3 font-semibold">
                Quick Suggestions
              </h3>

              <div className="flex flex-wrap gap-2">

                {quickSuggestions.map((item) => (

                  <button
                    key={item}
                    onClick={() => handleSuggestion(item)}
                    className="rounded-full bg-cyan-50 px-3 py-2 text-sm text-cyan-700 transition hover:bg-cyan-100"
                  >
                    {item}
                  </button>

                ))}

              </div>

            </div>

          </div>

          {/* Footer */}

          <div className="border-t border-slate-200 p-4">

            <div className="flex gap-2">

              <input
                type="text"
                placeholder="Ask anything..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                className="flex-1 rounded-xl border border-slate-300 px-4 py-3 outline-none focus:border-cyan-600"
              />

              <button
                onClick={() => {
                  if (!message.trim()) return;
                  handleSuggestion(message);
                }}
                className="rounded-xl bg-cyan-600 px-4 text-white transition hover:bg-cyan-700"
              >
                <Send size={18} />
              </button>

            </div>

          </div>

        </div>
      )}
    </>
  );
}

export default AIChatbot;