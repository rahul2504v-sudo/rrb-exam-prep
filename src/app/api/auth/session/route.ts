
import { NextResponse } from 'next/server'
import { jwtVerify } from 'jose'

const SECRET = new TextEncoder().encode(process.env.NEXTAUTH_SECRET || 'prepXcore-dev-secret-2026')

export async function GET(request: Request) {
  const cookie = request.headers.get('cookie') || ''
  const match = cookie.match(/session=([^;]+)/)
  if (!match) return NextResponse.json({ user: null })
  
  try {
    const { payload } = await jwtVerify(match[1], SECRET)
    return NextResponse.json({ user: { email: payload.email, name: payload.name } })
  } catch {
    return NextResponse.json({ user: null })
  }
}
