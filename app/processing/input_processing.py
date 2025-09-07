from ..user_session import get_user_session
from .input_command_processing import (input_command_add_processing, input_command_del_processing,
                                       input_command_set_processing)

def input_processing(message) -> None:
    user_id = message.from_user.id
    chat_id = message.chat.id

    user = get_user_session(user_id)
    current_type = user.type

    match current_type:
        case 'add':
            input_command_add_processing(message)
        case 'del':
            input_command_del_processing(message)
        case 'set':
            input_command_set_processing(message)