import telebot
from telebot import types

from dotenv import load_dotenv
import os

from ....session import create_user_session, create_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_add(user_id, chat_id) -> None:
    create_user_session(user_id, 'add', -1)
    create_product_session(user_id)

    markup = types.InlineKeyboardMarkup(row_width=1)
    button_wb = types.InlineKeyboardButton('Wildberries', callback_data='add_wb')
    markup.add(button_wb)

    text = 'Выберите маркетплейс для мониторинга товара'
    bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)