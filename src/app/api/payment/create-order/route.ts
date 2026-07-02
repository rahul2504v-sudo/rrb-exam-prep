import { NextResponse } from 'next/server'
import Razorpay from 'razorpay'

const razorpay = new Razorpay({
  key_id: process.env.RAZORPAY_KEY_ID || 'rzp_test_DUMMY_KEY',
  key_secret: process.env.RAZORPAY_KEY_SECRET || 'DUMMY_SECRET',
})

export async function POST(request: Request) {
  try {
    const { examId } = await request.json()
    
    const order = await razorpay.orders.create({
      amount: 9900, // ₹99 in paise
      currency: 'INR',
      receipt: `prepxcore-${examId}-${Date.now()}`,
      notes: { examId },
    })
    
    return NextResponse.json({
      orderId: order.id,
      amount: order.amount,
      currency: order.currency,
      key: process.env.RAZORPAY_KEY_ID || 'rzp_test_DUMMY_KEY',
    })
  } catch (error: any) {
    return NextResponse.json({ error: error.message || 'Failed to create order' }, { status: 500 })
  }
}
