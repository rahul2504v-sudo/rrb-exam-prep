import { Exam, Subject, ExamPattern } from '@/types';

// ============================================================================
// RRB Group D
// ============================================================================

const gdMathematics: Subject = {
  id: 'group-d-mathematics', name: 'Mathematics', slug: 'mathematics',
  topics: [{ id: 'group-d-mathematics-real', name: 'Mathematics Practice Sets', slug: 'real-exam-math', questionCount: 2309 }],
};
const gdScience: Subject = {
  id: 'group-d-science', name: 'General Science', slug: 'general-science',
  topics: [{ id: 'group-d-science-real', name: 'General Science Practice Sets', slug: 'real-exam-physics', questionCount: 2393 }],
};
const gdReasoning: Subject = {
  id: 'group-d-reasoning', name: 'General Intelligence & Reasoning', slug: 'reasoning',
  topics: [{ id: 'group-d-reasoning-real', name: 'Reasoning Practice Sets', slug: 'real-exam-reasoning', questionCount: 2472 }],
};
const gdGA: Subject = {
  id: 'group-d-general-awareness', name: 'General Awareness & Current Affairs', slug: 'general-awareness',
  topics: [{ id: 'group-d-ga-real', name: 'General Awareness Practice Sets', slug: 'real-exam-ga', questionCount: 2395 }],
};
const gdPattern: ExamPattern = {
  sections: [
    { name: 'Mathematics', questionCount: 25, marks: 25 },
    { name: 'General Science', questionCount: 25, marks: 25 },
    { name: 'General Intelligence & Reasoning', questionCount: 30, marks: 30 },
    { name: 'General Awareness & Current Affairs', questionCount: 20, marks: 20 },
  ],
  totalQuestions: 100, totalMarks: 100, durationMinutes: 90, negativeMarking: -1/3,
};

export const examList: Exam[] = [
  {
    id: 'group-d', name: 'RRB Group D', slug: 'group-d',
    description: 'Level 1 Posts — Track Maintainer, Pointsman, Helper, Assistant & more',
    icon: 'Wrench', color: 'rail-red', totalVacancies: 0, pattern: gdPattern,
    subjects: [gdMathematics, gdScience, gdReasoning, gdGA], status: 'upcoming',
  },
];

export const subjectMap: Record<string, Subject[]> = {
  'group-d': [gdMathematics, gdScience, gdReasoning, gdGA],
};
