# In Python gibt es scheinbar keie geschweiften Klammern, Python arbeitet mir Einrückungen
# if 2 < 3:
    # Logik im if
# else:
    # Login im else

if 2 < 3:
    print("Yes!")

shopping_list = ["Bananen", "Tomaten", "Kiwi"]

chosen_article = input("Bananen, Tomaten oder Kiwi?")

# mit dem Keyword in können wir direkt schauen ob etwas in einem Array existiert
if chosen_article in shopping_list:
    print(chosen_article, "sind auf der Liste!")
else:
    print(chosen_article, "sind nicht auf der Liste!")