def suggest_recipe(ingredients, mood):
    if mood == "tired":
        return "簡単5分レシピ：鶏むねとブロッコリーのレンジ蒸し"
    elif mood == "busy":
        return "コンビニで済ませる高たんぱくセット（サラダチキン＋ゆで卵）"
    else:
        if "鶏むね肉" in ingredients and "ブロッコリー" in ingredients:
            return "鶏むね肉とブロッコリーの塩炒め"
        elif "鶏むね肉" in ingredients:
            return "鶏むね肉の梅しそ焼き"
        return "高たんぱくオートミールチャーハン"
