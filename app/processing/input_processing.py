from ..session import get_user_session
from .input_command_processing import (processing_input_command_add, processing_input_command_del,
                                       processing_input_command_set)

def input_processing(user_id: int, chat_id: int, message_text: str = None) -> None:
    user = get_user_session(user_id)
    current_type = user.type

    match current_type:
        case 'add':
            processing_input_command_add(user_id, chat_id, message_text)
        case 'del':
            processing_input_command_del(user_id, chat_id, message_text)
        case 'set':
            processing_input_command_set(user_id, chat_id, message_text)