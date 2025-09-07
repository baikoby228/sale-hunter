import sqlite3
from pathlib import Path
from typing import List, Tuple

def create_db():
    db = sqlite3.connect(Path(__file__).parent / 'user_data_base.db')
    c = db.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS targets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            article INTEGER,
            max_price INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    db.commit()
    db.close()

def add_target(user_id: int, article: int, max_price: int):
    db = sqlite3.connect(Path(__file__).parent / 'user_data_base.db')
    c = db.cursor()

    c.execute("""
        INSERT INTO targets (user_id, article, max_price)
        VALUES (?, ?, ?)
    """, (user_id, article, max_price))

    db.commit()
    db.close()

def get_targets(user_id: int) -> List[Tuple[int, int]]:
    db = sqlite3.connect(Path(__file__).parent / 'user_data_base.db')
    c = db.cursor()

    c.execute("""
        SELECT article, max_price
        FROM targets
        WHERE user_id = ?
    """, (user_id,))

    res = c.fetchall()

    db.commit()
    db.close()

    return res

def del_target(user_id: int, article: str):
    db = sqlite3.connect(Path(__file__).parent / 'user_data_base.db')
    c = db.cursor()

    c.execute("""
        DELETE FROM targets
        WHERE user_id = ? AND article = ?
    """, (user_id, article))

    db.commit()
    db.close()

def check_target(user_id: int, article: str) -> bool:
    db = sqlite3.connect(Path(__file__).parent / 'user_data_base.db')
    c = db.cursor()

    c.execute("""
        SELECT 1 FROM targets
        WHERE user_id = ? AND article = ?
        LIMIT 1
    """, (user_id, article))

    res = c.fetchone()

    db.commit()
    db.close()

    return res is not None

def set_target_max_price(user_id: int, article: int, new_max_price: int):
    db = sqlite3.connect(Path(__file__).parent / 'user_data_base.db')
    c = db.cursor()

    c.execute("""
        UPDATE targets
        SET max_price = ?
        WHERE user_id = ? AND article = ?
    """, (new_max_price, user_id, article))

    db.commit()
    db.close()

def get_targets_amount(user_id: int) -> int:
    return len(get_targets(user_id))

if __name__ == '__main__':
    create_db()