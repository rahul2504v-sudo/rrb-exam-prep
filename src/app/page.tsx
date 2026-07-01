'use client';

import Link from 'next/link';
import { examList } from '@/data/exams';
import { BookOpen, Clock, Target, Layers, TrendingUp, Award, Zap, ArrowRight } from 'lucide-react';

export default function HomePage() {
  return (
    <div className="bg-white">
      {/* Hero */}
      <section className="relative bg-gradient-to-br from-indigo-600 via-indigo-700 to-purple-800 text-white overflow-hidden">
        <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmZmZmYiIGZpbGwtb3BhY2l0eT0iMC4wNSI+PGNpcmNsZSBjeD0iMzAiIGN5PSIzMCIgcj0iMiIvPjwvZz48L2c+PC9zdmc+')] opacity-30" />
        <div className="max-w-6xl mx-auto px-4 py-20 relative z-10">
          <div className="text-center max-w-3xl mx-auto">
            <div className="inline-flex items-center gap-2 bg-white/10 rounded-full px-4 py-2 text-sm mb-6">
              <Zap className="w-4 h-4" />
              10,000+ Questions · 1,300+ Practice Sets · 40 Mock Papers
            </div>
            <h1 className="text-5xl md:text-6xl font-extrabold tracking-tight mb-4">
              PrepxCore
            </h1>
            <p className="text-xl text-indigo-200 mb-3">
              Your Complete Exam Preparation Platform
            </p>
            <p className="text-indigo-200/80 max-w-xl mx-auto">
              Master RRB NTPC, Group D, and upcoming exams with bilingual mock tests, 
              topic-wise practice sets, and detailed performance tracking — all free.
            </p>
            <div className="flex flex-wrap justify-center gap-3 mt-8">
              <Link href="/exam/ntpc" className="px-6 py-3 bg-white text-indigo-700 font-semibold rounded-xl hover:bg-indigo-50 transition-colors shadow-lg">
                Start Practicing →
              </Link>
              <Link href="/login" className="px-6 py-3 bg-white/10 text-white font-semibold rounded-xl hover:bg-white/20 transition-colors border border-white/20">
                Sign In to Track Progress
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Exam Categories */}
      <section className="max-w-6xl mx-auto px-4 py-16">
        <h2 className="text-2xl font-bold text-gray-900 mb-2">Available Exams</h2>
        <p className="text-gray-500 mb-8">Pick an exam to start practicing with topic-wise sets and full mock tests</p>
        
        <div className="grid md:grid-cols-2 gap-6">
          {examList.map(exam => (
            <Link key={exam.id} href={`/exam/${exam.slug}`}
              className="group card hover:shadow-xl transition-all duration-300 border-2 border-transparent hover:border-indigo-200">
              <div className="flex items-start gap-4">
                <div className={`w-14 h-14 rounded-2xl flex items-center justify-center text-2xl ${exam.id === 'ntpc' ? 'bg-blue-100 text-blue-700' : 'bg-green-100 text-green-700'}`}>
                  {exam.id === 'ntpc' ? '🚂' : '🔧'}
                </div>
                <div className="flex-1">
                  <h3 className="text-lg font-bold text-gray-900 group-hover:text-indigo-700 transition-colors">{exam.name}</h3>
                  <p className="text-sm text-gray-500 mt-1">{exam.description}</p>
                  <div className="flex flex-wrap gap-2 mt-3">
                    <span className="text-xs bg-blue-50 text-blue-700 px-2 py-1 rounded-full">
                      <Target className="w-3 h-3 inline mr-1" />{exam.totalVacancies.toLocaleString()} Vacancies
                    </span>
                    <span className="text-xs bg-green-50 text-green-700 px-2 py-1 rounded-full">
                      <BookOpen className="w-3 h-3 inline mr-1" />{exam.pattern.totalQuestions} Questions
                    </span>
                    <span className="text-xs bg-orange-50 text-orange-700 px-2 py-1 rounded-full">
                      <Clock className="w-3 h-3 inline mr-1" />{exam.pattern.durationMinutes} Mins
                    </span>
                  </div>
                </div>
                <ArrowRight className="w-5 h-5 text-gray-300 group-hover:text-indigo-600 transition-colors flex-shrink-0 mt-1" />
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Mock Tests — Prominent */}
      <section className="bg-gradient-to-r from-indigo-50 to-purple-50 py-16">
        <div className="max-w-6xl mx-auto px-4">
          <div className="flex items-center gap-3 mb-2">
            <Layers className="w-6 h-6 text-indigo-600" />
            <h2 className="text-2xl font-bold text-gray-900">Full-Length Mock Tests</h2>
          </div>
          <p className="text-gray-500 mb-8">20 complete papers per exam, matching the real pattern. Timed, scored, with detailed explanations.</p>
          
          <div className="grid md:grid-cols-2 gap-6">
            {examList.map(exam => (
              <div key={exam.id} className="bg-white rounded-2xl p-6 shadow-sm border border-gray-100">
                <div className="flex items-center justify-between mb-4">
                  <h3 className="font-bold text-lg text-gray-900">{exam.name}</h3>
                  <span className="text-sm text-indigo-600 font-medium">{exam.pattern.totalQuestions} Qs · {exam.pattern.durationMinutes} min · -1/3 marking</span>
                </div>
                <div className="grid grid-cols-5 gap-2 mb-4">
                  {Array.from({ length: 10 }, (_, i) => (
                    <Link key={i} href={`/quiz/${exam.slug}/mock/${i}`}
                      className="flex flex-col items-center p-2 rounded-lg border border-gray-200 hover:border-indigo-300 hover:bg-indigo-50 transition-all">
                      <span className="text-sm font-bold text-indigo-600">#{i + 1}</span>
                      <span className="text-[10px] text-gray-400">100Q</span>
                    </Link>
                  ))}
                </div>
                <div className="grid grid-cols-5 gap-2">
                  {Array.from({ length: 10 }, (_, i) => (
                    <Link key={i + 10} href={`/quiz/${exam.slug}/mock/${i + 10}`}
                      className="flex flex-col items-center p-2 rounded-lg border border-gray-200 hover:border-indigo-300 hover:bg-indigo-50 transition-all">
                      <span className="text-sm font-bold text-indigo-600">#{i + 11}</span>
                      <span className="text-[10px] text-gray-400">100Q</span>
                    </Link>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="max-w-6xl mx-auto px-4 py-16">
        <h2 className="text-2xl font-bold text-gray-900 text-center mb-2">Why PrepxCore?</h2>
        <p className="text-gray-500 text-center mb-10">Built for serious exam preparation</p>
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            { icon: BookOpen, title: '10,000+ Questions', desc: 'Covers every topic from RRB NTPC & Group D syllabus with bilingual support.' },
            { icon: Layers, title: '40 Full Mock Papers', desc: '20 complete papers per exam matching the real pattern and difficulty.' },
            { icon: Award, title: 'Instant Results', desc: 'Get scored instantly with detailed explanations for every question.' },
            { icon: TrendingUp, title: 'Track Progress', desc: 'Monitor your performance across topics and improve weak areas.' },
          ].map((f, i) => (
            <div key={i} className="card text-center">
              <f.icon className="w-10 h-10 text-indigo-600 mx-auto mb-3" />
              <h3 className="font-bold text-gray-900 mb-1">{f.title}</h3>
              <p className="text-sm text-gray-500">{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-gray-200 py-8 text-center text-sm text-gray-400">
        <p>PrepxCore — Your Complete Exam Preparation Platform</p>
      </footer>
    </div>
  );
}
