from random import randint

test_num = randint(1, 100)
print("test_num", test_num)

num = randint(1, 100)

# Guess the Number
while True:

    inputNum = int(input("Zahl von 1-100: "))

    if num < inputNum:
        print("Die Zahl ist kleiner!")
    elif num == inputNum:
        print("Glückwunsch, du hast richtig geraten!")
        break
    else:
        print("Die Zahl ist größer!")