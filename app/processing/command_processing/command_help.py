import telebot

from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_help(user_id: int, chat_id: int) -> None:
    text = (
        '<code>/menu</code> для открытия меню отслеживаемых товаров\n'
        '<code>/add</code> для добовления товара в список отслеживаемых\n'
        '<code>/remove</code> для удаления товара из списока отслеживаемых\n'
        '<code>/change</code> для смены максимальной цены у отслеживаемого товара\n'
        '...'
    )
    bot.send_message(chat_id, text, parse_mode='html')