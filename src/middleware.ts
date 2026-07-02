import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl
  const pp = ['/', '/login', '/api/auth', '/api/payment']
  if (pp.some(p => pathname.startsWith(p))) return NextResponse.next()
  if (pathname.startsWith('/_next') || pathname.startsWith('/data/') ||
      pathname.startsWith('/favicon') || pathname.startsWith('/icon') ||
      pathname.startsWith('/manifest') || pathname.startsWith('/sw.js')) return NextResponse.next()
  const token = request.cookies.get('session')?.value
  if (!token) {
    const u = new URL('/login', request.url)
    u.searchParams.set('callbackUrl', pathname)
    return NextResponse.redirect(u)
  }
  return NextResponse.next()
}
export const config = { matcher: ['/((?!_next/static|_next/image|favicon.svg|icon-.*\.svg).*)'] }
