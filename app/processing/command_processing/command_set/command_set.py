import telebot
from telebot import types

from dotenv import load_dotenv
import os

from ....session import create_user_session, create_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_set(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    create_user_session(user_id, 'set', -1)
    create_product_session(user_id)

    markup = types.InlineKeyboardMarkup(row_width=1)
    button_wb = types.InlineKeyboardButton('Wildberries', callback_data='set_wb')
    markup.add(button_wb)

    text = 'Выберите маркетплейс товара из списка отслеживаемых, цену которого меняете'
    bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)