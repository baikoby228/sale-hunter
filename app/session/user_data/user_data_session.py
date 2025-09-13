from .user_data import UserData

session = {}

def create_user_session(id: int, type: str, start_step: int) -> None:
    session[id] = UserData(id, type, start_step)

def get_user_session(id: int, type: str = 'None', start_step: int = -1) -> UserData:
    if not id in session:
        create_user_session(id, type, start_step)
    return session[id]

def del_user_session(id: int) -> None:
    del session[id]