num1 = input("Zahl 1: ")
num2 = input("Zahl 2: ")

# Wir checken den Type von num1
type_of_num1 = type(num1)
print(type_of_num1, num1 + num2)

print("-------------")

# input() liefert einen String
# convert string to int
num3 = int(input("Ganzzahl 3: "))
num4 = int(input("Ganzzahl 4: "))
type_of_num3 = type(num3)
print(type_of_num3, num3 + num4)

print("-------------")

# convert string to float
num5 = float(input("Float 3: "))
num6 = float(input("Float 4: "))
type_of_num5 = type(num5)
print(type_of_num5, num5 + num6)