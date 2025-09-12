import telebot

from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_start(user_id: int, chat_id: int) -> None:
    text = (
        'Привет я бот sale hunter, я помогу тебе выгодно закупаться на маркетплейсах\n'
        '<code>/menu</code> для подробной инструкции пользования ботом\n'
        '<code>/help</code> для открытия меню отслеживаемых товаров\n'
        '<code>/add</code> для добовления товара в список отслеживаемых\n'
        '<code>/remove</code> для удаления товара из списока отслеживаемых\n'
        '<code>/change</code> для смены максимальной цены у отслеживаемого товара'
    )
    bot.send_message(chat_id, text, parse_mode='html')