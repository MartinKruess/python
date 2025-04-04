# Variablen

text = "Hallo World!"

print("first", text[0])
print("last", text[-1])

# Slice
print("------SLICE------")

print("slice 6:-1", text[6:])
print("slice 0:x", text[:5])
print("slice x:-y", text[6:-1])
print("slice x:y", text[6:11])

print("------Length------")

print("length", len(text))

print("------String Methods------")

print("Hallo" * 3)

text2 = "Guten Morgen, ich lerne Python"

print("uppercase:",text2.upper())
print("lowercase:",text2.lower())
print("capitalize:",text2.capitalize())

print("split:",text2.split())
print("split by o:",text2.split("o"))
print("split by ,:",text2.split(","))

text3 = "Papa ich lerne Python im privatunterricht!"

print("find start index",text3.find("Python"))

# text3[15: 15 + 6]
# starte bei "P" von Python (15) : ende bei "P" von Python (15) + die lenge von Python (length = 6)
# indexP : indexP + worldLength (15 : 15 + 6)
print(text3[text3.find("Python") : text3.find("Python") + len("Python")])