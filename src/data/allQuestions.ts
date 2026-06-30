export { examList } from './exams';
export { ntpcMathQuestions } from './questions/ntpc-math';
export { ntpcReasoningQuestions } from './questions/ntpc-reasoning';
export { ntpcGAQuestions } from './questions/ntpc-ga';
export { groupDMathQuestions } from './questions/groupd-math';
export { groupDScienceQuestions } from './questions/groupd-science';
export { groupDReasoningQuestions } from './questions/groupd-reasoning';
export { groupDGAQuestions } from './questions/groupd-ga';

import { Question } from '@/types';
import { ntpcMathQuestions } from './questions/ntpc-math';
import { ntpcReasoningQuestions } from './questions/ntpc-reasoning';
import { ntpcGAQuestions } from './questions/ntpc-ga';
import { groupDMathQuestions } from './questions/groupd-math';
import { groupDScienceQuestions } from './questions/groupd-science';
import { groupDReasoningQuestions } from './questions/groupd-reasoning';
import { groupDGAQuestions } from './questions/groupd-ga';

export const allQuestions: Record<string, Question[]> = {
  'ntpc-mathematics': ntpcMathQuestions,
  'ntpc-reasoning': ntpcReasoningQuestions,
  'ntpc-general-awareness': ntpcGAQuestions,
  'group-d-mathematics': groupDMathQuestions,
  'group-d-science': groupDScienceQuestions,
  'group-d-reasoning': groupDReasoningQuestions,
  'group-d-general-awareness': groupDGAQuestions,
};

export function getQuestionsByExam(examId: string): Question[] {
  const prefix = examId + '-';
  const subjects = Object.keys(allQuestions).filter(k => k.startsWith(prefix));
  return subjects.flatMap(s => allQuestions[s] || []);
}

export function getQuestionsByTopic(examId: string, topicId: string): Question[] {
  const questions = getQuestionsByExam(examId);
  // Exact match first
  let results = questions.filter(q => q.topicId === topicId);
  if (results.length > 0) return results;
  // Try prefix match: question topicId starts with search topicId (e.g. 'group-d-science-physics' matches 'group-d-science-physics-motion')
  results = questions.filter(q => q.topicId.startsWith(topicId));
  if (results.length > 0) return results;
  // Try reverse prefix: search topicId starts with question topicId
  results = questions.filter(q => topicId.startsWith(q.topicId));
  return results;
}

export function getQuestionsBySubject(examId: string, subjectId: string): Question[] {
  return allQuestions[subjectId] || [];
}
