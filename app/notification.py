import telebot

from dotenv import load_dotenv
import os

from .session import get_user_session
from models import ProductData
from utils import format_price_byn
from app import processing_callback_menu_del

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def send_notification(product: ProductData) -> None:
    user = get_user_session(product.user_id)
    user_id = user.id
    chat_id = user.chat_id

    url = f'https://www.wildberries.by/catalog/{product.article}/detail.aspx'
    text = (
        f'<a href="{url}">Товар</a> упал ниже отслеживаемой цены\n'
        f'<code>{product.article}</code>\n'
        f'Отслеживаемая цена - {format_price_byn(product.max_price)}\n'
        f'Текущая цена товара - {format_price_byn(product.current_price)}'
    )
    bot.send_message(chat_id, text, parse_mode='html')

    caption = f'{product.name}'
    bot.send_photo(chat_id, photo=product.photo_url, caption=caption, parse_mode='html')

    processing_callback_menu_del(user_id, chat_id, f'del_{product.marketplace}_{product.article}')