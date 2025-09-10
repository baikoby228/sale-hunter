import telebot

from dotenv import load_dotenv
import os

from config import MAX_AMOUNT_OF_TARGETS
from utils import find_number
from infra import add_product, check_product, get_products_amount
from ...session import get_user_session, del_user_session, get_product_session, del_product_session
from ...parsers import wb_parser

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def input_command_add_processing(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    user = get_user_session(user_id)
    current_step = user.step

    product = get_product_session(user_id)

    match current_step:
        case 0:
            product.article = find_number(message.text)
            text = (
                'Введите максимальную подходящую цену товара для оповещения\n'
                'Примеры ввода:\n178,32 р.\n9.00 BYN\n41,00'
            )
            bot.send_message(chat_id, text, parse_mode='html')
            user.step += 1
        case 1:
            product.max_price = find_number(message.text)

            if check_product(user_id, product.marketplace, product.article):
                text = 'Товар с эти артикулом уже отслеживается'
                bot.send_message(chat_id, text, parse_mode='html')
            elif get_products_amount(user_id) == MAX_AMOUNT_OF_TARGETS:
                text = f'Достигнут лимит отслеживаемых товаров ({MAX_AMOUNT_OF_TARGETS})'
                bot.send_message(chat_id, text, parse_mode='html')
            else:
                text = 'Получение данных о товаре...'
                bot.send_message(chat_id, text, parse_mode='html')

                pr = wb_parser(product.article)
                product.name = pr.name
                product.photo_url = pr.photo_url
                product.current_price = pr.current_price

                '''
                print(product.name)
                print(product.photo_url)
                print(product.current_price)
                '''

                if product.current_price <= product.max_price:
                    text = 'Товар на данный не превышает отслеживаемую цены'
                    bot.send_message(chat_id, text, parse_mode='html')
                else:
                    add_product(user_id, product)
                    text = 'Товар добавлен в список отслеживаемых'
                    bot.send_message(chat_id, text, parse_mode='html')

            del_user_session(user_id)
            del_product_session(user_id)