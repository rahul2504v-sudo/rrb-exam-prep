// Exam structure types
export interface ExamPattern {
  sections: ExamSection[];
  totalQuestions: number;
  totalMarks: number;
  durationMinutes: number;
  negativeMarking: number;
}

export interface ExamSection {
  name: string;
  questionCount: number;
  marks: number;
}

export interface Topic {
  id: string;
  name: string;
  slug: string;
  questionCount: number;
}

export interface Subject {
  id: string;
  name: string;
  slug: string;
  topics: Topic[];
}

export interface Exam {
  id: string;
  name: string;
  slug: string;
  description: string;
  icon: string;
  color: string;
  totalVacancies: number;
  pattern: ExamPattern;
  subjects: Subject[];
  status?: 'ongoing' | 'upcoming' | 'completed' | 'notified';
}

// Bilingual question format for per-topic JSON files
// Stored in public/data/questions/{exam}/{subject}/{topic}.json

export interface BilingualContent {
  question: string;
  options: [string, string, string, string];  // A, B, C, D
  explanation: string;
}

export interface QuestionJSON {
  id: string;
  correctOption: 'A' | 'B' | 'C' | 'D';
  difficulty: 'easy' | 'medium' | 'hard';
  sourceYear?: number;
  en: BilingualContent;
  hi: BilingualContent;
}

// Runtime question type used in the app
export interface Question {
  id: string;
  examId: string;
  subjectId: string;
  topicId: string;
  questionText: string;
  questionImage?: string;
  optionA: string;
  optionB: string;
  optionC: string;
  optionD: string;
  correctOption: 'A' | 'B' | 'C' | 'D';
  explanation: string;
  difficulty: 'easy' | 'medium' | 'hard';
  sourceYear?: number;
  language?: string;
}

export interface AnsweredQuestion {
  questionId: string;
  selectedOption: string | null;
  isCorrect: boolean;
  timeSpent: number;
}

export interface SectionBreakdown {
  name: string;
  correct: number;
  total: number;
}

export interface TopicBreakdown {
  topicId: string;
  topicName: string;
  correct: number;
  total: number;
  percentage: number;
}

export interface TestSession {
  id: string;
  examId: string;
  testType: 'topic' | 'mock' | 'sectional';
  topicId?: string;
  setIndex?: number;
  mockIndex?: number;
  testName: string;
  totalQuestions: number;
  correctAnswers: number;
  wrongAnswers: number;
  skipped: number;
  score: number;
  timeTaken: number;
  startedAt: string;
  completedAt: string;
  questions: AnsweredQuestion[];
  sectionBreakdown?: SectionBreakdown[];
  topicBreakdown?: TopicBreakdown[];
}

export interface UserProgress {
  sessions: TestSession[];
  totalTestsTaken: number;
  averageScore: number;
  bestScore: number;
  totalQuestionsAttempted: number;
}

// Convert a JSON question to runtime Question format for given language
export function questionFromJSON(
  q: QuestionJSON,
  examId: string,
  subjectId: string,
  topicId: string,
  lang: 'en' | 'hi'
): Question {
  const content = q[lang];
  return {
    id: q.id,
    examId,
    subjectId,
    topicId,
    questionText: content.question,
    questionImage: (q as any).imageUrl,
    optionA: content.options[0],
    optionB: content.options[1],
    optionC: content.options[2],
    optionD: content.options[3],
    correctOption: q.correctOption,
    explanation: content.explanation,
    difficulty: q.difficulty,
    sourceYear: q.sourceYear,
    language: lang,
  };
}
