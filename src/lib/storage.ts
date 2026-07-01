import { TestSession } from '@/types';

const BASE_KEY = 'prepxcore-sessions';

function getUserEmail(): string | null {
  if (typeof window === 'undefined') return null;
  const match = document.cookie.match(/session=([^;]+)/);
  if (!match) return null;
  try {
    const payload = JSON.parse(atob(match[1].split('.')[1]));
    return payload.email || null;
  } catch { return null; }
}

export function getStorageKey(): string {
  const email = getUserEmail();
  return email ? `${BASE_KEY}-${email}` : BASE_KEY;
}

export function getSessions(): TestSession[] {
  if (typeof window === 'undefined') return [];
  try {
    const data = localStorage.getItem(getStorageKey());
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
    localStorage.setItem(getStorageKey(), JSON.stringify(sessions.slice(0, 100)));
  } catch {}
}

export function getSession(id: string): TestSession | undefined {
  return getSessions().find(s => s.id === id);
}

export function clearAllSessions(): void {
  if (typeof window === 'undefined') return;
  localStorage.removeItem(getStorageKey());
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
