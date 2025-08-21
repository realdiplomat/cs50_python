from tabulate import tabulate
import sys

def main():
    menu_plate()

# MENU PLATE
def menu_plate():

    print()
    print("Simple Calculator")
    print()

    operandi = [
        ["Choice", "Operation"],
        [1, "Addition"],
        [2, "Subtration"],
        [3, "Multiplication"],
        [4, "Division"],
        [5, "Average"],
        [6, "Exit"]
        ]

    print(tabulate(operandi, headers = "firstrow", tablefmt="psql"))
    print()


    choice = int(input("Select your choice: "))

    # LOOP THE CHOICES
    while True:

        if choice not in [1,2,3,4,5,6]:

            print("Enter valid choice!")
            choice = int(input("Select your choice: "))
            continue

        if choice in [1,2,3,4,5,6]:

            if choice == 1:
                print("Choice 1 has been used...")
                print()
                print(addition(get_num()))
                break

            elif choice == 2:
                print("Choice 2 has been used...")
                print("NOTE: Succeeding to be subtracted")
                print()
                print(subtraction(get_num()))
                break

            elif choice == 3:
                print("Choice 3 has been used...")
                print()
                print(multiplication(get_num()))
                break

            elif choice == 4:
                print("Choice 4 has been used...")
                print()
                print(division(get_num()))
                break

            elif choice == 5:
                print("Choice 5 has been used...")
                print()
                print(average(get_num()))
                break

            elif choice == 6:
                sys.exit("Exiting the program...")

# GET NUMBERS
def get_num():
    numbers = []

    while True:
        try:
            num_input = input("Enter a number or press S to stop taking numbers: ").strip()
            print()
            if num_input.upper() == 'S':
                break

            num = float(num_input)
            numbers.append(num)

        except ValueError:
            print("Invalid input. Enter a number or press S to stop!")
            continue

    return numbers

def addition(num_add):
    op = 0
    if num_add:
        for number in num_add:
            op += number
        return f"Resultant of {num_add} = {op}"

# 1st num = result, succeeding to be subtracted
def subtraction(num_sub):
    op = num_sub[0]
    if num_sub:
        for number in num_sub[1:]:
            op -= number
        return f"Resultant of {num_sub} = {op}"

def multiplication(num_mult):
    op = 1
    if num_mult:
        for number in num_mult:
            op *= number
        return f"Resultant of {num_mult} = {op}"

# Zero division to be excepted
def division(num_div):
    try:
        if num_div:
            op = num_div[0]
            for number in num_div[1:]:
                op /= number
        return f"Resultant of {num_div} = {op}"
    except ZeroDivisionError:
        return "Number cannot be divided by zero!"

# Call addition function and divide by length
def average(num_avg):
    if num_avg:
        op = 0
        for number in num_avg:
            op += number
        return f"Resultant of {num_avg} = {op/len(num_avg)}"

if __name__ == "__main__":
    main()
