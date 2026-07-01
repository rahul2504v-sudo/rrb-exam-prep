import { NextResponse } from 'next/server'
import { SignJWT } from 'jose'

const SECRET = new TextEncoder().encode(
  process.env.NEXTAUTH_SECRET || 'prepXcore-dev-secret-2026'
)

export async function POST(request: Request) {
  const { email, password } = await request.json()
  
  if (!email || !email.includes('@') || !password || password.length < 3) {
    return NextResponse.json({ error: 'Invalid credentials' }, { status: 401 })
  }
  
  const token = await new SignJWT({ email, name: email.split('@')[0] })
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('30d')
    .sign(SECRET)
  
  const response = NextResponse.json({ ok: true, email })
  
  response.cookies.set('session', token, {
    httpOnly: true,
    secure: true,
    sameSite: 'lax',
    maxAge: 30 * 24 * 60 * 60,
    path: '/',
  })
  
  return response
}
