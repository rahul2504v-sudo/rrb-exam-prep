import NextAuth from "next-auth"
import Google from "next-auth/providers/google"
import Apple from "next-auth/providers/apple"
import Credentials from "next-auth/providers/credentials"

// Simple user store (in production, use a database)
// For MVP, we store hashed passwords in a simple object
const users: Record<string, { email: string; password: string; name: string }> = {
  // Default test user
  "test@prepXcore.com": { email: "test@prepXcore.com", password: "test123", name: "Test User" }
}

export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [
    Google({
      clientId: process.env.GOOGLE_CLIENT_ID || "",
      clientSecret: process.env.GOOGLE_CLIENT_SECRET || "",
    }),
    Apple({
      clientId: process.env.APPLE_CLIENT_ID || "",
      clientSecret: process.env.APPLE_CLIENT_SECRET || "",
    }),
    Credentials({
      name: "credentials",
      credentials: {
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        const email = credentials?.email as string
        const password = credentials?.password as string
        
        if (!email || !password) return null
        
        const user = users[email]
        if (user && user.password === password) {
          return { id: email, email: user.email, name: user.name }
        }
        
        // Auto-register new users
        users[email] = { email, password, name: email.split("@")[0] }
        return { id: email, email, name: email.split("@")[0] }
      },
    }),
  ],
  pages: {
    signIn: "/login",
    error: "/login",
  },
  session: {
    strategy: "jwt",
  },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.email = user.email
        token.name = user.name
      }
      return token
    },
    async session({ session, token }) {
      if (session.user) {
        session.user.email = token.email as string
        session.user.name = token.name as string
      }
      return session
    },
  },
})
