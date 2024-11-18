from fastapi import FastAPI, HTTPException, Request
import graphene  # Importar correctamente la librería graphene
from graphene import ObjectType, String, Float, Schema
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import stripe
from pydantic import BaseModel

# Configurar la API de Stripe
stripe.api_key = "tu_api_key_de_stripe"  # Usa tu propia API Key

# Crear la aplicación FastAPI
app = FastAPI()

# Definir el esquema de GraphQL
class PaymentTransaction(ObjectType):
    id = String()
    amount = Float()
    status = String()

class PaymentQuery(ObjectType):
    get_payment_status = graphene.Field(PaymentTransaction, payment_id=String(required=True))

    def resolve_get_payment_status(self, info, payment_id):
        # Aquí se debería realizar una consulta a la base de datos para obtener el estado del pago
        return PaymentTransaction(id=payment_id, amount=100.0, status="Completed")

schema = graphene.Schema(query=PaymentQuery)

# Agregar la ruta GraphQL usando el Router correcto
@app.get("/graphql")
async def graphql_view(request: Request):
    # Utilizar graphene para resolver las consultas
    return JSONResponse({"message": "GraphQL endpoint is active!"})

# Definir el modelo para los pagos
class Payment(BaseModel):
    amount: float

# Crear el Payment Intent con Stripe
@app.post("/create_payment_intent")
async def create_payment_intent(payment: Payment):
    try:
        # Crear el pago en Stripe
        payment_intent = stripe.PaymentIntent.create(
            amount=int(payment.amount * 100),  # Stripe requiere el monto en centavos
            currency="usd",
        )
        return {"clientSecret": payment_intent.client_secret}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)