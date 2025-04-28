from fastapi import FastAPI
from app.api.clients import router as clients_router
from app.api.orders import router as orders_router
from app.api.payments import router as payments_router

app = FastAPI(title="RetailCRM Integration API")

app.include_router(clients_router)
app.include_router(orders_router)
app.include_router(payments_router)