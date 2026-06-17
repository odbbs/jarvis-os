"use client";

import { useState, useEffect } from "react";

type Agent = {
  name: string;
  description: string;
  status: string;
};

export default function AgentsPage() {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/agents")
      .then((r) => r.json())
      .then((data) => setAgents(data.agents))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  const defaultAgents: Agent[] = [
    { name: "Commander", description: "Central orchestrator", status: "active" },
    { name: "Coding Supervisor", description: "Oversees coding agents", status: "placeholder" },
    { name: "Project Agent", description: "Manages project tasks", status: "placeholder" },
    { name: "Research", description: "Web research", status: "placeholder" },
    { name: "Office", description: "Document creation", status: "placeholder" },
    { name: "Memory", description: "Knowledge management", status: "active" },
    { name: "Automation", description: "Workflow automation", status: "placeholder" },
  ];

  const displayAgents = agents.length > 0 ? agents : defaultAgents;

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Agents</h1>
      <div className="grid gap-4">
        {displayAgents.map((agent, i) => (
          <div key={i} className="jarvis-card flex items-center justify-between">
            <div>
              <h2 className="text-lg font-semibold text-gray-900">{agent.name}</h2>
              <p className="text-sm text-gray-600">{agent.description}</p>
            </div>
            <span className={`px-3 py-1 rounded-full text-xs font-medium ${
              agent.status === "active" ? "bg-green-100 text-green-700" : "bg-yellow-100 text-yellow-700"
            }`}>
              {agent.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
