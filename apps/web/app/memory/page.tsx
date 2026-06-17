"use client";

import { useState } from "react";

export default function MemoryPage() {
  const [namespace, setNamespace] = useState("personal");
  const [content, setContent] = useState("");
  const [search, setSearch] = useState("");
  const [results, setResults] = useState<any[]>([]);
  const [message, setMessage] = useState("");

  const saveMemory = async () => {
    if (!content.trim()) return;
    try {
      const res = await fetch("http://localhost:8000/memory/save", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ type: "note", namespace, content }),
      });
      const data = await res.json();
      setMessage(`✅ Saved: ${data.saved?.id || "ok"}`);
      setContent("");
    } catch {
      setMessage("⚠️ Backend not connected. Memory saved locally in Phase 1.");
    }
  };

  const searchMemory = async () => {
    try {
      const params = new URLSearchParams({ q: search, namespace, limit: "10" });
      const res = await fetch(`http://localhost:8000/memory/search?${params}`);
      const data = await res.json();
      setResults(data.results);
    } catch {
      setMessage("⚠️ Backend not connected. Search unavailable.");
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Memory</h1>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Save */}
        <div className="jarvis-card">
          <h2 className="text-lg font-semibold mb-4">Save Memory</h2>
          <div className="space-y-3">
            <select className="jarvis-select" value={namespace} onChange={(e) => setNamespace(e.target.value)}>
              <option value="personal">Personal</option>
              <option value="system">System</option>
              <option value="project:aligna">Project: Aligna</option>
              <option value="project:raf4">Project: RAF4</option>
              <option value="project:oddb">Project: ODDB</option>
              <option value="documents">Documents</option>
              <option value="tasks">Tasks</option>
            </select>
            <textarea
              className="jarvis-input h-32 resize-none"
              placeholder="What would you like to remember?"
              value={content}
              onChange={(e) => setContent(e.target.value)}
            />
            <button className="jarvis-btn-primary" onClick={saveMemory}>
              Save
            </button>
          </div>
        </div>

        {/* Search */}
        <div className="jarvis-card">
          <h2 className="text-lg font-semibold mb-4">Search Memory</h2>
          <div className="space-y-3">
            <input
              className="jarvis-input"
              placeholder="Search query..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
            <button className="jarvis-btn-primary" onClick={searchMemory}>
              Search
            </button>
          </div>

          {results.length > 0 && (
            <div className="mt-4 space-y-2">
              {results.map((r, i) => (
                <div key={i} className="p-3 bg-gray-50 rounded text-sm">
                  <div className="text-xs text-gray-400 mb-1">{r.namespace} · {r.created_at}</div>
                  <div>{r.content}</div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {message && (
        <div className="mt-4 p-3 bg-blue-50 border border-blue-200 rounded text-sm text-blue-700">
          {message}
        </div>
      )}
    </div>
  );
}
