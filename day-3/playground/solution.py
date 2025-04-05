phone_book = {
    "Tina": "0153 832 361",
    "Bernd": "0178 545 443",
    "Susi": "0156 965 447",
    "Günni": "0170 831 457",
    "Lisa": "0176 161 86 20",
    "Max": "0165 448 35 11",
}

# Aufgabe - Telefonbuch (erzeuge keine Dopplungen!)

# 1. Erstelle je eine Funktion, die...
    # - einen Namen und eine Nummer hinzufügt
        # - passende Länge der Nummer min. 12 Zeichen max. 15 zeichen
    # - eine Nummer anhand des Namens herausfindet

def createEntrie(name, number):
    if len(number) < 12:
        return "Die Nummer", number, "ist zu kurz!"
    elif len(number) > 15:
        return "Die Nummer", number, "ist zu lang!"
    else:
        phone_book[name] = number
        return name, "wurde auf dem Telefonbuch mit der Nummer", number, "hinzugefügt!"

def findEntrie(name):
    if name in phone_book:
        return name, phone_book[name]
    else:
        return "Keinen Eintrag zum Namen", name, "gefunden!"

# 2. Hauptteil deines Programms
    # - Biete dem User folgende Möglichkeiten:
        # - find Number
        # - add Number
        # - exit Program
        #! Schaue hierfür in die Unterlagen!

while True:
    select = input("""Welchen Service möchtets du nutzen?
    - find
    - add
    - edit
    - delete
    - exit               
    """)

    if select == "find":
        find_name = input("Nach wem suchst du? ")
        result = findEntrie(find_name)
        print(result)
    elif select == "add":
        create_name = input("Gib den Namen an: ")
        create_number = input("Gib die Nummer an: ")
        result = createEntrie(create_name, create_number)
        print(result)
# 3. Bonus
    # - füge die Funktionen und Punkte Edit und Delete hinzu
    elif select == "edit":
        find_name = input("Nach wem suchst du? ")
        edit_entry = findEntrie(find_name)
        if edit_entry[0] == find_name:
            new_number = input("gib die neue Nummer ein: ")
            result = createEntrie(find_name, new_number)
            print(result)
        else:
            print("Keinen Eintrag gefunden, der bearbeitet werden kann!")
    elif select == "delete":
        remove_entry = input("Gib den zu löschenden Namen ein: ")
        del phone_book[remove_entry]
        print(remove_entry, "wurde auf dem Telefonbuch gelöscht!")
    else:
        print("Der Service wird beendet!")
        break
