import { useEffect, useRef, useState } from "react";
import { AudioLines, X, Send, Bot, User } from "lucide-react";
import { useAuth } from "../contexts/AuthContext";
import { generateAI } from "../services/aiService";

interface ChatMessage {
  id: number;
  sender: "user" | "ai";
  text: string;
}

function AIChatbot() {
  const { user } = useAuth();
  const [isOpen, setIsOpen] = useState(false);
  const [message, setMessage] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 1,
      sender: "ai",
      text: "Hello! I'm TalentSphere AI. Ask me anything about careers, skills, placements, resumes or learning.",
    },
  ]);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isTyping]);

  const quickSuggestions = [
    "How should I prepare for my target career?",
    "How can I improve my resume?",
    "How should I prepare for interviews?",
    "What skills should I learn next?",
  ];

  const sendMessage = async (raw: string) => {
    const text = raw.trim();
    if (!text || isTyping) return;

    setMessages((prev) => [
      ...prev,
      { id: Date.now(), sender: "user", text },
    ]);
    setMessage("");
    setIsTyping(true);

    try {
      const result = await generateAI(
        "chat",
        text,
        `Authenticated user role: ${user?.role ?? "unknown"}. Name: ${user?.full_name ?? "unknown"}.`
      );
      setMessages((prev) => [
        ...prev,
        { id: Date.now() + 1, sender: "ai", text: result.text },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          id: Date.now() + 1,
          sender: "ai",
          text: error instanceof Error
            ? error.message
            : "AI service is temporarily unavailable.",
        },
      ]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <>
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

      {isOpen && (
        <div className="fixed bottom-24 right-6 z-50 flex h-[500px] w-[360px] flex-col overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-2xl">
          <div className="flex items-center justify-between bg-gradient-to-r from-cyan-600 to-blue-600 px-6 py-4 text-white">
            <div className="flex items-center gap-3">
              <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-white/15">
                <AudioLines size={22} />
              </div>
              <div>
                <h2 className="font-bold">TalentSphere AI</h2>
                <p className="text-xs text-cyan-100">Gemini-powered Career Assistant</p>
              </div>
            </div>
            <button onClick={() => setIsOpen(false)} className="rounded-xl p-2.5 transition hover:bg-white/10">
              <X size={20} />
            </button>
          </div>

          <div className="flex-1 space-y-3 overflow-y-auto bg-slate-50 p-4">
            {messages.map((chat) => (
              <div key={chat.id} className={`flex ${chat.sender === "user" ? "justify-end" : "justify-start"}`}>
                <div className={`flex max-w-[82%] gap-3 ${chat.sender === "user" ? "flex-row-reverse" : ""}`}>
                  <div className={`flex h-10 w-10 shrink-0 items-center justify-center rounded-full ${chat.sender === "user" ? "bg-cyan-600 text-white" : "bg-slate-200 text-slate-700"}`}>
                    {chat.sender === "user" ? <User size={18} /> : <Bot size={18} />}
                  </div>
                  <div className={`rounded-2xl px-4 py-3 text-sm leading-6 shadow-sm ${chat.sender === "user" ? "bg-cyan-600 text-white" : "bg-white text-slate-700"}`}>
                    {chat.text}
                  </div>
                </div>
              </div>
            ))}
            {isTyping && (
              <div className="flex gap-3">
                <div className="flex h-10 w-10 items-center justify-center rounded-full bg-slate-200"><Bot size={18} /></div>
                <div className="rounded-2xl bg-white px-4 py-3 shadow-sm text-sm text-slate-500">Thinking…</div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <div className="border-t border-slate-200 bg-white p-3">
            {messages.length === 1 && (
              <div className="mb-2 flex flex-wrap gap-2">
                {quickSuggestions.map((item) => (
                  <button key={item} type="button" onClick={() => void sendMessage(item)} className="rounded-full bg-cyan-50 px-2.5 py-1.5 text-[11px] font-medium text-cyan-700 transition hover:bg-cyan-100">
                    {item}
                  </button>
                ))}
              </div>
            )}
            <div className="flex gap-2">
              <input
                type="text"
                placeholder="Ask anything..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={(e) => { if (e.key === "Enter") void sendMessage(message); }}
                className="flex-1 rounded-xl border border-slate-300 px-4 py-2.5 text-sm outline-none transition focus:border-cyan-500"
              />
              <button type="button" disabled={isTyping} onClick={() => void sendMessage(message)} className="rounded-xl bg-cyan-600 px-4 py-2.5 text-white transition hover:bg-cyan-700 disabled:opacity-50">
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
