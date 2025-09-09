import telebot

from dotenv import load_dotenv
import os

from infra import get_targets

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def print_all_processing(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    v = get_targets(user_id)
    for a, b in v:
        bot.send_message(chat_id, f'<code>{a}</code> - {b}', parse_mode='html')
