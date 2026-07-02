import { Exam, ExamPattern, Subject } from '@/types';

// ============================================================================
// NTPC Subjects
// ============================================================================

const ntpMathematics: Subject = {
  id: 'ntpc-mathematics',
  name: 'Mathematics',
  slug: 'mathematics',
  topics: [
    { id: 'ntpc-mathematics-number-system',      name: 'Number System',         slug: 'number-system',      questionCount: 0 },
    { id: 'ntpc-mathematics-lcm-hcf',             name: 'LCM & HCF',             slug: 'lcm-hcf',             questionCount: 0 },
    { id: 'ntpc-mathematics-simplification',      name: 'Simplification',        slug: 'simplification',      questionCount: 0 },
    { id: 'ntpc-mathematics-ratio-proportion',    name: 'Ratio & Proportion',    slug: 'ratio-proportion',    questionCount: 0 },
    { id: 'ntpc-mathematics-percentage',          name: 'Percentage',            slug: 'percentage',          questionCount: 0 },
    { id: 'ntpc-mathematics-profit-loss',         name: 'Profit & Loss',         slug: 'profit-loss',         questionCount: 0 },
    { id: 'ntpc-mathematics-simple-compound-interest', name: 'Simple & Compound Interest', slug: 'simple-compound-interest', questionCount: 0 },
    { id: 'ntpc-mathematics-time-work',           name: 'Time & Work',           slug: 'time-work',           questionCount: 0 },
    { id: 'ntpc-mathematics-time-speed-distance', name: 'Time Speed Distance',   slug: 'time-speed-distance', questionCount: 0 },
    { id: 'ntpc-mathematics-average',             name: 'Average',               slug: 'average',             questionCount: 0 },
    { id: 'ntpc-mathematics-mensuration',         name: 'Mensuration',           slug: 'mensuration',         questionCount: 0 },
    { id: 'ntpc-mathematics-algebra',             name: 'Algebra',               slug: 'algebra',             questionCount: 0 },
    { id: 'ntpc-mathematics-geometry',            name: 'Geometry',              slug: 'geometry',            questionCount: 0 },
    { id: 'ntpc-mathematics-trigonometry',        name: 'Trigonometry',          slug: 'trigonometry',        questionCount: 0 },
    { id: 'ntpc-mathematics-statistics',          name: 'Statistics',            slug: 'statistics',          questionCount: 0 },
    { id: 'ntpc-mathematics-age-problems',        name: 'Age Problems',          slug: 'age-problems',        questionCount: 0 },
    { id: 'ntpc-mathematics-pipes-cisterns',      name: 'Pipes & Cisterns',      slug: 'pipes-cisterns',      questionCount: 0 },
    { id: 'ntpc-mathematics-boats-streams',       name: 'Boats & Streams',       slug: 'boats-streams',       questionCount: 0 },
    { id: 'ntpc-mathematics-partnership',         name: 'Partnership',           slug: 'partnership',         questionCount: 0 },
  ],
};

const ntpReasoning: Subject = {
  id: 'ntpc-reasoning',
  name: 'General Intelligence & Reasoning',
  slug: 'reasoning',
  topics: [
    { id: 'ntpc-reasoning-analogies',              name: 'Analogies',               slug: 'analogies',              questionCount: 0 },
    { id: 'ntpc-reasoning-coding-decoding',        name: 'Coding-Decoding',         slug: 'coding-decoding',        questionCount: 0 },
    { id: 'ntpc-reasoning-series',                 name: 'Series',                  slug: 'series',                 questionCount: 0 },
    { id: 'ntpc-reasoning-blood-relations',        name: 'Blood Relations',         slug: 'blood-relations',        questionCount: 0 },
    { id: 'ntpc-reasoning-syllogism',              name: 'Syllogism',               slug: 'syllogism',              questionCount: 0 },
    { id: 'ntpc-reasoning-venn-diagrams',          name: 'Venn Diagrams',           slug: 'venn-diagrams',          questionCount: 0 },
    { id: 'ntpc-reasoning-direction-sense',        name: 'Direction Sense',         slug: 'direction-sense',        questionCount: 0 },
    { id: 'ntpc-reasoning-ordering-ranking',       name: 'Ordering & Ranking',      slug: 'ordering-ranking',       questionCount: 0 },
    { id: 'ntpc-reasoning-clock-calendar',         name: 'Clock & Calendar',        slug: 'clock-calendar',         questionCount: 0 },
    { id: 'ntpc-reasoning-puzzles',                name: 'Puzzles',                 slug: 'puzzles',                questionCount: 0 },
    { id: 'ntpc-reasoning-data-sufficiency',       name: 'Data Sufficiency',        slug: 'data-sufficiency',       questionCount: 0 },
    { id: 'ntpc-reasoning-mathematical-operations', name: 'Mathematical Operations', slug: 'mathematical-operations', questionCount: 0 },
    { id: 'ntpc-reasoning-statement-conclusion',   name: 'Statement & Conclusion',  slug: 'statement-conclusion',   questionCount: 0 },
    { id: 'ntpc-reasoning-classification',         name: 'Classification',          slug: 'classification',         questionCount: 0 },
    { id: 'ntpc-reasoning-missing-numbers',        name: 'Missing Numbers',         slug: 'missing-numbers',        questionCount: 0 },
    { id: 'ntpc-reasoning-non-verbal',             name: 'Non-Verbal Reasoning',    slug: 'non-verbal',             questionCount: 0 },
  ],
};

const ntpGeneralAwareness: Subject = {
  id: 'ntpc-general-awareness',
  name: 'General Awareness',
  slug: 'general-awareness',
  topics: [
    { id: 'ntpc-gk-indian-history',          name: 'Indian History',           slug: 'indian-history',          questionCount: 0 },
    { id: 'ntpc-gk-geography',               name: 'Geography',                slug: 'geography',               questionCount: 0 },
    { id: 'ntpc-gk-indian-polity',           name: 'Indian Polity',            slug: 'indian-polity',           questionCount: 0 },
    { id: 'ntpc-gk-economics',               name: 'Economics',                slug: 'economics',               questionCount: 0 },
    { id: 'ntpc-gk-general-science',         name: 'General Science',          slug: 'general-science',         questionCount: 0 },
    { id: 'ntpc-gk-current-affairs',         name: 'Current Affairs',          slug: 'current-affairs',         questionCount: 0 },
    { id: 'ntpc-gk-art-culture',             name: 'Art & Culture',            slug: 'art-culture',             questionCount: 0 },
    { id: 'ntpc-gk-sports',                  name: 'Sports',                   slug: 'sports',                  questionCount: 0 },
    { id: 'ntpc-gk-computers-technology',    name: 'Computers & Technology',   slug: 'computers-technology',    questionCount: 0 },
    { id: 'ntpc-gk-environment-ecology',     name: 'Environment & Ecology',    slug: 'environment-ecology',     questionCount: 0 },
    { id: 'ntpc-gk-books-authors',           name: 'Books & Authors',          slug: 'books-authors',           questionCount: 0 },
    { id: 'ntpc-gk-important-days-events',   name: 'Important Days & Events',  slug: 'important-days-events',   questionCount: 0 },
    { id: 'ntpc-gk-government-schemes',      name: 'Government Schemes',       slug: 'government-schemes',      questionCount: 0 },
    { id: 'ntpc-gk-transport-communication', name: 'Transport & Communication', slug: 'transport-communication', questionCount: 0 },
    { id: 'ntpc-gk-inventions-discoveries',  name: 'Inventions & Discoveries', slug: 'inventions-discoveries',  questionCount: 0 },
  ],
};

// ============================================================================
// Group D Subjects
// ============================================================================

const gdMathematics: Subject = {
  id: 'group-d-mathematics',
  name: 'Mathematics',
  slug: 'mathematics',
  topics: [
    { id: 'group-d-mathematics-real', name: 'Real Exam Questions (Dec 2025)', slug: 'real-exam-math', questionCount: 2309 },
  ],
};

const gdScience: Subject = {
  id: 'group-d-science',
  name: 'General Science',
  slug: 'general-science',
  topics: [
    { id: 'group-d-science-real', name: 'Real Exam Questions (Dec 2025)', slug: 'real-exam-physics', questionCount: 2393 },
  ],
};

const gdReasoning: Subject = {
  id: 'group-d-reasoning',
  name: 'General Intelligence & Reasoning',
  slug: 'reasoning',
  topics: [
    { id: 'group-d-reasoning-real', name: 'Real Exam Questions (Dec 2025)', slug: 'real-exam-reasoning', questionCount: 2472 },
  ],
};

const gdGeneralAwareness: Subject = {
  id: 'group-d-general-awareness',
  name: 'General Awareness',
  slug: 'general-awareness',
  topics: [
    { id: 'group-d-ga-real', name: 'Real Exam Questions (Dec 2025)', slug: 'real-exam-ga', questionCount: 2395 },
  ],
};

// ============================================================================
// Exam Patterns
// ============================================================================

const ntpPattern: ExamPattern = {
  sections: [
    { name: 'General Awareness',              questionCount: 40, marks: 40 },
    { name: 'Mathematics',                    questionCount: 30, marks: 30 },
    { name: 'General Intelligence & Reasoning', questionCount: 30, marks: 30 },
  ],
  totalQuestions: 100,
  totalMarks: 100,
  durationMinutes: 90,
  negativeMarking: -1 / 3,
};

const gdPattern: ExamPattern = {
  sections: [
    { name: 'Mathematics',                    questionCount: 25, marks: 25 },
    { name: 'General Science',                questionCount: 25, marks: 25 },
    { name: 'General Intelligence & Reasoning', questionCount: 30, marks: 30 },
    { name: 'General Awareness',              questionCount: 20, marks: 20 },
  ],
  totalQuestions: 100,
  totalMarks: 100,
  durationMinutes: 90,
  negativeMarking: -1 / 3,
};

// ============================================================================
// Exam List
// ============================================================================

export const examList: Exam[] = [
  {
    id: 'ntpc',
    name: 'RRB NTPC',
    slug: 'ntpc',
    description: 'Non-Technical Popular Categories — Graduate & Undergraduate Level',
    icon: 'Train',
    color: 'rail-navy',
    totalVacancies: 8868,
    pattern: ntpPattern,
    subjects: [ntpMathematics, ntpReasoning, ntpGeneralAwareness],
    status: 'ongoing',
  },
  {
    id: 'alp',
    name: 'RRB ALP',
    slug: 'alp',
    description: 'Assistant Loco Pilot — Mathematics, Reasoning, Basic Science & Engineering',
    icon: 'Train',
    color: 'rail-red',
    totalVacancies: 11127,
    pattern: {
      sections: [
        { name: 'Mathematics', questionCount: 25, marks: 25 },
        { name: 'General Intelligence & Reasoning', questionCount: 25, marks: 25 },
        { name: 'Basic Science & Engineering', questionCount: 40, marks: 40 },
        { name: 'General Awareness', questionCount: 10, marks: 10 },
      ],
      totalQuestions: 100,
      totalMarks: 100,
      durationMinutes: 90,
      negativeMarking: -1 / 3,
    },
    subjects: [
      ntpMathematics,  // Reuse NTPC Math — identical syllabus
      ntpReasoning,     // Reuse NTPC Reasoning
      { id: 'basic-science-engineering', name: 'Basic Science & Engineering', slug: 'basic-science-engineering', topics: [
        { id: 'bse-engineering-basics', name: 'Engineering Basics', slug: 'engineering-basics', questionCount: 0 },
        { id: 'bse-physics-applied', name: 'Applied Physics', slug: 'physics-applied', questionCount: 0 },
        { id: 'bse-it-literacy', name: 'IT Literacy', slug: 'it-literacy', questionCount: 0 },
      ]},
      ntpGeneralAwareness,  // Reuse NTPC GA
    ],
    status: 'ongoing',
  },
  {
    id: 'technician',
    name: 'RRB Technician Gr I',
    slug: 'technician',
    description: 'Grade I Signal — Computers, Science & Engineering focus',
    icon: 'Wrench',
    color: 'rail-green',
    totalVacancies: 6557,
    pattern: {
      sections: [
        { name: 'Mathematics', questionCount: 20, marks: 20 },
        { name: 'General Intelligence & Reasoning', questionCount: 15, marks: 15 },
        { name: 'Basics of Computers & Applications', questionCount: 20, marks: 20 },
        { name: 'Basic Science & Engineering', questionCount: 35, marks: 35 },
        { name: 'General Awareness', questionCount: 10, marks: 10 },
      ],
      totalQuestions: 100,
      totalMarks: 100,
      durationMinutes: 90,
      negativeMarking: -1 / 3,
    },
    subjects: [
      ntpMathematics,
      ntpReasoning,
      { id: 'computers-applications', name: 'Basics of Computers & Applications', slug: 'computers-applications', topics: [
        { id: 'comp-hardware', name: 'Hardware & Architecture', slug: 'hardware', questionCount: 0 },
        { id: 'comp-software', name: 'Software & OS', slug: 'software-os-office', questionCount: 0 },
        { id: 'comp-networks', name: 'Networks & Security', slug: 'networks-security', questionCount: 0 },
      ]},
      { id: 'basic-science-engineering', name: 'Basic Science & Engineering', slug: 'basic-science-engineering', topics: [
        { id: 'bse-engineering-basics', name: 'Engineering Basics', slug: 'engineering-basics', questionCount: 0 },
        { id: 'bse-physics-applied', name: 'Applied Physics', slug: 'physics-applied', questionCount: 0 },
        { id: 'bse-it-literacy', name: 'IT Literacy', slug: 'it-literacy', questionCount: 0 },
      ]},
      ntpGeneralAwareness,
    ],
    status: 'notified',
  },
  {
    id: 'group-d',
    name: 'RRB Group D',
    slug: 'group-d',
    description: 'Level 1 Posts — Track Maintainer, Pointsman, Assistant & more',
    icon: 'Wrench',
    color: 'rail-red',
    totalVacancies: 22082,
    pattern: gdPattern,
    subjects: [gdMathematics, gdScience, gdReasoning, gdGeneralAwareness],
    status: 'upcoming',
  },
];

// ============================================================================
// Subject Map (exam-slug → subjects)
// ============================================================================

export const subjectMap: Record<string, Subject[]> = {
  'ntpc':     [ntpMathematics, ntpReasoning, ntpGeneralAwareness],
  'group-d':  [gdMathematics, gdScience, gdReasoning, gdGeneralAwareness],
};
