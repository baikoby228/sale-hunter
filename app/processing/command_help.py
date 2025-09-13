import telebot

from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_help(user_id: int, chat_id: int) -> None:
    text = (
        '<code>/settings</code> для настраивания бота\n'
        '<code>/menu</code> для открытия меню отслеживаемых товаров\n'
        '<code>/add</code> для добавления товара в список отслеживаемых\n'
        '<code>/remove</code> для удаления товара из списока отслеживаемых\n'
        '<code>/change</code> для изменения отслеживаемой цены у товара'
    )
    bot.send_message(chat_id, text, parse_mode='html')