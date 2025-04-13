import sqlite3

def create_table():
    conn = sqlite3.connect("onigiri.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS onigiri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        energy TEXT,
        protein TEXT,
        fat TEXT,
        carbs TEXT,
        salt TEXT
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    print("🍙 onigiri テーブル作成完了！")
