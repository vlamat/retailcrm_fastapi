import httpx
from app.config import RETAILCRM_API_URL, RETAILCRM_API_KEY

async def get_clients(filters: dict = None):
    params = {'apiKey': RETAILCRM_API_KEY}
    if filters:
        params.update(filters)
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{RETAILCRM_API_URL}/customers", params=params)
    response.raise_for_status()
    return response.json()

async def create_client(client_data: dict):
    params = {'apiKey': RETAILCRM_API_KEY}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{RETAILCRM_API_URL}/customers/create", params=params, json={"customer": client_data})
    response.raise_for_status()
    return response.json()

async def get_orders_by_customer(customer_id: str):
    params = {
        'apiKey': RETAILCRM_API_KEY,
        'filter[customerId]': customer_id
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{RETAILCRM_API_URL}/orders", params=params)
    response.raise_for_status()
    return response.json()

async def create_order(order_data: dict):
    params = {'apiKey': RETAILCRM_API_KEY}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{RETAILCRM_API_URL}/orders/create", params=params, json={"order": order_data})
    response.raise_for_status()
    return response.json()

async def create_payment(order_id: str, payment_data: dict):
    payment_data.update({"order": {"id": order_id}})
    params = {'apiKey': RETAILCRM_API_KEY}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{RETAILCRM_API_URL}/orders/payments/create", params=params, json={"payment": payment_data})
    response.raise_for_status()
    return response.json()