age = int(input("Wie alt bist du? "))

print("--------IF-ELIF-ELSE--------")

if age < 18:
    print("Achtung der Nutzer ist jünger als 18!")
elif age == 18:
    print("Der Nutzer ist gerade eben 18.")
else:
    print("Der Nutzer ist über 18.")

print("--------AND--------")

if age < 18 and age == 17:
    print("Der Nutzer ist jünger als 18 und ist genau 17")

print("--------OR--------")

if age == 17 or age == 18:
    print("Der Benutzer ist 17 oder 18.")

print("--------NOT--------")

fruits = ["Apfel", "Banane", "Kirsche"]

if "Orange" not in fruits:
    print("Orange ist nicht in der Liste!")
else:
    print("Orange ist in der Liste!")