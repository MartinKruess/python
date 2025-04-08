# @property -> getter

print("""
------LÖSUNG-1------""")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Wird einmal erstellt und ist nicht wieder Änderbar
        self.descr = name + " is " + str(age) + " years old."

    def speak(self):
        return self.name + " is barking"
    
    # Lösung 1
    def description(self):
        return self.name + " is " + str(self.age) + " years old."
    
dog_1 = Dog("Bello", 5)

# Bello hat Geburtstag und ist nun 6 Jahre alt! 🎂
dog_1.age = 6

print("Name:", dog_1.name)
print("Descr:", dog_1.descr)
print("Description Function:", dog_1.description())
print("Speak Function:", dog_1.speak())

print("""
------BESSERE-LÖSUNG------""")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return self.name + " is mauzing."
    
    # Lösung 2
    @property
    def description(self):
        return self.name + " is " + str(self.age) + " years old."
    
cat_1 = Cat("Hektropascal", 7)

# Hektopascal hat Geburtstag und ist nun 8 Jahre alt! 🎂
cat_1.age = 8

print("Name:", cat_1.name)
print("Description as Property:", cat_1.description)
print("Speak Function:", cat_1.speak())