"use client";

import { useState, useRef, useEffect } from "react";

type Message = {
  role: "user" | "assistant";
  content: string;
  model?: string;
  agent?: string;
};

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [project, setProject] = useState("auto");
  const [agent, setAgent] = useState("commander");
  const [model, setModel] = useState("auto");
  const [mode, setMode] = useState("chat");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMessage: Message = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input, model, agent, project, mode }),
      });

      const data = await res.json();
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.response,
          model: data.model,
          agent: data.agent,
        },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "⚠️ Could not connect to JARVIS API. Make sure the backend is running on http://localhost:8000.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="h-full flex flex-col">
      {/* Controls */}
      <div className="p-4 bg-white border-b flex flex-wrap gap-3 items-center">
        <select className="jarvis-select text-sm" value={project} onChange={(e) => setProject(e.target.value)}>
          <option value="auto">Project: Auto</option>
          <option value="aligna">Aligna</option>
          <option value="raf4">RAF4</option>
          <option value="oddb">ODDB</option>
        </select>
        <select className="jarvis-select text-sm" value={agent} onChange={(e) => setAgent(e.target.value)}>
          <option value="commander">Agent: Commander</option>
          <option value="coding-supervisor">Coding Supervisor</option>
          <option value="project-agent">Project Agent</option>
          <option value="research">Research</option>
          <option value="office">Office</option>
          <option value="memory">Memory</option>
          <option value="automation">Automation</option>
        </select>
        <select className="jarvis-select text-sm" value={model} onChange={(e) => setModel(e.target.value)}>
          <option value="auto">Model: Auto</option>
          <option value="gpt">GPT</option>
          <option value="claude">Claude Code</option>
          <option value="deepseek">DeepSeek</option>
          <option value="moonshot">Moonshot</option>
        </select>
        <select className="jarvis-select text-sm" value={mode} onChange={(e) => setMode(e.target.value)}>
          <option value="chat">Mode: Chat</option>
          <option value="plan">Plan</option>
          <option value="execute">Execute (Coming Soon)</option>
          <option value="review">Review (Coming Soon)</option>
        </select>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.length === 0 && (
          <div className="text-center text-gray-400 mt-20">
            <div className="text-6xl mb-4">💬</div>
            <h2 className="text-xl font-semibold text-gray-600">JARVIS Chat</h2>
            <p className="mt-2">Select your model, agent, and project above.</p>
            <p className="text-sm">Then type a message to get started.</p>
          </div>
        )}

        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
            <div
              className={`max-w-[70%] rounded-lg p-4 ${
                msg.role === "user"
                  ? "bg-[#8DC63F] text-white"
                  : "bg-white border shadow-sm"
              }`}
            >
              {msg.role === "assistant" && (
                <div className="flex items-center gap-2 mb-2 text-xs text-gray-400">
                  {msg.model && <span className="px-2 py-0.5 bg-gray-100 rounded">Model: {msg.model}</span>}
                  {msg.agent && <span className="px-2 py-0.5 bg-gray-100 rounded">Agent: {msg.agent}</span>}
                </div>
              )}
              <div className="whitespace-pre-wrap text-sm">{msg.content}</div>
            </div>
          </div>
        ))}

        {loading && (
          <div className="flex justify-start">
            <div className="bg-white border rounded-lg p-4 shadow-sm">
              <div className="flex items-center gap-2 text-gray-400 text-sm">
                <div className="w-2 h-2 rounded-full bg-[#8DC63F] animate-pulse"></div>
                Thinking...
              </div>
            </div>
          </div>
        )}

        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div className="p-4 bg-white border-t">
        <div className="flex gap-3 max-w-4xl mx-auto">
          <input
            type="text"
            className="jarvis-input flex-1"
            placeholder="Type your message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button className="jarvis-btn-primary" onClick={sendMessage} disabled={loading}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
