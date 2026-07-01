import { Question, QuestionJSON, questionFromJSON } from '@/types';
import { examList } from './exams';

// Cache for loaded question files
const questionCache: Record<string, QuestionJSON[]> = {};

// Get the JSON path for a topic
function getTopicPath(examId: string, subjectSlug: string, topicSlug: string): string {
  return `/data/questions/${examId}/${subjectSlug}/${topicSlug}.json`;
}

// Map subject IDs to slugs
function getSubjectSlug(examId: string, subjectId: string): string {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return '';
  const subject = exam.subjects.find(s => s.id === subjectId);
  return subject?.slug || '';
}

// Map topic IDs to slugs
function getTopicSlug(examId: string, topicId: string): string {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return '';
  for (const subject of exam.subjects) {
    const topic = subject.topics.find(t => t.id === topicId);
    if (topic) return topic.slug;
  }
  return '';
}

// Find subjectId for a given topicId
function getSubjectForTopic(examId: string, topicId: string): { subjectId: string; subjectSlug: string } | null {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return null;
  for (const subject of exam.subjects) {
    const topic = subject.topics.find(t => t.id === topicId);
    if (topic) return { subjectId: subject.id, subjectSlug: subject.slug };
  }
  return null;
}

// Load questions from a topic JSON file (topicId only — derives subject internally)
export async function loadTopicQuestions(
  examId: string,
  subjectIdOrTopicId: string,
  topicId?: string,
  lang: 'en' | 'hi' = 'en'
): Promise<Question[]> {
  // If topicId is provided, use old signature. Otherwise, derive subject from topicId
  let actualSubjectId: string;
  let actualTopicId: string;
  
  if (topicId) {
    actualSubjectId = subjectIdOrTopicId;
    actualTopicId = topicId;
  } else {
    // Called with just (examId, topicId, lang) — derive subject
    actualTopicId = subjectIdOrTopicId;
    const info = getSubjectForTopic(examId, actualTopicId);
    if (!info) return [];
    actualSubjectId = info.subjectId;
  }
  
  const subjectSlug = getSubjectSlug(examId, actualSubjectId);
  const topicSlug = getTopicSlug(examId, actualTopicId);
  const path = getTopicPath(examId, subjectSlug, topicSlug);
  
  // Check cache first
  if (!questionCache[path]) {
    try {
      const response = await fetch(path);
      if (!response.ok) return [];
      questionCache[path] = await response.json();
    } catch {
      return [];
    }
  }

  return questionCache[path].map(q =>
    questionFromJSON(q, examId, actualSubjectId, actualTopicId, lang)
  );
}

// Load all questions for an exam
export async function loadExamQuestions(
  examId: string,
  lang: 'en' | 'hi' = 'en'
): Promise<Question[]> {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return [];

  const allQuestions: Question[] = [];
  
  for (const subject of exam.subjects) {
    for (const topic of subject.topics) {
      const questions = await loadTopicQuestions(examId, subject.id, topic.id, lang);
      allQuestions.push(...questions);
    }
  }
  
  return allQuestions;
}

// Load questions for a specific subject
export async function loadSubjectQuestions(
  examId: string,
  subjectId: string,
  lang: 'en' | 'hi' = 'en'
): Promise<Question[]> {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return [];
  
  const subject = exam.subjects.find(s => s.id === subjectId);
  if (!subject) return [];

  const allQuestions: Question[] = [];
  
  for (const topic of subject.topics) {
    const questions = await loadTopicQuestions(examId, subjectId, topic.id, lang);
    allQuestions.push(...questions);
  }
  
  return allQuestions;
}
