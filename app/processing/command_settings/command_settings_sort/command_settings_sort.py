import telebot
from telebot import types

from dotenv import load_dotenv
import os

from ....session import get_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_settings_sort(user_id: int, chat_id: int) -> None:
    user = get_user_session(user_id)

    markup = types.InlineKeyboardMarkup()

    button_date = types.InlineKeyboardButton('По дате', callback_data='sort_type_date')
    markup.row(button_date)

    button_current_price = types.InlineKeyboardButton('По текущей цене', callback_data='sort_type_current_price')
    markup.row(button_current_price)

    button_sort_false = types.InlineKeyboardButton('По возрастанию', callback_data='sort_reverse_false')
    button_sort_true = types.InlineKeyboardButton('По убыванию', callback_data='sort_reverse_true')
    markup.row(button_sort_false, button_sort_true)

    button_menu = types.InlineKeyboardButton('Вернуться к меню', callback_data='menu')
    markup.row(button_menu)

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
    bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)