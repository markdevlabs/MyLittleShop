import sqlite3
from contextlib import contextmanager
from typing import Generator

DB_NAME = 'shop.db'

@contextmanager
def get_connection() -> Generator[sqlite3.Connection, None, None]:
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
    finally:
        conn.commit()
        conn.close()

def create_tables() -> None:
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS seller_info(
                name TEXT,
                product TEXT,
                price INTEGER,
                id INTEGER PRIMARY KEY AUTOINCREMENT
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS user(
                name TEXT,
                lastname TEXT,
                age INTEGER,
                email TEXT UNIQUE,
                password TEXT,
                id INTEGER PRIMARY KEY AUTOINCREMENT
            )
        """)