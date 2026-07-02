'use client';

import { useState, useEffect } from 'react';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import { examList } from '@/data/exams';
import { getMockPaperCount } from '@/data/questionLoader';
import { Clock, BookOpen, AlertCircle, Check, Layers, ArrowLeft } from 'lucide-react';
import { useLanguage } from '@/lib/LanguageContext';
import { getSessions } from '@/lib/storage';

export default function MockPage() {
  const params = useParams();
  const slug = params.slug as string;
  const exam = examList.find(e => e.slug === slug);
  const { t } = useLanguage();
  const [mockCount, setMockCount] = useState(0);
  const [completedMocks, setCompletedMocks] = useState<Set<number>>(new Set());

  useEffect(() => {
    if (!exam) return;
    getMockPaperCount(exam.id).then(setMockCount);
    const sessions = getSessions();
    const mocks = new Set<number>();
    sessions.filter(s => s.testType === 'mock' && s.examId === exam.id).forEach(s => {
      if (s.mockIndex !== undefined) mocks.add(s.mockIndex);
    });
    setCompletedMocks(mocks);
  }, [exam]);

  if (!exam) {
    return (
      <div className="max-w-6xl mx-auto px-4 py-20 text-center">
        <AlertCircle className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <h1 className="text-2xl font-bold text-gray-900">Exam Not Found</h1>
        <Link href="/" className="text-rail-navy hover:underline mt-4 inline-block">Go Home</Link>
      </div>
    );
  }

  return (
    <div className="max-w-5xl mx-auto px-4 py-8">
      <div className="mb-8">
        <Link href={`/exam/${exam.slug}`} className="text-sm text-gray-500 hover:text-rail-navy mb-3 inline-flex items-center gap-1">
          <ArrowLeft className="w-3 h-3" /> Back to Section Practice
        </Link>
        <h1 className="text-3xl font-bold text-gray-900">{exam.name} — {exam.id === 'ssc-cgl' ? 'Previous Year Papers' : 'Full Length Tests'}</h1>
        <p className="text-gray-600 mt-1">{exam.description}</p>
        <div className="flex flex-wrap gap-4 mt-4">
          <div className="flex items-center gap-1.5 text-sm bg-blue-50 text-blue-700 px-3 py-1.5 rounded-full">
            100 Questions
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-orange-50 text-orange-700 px-3 py-1.5 rounded-full">
            <Clock className="w-4 h-4" /> {exam.pattern.durationMinutes} Minutes
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-red-50 text-red-700 px-3 py-1.5 rounded-full">
            -1/3 Negative Marking
          </div>
        </div>
      </div>

      <div className="card mb-6">
        <h3 className="font-bold text-lg text-gray-900 mb-3 flex items-center gap-2">
          <BookOpen className="w-5 h-5 text-rail-navy" />
          Exam Pattern
        </h3>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          {exam.pattern.sections.map((sec, i) => (
            <div key={i} className="bg-gray-50 rounded-xl p-3 text-center">
              <div className="text-xl font-bold text-indigo-600">{sec.questionCount}</div>
              <div className="text-xs text-gray-500">{sec.name}</div>
            </div>
          ))}
        </div>
      </div>

      <h2 className="text-xl font-bold text-gray-900 mb-4 flex items-center gap-2">
        <Layers className="w-5 h-5 text-rail-navy" />
        Full Length Tests
        <span className="text-sm font-normal text-gray-500">({mockCount} papers)</span>
      </h2>
      
      <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-10 gap-3">
        {Array.from({ length: mockCount }, (_, i) => {
          const isDone = completedMocks.has(i);
          return (
            <Link key={i} href={`/quiz/${exam.slug}/mock/${i}`}
              className={`flex flex-col items-center justify-center p-4 rounded-xl border-2 transition-all ${
                isDone
                  ? 'border-green-400 bg-green-50 hover:bg-green-100'
                  : 'border-gray-200 hover:border-indigo-300 hover:bg-indigo-50'
              }`}>
              <span className={`text-2xl font-bold ${isDone ? 'text-green-600' : 'text-indigo-600'}`}>
                {isDone ? <Check className="w-6 h-6" /> : `#${i + 1}`}
              </span>
              <span className="text-xs text-gray-400 mt-1">100 Qs</span>
              <span className="text-xs text-gray-400">90 min</span>
            </Link>
          );
        })}
      </div>

      {mockCount === 0 && (
        <div className="text-center py-12 text-gray-500">
          <AlertCircle className="w-10 h-10 mx-auto mb-3 text-gray-300" />
          <p>No mock papers available yet.</p>
        </div>
      )}
    </div>
  );
}
