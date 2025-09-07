import telebot

from dotenv import load_dotenv
import os

from config import MAX_AMOUNT_OF_TARGETS
from utils import find_number
from infra import add_target, check_target, get_targets_amount
from ...user_session import get_user_session, del_user_session
from ...wb_parser import wb_parser

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def input_command_add_processing(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    user = get_user_session(user_id)
    current_step = user.step

    match current_step:
        case 0:
            user.article = find_number(message.text)
            text = (
                'Введите максимальную подходящую цену товара для оповещения\n'
                'Примеры ввода:\n178,32 р.\n9.00 BYN\n41,00'
            )
            bot.send_message(chat_id, text, parse_mode='html')
            user.step += 1
        case 1:
            user.max_price = find_number(message.text)

            if check_target(user_id, user.article):
                text = 'Товар с эти артикулом уже отслеживается'
                bot.send_message(chat_id, text, parse_mode='html')
            elif get_targets_amount(user_id) == MAX_AMOUNT_OF_TARGETS:
                text = f'Достигнут лимит отслеживаемых товаров ({MAX_AMOUNT_OF_TARGETS})'
                bot.send_message(chat_id, text, parse_mode='html')
            else:
                text = 'Получение текущей цены товара...'
                bot.send_message(chat_id, text, parse_mode='html')

                current_price = find_number(wb_parser(user.article))
                if current_price <= user.max_price:
                    text = 'Товар на данный момент стоит меньше максимальной цены'
                    bot.send_message(chat_id, text, parse_mode='html')
                else:
                    add_target(user_id, user.article, user.max_price)
                    text = 'Товар добавлен в список отслеживаемых'
                    bot.send_message(chat_id, text, parse_mode='html')

            del_user_session(user_id)
