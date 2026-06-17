"use client";

import Link from "next/link";

export default function DashboardPage() {
  const cards = [
    { title: "Chat", description: "Talk to JARVIS", href: "/chat", icon: "💬", color: "bg-green-50 border-green-200" },
    { title: "Projects", description: "Manage your projects", href: "/projects", icon: "📁", color: "bg-blue-50 border-blue-200" },
    { title: "Agents", description: "View specialist agents", href: "/agents", icon: "🤖", color: "bg-purple-50 border-purple-200" },
    { title: "Memory", description: "Browse stored knowledge", href: "/memory", icon: "🧠", color: "bg-yellow-50 border-yellow-200" },
    { title: "Tools", description: "Available tool registry", href: "/tools", icon: "🔧", color: "bg-indigo-50 border-indigo-200" },
    { title: "Logs", description: "System activity log", href: "/logs", icon: "📋", color: "bg-gray-50 border-gray-200" },
  ];

  return (
    <div className="p-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-500 mt-1">Welcome to JARVIS OS Phase 1</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {cards.map((card) => (
          <Link
            key={card.href}
            href={card.href}
            className={`block p-6 rounded-lg border-2 ${card.color} hover:shadow-md transition-shadow`}
          >
            <div className="text-3xl mb-3">{card.icon}</div>
            <h2 className="text-lg font-semibold text-gray-900">{card.title}</h2>
            <p className="text-sm text-gray-600 mt-1">{card.description}</p>
          </Link>
        ))}
      </div>

      <div className="mt-12 p-6 rounded-lg bg-white border shadow-sm">
        <h2 className="text-lg font-semibold text-gray-900 mb-3">System Status</h2>
        <div className="space-y-2">
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 rounded-full bg-green-500"></div>
            <span className="text-sm text-gray-600">API Server — Checking...</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 rounded-full bg-gray-300"></div>
            <span className="text-sm text-gray-600">PostgreSQL — Not connected</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 rounded-full bg-gray-300"></div>
            <span className="text-sm text-gray-600">Redis — Not connected</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 rounded-full bg-gray-300"></div>
            <span className="text-sm text-gray-600">Qdrant — Not connected</span>
          </div>
        </div>
      </div>
    </div>
  );
}
