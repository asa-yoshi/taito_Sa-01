import sqlite3
import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

# トップページ
@app.route('/')
def index():
    return render_template('index.html')

# 結果ページ
@app.route('/result', methods=['GET', 'POST'])
def result():
    ingredients = request.form.get('ingredients', '鶏むね肉, ブロッコリー')
    mood = request.form.get('mood', 'normal')

    recipe = "suggest_recipe 関数が未定義のため仮の文字列"
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute('INSERT INTO history (ingredients, mood, recipe) VALUES (?, ?, ?)',
              (ingredients, mood, recipe))
    conn.commit()
    conn.close()
    return render_template('result.html', recipe=recipe)

# レシピ一覧
@app.route('/recipes')
def show_recipes():
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute("SELECT title, category, ingredients, url FROM recipes")
    recipes = c.fetchall()
    conn.close()
    return render_template('recipes.html', recipes=recipes)

# 履歴表示
@app.route('/history')
def history():
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM history ORDER BY created_at DESC')
    rows = c.fetchall()
    conn.close()
    return render_template('history.html', records=rows)

@app.route('/category', methods=['GET', 'POST'])
def category():
    if request.method == 'POST':
        selected_url = request.form.get('url')
        items = get_items_from_url(selected_url)
        return render_template('items.html', items=items)
    return render_template('select_category.html')

def get_items_from_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    items = []
    for li in soup.select("ul.wrap > li"):
        try:
            title_tag = li.select_one("p.name a")
            title = title_tag.get_text(strip=True) if title_tag else "タイトル不明"

            values = [td.get_text(strip=True) for td in li.select("td.con_nut")]
            if len(values) < 5:
                continue

            item = {
                "title": title,
                "energy": values[0],
                "protein": values[1],
                "fat": values[2],
                "carbs": values[3],
                "salt": values[4]
            }
            items.append(item)
        except Exception as e:
            print(f"[ERROR] {e}")
            continue
    return items


# 🍙 おにぎりページ 
@app.route('/onigiri')
def onigiri():
    items = get_onigiri_items()
    return render_template('onigiri.html', items=items)

# 🔽 商品一覧からタイトル＋栄養を取得
def get_onigiri_items():
    url = "https://www.family.co.jp/goods/safety/goods010.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    items = []

    for li in soup.select("ul.wrap > li"):
        try:
            # タイトル取得
            a_tag = li.select_one("p.name a")
            title = a_tag.get_text(strip=True) if a_tag else "タイトル不明"

            # 栄養情報取得
            values = [td.get_text(strip=True) for td in li.select("td.con_nut")]
            if len(values) < 5:
                print(f"[WARNING] 栄養情報が足りません → {title}")
                continue

            item = {
                "title": title,
                "energy": values[0],
                "protein": values[1],
                "fat": values[2],
                "carbs": values[3],
                "salt": values[4]
            }
            items.append(item)

        except Exception as e:
            print(f"[ERROR] 処理失敗: {e}")
            continue

    return items

# ====================
# Flask起動
# ====================
if __name__ == '__main__':
    app.run(debug=True)
