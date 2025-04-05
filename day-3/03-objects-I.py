# Objekt Methoden

article = {
    "name": "Vollmilch Schokolade",
    "color": "light brown",
    "price": 1.19,
    "weight": 100,
    "shops": ["Aldi", "Lidl", "Rewe"]
}

print(article)

print("""
------BRACKET-NOTATION------""")

print("Preis:", article["price"])
# ✅ Funktioniert, wenn der Key "shops" existiert
# ❌ Löst einen KeyError aus, wenn der Key nicht existiert
print("Shops:", article["shops"])
print("Index 1 aus Shops:",article["shops"][1])

print("""
------KEYS------""")

# Alle Keys des Objektes ausgeben
# Gibt ein Objekt zurück, das alle Schlüssel (Keys) enthält
print("Keys:", article.keys())

print("""
------GET------""")

# Zeige alle Werte eines Keys an
# ✅ Gibt den Wert zurück, wenn der Key existiert
# ✅ Gibt None zurück, wenn der Key nicht existiert (anstatt einen Fehler zu werfen)
print("get Methode ohne Fallback:", article.get("shops"))

# ✅ Du kannst sogar einen Standardwert mitgeben:
# ✅ Gibt den Fallback zurück, wenn der Key nicht existiert (anstatt None)
print("get Methode mit Fallback:", article.get("allshops", "Kein Key Names allshops gefunden!"))

print("""
------ITEMS------""")

# Alle Items des Objektes ausgeben
# Gibt ein Arrays zurück mit Unterarrays aber als Tupel
# in den Tupels steht dann immer das key-value Paar
print("Items:", article.items())

print("""
------VALUES------""")

# Alle Werte des Objektes ausgeben
print("Values:", article.values())

print("""
------SHALLOW-COPIE------""")

# Erstellt eine Shallow Copy des übergebenen Objektes oder Arrays
# übergabe = object oder array
# initialValue = überschreibt alle Daten mit diesem Wert
# fromkeys(übergabe, initialValue)
neues_dict = dict.fromkeys(article, "")
print("Shallow Kopie", neues_dict)

# Shallo Copy nur von Objekten!
print(article.copy())