import sqlite3
from pathlib import Path
from models.product_data import ProductData

DB_PATH = Path(__file__).parent / 'data_base.db'

def create_table() -> None:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            marketplace TEXT,
            article INTEGER,
            name TEXT,
            photo_url TEXT,
            current_price INTEGER,
            start_price INTEGER,
            add_time TEXT,
            max_price INTEGER
            )
        """)

    db.commit()
    db.close()

def add_product(product: ProductData) -> None:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        INSERT INTO products (
            user_id,
            marketplace,
            article,
            name,
            photo_url,
            current_price,
            start_price,
            add_time,
            max_price
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        product.user_id,
        product.marketplace,
        product.article,
        product.name,
        product.photo_url,
        product.current_price,
        product.start_price,
        product.add_time,
        product.max_price
    ))

    db.commit()
    db.close()

def get_products(user_id: int = None) -> list[ProductData]:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    if user_id:
        c.execute("""
            SELECT
                user_id,
                marketplace,
                article,
                name,
                photo_url,
                current_price,
                start_price,
                add_time,
                max_price
            FROM products
            WHERE user_id = ?
        """, (user_id,))
    else:
        c.execute("""
            SELECT
                user_id,
                marketplace,
                article,
                name,
                photo_url,
                current_price,
                start_price,
                add_time,
                max_price
            FROM products
        """)

    rows = c.fetchall()

    db.commit()
    db.close()

    return [ProductData(*row) for row in rows]

def get_product(user_id: int, marketplace: str, article: int) -> ProductData:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        SELECT
            user_id,
            marketplace,
            article,
            name,
            photo_url,
            current_price,
            start_price,
            add_time,
            max_price
        FROM products
        WHERE user_id = ? AND marketplace = ? AND article = ?
    """, (user_id, marketplace, article))

    res = c.fetchone()

    db.commit()
    db.close()

    return ProductData(*res)

def del_product(user_id: int, marketplace: str, article: int) -> None:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        DELETE FROM products
        WHERE user_id = ? AND marketplace = ? AND article = ?
    """, (user_id, marketplace, article))

    db.commit()
    db.close()

def check_product(user_id: int, marketplace: str, article: int) -> bool:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        SELECT 1 FROM products
        WHERE user_id = ? AND marketplace = ? AND article = ?
        LIMIT 1
    """, (user_id, marketplace, article))

    res = c.fetchone()

    db.commit()
    db.close()

    return res is not None

def get_products_amount(user_id: int = None) -> int:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    if user_id:
        c.execute("SELECT COUNT(*) FROM products WHERE user_id = ?", (user_id,))
    else:
        c.execute("SELECT COUNT(*) FROM products")

    res = c.fetchone()[0]

    db.commit()
    db.close()

    return res

def set_product_current_price(user_id: int, marketplace: str, article: int, new_current_price: int) -> None:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        UPDATE products
        SET current_price = ?
        WHERE user_id = ? AND marketplace = ? AND article = ?
    """, (new_current_price, user_id, marketplace, article))

    db.commit()
    db.close()

def get_product_current_price(user_id: int, marketplace: str, article: int) -> int:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        SELECT current_price
        FROM products
        WHERE user_id = ? AND marketplace = ? AND article = ?
        LIMIT 1
    """, (user_id, marketplace, article))

    row = c.fetchone()
    db.close()

    return row[0]

def set_product_max_price(user_id: int, marketplace: str, article: int, new_max_price: int) -> None:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        UPDATE products
        SET max_price = ?
        WHERE user_id = ? AND marketplace = ? AND article = ?
    """, (new_max_price, user_id, marketplace, article))

    db.commit()
    db.close()

def get_product_max_price(user_id: int, marketplace: str, article: int) -> int:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        SELECT max_price
        FROM products
        WHERE user_id = ? AND marketplace = ? AND article = ?
        LIMIT 1
    """, (user_id, marketplace, article))

    row = c.fetchone()
    db.close()

    return row[0]