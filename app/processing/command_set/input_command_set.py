import logging
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv
import os

from utils import find_number, find_price
from infra import set_product_max_price, check_product, get_product_current_price
from ...session import get_user_session, del_user_session, get_product_session, del_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

async def processing_input_command_set(user_id: int, chat_id: int, message_text: str = None) -> None:
    user = await get_user_session(user_id)
    current_step = user.step

    product = await get_product_session(user_id)

    match current_step:
        case 0:
            product.article = find_number(message_text)

            if not await check_product(user_id, product.marketplace, product.article):
                markup = InlineKeyboardMarkup(inline_keyboard=[])
                button_menu = InlineKeyboardButton(text='Вернуться к меню', callback_data='menu')
                markup.inline_keyboard.append([button_menu])

                text = 'Товара нету в списке отслеживаемых'
                await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)

                await del_user_session(user_id)
                await del_product_session(user_id)
                return

            text = 'Введите новую цену товара для отслеживания'
            await bot.send_message(chat_id, text=text, parse_mode='html')
            user.step += 1
        case 1:
            product.max_price = find_price(message_text)

            current_price = await get_product_current_price(user_id, product.marketplace, product.article)
            if current_price <= product.max_price:
                markup = InlineKeyboardMarkup(inline_keyboard=[])
                button_menu = InlineKeyboardButton(text='Вернуться к меню', callback_data='menu')
                markup.inline_keyboard.append([button_menu])

                text = 'Цена товар на данный момент не превышает отслеживаемую цены'
                await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)

                await del_user_session(user_id)
                await del_product_session(user_id)
                return

            user.step += 1
            await processing_input_command_set(user_id, chat_id, message_text)
        case 2:
            await set_product_max_price(user_id, product.marketplace, product.article, product.max_price)

            markup = InlineKeyboardMarkup(inline_keyboard=[])
            button_menu = InlineKeyboardButton(text='Вернуться к меню', callback_data='menu')
            markup.inline_keyboard.append([button_menu])

            text = 'Новая цена отслеживания установлена'
            await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)

            await del_user_session(user_id)
            await del_product_session(user_id)