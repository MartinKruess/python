# Complexe Datentypen - Listen/Array Methoden

shopping_list = ["Tomaten"]

print("""
------ARR-APPEND------""")

# normales push -> append
# In python können wir nur 1 Item pushen!
shopping_list.append("Bananen")
print(shopping_list)

print("""
------ARR-LENGTH-MIN-MAX------""")

print("arr Länge", len(shopping_list))

# Gibt das 1. Element aus
print("Element an Index 0:", min(shopping_list))

# Gibt das letzte Element aus
print("Element and Index -1:", max(shopping_list))


print("""
------ARR-INSERT------""")

# push wie einfügen mit splice -> insert
# ABER auch wieder nur einzelne Items

# push "Kiwi" an Index 1
shopping_list.insert(1, "Kiwi")
print(shopping_list)

# push "Schokolade" an Index 1
shopping_list.insert(1, "Schokolade")
print(shopping_list)

print("""
------ARR-SLICE------""")

# Ausgabe von Index1 bis Index2
# index1 = Schokolade (inclusiv)
# index3 = Banane (exclusiv)
print(shopping_list[1:3])

middel_part_of_shopping_list = shopping_list[1:3]

print("original shopping_list:", shopping_list)
print("middel_part_of_shopping_list:", middel_part_of_shopping_list)

print("""
------ARR-REMOVE-ITEM------""")

middel_part_of_shopping_list.remove("Kiwi")

# Kiwi verschwindet nur aus der Kopie, nicht aber aus dem original Array!
print("original shopping_list:", shopping_list)
print("middel_part_of_shopping_list:", middel_part_of_shopping_list)
print("Wir sehen, das middel... Array ist eine echte Kopie!")

print("""
------ARR-POP------""")

# löscht das letzte Element
deleted_item = middel_part_of_shopping_list.pop()

print(deleted_item, "wurde gelöscht! Die neue Liste sieht so aus:", middel_part_of_shopping_list)

print("""
------DEL------""")

print("vor dem Löschen:",shopping_list)


# delete Item an Index 1 aus der Liste
del shopping_list[1]

print("nach dem Löschen:", shopping_list)

print("""
------🌟-LIST-COMPREHENSION-🌟------""")

# List Comprehension 🌟
# eine kompakte und elegante Möglichkeit, in Python Listen zu erstellen, ohne eine Schleife schreiben zu müssen

# 🐌 Liste mit Zahlen erstellen mit einer normalen Schleife:
numbers1 = []
for i in range(5):
    numbers1.append(i * 2)
print("klassich:", numbers1)

# ⚡ Liste mit Zahlen erstellen mit List Comprehension:
numbers2 = [i * 2 for i in range(5)]
print("Comprehension:", numbers2)
