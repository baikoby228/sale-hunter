import telebot

from dotenv import load_dotenv
import os

from utils import find_number
from infra import del_target, check_target
from ...session import get_user_session, del_user_session, get_product_session, del_product_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def input_command_del_processing(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    user = get_user_session(user_id)
    current_step = user.step

    product = get_product_session(user_id)

    match current_step:
        case 0:
            product.article = find_number(message.text)

            if check_target(user_id, product.marketplace, product.article):
                del_target(user_id, product.marketplace, product.article)
                text = 'Товар удалён из списка отслеживаемых'
                bot.send_message(chat_id, text, parse_mode='html')
            else:
                text = 'Товара нету в списке отслеживаемых'
                bot.send_message(chat_id, text, parse_mode='html')

            del_user_session(user_id)
            del_product_session(user_id)