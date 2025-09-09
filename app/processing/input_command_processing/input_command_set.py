import telebot

from dotenv import load_dotenv
import os

from utils import find_number
from infra import set_target_max_price, check_target
from ...session import get_user_session, del_user_session, get_product_session, del_product_session
from ...wb_parser import wb_parser

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def input_command_set_processing(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    user = get_user_session(user_id)
    current_step = user.step

    product = get_product_session(user_id)

    match current_step:
        case 0:
            product.article = find_number(message.text)

            if not check_target(user_id, product.marketplace, product.article):
                text = 'Товара нету в списке отслеживаемых'
                bot.send_message(chat_id, text, parse_mode='html')
                del_user_session(user_id)

            else:
                text = (
                    'Введите новую максимальную подходящую цену товара для оповещения\n'
                    'Примеры ввода:\n178,32 р.\n9.00 BYN\n41,00'
                )
                bot.send_message(chat_id, text, parse_mode='html')
                user.step += 1
        case 1:
            product.max_price = find_number(message.text)

            text = 'Получение текущей цены товара...'
            bot.send_message(chat_id, text, parse_mode='html')

            current_price = find_number(wb_parser(product.article))
            if current_price <= product.max_price:
                text = 'Товар на данный момент стоит меньше максимальной цены'
                bot.send_message(chat_id, text, parse_mode='html')
            else:
                set_target_max_price(user_id, product.marketplace, product.article, product.max_price)
                text = 'Новая цена отслеживания установлена'
                bot.send_message(chat_id, text, parse_mode='html')

            del_user_session(user_id)
            del_product_session(user_id)