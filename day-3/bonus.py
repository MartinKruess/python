# WEIRD ABER PYTHON!

"""
Konstante Variable:
Python selbst hat leider keinen Weg wie JS, dass wir eine Art 'const' Variable erstellen.
Das bedeutet wir können zu jeder Zeit jede Variable überschreiben.
Es gibt zwar eine Konvention unter Python Entwickler, dass MYNUMER nicht überschrieben werden darf, weil sie groß geschrieben ist, aber Python selbst prüft das nicht und wirft keinen Fehler, wenn die Variable plötzlich nen anderen Wert oder Datentypen hat.

Tupel:
Ein Tupel (unveränderliche Liste) ist das einzige, was ähnlich einer 'const' Variable ist, allerdings schützt eint Tupel nicht nur das Äußere, sondern auch die Daten im inneren.

Typsicherheit:
Die Typensicherhei, kann man mit extra Tools wie 'mypy' halbwegs gut gewährleisten, ebenfalls gibt es de möglichkeit, durch das Keyword 'Final' solche Variablen zu kennzeichnen.
"""

# Beispiel 1: Ob mit einer class oder durch Großschreibung, wirklich helfen tut das alles nicht...
class Car:
    def __init__(self, brand, color, ps):
        self.brand_name = brand
        self.color = color
        self.ps = ps

car1 = Car("VW", "red", 65)
CAR1 = Car("Ford", "black", 210)


print(car1)
print(CAR1)


car1 = "Mein lieblings Auto ist der VW Golf GTI!"
CAR1 = "Mein lieblings Auto ist der Ford Mustang!"

print(car1)
print(CAR1)

#Beispiel 2 mit Array

print("""
Beispiel 2 - Array""")

employees_arr = [{"name": "Susi Sorglos", "job": "Junior Frontend Developer", "salery": 37500}]

print("Array vor der Beförderung: ", employees_arr)


# Susi ist nun Senior!
employees_arr[0]["job"] = "Senio Frontend Developer"
employees_arr[0]["salery"] = 48000

print("Array nach der Beförderung: ", employees_arr)

# Beispiel 2 mit Tupel
print("""
Beispiel 2 - Tupel""")

#! Achtung: Ein Tupel ist erst ein Tupel, wenn es mindestens 1 Komma auf oberster Ebene gibt
# Auch wenn es nur ein Objekt beinhaltet, so muss nach dem Objekt das Komma stehen, sonst funktioniert der Code nicht!
employees_tupel = ({"name": "Susi Sorglos", "job": "Junior Frontend Developer", "salery": 37500},)

print("Tupel vor der Beforderung: ", employees_tupel)

employee_from_tupel = employees_tupel[0]
# Susi ist nun Senior!
employee_from_tupel["job"] = "Senio Frontend Developer"
employee_from_tupel["salery"] = 48000

print("Veränderte Kopie des Tupel: ", employee_from_tupel)