# class: wir arbeiten also mit typischen Klassen
# Auf bau einer Speziellen Funktion namens init
# def __init__ entspricht unserem construtor()
# self entspricht unserem this ;)

class Car:
    def __init__(self, brand, ps, color):
        self.car_brand = brand
        self.ps = ps
        self.color = color

# Wir verzichten beim Erzeugen einer neuen Instanz (Objekt) in Python auf das "new" Keyword!
# Zuweisungen passieren hier in einzelnen Zeilen statt als Parameter
car1 = Car("VW", 65, "red")
print("komische Ausagbe", car1)
print("car_brand", car1.car_brand)
print("ps", car1.ps)
print("color", car1.color)

print("------------")

car2 = Car("Ford", 210, "black")
print("car_brand", car2.car_brand)
print("ps", car2.ps)
print("color", car2.color)

print("""
      ------METHODS-IN-CLASSES------
""")

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greet(self, greeting):
        return greeting + " " + self.first_name

user1 = User("Lisa", "Lustig", 32)
print(user1.greet("Hi"))