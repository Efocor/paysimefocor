import stripe
from fastapi import HTTPException

stripe.api_key = "tu_api_key_de_stripe"  # Usa tu propia API Key

def create_payment(amount: float):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),
            currency="usd",
        )
        return payment_intent
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=f"Payment failed: {e}")