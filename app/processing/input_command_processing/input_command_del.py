import telebot

from dotenv import load_dotenv
import os

from utils import find_number
from infra import del_target, check_target
from ...user_session import get_user_session, del_user_session

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def input_command_del_processing(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    user = get_user_session(user_id)
    current_step = user.step

    match current_step:
        case 0:
            user.article = find_number(message.text)

            if check_target(user_id, user.article):
                del_target(user_id, user.article)
                text = 'Товар удалён из списка отслеживаемых'
                bot.send_message(chat_id, text, parse_mode='html')
            else:
                text = 'Товара нету в списке отслеживаемых'
                bot.send_message(chat_id, text, parse_mode='html')

            del_user_session(user_id)