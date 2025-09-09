class UserData:
    marketplace: str
    article: int
    max_price: int

    def __init__(self, type: str, start_step: int) -> None:
        self.type = type
        self.step = start_step