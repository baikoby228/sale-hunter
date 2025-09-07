import telebot

from dotenv import load_dotenv
import os

from app import (input_processing, processing_command_start, processing_command_add,
                 processing_callback_add_marketplace, processing_command_del, processing_callback_del_marketplace,
                 processing_command_set, processing_callback_set_marketplace)
#from print_all import print_all_processing

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def command_start_handler(message) -> None:
    processing_command_start(message)

@bot.message_handler(commands=['add'])
def command_start_handler(message) -> None:
    processing_command_add(message)

@bot.message_handler(commands=['remove'])
def command_start_handler(message) -> None:
    processing_command_del(message)

@bot.message_handler(commands=['change'])
def command_start_handler(message) -> None:
    processing_command_set(message)

'''
@bot.message_handler(commands=['all'])
def command_start_handler(message) -> None:
    print_all_processing(message)
'''

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