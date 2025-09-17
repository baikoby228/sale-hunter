import logging
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv
import os

from config import MAX_AMOUNT_OF_PRODUCTS
from infra import get_products_amount
from app.session import create_user_session, create_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

async def processing_command_add(user_id: int, chat_id: int) -> None:
    if await get_products_amount(user_id) == MAX_AMOUNT_OF_PRODUCTS:
        text = f'Достигнут лимит отслеживаемых товаров ({MAX_AMOUNT_OF_PRODUCTS})'
        await bot.send_message(chat_id, text=text, parse_mode='html')
        return

    await create_user_session(user_id, chat_id, 'add', -1)
    await create_product_session(user_id)

    markup = InlineKeyboardMarkup(inline_keyboard=[])
    button_wb = InlineKeyboardButton(text='Wildberries', callback_data='add_wb')
    markup.inline_keyboard.append([button_wb])

    text = 'Выберите маркетплейс для отслеживания товара'
    await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)