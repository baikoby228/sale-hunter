import logging
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv
import os

from infra import get_products, get_products_amount
from utils import format_price_byn
from config import MAX_AMOUNT_OF_PRODUCTS, INF
from ...session import get_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

async def processing_command_menu(user_id: int, chat_id: int) -> None:
    user = await get_user_session(user_id, chat_id)

    amount = await get_products_amount(user_id)
    products = await get_products(user_id)

    markup = InlineKeyboardMarkup(inline_keyboard=[])

    button_settings = InlineKeyboardButton(text='⚙️ Настройки сортировки', callback_data='settings_sort')
    markup.inline_keyboard.append([button_settings])

    if len(products) == 0:
        button_add = InlineKeyboardButton(text='➕ Добавить товар', callback_data='add')
        markup.inline_keyboard.append([button_add])

    text = (
        f'Меню ({amount}/{MAX_AMOUNT_OF_PRODUCTS})\n'
        '...'
    )

    await bot.send_message(chat_id, text, parse_mode='html', reply_markup=markup)

    if user.sort_type == 'date':
        products.sort(key=lambda product: product.add_time, reverse=user.sort_reverse)
    if user.sort_type == 'current_price':
        products.sort(key=lambda product: product.current_price, reverse=user.sort_reverse)

    for i in range(len(products)):
        product = products[i]

        markup = InlineKeyboardMarkup(inline_keyboard=[])

        emoji1 = ''
        emoji2 = ''
        if product.marketplace == 'wb':
            emoji1 = '🟣'
            emoji2 = '🟣'
        if product.marketplace == 'ozon':
            emoji1 = '🔵'
            emoji2 = '🔴'

        text = f'{emoji1} {product.marketplace.upper()} - {product.article} {emoji2}'
        button_info = InlineKeyboardButton(text=text, callback_data=f'info_{product.marketplace}_{product.article}')
        markup.inline_keyboard.append([button_info])

        text = '✏️ Изменить'
        button_set = InlineKeyboardButton(text=text, callback_data=f'set_{product.marketplace}_{product.article}')

        text = '🗑️ Удалить'
        button_del = InlineKeyboardButton(text=text, callback_data=f'del_{product.marketplace}_{product.article}')

        markup.inline_keyboard.append([button_set, button_del])

        if i == len(products) - 1 and amount != MAX_AMOUNT_OF_PRODUCTS:
            button_add = InlineKeyboardButton(text='➕ Добавить товар', callback_data='add')
            markup.inline_keyboard.append([button_add])

        string_current_price: str
        if product.current_price == INF:
            string_current_price = 'нету в наличии'
        else:
            string_current_price = f'{format_price_byn(product.current_price)}'

        text = (
            f'{product.name[:min(len(product.name), 17)]}...\n'
            f'{format_price_byn(product.max_price)} - {string_current_price}'
        )
        await bot.send_message(chat_id, text=text, parse_mode='html', reply_markup=markup)