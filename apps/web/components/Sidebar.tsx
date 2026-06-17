"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const navItems = [
  { href: "/dashboard", label: "Dashboard", icon: "📊" },
  { href: "/chat", label: "Chat", icon: "💬" },
  { href: "/projects", label: "Projects", icon: "📁" },
  { href: "/agents", label: "Agents", icon: "🤖" },
  { href: "/memory", label: "Memory", icon: "🧠" },
  { href: "/tools", label: "Tools", icon: "🔧" },
  { href: "/settings", label: "Settings", icon: "⚙️" },
  { href: "/logs", label: "Logs", icon: "📋" },
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="fixed left-0 top-0 h-full w-64 jarvis-gradient text-white flex flex-col z-50">
      <div className="p-6 border-b border-white/10">
        <Link href="/dashboard" className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-lg bg-[#8DC63F] flex items-center justify-center text-xl font-bold">
            J
          </div>
          <div>
            <h1 className="text-lg font-bold">JARVIS OS</h1>
            <p className="text-xs text-gray-400">Phase 1</p>
          </div>
        </Link>
      </div>

      <nav className="flex-1 p-4 space-y-1">
        {navItems.map((item) => {
          const isActive = pathname === item.href;
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                isActive
                  ? "bg-white/10 text-white font-medium"
                  : "text-gray-300 hover:bg-white/5 hover:text-white"
              }`}
            >
              <span className="text-lg">{item.icon}</span>
              <span>{item.label}</span>
            </Link>
          );
        })}
      </nav>

      <div className="p-4 border-t border-white/10">
        <div className="text-xs text-gray-400">
          <p>JARVIS OS v0.1.0</p>
          <p>Mode: Development</p>
        </div>
      </div>
    </aside>
  );
}
