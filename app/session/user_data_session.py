from models import UserData
from infra import get_user_data

session = {}

def create_user_session(id: int, chat_id: int, type: str, start_step: int) -> None:
    session[id] = UserData(id, chat_id, type, start_step)

def get_user_session(id: int, chat_id: int = None, type: str = 'None', start_step: int = -1) -> UserData:
    if not id in session:
        res = get_user_data(id)
        if res:
            chat_id, type, start_step = res
            session[id] = UserData(id, chat_id, type, start_step)
        else:
            create_user_session(id, chat_id, type, start_step)
    return session[id]

def del_user_session(id: int) -> None:
    del session[id]