"""Швидка перевірка підключення: створює тимчасову таблицю і читає її назад."""
from .db import get_engine

def main():
    engine = get_engine()
    with engine.begin() as conn:
        conn.exec_driver_sql("CREATE TABLE IF NOT EXISTS __ping__(id INTEGER PRIMARY KEY, note TEXT);")
        conn.exec_driver_sql("DELETE FROM __ping__;")
        conn.exec_driver_sql("INSERT INTO __ping__(note) VALUES ('ok');")
        res = conn.exec_driver_sql("SELECT COUNT(*) FROM __ping__").scalar_one()
        print(f"Ping OK, rows in __ping__: {res}")

if __name__ == "__main__":
    main()