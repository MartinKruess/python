# Complexe Datentypen - 🌟 Tupel 🌟

# Listen sind Arrays und diese sind veränderbar
shopping_list = ["Tomaten", "Bananen", "Kiwi"]
shopping_list[1] = "Schokolade"
print("shopping_list:", shopping_list, "Type:", type(shopping_list))

# Ein Tupel ist ein Array, dass unveränderbar ist um die integrität einer Liste bzw. der Daten in der Liste zu bewahren!

# Ein Tupel wird statt mit [] mit () gebaut!
shopping_list_fixed = ("Tomaten", "Bananen", "Kiwi")
print("shopping_list:", shopping_list_fixed, "Type:", type(shopping_list_fixed))

# Du kannst mit Tupel alles machen, was du mit Listen machen kannst, außer diese zu verändern, also Hinzufügen, Ändern, Löschen geht nicht. Probiere die folgenden Kommentare aus.

# shopping_list_fixed.append("Brot")

# shopping_list_fixed.insert(1, "Brot")

# shopping_list_fixed.pop()

# shopping_list_fixed.remove("Bananen")

# del shopping_list_fixed[1]

print("Tuple am Ende", shopping_list_fixed)