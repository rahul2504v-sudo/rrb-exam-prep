'use client';

import { useState, useEffect } from 'react';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import { examList } from '@/data/exams';
import { getTopicSetCount, getMockPaperCount } from '@/data/questionLoader';
import { BookOpen, Clock, ArrowRight, Target, AlertCircle, RotateCcw, Eye, Layers } from 'lucide-react';
import { useLanguage } from '@/lib/LanguageContext';
import { Subject } from '@/types';
import { getSessions } from '@/lib/storage';
import { formatTime } from '@/lib/utils';

export default function ExamPage() {
  const params = useParams();
  const slug = params.slug as string;
  const exam = examList.find(e => e.slug === slug);
  const { t } = useLanguage();
  const [sectionalTests, setSectionalTests] = useState<any[]>([]);
  const [topicSetCounts, setTopicSetCounts] = useState<Record<string, number>>({});
  const [mockCount, setMockCount] = useState(0);

  useEffect(() => {
    const sessions = getSessions();
    setSectionalTests(sessions.filter(s => s.testType === 'sectional' && s.examId === exam?.id));
  }, [exam]);

  useEffect(() => {
    if (!exam) return;
    async function load() {
      const counts: Record<string, number> = {};
      for (const subject of exam!.subjects) {
        for (const topic of subject.topics) {
          counts[topic.id] = await getTopicSetCount(exam!.id, topic.id);
        }
      }
      setTopicSetCounts(counts);
      setMockCount(await getMockPaperCount(exam!.id));
    }
    load();
  }, [exam]);

  if (!exam) {
    return (
      <div className="max-w-6xl mx-auto px-4 py-20 text-center">
        <AlertCircle className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <h1 className="text-2xl font-bold text-gray-900">Exam Not Found</h1>
        <Link href="/" className="text-rail-navy hover:underline mt-4 inline-block">{t('backToHome')}</Link>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      {/* Header */}
      <div className="mb-8">
        <Link href="/" className="text-sm text-gray-500 hover:text-rail-navy mb-2 inline-block">{t('backToExams')}</Link>
        <h1 className="text-3xl font-bold text-gray-900">{exam.name} — Topic Practice</h1>
        <p className="text-gray-600 mt-1">{exam.description}</p>
        <div className="flex flex-wrap gap-4 mt-4">
          <div className="flex items-center gap-1.5 text-sm bg-green-50 text-green-700 px-3 py-1.5 rounded-full">
            <BookOpen className="w-4 h-4" /> {exam.pattern.totalQuestions} {t('questions')}
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-orange-50 text-orange-700 px-3 py-1.5 rounded-full">
            <Clock className="w-4 h-4" /> {exam.pattern.durationMinutes} {t('minutes')}
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-red-50 text-red-700 px-3 py-1.5 rounded-full">
            {t('negativeMarking')}
          </div>
          {/* Mock/Previous Year Button */}
          <Link href={`/exam/${exam.slug}/mock`}
            className={`flex items-center gap-2 text-sm text-white px-4 py-2 rounded-full hover:bg-emerald-700 font-medium ${exam.id === 'ssc-cgl' ? 'bg-indigo-600 hover:bg-indigo-700' : 'bg-emerald-600 hover:bg-emerald-700'}`}>
            <Layers className="w-4 h-4" /> {exam.id === 'ssc-cgl' ? 'Previous Year Papers' : 'Full Length Tests'} ({mockCount} papers)
          </Link>
        </div>
      </div>

      <div className="grid lg:grid-cols-3 gap-8">
        {exam.id !== 'ssc-cgl' && (
        <div className="lg:col-span-2 space-y-6">
          <h2 className="text-xl font-bold text-gray-900">Section-wise Practice Sets</h2>

          {exam.subjects.map((subject: Subject) => (
            <div key={subject.id} className="card">
              <h3 className="font-bold text-lg text-gray-900 mb-1 flex items-center gap-2">
                <BookOpen className="w-5 h-5 text-rail-navy" />
                {subject.name}
              </h3>
              <p className="text-xs text-gray-400 mb-3">Click a topic to see available sets (10 questions each)</p>
              <div className="grid sm:grid-cols-2 gap-1.5">
                {subject.topics.map((topic) => {
                  const setCount = topicSetCounts[topic.id] || 0;
                  return (
                    <Link key={topic.id} href={`/quiz/${exam.slug}/topic/${topic.id}`}
                      className="flex items-center justify-between p-2.5 rounded-lg border border-gray-100 
                               hover:border-rail-navy hover:bg-blue-50/50 transition-all group">
                      <span className="text-sm font-medium text-gray-700 group-hover:text-rail-navy truncate">
                        {topic.name}
                      </span>
                      <span className="flex items-center gap-1 text-xs text-gray-400 flex-shrink-0 ml-2">
                        {setCount > 0 && (
                          <span className="bg-green-50 text-green-700 px-1.5 py-0.5 rounded font-medium">{setCount} sets</span>
                        )}
                        <ArrowRight className="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity" />
                      </span>
                    </Link>
                  );
                })}
              </div>
            </div>
          ))}
        </div>
        )}

        {/* Sectional Test History */}
        <div className="space-y-4">
          {sectionalTests.length > 0 && (
            <div className="card">
              <h3 className="font-semibold text-gray-900 mb-3 flex items-center gap-2">
                <RotateCcw className="w-4 h-4 text-rail-navy" /> Recent Sets
              </h3>
              <div className="space-y-2">
                {sectionalTests.slice(0, 5).map(st => {
                  const pct = Math.round((st.correctAnswers / st.totalQuestions) * 100);
                  return (
                    <div key={st.id} className="flex items-center justify-between p-2 bg-gray-50 rounded-lg">
                      <div>
                        <span className="text-sm font-medium text-gray-700">{st.testName}</span>
                        <span className="text-xs text-gray-400 ml-2">
                          {new Date(st.completedAt).toLocaleDateString('en-IN', { day: 'numeric', month: 'short' })}
                        </span>
                      </div>
                      <div className="flex items-center gap-2">
                        <span className={`text-sm font-bold ${pct >= 70 ? 'text-green-600' : pct >= 40 ? 'text-amber-600' : 'text-red-600'}`}>
                          {pct}%
                        </span>
                        <Link href={`/results/${st.id}`} className="text-xs text-rail-navy hover:underline flex items-center gap-1">
                          <Eye className="w-3 h-3" /> Review
                        </Link>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
