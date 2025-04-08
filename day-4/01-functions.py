# def = define also definiere 
# keyword um eine funktion zu definieren
def addition(a, b, c):
    return a + b + c

print(addition(2, 3, 6))

# Wenn eine Variable unbekannt viele Parameter annehmen soll, geht das so
# in JS machen wir das elbe mit dem rest operator, die sogenanten args
# (...values)
def calc_sum(*numbers):
    print(sum(numbers))

calc_sum(20, 5, 30, 45)
calc_sum(5, 45)

# Das 1. Sternchen bedeutet das beliebigviele Argumente werden übergeben (args)
# Das 2. Sterchen steht für mehrere Daten. Achtung hier kommen Daten mit einer Zuweisung!
# key = value
# Die Ausgabe ist ein Dictionary (Object)
def create_dict(**daten):
    print(daten)

create_dict(name= "Max", age=33, hobbys = ["Programmieren", "Schwimmen"])

# In Python dürfen Funktionen nie leer sein, also der Funktionskörper muss Inhalt haben.
# Leerstehende Funktionen, die noch nicht gecoded sind können aber das Keyword "pass" bekommen

def new_func():
    pass

# pass verhidnert, dass es zu einer Fehlermeldung kommt und wir könenn unsere Proejktstruktur breits aufbauen ohne überein einen print in die funktion schrieben zu müssen.

# Es gibt verschiedene Arten zu Kommentieren, die einzeiligen Kommentare geschehen mit dem "#"
# Mehrzeilige Kommentare erstellem man mit """ """ oder ''' '''
# Diese Kommentarart nennt sich DOCSTRINGS
# VORTEIL: Beim hovern über die Funktion, siehst du den Kommentar als Beschreibung, was in der jeweiligen Funktion geschieht.
def example_func():
    """
    Das ist die Standardbescheibung: (function) def example_func() -> None

    Aber wir wollen nun erzählen, dass es in dieser Funktion um folgendes geht...
    """
    pass

def add_user(user):
    """
    add_user(user: Type Obj) -> User from Frontend!

    In dieser Funktion wird überprüft, ob der User, der sich gerade versucht zu registrieren
    bereits in der Datenbank hinterlegt ist.

        -> success: der user wird in der DB gespreichert

        -> fail: an das Frontend wird eine Meldung gegeben, dass der username bereits vergeben ist
    """
    pass