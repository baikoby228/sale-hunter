import telebot
from telebot import types

from dotenv import load_dotenv
import os

from infra import get_product
from utils import format_price_byn, parse_callback_data
from ....session import get_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_callback_menu_info(user_id: int, chat_id: int, callback_data: str):
    user = get_user_session(user_id)

    a = parse_callback_data(callback_data)
    marketplace = a[1]
    article = int(a[2])

    product = get_product(user_id, marketplace, article)

    url = f'https://www.wildberries.by/catalog/{product.article}/detail.aspx'
    caption = f'{product.name}'
    bot.send_photo(chat_id, photo=product.photo_url, caption=caption, parse_mode='html')

    markup = types.InlineKeyboardMarkup()

    text = 'изменить'
    button_set = types.InlineKeyboardButton(text, callback_data=f'set_wb_{product.article}')

    text = 'удалить'
    button_del = types.InlineKeyboardButton(text, callback_data=f'del_wb_{product.article}')

    markup.row(button_set, button_del)

    text = (
        f'{product.marketplace.upper()} <code>{product.article}</code> <a href="{url}">ссылка</a>\n'
        f'Отслеживаемая цена - {format_price_byn(product.max_price)}\n'
        f'Текущая цена - {format_price_byn(product.current_price)}\n'
        f'Стартовая цена - {format_price_byn(product.start_price)}\n'
        f'Время добавления в спиоск отслеживаемых товаров:\n{product.add_time[:16]}'
    )
    bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)