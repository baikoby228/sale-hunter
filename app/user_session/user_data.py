class UserData:
    current_marketplace: str

    def __init__(self, type) -> None:
        self.type = type
        self.step = 0
        self.marketplaces = {}