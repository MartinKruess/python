# Aufgabe - Teilnehmerliste verwalten

# 1. Erstelle eine leere Liste
    # füge mindestens 5 Teilnehmern hinzu
        # die Daten jedes Teilnehmers sollen:
            # Name, Alter, Abteilung
            # und unveränderbar sein!

employees = []

employees.append(("Susi", 32, "HR"))
employees.append(("Max", 35, "Production"))
employees.append(("Lisa", 38, "Production"))
employees.append(("Günni", 54, "Marketing"))
employees.append(("Dörte", 43, "Marketing"))

print("""
---TASK-1---""")

print(employees)


# 2. Gib alle Namen der Teilnehmer in einer Schleife aus.

print("""
---TASK-2---""")


for elem in employees:
    print(elem)

# 3. Zeige nur die Teilnehmer an, die über 18 Jahre alt sind.

print("""
---TASK-3---""")

count = 0
even_age_employees = []

for elem in employees:
    if elem[1] % 2 == 0:
        count += 1
        even_age_employees.append(elem)
        print(elem)

# 4. Zähle, wie viele Teilnehmer ein gerades Alter (durch 2 teilbar) haben.
    # Erstelle eine neue Liste, die nur die Namen der Teilnehmer enthält, bei denen das Alter durch 2 teilbar ist.

print("""
---TASK-4---""")

print(count)
print(even_age_employees)

# 5. Du hast den Chef (Leonardo, 41, "Chef") vergessen, führ ihn am Anfang der Liste hinzu

print("""
---TASK-5---""")

employees.insert(0, ("Leonardo", 41, "Chef"))

print(employees)

# 6. Gib nun die neusten Mitarbeiter aus (die letzten 2)

print("""
---TASK-6---""")

print(employees[-2:])