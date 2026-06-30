'use client';

import { useParams } from 'next/navigation';
import Link from 'next/link';
import { examList } from '@/data/exams';
import { getQuestionsByTopic } from '@/data/allQuestions';
import { BookOpen, Clock, ArrowRight, Play, Target, AlertCircle } from 'lucide-react';

export default function ExamPage() {
  const params = useParams();
  const slug = params.slug as string;
  const exam = examList.find(e => e.slug === slug);

  if (!exam) {
    return (
      <div className="max-w-6xl mx-auto px-4 py-20 text-center">
        <AlertCircle className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <h1 className="text-2xl font-bold text-gray-900">Exam not found</h1>
        <Link href="/" className="text-rail-navy hover:underline mt-4 inline-block">
          ← Back to Home
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      {/* Exam Header */}
      <div className="mb-8">
        <Link href="/" className="text-sm text-gray-500 hover:text-rail-navy mb-2 inline-block">
          ← Back to Exams
        </Link>
        <h1 className="text-3xl font-bold text-gray-900">{exam.name}</h1>
        <p className="text-gray-600 mt-1">{exam.description}</p>
        
        {/* Exam Pattern Summary */}
        <div className="flex flex-wrap gap-4 mt-4">
          <div className="flex items-center gap-1.5 text-sm bg-blue-50 text-blue-700 px-3 py-1.5 rounded-full">
            <Target className="w-4 h-4" />
            {exam.totalVacancies.toLocaleString()} Vacancies
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-green-50 text-green-700 px-3 py-1.5 rounded-full">
            <BookOpen className="w-4 h-4" />
            {exam.pattern.totalQuestions} Questions
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-orange-50 text-orange-700 px-3 py-1.5 rounded-full">
            <Clock className="w-4 h-4" />
            {exam.pattern.durationMinutes} Minutes
          </div>
          <div className="flex items-center gap-1.5 text-sm bg-red-50 text-red-700 px-3 py-1.5 rounded-full">
            -1/3 Negative Marking
          </div>
        </div>
      </div>

      <div className="grid lg:grid-cols-3 gap-8">
        {/* Subject & Topic List */}
        <div className="lg:col-span-2 space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-bold text-gray-900">Topic-wise Practice</h2>
          </div>

          {exam.subjects.map((subject) => {
            const subjectQuestions = getQuestionsByTopic(exam.id, '');
            return (
              <div key={subject.id} className="card">
                <h3 className="font-bold text-lg text-gray-900 mb-4 flex items-center gap-2">
                  <BookOpen className="w-5 h-5 text-rail-navy" />
                  {subject.name}
                  <span className="text-sm font-normal text-gray-500">
                    ({subject.topics.length} topics)
                  </span>
                </h3>
                <div className="grid sm:grid-cols-2 gap-2">
                  {subject.topics.map((topic) => {
                    const count = getQuestionsByTopic(exam.id, topic.id).length;
                    return (
                      <Link
                        key={topic.id}
                        href={`/quiz/${exam.slug}/topic/${topic.id}`}
                        className="flex items-center justify-between p-3 rounded-lg border border-gray-100 
                                 hover:border-rail-navy hover:bg-blue-50/50 transition-all group"
                      >
                        <span className="text-sm font-medium text-gray-700 group-hover:text-rail-navy">
                          {topic.name}
                        </span>
                        <span className="flex items-center gap-1.5 text-xs text-gray-400">
                          <span className="bg-gray-100 px-2 py-0.5 rounded-full">{count} Qs</span>
                          <ArrowRight className="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity" />
                        </span>
                      </Link>
                    );
                  })}
                </div>
              </div>
            );
          })}
        </div>

        {/* Mock Test Sidebar */}
        <div className="space-y-4">
          <h2 className="text-xl font-bold text-gray-900">Mock Tests</h2>
          
          <div className="card bg-gradient-to-br from-rail-navy to-blue-900 text-white">
            <Play className="w-8 h-8 mb-3" />
            <h3 className="font-bold text-lg mb-1">Full-Length Mock</h3>
            <p className="text-sm text-blue-200 mb-4">
              Complete {exam.pattern.totalQuestions} questions in {exam.pattern.durationMinutes} minutes
            </p>
            <div className="space-y-2 mb-4">
              {exam.pattern.sections.map((sec, i) => (
                <div key={i} className="flex justify-between text-sm text-blue-100">
                  <span>{sec.name}</span>
                  <span>{sec.questionCount} Q</span>
                </div>
              ))}
            </div>
            <Link
              href={`/quiz/${exam.slug}/mock/full`}
              className="block w-full text-center bg-white text-rail-navy font-semibold py-2.5 rounded-lg hover:bg-blue-50 transition-colors"
            >
              Start Mock Test
            </Link>
          </div>

          {/* Pattern Info */}
          <div className="card text-sm">
            <h4 className="font-semibold text-gray-900 mb-3">Exam Pattern</h4>
            {exam.pattern.sections.map((sec, i) => (
              <div key={i} className="flex justify-between py-1.5 border-b border-gray-50 last:border-0">
                <span className="text-gray-600">{sec.name}</span>
                <span className="font-medium">{sec.questionCount} Questions</span>
              </div>
            ))}
            <div className="flex justify-between py-1.5 mt-1 pt-2 border-t">
              <span className="text-gray-600">Negative Marking</span>
              <span className="font-medium text-red-600">-1/3 per wrong</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
