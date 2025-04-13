import sqlite3

# DBに接続（なければ作成される）
conn = sqlite3.connect('recipes.db')
c = conn.cursor()

# テーブル作成
c.execute('''
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredients TEXT,
    mood TEXT,
    recipe TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("✅ history テーブルを作成しました")
