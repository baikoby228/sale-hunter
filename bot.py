import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from dotenv import load_dotenv
import os

from app import (input_processing, processing_command_start, processing_command_help, processing_command_add,
                 processing_callback_add_marketplace, processing_command_del, processing_callback_del_marketplace,
                 processing_command_set, processing_callback_set_marketplace, processing_command_menu,
                 processing_callback_menu_info, processing_callback_menu_set, processing_callback_menu_del,
                 processing_command_settings_sort, processing_callback_settings_sort, processing_command_settings)

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

from test import add_test_products
@dp.message(Command("test"))
async def command_test_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    await add_test_products(user_id, chat_id)

@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    await processing_command_start(user_id, chat_id)

@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    await processing_command_help(user_id, chat_id)

@dp.message(Command("add"))
async def command_add_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    await processing_command_add(user_id, chat_id)

@dp.message(Command("remove"))
async def command_del_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    await processing_command_del(user_id, chat_id)

@dp.message(Command("change"))
async def command_set_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    await processing_command_set(user_id, chat_id)

@dp.message(Command("menu"))
async def command_menu_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    await processing_command_menu(user_id, chat_id)

@dp.message(Command("settings"))
async def command_settings_handler(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    await processing_command_settings(user_id, chat_id)

@dp.callback_query(lambda callback: callback.data in ['add'])
async def callback_add_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    await processing_command_add(user_id, chat_id)

@dp.callback_query(lambda callback: callback.data in ['menu'])
async def callback_menu_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    await processing_command_menu(user_id, chat_id)

@dp.callback_query(lambda callback: callback.data in ['add_wb', 'add_ozon'])
async def callback_add_marketplace_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    await processing_callback_add_marketplace(user_id, chat_id, callback.data)

@dp.callback_query(lambda callback: callback.data in ['del_wb', 'del_ozon'])
async def callback_del_marketplace_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    await processing_callback_del_marketplace(user_id, chat_id, callback.data)

@dp.callback_query(lambda callback: callback.data in ['set_wb', 'set_ozon'])
async def callback_set_marketplace_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    await processing_callback_set_marketplace(user_id, chat_id, callback.data)

@dp.callback_query(lambda callback: len(callback.data) >= 4 and callback.data[:4] == 'info' and callback.data.count('_') == 2)
async def callback_menu_info_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    await processing_callback_menu_info(user_id, chat_id, callback.data)

@dp.callback_query(lambda callback: len(callback.data) >= 4 and callback.data[:3] == 'set' and callback.data.count('_') == 2)
async def callback_menu_set_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    await processing_callback_menu_set(user_id, chat_id, callback.data)

@dp.callback_query(lambda callback: len(callback.data) >= 4 and callback.data[:3] == 'del' and callback.data.count('_') == 2)
async def callback_menu_del_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    await  processing_callback_menu_del(user_id, chat_id, callback.data)

@dp.callback_query(lambda callback: callback.data in ['settings_sort'])
async def callback_command_settings_sort_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    await processing_command_settings_sort(user_id, chat_id)

@dp.callback_query(lambda callback: len(callback.data) >= 4 and callback.data[:4] == 'sort' and callback.data.count('_') >= 2)
async def callback_settings_sort_handler(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    await processing_callback_settings_sort(user_id, chat_id, callback.data)

@router.message(F.text)
async def input_text(message: Message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id
    await input_processing(user_id, chat_id, message.text)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())