'use client';

import { useState, useEffect, useCallback, useRef } from 'react';
import { useParams, useRouter, useSearchParams } from 'next/navigation';
import Link from 'next/link';
import { examList } from '@/data/exams';
import { loadTopicQuestions, loadTopicSet, loadMockPaper, getTopicSetCount } from '@/data/questionLoader';
import { calculateScore, calculateTopicBreakdown } from '@/lib/quiz';
import { saveSession, getSessions } from '@/lib/storage';
import { formatTime, shuffleArray } from '@/lib/utils';
import { Question, TestSession, AnsweredQuestion } from '@/types';
import { Clock, ChevronLeft, ChevronRight, CheckCircle, XCircle, AlertCircle, Send, Grid3X3 } from 'lucide-react';
import { useLanguage } from '@/lib/LanguageContext';

export default function QuizPage() {
  const params = useParams();
  const router = useRouter();
  const searchParams = useSearchParams();
  const slug = params.slug as string;
  const type = params.type as string;
  const paramId = params.id as string;
  const { t, language } = useLanguage();
  const lang = (language === 'hi' ? 'hi' : 'en') as 'en' | 'hi';

  const exam = examList.find(e => e.slug === slug);

  const [questions, setQuestions] = useState<Question[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, string | null>>({});
  const [timeLeft, setTimeLeft] = useState(90 * 60);
  const [startTime] = useState(Date.now());
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [session, setSession] = useState<TestSession | null>(null);
  const [loading, setLoading] = useState(true);
  const [showPalette, setShowPalette] = useState(false);
  const [showSetSelector, setShowSetSelector] = useState(false);
  const [setCount, setSetCount] = useState(0);
  const [completedSets, setCompletedSets] = useState<Set<number>>(new Set());
  const [mockCompleted, setMockCompleted] = useState<Set<number>>(new Set());
  const questionStartTimes = useRef<Record<string, number>>({});

  const isMock = type === 'mock';
  const isTopic = type === 'topic';
  const setNum = searchParams.get('set');
  const isSetMode = isTopic && setNum !== null;
  const testName = isMock ? `Mock Paper #${parseInt(paramId) + 1}` : isSetMode ? `Set #${parseInt(setNum!) + 1}` : 'Topic Practice';

  // Show set selector for topics without a set parameter
  const needsSetSelector = isTopic && setNum === null;

  // Load sets count for set selector
  useEffect(() => {
    if (needsSetSelector && exam) {
      getTopicSetCount(exam.id, paramId).then(setSetCount);
    }
  }, [needsSetSelector, exam, paramId]);

  // Load completed sets/mocks for styling
  useEffect(() => {
    if (!exam) return;
    const sessions = getSessions();
    const completed = new Set<number>();
    const mockDone = new Set<number>();
    
    for (const s of sessions) {
      if (s.examId !== exam.id) continue;
      if (s.testType === 'sectional' && s.topicId === paramId && s.setIndex !== undefined) {
        completed.add(s.setIndex);
      }
      if (s.testType === 'mock') {
        mockDone.add(s.mockIndex || 0);
      }
    }
    setCompletedSets(completed);
    setMockCompleted(mockDone);
  }, [exam, paramId]);

  // Load questions
  useEffect(() => {
    async function loadQuestions() {
      let selectedQuestions: Question[] = [];

      if (isMock) {
        // Load specific mock paper
        selectedQuestions = await loadMockPaper(exam?.id || '', parseInt(paramId), lang);
        setTimeLeft(90 * 60);
      } else if (isSetMode) {
        // Load specific topic set
        selectedQuestions = await loadTopicSet(exam?.id || '', paramId, parseInt(setNum!), lang);
        setTimeLeft(15 * 60);
      } else if (needsSetSelector) {
        setLoading(false);
        return;
      }

      setQuestions(selectedQuestions);
      const initialAnswers: Record<string, string | null> = {};
      selectedQuestions.forEach(q => { initialAnswers[q.id] = null; });
      setAnswers(initialAnswers);
      setLoading(false);
    }
    loadQuestions();
  }, [exam, slug, type, paramId, lang, isMock, isSetMode, needsSetSelector, setNum]);

  // Timer
  useEffect(() => {
    if (needsSetSelector || (!isMock && !isSetMode) || isSubmitted || timeLeft <= 0) return;
    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) { clearInterval(timer); handleSubmit(); return 0; }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [needsSetSelector, isMock, isSetMode, isSubmitted, timeLeft]);

  // Track time per question
  useEffect(() => {
    const q = questions[currentIndex];
    if (q && !questionStartTimes.current[q.id]) questionStartTimes.current[q.id] = Date.now();
  }, [currentIndex, questions]);

  const handleSelectOption = (questionId: string, option: string) => {
    if (isSubmitted) return;
    setAnswers(prev => ({ ...prev, [questionId]: option }));
  };

  const handleSubmit = useCallback(() => {
    if (isSubmitted) return;
    const answeredQuestions: AnsweredQuestion[] = questions.map(q => {
      const st = questionStartTimes.current[q.id] || Date.now();
      return {
        questionId: q.id, selectedOption: answers[q.id] || null,
        isCorrect: answers[q.id] === q.correctOption,
        timeSpent: Math.round((Date.now() - st) / 1000),
      };
    });
    const { correct, wrong, skipped, score } = calculateScore(answeredQuestions);
    const topicBreakdown = calculateTopicBreakdown(answeredQuestions, questions);
    const newSession: TestSession = {
      id: `session-${Date.now()}`, examId: exam?.id || '',
      testType: isMock ? 'mock' : isSetMode ? 'sectional' : 'topic', testName,
      topicId: paramId,
      setIndex: isSetMode ? parseInt(setNum!) : undefined,
      mockIndex: isMock ? parseInt(paramId) : undefined,
      totalQuestions: questions.length, correctAnswers: correct, wrongAnswers: wrong,
      skipped, score: Math.max(0, score),
      timeTaken: Math.round((Date.now() - startTime) / 1000),
      startedAt: new Date(startTime).toISOString(), completedAt: new Date().toISOString(),
      questions: answeredQuestions, topicBreakdown,
    };
    saveSession(newSession);
    setSession(newSession);
    setIsSubmitted(true);
  }, [isSubmitted, questions, answers, startTime, exam, isMock, testName]);

  const goToQuestion = (index: number) => {
    if (index >= 0 && index < questions.length) setCurrentIndex(index);
  };

  const getOptionStyle = (question: Question, optionKey: string) => {
    if (!isSubmitted) return answers[question.id] === optionKey ? 'option-btn option-btn-selected' : 'option-btn';
    if (optionKey === question.correctOption) return 'option-btn option-btn-correct';
    if (answers[question.id] === optionKey && optionKey !== question.correctOption) return 'option-btn option-btn-incorrect';
    return 'option-btn opacity-60';
  };

  // Set Selector View
  if (needsSetSelector) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-12">
        <Link href={`/exam/${slug}`} className="text-sm text-gray-500 hover:text-rail-navy mb-4 inline-block">
          {t('backToExams')}
        </Link>
        <h1 className="text-2xl font-bold text-gray-900 mb-2">Select a Set</h1>
        <p className="text-gray-600 mb-6">Each set contains 10 questions. Choose a set to start practicing.</p>
        
        {loading ? (
          <div className="text-center py-8">
            <div className="animate-spin w-8 h-8 border-4 border-rail-navy border-t-transparent rounded-full mx-auto" />
          </div>
        ) : (
          <div className="grid grid-cols-4 sm:grid-cols-5 gap-3">
            {Array.from({ length: setCount }, (_, i) => {
              const isDone = completedSets.has(i);
              return (
                <Link key={i} href={`?set=${i}`}
                  className={`flex flex-col items-center justify-center p-4 rounded-xl border-2 transition-all ${
                    isDone 
                      ? 'border-green-400 bg-green-50 hover:bg-green-100' 
                      : 'border-gray-200 hover:border-rail-navy hover:bg-blue-50'
                  }`}>
                  <span className={`text-2xl font-bold ${isDone ? 'text-green-700' : 'text-rail-navy'}`}>
                    {isDone ? '✓' : `#${i + 1}`}
                  </span>
                  <span className="text-xs text-gray-400 mt-1">10 Qs</span>
                </Link>
              );
            })}
            {setCount === 0 && (
              <p className="col-span-full text-center text-gray-500">No sets available for this topic yet.</p>
            )}
          </div>
        )}
      </div>
    );
  }

  // Loading
  if (loading) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center">
        <div className="animate-spin w-8 h-8 border-4 border-rail-navy border-t-transparent rounded-full mx-auto" />
        <p className="text-gray-500 mt-4">{t('loading')}</p>
      </div>
    );
  }

  if (!exam || questions.length === 0) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center">
        <AlertCircle className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <h2 className="text-xl font-bold text-gray-900">{t('noQuestions')}</h2>
        <p className="text-gray-500 mt-2">{t('noQuestionsDesc')}</p>
        <Link href={`/exam/${slug}`} className="text-rail-navy hover:underline mt-4 inline-block">
          {t('backToExams')}
        </Link>
      </div>
    );
  }

  // Results
  if (isSubmitted && session) {
    return <ResultsView session={session} questions={questions} examId={exam.id} />;
  }

  const currentQuestion = questions[currentIndex];
  const answeredCount = Object.values(answers).filter(a => a !== null).length;
  const hasTimer = isMock || isSetMode;

  return (
    <div className="max-w-5xl mx-auto px-4 py-4">
      <div className="sticky top-16 z-40 bg-white border-b pb-3 mb-4">
        <div className="flex items-center justify-between">
          <div>
            <Link href={`/exam/${slug}`} className="text-sm text-gray-500 hover:text-rail-navy">
              {t('backToExams')}
            </Link>
            <h1 className="font-semibold text-gray-900">{testName}</h1>
          </div>
          <div className="flex items-center gap-4">
            {hasTimer && (
              <div className={`flex items-center gap-1.5 font-mono font-bold text-lg ${timeLeft < 300 ? 'text-red-600 timer-warning' : 'text-gray-900'}`}>
                <Clock className="w-5 h-5" /> {formatTime(timeLeft)}
              </div>
            )}
            <div className="text-sm text-gray-500">{answeredCount}/{questions.length} {t('answered')}</div>
            <button onClick={() => setShowPalette(!showPalette)} className="text-sm text-rail-navy font-medium hover:underline">
              {showPalette ? t('hide') : t('palette')}
            </button>
          </div>
        </div>
        <div className="w-full bg-gray-200 h-1.5 rounded-full mt-3">
          <div className="bg-rail-navy h-1.5 rounded-full transition-all duration-300"
            style={{ width: `${((currentIndex + 1) / questions.length) * 100}%` }} />
        </div>
      </div>

      <div className="flex gap-4">
        <div className="flex-1 min-w-0">
          <div className="card">
            <div className="flex items-center justify-between mb-4">
              <span className="text-sm font-medium text-gray-500">
                Q{currentIndex + 1} of {questions.length}
                <span className={`ml-2 px-2 py-0.5 rounded-full text-xs ${currentQuestion.difficulty === 'easy' ? 'bg-green-50 text-green-700' : currentQuestion.difficulty === 'hard' ? 'bg-red-50 text-red-700' : 'bg-yellow-50 text-yellow-700'}`}>
                  {currentQuestion.difficulty}
                </span>
              </span>
              {currentQuestion.sourceYear && <span className="text-xs text-gray-400">Source: {currentQuestion.sourceYear}</span>}
            </div>
            <p className="text-lg font-medium text-gray-900 mb-6 leading-relaxed">{currentQuestion.questionText}</p>
            <div className="space-y-3">
              {(['A', 'B', 'C', 'D'] as const).map(option => (
                <button key={option} onClick={() => handleSelectOption(currentQuestion.id, option)} disabled={isSubmitted}
                  className={getOptionStyle(currentQuestion, option)}>
                  <span className="font-semibold mr-3 text-gray-400">({option})</span>
                  {currentQuestion[`option${option}` as keyof Question] as string}
                </button>
              ))}
            </div>
          </div>

          <div className="flex items-center justify-between mt-4">
            <button onClick={() => goToQuestion(currentIndex - 1)} disabled={currentIndex === 0}
              className="flex items-center gap-1 px-4 py-2 text-sm font-medium text-gray-700 bg-white rounded-lg border hover:bg-gray-50 disabled:opacity-30">
              <ChevronLeft className="w-4 h-4" /> {t('previous')}
            </button>
            {currentIndex < questions.length - 1 ? (
              <button onClick={() => goToQuestion(currentIndex + 1)}
                className="flex items-center gap-1 px-4 py-2 text-sm font-medium text-white bg-rail-navy rounded-lg hover:bg-blue-900">
                {t('next')} <ChevronRight className="w-4 h-4" />
              </button>
            ) : (
              <button onClick={handleSubmit}
                className="flex items-center gap-2 px-6 py-2.5 text-sm font-bold text-white bg-green-600 rounded-lg hover:bg-green-700 shadow-md">
                <Send className="w-4 h-4" /> {t('submitTest')}
              </button>
            )}
          </div>
        </div>

        {showPalette && (
          <div className="hidden lg:block w-64 flex-shrink-0">
            <div className="card sticky top-36">
              <h4 className="font-semibold text-sm text-gray-700 mb-3">{t('questions')}</h4>
              <div className="grid grid-cols-5 gap-1.5">
                {questions.map((q, idx) => (
                  <button key={q.id} onClick={() => goToQuestion(idx)}
                    className={`w-9 h-9 text-xs font-medium rounded-lg transition-all
                      ${idx === currentIndex ? 'ring-2 ring-rail-navy bg-blue-50 text-rail-navy' :
                        answers[q.id] !== null ? 'bg-green-100 text-green-700' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`}>
                    {idx + 1}
                  </button>
                ))}
              </div>
              <div className="mt-4 space-y-1.5 text-xs">
                <div className="flex items-center gap-2"><span className="w-3 h-3 rounded bg-green-100" /> {t('answered')} ({answeredCount})</div>
                <div className="flex items-center gap-2"><span className="w-3 h-3 rounded bg-gray-100" /> {t('skipped')} ({questions.length - answeredCount})</div>
              </div>
              <button onClick={handleSubmit} className="w-full mt-4 btn-primary text-sm py-2">{t('submitTest')}</button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

// Results component
function ResultsView({ session, questions, examId }: { session: TestSession; questions: Question[]; examId: string }) {
  const router = useRouter();
  const percentage = Math.round((session.correctAnswers / session.totalQuestions) * 100);
  const scoreColor = percentage >= 70 ? 'text-green-600' : percentage >= 40 ? 'text-yellow-600' : 'text-red-600';
  const bgColor = percentage >= 70 ? 'bg-green-50' : percentage >= 40 ? 'bg-yellow-50' : 'bg-red-50';

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Test Results</h1>
      <div className="card mb-6">
        <div className="flex flex-col sm:flex-row items-center gap-6">
          <div className={`w-32 h-32 rounded-full ${bgColor} flex items-center justify-center`}>
            <div className="text-center">
              <div className={`text-3xl font-bold ${scoreColor}`}>{percentage}%</div>
              <div className="text-xs text-gray-500">{session.score.toFixed(1)}/{session.totalQuestions}</div>
            </div>
          </div>
          <div className="flex-1 grid grid-cols-2 sm:grid-cols-4 gap-4 text-center">
            <div><div className="text-2xl font-bold text-green-600">{session.correctAnswers}</div><div className="text-xs text-gray-500">Correct</div></div>
            <div><div className="text-2xl font-bold text-red-600">{session.wrongAnswers}</div><div className="text-xs text-gray-500">Wrong</div></div>
            <div><div className="text-2xl font-bold text-gray-400">{session.skipped}</div><div className="text-xs text-gray-500">Skipped</div></div>
            <div><div className="text-2xl font-bold text-gray-700">{formatTime(session.timeTaken)}</div><div className="text-xs text-gray-500">Time</div></div>
          </div>
        </div>
      </div>
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
      <div className="card mb-6">
        <h3 className="font-bold text-gray-900 mb-4">Question Review</h3>
        <div className="space-y-4">
          {questions.map((q, idx) => {
            const answer = session.questions.find(a => a.questionId === q.id);
            const isCorrect = answer?.isCorrect;
            const isSkipped = !answer?.selectedOption;
            return (
              <div key={q.id} className={`p-4 rounded-lg border ${isCorrect ? 'border-green-200 bg-green-50/50' : isSkipped ? 'border-gray-200 bg-gray-50' : 'border-red-200 bg-red-50/50'}`}>
                <div className="flex items-start gap-3">
                  <div className="flex-shrink-0 mt-0.5">
                    {isCorrect ? <CheckCircle className="w-5 h-5 text-green-600" /> : isSkipped ? <AlertCircle className="w-5 h-5 text-gray-400" /> : <XCircle className="w-5 h-5 text-red-600" />}
                  </div>
                  <div className="flex-1">
                    <p className="font-medium text-gray-900"><span className="text-gray-400 mr-2">Q{idx + 1}.</span>{q.questionText}</p>
                    <div className="mt-2 space-y-1">
                      {(['A', 'B', 'C', 'D'] as const).map(opt => {
                        const isSelected = answer?.selectedOption === opt;
                        const isCorrectOpt = q.correctOption === opt;
                        return (
                          <div key={opt} className={`text-sm pl-4 ${isCorrectOpt ? 'text-green-700 font-medium' : (isSelected && !isCorrectOpt) ? 'text-red-600' : 'text-gray-600'}`}>
                            ({opt}) {q[`option${opt}` as keyof Question] as string}{isCorrectOpt && ' ✓'}{isSelected && !isCorrectOpt && ' ✗'}
                          </div>
                        );
                      })}
                    </div>
                    {!isCorrect && (
                      <div className="mt-2 p-3 bg-white rounded border border-gray-200">
                        <p className="text-sm font-medium text-gray-700">Explanation:</p>
                        <p className="text-sm text-gray-600 mt-1">{q.explanation}</p>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
      <div className="flex gap-3">
        <button onClick={() => router.push(`/exam/${examId}`)} className="btn-secondary text-sm">Back to Exam</button>
        <button onClick={() => window.location.reload()} className="btn-primary text-sm">Retake</button>
        <button onClick={() => router.push('/results')} className="btn-secondary text-sm">All Results</button>
      </div>
    </div>
  );
}
