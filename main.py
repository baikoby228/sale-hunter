import telebot

from dotenv import load_dotenv
import os

from app import (input_processing, processing_command_start, processing_command_add,
                 processing_callback_add_marketplace, processing_command_del, processing_callback_del_marketplace,
                 processing_command_set, processing_callback_set_marketplace, processing_command_menu)
from print_all import print_all_processing
from test import test_processing

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

'''
from infra.database.connector import create_db
if __name__ == '__main__':
    create_db()
'''

@bot.message_handler(commands=['start'])
def command_start_handler(message) -> None:
    processing_command_start(message)

@bot.message_handler(commands=['add'])
def command_start_handler(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    processing_command_add(user_id, chat_id)

@bot.message_handler(commands=['remove'])
def command_start_handler(message) -> None:
    processing_command_del(message)

@bot.message_handler(commands=['change'])
def command_start_handler(message) -> None:
    processing_command_set(message)

@bot.message_handler(commands=['menu'])
def command_menu_handler(message) -> None:
    processing_command_menu(message)

@bot.message_handler(commands=['all'])
def command_all_handler(message) -> None:
    print_all_processing(message)

@bot.message_handler(commands=['test'])
def command_test_handler(message) -> None:
    test_processing(message)

@bot.callback_query_handler(func=lambda callback: callback.data in ['add'])
def callback_add_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_command_add(user_id, chat_id)

@bot.callback_query_handler(func=lambda callback: callback.data in ['add_wb'])
def callback_add_marketplace_handler(callback) -> None:
    processing_callback_add_marketplace(callback)

@bot.callback_query_handler(func=lambda callback: callback.data in ['del_wb'])
def callback_del_marketplace_handler(callback) -> None:
    processing_callback_del_marketplace(callback)

@bot.callback_query_handler(func=lambda callback: callback.data in ['set_wb'])
def callback_set_marketplace_handler(callback) -> None:
    processing_callback_set_marketplace(callback)

@bot.message_handler(content_types=['text'])
def input_text(message) -> None:
    input_processing(message)

bot.infinity_polling()