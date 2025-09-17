import logging
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv
import os

from ...session import get_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

async def processing_command_settings(user_id: int, chat_id: int) -> None:
    user = await get_user_session(user_id)

    markup = InlineKeyboardMarkup(inline_keyboard=[])

    button_language = InlineKeyboardButton(text='🌐 Язык', callback_data='settings_language')
    markup.inline_keyboard.append([button_language])

    button_sort = InlineKeyboardButton(text='📋 Сортировка отслеживаемых товаров', callback_data='settings_sort')
    markup.inline_keyboard.append([button_sort])

    button_menu = InlineKeyboardButton(text='🔙 Вернуться к меню', callback_data='menu')
    markup.inline_keyboard.append([button_menu])

    text = 'Выберите раздел настроек'
    await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)