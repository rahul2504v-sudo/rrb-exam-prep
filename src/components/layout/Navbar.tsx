'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Train, BarChart3, Home } from 'lucide-react';

export function Navbar() {
  const pathname = usePathname();

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-white border-b border-gray-200 shadow-sm">
      <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2 font-bold text-xl text-rail-navy">
          <Train className="w-6 h-6" />
          <span className="hidden sm:inline">RRB Exam Prep</span>
        </Link>
        
        <div className="flex items-center gap-1">
          <Link
            href="/"
            className={`flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors
              ${pathname === '/' ? 'bg-blue-50 text-rail-navy' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'}`}
          >
            <Home className="w-4 h-4" />
            <span className="hidden sm:inline">Home</span>
          </Link>
          <Link
            href="/exam/ntpc"
            className={`flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors
              ${pathname.startsWith('/exam') ? 'bg-blue-50 text-rail-navy' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'}`}
          >
            <Train className="w-4 h-4" />
            <span className="hidden sm:inline">NTPC</span>
          </Link>
          <Link
            href="/exam/group-d"
            className={`flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors
              ${pathname.startsWith('/exam/group-d') ? 'bg-red-50 text-rail-red' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'}`}
          >
            <span className="text-sm font-bold">GD</span>
            <span className="hidden sm:inline">Group D</span>
          </Link>
          <Link
            href="/results"
            className={`flex items-center gap-1.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors
              ${pathname.startsWith('/results') ? 'bg-blue-50 text-rail-navy' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'}`}
          >
            <BarChart3 className="w-4 h-4" />
            <span className="hidden sm:inline">Results</span>
          </Link>
        </div>
      </div>
    </nav>
  );
}
