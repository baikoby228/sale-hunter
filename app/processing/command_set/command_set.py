import logging
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv
import os

from ...session import create_user_session, create_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

async def processing_command_set(user_id: int, chat_id: int) -> None:
    await create_user_session(user_id, chat_id, 'set', -1)
    await create_product_session(user_id)

    markup = InlineKeyboardMarkup(inline_keyboard=[])
    button_wb = InlineKeyboardButton(text='🟣 Wildberries 🟣', callback_data='set_wb')
    markup.inline_keyboard.append([button_wb])

    text = 'Выберите маркетплейс товара, цену которого меняете'
    await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)