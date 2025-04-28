from fastapi import APIRouter
from app.services.retailcrm import get_orders_by_customer, create_order

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/client/{customer_id}")
async def orders_for_client(customer_id: str):
    return await get_orders_by_customer(customer_id)

@router.post("/")
async def add_order(order: dict):
    return await create_order(order)