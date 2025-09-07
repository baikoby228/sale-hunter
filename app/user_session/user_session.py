from .user_data import UserData

session = {}

def create_user_session(id: int, type: str, start_step: int):
    session[id] = UserData(type, start_step)
    return session[id]

def get_user_session(id: int):
    if not id in session:
        create_user_session(id, 'None', 0)
    return session[id]

def del_user_session(id: int):
    del session[id]