article = {
    "name": "Vollmilch Schokolade",
    "color": "light brown",
    "price": 1.19,
    "weight": 100,
    "shops": ["Aldi", "Lidl", "Rewe"]
}

# Wie in JS updaten eines Values
article["price"] = 1.34

# Hinzufügen eines key-value pairs
article["top_quality"] = True

print(article)

# Iterieren über ein Object

print("""
------FOR-KEYS------""")

# hier sehen wir aber nur die keys...
for element in article:
    print(element)

print("""
------FOR-[KEYS]------""")

# passen wir das etwas an element ist also key oder i
for key in article:
    print(article[key])