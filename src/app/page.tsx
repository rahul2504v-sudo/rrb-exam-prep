'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { examList } from '@/data/exams';
import { BookOpen, Clock, Layers, ArrowRight, ChevronDown, Megaphone, Calendar, ExternalLink, Lock, Check, Zap } from 'lucide-react';
import { getPurchasedExams, purchaseExam } from '@/lib/purchases';

export default function HomePage() {
  const [openExam, setOpenExam] = useState<string | null>(null);
  const [purchased, setPurchased] = useState<string[]>([]);
  const [showPurchase, setShowPurchase] = useState<string | null>(null);
  const [paying, setPaying] = useState(false);
  const [bulletin, setBulletin] = useState<any[]>([]);

  useEffect(() => {
    setPurchased(getPurchasedExams());
    fetch('/data/bulletin.json').then(r => r.json()).then(setBulletin).catch(() => {});
  }, []);

  const displayBulletin = bulletin.length > 0 ? bulletin : [
    { name: 'RRB ALP CBT 2', date: 'July 28, 2026', vacancies: '11,127', status: 'Ongoing' },
    { name: 'RRB NTPC CBT 2 (UG)', date: 'September 17, 2026', vacancies: '3,058', status: 'Upcoming' },
    { name: 'RRB Technician 2026-27', date: 'Notification Out', vacancies: '6,557', status: 'Notified' },
    { name: 'SSC CGL Tier 2', date: 'October 2026', vacancies: '~8,000', status: 'Upcoming' },
    { name: 'RRB Group D (New)', date: 'Notification Expected', vacancies: '22,082', status: 'Expected' },
  ];

  const handleBuy = async (examId: string) => {
    setPaying(true);
    try {
      const res = await fetch('/api/payment/create-order', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ examId }),
      });
      const order = await res.json();
      if (order.error) { alert(order.error); setPaying(false); return; }

      const script = document.createElement('script');
      script.src = 'https://checkout.razorpay.com/v1/checkout.js';
      script.onload = () => {
        const rzp = new (window as any).Razorpay({
          key: order.key,
          amount: order.amount,
          currency: 'INR',
          name: 'prepXcore',
          description: `Full access to ${examList.find(e => e.id === examId)?.name}`,
          order_id: order.orderId,
          handler: async function(response: any) {
            const vRes = await fetch('/api/payment/verify', {
              method: 'POST', headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(response),
            });
            if ((await vRes.json()).verified) {
              purchaseExam(examId);
              setPurchased(getPurchasedExams());
              setShowPurchase(null);
            }
          },
          theme: { color: '#4f46e5' },
        });
        rzp.open();
        setPaying(false);
      };
      document.body.appendChild(script);
    } catch { setPaying(false); }
  };

  const isOwned = (id: string) => purchased.includes(id);

  return (
    <div>
      {/* Hero */}
      <section className="relative overflow-hidden bg-gradient-to-br from-indigo-600 via-indigo-700 to-purple-800 text-white">
        <div className="max-w-6xl mx-auto px-4 py-20 text-center relative z-10">
          <h1 className="text-4xl sm:text-5xl font-extrabold tracking-tight mb-4">
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-white to-indigo-200">prepXcore</span>
          </h1>
          <p className="text-xl sm:text-2xl text-indigo-100 font-light mb-3">
            India's Smartest Exam Preparation Platform
          </p>
          <p className="text-indigo-200/80 max-w-xl mx-auto">
            10,000+ questions, full-length mocks, detailed analytics. Practice for RRB NTPC, ALP, Technician, Group D & more.
          </p>
          <div className="flex flex-wrap justify-center gap-3 mt-8">
            <Link href="#exams" className="px-6 py-3 bg-white text-indigo-700 font-semibold rounded-xl hover:bg-indigo-50 transition-all shadow-lg hover:shadow-xl">
              View Exams →
            </Link>
          </div>
        </div>
      </section>

      {/* Available Exams */}
      <section id="exams" className="max-w-6xl mx-auto px-4 py-16">
        <div className="grid lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <h2 className="text-3xl font-bold text-gray-900 mb-6">Available Exams</h2>
            
            <div className="space-y-4">
              {examList.map(exam => {
                const owned = isOwned(exam.id);
                return (
                  <div key={exam.id} className={`border rounded-2xl overflow-hidden transition-all ${owned ? 'border-green-300 bg-green-50/30' : 'border-gray-200 hover:border-indigo-300'}`}>
                    <button onClick={() => setOpenExam(openExam === exam.id ? null : exam.id)}
                      className="w-full flex items-center justify-between p-5 hover:bg-gray-50 transition-colors">
                      <div className="flex items-center gap-4">
                        <div className={`w-12 h-12 rounded-xl flex items-center justify-center text-xl ${exam.id === 'ntpc' ? 'bg-blue-100' : 'bg-green-100'}`}>
                          {exam.id === 'ntpc' ? '🚂' : exam.id === 'alp' ? '🚂' : '🔧'}
                        </div>
                        <div className="text-left">
                          <h3 className="font-bold text-lg text-gray-900">
                            {exam.name}
                            {exam.status && (
                              <span className={`ml-2 text-[10px] px-2 py-0.5 rounded-full font-medium ${
                                exam.status === 'ongoing' ? 'bg-green-100 text-green-700' :
                                exam.status === 'upcoming' ? 'bg-amber-100 text-amber-700' :
                                exam.status === 'notified' ? 'bg-blue-100 text-blue-700' : 'bg-gray-100 text-gray-600'
                              }`}>
                                {exam.status === 'ongoing' ? 'Active' : exam.status === 'notified' ? 'New' : 'Upcoming'}
                              </span>
                            )}
                            {owned && <span className="ml-2 text-[10px] px-2 py-0.5 rounded-full bg-green-100 text-green-700 font-medium">✓ Purchased</span>}
                          </h3>
                          <p className="text-sm text-gray-500">{exam.description}</p>
                        </div>
                      </div>
                      <div className="flex items-center gap-3">
                        <span className="hidden sm:inline text-xs bg-blue-50 text-blue-700 px-2 py-1 rounded-full">{exam.totalVacancies.toLocaleString()} Posts</span>
                        <span className="hidden sm:inline text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-full">{exam.pattern.totalQuestions} Qs</span>
                        {/* Price */}
                        <span className="flex items-center gap-1">
                          <span className="text-sm font-bold text-green-700">₹99</span>
                          <span className="text-xs text-gray-400 line-through">₹749</span>
                        </span>
                        <ChevronDown className={`w-5 h-5 text-gray-400 transition-transform ${openExam === exam.id ? 'rotate-180' : ''}`} />
                      </div>
                    </button>
                    
                    {openExam === exam.id && (
                      <div className="border-t border-gray-100 p-5 bg-gray-50/50">
                        <div className="grid sm:grid-cols-4 gap-4 mb-4">
                          {exam.pattern.sections.map((sec, i) => (
                            <div key={i} className="bg-white rounded-xl p-3 border border-gray-100 text-center">
                              <div className="text-lg font-bold text-indigo-600">{sec.questionCount}</div>
                              <div className="text-xs text-gray-500">{sec.name}</div>
                            </div>
                          ))}
                        </div>
                        <div className="text-sm text-gray-500 mb-3">
                          <Clock className="w-4 h-4 inline mr-1" />{exam.pattern.durationMinutes} min · -1/3 negative marking
                        </div>
                        
                        {owned ? (
                          <div className="flex gap-3">
                            <Link href={`/exam/${exam.slug}`} className="px-4 py-2 bg-green-600 text-white rounded-lg text-sm font-medium hover:bg-green-700">
                              Go to Dashboard →
                            </Link>
                          </div>
                        ) : showPurchase === exam.id ? (
                          <div className="bg-white rounded-xl border border-indigo-200 p-4">
                            <div className="flex items-start justify-between mb-3">
                              <div>
                                <h4 className="font-bold text-gray-900">{exam.name} — Complete Access</h4>
                                <ul className="text-xs text-gray-500 mt-1 space-y-0.5">
                                  <li>✓ {exam.pattern.totalQuestions}+ practice questions</li>
                                  <li>✓ 10,000+ topic-wise question bank</li>
                                  <li>✓ 20 full-length mock tests</li>
                                  <li>✓ Detailed analytics & performance tracking</li>
                                  <li>✓ Bilingual (English + Hindi)</li>
                                </ul>
                              </div>
                              <div className="text-right flex-shrink-0 ml-4">
                                <div className="text-xs text-red-500 font-medium uppercase">Limited Time</div>
                                <div className="text-2xl font-bold text-green-700">₹99</div>
                                <div className="text-sm text-gray-400 line-through">₹749</div>
                                <div className="text-[10px] text-gray-400">87% off</div>
                              </div>
                            </div>
                            <div className="flex gap-2">
                              <button onClick={() => handleBuy(exam.id)} disabled={paying}
                                className="flex-1 px-4 py-2.5 bg-indigo-600 text-white rounded-lg text-sm font-bold hover:bg-indigo-700 disabled:opacity-50 flex items-center justify-center gap-2">
                                {paying ? 'Processing...' : <>Buy Now <Lock className="w-4 h-4" /></>}
                              </button>
                              <button onClick={() => setShowPurchase(null)}
                                className="px-4 py-2.5 border text-gray-600 rounded-lg text-sm hover:bg-gray-50">Cancel</button>
                            </div>
                          </div>
                        ) : (
                          <div className="flex gap-3 items-center">
                            <button onClick={() => setShowPurchase(exam.id)}
                              className="px-4 py-2 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-lg text-sm font-medium hover:shadow-lg flex items-center gap-2">
                              <Zap className="w-4 h-4" /> Get Access at ₹99
                            </button>
                            <span className="text-xs text-gray-400">Limited time deal</span>
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>

          {/* Bulletin Side Panel */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-2xl shadow-lg border border-gray-200 p-5 sticky top-24">
              <div className="flex items-center gap-2 mb-4">
                <Megaphone className="w-5 h-5 text-amber-600" />
                <h2 className="text-lg font-bold text-gray-900">Exam Bulletin</h2>
              </div>
              <div className="space-y-3">
                {displayBulletin.map((item: any, i: number) => (
                  <a key={i} href={item.url || '#'} target={item.url ? '_blank' : undefined} rel="noopener"
                    className="flex items-start gap-3 p-3 rounded-xl border border-gray-100 hover:border-amber-200 hover:bg-amber-50/50 transition-all group">
                    <div className={`w-2 h-2 rounded-full mt-1.5 flex-shrink-0 ${
                      item.status === 'Ongoing' ? 'bg-green-500' : item.status === 'Upcoming' ? 'bg-amber-500' : 'bg-blue-500'
                    }`} />
                    <div className="min-w-0 flex-1">
                      <p className="text-sm font-medium text-gray-800 truncate">{item.name}</p>
                      <div className="flex items-center gap-2 mt-1">
                        <span className="text-xs text-gray-400 flex items-center gap-1"><Calendar className="w-3 h-3" />{item.date}</span>
                        {item.vacancies && <span className="text-xs text-gray-400">{item.vacancies} posts</span>}
                      </div>
                    </div>
                  </a>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="bg-indigo-600 text-white py-12">
        <div className="max-w-5xl mx-auto px-4 grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
          {[['10,000+', 'Questions'], ['1,400+', 'Topic Sets'], ['80', 'Mock Papers'], ['15', 'Languages']].map(([val, label], i) => (
            <div key={i}>
              <div className="text-2xl font-bold">{val}</div>
              <div className="text-indigo-200 text-sm">{label}</div>
            </div>
          ))}
        </div>
      </section>

      <footer className="bg-gray-900 text-gray-400 text-xs text-center py-8">
        <div className="max-w-6xl mx-auto px-4">
          <span className="font-bold text-white">prepXcore</span> — Competitive Exam Preparation Platform
          <div className="mt-2">© 2026 prepXcore. All rights reserved.</div>
        </div>
      </footer>
    </div>
  );
}
