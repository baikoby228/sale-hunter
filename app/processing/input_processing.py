import telebot

from dotenv import load_dotenv
import os

from ..user_session import get_user_session, del_user_session
from ..wb_parser import wb_parser
from utils import find_number

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def input_processing(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    user = get_user_session(user_id)
    current_step = user.step

    match current_step:
        case 0:
            user.marketplaces[user.current_marketplace].article = find_number(message.text)
            text = (
                'Введите максимальную подходящую цену товара для оповещения\n'
                'Примеры ввода:\n178,32 р.\n9.00 BYN\n41,00'
            )
            bot.send_message(chat_id, text, parse_mode='html')
            user.step += 1
        case 1:
            user.marketplaces[user.current_marketplace].max_price = find_number(message.text)

            text = 'Получение текущей цены товара...'
            bot.send_message(chat_id, text, parse_mode='html')

            current_price = find_number(wb_parser(user.marketplaces[user.current_marketplace].article))
            if current_price > user.marketplaces[user.current_marketplace].max_price:
                # тут будет добавление
                print(user.marketplaces[user.current_marketplace].article)
                print(user.marketplaces[user.current_marketplace].max_price)
                text = 'Товар добавлен в список отслеживаемых'
                bot.send_message(chat_id, text, parse_mode='html')
            else:
                text = 'Товар и так стоит меньше максимальной цены'
                bot.send_message(chat_id, text, parse_mode='html')

            del_user_session(user_id)