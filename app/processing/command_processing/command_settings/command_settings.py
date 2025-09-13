import telebot
from telebot import types

from dotenv import load_dotenv
import os

from app.session import get_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_settings(user_id: int, chat_id: int) -> None:
    user = get_user_session(user_id)

    markup = types.InlineKeyboardMarkup()

    button_language = types.InlineKeyboardButton('Язык', callback_data='settings_language')
    markup.row(button_language)

    button_sort = types.InlineKeyboardButton('Сортировка отслеживаемых товаров', callback_data='settings_sort')
    markup.row(button_sort)

    button_menu = types.InlineKeyboardButton('Вернуться к меню', callback_data='menu')
    markup.row(button_menu)

    text = 'Выберите раздел настроек'
    bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)