import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / 'data_base.db'

async def create_table() -> None:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            chat_id INTEGER,
            sort_type TEXT,
            sort_reverse BOOLEAN
            )
        """)

    db.commit()
    db.close()

async def get_user_data(id: int):
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("""
        SELECT chat_id, sort_type, sort_reverse FROM users
        WHERE id = ?
        """, (id,))

    res = c.fetchone()

    db.commit()
    db.close()

    return res if res else None

async def set_user_data(id: int, chat_id: int, sort_type: str, sort_reverse: bool) -> None:
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()

    c.execute("INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?)", (id, chat_id, sort_type, sort_reverse))

    db.commit()
    db.close()