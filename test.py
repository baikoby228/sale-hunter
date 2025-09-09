import telebot

from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def test_processing(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    caption = 'photo'
    url = 'https://basket-15.wbbasket.ru/vol2374/part237496/237496144/images/c246x328/1.webp'
    bot.send_photo(chat_id, photo=url, caption=caption, parse_mode='html')