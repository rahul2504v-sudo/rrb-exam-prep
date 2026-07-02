// Purchase tracking — localStorage scoped by user email
const BASE_KEY = 'prepxcore-purchases';

function getUserEmail(): string {
  if (typeof window === 'undefined') return 'anonymous';
  const match = document.cookie.match(/session=([^;]+)/);
  if (!match) return 'anonymous';
  try {
    return JSON.parse(atob(match[1].split('.')[1])).email || 'anonymous';
  } catch { return 'anonymous'; }
}

export function getPurchasedExams(): string[] {
  if (typeof window === 'undefined') return [];
  try {
    const data = localStorage.getItem(`${BASE_KEY}-${getUserEmail()}`);
    return data ? JSON.parse(data) : [];
  } catch { return []; }
}

export function purchaseExam(examId: string): void {
  if (typeof window === 'undefined') return;
  const exams = getPurchasedExams();
  if (!exams.includes(examId)) {
    exams.push(examId);
    localStorage.setItem(`${BASE_KEY}-${getUserEmail()}`, JSON.stringify(exams));
  }
}

export function hasPurchased(examId: string): boolean {
  return getPurchasedExams().includes(examId);
}

export function getAllPurchased(): string[] {
  return getPurchasedExams();
}
