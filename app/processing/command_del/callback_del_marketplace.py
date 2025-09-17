import logging
from aiogram import Bot

from dotenv import load_dotenv
import os

from ...session import get_user_session, get_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

async def processing_callback_del_marketplace(user_id: int, chat_id: int, callback_data: str) -> None:
    user = await get_user_session(user_id)
    user.step = 0

    product = await get_product_session(user_id)
    product.marketplace = callback_data[4:]

    text = 'Введите артикул товара'
    await bot.send_message(chat_id, text=text, parse_mode='html')