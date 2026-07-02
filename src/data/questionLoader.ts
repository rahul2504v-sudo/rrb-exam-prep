import { Question, QuestionJSON, questionFromJSON } from '@/types';
import { examList } from './exams';

const questionCache: Record<string, QuestionJSON[]> = {};
const setIndexCache: Record<string, any> = {};

function getSubjectExamDir(subjectId: string): string {
  if (subjectId.startsWith('ntpc-')) return 'ntpc';
  if (subjectId.startsWith('group-d-')) return 'group-d';
  if (subjectId.startsWith('tech-')) return subjectId.split('-').slice(0, 2).join('-');
  if (subjectId.startsWith('basic-science')) return 'basic-science-engineering';
  if (subjectId.startsWith('computers')) return 'computers-applications';
  return subjectId.split('-')[0];
}

function getSubjectSlug(examId: string, subjectId: string): string {
  const exam = examList.find(e => e.id === examId);
  return exam?.subjects.find(s => s.id === subjectId)?.slug || '';
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

export async function loadTopicQuestions(examId: string, subjectIdOrTopicId: string, topicId?: string, lang: 'en' | 'hi' = 'en'): Promise<Question[]> {
  let sid: string, tid: string;
  if (topicId && topicId.length > 2) { sid = subjectIdOrTopicId; tid = topicId; }
  else {
    const info = getSubjectForTopic(examId, subjectIdOrTopicId);
    if (!info) return []; tid = subjectIdOrTopicId; sid = info.subjectId;
  }
  const dir = getSubjectExamDir(sid);
  const path = `/data/questions/${dir}/${getSubjectSlug(examId, sid)}/${getTopicSlug(examId, tid)}.json`;
  if (!questionCache[path]) {
    try { const r = await fetch(path); if (!r.ok) return []; questionCache[path] = await r.json(); }
    catch { return []; }
  }
  return questionCache[path].map(q => questionFromJSON(q, examId, sid, tid, lang));
}

export async function loadExamQuestions(examId: string, lang: 'en' | 'hi' = 'en'): Promise<Question[]> {
  const exam = examList.find(e => e.id === examId);
  if (!exam) return [];
  const all: Question[] = [];
  for (const s of exam.subjects) for (const t of s.topics) all.push(...await loadTopicQuestions(examId, s.id, t.id, lang));
  return all;
}

// SET-BASED LOADING
async function loadSetsIndex(): Promise<Record<string, string[][]>> {
  if (!setIndexCache['topics']) { const r = await fetch('/data/sets/topics.json'); setIndexCache['topics'] = await r.json(); }
  return setIndexCache['topics'];
}
async function loadMockIndex(examId: string): Promise<any[]> {
  const k = `mocks-${examId}`;
  if (!setIndexCache[k]) { const r = await fetch(`/data/sets/mocks/${examId}.json`); setIndexCache[k] = await r.json(); }
  return setIndexCache[k];
}

export async function getTopicSetCount(examId: string, topicId: string): Promise<number> {
  const sets = await loadSetsIndex();
  const info = getSubjectForTopic(examId, topicId);
  if (!info) return 0;
  const dir = getSubjectExamDir(info.subjectId);
  const subjSlug = getSubjectSlug(examId, info.subjectId);
  const topSlug = getTopicSlug(examId, topicId);
  // Key matches file path: {dir}-{subjSlug}-{topSlug} for 3-level, {dir}-{topSlug} for 2-level
  let key = `${dir}-${subjSlug}-${topSlug}`;
  // If 3-level key doesn't exist, try 2-level (consolidated file without subject dir)
  if (!sets[key]) {
    key = `${dir}-${topSlug}`;
  }
  return (sets[key] || []).length;
}

export async function loadTopicSet(examId: string, topicId: string, setIndex: number, lang: 'en' | 'hi' = 'en'): Promise<Question[]> {
  const sets = await loadSetsIndex();
  const info = getSubjectForTopic(examId, topicId);
  if (!info) return [];
  const dir = getSubjectExamDir(info.subjectId);
  const subjSlug = getSubjectSlug(examId, info.subjectId);
  const topSlug = getTopicSlug(examId, topicId);
  const key = dir === subjSlug ? `${dir}-${topSlug}` : `${dir}-${subjSlug}-${topSlug}`;
  let ts = sets[key];
  // Fallback to 2-level key if 3-level not found
  if (!ts) {
    ts = sets[`${dir}-${topSlug}`];
  }
  if (!ts || setIndex >= ts.length) return [];
  const raw = ts[setIndex];
  return raw.map((q: any) => typeof q === 'string' ? null : questionFromJSON(q, examId, info.subjectId, topicId, lang)).filter(Boolean) as Question[];
}

export async function loadMockPaper(examId: string, pi: number, lang: 'en' | 'hi' = 'en'): Promise<Question[]> {
  const papers = await loadMockIndex(examId);
  if (!papers || pi >= papers.length) return [];
  const raw = papers[pi].questionOrder;
  return raw.map((q: any) => typeof q === 'string' ? null : questionFromJSON(q, examId, examId, examId, lang)).filter(Boolean) as Question[];
}

export async function getMockPaperCount(examId: string): Promise<number> {
  return (await loadMockIndex(examId)).length;
}
