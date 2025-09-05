import telebot

from dotenv import load_dotenv
import os

from app.user_session import get_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_callback_add_marketplace(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id

    data = get_user_session(user_id)
    data.marketplace = callback.data