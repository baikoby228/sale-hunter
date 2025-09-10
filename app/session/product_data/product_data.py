class ProductData:
    marketplace: str
    article: int

    name: str
    photo_url: str
    current_price: int

    max_price: int

    def __init__(self, marketplace = None, article = None, name = None, photo_url = None, current_price = None, max_price = None):
        self.marketplace = marketplace
        self.article = article
        self.name = name
        self.photo_url = photo_url
        self.current_price = current_price
        self.max_price = max_price