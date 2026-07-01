import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { getToken } from 'next-auth/jwt'

export async function middleware(request: NextRequest) {
  const token = await getToken({ 
    req: request,
    secret: process.env.NEXTAUTH_SECRET || 'prepXcore-dev-secret-change-in-production'
  })
  
  const { pathname } = request.nextUrl
  
  // Public routes — no auth required
  const publicPaths = ['/', '/login', '/api/auth']
  if (publicPaths.some(p => pathname === p || pathname.startsWith(p + '/'))) {
    return NextResponse.next()
  }
  
  // Allow static assets
  if (pathname.startsWith('/_next') || pathname.startsWith('/data/') || 
      pathname.startsWith('/favicon') || pathname.startsWith('/icon') ||
      pathname.startsWith('/manifest') || pathname.startsWith('/sw.js')) {
    return NextResponse.next()
  }
  
  // Require auth for everything else (exam pages, quiz pages, results)
  if (!token) {
    const loginUrl = new URL('/login', request.url)
    loginUrl.searchParams.set('callbackUrl', pathname)
    return NextResponse.redirect(loginUrl)
  }
  
  return NextResponse.next()
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.svg|icon-.*\\.svg).*)'],
}
