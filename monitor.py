import asyncio
import time
import random

from config import CYCLE_TIME, CYCLE_TIME_DELTA,  REQUEST_TIME_DELTA
from infra import get_products_amount, get_products, set_product_current_price
from app import wb_parser, send_notification, ozon_parser
from models import ProductData

async def main():
    print('big_start')
    start_time = time.time()

    products_amount = await get_products_amount()
    if products_amount == 0:
        await asyncio.sleep(1)
        return

    request_time = CYCLE_TIME / products_amount
    print(f'request_time = {request_time}')

    products = await get_products()
    found_prices = {}

    for product in products:
        print('small_start')
        start_request_time = time.time()

        current_price: int | None
        if (product.marketplace, product.article) in found_prices:
            current_price = found_prices[(product.marketplace, product.article)]
        else:
            new_product: ProductData
            if product.marketplace == 'wb':
                new_product = await wb_parser(product.article)
            if product.marketplace == 'ozon':
                new_product = await ozon_parser(product.article)

            if new_product:
                current_price = new_product.current_price
                found_prices[(product.marketplace, product.article)] = current_price
            else:
                current_price = None
                found_prices[(product.marketplace, product.article)] = None

        if current_price is not None:
            await set_product_current_price(product.user_id, product.marketplace, product.article, current_price)
            if current_price <= product.max_price:
                product.current_price = current_price
                await send_notification(product)

        print('start_small_sleep')
        current_request_time = request_time * (1 + random.uniform(-REQUEST_TIME_DELTA, REQUEST_TIME_DELTA))
        while time.time() - start_request_time < current_request_time:
            await asyncio.sleep(0.17)
        print('end_small_sleep')
    print('start_big_sleep')
    while time.time() - start_time < CYCLE_TIME * (1 + random.uniform(0, CYCLE_TIME_DELTA)):
        await asyncio.sleep(0.97)
    print('end_big_sleep')

if __name__ == '__main__':
    asyncio.run(main())