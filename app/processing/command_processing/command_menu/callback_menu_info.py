import telebot

from dotenv import load_dotenv
import os

from infra import get_product
from utils import format_price_byn
from ....session import get_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_callback_menu_info(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id

    user = get_user_session(user_id)

    a = []
    cur = ''
    for x in callback.data:
        if x == '_':
            a.append(cur)
            cur = ''
        else:
            cur += x
    a.append(cur)

    marketplace = a[1]
    article = int(a[2])

    product = get_product(user_id, marketplace, article)

    url = f'https://www.wildberries.by/catalog/{product.article}/detail.aspx'
    caption = (
        f'{product.name}\n'
        f'{product.marketplace.upper()} <a href="{url}">{product.article}</a>\n'
        f'Отслеживаемая цена - {format_price_byn(product.max_price)}\n'
        f'Текущая цена - {format_price_byn(product.current_price)}\n'
        f'Стартовая цена - {format_price_byn(product.start_price)}\n'
        f'Время добавления в спиоск отслеживаемых товаров:\n{product.add_time[:16]}'
    )
    bot.send_photo(chat_id, photo=product.photo_url, caption=caption, parse_mode='html')