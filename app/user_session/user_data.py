class UserData:
    current_marketplace: str

    def __init__(self) -> None:
        self.step = -1
        self.marketplaces = {}