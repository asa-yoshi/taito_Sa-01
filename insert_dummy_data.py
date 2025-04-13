import sqlite3

# ダミーデータ一覧
dummy_recipes = [
    ("鶏むね肉の照り焼き", "主菜", "鶏むね肉, 醤油, みりん, 砂糖", "https://cookpad.com/recipe/0001", 32.0),
    ("ブロッコリーのナムル", "副菜", "ブロッコリー, ごま油, 塩", "https://cookpad.com/recipe/0002", 4.5),
    ("豆腐とわかめの味噌汁", "スープ", "豆腐, わかめ, 味噌", "https://cookpad.com/recipe/0003", 8.2),
    ("ツナと大根のサラダ", "サラダ", "ツナ缶, 大根, マヨネーズ", "https://cookpad.com/recipe/0004", 10.0),
    ("ゆで卵", "副菜", "卵", "https://cookpad.com/recipe/0005", 6.0)
]

# データベースに接続
conn = sqlite3.connect('recipes.db')
c = conn.cursor()

# データを挿入
c.executemany('''
INSERT INTO recipes (title, category, ingredients, url, protein)
VALUES (?, ?, ?, ?, ?)
''', dummy_recipes)

conn.commit()
conn.close()

print("✅ ダミーレシピを5件追加しました！")