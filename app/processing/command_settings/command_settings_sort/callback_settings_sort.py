import telebot

from dotenv import load_dotenv
import os

from ....session import get_user_session
from .command_settings_sort import processing_command_settings_sort

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_callback_settings_sort(user_id: int, chat_id: int, callback_data: str) -> None:
    user = get_user_session(user_id)

    text: str
    if callback_data == 'sort_type_date':
        user.set_sort_type('date')
        text = 'Критерий сортировки изменён'
    if callback_data == 'sort_type_current_price':
        user.set_sort_type('current_price')
        text = 'Критерий сортировки изменён'

    if callback_data == 'sort_reverse_false':
        user.set_sort_reverse(False)
        text = 'Порядок сртировки изменён'
    if callback_data == 'sort_reverse_true':
        user.set_sort_reverse(True)
        text = 'Порядок сотировки изменён'

    bot.send_message(chat_id, text, parse_mode='html')
    processing_command_settings_sort(user_id, chat_id)