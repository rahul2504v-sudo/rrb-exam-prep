'use client';

import { useState, useEffect } from 'react';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import { examList } from '@/data/exams';
import { getTopicSetCount, getMockPaperCount } from '@/data/questionLoader';
import { BookOpen, Clock, ArrowRight, Play, Target, AlertCircle, RotateCcw, Eye, Layers } from 'lucide-react';
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
  const [completedMocks, setCompletedMocks] = useState<Set<number>>(new Set());

  useEffect(() => {
    const sessions = getSessions();
    setSectionalTests(sessions.filter(s => s.testType === 'sectional' && s.examId === exam?.id));
    const mocks = new Set<number>();
    sessions.filter(s => s.testType === 'mock' && s.examId === exam?.id).forEach(s => {
      if (s.mockIndex !== undefined) mocks.add(s.mockIndex);
    });
    setCompletedMocks(mocks);
  }, [exam]);

  useEffect(() => {
    if (!exam) return;
    // Load set counts for all topics
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
        <h1 className="text-2xl font-bold text-gray-900">{t('noQuestions')}</h1>
        <Link href="/" className="text-rail-navy hover:underline mt-4 inline-block">{t('backToHome')}</Link>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="mb-8">
        <Link href="/" className="text-sm text-gray-500 hover:text-rail-navy mb-2 inline-block">{t('backToExams')}</Link>
        <h1 className="text-3xl font-bold text-gray-900">{exam.name}</h1>
        <p className="text-gray-600 mt-1">{exam.description}</p>
        <div className="flex flex-wrap gap-4 mt-4">
          <div className="flex items-center gap-1.5 text-sm bg-blue-50 text-blue-700 px-3 py-1.5 rounded-full">
            <Target className="w-4 h-4" /> {exam.totalVacancies.toLocaleString()} {t('vacancies')}
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-green-50 text-green-700 px-3 py-1.5 rounded-full">
            <BookOpen className="w-4 h-4" /> {exam.pattern.totalQuestions} {t('questions')}
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-orange-50 text-orange-700 px-3 py-1.5 rounded-full">
            <Clock className="w-4 h-4" /> {exam.pattern.durationMinutes} {t('minutes')}
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-red-50 text-red-700 px-3 py-1.5 rounded-full">
            {t('negativeMarking')}
          </div>
        </div>
      </div>

      <div className="grid lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-6">
          <h2 className="text-xl font-bold text-gray-900">Topic-wise Sets</h2>

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

          {/* Mock Test Papers */}
          <div className="card">
            <h3 className="font-bold text-lg text-gray-900 mb-3 flex items-center gap-2">
              <Layers className="w-5 h-5 text-rail-navy" />
              Full-Length Mock Papers
              <span className="text-sm font-normal text-gray-500">({mockCount} papers)</span>
            </h3>
            <div className="grid grid-cols-4 sm:grid-cols-5 md:grid-cols-10 gap-2">
              {Array.from({ length: mockCount }, (_, i) => {
                const isDone = completedMocks.has(i);
                return (
                  <Link key={i} href={`/quiz/${exam.slug}/mock/${i}`}
                    className={`flex flex-col items-center justify-center p-3 rounded-lg border transition-all ${
                      isDone
                        ? 'border-green-400 bg-green-50 hover:bg-green-100'
                        : 'border-gray-200 hover:border-rail-navy hover:bg-blue-50'
                    }`}>
                    <span className={`text-lg font-bold ${isDone ? 'text-green-700' : 'text-rail-navy'}`}>
                      {isDone ? '✓' : `#${i + 1}`}
                    </span>
                    <span className="text-xs text-gray-400">100 Q</span>
                  </Link>
                );
              })}
            </div>
          </div>
        </div>

        <div className="space-y-4">
          <h2 className="text-xl font-bold text-gray-900">{t('mockTests')}</h2>

          {/* Sectional Test History */}
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
                        <span className={`text-xs font-bold ${pct >= 70 ? 'text-green-600' : pct >= 40 ? 'text-yellow-600' : 'text-red-600'}`}>
                          {st.correctAnswers}/{st.totalQuestions}
                        </span>
                        <Link href={`/exam/${exam.slug}`} className="px-2 py-0.5 text-xs bg-rail-navy text-white rounded">Retry</Link>
                        <Link href={`/results/${st.id}`} className="px-2 py-0.5 text-xs bg-gray-200 rounded">Review</Link>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}

          <div className="card text-sm">
            <h4 className="font-semibold text-gray-900 mb-3">{t('examPattern')}</h4>
            {exam.pattern.sections.map((sec, i) => (
              <div key={i} className="flex justify-between py-1.5 border-b border-gray-50 last:border-0">
                <span className="text-gray-600">{sec.name}</span>
                <span className="font-medium">{sec.questionCount} Q</span>
              </div>
            ))}
            <div className="flex justify-between py-1.5 mt-1 pt-2 border-t">
              <span className="text-gray-600">Negative</span>
              <span className="font-medium text-red-600">-1/3</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
