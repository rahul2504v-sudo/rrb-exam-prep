'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { getSessions, clearAllSessions, getAverageScore, getBestScore } from '@/lib/storage';
import { formatTime } from '@/lib/utils';
import { TestSession } from '@/types';
import { BarChart3, Clock, Target, Trophy, Trash2, ChevronRight, BookOpen, FileText } from 'lucide-react';
import { examList } from '@/data/exams';

export default function ResultsPage() {
  const [sessions, setSessions] = useState<TestSession[]>([]);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    setSessions(getSessions());
  }, []);

  if (!mounted) return null;

  const averageScore = getAverageScore();
  const bestScore = getBestScore();

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Your Results</h1>

      {sessions.length === 0 ? (
        <div className="card text-center py-16">
          <BarChart3 className="w-16 h-16 text-gray-300 mx-auto mb-4" />
          <h2 className="text-xl font-semibold text-gray-700 mb-2">No test results yet</h2>
          <p className="text-gray-500 mb-6">Start a mock test or topic practice to see your results here.</p>
          <div className="flex justify-center gap-3">
            {examList.map(exam => (
              <Link key={exam.id} href={`/exam/${exam.slug}`} className="btn-primary text-sm">
                Start {exam.name}
              </Link>
            ))}
          </div>
        </div>
      ) : (
        <>
          {/* Stats Overview */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-8">
            <div className="card text-center">
              <FileText className="w-5 h-5 text-rail-navy mx-auto mb-1" />
              <div className="text-2xl font-bold text-gray-900">{sessions.length}</div>
              <div className="text-xs text-gray-500">Tests Taken</div>
            </div>
            <div className="card text-center">
              <Trophy className="w-5 h-5 text-yellow-500 mx-auto mb-1" />
              <div className="text-2xl font-bold text-gray-900">{bestScore.toFixed(1)}</div>
              <div className="text-xs text-gray-500">Best Score</div>
            </div>
            <div className="card text-center">
              <Target className="w-5 h-5 text-green-500 mx-auto mb-1" />
              <div className="text-2xl font-bold text-gray-900">{averageScore.toFixed(1)}</div>
              <div className="text-xs text-gray-500">Average Score</div>
            </div>
            <div className="card text-center">
              <Clock className="w-5 h-5 text-orange-500 mx-auto mb-1" />
              <div className="text-2xl font-bold text-gray-900">
                {sessions.reduce((sum, s) => sum + s.totalQuestions, 0)}
              </div>
              <div className="text-xs text-gray-500">Total Questions</div>
            </div>
          </div>

          {/* Session List */}
          <div className="space-y-3">
            {sessions.map(session => {
              const exam = examList.find(e => e.id === session.examId);
              const percentage = Math.round((session.correctAnswers / session.totalQuestions) * 100);
              const scoreColor = percentage >= 70 ? 'text-green-600' : percentage >= 40 ? 'text-yellow-600' : 'text-red-600';
              
              return (
                <Link
                  key={session.id}
                  href={`/results/${session.id}`}
                  className="card flex items-center justify-between group cursor-pointer"
                >
                  <div className="flex items-center gap-4">
                    <div className={`w-12 h-12 rounded-full flex items-center justify-center font-bold text-lg ${
                      percentage >= 70 ? 'bg-green-50 text-green-600' :
                      percentage >= 40 ? 'bg-yellow-50 text-yellow-600' :
                      'bg-red-50 text-red-600'
                    }`}>
                      {percentage}%
                    </div>
                    <div>
                      <h3 className="font-semibold text-gray-900 group-hover:text-rail-navy transition-colors">
                        {session.testName}
                      </h3>
                      <p className="text-sm text-gray-500">
                        {exam?.name || 'Unknown Exam'} • {session.correctAnswers}/{session.totalQuestions} correct
                      </p>
                      <p className="text-xs text-gray-400 mt-0.5">
                        {new Date(session.completedAt).toLocaleDateString('en-IN', { 
                          day: 'numeric', month: 'short', year: 'numeric',
                          hour: '2-digit', minute: '2-digit'
                        })}
                      </p>
                    </div>
                  </div>
                  
                  <div className="flex items-center gap-4">
                    <div className="text-right hidden sm:block">
                      <div className="text-sm font-medium text-gray-700">
                        Score: <span className={scoreColor}>{session.score.toFixed(1)}</span>
                      </div>
                      <div className="text-xs text-gray-400">
                        {formatTime(session.timeTaken)}
                      </div>
                    </div>
                    <ChevronRight className="w-5 h-5 text-gray-300 group-hover:text-rail-navy transition-colors" />
                  </div>
                </Link>
              );
            })}
          </div>

          {/* Clear All */}
          {sessions.length > 0 && (
            <div className="mt-8 text-center">
              <button
                onClick={() => {
                  if (confirm('Clear all test results? This cannot be undone.')) {
                    clearAllSessions();
                    setSessions([]);
                  }
                }}
                className="flex items-center gap-1.5 mx-auto text-sm text-gray-400 hover:text-red-600 transition-colors"
              >
                <Trash2 className="w-4 h-4" />
                Clear All Results
              </button>
            </div>
          )}
        </>
      )}
    </div>
  );
}
