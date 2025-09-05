import telebot

from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def processing_command_start(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    text = (
        f'Привет я бот sale hunter, я помогу тебе выгодно закупаться на маркетплейсах\n'
        f'<code>/add</code> для добовления товара в список отслеживаемых\n'
        f'<code>/remove</code> для удаления товара из списока отслеживаемых'
    )
    bot.send_message(chat_id, text, parse_mode='html')