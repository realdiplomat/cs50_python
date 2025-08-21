# to assume input will be titlecased
# ctrl+d to end user input

ft_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

total = 0 #flag

while True:
    try:
        items = input("Item: ").title()

        if items in ft_menu:
            total = total + ft_menu[items]
            print(f"Total: ${total:.2f}")

    except EOFError:
        break




