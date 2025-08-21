'''
1. Start with atleast 2 letters
2. max char = 6 and min char = 2 both included and must be alphanumeric
3. first number != 0 and numbers cant be used in middle
4. no spl char
5. I/P --> caps only (assumption)
6. O/P --> valid or invalid
'''
def main():
    plate = input("Plate: ") #5
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s[0:2].isalpha(): #1
        return False

    if not 2 <= len(s) <= 6: #2
        return False

    if not(s.isalnum()):
        return False

    for i in range(len(s)): #3
        element = s[i]

        if element.isdigit():

            if element == "0":
                return False

            if not s[i:].isdigit():
                return False

            break

    return True

main()
