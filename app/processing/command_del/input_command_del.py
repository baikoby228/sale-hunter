import telebot
from telebot import types

from dotenv import load_dotenv
import os

from utils import find_number
from infra import del_product, check_product
from ...session import get_user_session, del_user_session, get_product_session, del_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_input_command_del(user_id: int, chat_id: int, message_text: str = None) -> None:
    user = get_user_session(user_id)
    current_step = user.step

    product = get_product_session(user_id)

    match current_step:
        case 0:
            product.article = find_number(message_text)

            if not check_product(user_id, product.marketplace, product.article):
                markup = types.InlineKeyboardMarkup()
                button_menu = types.InlineKeyboardButton('Вернуться к меню', callback_data='menu')
                markup.row(button_menu)

                text = 'Товара нету в списке отслеживаемых'
                bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)

                del_user_session(user_id)
                del_product_session(user_id)
                return

            user.step += 1
            processing_input_command_del(user_id, chat_id, message_text)
        case 1:
            del_product(user_id, product.marketplace, product.article)

            markup = types.InlineKeyboardMarkup()
            button_menu = types.InlineKeyboardButton('Вернуться к меню', callback_data='menu')
            markup.row(button_menu)

            text = 'Товар удалён из списка отслеживаемых'
            bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)

            del_user_session(user_id)
            del_product_session(user_id)