import logging
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

from dotenv import load_dotenv
import os

from utils import find_number, find_price
from infra import add_product, check_product
from ...session import get_user_session, del_user_session, get_product_session, del_product_session
from ...parsers import wb_parser

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

async def processing_input_command_add(user_id: int, chat_id: int, message_text: str = None) -> None:
    user = await get_user_session(user_id)
    current_step = user.step

    product = await get_product_session(user_id)

    match current_step:
        case 0:
            product.article = find_number(message_text)

            if await check_product(user_id, product.marketplace, product.article):
                text = 'Товар с эти артикулом уже отслеживается'

                markup = InlineKeyboardMarkup(inline_keyboard=[])
                button_menu = InlineKeyboardButton(text='Вернуться к меню', callback_data='menu')
                markup.inline_keyboard.append([button_menu])

                await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)

                await del_user_session(user_id)
                await del_product_session(user_id)
                return

            text = 'Введите цену товара для отслеживания'
            await bot.send_message(chat_id, text=text, parse_mode='html')

            user.step += 1
        case 1:
            product.max_price = find_price(message_text)

            text = 'Получение данных о товаре...'
            await bot.send_message(chat_id, text=text, parse_mode='html')

            pr = await wb_parser(product.article)

            if not pr:
                markup = InlineKeyboardMarkup(inline_keyboard=[])
                button_menu = InlineKeyboardButton(text='Вернуться к меню', callback_data='menu')
                markup.inline_keyboard.append([button_menu])

                text = 'Артикул невалиден'
                await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)

                await del_user_session(user_id)
                await del_product_session(user_id)
                return

            product.name = pr.name
            product.photo_url = pr.photo_url
            product.current_price = pr.current_price
            product.start_price = pr.current_price

            if product.current_price <= product.max_price:
                markup = InlineKeyboardMarkup(inline_keyboard=[])
                button_menu = InlineKeyboardButton(text='Вернуться к меню', callback_data='menu')
                markup.inline_keyboard.append([button_menu])

                text = 'Цена товар на данный момент не превышает отслеживаемую цену'
                await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)

                await del_user_session(user_id)
                await del_product_session(user_id)
                return

            user.step += 1
            await processing_input_command_add(user_id, chat_id, message_text)
        case 2:
            product.add_time = str(datetime.now())
            await add_product(product)

            markup = InlineKeyboardMarkup(inline_keyboard=[])
            button_menu = InlineKeyboardButton(text='Вернуться к меню', callback_data='menu')
            markup.inline_keyboard.append([button_menu])

            text = 'Товар добавлен в список отслеживаемых'
            await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)

            await del_user_session(user_id)
            await del_product_session(user_id)