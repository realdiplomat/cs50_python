

x = input("Input: ")
vowels = "aeiouAEIOU"
print("Output: ", end="")

for letter in x:
    if letter not in vowels:
        print(letter, end="")
print()


