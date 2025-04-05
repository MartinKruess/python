# In Python gibt es zwei unterschiedliche Arten von Objekten
# Wir haben bereits beide Arten gesehen.

print("------DICTIONARYS------")

# Keys müssen Strings sein (wie in JSON)
# Nachstehende Kommatas sind Pflicht!
user_dictionary = {
    "first_name": "Max",
    "last_name": "Mustermann",
    "age": 30
}

# Dadurch, dass die Keys Strings sind...
# müssen wir die bracket notation verwenden!
# dot notatrion funktioniert nicht!
print(user_dictionary["first_name"])
print(user_dictionary["last_name"])
print(user_dictionary["age"])

print("------CLASS-OBJECTS------")

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

user1 = User("Lisa", "Lustig", 32)

print(user1)

# dot notation funktioniert
# bracket notation funktioniert nicht!
print(user1.first_name)
print(user1.last_name)
print(user1.age)


# Ein kurzer Test

def title(car):
    return f"{car['brand']} mit {car['ps']} PS!"

golf = {
    "brand": "VW",
    "color": "red",
    "ps": 65,
    "title": title
}

print(golf["title"](golf))

# Ok das hat irgendwie funktioniert xD

"""
Kurze Erklärung:

Wir können wie gewohnt unseren Objekten Methoden hinzufügen,
allerdings müssen wir das dann wie oben tun.

    Dies ist der Schlüssel um an die Daten zu kommen!
    return f"{car['brand']} mit {car['ps']} PS!"

    1. f'...'
    Das f vor dem String aktiviert den f-String-Modus
    Dadurch können wir Code in Strings ausgeben

    in JS wäre das der Template String: `${variable}`

    in Python der f-String-Modus: f'{variable}'
"""