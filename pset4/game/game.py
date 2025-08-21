from random import randint

#strings not allowed!
#If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#If the guess is the same as that integer, the program should output Just right! and exit.

#Level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        elif level <= 0:
            continue
    except ValueError:
            pass

#Random
number = randint(1,level)

#Guess
while True:
    try:
        guess = int(input("Guess: "))
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass

