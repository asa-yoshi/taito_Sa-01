import sqlite3

conn = sqlite3.connect("recipes.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS famima (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    energy TEXT,
    protein TEXT,
    fat TEXT,
    carbs TEXT,
    salt TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("famimaテーブルを作成しました。")
    