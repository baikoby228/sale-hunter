class UserData:
    article: int
    max_price: int

    def __init__(self, type, start_step) -> None:
        self.type = type
        self.step = start_step