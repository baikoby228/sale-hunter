import asyncio
from models import ProductData

session = {}
session_lock = asyncio.Lock()

async def create_product_session(id: int) -> None:
    async with session_lock:
        session[id] = ProductData(id)

async def get_product_session(id: int) -> ProductData:
    async with session_lock:
        if id not in session:
            session[id] = ProductData(id)
        return session[id]

async def del_product_session(id: int) -> None:
    async with session_lock:
        del session[id]