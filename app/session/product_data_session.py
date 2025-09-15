from models import ProductData

session = {}

def create_product_session(id: int) -> None:
    session[id] = ProductData(id)

def get_product_session(id: int) -> ProductData:
    if not id in session:
        create_product_session(id)
    return session[id]

def del_product_session(id: int) -> None:
    del session[id]