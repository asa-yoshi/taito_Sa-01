import sqlite3

conn = sqlite3.connect('recipes.db')
c = conn.cursor()

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
print("✅ データベースとテーブル作成完了")
