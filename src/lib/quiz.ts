import { Question, TestSession, AnsweredQuestion, SectionBreakdown, TopicBreakdown } from '@/types';
import { shuffleArray } from './utils';

export function generateMockTest(
  questions: Question[],
  sectionDistribution: { subjectId: string; count: number }[],
  testName: string,
  examId: string
): { questions: Question[]; sectionBreakdown: SectionBreakdown[] } {
  const selectedQuestions: Question[] = [];
  const sectionBreakdown: SectionBreakdown[] = [];

  for (const section of sectionDistribution) {
    const pool = questions.filter(q => q.subjectId === section.subjectId);
    const selected = shuffleArray(pool).slice(0, section.count);
    selectedQuestions.push(...selected);
    sectionBreakdown.push({
      name: section.subjectId.split('-').pop() || section.subjectId,
      correct: 0,
      total: selected.length,
    });
  }

  return {
    questions: shuffleArray(selectedQuestions),
    sectionBreakdown,
  };
}

export function calculateScore(answers: AnsweredQuestion[]): {
  correct: number;
  wrong: number;
  skipped: number;
  score: number;
  total: number;
} {
  let correct = 0;
  let wrong = 0;
  let skipped = 0;

  for (const answer of answers) {
    if (answer.selectedOption === null) {
      skipped++;
    } else if (answer.isCorrect) {
      correct++;
    } else {
      wrong++;
    }
  }

  const score = correct - wrong * (1 / 3);
  return {
    correct,
    wrong,
    skipped,
    score: Math.round(score * 100) / 100,
    total: answers.length,
  };
}

export function calculateTopicBreakdown(
  answers: AnsweredQuestion[],
  questions: Question[]
): TopicBreakdown[] {
  const topicMap = new Map<string, { correct: number; total: number; name: string }>();

  for (const answer of answers) {
    const question = questions.find(q => q.id === answer.questionId);
    if (!question) continue;

    const key = question.topicId;
    if (!topicMap.has(key)) {
      topicMap.set(key, { correct: 0, total: 0, name: question.topicId.split('-').pop() || key });
    }

    const entry = topicMap.get(key)!;
    entry.total++;
    if (answer.isCorrect) entry.correct++;
  }

  return Array.from(topicMap.entries()).map(([topicId, data]) => ({
    topicId,
    topicName: data.name,
    correct: data.correct,
    total: data.total,
    percentage: data.total > 0 ? Math.round((data.correct / data.total) * 100) : 0,
  }));
}

export function getDifficultyColor(difficulty: string): string {
  switch (difficulty) {
    case 'easy': return 'text-green-600 bg-green-50';
    case 'medium': return 'text-yellow-600 bg-yellow-50';
    case 'hard': return 'text-red-600 bg-red-50';
    default: return 'text-gray-600 bg-gray-50';
  }
}
