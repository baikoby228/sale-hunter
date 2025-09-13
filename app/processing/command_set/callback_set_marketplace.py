import telebot

from dotenv import load_dotenv
import os

from ...session import get_user_session, get_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_callback_set_marketplace(user_id: int, chat_id: int, callback_data: str) -> None:
    user = get_user_session(user_id)
    user.step = 0

    product = get_product_session(user_id)
    product.marketplace = callback_data[4:]

    text = 'Введите артикул товара'
    bot.send_message(chat_id, text, parse_mode='html')