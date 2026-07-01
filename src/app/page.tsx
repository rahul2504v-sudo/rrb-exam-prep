'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { examList } from '@/data/exams';
import { BookOpen, Clock, Layers, TrendingUp, Award, Zap, ArrowRight, ChevronDown, Bell, Calendar, CheckCircle, Globe, BarChart3, Target, ExternalLink, Megaphone } from 'lucide-react';

interface BulletinItem {
  name: string;
  date: string;
  vacancies: string;
  status: string;
  url?: string;
}

export default function HomePage() {
  const [openExam, setOpenExam] = useState<string | null>(null);
  const [bulletin, setBulletin] = useState<BulletinItem[]>([]);

  useEffect(() => {
    fetch('/data/bulletin.json')
      .then(r => r.json())
      .then(data => setBulletin(data.slice(0, 6)))
      .catch(() => setBulletin([]));
  }, []);

  const fallbackBulletin: BulletinItem[] = [
    { name: 'RRB Group D Level 1 CBT', date: 'August 2026', vacancies: '22,195', status: 'Upcoming', url: 'https://www.rrbcdg.gov.in/' },
    { name: 'RRB NTPC CBT 2 (Graduate)', date: 'July 2026', vacancies: '5,810', status: 'Ongoing', url: 'https://www.rrbcdg.gov.in/' },
    { name: 'RRB NTPC CBT 2 (UG Level)', date: 'September 2026', vacancies: '3,058', status: 'Upcoming', url: 'https://www.rrbcdg.gov.in/' },
    { name: 'SSC CGL Tier 2 2026', date: 'October 2026', vacancies: '~8,000', status: 'Upcoming', url: 'https://ssc.nic.in/' },
    { name: 'IBPS PO 2026 Prelims', date: 'October 2026', vacancies: '~5,000', status: 'Expected', url: 'https://www.ibps.in/' },
  ];

  const displayBulletin = bulletin.length > 0 ? bulletin : fallbackBulletin;

  return (
    <div className="bg-white">
      {/* Hero */}
      <section className="relative bg-gradient-to-br from-indigo-600 via-indigo-700 to-purple-800 text-white overflow-hidden">
        <div className="absolute inset-0 opacity-20">
          <div className="absolute top-10 left-10 w-72 h-72 bg-white rounded-full blur-3xl" />
          <div className="absolute bottom-10 right-10 w-96 h-96 bg-purple-400 rounded-full blur-3xl" />
        </div>
        <div className="max-w-6xl mx-auto px-4 py-16 md:py-20 relative z-10 text-center">
          <div className="inline-flex items-center gap-2 bg-white/10 rounded-full px-4 py-2 text-sm mb-6 border border-white/10">
            <Zap className="w-4 h-4" />
            10,000+ Questions · 1,300+ Sets · 40 Mock Papers
          </div>
          <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight mb-4">
            prep<span className="text-yellow-300">X</span>core
          </h1>
          <p className="text-xl md:text-2xl text-indigo-200 mb-3 font-light">
            Your Complete Exam Preparation Platform
          </p>
          <p className="text-indigo-200/80 max-w-xl mx-auto">
            Free mock tests, topic-wise practice, and detailed analytics for competitive exams.
          </p>
          <div className="flex flex-wrap justify-center gap-3 mt-8">
            <Link href="/exam/ntpc" className="px-6 py-3 bg-white text-indigo-700 font-semibold rounded-xl hover:bg-indigo-50 transition-all shadow-lg hover:shadow-xl">
              Start Practicing →
            </Link>
            <Link href="#exams" className="px-6 py-3 bg-white/10 text-white font-semibold rounded-xl hover:bg-white/20 transition-all border border-white/20">
              Explore Exams
            </Link>
          </div>
        </div>
      </section>

      {/* Available Exams + Bulletin side by side */}
      <section id="exams" className="max-w-6xl mx-auto px-4 py-16">
        <div className="grid lg:grid-cols-3 gap-8">
          {/* Left: Available Exams */}
          <div className="lg:col-span-2">
            <h2 className="text-3xl font-bold text-gray-900 mb-2">Available Exams</h2>
            <p className="text-gray-500 mb-6">Select an exam to practice topic-wise sets or take full-length mock tests</p>
            
            <div className="space-y-4">
              {examList.map(exam => (
                <div key={exam.id} className="border border-gray-200 rounded-2xl overflow-hidden hover:border-indigo-300 transition-all">
                  <button
                    onClick={() => setOpenExam(openExam === exam.id ? null : exam.id)}
                    className="w-full flex items-center justify-between p-5 hover:bg-gray-50 transition-colors"
                  >
                    <div className="flex items-center gap-4">
                      <div className={`w-12 h-12 rounded-xl flex items-center justify-center text-xl ${exam.id === 'ntpc' ? 'bg-blue-100' : 'bg-green-100'}`}>
                        {exam.id === 'ntpc' ? '🚂' : '🔧'}
                      </div>
                      <div className="text-left">
                        <h3 className="font-bold text-lg text-gray-900">{exam.name}</h3>
                        <p className="text-sm text-gray-500">{exam.description}</p>
                      </div>
                    </div>
                    <div className="flex items-center gap-3">
                      <span className="hidden sm:inline text-xs bg-blue-50 text-blue-700 px-2 py-1 rounded-full">{exam.totalVacancies.toLocaleString()} Posts</span>
                      <span className="hidden sm:inline text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full">{exam.pattern.totalQuestions} Qs</span>
                      <ChevronDown className={`w-5 h-5 text-gray-400 transition-transform ${openExam === exam.id ? 'rotate-180' : ''}`} />
                    </div>
                  </button>
                  
                  {openExam === exam.id && (
                    <div className="border-t border-gray-100 p-5 bg-gray-50/50">
                      <div className="grid sm:grid-cols-3 gap-4 mb-4">
                        {exam.pattern.sections.map((sec, i) => (
                          <div key={i} className="bg-white rounded-xl p-3 border border-gray-100 text-center">
                            <div className="text-lg font-bold text-indigo-600">{sec.questionCount}</div>
                            <div className="text-xs text-gray-500">{sec.name}</div>
                          </div>
                        ))}
                      </div>
                      <div className="text-sm text-gray-500 mb-3">
                        <Clock className="w-4 h-4 inline mr-1" />{exam.pattern.durationMinutes} min · -1/3 negative marking
                      </div>
                      <div className="flex gap-3">
                        <Link href={`/exam/${exam.slug}`} className="px-4 py-2 bg-indigo-600 text-white rounded-lg text-sm font-medium hover:bg-indigo-700">
                          Topic-wise Practice
                        </Link>
                        <Link href={`/quiz/${exam.slug}/mock/0`} className="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-100">
                          Full Mock Test
                        </Link>
                      </div>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>

          {/* Right: Exam Bulletin Side Panel */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-2xl shadow-lg border border-gray-200 p-5 sticky top-24">
              <div className="flex items-center gap-2 mb-4">
                <Megaphone className="w-5 h-5 text-amber-600" />
                <h2 className="text-lg font-bold text-gray-900">Exam Bulletin</h2>
              </div>
              <div className="space-y-3">
                {displayBulletin.map((item, i) => (
                  <a key={i}
                    href={item.url || '#'}
                    target={item.url ? '_blank' : undefined}
                    rel="noopener"
                    className="flex items-start gap-3 p-3 rounded-xl border border-gray-100 hover:border-amber-200 hover:bg-amber-50/50 transition-all group"
                  >
                    <div className={`w-2 h-2 rounded-full mt-1.5 flex-shrink-0 ${
                      item.status === 'Ongoing' ? 'bg-green-500' :
                      item.status === 'Upcoming' ? 'bg-amber-500' :
                      'bg-blue-500'
                    }`} />
                    <div className="min-w-0 flex-1">
                      <p className="text-sm font-medium text-gray-800 group-hover:text-indigo-700 transition-colors truncate">
                        {item.name}
                      </p>
                      <div className="flex items-center gap-2 mt-1">
                        <span className="text-xs text-gray-400 flex items-center gap-1">
                          <Calendar className="w-3 h-3" />{item.date}
                        </span>
                        {item.vacancies && (
                          <span className="text-xs text-gray-400">{item.vacancies} posts</span>
                        )}
                      </div>
                    </div>
                    {item.url && <ExternalLink className="w-3 h-3 text-gray-300 group-hover:text-indigo-500 flex-shrink-0 mt-1 opacity-0 group-hover:opacity-100 transition-opacity" />}
                  </a>
                ))}
              </div>
              <p className="text-[10px] text-gray-400 mt-3 text-center">Auto-updated daily from official sources</p>
            </div>
          </div>
        </div>
      </section>

      {/* Platform Features */}
      <section className="bg-gray-50 py-16">
        <div className="max-w-6xl mx-auto px-4">
          <h2 className="text-3xl font-bold text-gray-900 text-center mb-2">Why prepXcore?</h2>
          <p className="text-gray-500 text-center mb-12">Everything you need for complete exam preparation — free</p>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              { icon: BookOpen, title: '10,000+ Questions', desc: 'Every topic from RRB syllabus with bilingual English-Hindi support and explanations.' },
              { icon: Layers, title: '1,300+ Practice Sets', desc: 'Topic-wise 10-question sets. Complete and track your progress.' },
              { icon: BarChart3, title: 'Performance Analytics', desc: 'Breakdown by topic, difficulty, time. Identify weak areas.' },
              { icon: Globe, title: '15 Languages', desc: 'All RRB exam languages: Hindi, Tamil, Telugu, Bengali & more.' },
              { icon: Target, title: 'Real Exam Pattern', desc: 'Matches actual exam format — sections, timing, negative marking.' },
              { icon: CheckCircle, title: 'Instant Scoring', desc: 'Results with correct answers and explanations for every question.' },
              { icon: TrendingUp, title: 'Track Progress', desc: 'Monitor improvement across sessions with score trends.' },
            ].map((f, i) => (
              <div key={i} className="bg-white rounded-xl p-6 text-center border border-gray-100 hover:shadow-lg transition-shadow">
                <f.icon className="w-10 h-10 text-indigo-600 mx-auto mb-3" />
                <h3 className="font-bold text-gray-900 mb-1">{f.title}</h3>
                <p className="text-sm text-gray-500">{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="bg-gray-900 text-white py-12">
        <div className="max-w-6xl mx-auto px-4">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            {[
              { value: '10,000+', label: 'Questions' },
              { value: '1,300+', label: 'Practice Sets' },
              { value: '40', label: 'Mock Papers' },
              { value: '15', label: 'Languages' },
            ].map((s, i) => (
              <div key={i}>
                <div className="text-3xl font-bold text-indigo-400">{s.value}</div>
                <div className="text-sm text-gray-400 mt-1">{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-gray-200 py-8">
        <div className="max-w-6xl mx-auto px-4 text-center text-sm text-gray-400">
          <p className="font-semibold text-gray-500 mb-1">prepXcore</p>
          <p>Free exam preparation platform for competitive exams in India.</p>
        </div>
      </footer>
    </div>
  );
}
