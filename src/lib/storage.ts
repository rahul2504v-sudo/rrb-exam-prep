import { TestSession } from '@/types';

const STORAGE_KEY = 'rrb-exam-prep-sessions';

export function getSessions(): TestSession[] {
  if (typeof window === 'undefined') return [];
  try {
    const data = localStorage.getItem(STORAGE_KEY);
    return data ? JSON.parse(data) : [];
  } catch {
    return [];
  }
}

export function saveSession(session: TestSession): void {
  if (typeof window === 'undefined') return;
  const sessions = getSessions();
  const existingIndex = sessions.findIndex(s => s.id === session.id);
  if (existingIndex >= 0) {
    sessions[existingIndex] = session;
  } else {
    sessions.unshift(session);
  }
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(sessions.slice(0, 100)));
  } catch {
    // Storage full or unavailable
  }
}

export function getSession(id: string): TestSession | undefined {
  return getSessions().find(s => s.id === id);
}

export function clearAllSessions(): void {
  if (typeof window === 'undefined') return;
  localStorage.removeItem(STORAGE_KEY);
}

export function getAverageScore(): number {
  const sessions = getSessions();
  if (sessions.length === 0) return 0;
  const total = sessions.reduce((sum, s) => sum + s.score, 0);
  return Math.round((total / sessions.length) * 100) / 100;
}

export function getBestScore(): number {
  const sessions = getSessions();
  if (sessions.length === 0) return 0;
  return Math.max(...sessions.map(s => s.score));
}
