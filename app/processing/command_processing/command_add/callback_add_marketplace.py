import telebot

from dotenv import load_dotenv
import os

from ....session import get_user_session, get_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_callback_add_marketplace(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id

    user = get_user_session(user_id)
    user.step = 0

    product = get_product_session(user_id)
    product.marketplace = callback.data[4:]

    text = 'Введите артикул товара'
    bot.send_message(chat_id, text, parse_mode='html')