'use client';

import { useState, useEffect } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { getSession } from '@/lib/storage';
import { formatTime } from '@/lib/utils';
import { TestSession } from '@/types';
import { CheckCircle, XCircle, AlertCircle, ArrowLeft, RotateCcw } from 'lucide-react';

export default function ResultDetailPage() {
  const params = useParams();
  const router = useRouter();
  const sessionId = params.sessionId as string;
  const [session, setSession] = useState<TestSession | null>(null);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    const s = getSession(sessionId);
    setSession(s || null);
  }, [sessionId]);

  if (!mounted) return null;
  if (!session) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center">
        <AlertCircle className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <h1 className="text-xl font-bold">Result not found</h1>
        <Link href="/results" className="text-rail-navy hover:underline mt-4 inline-block">Back to Results</Link>
      </div>
    );
  }

  const percentage = Math.round((session.correctAnswers / session.totalQuestions) * 100);
  const scoreColor = percentage >= 70 ? 'text-green-600' : percentage >= 40 ? 'text-yellow-600' : 'text-red-600';
  const bgColor = percentage >= 70 ? 'bg-green-50' : percentage >= 40 ? 'bg-yellow-50' : 'bg-red-50';

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <button onClick={() => router.back()} className="text-sm text-gray-500 hover:text-rail-navy mb-4 flex items-center gap-1">
        <ArrowLeft className="w-4 h-4" /> Back
      </button>

      <h1 className="text-2xl font-bold text-gray-900 mb-2">{session.testName}</h1>
      <p className="text-sm text-gray-500 mb-6">
        {new Date(session.completedAt).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })}
      </p>

      {/* Score Card */}
      <div className="card mb-6">
        <div className="flex flex-col sm:flex-row items-center gap-6">
          <div className={`w-32 h-32 rounded-full ${bgColor} flex items-center justify-center`}>
            <div className="text-center">
              <div className={`text-3xl font-bold ${scoreColor}`}>{percentage}%</div>
              <div className="text-xs text-gray-500">{session.score.toFixed(1)}/{session.totalQuestions}</div>
            </div>
          </div>
          
          <div className="flex-1 grid grid-cols-2 sm:grid-cols-4 gap-4 text-center">
            <div>
              <div className="text-2xl font-bold text-green-600">{session.correctAnswers}</div>
              <div className="text-xs text-gray-500">Correct</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-red-600">{session.wrongAnswers}</div>
              <div className="text-xs text-gray-500">Wrong</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-gray-400">{session.skipped}</div>
              <div className="text-xs text-gray-500">Skipped</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-gray-700">{formatTime(session.timeTaken)}</div>
              <div className="text-xs text-gray-500">Time</div>
            </div>
          </div>
        </div>
      </div>

      {/* Topic Breakdown */}
      {session.topicBreakdown && session.topicBreakdown.length > 0 && (
        <div className="card mb-6">
          <h3 className="font-bold text-gray-900 mb-4">Topic-wise Performance</h3>
          <div className="space-y-3">
            {session.topicBreakdown.map(tb => (
              <div key={tb.topicId}>
                <div className="flex justify-between text-sm mb-1">
                  <span className="text-gray-600">{tb.topicName.replace(/-/g, ' ')}</span>
                  <span className="font-medium">{tb.correct}/{tb.total} ({tb.percentage}%)</span>
                </div>
                <div className="w-full bg-gray-200 h-2 rounded-full">
                  <div className={`h-2 rounded-full ${tb.percentage >= 70 ? 'bg-green-500' : tb.percentage >= 40 ? 'bg-yellow-500' : 'bg-red-500'}`}
                    style={{ width: `${tb.percentage}%` }} />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Question Review */}
      <div className="card mb-6">
        <h3 className="font-bold text-gray-900 mb-4">Question Review</h3>
        <div className="space-y-4">
          {session.questions.map((answer, idx) => {
            const isCorrect = answer.isCorrect;
            const isSkipped = !answer.selectedOption;
            
            return (
              <div key={answer.questionId} className={`p-4 rounded-lg border ${isCorrect ? 'border-green-200 bg-green-50/50' : isSkipped ? 'border-gray-200 bg-gray-50' : 'border-red-200 bg-red-50/50'}`}>
                <div className="flex items-start gap-3">
                  <div className="flex-shrink-0 mt-0.5">
                    {isCorrect ? <CheckCircle className="w-5 h-5 text-green-600" /> :
                     isSkipped ? <AlertCircle className="w-5 h-5 text-gray-400" /> :
                     <XCircle className="w-5 h-5 text-red-600" />}
                  </div>
                  <div className="flex-1">
                    <p className="font-medium text-gray-900">
                      <span className="text-gray-400 mr-2">Q{idx + 1}.</span>
                      Selected: {answer.selectedOption || 'None'}
                      {isCorrect ? ' ✓' : !isSkipped ? ' ✗' : ''}
                    </p>
                    <p className="text-xs text-gray-500 mt-1">Time: {answer.timeSpent}s</p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      <div className="flex gap-3">
        <button onClick={() => router.push('/results')} className="btn-secondary text-sm">All Results</button>
        <button onClick={() => window.history.back()} className="btn-primary text-sm">
          <RotateCcw className="w-4 h-4 inline mr-1" /> Back
        </button>
      </div>
    </div>
  );
}
