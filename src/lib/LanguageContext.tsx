'use client';

import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { translations, TranslationKey } from '@/lib/translations';
import { DEFAULT_LANGUAGE, RRB_LANGUAGES } from '@/lib/languages';

type LanguageContextType = {
  language: string;
  setLanguage: (code: string) => void;
  t: (key: TranslationKey) => string;
  languages: typeof RRB_LANGUAGES;
};

const LanguageContext = createContext<LanguageContextType>({
  language: DEFAULT_LANGUAGE,
  setLanguage: () => {},
  t: (key) => key,
  languages: RRB_LANGUAGES,
});

export function LanguageProvider({ children }: { children: ReactNode }) {
  const [language, setLanguageState] = useState(DEFAULT_LANGUAGE);

  useEffect(() => {
    const saved = localStorage.getItem('rrb-language');
    if (saved && RRB_LANGUAGES.some(l => l.code === saved)) {
      setLanguageState(saved);
    }
  }, []);

  const setLanguage = (code: string) => {
    setLanguageState(code);
    localStorage.setItem('rrb-language', code);
    document.documentElement.lang = code;
    if (code === 'ur') {
      document.documentElement.dir = 'rtl';
    } else {
      document.documentElement.dir = 'ltr';
    }
  };

  const t = (key: TranslationKey): string => {
    return translations[language]?.[key] || translations.en?.[key] || key;
  };

  return (
    <LanguageContext.Provider value={{ language, setLanguage, t, languages: RRB_LANGUAGES }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  return useContext(LanguageContext);
}
