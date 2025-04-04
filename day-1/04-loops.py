i = 0

while i < 10:
    print(i)
    i += 1

print("------FOR-STRING------")

name = "Mustermann"

print("index 0: ", name[0])
print("index 6-end", name[6:])

for element in name:
    print("char from Name: ", element)

print("------FOR-ARRAY------")

first_list = [1, 2, 3, 4, 5]
print("index 0: ", first_list[0])
print("index 2-end", first_list[2:])

for element in first_list:
    print("arrItem", element)

print("------FOR-OBJECT------")

first_obj = {"a": 1, "b": 2, "c": 3}

for element in first_obj:
    print("objElem", element)

print("------FOR-ZÄHLER------")

# range() erzeugt iterierbares Objekt 0-5 (exklusiv)
for element in range(5):
    print("count", element)

print("""
range(1, 5)""")

# 1-5 (exklusiv)
for element in range(1, 5):
    print("count", element)

print("""
range(1, 5, 2)""")

# 1-5 Schrittweite 2 (1, 3)
for element in range(1, 5, 2):
    print("count", element)