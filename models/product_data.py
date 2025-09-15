class ProductData:
    user_id: int

    marketplace: str
    article: int

    name: str
    photo_url: str
    current_price: int
    start_price: int
    add_time: str

    max_price: int

    def __init__(self, user_id = None, marketplace = None, article = None, name = None, photo_url = None,
                 current_price = None, start_price = None, add_time = None, max_price = None):
        self.user_id = user_id
        self.marketplace = marketplace
        self.article = article
        self.name = name
        self.photo_url = photo_url
        self.current_price = current_price
        self.start_price = start_price
        self.add_time = add_time
        self.max_price = max_price