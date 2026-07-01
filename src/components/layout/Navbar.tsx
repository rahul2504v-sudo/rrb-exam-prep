'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useSession, signOut } from 'next-auth/react';
import { BookOpen, BarChart3, Home, LogIn, User, LogOut } from 'lucide-react';
import { LanguageSwitcher } from './LanguageSwitcher';
import { useLanguage } from '@/lib/LanguageContext';

export function Navbar() {
  const pathname = usePathname();
  const { t } = useLanguage();
  const { data: session } = useSession();

  const isActive = (path: string) => pathname.startsWith(path)
    ? 'text-indigo-600 font-semibold'
    : 'text-gray-600 hover:text-indigo-600';

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
        <div className="flex items-center gap-6">
          <Link href="/" className="flex items-center gap-2 font-bold text-lg text-gray-900">
            <BookOpen className="w-6 h-6 text-indigo-600" />
            <span className="hidden sm:inline">PrepxCore</span>
          </Link>
          <div className="hidden md:flex items-center gap-1">
            <Link href="/" className={`px-3 py-1.5 rounded-lg text-sm transition-colors ${isActive('/exam') || pathname === '/' ? 'text-indigo-600 bg-indigo-50 font-medium' : 'text-gray-600 hover:text-indigo-600'}`}>
              <Home className="w-4 h-4 inline mr-1" />{t('home')}
            </Link>
            <Link href="/exam/ntpc" className={`px-3 py-1.5 rounded-lg text-sm transition-colors ${isActive('/exam/ntpc') || isActive('/exam/group-d') ? 'text-indigo-600 bg-indigo-50 font-medium' : 'text-gray-600 hover:text-indigo-600'}`}>
              {t('exams')}
            </Link>
            <Link href="/results" className={`px-3 py-1.5 rounded-lg text-sm transition-colors ${isActive('/results') ? 'text-indigo-600 bg-indigo-50 font-medium' : 'text-gray-600 hover:text-indigo-600'}`}>
              <BarChart3 className="w-4 h-4 inline mr-1" />{t('results')}
            </Link>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <LanguageSwitcher />
          {session?.user ? (
            <div className="flex items-center gap-2">
              <span className="hidden sm:inline text-sm text-gray-600">{session.user.name}</span>
              <button
                onClick={() => signOut()}
                className="flex items-center gap-1 px-3 py-1.5 text-sm font-medium text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors"
              >
                <LogOut className="w-4 h-4" />
                <span className="hidden sm:inline">Sign Out</span>
              </button>
            </div>
          ) : (
            <Link
              href="/login"
              className="flex items-center gap-1 px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors shadow-sm"
            >
              <LogIn className="w-4 h-4" />
              <span className="hidden sm:inline">Sign In</span>
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
}
