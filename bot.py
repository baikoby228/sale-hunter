import telebot

from dotenv import load_dotenv
import os

from app import (input_processing, processing_command_start, processing_command_help, processing_command_add,
                 processing_callback_add_marketplace, processing_command_del, processing_callback_del_marketplace,
                 processing_command_set, processing_callback_set_marketplace, processing_command_menu,
                 processing_callback_menu_info, processing_callback_menu_set, processing_callback_menu_del,
                 processing_command_settings_sort, processing_callback_settings_sort, processing_command_settings)

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

from test import add_test_products
@bot.message_handler(commands=['test'])
def command_start_handler(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    add_test_products(user_id, chat_id)

@bot.message_handler(commands=['start'])
def command_start_handler(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    processing_command_start(user_id, chat_id)

@bot.message_handler(commands=['help'])
def command_help_handler(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    processing_command_help(user_id, chat_id)

@bot.message_handler(commands=['add'])
def command_add_handler(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    processing_command_add(user_id, chat_id)

@bot.message_handler(commands=['remove'])
def command_del_handler(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    processing_command_del(user_id, chat_id)

@bot.message_handler(commands=['change'])
def command_set_handler(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    processing_command_set(user_id, chat_id)

@bot.message_handler(commands=['menu'])
def command_menu_handler(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    processing_command_menu(user_id, chat_id)

@bot.message_handler(commands=['settings'])
def command_settings_handler(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    processing_command_settings(user_id, chat_id)

@bot.callback_query_handler(func=lambda callback: callback.data in ['add'])
def callback_add_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_command_add(user_id, chat_id)

@bot.callback_query_handler(func=lambda callback: callback.data in ['menu'])
def callback_add_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_command_menu(user_id, chat_id)

@bot.callback_query_handler(func=lambda callback: callback.data in ['add_wb'])
def callback_add_marketplace_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_callback_add_marketplace(user_id, chat_id, callback.data)

@bot.callback_query_handler(func=lambda callback: callback.data in ['del_wb'])
def callback_del_marketplace_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_callback_del_marketplace(user_id, chat_id, callback.data)

@bot.callback_query_handler(func=lambda callback: callback.data in ['set_wb'])
def callback_set_marketplace_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_callback_set_marketplace(user_id, chat_id, callback.data)

@bot.callback_query_handler(func=lambda callback: len(callback.data) >= 4 and callback.data[:4] == 'info' and callback.data.count('_') == 2)
def callback_menu_info_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_callback_menu_info(user_id, chat_id, callback.data)

@bot.callback_query_handler(func=lambda callback: len(callback.data) >= 4 and callback.data[:3] == 'set' and callback.data.count('_') == 2)
def callback_menu_set_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_callback_menu_set(user_id, chat_id, callback.data)

@bot.callback_query_handler(func=lambda callback: len(callback.data) >= 4 and callback.data[:3] == 'del' and callback.data.count('_') == 2)
def callback_menu_del_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_callback_menu_del(user_id, chat_id, callback.data)

@bot.callback_query_handler(func=lambda callback: callback.data == 'settings_sort')
def callback_settings_sort_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_command_settings_sort(user_id, chat_id)

@bot.callback_query_handler(func=lambda callback: len(callback.data) >= 4 and callback.data[:4] == 'sort' and callback.data.count('_') >= 2)
def callback_settings_sort_handler(callback) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    processing_callback_settings_sort(user_id, chat_id, callback.data)

@bot.message_handler(content_types=['text'])
def input_text(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    input_processing(user_id, chat_id, message.text)

bot.infinity_polling()

'''
from infra.database import connector_products
from infra.database import connector_users
if __name__ == '__main__':
    connector_users.create_table()
    connector_products.create_table()
'''