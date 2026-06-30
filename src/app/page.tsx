'use client';

import Link from 'next/link';
import { examList } from '@/data/exams';
import { Train, Wrench, Clock, BookOpen, Trophy, BarChart3 } from 'lucide-react';
import { useLanguage } from '@/lib/LanguageContext';

const examIcons: Record<string, React.ReactNode> = {
  Train: <Train className="w-8 h-8" />,
  Wrench: <Wrench className="w-8 h-8" />,
};

export default function HomePage() {
  const { t } = useLanguage();

  return (
    <div>
      <section className="bg-gradient-to-br from-rail-navy via-blue-900 to-indigo-900 text-white py-20">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">{t('heroTitle')}</h1>
          <p className="text-xl text-blue-200 mb-2">{t('heroSubtitle')}</p>
          <p className="text-lg text-blue-300 max-w-2xl mx-auto mb-8">{t('heroDesc')}</p>
          <div className="flex flex-wrap justify-center gap-4 text-sm">
            <span className="bg-white/10 rounded-full px-4 py-2">{t('tagQuestions')}</span>
            <span className="bg-white/10 rounded-full px-4 py-2">{t('tagMocks')}</span>
            <span className="bg-white/10 rounded-full px-4 py-2">{t('tagSolutions')}</span>
            <span className="bg-white/10 rounded-full px-4 py-2">{t('tagProgress')}</span>
          </div>
        </div>
      </section>

      <section className="max-w-6xl mx-auto px-4 -mt-10 relative z-10">
        <div className="grid md:grid-cols-2 gap-6">
          {examList.map((exam) => (
            <Link key={exam.id} href={`/exam/${exam.slug}`}
              className="card group cursor-pointer hover:border-rail-navy/30">
              <div className="flex items-start gap-4">
                <div className="p-3 rounded-xl text-white"
                     style={{ backgroundColor: exam.color === 'rail-navy' ? '#1a237e' : '#d32f2f' }}>
                  {examIcons[exam.icon] || <BookOpen className="w-8 h-8" />}
                </div>
                <div className="flex-1">
                  <h2 className="text-xl font-bold text-gray-900 group-hover:text-rail-navy transition-colors">
                    {exam.name}
                  </h2>
                  <p className="text-gray-600 mt-1">{exam.description}</p>
                  <div className="flex flex-wrap gap-3 mt-4">
                    <span className="text-xs bg-blue-50 text-blue-700 px-3 py-1 rounded-full font-medium">
                      {exam.totalVacancies.toLocaleString()} {t('vacancies')}
                    </span>
                    <span className="text-xs bg-green-50 text-green-700 px-3 py-1 rounded-full font-medium">
                      {exam.pattern.totalQuestions} {t('questions')}
                    </span>
                    <span className="text-xs bg-orange-50 text-orange-700 px-3 py-1 rounded-full font-medium">
                      {exam.pattern.durationMinutes} {t('minutes')}
                    </span>
                  </div>
                  <div className="mt-4 flex items-center text-sm text-rail-navy font-semibold">
                    {t('startPracticing')}
                  </div>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </section>

      <section className="max-w-6xl mx-auto px-4 py-16">
        <h2 className="text-2xl font-bold text-center mb-10">{t('whyPractice')}</h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            { icon: Clock, title: t('featureTimer'), desc: t('featureTimerDesc') },
            { icon: BookOpen, title: t('featureTopic'), desc: t('featureTopicDesc') },
            { icon: Trophy, title: t('featureResults'), desc: t('featureResultsDesc') },
            { icon: BarChart3, title: t('featureTrack'), desc: t('featureTrackDesc') },
          ].map((feature, i) => (
            <div key={i} className="card text-center">
              <div className="inline-flex p-3 rounded-xl bg-blue-50 text-rail-navy mb-4">
                <feature.icon className="w-6 h-6" />
              </div>
              <h3 className="font-semibold text-gray-900 mb-2">{feature.title}</h3>
              <p className="text-sm text-gray-600">{feature.desc}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="bg-gray-100 py-12">
        <div className="max-w-6xl mx-auto px-4">
          <div className="grid grid-cols-3 gap-8 text-center">
            <div>
              <div className="text-3xl font-bold text-rail-navy">{t('tagQuestions')}</div>
              <div className="text-sm text-gray-600 mt-1">{t('statQuestions')}</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-rail-navy">7</div>
              <div className="text-sm text-gray-600 mt-1">{t('statSubjects')}</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-rail-navy">2</div>
              <div className="text-sm text-gray-600 mt-1">{t('statExams')}</div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
