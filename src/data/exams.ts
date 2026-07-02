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

// ============================================================================
// SSC CGL
// ============================================================================

const sscReasoning: Subject = {
  id: 'ssc-reasoning', name: 'General Intelligence & Reasoning', slug: 'reasoning',
  topics: [{ id: 'ssc-reasoning-real', name: 'Reasoning Practice Sets', slug: 'reasoning', questionCount: 25 }],
};
const sscGA: Subject = {
  id: 'ssc-ga', name: 'General Awareness', slug: 'general-awareness',
  topics: [{ id: 'ssc-ga-real', name: 'GA Practice Sets', slug: 'general-awareness', questionCount: 25 }],
};
const sscQuant: Subject = {
  id: 'ssc-quant', name: 'Quantitative Aptitude', slug: 'quantitative-aptitude',
  topics: [{ id: 'ssc-quant-real', name: 'Quant Practice Sets', slug: 'quantitative-aptitude', questionCount: 25 }],
};
const sscEnglish: Subject = {
  id: 'ssc-english', name: 'English Comprehension', slug: 'english',
  topics: [{ id: 'ssc-english-real', name: 'English Practice Sets', slug: 'english', questionCount: 25 }],
};
const sscPattern: ExamPattern = {
  sections: [
    { name: 'General Intelligence & Reasoning', questionCount: 25, marks: 50 },
    { name: 'General Awareness', questionCount: 25, marks: 50 },
    { name: 'Quantitative Aptitude', questionCount: 25, marks: 50 },
    { name: 'English Comprehension', questionCount: 25, marks: 50 },
  ],
  totalQuestions: 100, totalMarks: 200, durationMinutes: 60, negativeMarking: -0.5,
};

export const examList: Exam[] = [
  {
    id: 'ssc-cgl', name: 'SSC CGL Tier I', slug: 'ssc-cgl',
    description: 'Combined Graduate Level — Previous Year Paper',
    icon: 'BookOpen', color: 'rail-navy', totalVacancies: 0, pattern: sscPattern,
    subjects: [sscReasoning, sscGA, sscQuant, sscEnglish], status: 'upcoming',
  },
  {
    id: 'group-d', name: 'RRB Group D', slug: 'group-d',
    description: 'Level 1 Posts — Track Maintainer, Pointsman, Helper, Assistant & more',
    icon: 'Wrench', color: 'rail-red', totalVacancies: 0, pattern: gdPattern,
    subjects: [gdMathematics, gdScience, gdReasoning, gdGA], status: 'upcoming',
  },
];

export const subjectMap: Record<string, Subject[]> = {
  'ssc-cgl': [sscReasoning, sscGA, sscQuant, sscEnglish],
  'group-d': [gdMathematics, gdScience, gdReasoning, gdGA],
};
