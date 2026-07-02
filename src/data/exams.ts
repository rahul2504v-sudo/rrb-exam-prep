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
// RRB Technician Grade 1
// ============================================================================

const tg1All: Subject = {
  id: 'tech-g1-all', name: 'All Sections', slug: 'all-questions',
  topics: [{ id: 'tech-g1-real', name: 'Technician Grade 1 Questions', slug: 'all-questions', questionCount: 458 }],
};
const tg1Pattern: ExamPattern = {
  sections: [
    { name: 'Basics of Science & Engineering', questionCount: 20, marks: 20 },
    { name: 'General Awareness', questionCount: 10, marks: 10 },
    { name: 'General Intelligence & Reasoning', questionCount: 15, marks: 15 },
    { name: 'Basic Science & Engineering', questionCount: 35, marks: 35 },
    { name: 'Mathematics', questionCount: 20, marks: 20 },
  ],
  totalQuestions: 100, totalMarks: 100, durationMinutes: 90, negativeMarking: -1/3,
};

// ============================================================================
// RRB Technician Grade 3
// ============================================================================

const tg3All: Subject = {
  id: 'tech-g3-all', name: 'All Sections', slug: 'all-questions',
  topics: [{ id: 'tech-g3-real', name: 'Technician Grade 3 Questions', slug: 'all-questions', questionCount: 277 }],
};
const tg3Pattern: ExamPattern = {
  sections: [
    { name: 'General Science', questionCount: 40, marks: 40 },
    { name: 'Mathematics', questionCount: 25, marks: 25 },
    { name: 'General Intelligence & Reasoning', questionCount: 25, marks: 25 },
    { name: 'General Awareness', questionCount: 10, marks: 10 },
  ],
  totalQuestions: 100, totalMarks: 100, durationMinutes: 90, negativeMarking: -1/3,
};

// ============================================================================
// SSC CGL
// ============================================================================

const sscAll: Subject = {
  id: 'ssc-all', name: 'All Sections', slug: 'all-questions',
  topics: [{ id: 'ssc-all-real', name: 'SSC CGL Questions', slug: 'all-questions', questionCount: 17235 }],
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

// ============================================================================
// Exam List
// ============================================================================

export const examList: Exam[] = [
  {
    id: 'group-d', name: 'RRB Group D', slug: 'group-d',
    description: 'Level 1 Posts — Track Maintainer, Pointsman, Helper, Assistant & more',
    icon: 'Wrench', color: 'rail-red', totalVacancies: 0, pattern: gdPattern,
    subjects: [gdMathematics, gdScience, gdReasoning, gdGA], status: 'upcoming',
  },
  {
    id: 'technician-g1', name: 'RRB Technician Grade 1', slug: 'technician-g1',
    description: 'Grade 1 Signal — 6,557 vacancies, Computer-Based Test',
    icon: 'Wrench', color: 'rail-green', totalVacancies: 0, pattern: tg1Pattern,
    subjects: [tg1All], status: 'upcoming',
  },
  {
    id: 'technician-g3', name: 'RRB Technician Grade 3', slug: 'technician-g3',
    description: 'Grade 3 — 6,557 vacancies, Computer-Based Test',
    icon: 'Wrench', color: 'rail-navy', totalVacancies: 0, pattern: tg3Pattern,
    subjects: [tg3All], status: 'upcoming',
  },
  {
    id: 'ssc-cgl', name: 'SSC CGL', slug: 'ssc-cgl',
    description: 'Combined Graduate Level — Tier 1 (Reasoning, GA, Quant, English)',
    icon: 'Wrench', color: 'rail-navy', totalVacancies: 0, pattern: sscPattern,
    subjects: [sscAll], status: 'upcoming',
  },
];

export const subjectMap: Record<string, Subject[]> = {
  'group-d': [gdMathematics, gdScience, gdReasoning, gdGA],
  'technician-g1': [tg1All],
  'technician-g3': [tg3All],
  'ssc-cgl': [sscAll],
};
