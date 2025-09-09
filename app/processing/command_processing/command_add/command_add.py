import telebot
from telebot import types

from dotenv import load_dotenv
import os

from ....user_session import create_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_add(user_id, chat_id) -> None:
    data = create_user_session(id=user_id, type='add', start_step=-1)

    markup = types.InlineKeyboardMarkup(row_width=1)
    button_wb = types.InlineKeyboardButton('Wildberries', callback_data='add_wb')
    markup.add(button_wb)

    text = 'Выберите маркетплейс для мониторинга товара'
    bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)