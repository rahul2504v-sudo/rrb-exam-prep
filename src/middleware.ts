import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const pathname = request.nextUrl.pathname
  
  // Allow public routes
  if (pathname === '/' || pathname === '/login' || pathname.startsWith('/api/') ||
      pathname.startsWith('/_next') || pathname.startsWith('/data/') ||
      pathname.startsWith('/favicon') || pathname.startsWith('/manifest')) {
    return NextResponse.next()
  }
  
  // Check session cookie
  if (!request.cookies.has('session')) {
    const url = request.nextUrl.clone()
    url.pathname = '/login'
    url.searchParams.set('callbackUrl', pathname)
    return NextResponse.redirect(url)
  }
  
  return NextResponse.next()
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.svg|icon-.*\\.svg).*)'],
}
