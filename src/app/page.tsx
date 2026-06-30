'use client';

import { useState } from 'react';
import Link from 'next/link';
import { examList } from '@/data/exams';
import { Train, Wrench, Clock, BookOpen, Trophy, BarChart3 } from 'lucide-react';

const featureIcons = {
  Clock: <Clock className="w-6 h-6" />,
  BookOpen: <BookOpen className="w-6 h-6" />,
  Trophy: <Trophy className="w-6 h-6" />,
  BarChart3: <BarChart3 className="w-6 h-6" />,
};

const examIcons: Record<string, React.ReactNode> = {
  Train: <Train className="w-8 h-8" />,
  Wrench: <Wrench className="w-8 h-8" />,
};

export default function HomePage() {
  return (
    <div>
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-rail-navy via-blue-900 to-indigo-900 text-white py-20">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">
            RRB Exam Preparation
          </h1>
          <p className="text-xl text-blue-200 mb-2">
            NTPC & Group D 2026
          </p>
          <p className="text-lg text-blue-300 max-w-2xl mx-auto mb-8">
            Free mock tests, topic-wise practice, and detailed explanations.
            Built from actual syllabus and previous year patterns.
          </p>
          <div className="flex flex-wrap justify-center gap-4 text-sm">
            <span className="bg-white/10 rounded-full px-4 py-2">1000+ Questions</span>
            <span className="bg-white/10 rounded-full px-4 py-2">Full-Length Mocks</span>
            <span className="bg-white/10 rounded-full px-4 py-2">Detailed Solutions</span>
            <span className="bg-white/10 rounded-full px-4 py-2">Track Progress</span>
          </div>
        </div>
      </section>

      {/* Exam Cards */}
      <section className="max-w-6xl mx-auto px-4 -mt-10 relative z-10">
        <div className="grid md:grid-cols-2 gap-6">
          {examList.map((exam) => (
            <Link
              key={exam.id}
              href={`/exam/${exam.slug}`}
              className="card group cursor-pointer hover:border-rail-navy/30"
            >
              <div className="flex items-start gap-4">
                <div className={`p-3 rounded-xl bg-${exam.color === 'rail-navy' ? 'rail-navy' : 'rail-red'} text-white`}
                     style={{ backgroundColor: exam.color === 'rail-navy' ? '#1a237e' : '#d32f2f' }}>
                  {examIcons[exam.icon] || <BookOpen className="w-8 h-8" />}
                </div>
                <div className="flex-1">
                  <h2 className="text-xl font-bold text-gray-900 group-hover:text-rail-navy transition-colors">
                    {exam.name}
                  </h2>
                  <p className="text-gray-600 mt-1">{exam.description}</p>
                  <div className="flex flex-wrap gap-3 mt-4">
                    <span className="text-xs bg-blue-50 text-blue-700 px-3 py-1 rounded-full font-medium">
                      {exam.totalVacancies.toLocaleString()} Vacancies
                    </span>
                    <span className="text-xs bg-green-50 text-green-700 px-3 py-1 rounded-full font-medium">
                      {exam.pattern.totalQuestions} Questions
                    </span>
                    <span className="text-xs bg-orange-50 text-orange-700 px-3 py-1 rounded-full font-medium">
                      {exam.pattern.durationMinutes} Minutes
                    </span>
                  </div>
                  <div className="mt-4 flex items-center text-sm text-rail-navy font-semibold group-hover:gap-2 transition-all">
                    Start Practicing →
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Features */}
      <section className="max-w-6xl mx-auto px-4 py-16">
        <h2 className="text-2xl font-bold text-center mb-10">Why Practice Here?</h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            { icon: Clock, title: 'Timed Mock Tests', desc: '90-minute exams matching the real pattern with countdown timer' },
            { icon: BookOpen, title: 'Topic-Wise Practice', desc: 'Pick any subject and topic to focus your preparation' },
            { icon: Trophy, title: 'Instant Results', desc: 'Score calculation with negative marking as per official pattern' },
            { icon: BarChart3, title: 'Performance Tracking', desc: 'Track your progress across tests with detailed analytics' },
          ].map((feature, i) => (
            <div key={i} className="card text-center">
              <div className="inline-flex p-3 rounded-xl bg-blue-50 text-rail-navy mb-4">
                <feature.icon className="w-6 h-6" />
              </div>
              <h3 className="font-semibold text-gray-900 mb-2">{feature.title}</h3>
              <p className="text-sm text-gray-600">{feature.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Stats */}
      <section className="bg-gray-100 py-12">
        <div className="max-w-6xl mx-auto px-4">
          <div className="grid grid-cols-3 gap-8 text-center">
            <div>
              <div className="text-3xl font-bold text-rail-navy">1000+</div>
              <div className="text-sm text-gray-600 mt-1">Practice Questions</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-rail-navy">7</div>
              <div className="text-sm text-gray-600 mt-1">Subject Areas</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-rail-navy">2</div>
              <div className="text-sm text-gray-600 mt-1">Exam Patterns</div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
