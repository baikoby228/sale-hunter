import logging
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv
import os

from ....session import get_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

async def processing_command_settings_sort(user_id: int, chat_id: int) -> None:
    user = await get_user_session(user_id)

    markup = InlineKeyboardMarkup(inline_keyboard=[])

    button_date = InlineKeyboardButton(text='По дате', callback_data='sort_type_date')
    markup.inline_keyboard.append([button_date])

    button_current_price = InlineKeyboardButton(text='По текущей цене', callback_data='sort_type_current_price')
    markup.inline_keyboard.append([button_current_price])

    button_sort_false = InlineKeyboardButton(text='По возрастанию', callback_data='sort_reverse_false')
    button_sort_true = InlineKeyboardButton(text='По убыванию', callback_data='sort_reverse_true')
    markup.inline_keyboard.append([button_sort_false, button_sort_true])

    button_menu = InlineKeyboardButton(text='Вернуться к меню', callback_data='menu')
    markup.inline_keyboard.append([button_menu])

    text_sort_type: str
    if user.sort_type == 'date':
        text_sort_type = 'дате добавления товара в список отслеживаемых'
    else:
        text_sort_type = 'текущей цене товара'

    text_sort_reverse: str
    if user.sort_reverse:
        text_sort_reverse = 'убыванию'
    else:
        text_sort_reverse = 'возрастанию'

    text = (
        f'Сейчас сортируется по {text_sort_type}, по {text_sort_reverse}\n'
        'Выберите критерий сортировки и порядок сортировки'
    )
    await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)