import type { Metadata, Viewport } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import { Navbar } from '@/components/layout/Navbar';
import { LanguageProvider } from '@/lib/LanguageContext';
import { PWAProvider } from '@/components/layout/PWAProvider';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'RRB Exam Prep - NTPC & Group D Mock Tests',
  description: 'Free topic-wise practice and full-length mock tests for RRB NTPC and Group D exams. 10,000+ bilingual questions with detailed explanations.',
  keywords: 'RRB NTPC mock test, RRB Group D practice, railway exam preparation, NTPC 2026, Group D 2026, free mock tests',
  manifest: '/manifest.json',
  appleWebApp: {
    capable: true,
    statusBarStyle: 'black-translucent',
    title: 'RRB Exam Prep',
  },
  other: {
    'mobile-web-app-capable': 'yes',
  },
};

export const viewport: Viewport = {
  themeColor: '#1a237e',
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="apple-touch-icon" href="/icons/icon-192.svg" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
      </head>
      <body className={inter.className}>
        <LanguageProvider>
          <PWAProvider />
          <Navbar />
          <main className="min-h-screen pt-16">
            {children}
          </main>
          <footer className="bg-gray-900 text-gray-400 py-8 mt-16">
            <div className="max-w-6xl mx-auto px-4 text-center text-sm">
              <p>RRB Exam Prep — Free mock tests for RRB NTPC & Group D</p>
              <p className="mt-1">Not affiliated with Railway Recruitment Board. For educational practice only.</p>
            </div>
          </footer>
        </LanguageProvider>
      </body>
    </html>
  );
}
