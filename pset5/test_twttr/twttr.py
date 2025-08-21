#MISTAKE: only main should print the function
#MISTAKE: return value must be INT not string



def main():
    x = input("Input: ")
    print("Output:", shorten(x))

def shorten(word):

    vowels = "aeiouAEIOU"

    for letter in word:
        if letter in vowels:
            word = word.replace(letter, "")
    return word

if __name__ == "__main__":
    main()
