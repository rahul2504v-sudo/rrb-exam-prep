// Core types for the RRB Exam Prep app

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
}

export interface ExamPattern {
  sections: ExamSection[];
  totalQuestions: number;
  totalMarks: number;
  durationMinutes: number;
  negativeMarking: number; // fraction deducted per wrong answer
}

export interface ExamSection {
  name: string;
  questionCount: number;
  marks: number;
}

export interface Subject {
  id: string;
  name: string;
  slug: string;
  topics: Topic[];
}

export interface Topic {
  id: string;
  name: string;
  slug: string;
  questionCount: number;
}

export interface Question {
  id: string;
  examId: string;
  subjectId: string;
  topicId: string;
  questionText: string;
  optionA: string;
  optionB: string;
  optionC: string;
  optionD: string;
  correctOption: 'A' | 'B' | 'C' | 'D';
  explanation: string;
  difficulty: 'easy' | 'medium' | 'hard';
  sourceYear?: number;
}

export interface TestSession {
  id: string;
  examId: string;
  testType: 'topic' | 'mock';
  testName: string;
  totalQuestions: number;
  correctAnswers: number;
  wrongAnswers: number;
  skipped: number;
  score: number;
  timeTaken: number; // seconds
  startedAt: string;
  completedAt: string;
  questions: AnsweredQuestion[];
  sectionBreakdown?: SectionBreakdown[];
  topicBreakdown?: TopicBreakdown[];
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

export interface UserProgress {
  sessions: TestSession[];
  totalTestsTaken: number;
  averageScore: number;
  bestScore: number;
  totalQuestionsAttempted: number;
}
