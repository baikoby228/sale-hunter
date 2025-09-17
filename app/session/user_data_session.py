import asyncio
from models import UserData
from infra import get_user_data

session = {}
session_lock = asyncio.Lock()

async def create_user_session(id: int, chat_id: int, type: str, start_step: int) -> None:
    async with session_lock:
        session[id] = UserData(id, chat_id, type, start_step)
        await session[id].init()

async def get_user_session(id: int, chat_id: int = None, type: str = 'None', start_step: int = -1) -> UserData:
    async with session_lock:
        if not id in session:
            res = await get_user_data(id)
            if res:
                chat_id, type, start_step = res
            session[id] = UserData(id, chat_id, type, start_step)
            await session[id].init()
        return session[id]

async def del_user_session(id: int) -> None:
    async with session_lock:
        if id in session:
            del session[id]