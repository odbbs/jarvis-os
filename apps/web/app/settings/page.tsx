"use client";

export default function SettingsPage() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Settings</h1>
      <div className="jarvis-card space-y-6">
        <div>
          <h2 className="text-lg font-semibold mb-2">Default Model</h2>
          <select className="jarvis-select max-w-xs" defaultValue="gpt">
            <option value="gpt">GPT</option>
            <option value="claude">Claude Code</option>
            <option value="deepseek">DeepSeek</option>
            <option value="moonshot">Moonshot</option>
          </select>
          <p className="text-xs text-gray-400 mt-1">Configured in .env as JARVIS_DEFAULT_MODEL</p>
        </div>

        <div>
          <h2 className="text-lg font-semibold mb-2">API Keys</h2>
          <div className="space-y-2 text-sm text-gray-600">
            <p>🔑 OpenAI: <span className="text-gray-400">Configured in .env</span></p>
            <p>🔑 DeepSeek: <span className="text-gray-400">Configured in .env</span></p>
            <p>🔑 Moonshot: <span className="text-gray-400">Configured in .env</span></p>
            <p>🔑 Anthropic: <span className="text-gray-400">Configured in .env</span></p>
          </div>
        </div>

        <div>
          <h2 className="text-lg font-semibold mb-2">Workspace</h2>
          <p className="text-sm text-gray-600">Root: <code className="bg-gray-100 px-2 py-0.5 rounded">C:\JARVIS</code></p>
        </div>

        <div>
          <h2 className="text-lg font-semibold mb-2">About</h2>
          <div className="text-sm text-gray-600 space-y-1">
            <p>JARVIS OS v0.1.0 — Phase 1</p>
            <p>FastAPI + Next.js + PostgreSQL + Redis + Qdrant</p>
            <p>Running in development mode</p>
          </div>
        </div>
      </div>
    </div>
  );
}
