from models import ProductData
from infra import add_product

import asyncio
from infra.database import connector_products
from infra.database import connector_users
async def create_tables() -> None:
    await connector_users.create_table()
    await connector_products.create_table()

from app.parsers.ozon_parser import get_html, ozon_parser
async def main(article: int) -> None:
    product = await ozon_parser(article)
    print(f'name = {product.name}')
    print(f'pr = {product.current_price}')
    print(f'url = {product.photo_url}')

if __name__ == '__main__':
    #asyncio.run(create_tables())
    article = 2415425494
    asyncio.run(main(article=article))

async def add_test_products(user_id: int, chat_id: int) -> None:
    return
    product = ProductData(user_id, 'wb', 307819738, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          15000, 15000, '2025-09-16 10:11', 12000)
    await add_product(product)
    product = ProductData(user_id, 'ozon', 1414409777, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          15000,  15000, '2025-09-16 10:11', 12000)
    await add_product(product)
    product = ProductData(user_id, 'wb', 214960980, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          3210,  3210, '2025-09-16 10:11', 3209)
    await add_product(product)
    product = ProductData(user_id, 'wb', 293395799, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2612,  2612, '2025-09-16 10:11', 2611)
    await add_product(product)
    product = ProductData(user_id, 'wb', 463685914, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1128,  1128, '2025-09-16 10:11', 1127)
    await add_product(product)
    product = ProductData(user_id, 'wb', 150297737, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          514,  514, '2025-09-16 10:11', 513)
    await add_product(product)
    product = ProductData(user_id, 'wb', 174990597, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2127,  2127, '2025-09-16 10:11', 2126)
    await add_product(product)
    product = ProductData(user_id, 'wb', 376608441, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          5943,  5943, '2025-09-16 10:11', 5942)
    await add_product(product)
    product = ProductData(user_id, 'wb', 31019930, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1179,  1179, '2025-09-16 10:11', 1178)
    await add_product(product)
    product = ProductData(user_id, 'wb', 312175416, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          5233,  5233, '2025-09-16 10:11', 5232)
    await add_product(product)
    product = ProductData(user_id, 'wb', 295624792, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2063,  2063, '2025-09-16 10:11', 2062)
    await add_product(product)
    product = ProductData(user_id, 'wb', 322164848, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2859,  2859, '2025-09-16 10:11', 2858)
    await add_product(product)
    product = ProductData(user_id, 'wb', 267310826, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          7301,  7301, '2025-09-16 10:11', 7300)
    await add_product(product)
    product = ProductData(user_id, 'wb', 223376823, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1342,  1342, '2025-09-16 10:11', 1341)
    await add_product(product)
    product = ProductData(user_id, 'wb', 494631116, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          9063,  9063, '2025-09-16 10:11', 9062)
    await add_product(product)
    product = ProductData(user_id, 'wb', 327346501, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          5296,  5296, '2025-09-16 10:11', 5295)
    await add_product(product)
    product = ProductData(user_id, 'wb', 175935456, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1041,  1041, '2025-09-16 10:11', 1040)
    await add_product(product)
    product = ProductData(user_id, 'wb', 209666407, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          31637,  31637, '2025-09-16 10:11', 31636)
    await add_product(product)
    product = ProductData(user_id, 'wb', 163352692, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2045,  2045, '2025-09-16 10:11', 2044)
    await add_product(product)
    product = ProductData(user_id, 'wb', 399760528, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          3233,  3233, '2025-09-16 10:11', 3232)
    await add_product(product)
    product = ProductData(user_id, 'wb', 276267243, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1134,  1134, '2025-09-16 10:11', 1133)
    await add_product(product)
    product = ProductData(user_id, 'wb', 322912169, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          7091,  7091, '2025-09-16 10:11', 7090)
    await add_product(product)
    product = ProductData(user_id, 'wb', 50238954, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          5014,  5014, '2025-09-16 10:11', 5013)
    await add_product(product)
    product = ProductData(user_id, 'wb', 148674008, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1143,  1143, '2025-09-16 10:11', 1142)
    await add_product(product)
    product = ProductData(user_id, 'wb', 134050297, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1336,  1336, '2025-09-16 10:11', 1335)
    await add_product(product)
    product = ProductData(user_id, 'wb', 228680705, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1851,  1851, '2025-09-16 10:11', 1850)
    await add_product(product)
    product = ProductData(user_id, 'wb', 372030450, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1296,  1296, '2025-09-16 10:11', 1295)
    await add_product(product)
    product = ProductData(user_id, 'wb', 303240677, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1840,  1840, '2025-09-16 10:11', 1839)
    await add_product(product)
    product = ProductData(user_id, 'wb', 293207129, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1281,  1281, '2025-09-16 10:11', 1280)
    await add_product(product)
    product = ProductData(user_id, 'wb', 273111361, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2868,  2868, '2025-09-16 10:11', 2867)
    await add_product(product)
    product = ProductData(user_id, 'wb', 23651254, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          16404,  16404, '2025-09-16 10:11', 16403)
    await add_product(product)
    product = ProductData(user_id, 'wb', 304634534, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1681,  1681, '2025-09-16 10:11', 1680)
    await add_product(product)
    product = ProductData(user_id, 'wb', 217353421, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          4074,  4074, '2025-09-16 10:11', 4073)
    await add_product(product)
    product = ProductData(user_id, 'wb', 185671213, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          6222,  6222, '2025-09-16 10:11', 6221)
    await add_product(product)
    product = ProductData(user_id, 'wb', 492810820, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          15356,  15356, '2025-09-16 10:11', 15355)
    await add_product(product)
    product = ProductData(user_id, 'wb', 7807903, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1868,  1868, '2025-09-16 10:11', 1867)
    await add_product(product)
    product = ProductData(user_id, 'wb', 273095379, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          13235,  13235, '2025-09-16 10:11', 13234)
    await add_product(product)
    product = ProductData(user_id, 'wb', 378936841, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1441,  1441, '2025-09-16 10:11', 1440)
    await add_product(product)
    product = ProductData(user_id, 'wb', 126897737, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1281,  1281, '2025-09-16 10:11', 1280)
    await add_product(product)
    product = ProductData(user_id, 'wb', 133625091, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1028,  1028, '2025-09-16 10:11', 1027)
    await add_product(product)
    product = ProductData(user_id, 'wb', 318231385, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1054,  1054, '2025-09-16 10:11', 1053)
    await add_product(product)
    product = ProductData(user_id, 'wb', 231344541, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          4880,  4880, '2025-09-16 10:11', 4879)
    await add_product(product)
    product = ProductData(user_id, 'wb', 321856538, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1459,  1459, '2025-09-16 10:11', 1458)
    await add_product(product)
    product = ProductData(user_id, 'wb', 171957947, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          13423,  13423, '2025-09-16 10:11', 13422)
    await add_product(product)
    product = ProductData(user_id, 'wb', 177487408, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          4137,  4137, '2025-09-16 10:11', 4136)
    await add_product(product)
    product = ProductData(user_id, 'wb', 176559965, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2169,  2169, '2025-09-16 10:11', 2168)
    await add_product(product)
    product = ProductData(user_id, 'wb', 102136669, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1834,  1834, '2025-09-16 10:11', 1833)
    await add_product(product)
    product = ProductData(user_id, 'wb', 309025813, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2321,  2321, '2025-09-16 10:11', 2320)
    await add_product(product)
    product = ProductData(user_id, 'wb', 279544520, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1311,  1311, '2025-09-16 10:11', 1310)
    await add_product(product)
    product = ProductData(user_id, 'wb', 216157923, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          3430,  3430, '2025-09-16 10:11', 3429)
    await add_product(product)
    product = ProductData(user_id, 'wb', 237976737, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1887,  1887, '2025-09-16 10:11', 1886)
    await add_product(product)
    product = ProductData(user_id, 'wb', 192146969, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1073,  1073, '2025-09-16 10:11', 1072)
    await add_product(product)
    product = ProductData(user_id, 'wb', 252243754, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1907,  1907, '2025-09-16 10:11', 1906)
    await add_product(product)
    product = ProductData(user_id, 'wb', 114407751, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          4119,  4119, '2025-09-16 10:11', 4118)
    await add_product(product)
    product = ProductData(user_id, 'wb', 165875418, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          3812,  3812, '2025-09-16 10:11', 3811)
    await add_product(product)
    product = ProductData(user_id, 'wb', 211860789, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          4394,  4394, '2025-09-16 10:11', 4393)
    await add_product(product)
    product = ProductData(user_id, 'wb', 210772536, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          3666,  3666, '2025-09-16 10:11', 3665)
    await add_product(product)
    product = ProductData(user_id, 'wb', 302201478, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2600,  2600, '2025-09-16 10:11', 2599)
    await add_product(product)
    product = ProductData(user_id, 'wb', 215171768, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1430,  1430, '2025-09-16 10:11', 1429)
    await add_product(product)
    product = ProductData(user_id, 'wb', 478100479, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          11506,  11506, '2025-09-16 10:11', 11505)
    await add_product(product)
    product = ProductData(user_id, 'wb', 254222294, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          6279,  6279, '2025-09-16 10:11', 6278)
    await add_product(product)
    product = ProductData(user_id, 'wb', 394392742, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          10639,  10639, '2025-09-16 10:11', 10638)
    await add_product(product)
    product = ProductData(user_id, 'wb', 162711178, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          6571,  6571, '2025-09-16 10:11', 6570)
    await add_product(product)
    product = ProductData(user_id, 'wb', 123419931, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          807,  807, '2025-09-16 10:11', 806)
    await add_product(product)
    product = ProductData(user_id, 'wb', 158704002, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1194,  1194, '2025-09-16 10:11', 1193)
    await add_product(product)
    product = ProductData(user_id, 'wb', 185422945, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2157,  2157, '2025-09-16 10:11', 2156)
    await add_product(product)
    product = ProductData(user_id, 'wb', 12571593, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          3416,  3416, '2025-09-16 10:11', 3415)
    await add_product(product)
    product = ProductData(user_id, 'wb', 216413341, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1795,  1795, '2025-09-16 10:11', 1794)
    await add_product(product)
    product = ProductData(user_id, 'wb', 270901464, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2135,  2135, '2025-09-16 10:11', 2134)
    await add_product(product)
    product = ProductData(user_id, 'wb', 241531325, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1457,  1457, '2025-09-16 10:11', 1456)
    await add_product(product)
    product = ProductData(user_id, 'wb', 221980284, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2116,  2116, '2025-09-16 10:11', 2115)
    await add_product(product)
    product = ProductData(user_id, 'wb', 445355318, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1296,  1296, '2025-09-16 10:11', 1295)
    await add_product(product)
    product = ProductData(user_id, 'wb', 154508866, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1431,  1431, '2025-09-16 10:11', 1430)
    await add_product(product)
    product = ProductData(user_id, 'wb', 171494039, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2218,  2218, '2025-09-16 10:11', 2217)
    await add_product(product)
    product = ProductData(user_id, 'wb', 257389562, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          7388,  7388, '2025-09-16 10:11', 7387)
    await add_product(product)
    product = ProductData(user_id, 'wb', 37031924, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          19370,  19370, '2025-09-16 10:11', 19369)
    await add_product(product)
    product = ProductData(user_id, 'wb', 14504537, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1237,  1237, '2025-09-16 10:11', 1236)
    await add_product(product)
    product = ProductData(user_id, 'wb', 445484626, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1229,  1229, '2025-09-16 10:11', 1228)
    await add_product(product)
    product = ProductData(user_id, 'wb', 228694961, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          3112,  3112, '2025-09-16 10:11', 3111)
    await add_product(product)
    product = ProductData(user_id, 'wb', 217757709, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          5290,  5290, '2025-09-16 10:11', 5289)
    await add_product(product)
    product = ProductData(user_id, 'wb', 232876440, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          3021,  3021, '2025-09-16 10:11', 3020)
    await add_product(product)
    product = ProductData(user_id, 'wb', 492810825, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          12075,  12075, '2025-09-16 10:11', 12074)
    await add_product(product)
    product = ProductData(user_id, 'wb', 171618037, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          583,  583, '2025-09-16 10:11', 582)
    await add_product(product)
    product = ProductData(user_id, 'wb', 260473795, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2109,  2109, '2025-09-16 10:11', 2108)
    await add_product(product)
    product = ProductData(user_id, 'wb', 452271123, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          7684,  7684, '2025-09-16 10:11', 7683)
    await add_product(product)
    product = ProductData(user_id, 'wb', 209038735, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2076,  2076, '2025-09-16 10:11', 2075)
    await add_product(product)
    product = ProductData(user_id, 'wb', 420681687, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          49598,  49598, '2025-09-16 10:11', 49597)
    await add_product(product)
    product = ProductData(user_id, 'wb', 315419547, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1791,  1791, '2025-09-16 10:11', 1790)
    await add_product(product)
    product = ProductData(user_id, 'wb', 253145695, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1604,  1604, '2025-09-16 10:11', 1603)
    await add_product(product)
    product = ProductData(user_id, 'wb', 157337880, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1422,  1422, '2025-09-16 10:11', 1421)
    await add_product(product)
    product = ProductData(user_id, 'wb', 199959150, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          3025,  3025, '2025-09-16 10:11', 3024)
    await add_product(product)
    product = ProductData(user_id, 'wb', 156411600, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1161,  1161, '2025-09-16 10:11', 1160)
    await add_product(product)
    product = ProductData(user_id, 'wb', 228691098, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          9112,  9112, '2025-09-16 10:11', 9111)
    await add_product(product)
    product = ProductData(user_id, 'wb', 299560632, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1392,  1392, '2025-09-16 10:11', 1391)
    await add_product(product)
    product = ProductData(user_id, 'wb', 316619860, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          17639,  17639, '2025-09-16 10:11', 17638)
    await add_product(product)
    product = ProductData(user_id, 'wb', 94572379, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1641,  1641, '2025-09-16 10:11', 1640)
    await add_product(product)
    product = ProductData(user_id, 'wb', 303955351, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2903,  2903, '2025-09-16 10:11', 2902)
    await add_product(product)
    product = ProductData(user_id, 'wb', 223802891, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2635,  2635, '2025-09-16 10:11', 2634)
    await add_product(product)
    product = ProductData(user_id, 'wb', 294409952, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          1924,  1924, '2025-09-16 10:11', 1923)
    await add_product(product)
    product = ProductData(user_id, 'wb', 399764294, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          3236,  3236, '2025-09-16 10:11', 3235)
    await add_product(product)
    product = ProductData(user_id, 'wb', 27765179, '*описание товара*',
                          'https://basket-05.wbbasket.ru/vol734/part73458/73458197/images/c246x328/1.webp',
                          2997,  2997, '2025-09-16 10:11', 2996)
    await add_product(product)