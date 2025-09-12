import telebot
from telebot import types

from dotenv import load_dotenv
import os

from infra import get_products, get_products_amount
from utils import format_price_byn
from config import MAX_AMOUNT_OF_PRODUCTS
from ....session import get_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_menu(user_id: int, chat_id: int) -> None:
    user = get_user_session(user_id)

    amount = get_products_amount(user_id)
    products = get_products(user_id)

    markup = types.InlineKeyboardMarkup()
    if len(products) == 0:
        button_add = types.InlineKeyboardButton('Добавить товар', callback_data='add')
        markup.row(button_add)

    text = (
        f'Меню ({amount}/{MAX_AMOUNT_OF_PRODUCTS})\n'
        '...'
    )

    bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)

    for i in range(len(products)):
        product = products[i]

        markup = types.InlineKeyboardMarkup()

        button_info = types.InlineKeyboardButton(f'{product.marketplace.upper()} - {product.article}', callback_data=f'info_wb_{product.article}')
        markup.row(button_info)

        text = 'изменить'
        button_set = types.InlineKeyboardButton(text, callback_data=f'set_wb_{product.article}')

        text = 'удалить'
        button_del = types.InlineKeyboardButton(text, callback_data=f'del_wb_{product.article}')

        markup.row(button_set, button_del)

        if i == len(products) - 1 and amount != MAX_AMOUNT_OF_PRODUCTS:
            button_add = types.InlineKeyboardButton('Добавить товар', callback_data='add')
            markup.row(button_add)

        text = f'{format_price_byn(product.max_price)} - {format_price_byn(product.current_price)}'
        bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)