import { NextResponse } from 'next/server'
import crypto from 'crypto'

export async function POST(request: Request) {
  try {
    const { razorpay_order_id, razorpay_payment_id, razorpay_signature } = await request.json()
    
    const secret = process.env.RAZORPAY_KEY_SECRET || 'DUMMY_SECRET'
    const sign = razorpay_order_id + '|' + razorpay_payment_id
    const expected = crypto.createHmac('sha256', secret).update(sign).digest('hex')
    
    if (expected === razorpay_signature) {
      return NextResponse.json({ verified: true })
    }
    return NextResponse.json({ verified: false, error: 'Invalid signature' }, { status: 400 })
  } catch {
    return NextResponse.json({ error: 'Verification failed' }, { status: 500 })
  }
}
