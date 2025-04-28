from fastapi import APIRouter
from app.services.retailcrm import get_clients, create_client

router = APIRouter(prefix="/clients", tags=["Clients"])

@router.get("/")
async def list_clients(name: str = None, email: str = None, created_at: str = None):
    filters = {}
    if name:
        filters["filter[firstName]"] = name
    if email:
        filters["filter[email]"] = email
    if created_at:
        filters["filter[createdAtFrom]"] = created_at
    return await get_clients(filters)

@router.post("/")
async def add_client(client: dict):
    return await create_client(client)