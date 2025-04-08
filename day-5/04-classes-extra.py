# Decorators - setter & deleter

class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # Setter bezogen auf First- und Lastname
    # Aktualisiert beide Properties bei der Aktualisieurng von Fullname
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

    @property
    def email(self):
        return '{}.{}@mail.com'.format(self.first, self.last)
    
    @email.deleter
    def email(self):
        print("E-Mail wurde gelsöcht!")

student_1 = Student("Lisa", "Sorglos")

student_1.fullname = "Max Mustermann"

print("Firstname:", student_1.first)
print("Lastname:", student_1.last)
print("Fullname:", student_1.fullname)
print("E-Mail:", student_1.email)

del student_1.email
