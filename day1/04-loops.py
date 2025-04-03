i = 0

while i < 10:
    print(i)
    i += 1

print("------FOR-STRING------")

name = "Max"

for element in name:
    print("char from Name: ", element)

print("------FOR-ARRAY------")

first_list = [1, 2, 3, 4, 5]
print("index 0: ", first_list[0])

for element in first_list:
    print("arrItem", element)

print("------FOR-OBJECT------")

first_obj = {"a": 1, "b": 2, "c": 3}

for element in first_obj:
    print("objElem", element)

print("------FOR-ZÄHLER------")

# range() erzeugt iterierbares Objekt 0-9 (exklusive)
for element in range(10):
    print("count", element)

# 1-9 
for element in range(1, 10):
    print("count", element)

# 1-9 Schrittweite 2 (1, 3, 5, 7, 9)
for element in range(1, 10, 2):
    print("count", element)