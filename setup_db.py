import sqlite3

# データベース接続
conn = sqlite3.connect('recipes.db')
c = conn.cursor()

# テーブル作成
c.execute('''
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    category TEXT,
    ingredients TEXT,
    url TEXT,
    protein REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("✅ recipes テーブルを作成しました")
