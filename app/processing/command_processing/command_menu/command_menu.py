import telebot
from telebot import types

from dotenv import load_dotenv
import os

from infra import get_targets, get_targets_amount
from utils import format_price_byn
from ....session import get_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_menu(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    user = get_user_session(user_id)

    amount = get_targets_amount(user_id)
    targets = get_targets(user_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    for target in targets:
        marketplace, article, max_price = target

        button_info = types.InlineKeyboardButton(f'{marketplace.upper()} - {article} - {format_price_byn(max_price)}', callback_data=f'set_wb_{article}')
        markup.row(button_info)

        button_del = types.InlineKeyboardButton('максимальная цена', callback_data=f'del_wb_{article}')
        button_set = types.InlineKeyboardButton('текущая цена', callback_data=f'set_wb_{article}')
        markup.row(button_del, button_set)

    button_add = types.InlineKeyboardButton('Добавить товар в список отслеживаемых', callback_data=f'add')
    markup.row(button_add)

    text = 'Меню'
    bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)