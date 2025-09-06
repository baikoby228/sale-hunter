from .user_data import UserData

session = {}

def create_user_session(id: int, type: str):
    session[id] = UserData(type)
    return session[id]

def get_user_session(id: int):
    return session[id]

def del_user_session(id: int):
    del session[id]