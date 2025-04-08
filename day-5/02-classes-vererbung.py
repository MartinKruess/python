class Animal:
    # Klassenvariablen
    # sollen konstant sein, daher groß schreiben!
    cute = True
    

    def __init__(self, breed, sex, age):
        self.breed = breed
        self.sex = sex
        self.age = age

    def print_breed(self):
        print("Breed (Animal):", self.breed)

class Dog(Animal):
    bark = ""

    def __init__(self, bark, breed, sex, age):
        # Aufruf des Animal constructors
        # Vor Python v3 musste man die parentclass angeben
        # in v2: super(Dog, self).__init__(breed, sex, age)
        super().__init__(breed, sex, age)
        self.bark = bark

    # Kombinieren statt überschreiben!
    def print_breed(self):
        # Erbt alles aus der Funktion, der Animal Klasse
        super().print_breed()
        # Erweitert die Funktion
        print("Breed (Dog):", self.breed)
    


dog1 = Dog("wuff wuff", "Dackel", "male", 3)

print(dog1.bark)
dog1.print_breed()

"""
Das 'super' Keyword

!bezieht sich bei der einfachen vererbung auf die Parentklasse

super().__init__() -> Parentklasse.___init__(die Parameter)

super().my_function() -> Parentklasse.my_function()

Wir rufen also mit dem super Keyword, manuel die einzelnen Teile der parent class auf und übergeben die eingebenen Werte an die parent class
"""