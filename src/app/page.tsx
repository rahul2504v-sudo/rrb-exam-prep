'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { examList } from '@/data/exams';
import { Clock, ChevronDown, Megaphone, Calendar, ExternalLink, ArrowRight } from 'lucide-react';

export default function HomePage() {
  const [openExam, setOpenExam] = useState<string | null>(null);
  const [bulletin, setBulletin] = useState<any[]>([]);

  useEffect(() => {
    fetch('/data/bulletin.json').then(r => r.json()).then(setBulletin).catch(() => {});
  }, []);

  const displayBulletin = bulletin.length > 0 ? bulletin : [
    { name: 'RRB ALP CBT 2', date: 'July 28, 2026', vacancies: '11,127', status: 'Ongoing' },
    { name: 'RRB NTPC CBT 2 (UG)', date: 'September 17, 2026', vacancies: '3,058', status: 'Upcoming' },
    { name: 'RRB Technician 2026-27', date: 'Notification Out', vacancies: '6,557', status: 'Notified' },
    { name: 'SSC CGL Tier 2', date: 'October 2026', vacancies: '~8,000', status: 'Upcoming' },
    { name: 'RRB Group D (New)', date: 'Notification Expected', vacancies: '22,082', status: 'Expected' },
  ];

  return (
    <div>
      {/* Hero */}
      <section className="relative overflow-hidden bg-gradient-to-br from-indigo-600 via-indigo-700 to-purple-800 text-white">
        <div className="max-w-6xl mx-auto px-4 py-20 text-center relative z-10">
          <h1 className="text-4xl sm:text-5xl font-extrabold tracking-tight mb-4">
            <span className="text-white">prepXcore</span>
          </h1>
          <p className="text-xl sm:text-2xl text-indigo-100 font-light mb-3">
            India's Smartest Exam Preparation Platform
          </p>
          <p className="text-indigo-200/80 max-w-xl mx-auto">
            10,000+ questions, full-length mocks, detailed analytics. Practice for RRB NTPC, ALP, Technician, Group D & more.
          </p>
          <div className="flex flex-wrap justify-center gap-3 mt-8">
            <Link href="#exams" className="px-6 py-3 bg-white text-indigo-700 font-semibold rounded-xl hover:bg-indigo-50 transition-all shadow-lg hover:shadow-xl">
              Start Practicing →
            </Link>
          </div>
        </div>
      </section>

      {/* Available Exams */}
      <section id="exams" className="max-w-6xl mx-auto px-4 py-16">
        <div className="grid lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <h2 className="text-3xl font-bold text-gray-900 mb-6">Available Exams</h2>
            
            <div className="space-y-4">
              {examList.map(exam => (
                <div key={exam.id} className="border border-gray-200 rounded-2xl overflow-hidden hover:border-indigo-300 transition-all">
                  <button onClick={() => setOpenExam(openExam === exam.id ? null : exam.id)}
                    className="w-full flex items-center justify-between p-5 hover:bg-gray-50 transition-colors">
                    <div className="flex items-center gap-4">
                      <div className={`w-12 h-12 rounded-xl flex items-center justify-center text-xl ${exam.id === 'ntpc' ? 'bg-blue-100' : 'bg-green-100'}`}>
                        {exam.id === 'ntpc' || exam.id === 'alp' ? '🚂' : '🔧'}
                      </div>
                      <div className="text-left">
                        <h3 className="font-bold text-lg text-gray-900">
                          {exam.name}
                          {exam.status && (
                            <span className={`ml-2 text-[10px] px-2 py-0.5 rounded-full font-medium ${
                              exam.status === 'ongoing' ? 'bg-green-100 text-green-700' :
                              exam.status === 'upcoming' ? 'bg-amber-100 text-amber-700' :
                              exam.status === 'notified' ? 'bg-blue-100 text-blue-700' : 'bg-gray-100 text-gray-600'
                            }`}>
                              {exam.status === 'ongoing' ? 'Active' : exam.status === 'notified' ? 'New' : 'Upcoming'}
                            </span>
                          )}
                        </h3>
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
                      <div className="grid sm:grid-cols-4 gap-4 mb-4">
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
                          Topic-wise Practice <ArrowRight className="w-3.5 h-3.5 inline ml-1" />
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

          {/* Bulletin Side Panel */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-2xl shadow-lg border border-gray-200 p-5 sticky top-24">
              <div className="flex items-center gap-2 mb-4">
                <Megaphone className="w-5 h-5 text-amber-600" />
                <h2 className="text-lg font-bold text-gray-900">Exam Bulletin</h2>
              </div>
              <div className="space-y-3">
                {displayBulletin.map((item: any, i: number) => (
                  <a key={i} href={item.url || '#'} target={item.url ? '_blank' : undefined} rel="noopener"
                    className="flex items-start gap-3 p-3 rounded-xl border border-gray-100 hover:border-amber-200 hover:bg-amber-50/50 transition-all group">
                    <div className={`w-2 h-2 rounded-full mt-1.5 flex-shrink-0 ${
                      item.status === 'Ongoing' ? 'bg-green-500' : item.status === 'Upcoming' ? 'bg-amber-500' : 'bg-blue-500'
                    }`} />
                    <div className="min-w-0 flex-1">
                      <p className="text-sm font-medium text-gray-800 truncate">{item.name}</p>
                      <div className="flex items-center gap-2 mt-1">
                        <span className="text-xs text-gray-400 flex items-center gap-1"><Calendar className="w-3 h-3" />{item.date}</span>
                        {item.vacancies && <span className="text-xs text-gray-400">{item.vacancies} posts</span>}
                      </div>
                    </div>
                  </a>
                ))}
              </div>
              <p className="text-[10px] text-gray-400 mt-3 text-center">Auto-updated daily from official sources</p>
            </div>
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="bg-indigo-600 text-white py-12">
        <div className="max-w-5xl mx-auto px-4 grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
          {[['10,000+', 'Questions'], ['1,400+', 'Topic Sets'], ['80', 'Mock Papers'], ['15', 'Languages']].map(([val, label], i) => (
            <div key={i}>
              <div className="text-2xl font-bold">{val}</div>
              <div className="text-indigo-200 text-sm">{label}</div>
            </div>
          ))}
        </div>
      </section>

      <footer className="bg-gray-900 text-gray-400 text-xs text-center py-8">
        <div className="max-w-6xl mx-auto px-4">
          <span className="font-bold text-white">prepXcore</span> — Competitive Exam Preparation Platform
          <div className="mt-2">© 2026 prepXcore. All rights reserved.</div>
        </div>
      </footer>
    </div>
  );
}
