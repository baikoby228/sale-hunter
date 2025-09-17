from ..session import get_user_session
from .command_add import processing_input_command_add
from .command_del import processing_input_command_del
from .command_set import processing_input_command_set

async def input_processing(user_id: int, chat_id: int, message_text: str = None) -> None:
    user = await get_user_session(user_id, chat_id)
    current_type = user.type

    match current_type:
        case 'add':
            await processing_input_command_add(user_id, chat_id, message_text)
        case 'del':
            await processing_input_command_del(user_id, chat_id, message_text)
        case 'set':
            await processing_input_command_set(user_id, chat_id, message_text)