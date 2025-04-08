# Errorhandling

status = True

num1 = 10
num2 = 0
num3 = "2"

try:
    if status:
        sum = num1 / num2
    else:
        sum = num1 / num3
    
    print(sum)

# Name der Fehlermelung x / 0
except ZeroDivisionError:
    print("Du darfst nicht duirch 0 dividieren!")

# Name der Fehlermelung x / String
except TypeError:
    print("Du kannst nur mit Zahlen rechnen!")

# Alle Fehlermeldungen
except:
    print("Ups da ist was schief gelaufen!")
finally:
    print("Fertig!")

print("""
Error Raising (throw)""")

x = 10

if x >=10:
    raise Exception("Sorry x darf nicht größer oder gleich 10 sein!")