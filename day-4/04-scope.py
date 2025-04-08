def func():
    inner_func = "Inner Funk 1"

print("""
------FUNCTION-TEST------""")

try:
    print(func(), inner_func)
except:
    print("eine Function hat einen Scope!")

print("""
------IF-TEST------""")

a = 1

if a < 2:
    inner_first_if = "Inner first If"
elif a == 2:
    inner_first_elif = "Inner first elif"
else:
    inner_first_else = "Inner first else"

try:
    if a < 2:
        print("in if 2:", inner_first_if)
    
    if a == 2:
        print("in if 2:", inner_first_elif)
    
    if a > 2:
        print("in if 2:", inner_first_else)

    inner_try = "Inner Try"

    print("If hat also keinen Scope...")

except:
    print("ein if/elif/else hat einen Scope!")

print("""
------TRY-TEST------""")

print("on top_level:", inner_try)

print("""
------FAZIT------""")

print("Das einzige mit einem Scope ist eine Funktion und das wahrscheinlich auch nur, da diese zuvor aufgerufen werden muss und da Varibale ohne Aufruf überhaupt nicht existier...")