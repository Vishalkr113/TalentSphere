import { useEffect, useRef, useState } from "react";
import { AudioLines, X, Send, Bot, User } from "lucide-react";

interface ChatMessage {
  id: number;
  sender: "user" | "ai";
  text: string;
}

function AIChatbot() {
  const [isOpen, setIsOpen] = useState(false);

  const [message, setMessage] = useState("");

  const [isTyping, setIsTyping] = useState(false);

  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 1,
      sender: "ai",
      text: "👋 Hello! Welcome to TalentSphere Elevate. I'm your AI Career Assistant. Ask me anything about careers, skills, placements, resumes or learning.",
    },
  ]);

  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, isTyping]);

  const quickSuggestions = [
    "Career Explorer",
    "Resume Builder",
    "Coding Assessment",
    "Mock Interview",
    "Career Roadmap",
    "Placement Preparation",
  ];

  const getAIResponse = (text: string): string => {
    const msg = text.toLowerCase().trim();

    if (msg.includes("hi") || msg.includes("hello")) {
      return "👋 Hello! Welcome to TalentSphere. How can I help you with your career today?";
    }

    if (msg.includes("career")) {
      return "🎯 TalentSphere helps you discover career paths based on your interests, skills and future goals.";
    }

    if (msg.includes("resume")) {
      return "📄 Our Resume Builder helps you create ATS-friendly resumes with professional formatting and suggestions.";
    }

    if (msg.includes("coding")) {
      return "💻 Practice coding questions, improve problem-solving skills and prepare for technical interviews.";
    }

    if (
      msg.includes("placement") ||
      msg.includes("job")
    ) {
      return "🚀 Improve your placement readiness with aptitude practice, coding assessments and mock interviews.";
    }

    if (msg.includes("interview")) {
      return "🎤 Practice HR and technical interviews with AI-generated questions and instant feedback.";
    }

    if (
      msg.includes("roadmap") ||
      msg.includes("learning")
    ) {
      return "🛣️ TalentSphere creates personalized learning roadmaps according to your target career.";
    }

    if (
      msg.includes("skill") ||
      msg.includes("assessment")
    ) {
      return "📊 Skill Assessment evaluates your strengths and recommends areas for improvement.";
    }

    if (
      msg.includes("college") ||
      msg.includes("student")
    ) {
      return "🎓 College students can access Resume Builder, Coding Practice, Placement Preparation and Career Guidance.";
    }

    if (
      msg.includes("school") ||
      msg.includes("12th")
    ) {
      return "🏫 High School students receive stream selection guidance, scholarship information and career exploration support.";
    }

    if (
      msg.includes("professional") ||
      msg.includes("promotion")
    ) {
      return "💼 Working professionals can use TalentSphere for career growth, promotions, resume upgrades and skill development.";
    }

    if (
      msg.includes("python") ||
      msg.includes("java") ||
      msg.includes("javascript")
    ) {
      return "👨‍💻 Learning programming with regular practice and projects is the best way to build a strong technical career.";
    }

    if (
      msg.includes("ai") ||
      msg.includes("artificial intelligence")
    ) {
      return "🤖 TalentSphere AI provides career guidance, resume analysis, mock interviews, skill gap analysis and learning recommendations.";
    }

    if (
      msg.includes("thanks") ||
      msg.includes("thank you")
    ) {
      return "😊 You're welcome! I'm always here to help with your career journey.";
    }

    return "🤖 I couldn't understand your question completely. Try asking about careers, resumes, placements, coding, interviews, roadmaps or skills.";
  };

  return (
    <>
      {/* Floating AI Button */}

      <button
        type="button"
        onClick={() => setIsOpen(true)}
        aria-label="Open AI Assistant"
        className="group fixed bottom-5 right-5 z-50 flex h-14 w-14 items-center justify-center rounded-full bg-gradient-to-br from-cyan-500 via-blue-500 to-violet-600 text-white shadow-xl transition-all duration-300 hover:-translate-y-1 hover:scale-110 hover:shadow-2xl"
      >
        <span className="absolute inset-0 animate-ping rounded-full bg-cyan-400 opacity-20" />

        <span className="relative flex h-11 w-11 items-center justify-center rounded-full bg-white/15 backdrop-blur">
          <AudioLines size={26} strokeWidth={2.3} />
        </span>
      </button>

      {/* Chat Window */}

      {isOpen && (
        <div className="fixed bottom-24 right-6 z-50 flex h-[500px] w-[360px] flex-col overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-2xl">

          {/* Header */}

          <div className="flex items-center justify-between bg-gradient-to-r from-cyan-600 to-blue-600 px-6 py-4 text-white">

            <div className="flex items-center gap-3">

              <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-white/15">
                <AudioLines size={22} />
              </div>

              <div>
                <h2 className="font-bold">
                  TalentSphere AI
                </h2>

                <p className="text-xs text-cyan-100">
                  Smart Career Assistant
                </p>
              </div>

            </div>

            <button
              onClick={() => setIsOpen(false)}
              className="rounded-xl p-2.5 transition hover:bg-white/10"
            >
              <X size={20} />
            </button>

          </div>

          {/* Messages */}

          <div className="flex-1 space-y-3 overflow-y-auto bg-slate-50 p-4">

            {messages.map((chat) => (

              <div
                key={chat.id}
                className={`flex ${chat.sender === "user"
                  ? "justify-end"
                  : "justify-start"
                  }`}
              >

                <div
                  className={`flex max-w-[80%] gap-3 ${chat.sender === "user"
                    ? "flex-row-reverse"
                    : ""
                    }`}
                >

                  {/* Avatar */}

                  <div
                    className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full ${chat.sender === "user"
                      ? "bg-cyan-600 text-white"
                      : "bg-slate-200 text-slate-700"
                      }`}
                  >

                    {chat.sender === "user" ? (
                      <User size={18} />
                    ) : (
                      <Bot size={18} />
                    )}

                  </div>

                  {/* Bubble */}

                  <div
                    className={`rounded-2xl px-4 py-3 text-sm leading-6 shadow-sm ${chat.sender === "user"
                      ? "bg-cyan-600 text-white"
                      : "bg-white text-slate-700"
                      }`}
                  >
                    {chat.text}
                  </div>

                </div>

              </div>

            ))}

            {/* Typing */}

            {isTyping && (

              <div className="flex gap-3">

                <div className="flex h-10 w-10 items-center justify-center rounded-full bg-slate-200">
                  <Bot size={18} />
                </div>

                <div className="rounded-2xl bg-white px-4 py-3 shadow-sm">

                  <div className="flex gap-1">

                    <span className="h-2 w-2 animate-bounce rounded-full bg-slate-400" />

                    <span
                      className="h-2 w-2 animate-bounce rounded-full bg-slate-400"
                      style={{ animationDelay: "0.15s" }}
                    />

                    <span
                      className="h-2 w-2 animate-bounce rounded-full bg-slate-400"
                      style={{ animationDelay: "0.3s" }}
                    />

                  </div>

                </div>

              </div>

            )}

            <div ref={messagesEndRef} />

          </div>
          {/* Footer */}

          <div className="border-t border-slate-200 bg-white p-3">

            {/* Quick Suggestions */}

            {messages.length === 1 && (
              <div className="mb-2 flex flex-wrap gap-2">
                {quickSuggestions.map((item) => (

                  <button
                    key={item}
                    type="button"
                    onClick={() => {

                      const userMessage: ChatMessage = {
                        id: Date.now(),
                        sender: "user",
                        text: item,
                      };

                      setMessages((prev) => [...prev, userMessage]);

                      setIsTyping(true);

                      setTimeout(() => {

                        const aiMessage: ChatMessage = {
                          id: Date.now() + 1,
                          sender: "ai",
                          text: getAIResponse(item),
                        };

                        setMessages((prev) => [...prev, aiMessage]);

                        setIsTyping(false);

                      }, 700);

                    }}
                    className="rounded-full bg-cyan-50 px-2.5 py-1.5 text-[11px] font-medium text-cyan-700 transition hover:bg-cyan-100"
                  >
                    {item}
                  </button>

                ))}

              </div>
            )}

            {/* Input */}

            <div className="flex gap-2">

              <input
                type="text"
                placeholder="Ask anything..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={(e) => {

                  if (e.key !== "Enter") return;

                  if (!message.trim()) return;

                  const userMessage: ChatMessage = {
                    id: Date.now(),
                    sender: "user",
                    text: message,
                  };

                  setMessages((prev) => [...prev, userMessage]);

                  const currentMessage = message;

                  setMessage("");

                  setIsTyping(true);

                  setTimeout(() => {

                    const aiMessage: ChatMessage = {
                      id: Date.now() + 1,
                      sender: "ai",
                      text: getAIResponse(currentMessage),
                    };

                    setMessages((prev) => [...prev, aiMessage]);

                    setIsTyping(false);

                  }, 900);

                }}
                className="flex-1 rounded-xl border border-slate-300 px-4 py-2.5 text-sm outline-none transition focus:border-cyan-500"
              />

              <button
                type="button"
                onClick={() => {

                  if (!message.trim()) return;

                  const userMessage: ChatMessage = {
                    id: Date.now(),
                    sender: "user",
                    text: message,
                  };

                  setMessages((prev) => [...prev, userMessage]);

                  const currentMessage = message;

                  setMessage("");

                  setIsTyping(true);

                  setTimeout(() => {

                    const aiMessage: ChatMessage = {
                      id: Date.now() + 1,
                      sender: "ai",
                      text: getAIResponse(currentMessage),
                    };

                    setMessages((prev) => [...prev, aiMessage]);

                    setIsTyping(false);

                  }, 900);

                }}
                className="rounded-xl bg-cyan-600 px-4 py-2.5 text-white transition hover:bg-cyan-700"
              >
                <Send size={18} />
              </button>

            </div>

          </div>

        </div >

      )
      }

    </>

  );

}

export default AIChatbot;