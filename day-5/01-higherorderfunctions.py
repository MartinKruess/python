# Das equivalent zu JS higher order funktions

# allgemeiner Aufbau
"""
list(methode(function, array))
[methode(function, array)]

hierbei könenn funktionen von außerhalb benutzt werden
oder die anonyme lambda funktion.
"""

print("""
------MAP------""")

users = [
    {"fullname": "Lisa Lustig"},
    {"fullname": "Susi Sorglos"},
    {"fullname": "Peter Pampig"}
]

def add_city(user):
    user["city"] = "Hamburg"
    return user

# 1,. mape über users
# 2. verändere jeden user mit der add_city()
# 3. Wenn map durch ist erzeuge ein neues Array aus dem Ergebnis
updated_users = list(map(add_city, users))

print(updated_users)

# für kleinere Aufgabe wie das Berechnen von Zahlen
# oder anderen Anweisungen ohne Zuweisung (=)
# wird in Python gerne die `lambda` Funktion verwendet.
# lambda ist eine anonyme Funktion,
# die einzeiliges Arbeiten erleichtert

list_of_names = list(map(lambda user: user["fullname"], users))

print(list_of_names)

print("""
------FILTER------""")

def filter_options(user):
    if "s" in user["fullname"]:
        return user

filtered_users = list(filter(filter_options, users))

# lambda alternative
filtered_users2 = list(filter(lambda user: "s" in user["fullname"], users))


print(filtered_users)
print(filtered_users2)

print("""
------FIND------""")

names = ["Lisa", "Susi", "Max", "Paul"]

searched_in_string = "Paul" in "Paulo"

print(searched_in_string)

# eine Art find
# x wird definiert dann for-in x in y und ein if ranhängen
# next((x for x in users if user["key"] ==value), None)
searched_user = next((user for user in users if user["fullname"] == "Lisa Lustig"), None)

print(searched_user)

print("""
------REDUCE------""")

from functools import reduce

nums = [1, 2, 3 , 4 , 5]

average = reduce(lambda acc, x:( acc + x), nums) / len(nums)

print(average)

print("""
------SORT------""")

nums_out_of_oder = [1, 3, 2, 7, 5, 6]

# simple
ordered_nums = sorted(nums_out_of_oder)

print(ordered_nums)


str_out_of_order = [ "Malte", "Beate", "Adam", "Gustaf", "Dörte", "Björn"]

ordered_str = sorted(str_out_of_order)

print(ordered_str)