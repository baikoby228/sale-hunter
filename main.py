import telebot

from dotenv import load_dotenv
import os

from app import input_processing, processing_command_start, processing_command_add, processing_callback_add_marketplace

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def command_start_handler(message) -> None:
    processing_command_start(message)

@bot.message_handler(commands=['add'])
def command_start_handler(message) -> None:
    processing_command_add(message)

@bot.callback_query_handler(func=lambda callback: callback.data in ['wb'])
def callback_add_marketplace_handler(callback) -> None:
    processing_callback_add_marketplace(callback)

@bot.message_handler(content_types=['text'])
def input_text(message):
    input_processing(message)

bot.infinity_polling()