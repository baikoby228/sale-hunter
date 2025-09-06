class UserData:
    article: int
    max_price: int

    def __init__(self, type) -> None:
        self.type = type
        self.step = 0