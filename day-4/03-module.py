# Die Grundlage von Mopdulen kennst du bereits aus JS, allerdings zählen importierte Funtkionen ebenfalls als Module zum Beispiel random()

# Importiere die ganze Datei mit allen Functions
import modules.greeting

# Importiere gezielt eine Function
from modules.calc_rest import calc_rest

greet = modules.greeting.greeting("Max")
print(greet)

sum = calc_rest(1440, 1220)
print(str(sum) + "€")

print("""
------Weitere Module------""")

# wie Math.random()
import random
random(1, 10)

# wie Math in JS
import math
math.sqrt(16)
# Alternativ kann man auch jede benötigte Funktion einzeln importieren
# from math import sqrt

import os
# console.clear()
os.system("cls")

"""
LISTE MIT WEITEREN IMPORTS, DIE MAN MAL BRAUCHEN KANN!

🧰 Allgemeine Helfer
Modul	Zweck
time	Zeitmessung, Sleep
datetime	Datums- und Zeitfunktionen
re	Reguläre Ausdrücke
typing	Typ-Hinweise wie List, Dict, Tuple, Literal

📂 Dateiverwaltung
shutil	Dateien/Ordner kopieren, verschieben, löschen
pathlib	Modernes Pfad-Handling (Alternative zu os.path)
glob	Dateisuche mit Wildcards (z. B. *.txt)
csv	CSV-Dateien lesen und schreiben
json	JSON-Dateien lesen und schreiben
pickle	Python-Objekte speichern/laden (serialisieren)

📡 Netzwerk & Internet
urllib	URLs öffnen, Daten abrufen
http.client	HTTP-Verbindungen
socket	Low-Level-Netzwerkkommunikation

🧪 Entwicklung & Test
unittest	Tests schreiben und ausführen
logging	Logging statt print()
traceback	Fehler- und Stack-Analyse
inspect	Infos über Funktionen, Klassen etc. abrufen

🔐 Sicherheit & Hashes
hashlib	Hashes wie MD5, SHA-1, SHA-256
secrets	Sichere Zufallszahlen (für Passwörter, Tokens)
"""
