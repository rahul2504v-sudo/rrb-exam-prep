export { examList } from './exams';
export { loadTopicQuestions, loadExamQuestions, loadSubjectQuestions } from './questionLoader';

import { Question } from '@/types';
import { loadTopicQuestions, loadExamQuestions } from './questionLoader';

// Legacy sync wrappers that return empty — use async functions instead
// These exist only for backward compat; the quiz page uses async loading

// For the exam page topic counts, we use a different approach now
// The count is fetched async

import { examList } from './exams';

// Calculate approximate questions per topic based on JSON file existence
export function getEstimatedTopicCount(examId: string, topicId: string): number {
  // Returns 0 — actual count comes from JSON files
  return 0;
}
