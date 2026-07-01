import { Question, QuestionJSON, questionFromJSON } from '@/types';
import { examList } from './exams';

const questionCache: Record<string, QuestionJSON[]> = {};
const setIndexCache: Record<string, any> = {};

function getTopicPath(examId: string, subjectSlug: string, topicSlug: string): string {
  return `/data/questions/${examId}/${subjectSlug}/${topicSlug}.json`;
}
function getSubjectSlug(examId: string, subjectId: string): string {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return '';
  return exam.subjects.find(s => s.id === subjectId)?.slug || '';
}
function getTopicSlug(examId: string, topicId: string): string {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return '';
  for (const subject of exam.subjects) {
    const topic = subject.topics.find(t => t.id === topicId);
    if (topic) return topic.slug;
  }
  return '';
}
function getSubjectForTopic(examId: string, topicId: string): { subjectId: string; subjectSlug: string } | null {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return null;
  for (const subject of exam.subjects) {
    const topic = subject.topics.find(t => t.id === topicId);
    if (topic) return { subjectId: subject.id, subjectSlug: subject.slug };
  }
  return null;
}

export async function loadTopicQuestions(
  examId: string, subjectIdOrTopicId: string, topicId?: string, lang: 'en' | 'hi' = 'en'
): Promise<Question[]> {
  let actualSubjectId: string, actualTopicId: string;
  if (topicId && topicId.length > 2) {
    actualSubjectId = subjectIdOrTopicId; actualTopicId = topicId;
  } else {
    actualTopicId = subjectIdOrTopicId;
    const info = getSubjectForTopic(examId, actualTopicId);
    if (!info) return [];
    actualSubjectId = info.subjectId;
  }
  const subjectSlug = getSubjectSlug(examId, actualSubjectId);
  const topicSlug = getTopicSlug(examId, actualTopicId);
  const path = getTopicPath(examId, subjectSlug, topicSlug);
  if (!questionCache[path]) {
    try {
      const response = await fetch(path);
      if (!response.ok) return [];
      questionCache[path] = await response.json();
    } catch { return []; }
  }
  return questionCache[path].map(q => questionFromJSON(q, examId, actualSubjectId, actualTopicId, lang));
}

export async function loadExamQuestions(examId: string, lang: 'en' | 'hi' = 'en'): Promise<Question[]> {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return [];
  const all: Question[] = [];
  for (const subject of exam.subjects)
    for (const topic of subject.topics)
      all.push(...await loadTopicQuestions(examId, subject.id, topic.id, lang));
  return all;
}

export async function loadSubjectQuestions(examId: string, subjectId: string, lang: 'en' | 'hi' = 'en'): Promise<Question[]> {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return [];
  const subject = exam.subjects.find(s => s.id === subjectId);
  if (!subject) return [];
  const all: Question[] = [];
  for (const topic of subject.topics)
    all.push(...await loadTopicQuestions(examId, subjectId, topic.id, lang));
  return all;
}

// =========== SET-BASED LOADING ===========

async function loadSetsIndex(): Promise<Record<string, string[][]>> {
  if (!setIndexCache['topics']) {
    const res = await fetch('/data/sets/topics.json');
    setIndexCache['topics'] = await res.json();
  }
  return setIndexCache['topics'];
}

async function loadMockIndex(examId: string): Promise<any[]> {
  const key = `mocks-${examId}`;
  if (!setIndexCache[key]) {
    const res = await fetch(`/data/sets/mocks/${examId}.json`);
    setIndexCache[key] = await res.json();
  }
  return setIndexCache[key];
}

export async function getTopicSetCount(examId: string, topicId: string): Promise<number> {
  const sets = await loadSetsIndex();
  const info = getSubjectForTopic(examId, topicId);
  if (!info) return 0;
  const topicSlug = getTopicSlug(examId, topicId);
  const topicKey = `${examId}-${getSubjectSlug(examId, info.subjectId)}-${topicSlug}`;
  return (sets[topicKey] || []).length;
}

export async function loadTopicSet(examId: string, topicId: string, setIndex: number, lang: 'en' | 'hi' = 'en'): Promise<Question[]> {
  const sets = await loadSetsIndex();
  const info = getSubjectForTopic(examId, topicId);
  if (!info) return [];
  const topicKey = `${examId}-${getSubjectSlug(examId, info.subjectId)}-${getTopicSlug(examId, topicId)}`;
  const topicSets = sets[topicKey];
  if (!topicSets || setIndex >= topicSets.length) return [];
  
  // Questions are stored inline in the sets now
  const rawQuestions = topicSets[setIndex];
  return rawQuestions.map((q: any) => {
    if (typeof q === 'string') return null; // Legacy string ID (shouldn't happen)
    return questionFromJSON(q, examId, info.subjectId, topicId, lang);
  }).filter(Boolean) as Question[];
}

export async function loadMockPaper(examId: string, paperIndex: number, lang: 'en' | 'hi' = 'en'): Promise<Question[]> {
  const papers = await loadMockIndex(examId);
  if (!papers || paperIndex >= papers.length) return [];
  
  const paper = papers[paperIndex];
  const rawQuestions = paper.questionOrder;
  
  // Questions are stored inline — derive subject/topic from the first one or just use empty
  return rawQuestions.map((q: any) => {
    if (typeof q === 'string') return null;
    return questionFromJSON(q, examId, examId, examId, lang);
  }).filter(Boolean) as Question[];
}

export async function getMockPaperCount(examId: string): Promise<number> {
  return (await loadMockIndex(examId)).length;
}
