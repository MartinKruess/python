# Input: Martin 35
# Output: M40-02468

name = input("Gib deinen Namen ein: ")
age = int(input("Gib dein Alter an: "))

def greet_user(user):
    print("Hallo", user)

greet_user(name)

def name_converter(age, name):
    num = age +5
    if num < 30:
        print("Du bist {age} Jahr jung!")
    else:
        print("Du bist {age} Jahr alt!")
    
    return name[0] + str(num)

converted_name = name_converter(age, name)

print(converted_name)

converted_name += "-"

for element in range(0, 10, 2):
    converted_name += str(element)

print(converted_name)
