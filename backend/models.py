from pydantic import BaseModel

class PaymentTransaction(BaseModel):
    user_id: int
    amount: float
    status: str
    created_at: str  # Timestamp
