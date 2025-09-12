from ..session import get_user_session
from .input_command_processing import (processing_input_command_add, processing_input_command_del,
                                       processing_input_command_set)

def input_processing(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    user = get_user_session(user_id)
    current_type = user.type

    match current_type:
        case 'add':
            processing_input_command_add(message)
        case 'del':
            processing_input_command_del(message)
        case 'set':
            processing_input_command_set(user_id, chat_id, message.text)