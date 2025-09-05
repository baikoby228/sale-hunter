import telebot

from dotenv import load_dotenv
import os

from app import processing_command_start

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def command_start_handler(message):
    processing_command_start(message)

bot.infinity_polling()