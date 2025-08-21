grocery = {}

while True:
    try:
        item = input("").upper()

        if item in grocery:
           grocery[item] = grocery[item] + 1
        else:
           grocery[item] = 1

    except EOFError:
        break

for item in sorted(grocery.keys()):
    print(grocery[item], item)



