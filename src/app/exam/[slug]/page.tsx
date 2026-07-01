'use client';

import { useState, useEffect } from 'react';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import { examList } from '@/data/exams';
import { BookOpen, Clock, ArrowRight, Play, Target, AlertCircle, RotateCcw, Eye } from 'lucide-react';
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

  useEffect(() => {
    const sessions = getSessions();
    setSectionalTests(sessions.filter(s => s.testType === 'sectional' && s.examId === exam?.id));
  }, [exam]);

  if (!exam) {
    return (
      <div className="max-w-6xl mx-auto px-4 py-20 text-center">
        <AlertCircle className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <h1 className="text-2xl font-bold text-gray-900">{t('noQuestions')}</h1>
        <Link href="/" className="text-rail-navy hover:underline mt-4 inline-block">
          {t('backToHome')}
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="mb-8">
        <Link href="/" className="text-sm text-gray-500 hover:text-rail-navy mb-2 inline-block">
          {t('backToExams')}
        </Link>
        <h1 className="text-3xl font-bold text-gray-900">{exam.name}</h1>
        <p className="text-gray-600 mt-1">{exam.description}</p>
        
        <div className="flex flex-wrap gap-4 mt-4">
          <div className="flex items-center gap-1.5 text-sm bg-blue-50 text-blue-700 px-3 py-1.5 rounded-full">
            <Target className="w-4 h-4" />
            {exam.totalVacancies.toLocaleString()} {t('vacancies')}
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-green-50 text-green-700 px-3 py-1.5 rounded-full">
            <BookOpen className="w-4 h-4" />
            {exam.pattern.totalQuestions} {t('questions')}
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-orange-50 text-orange-700 px-3 py-1.5 rounded-full">
            <Clock className="w-4 h-4" />
            {exam.pattern.durationMinutes} {t('minutes')}
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-red-50 text-red-700 px-3 py-1.5 rounded-full">
            {t('negativeMarking')}
          </div>
        </div>
      </div>

      <div className="grid lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-6">
          <h2 className="text-xl font-bold text-gray-900">{t('topicPractice')}</h2>

          {exam.subjects.map((subject: Subject) => (
            <div key={subject.id} className="card">
              <div className="flex items-center justify-between mb-4">
                <h3 className="font-bold text-lg text-gray-900 flex items-center gap-2">
                  <BookOpen className="w-5 h-5 text-rail-navy" />
                  {subject.name}
                  <span className="text-sm font-normal text-gray-500">
                    ({subject.topics.length} {t('topics')})
                  </span>
                </h3>
                <Link
                  href={`/quiz/${exam.slug}/sectional/${subject.id}`}
                  className="flex items-center gap-1 px-3 py-1.5 text-xs font-semibold bg-green-50 text-green-700 rounded-lg hover:bg-green-100 transition-colors"
                >
                  <Play className="w-3 h-3" /> 10Q Set
                </Link>
              </div>
              <div className="grid sm:grid-cols-2 gap-2">
                {subject.topics.map((topic) => (
                    <Link key={topic.id} href={`/quiz/${exam.slug}/topic/${topic.id}`}
                      className="flex items-center justify-between p-3 rounded-lg border border-gray-100 
                               hover:border-rail-navy hover:bg-blue-50/50 transition-all group">
                      <span className="text-sm font-medium text-gray-700 group-hover:text-rail-navy">
                        {topic.name}
                      </span>
                      <span className="flex items-center gap-1.5 text-xs text-gray-400">
                        <ArrowRight className="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity" />
                      </span>
                    </Link>
                ))}
              </div>
            </div>
          ))}

          {/* Sectional Test History */}
          {sectionalTests.length > 0 && (
            <div className="card">
              <h3 className="font-bold text-lg text-gray-900 mb-4 flex items-center gap-2">
                <RotateCcw className="w-5 h-5 text-rail-navy" />
                Your Sectional Tests
              </h3>
              <div className="space-y-2">
                {sectionalTests.slice(0, 10).map(st => {
                  const pct = Math.round((st.correctAnswers / st.totalQuestions) * 100);
                  return (
                    <div key={st.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                      <div>
                        <span className="text-sm font-medium text-gray-700">{st.testName}</span>
                        <span className="text-xs text-gray-400 ml-2">
                          {new Date(st.completedAt).toLocaleDateString('en-IN', { day: 'numeric', month: 'short' })}
                        </span>
                      </div>
                      <div className="flex items-center gap-3">
                        <span className={`text-sm font-bold ${pct >= 70 ? 'text-green-600' : pct >= 40 ? 'text-yellow-600' : 'text-red-600'}`}>
                          {st.correctAnswers}/{st.totalQuestions} ({pct}%)
                        </span>
                        <Link href={`/exam/${exam.slug}`}
                          className="flex items-center gap-1 px-2 py-1 text-xs font-medium bg-rail-navy text-white rounded hover:bg-blue-900"
                        >
                          <RotateCcw className="w-3 h-3" /> Retry
                        </Link>
                        <Link href={`/results/${st.id}`}
                          className="flex items-center gap-1 px-2 py-1 text-xs font-medium bg-gray-200 text-gray-700 rounded hover:bg-gray-300"
                        >
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

        <div className="space-y-4">
          <h2 className="text-xl font-bold text-gray-900">{t('mockTests')}</h2>
          
          <div className="card bg-gradient-to-br from-rail-navy to-blue-900 text-white">
            <Play className="w-8 h-8 mb-3" />
            <h3 className="font-bold text-lg mb-1">{t('fullMock')}</h3>
            <p className="text-sm text-blue-200 mb-4">
              {exam.pattern.totalQuestions} {t('questions')} · {exam.pattern.durationMinutes} {t('minutes')}
            </p>
            <div className="space-y-2 mb-4">
              {exam.pattern.sections.map((sec, i) => (
                <div key={i} className="flex justify-between text-sm text-blue-100">
                  <span>{sec.name}</span>
                  <span>{sec.questionCount} {t('questions')}</span>
                </div>
              ))}
            </div>
            <Link href={`/quiz/${exam.slug}/mock/full`}
              className="block w-full text-center bg-white text-rail-navy font-semibold py-2.5 rounded-lg hover:bg-blue-50 transition-colors">
              {t('startMock')}
            </Link>
          </div>

          <div className="card text-sm">
            <h4 className="font-semibold text-gray-900 mb-3">{t('examPattern')}</h4>
            {exam.pattern.sections.map((sec, i) => (
              <div key={i} className="flex justify-between py-1.5 border-b border-gray-50 last:border-0">
                <span className="text-gray-600">{sec.name}</span>
                <span className="font-medium">{sec.questionCount} {t('questions')}</span>
              </div>
            ))}
            <div className="flex justify-between py-1.5 mt-1 pt-2 border-t">
              <span className="text-gray-600">{t('negativeMarking')}</span>
              <span className="font-medium text-red-600">-1/3</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
