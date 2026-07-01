import type { Metadata, Viewport } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import { Navbar } from '@/components/layout/Navbar';
import { LanguageProvider } from '@/lib/LanguageContext';
import { PWAProvider } from '@/components/layout/PWAProvider';
import { SessionProvider } from '@/components/layout/SessionProvider';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'PrepxCore — Free Exam Mock Tests & Practice',
  description: 'Free topic-wise practice and full-length mock tests for competitive exams. RRB NTPC, Group D, and more. 10,000+ bilingual questions with detailed explanations.',
  manifest: '/manifest.json',
  icons: { icon: '/favicon.svg', apple: '/icon-192.svg' },
  appleWebApp: { capable: true, title: 'PrepxCore', statusBarStyle: 'default' },
};

export const viewport: Viewport = {
  themeColor: '#4f46e5',
  width: 'device-width',
  initialScale: 1,
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <link rel="apple-touch-icon" href="/icon-192.svg" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
      </head>
      <body className={`${inter.className} bg-gray-50 text-gray-900 antialiased`}>
        <SessionProvider>
          <LanguageProvider>
            <PWAProvider />
            <Navbar />
            <main className="min-h-screen pt-16">{children}</main>
          </LanguageProvider>
        </SessionProvider>
      </body>
    </html>
  );
}
