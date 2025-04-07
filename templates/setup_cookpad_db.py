import sqlite3

# データベース接続（なければ作成）
conn = sqlite3.connect('recipes.db')
c = conn.cursor()

# テーブル作成
c.execute('''
CREATE TABLE IF NOT EXISTS cookpad_recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    title TEXT,
    url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()
print("✅ cookpad_recipes テーブルを作成しました")
