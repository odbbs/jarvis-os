"use client";

import { useState, useEffect } from "react";

type Tool = {
  name: string;
  description: string;
  risk_level: string;
  requires_approval: boolean;
};

export default function ToolsPage() {
  const [tools, setTools] = useState<Tool[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/tools")
      .then((r) => r.json())
      .then((data) => setTools(data.tools))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  const defaultTools: Tool[] = [
    { name: "filesystem.read", description: "Read a file", risk_level: "SAFE", requires_approval: false },
    { name: "filesystem.write", description: "Write to a file", risk_level: "APPROVAL_REQUIRED", requires_approval: true },
    { name: "filesystem.search", description: "Search files", risk_level: "SAFE", requires_approval: false },
    { name: "git.status", description: "Check git status", risk_level: "SAFE", requires_approval: false },
    { name: "terminal.run", description: "Run terminal command", risk_level: "APPROVAL_REQUIRED", requires_approval: true },
    { name: "memory.search", description: "Search memory", risk_level: "SAFE", requires_approval: false },
    { name: "memory.save", description: "Save to memory", risk_level: "SAFE", requires_approval: false },
  ];

  const displayTools = tools.length > 0 ? tools : defaultTools;

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Tools</h1>
      <div className="grid gap-4">
        {displayTools.map((tool, i) => (
          <div key={i} className="jarvis-card flex items-center justify-between">
            <div>
              <h2 className="text-lg font-semibold text-gray-900">{tool.name}</h2>
              <p className="text-sm text-gray-600">{tool.description}</p>
            </div>
            <span className={`px-3 py-1 rounded-full text-xs font-medium ${
              tool.risk_level === "SAFE" ? "bg-green-100 text-green-700" :
              tool.risk_level === "APPROVAL_REQUIRED" ? "bg-yellow-100 text-yellow-700" :
              "bg-red-100 text-red-700"
            }`}>
              {tool.risk_level === "SAFE" ? "Safe" : "Approval Required"}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
