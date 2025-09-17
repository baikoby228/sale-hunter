import logging
from aiogram import Bot

from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

async def processing_command_start(user_id: int, chat_id: int) -> None:
    text = (
        'Привет я бот sale hunter, я помогу тебе выгодно закупаться на маркетплейсах\n'
        '<code>/help</code> для подробной инструкции пользования ботом\n'
        '<code>/settings</code> для настраивания бота\n'
        '<code>/menu</code> для открытия меню отслеживаемых товаров\n'
        '<code>/add</code> для добавления товара в список отслеживаемых\n'
        '<code>/remove</code> для удаления товара из списока отслеживаемых\n'
        '<code>/change</code> для изменения отслеживаемой цены у товара'
    )
    await bot.send_message(chat_id, text=text, parse_mode='html')