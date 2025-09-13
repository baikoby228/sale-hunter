import telebot
from telebot import types

from dotenv import load_dotenv
import os

from utils import find_number, find_price
from infra import set_product_max_price, check_product, get_product_current_price
from ...session import get_user_session, del_user_session, get_product_session, del_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_input_command_set(user_id: int, chat_id: int, message_text: str = None) -> None:
    user = get_user_session(user_id)
    current_step = user.step

    product = get_product_session(user_id)

    match current_step:
        case 0:
            product.article = find_number(message_text)

            if not check_product(user_id, product.marketplace, product.article):
                text = 'Товара нету в списке отслеживаемых'
                bot.send_message(chat_id, text, parse_mode='html')

                del_user_session(user_id)
                del_product_session(user_id)
                return

            text = 'Введите новую цену товара для отслеживания'
            bot.send_message(chat_id, text, parse_mode='html')
            user.step += 1
        case 1:
            product.max_price = find_price(message_text)

            current_price = get_product_current_price(user_id, product.marketplace, product.article)
            if current_price <= product.max_price:
                text = 'Товар на данный момент стоит меньше максимальной цены'
                bot.send_message(chat_id, text, parse_mode='html')

                del_user_session(user_id)
                del_product_session(user_id)
                return

            user.step += 1
            processing_input_command_set(user_id, chat_id, message_text)
        case 2:
            set_product_max_price(user_id, product.marketplace, product.article, product.max_price)

            markup = types.InlineKeyboardMarkup()
            button_menu = types.InlineKeyboardButton('Вернуться к меню', callback_data='menu')
            markup.row(button_menu)

            text = 'Новая цена отслеживания установлена'
            bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)

            del_user_session(user_id)
            del_product_session(user_id)