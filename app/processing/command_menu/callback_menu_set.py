import telebot

from dotenv import load_dotenv
import os

from utils import parse_callback_data
from ...session import get_user_session, get_product_session
from ..command_set import processing_input_command_set

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_callback_menu_set(user_id: int, chat_id: int, callback_data: str):
    user = get_user_session(user_id)
    user.step = 0
    user.type = 'set'

    a = parse_callback_data(callback_data)
    marketplace = a[1]
    article = int(a[2])

    product = get_product_session(user_id)
    product.marketplace = marketplace

    processing_input_command_set(user_id, chat_id, article)