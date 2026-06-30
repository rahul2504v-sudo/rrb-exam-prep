'use client';

import { useState, useRef, useEffect } from 'react';
import { useLanguage } from '@/lib/LanguageContext';
import { Globe } from 'lucide-react';

export function LanguageSwitcher() {
  const { language, setLanguage, languages } = useLanguage();
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const currentLang = languages.find(l => l.code === language);

  return (
    <div ref={ref} className="relative">
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center gap-1.5 px-2.5 py-2 rounded-lg text-sm font-medium 
                   text-gray-600 hover:text-gray-900 hover:bg-gray-50 transition-colors"
        title="Change language"
      >
        <Globe className="w-4 h-4" />
        <span className="hidden sm:inline">{currentLang?.nativeName || currentLang?.name}</span>
      </button>

      {open && (
        <div className="absolute right-0 top-full mt-1 w-56 bg-white rounded-xl shadow-lg border border-gray-200 
                        max-h-80 overflow-y-auto z-50">
          <div className="p-1.5">
            {languages.map((lang) => (
              <button
                key={lang.code}
                onClick={() => { setLanguage(lang.code); setOpen(false); }}
                className={`w-full flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm transition-colors
                  ${language === lang.code 
                    ? 'bg-blue-50 text-rail-navy font-semibold' 
                    : 'text-gray-700 hover:bg-gray-50'}`}
              >
                <span className="text-base">{lang.flag}</span>
                <span className="flex-1 text-left">
                  {lang.nativeName}
                  {lang.code !== 'en' && lang.code !== 'hi' && (
                    <span className="text-gray-400 ml-1">({lang.name})</span>
                  )}
                </span>
                {language === lang.code && (
                  <span className="text-rail-navy text-xs">✓</span>
                )}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
