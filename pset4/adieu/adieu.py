import inflect
p = inflect.engine()

names_L = []
while True:
    try:
        Input = input("Name: ")
        names_L.append(Input)
        names_T = tuple(names_L)
    except EOFError:
        break


print()
print("Adieu, adieu, to", p.join(names_T), "\n")

