import telebot
from datetime import datetime

from dotenv import load_dotenv
import os

from utils import find_number, find_price
from infra import add_product, check_product
from ...session import get_user_session, del_user_session, get_product_session, del_product_session
from ...parsers import wb_parser

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_input_command_add(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    user = get_user_session(user_id)
    current_step = user.step

    product = get_product_session(user_id)

    match current_step:
        case 0:
            product.article = find_number(message.text)

            if check_product(user_id, product.marketplace, product.article):
                text = 'Товар с эти артикулом уже отслеживается'
                bot.send_message(chat_id, text, parse_mode='html')

                del_user_session(user_id)
                del_product_session(user_id)
                return

            text = 'Введите максимальную подходящую цену товара для оповещения'
            bot.send_message(chat_id, text, parse_mode='html')

            user.step += 1
        case 1:
            product.max_price = find_price(message.text)

            text = 'Получение данных о товаре...'
            bot.send_message(chat_id, text, parse_mode='html')

            pr = wb_parser(product.article)

            if not pr:
                text = 'Артикул невалиден'
                bot.send_message(chat_id, text, parse_mode='html')

                del_user_session(user_id)
                del_product_session(user_id)
                return

            product.name = pr.name
            product.photo_url = pr.photo_url
            product.current_price = pr.current_price
            product.start_price = pr.current_price

            '''
            print(product.name)
            print(product.photo_url)
            print(product.current_price)
            '''

            if product.current_price <= product.max_price:
                text = 'Товар на данный не превышает отслеживаемую цены'
                bot.send_message(chat_id, text, parse_mode='html')

                del_user_session(user_id)
                del_product_session(user_id)
                return

            product.add_time = str(datetime.now())
            add_product(user_id, product)

            text = 'Товар добавлен в список отслеживаемых'
            bot.send_message(chat_id, text, parse_mode='html')

            del_user_session(user_id)
            del_product_session(user_id)