import telebot
from telebot import types

from dotenv import load_dotenv
import os

from ....user_session import create_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_add(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    data = create_user_session(user_id)
    data.step = 0

    markup = types.InlineKeyboardMarkup(row_width=1)
    button_wb = types.InlineKeyboardButton('Wildberries', callback_data='wb')
    markup.add(button_wb)

    text = 'Выберите маркетплейс для мониторинга товара'
    bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)