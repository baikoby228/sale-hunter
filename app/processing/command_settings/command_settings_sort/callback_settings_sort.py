import logging
from aiogram import Bot

from dotenv import load_dotenv
import os

from ....session import get_user_session
from .command_settings_sort import processing_command_settings_sort

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

async def processing_callback_settings_sort(user_id: int, chat_id: int, callback_data: str) -> None:
    user = await get_user_session(user_id)

    text: str
    if callback_data == 'sort_type_date':
        await user.set_sort_type('date')
        text = '✅ Критерий сортировки изменён'
    if callback_data == 'sort_type_current_price':
        await user.set_sort_type('current_price')
        text = '✅ Критерий сортировки изменён'

    if callback_data == 'sort_reverse_false':
        await user.set_sort_reverse(False)
        text = '✅ Порядок сртировки изменён'
    if callback_data == 'sort_reverse_true':
        await user.set_sort_reverse(True)
        text = '✅ Порядок сотировки изменён'

    await bot.send_message(chat_id, text=text, parse_mode='html')
    await processing_command_settings_sort(user_id, chat_id)