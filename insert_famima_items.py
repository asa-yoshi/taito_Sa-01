from recipes import save_famima_item
from app import get_onigiri_items  # ← get_onigiri_items でデータを取得してる前提

items = get_onigiri_items()

for item in items:
    save_famima_item(item)
    print(f"✔︎ 登録: {item['title']}")  