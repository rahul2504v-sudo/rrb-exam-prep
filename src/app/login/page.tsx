'use client'

import { useState, Suspense } from 'react'
import { useSearchParams } from 'next/navigation'
import Link from 'next/link'
import { BookOpen, Mail, Lock, Eye, EyeOff, ArrowRight } from 'lucide-react'

function LoginForm() {
  const searchParams = useSearchParams()
  const callbackUrl = searchParams.get('callbackUrl') || '/exam/ntpc'
  
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    
    if (!email.includes('@')) {
      setError('Please enter a valid email address')
      return
    }
    if (password.length < 3) {
      setError('Password must be at least 3 characters')
      return
    }
    
    setLoading(true)
    
    // Submit form directly to NextAuth callback — this sets cookies via redirect
    const form = document.createElement('form')
    form.method = 'POST'
    form.action = '/api/auth/callback/credentials'
    
    // Get CSRF token
    const csrfRes = await fetch('/api/auth/csrf')
    const { csrfToken } = await csrfRes.json()
    
    const fields = [
      ['csrfToken', csrfToken],
      ['email', email],
      ['password', password],
      ['callbackUrl', callbackUrl],
      ['json', 'true'],
    ]
    
    fields.forEach(([name, value]) => {
      const input = document.createElement('input')
      input.type = 'hidden'
      input.name = name
      input.value = value
      form.appendChild(input)
    })
    
    document.body.appendChild(form)
    form.submit()
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-50 via-white to-purple-50">
        <div className="text-center">
          <div className="animate-spin w-10 h-10 border-4 border-indigo-600 border-t-transparent rounded-full mx-auto mb-4" />
          <p className="text-gray-500">Signing you in...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-50 via-white to-purple-50 px-4">
      <div className="w-full max-w-md">
        <div className="text-center mb-8">
          <Link href="/" className="inline-flex items-center gap-2">
            <BookOpen className="w-8 h-8 text-indigo-600" />
            <span className="text-2xl font-bold text-gray-900">prepXcore</span>
          </Link>
          <p className="text-gray-500 mt-2">Sign in to start practicing</p>
        </div>

        <div className="bg-white rounded-2xl shadow-xl border border-gray-100 p-8">
          <h2 className="text-xl font-bold text-gray-900 mb-1">Welcome</h2>
          <p className="text-sm text-gray-500 mb-6">Enter your email to continue</p>

          {error && (
            <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-sm text-red-700">
              {error}
            </div>
          )}

          <form onSubmit={handleLogin} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
              <div className="relative">
                <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-sm"
                  placeholder="you@example.com"
                  autoFocus
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Password</label>
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                <input
                  type={showPassword ? 'text' : 'password'}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full pl-10 pr-10 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-sm"
                  placeholder="Enter any password"
                  required
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3 top-1/2 -translate-y-1/2"
                >
                  {showPassword ? <EyeOff className="w-4 h-4 text-gray-400" /> : <Eye className="w-4 h-4 text-gray-400" />}
                </button>
              </div>
            </div>

            <button
              type="submit"
              className="w-full py-3 bg-indigo-600 text-white rounded-xl hover:bg-indigo-700 font-medium text-sm transition-colors flex items-center justify-center gap-2"
            >
              Continue <ArrowRight className="w-4 h-4" />
            </button>
          </form>

          <p className="mt-6 text-center text-xs text-gray-400">
            New here? Just enter any email and password — we'll create your account automatically.
          </p>
        </div>

        <p className="mt-4 text-center text-[11px] text-gray-400">
          By continuing, you agree to prepXcore's terms of use.
        </p>
      </div>
    </div>
  )
}

export default function LoginPage() {
  return (
    <Suspense fallback={
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin w-8 h-8 border-4 border-indigo-600 border-t-transparent rounded-full" />
      </div>
    }>
      <LoginForm />
    </Suspense>
  )
}
