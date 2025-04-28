from fastapi import APIRouter
from app.services.retailcrm import create_payment

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/")
async def add_payment(order_id: str, payment: dict):
    return await create_payment(order_id, payment)