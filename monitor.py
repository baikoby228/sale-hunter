import time
import random

from config import ITERATION_TIME, DELTA
from infra import get_products_amount, get_products, set_product_current_price
from app import wb_parser, send_notification

while True:
    start_time = time.time()

    products_amount = get_products_amount()
    if products_amount == 0:
        time.sleep(1)
        continue
    request_time = ITERATION_TIME / products_amount

    products = get_products()
    found_prices = {}

    for product in products:
        start_request_time = time.time()

        current_price: int | None
        if (product.marketplace, product.article) in found_prices:
            current_price = found_prices[(product.marketplace, product.article)]
        else:
            if product.marketplace == 'wb':
                new_product = wb_parser(product.article)
                if new_product:
                    current_price = new_product.current_price
                    found_prices[(product.marketplace, product.article)] = current_price
                else:
                    current_price = None
                    found_prices[(product.marketplace, product.article)] = None

        if current_price:
            set_product_current_price(product.user_id, product.marketplace, product.article, current_price)
            if current_price <= product.max_price:
                product.current_price = current_price
                send_notification(product)

        current_request_time = request_time * (1 + random.uniform(-DELTA, DELTA))
        while time.time() - start_request_time < current_request_time:
            time.sleep(0.11)
    while time.time() - start_time < ITERATION_TIME:
        time.sleep(1.01)