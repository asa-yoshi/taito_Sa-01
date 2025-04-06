import sqlite3
from flask import Flask, render_template, request
from recipes import suggest_recipe

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    ingredients = request.form.get('ingredients', '')
    mood = request.form.get('mood', 'normal')
    recipe = suggest_recipe(ingredients, mood)
    return render_template('result.html', recipe=recipe)

    # 🔽 DBに保存
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute('INSERT INTO history (ingredients, mood, recipe) VALUES (?, ?, ?)',
              (ingredients, mood, recipe))
    conn.commit()
    conn.close()

    return render_template('result.html', recipe=recipe)

# 🆕 履歴を表示するルート
@app.route('/history')
def history():
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM history ORDER BY created_at DESC')
    rows = c.fetchall()
    conn.close()
    return render_template('history.html', records=rows)        

if __name__ == '__main__':
    app.run(debug=True)
