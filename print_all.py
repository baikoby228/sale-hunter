import telebot

from dotenv import load_dotenv
import os

from infra import get_products

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def print_all_processing(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    products = get_products(user_id)
    for product in products:
        text = (
            f'mp = {product.marketplace}\n'
            f'art = {product.article}\n'
            f'name = {product.name}\n'
            f'photo = {product.photo_url}\n'
            f'cur_price = {product.current_price}\n'
            f'st_price = {product.start_price}\n'
            f'time = {product.add_time}\n'
            f'mx_pr = {product.max_price}\n'
        )
        bot.send_message(chat_id, text, parse_mode='html')
