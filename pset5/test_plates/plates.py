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
    if is_valid(plate): #6
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if 2 <= len(s) <= 6: #2

        if s.isalpha():
            return True

        elif s.isalnum() and s[0:2].isalpha(): #1,2,4
            for element in s:
                if element.isdigit():
                    Index = s.index(element)

                    if s[Index:].isdigit() and int(element) != 0: #3
                        return True

                    else:
                        return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()



