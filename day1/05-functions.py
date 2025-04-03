# print(), input(), type(), int()... sind sogenannte build-in Functions
# build-in Functions sind Funktionen die bereits hinterlegt sind

print("------Simple-Function------")

# def = definition
def greeting():
    print("Hallo World!")

greeting()

print("------Function-Parameter------")

def greeting_by_name(name):
    print("Hallo", name)

greeting_by_name("Max")

print("------Function-ohne-return------")

def greet_lisa(name):
    print("Hallo", name)

# None statt undefined!
# None hat den Datentypen NoneType
print(greet_lisa("Lisa"))

print("------Function-mit-return------")

def greet_by_fullname(first_name, last_name):
    return first_name + " " + last_name

greet_by_fullname = greet_by_fullname("Susi", "Sorglos")
print(greet_by_fullname)