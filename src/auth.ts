import NextAuth from "next-auth"
import Credentials from "next-auth/providers/credentials"

export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [
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
        if (!email.includes("@") || password.length < 3) return null
        
        return { id: email, email, name: email.split("@")[0] }
      },
    }),
  ],
  pages: { signIn: "/login" },
  session: { strategy: "jwt" },
  secret: process.env.NEXTAUTH_SECRET || "prepXcore-dev-secret-change-in-production",
  callbacks: {
    async jwt({ token, user }) {
      if (user) { token.email = user.email as string; token.name = user.name as string }
      return token
    },
    async session({ session, token }) {
      if (session.user) { session.user.email = token.email as string; session.user.name = token.name as string }
      return session
    },
  },
})
