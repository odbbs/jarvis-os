"use client";

import { useState, useEffect } from "react";

type Project = {
  id: string;
  name: string;
  description: string;
  status: string;
};

export default function ProjectsPage() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/projects")
      .then((r) => r.json())
      .then((data) => setProjects(data.projects))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Projects</h1>
      <div className="grid gap-4">
        {loading ? (
          <p className="text-gray-400">Loading...</p>
        ) : projects.length === 0 ? (
          <p className="text-gray-400">Backend not connected. Showing Phase 1 defaults.</p>
        ) : null}

        {/* Always show known projects */}
        {[
          { id: "auto", name: "Auto", description: "Automatic project detection", status: "active" },
          { id: "aligna", name: "Aligna", description: "Career Readiness Assessment Platform", status: "placeholder" },
          { id: "raf4", name: "RAF4", description: "RAF4 Project", status: "placeholder" },
          { id: "oddb", name: "ODDB", description: "ODDB Project", status: "placeholder" },
        ].map((project) => (
          <div key={project.id} className="jarvis-card flex items-center justify-between">
            <div>
              <h2 className="text-lg font-semibold text-gray-900">{project.name}</h2>
              <p className="text-sm text-gray-600">{project.description}</p>
            </div>
            <span className={`px-3 py-1 rounded-full text-xs font-medium ${
              project.status === "active" ? "bg-green-100 text-green-700" : "bg-yellow-100 text-yellow-700"
            }`}>
              {project.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
