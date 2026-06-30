import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import { Navbar } from '@/components/layout/Navbar';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'RRB Exam Prep - NTPC & Group D 2026 Mock Tests',
  description: 'Free topic-wise practice and full-length mock tests for RRB NTPC and Group D 2026 exams. 500+ questions with detailed explanations.',
  keywords: 'RRB NTPC mock test, RRB Group D practice, railway exam preparation, NTPC 2026, Group D 2026, free mock tests',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Navbar />
        <main className="min-h-screen pt-16">
          {children}
        </main>
        <footer className="bg-gray-900 text-gray-400 py-8 mt-16">
          <div className="max-w-6xl mx-auto px-4 text-center text-sm">
            <p>RRB Exam Prep — Free mock tests for RRB NTPC & Group D 2026</p>
            <p className="mt-1">Not affiliated with Railway Recruitment Board. For educational practice only.</p>
          </div>
        </footer>
      </body>
    </html>
  );
}
