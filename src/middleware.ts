import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { jwtVerify } from 'jose'

const SECRET = new TextEncoder().encode(
  process.env.NEXTAUTH_SECRET || 'prepXcore-dev-secret-2026'
)

export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl
  
  // Public routes
  const publicPaths = ['/', '/login', '/api/auth/login']
  if (publicPaths.some(p => pathname === p || pathname.startsWith(p + '/'))) {
    return NextResponse.next()
  }
  
  // Static assets
  if (pathname.startsWith('/_next') || pathname.startsWith('/data/') || 
      pathname.startsWith('/favicon') || pathname.startsWith('/icon') ||
      pathname.startsWith('/manifest') || pathname.startsWith('/sw.js')) {
    return NextResponse.next()
  }
  
  // Check session cookie
  const token = request.cookies.get('session')?.value
  
  if (!token) {
    const loginUrl = new URL('/login', request.url)
    loginUrl.searchParams.set('callbackUrl', pathname)
    return NextResponse.redirect(loginUrl)
  }
  
  // Verify JWT
  try {
    await jwtVerify(token, SECRET)
    return NextResponse.next()
  } catch {
    const loginUrl = new URL('/login', request.url)
    loginUrl.searchParams.set('callbackUrl', pathname)
    return NextResponse.redirect(loginUrl)
  }
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.svg|icon-.*\\.svg).*)'],
}
